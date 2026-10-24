#!/usr/bin/env python3
"""Check Kritva Actuator Markdown documents for the mandatory header and revision history.

Copyright (c) 2026 Kritvaos. Licensed under the Apache License, Version 2.0 (see LICENSE).

Scope
-----
Every ``.md`` file under the controlled document directories (requirements/,
planning/, docs/, mechanical/, embedded/, audit/) is inspected.

A file is treated as a controlled KA- document when the first Markdown table
in the file contains a ``Document ID`` row. For such documents the script
checks (ERROR unless stated otherwise):

  * header fields present: Document ID, Repository, Revision, Date,
    Document owner, an approver field (``Reviewer / Approver``, ``Approver``
    or ``Reviewer``) and Classification; ``Applies to`` missing is a WARNING;
  * Document ID format ``KA-<AREA>-<NAME>`` (upper case, digits, hyphens);
  * Document IDs unique across the repository;
  * Revision starts with a number such as ``0.1``;
  * Date is ISO ``YYYY-MM-DD``;
  * a ``Revision history`` heading followed by a table;
  * WARNING when the last revision-history row does not match the header
    revision, when no status note is found near the top, when the
    classification does not say "Public", or when emoji characters are
    present (the documentation standard forbids them).

Files without a ``Document ID`` header:

  * ``README.md`` files are folder guides and are skipped (reported as INFO
    with ``--verbose``);
  * any other file gets a WARNING (an ERROR with ``--strict``).

Missing directories produce a WARNING, not a crash: the repository is
populated incrementally.

Exit status: 0 when there are no errors (warnings allowed), 1 when there are
errors, or when there are warnings and ``--strict`` is given. 2 on usage error.

Standard library only. Python 3.8+.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

DEFAULT_DIRS = [
    "requirements",
    "planning",
    "docs",
    "mechanical",
    "embedded",          # submodule kritva-actuator-embedded (when checked out)
    "audit",
]

REQUIRED_FIELDS = [
    "Document ID",
    "Repository",
    "Revision",
    "Date",
    "Document owner",
    "Classification",
]
APPROVER_FIELDS = ["Reviewer / Approver", "Reviewer/Approver", "Approver", "Reviewer"]
RECOMMENDED_FIELDS = ["Applies to"]

DOC_ID_RE = re.compile(r"^KA-[A-Z0-9]+(?:-[A-Z0-9]+)*$")
REVISION_RE = re.compile(r"^(\d+(?:\.\d+)*)")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
REV_HIST_HEADING_RE = re.compile(
    r"^#{1,6}\s+(?:\d+(?:\.\d+)*\.?\s+)?revision history\s*$", re.IGNORECASE
)
FENCE_RE = re.compile(r"^\s*(```|~~~)")
# Common emoji blocks (pictographs, symbols, dingbats, flags, variation selector).
EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U0001F1E6-\U0001F1FF☀-⛿✀-➿️]"
)
SKIP_DIR_NAMES = {".git", "node_modules", "build", "__pycache__", ".venv", "venv"}


class Report:
    """Collects findings and prints them in a stable format."""

    def __init__(self, verbose: bool = False) -> None:
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.infos: List[str] = []
        self.verbose = verbose

    def error(self, where: str, msg: str) -> None:
        self.errors.append(f"ERROR   {where}: {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"WARNING {where}: {msg}")

    def info(self, where: str, msg: str) -> None:
        self.infos.append(f"INFO    {where}: {msg}")

    def emit(self) -> None:
        if self.verbose:
            for line in self.infos:
                print(line)
        for line in self.warnings:
            print(line)
        for line in self.errors:
            print(line)


def strip_md(value: str) -> str:
    """Remove simple Markdown emphasis/code markers around a table cell value."""
    v = value.strip()
    for marker in ("**", "__", "`", "*", "_"):
        if v.startswith(marker) and v.endswith(marker) and len(v) >= 2 * len(marker):
            v = v[len(marker) : -len(marker)].strip()
    return v


def split_row(line: str) -> List[str]:
    """Split a Markdown table row into cells (handles escaped pipes)."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    cells = re.split(r"(?<!\\)\|", s)
    return [c.strip().replace("\\|", "|") for c in cells]


