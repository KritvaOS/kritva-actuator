#!/usr/bin/env python3
"""Validate the Kritva Actuator requirements traceability matrix.

Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved.

Inputs
------
* ``audit/requirements_traceability/REQUIREMENTS_TRACEABILITY.csv``
  (the canonical traceability matrix, SYS-REQ-102);
* every ``requirements/*.md`` document (the canonical requirement sources).

CSV schema (exact column order, UTF-8, comma separated, one header row)::

    requirement_id,source_document,requirement_summary,parent_ids,owner,phase,
    verification_method,verification_procedure,evidence_location,
    verification_status,audit_document,audit_status,last_updated,notes

Checks (ERROR unless stated otherwise)
--------------------------------------
CSV structure
  * header matches the schema exactly (names and order);
  * every row has exactly 14 fields;
  * ``requirement_id`` present, well formed (``SYS|ACT|MECH|ELEC|FW|CTRL|IF|SAF-REQ-NNN``)
    and unique;
  * ``verification_status`` and ``audit_status`` in
    {NOT_STARTED, IN_PROGRESS, PASS, PASS_WITH_ACTIONS, FAIL, NOT_VERIFIED};
  * ``requirement_summary``, ``source_document``, ``owner``, ``phase`` and
    ``verification_method`` not empty;
  * ``phase`` uses A0/A1/A2 tokens (e.g. ``A1``, ``A0/A1``, ``A0-A2``);
  * ``verification_method`` uses T/A/I/D letters (e.g. ``T``, ``A, T``);
  * ``last_updated`` is ISO ``YYYY-MM-DD``;
  * a ``PASS`` or ``PASS_WITH_ACTIONS`` verification status requires
    ``evidence_location`` (evidence, not documentation, closes a requirement);
  * an audit status other than NOT_STARTED requires ``audit_document``;
  * ``FAIL`` or ``PASS_WITH_ACTIONS`` should explain itself in ``notes`` (WARNING);
  * child requirements (not SYS-REQ) must list ``parent_ids``; every parent ID
    must exist in the CSV or in requirements/*.md;
  * WARNING if ``source_document`` does not exist, or differs from the file
    in which the requirement is actually defined.

Coverage against requirements/*.md
  * every requirement ID **defined** in requirements/*.md (first cell of a
    table row, or the start of a heading) appears in the CSV (ERROR);
  * an ID defined in two places is an ERROR (IDs are unique, never reused);
  * a CSV ID that is not defined in any requirements document is a WARNING
    (deleted requirements must be kept and marked, never reused);
  * IDs referenced in requirements/*.md but defined nowhere are WARNINGS;
  * WARNING if a prefix is defined outside its owning document or outside its
    allocated number range.

Missing files are reported as WARNINGS so that the script can run while the
baseline is still being written.

Exit status: 0 = no errors; 1 = errors (or warnings with ``--strict``); 2 = usage.

Standard library only. Python 3.8+.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

SCHEMA = [
    "requirement_id",
    "source_document",
    "requirement_summary",
    "parent_ids",
    "owner",
    "phase",
    "verification_method",
    "verification_procedure",
    "evidence_location",
    "verification_status",
    "audit_document",
    "audit_status",
    "last_updated",
    "notes",
]
STATUS_VALUES = {"NOT_STARTED", "IN_PROGRESS", "PASS", "PASS_WITH_ACTIONS", "FAIL", "NOT_VERIFIED"}
DEFAULT_CSV = "audit/requirements_traceability/REQUIREMENTS_TRACEABILITY.csv"

ID_PATTERN = r"(?:SYS|ACT|MECH|ELEC|FW|CTRL|IF|SAF)-REQ-\d{3}"
ID_RE = re.compile(rf"^{ID_PATTERN}$")
ID_FIND_RE = re.compile(rf"\b{ID_PATTERN}\b")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PHASE_TOKEN_RE = re.compile(r"A[0-2]")
PHASE_BAD_TOKEN_RE = re.compile(r"\bA[3-9]\b")
METHOD_RE = re.compile(r"^[TAID](?:\s*[,/ ]\s*[TAID])*$")
GATE_STATUSES = {"PASS", "PASS_WITH_ACTIONS", "FAIL"}
PLACEHOLDER_RE = re.compile(r"\b(TBD|TBC|TODO|placeholder)\b", re.IGNORECASE)
GENERIC_PROCEDURES = {"docs/validation/VALIDATION_PLAN.md", "docs/validation"}
TEST_ID_RE = re.compile(r"\b(BU|MC|GB|MI|PC|FI|CT|CAN|INT|DU|C)-?\d{1,2}\b|#|§|\b[A-Z]{2,5}-\d{2,3}\b")
FENCE_RE = re.compile(r"^\s*(```|~~~)")

# Owning document and allowed number range per prefix (baseline brief section 6).
PREFIX_RULES: Dict[str, Tuple[str, int, int]] = {
    "SYS": ("SYSTEM_REQUIREMENTS.md", 1, 999),
    "ACT": ("ACTUATOR_SPECIFICATION.md", 1, 99),
    "MECH": ("MECHANICAL_REQUIREMENTS.md", 1, 199),
    "ELEC": ("ELECTRICAL_REQUIREMENTS.md", 1, 199),
    "FW": ("FIRMWARE_REQUIREMENTS.md", 1, 199),
    "CTRL": ("FIRMWARE_REQUIREMENTS.md", 1, 199),
    "IF": ("INTERFACE_REQUIREMENTS.md", 1, 199),
    "SAF": ("SAFETY_REQUIREMENTS.md", 1, 199),
}


class Report:
    def __init__(self) -> None:
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def error(self, where: str, msg: str) -> None:
        self.errors.append(f"ERROR   {where}: {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"WARNING {where}: {msg}")

    def info(self, where: str, msg: str) -> None:
        print(f"INFO    {where}: {msg}")


def clean_cell(cell: str) -> str:
    c = cell.strip()
    c = re.sub(r"[*_`]", "", c)
    return c.strip()


def scan_requirements(req_dir: Path, root: Path, report: Report
                      ) -> Tuple[Dict[str, str], Dict[str, Set[str]]]:
    """Return (defined: id -> rel path, referenced: id -> set of rel paths)."""
    defined: Dict[str, str] = {}
    referenced: Dict[str, Set[str]] = {}
    if not req_dir.is_dir():
        report.warn("requirements/", "directory not present; coverage check skipped")
        return defined, referenced
    files = sorted(p for p in req_dir.glob("*.md") if p.is_file() and p.name.lower() != "readme.md")
    if not files:
        report.warn("requirements/", "no requirement documents found; coverage check skipped")
    for path in files:
        rel = path.relative_to(root).as_posix()
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeDecodeError) as exc:
            report.error(rel, f"cannot read ({exc})")
            continue
        in_fence = False
        for lineno, line in enumerate(lines, start=1):
            if FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            stripped = line.strip()
            def_id: Optional[str] = None
            if stripped.startswith("|"):
                cells = stripped.strip("|").split("|")
                first = clean_cell(cells[0]) if cells else ""
                if ID_RE.match(first):
                    # A table row only defines an ID in the prefix's owning document;
                    # elsewhere (allocation / coverage tables) it is a reference.
                    if PREFIX_RULES[first.split("-", 1)[0]][0] == path.name:
                        def_id = first
            elif stripped.startswith("#"):
                m = re.match(rf"^#+\s+({ID_PATTERN})\b", re.sub(r"[*_`]", "", stripped))
                if m:
                    def_id = m.group(1)
            if def_id:
                if def_id in defined:
                    report.error(f"{rel}:{lineno}", f"{def_id} already defined in {defined[def_id]} "
                                                    "(requirement IDs must be unique)")
                else:
                    defined[def_id] = rel
                    prefix = def_id.split("-", 1)[0]
                    owner_doc, lo, hi = PREFIX_RULES[prefix]
                    number = int(def_id.rsplit("-", 1)[1])
                    if path.name != owner_doc:
                        report.warn(f"{rel}:{lineno}", f"{def_id} defined outside its owning document "
                                                       f"requirements/{owner_doc}")
                    if not lo <= number <= hi:
                        report.warn(f"{rel}:{lineno}", f"{def_id} outside the allocated range "
                                                       f"{prefix}-REQ-{lo:03d}..{hi:03d}")
            for m in ID_FIND_RE.finditer(line):
                referenced.setdefault(m.group(0), set()).add(rel)
    return defined, referenced


def split_ids(value: str) -> List[str]:
    return [p for p in re.split(r"[;,\s]+", value.strip()) if p]


def check_csv(csv_path: Path, root: Path, report: Report) -> Optional[Dict[str, Dict[str, str]]]:
    """Validate the CSV. Return the records keyed by ID, or None when the file
    is missing or structurally unusable (coverage checks are then skipped)."""
    try:
        rel = csv_path.relative_to(root).as_posix()
    except ValueError:
        rel = str(csv_path)
    if not csv_path.is_file():
        report.warn(rel, "traceability CSV not present yet; CSV and coverage checks skipped")
        return None
    try:
        with csv_path.open(encoding="utf-8-sig", newline="") as fh:
            rows = list(csv.reader(fh))
    except (OSError, UnicodeDecodeError, csv.Error) as exc:
        report.error(rel, f"cannot parse CSV ({exc})")
        return None
    if not rows:
        report.error(rel, "file is empty (header row required)")
        return None
    header = [h.strip() for h in rows[0]]
    if header != SCHEMA:
        missing = [c for c in SCHEMA if c not in header]
        extra = [c for c in header if c not in SCHEMA]
        detail = []
        if missing:
            detail.append("missing: " + ", ".join(missing))
        if extra:
            detail.append("unexpected: " + ", ".join(extra))
        if not missing and not extra:
            detail.append("columns are in the wrong order")
        report.error(f"{rel}:1", "header does not match the schema (" + "; ".join(detail) + ")")
        report.error(f"{rel}:1", "expected: " + ",".join(SCHEMA))
        return None

    records: Dict[str, Dict[str, str]] = {}
    placeholder_rows: List[str] = []
    for lineno, raw in enumerate(rows[1:], start=2):
        if not any(c.strip() for c in raw):
            continue  # blank line
        where = f"{rel}:{lineno}"
        if len(raw) != len(SCHEMA):
            report.error(where, f"row has {len(raw)} field(s), expected {len(SCHEMA)} "
                                "(quote fields that contain commas)")
            continue
        row = {k: v.strip() for k, v in zip(SCHEMA, raw)}
        rid = row["requirement_id"]
        if not rid:
            report.error(where, "requirement_id is empty")
            continue
        if not ID_RE.match(rid):
            report.error(where, f"requirement_id '{rid}' is not a valid requirement ID")
        if rid in records:
            report.error(where, f"duplicate requirement_id {rid}")
            continue
        where = f"{where} [{rid}]"
        for field in ("source_document", "requirement_summary", "owner", "phase",
                      "verification_method"):
            if not row[field]:
                report.error(where, f"{field} is empty")
        if row["phase"] and (not PHASE_TOKEN_RE.search(row["phase"])
                             or PHASE_BAD_TOKEN_RE.search(row["phase"])):
            report.error(where, f"phase '{row['phase']}' must use A0/A1/A2 (e.g. A1, A0/A1, A0-A2)")
        if row["verification_method"] and not METHOD_RE.match(row["verification_method"]):
            report.error(where, f"verification_method '{row['verification_method']}' must use "
                                "T, A, I, D (e.g. 'A, T')")
        for field in ("verification_status", "audit_status"):
            value = row[field]
            if value not in STATUS_VALUES:
                report.error(where, f"{field} '{value}' not in {sorted(STATUS_VALUES)}")
        if row["last_updated"] and not DATE_RE.match(row["last_updated"]):
            report.error(where, f"last_updated '{row['last_updated']}' is not ISO YYYY-MM-DD")
        elif not row["last_updated"]:
            report.error(where, "last_updated is empty")
        if row["verification_status"] in {"PASS", "PASS_WITH_ACTIONS"} and not row["evidence_location"]:
            report.error(where, f"verification_status {row['verification_status']} requires "
                                "evidence_location (a results/ record)")
        if row["audit_status"] not in {"NOT_STARTED", ""} and not row["audit_document"]:
            report.error(where, f"audit_status {row['audit_status']} requires audit_document")
        if row["verification_status"] in {"FAIL", "PASS_WITH_ACTIONS"} and not row["notes"]:
            report.warn(where, f"verification_status {row['verification_status']}: record the "
                               "disposition or actions in notes")
        if row["verification_status"] in {"PASS", "PASS_WITH_ACTIONS"} and not row["verification_procedure"]:
            report.warn(where, "verified requirement without verification_procedure")
        # Gate-readiness rule (EXT-AUD-010): a requirement may only claim a verification
        # result when it links to a requirement-specific procedure and a concrete evidence
        # record, never to placeholders or the generic validation plan alone.
        if row["verification_status"] in GATE_STATUSES:
            if (not row["evidence_location"] or PLACEHOLDER_RE.search(row["evidence_location"])
                    or not any(t.startswith("results/") for t in split_ids(row["evidence_location"]))):
                report.error(where, f"verification_status {row['verification_status']} requires a "
                                    "concrete results/ evidence record (no TBD/placeholder)")
            proc = row["verification_procedure"]
            if (not proc or PLACEHOLDER_RE.search(proc)
                    or proc.strip().rstrip("/") in GENERIC_PROCEDURES
                    or not TEST_ID_RE.search(proc)):
                report.error(where, f"verification_status {row['verification_status']} requires a "
                                    "requirement-specific procedure with a test/analysis ID "
                                    "(e.g. 'docs/validation/PERFORMANCE_CHARACTERIZATION.md#PC-03')")
        elif PLACEHOLDER_RE.search(row["evidence_location"] or "TBD"):
            placeholder_rows.append(rid)
        src = row["source_document"]
        if src and not (root / src).exists():
            report.warn(where, f"source_document '{src}' does not exist yet")
        for field in ("evidence_location", "audit_document"):
            for item in split_ids(row[field].replace("|", ";")):
                if "/" in item and not item.startswith(("http://", "https://")):
                    target = item.split("#", 1)[0]
                    if target and not (root / target).exists():
                        report.warn(where, f"{field} '{item}' does not exist")
        records[rid] = row
    if placeholder_rows:
        report.info(rel, f"{len(placeholder_rows)} requirement(s) still have placeholder evidence "
                         "(allowed while NOT_STARTED/IN_PROGRESS/NOT_VERIFIED; blocks PASS/FAIL claims)")
    return records


def default_root() -> Path:
    return Path(__file__).resolve().parents[2]


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the requirements traceability CSV.")
    parser.add_argument("--root", type=Path, default=default_root(),
                        help="repository root (default: two levels above this script)")
    parser.add_argument("--csv", default=DEFAULT_CSV,
                        help=f"traceability CSV relative to the root (default: {DEFAULT_CSV})")
    parser.add_argument("--strict", action="store_true", help="treat warnings as errors")
    parser.add_argument("--summary", action="store_true",
                        help="print verification/audit status counts")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    if not root.is_dir():
        print(f"ERROR   repository root '{root}' does not exist")
        return 2

    report = Report()
    defined, referenced = scan_requirements(root / "requirements", root, report)
    records = check_csv(root / args.csv, root, report)

    if records is not None:
        csv_ids = set(records)
        for rid, src in sorted(defined.items()):
            if rid not in csv_ids:
                report.error(src, f"{rid} is defined here but missing from {args.csv}")
        for rid in sorted(csv_ids - set(defined)):
            if defined:
                report.warn(args.csv, f"{rid} is not defined in any requirements/*.md document "
                                      "(if deleted, keep the row and say so in notes)")
        for rid, row in sorted(records.items()):
            parents = split_ids(row["parent_ids"])
            if not rid.startswith("SYS-") and not parents:
                report.error(f"{args.csv} [{rid}]", "child requirement has no parent_ids")
            for pid in parents:
                if not ID_RE.match(pid):
                    report.error(f"{args.csv} [{rid}]", f"parent_ids entry '{pid}' is not a valid ID")
                elif pid not in csv_ids and pid not in defined:
                    report.error(f"{args.csv} [{rid}]", f"parent {pid} is not defined anywhere")
            src = defined.get(rid)
            if src and row["source_document"] and row["source_document"] != src:
                report.warn(f"{args.csv} [{rid}]", f"source_document '{row['source_document']}' "
                                                   f"but the ID is defined in {src}")
    known = set(defined) | set(records or {})
    for rid, files in sorted(referenced.items()):
        if rid not in known:
            report.warn(", ".join(sorted(files)), f"{rid} is referenced but not defined anywhere")

    for line in report.warnings:
        print(line)
    for line in report.errors:
        print(line)
    if args.summary and records:
        for field in ("verification_status", "audit_status"):
            counts: Dict[str, int] = {}
            for row in records.values():
                counts[row[field]] = counts.get(row[field], 0) + 1
            print(f"{field}: " + ", ".join(f"{k}={counts[k]}" for k in sorted(counts)))
    n_csv = len(records) if records else 0
    print(f"check_traceability: {len(defined)} requirement ID(s) defined in requirements/*.md, "
          f"{n_csv} row(s) in the CSV; {len(report.errors)} error(s), "
          f"{len(report.warnings)} warning(s).")
    if report.errors or (args.strict and report.warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