def is_separator_row(cells: List[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{2,}:?", c.replace(" ", "")) for c in cells if c)


def non_code_lines(lines: List[str]) -> List[Tuple[int, str]]:
    """Return (line_number, text) for lines outside fenced code blocks."""
    out: List[Tuple[int, str]] = []
    in_fence = False
    for i, line in enumerate(lines, start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append((i, line))
    return out


def first_table(lines: List[Tuple[int, str]]) -> Optional[List[List[str]]]:
    """Return the rows (as cell lists, separator removed) of the first table."""
    rows: List[List[str]] = []
    started = False
    for _, line in lines:
        if line.lstrip().startswith("|"):
            started = True
            cells = split_row(line)
            if not is_separator_row(cells):
                rows.append(cells)
        elif started:
            break
    return rows if rows else None


def table_after(lines: List[Tuple[int, str]], start_index: int) -> Optional[List[List[str]]]:
    """Return the first table that starts after position ``start_index`` and
    before the next heading."""
    rows: List[List[str]] = []
    started = False
    for _, line in lines[start_index + 1 :]:
        stripped = line.strip()
        if not started and stripped.startswith("#"):
            return None
        if stripped.startswith("|"):
            started = True
            cells = split_row(stripped)
            if not is_separator_row(cells):
                rows.append(cells)
        elif started:
            break
    return rows if rows else None


def check_file(path: Path, root: Path, report: Report, strict: bool,
               seen_ids: Dict[str, str]) -> None:
    rel = path.relative_to(root).as_posix()
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        report.error(rel, "file is not valid UTF-8")
        return
    except OSError as exc:
        report.error(rel, f"cannot read file ({exc})")
        return

    raw_lines = text.splitlines()
    lines = non_code_lines(raw_lines)
    table = first_table(lines)

    header: Dict[str, str] = {}
    if table:
        for cells in table:
            if len(cells) >= 2:
                header[strip_md(cells[0])] = strip_md(cells[1])

    if "Document ID" not in header:
        if path.name.lower() == "readme.md":
            report.info(rel, "folder README without KA- header (allowed)")
        elif strict:
            report.error(rel, "no 'Document ID' header table (controlled documents must start "
                              "with the KA- header table; see CONTRIBUTING.md section 6)")
        else:
            report.warn(rel, "no 'Document ID' header table; add the KA- header if this is a "
                             "controlled document")
        return

    # --- header fields -----------------------------------------------------
    for field in REQUIRED_FIELDS:
        if not header.get(field):
            report.error(rel, f"header field '{field}' missing or empty")
    if not any(header.get(f) for f in APPROVER_FIELDS):
        report.error(rel, "header has no approver field ('Reviewer / Approver', 'Approver' or "
                          "'Reviewer')")
    for field in RECOMMENDED_FIELDS:
        if not header.get(field):
            report.warn(rel, f"header field '{field}' missing (recommended)")

    doc_id = header.get("Document ID", "")
    if doc_id:
        if not DOC_ID_RE.match(doc_id):
            report.error(rel, f"Document ID '{doc_id}' does not match KA-<AREA>-<NAME> "
                              "(upper case letters, digits and hyphens)")
        if doc_id in seen_ids:
            report.error(rel, f"Document ID '{doc_id}' already used by {seen_ids[doc_id]}")
        else:
            seen_ids[doc_id] = rel

    header_rev: Optional[str] = None
    revision = header.get("Revision", "")
    if revision:
        m = REVISION_RE.match(revision)
        if not m:
            report.error(rel, f"Revision '{revision}' must start with a number such as 0.1")
        else:
            header_rev = m.group(1)

    date = header.get("Date", "")
    if date and not DATE_RE.match(date):
        report.error(rel, f"Date '{date}' is not ISO YYYY-MM-DD")

    classification = header.get("Classification", "")
    if classification and "public" not in classification.lower():
        report.warn(rel, f"Classification '{classification}' does not state 'Public'")

    # --- status note --------------------------------------------------------
    head_text = "\n".join(raw_lines[:60]).lower()
    if "status note" not in head_text and "pending approval" not in head_text:
        report.warn(rel, "no status note ('proposed targets pending approval ...') found near "
                         "the top of the document")

    # --- revision history ---------------------------------------------------
    rh_index = None
    for idx, (_, line) in enumerate(lines):
        if REV_HIST_HEADING_RE.match(line.strip()):
            rh_index = idx
    if rh_index is None:
        report.error(rel, "missing 'Revision history' section (heading + table)")
    else:
        rh_table = table_after(lines, rh_index)
        if not rh_table or len(rh_table) < 2:
            report.error(rel, "'Revision history' heading is not followed by a table with at "
                              "least one entry")
        else:
            head = [c.lower() for c in rh_table[0]]
            if not any(h.startswith("rev") for h in head) or "date" not in head:
                report.warn(rel, "revision history table should have 'Rev' and 'Date' columns")
            last = rh_table[-1]
            last_rev = strip_md(last[0]) if last else ""
            if header_rev and last_rev and REVISION_RE.match(last_rev):
                if REVISION_RE.match(last_rev).group(1) != header_rev:
                    report.warn(rel, f"header Revision {header_rev} differs from last revision "
                                     f"history entry {last_rev}")

    # --- emoji --------------------------------------------------------------
    for lineno, line in lines:
        if EMOJI_RE.search(line):
            report.warn(f"{rel}:{lineno}", "emoji character found (not permitted in documents)")
            break


def iter_markdown(directory: Path):
    for path in sorted(directory.rglob("*.md")):
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        if path.is_file():
            yield path


def default_root() -> Path:
    return Path(__file__).resolve().parents[2]


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check KA- document headers and revision history tables.")
    parser.add_argument("--root", type=Path, default=default_root(),
                        help="repository root (default: two levels above this script)")
    parser.add_argument("--dirs", nargs="+", default=DEFAULT_DIRS,
                        help="directories to scan, relative to the root")
    parser.add_argument("--strict", action="store_true",
                        help="treat warnings as errors")
    parser.add_argument("-v", "--verbose", action="store_true", help="print INFO lines")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    if not root.is_dir():
        print(f"ERROR   repository root '{root}' does not exist")
        return 2

    report = Report(verbose=args.verbose)
    seen_ids: Dict[str, str] = {}
    count = 0
    controlled = 0
    for d in args.dirs:
        directory = root / d
        if not directory.is_dir():
            if d != "embedded":      # submodule; absent until checked out
                report.warn(d + "/", "directory not present yet; skipped")
            continue
        for path in iter_markdown(directory):
            count += 1
            before = len(seen_ids)
            check_file(path, root, report, args.strict, seen_ids)
            if len(seen_ids) > before:
                controlled += 1

    report.emit()
    print(f"check_docs: scanned {count} Markdown file(s), {controlled} controlled KA- "
          f"document(s); {len(report.errors)} error(s), {len(report.warnings)} warning(s).")
    if count == 0:
        print("check_docs: no Markdown files found in the scanned directories (nothing to check).")
    if report.errors or (args.strict and report.warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
