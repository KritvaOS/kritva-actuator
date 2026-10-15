#!/usr/bin/env python3
"""Check relative links in the Kritva Actuator Markdown files.

Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved.

What is checked
---------------
Every ``.md`` file in the repository (excluding ``.git`` and build/venv
folders) is scanned for:

  * inline links and images: ``[text](target)`` and ``![alt](target)``;
  * reference definitions: ``[label]: target``.

Links inside fenced code blocks and inline code spans are ignored.

For each relative target (anything that is not ``http(s):``, ``mailto:``,
``tel:`` or a pure ``#anchor``):

  * ERROR if the target file or directory does not exist. Targets are
    resolved relative to the linking file; a target starting with ``/`` is
    resolved relative to the repository root (GitHub behaviour);
  * WARNING if the target is a Markdown file and the ``#anchor`` does not
    match any heading in it (GitHub-style slugs; the slug algorithm is an
    approximation, so anchor problems are warnings only);
  * pure ``#anchor`` links are checked against the headings of the same file
    (WARNING).

Optional: ``--code-paths`` also reports (as WARNING) repository paths written
in inline code, for example ``planning/v1/DECISIONS.md``, that do not exist
yet. The documentation convention is to cite repository-relative paths in
inline code, so this is a useful "not yet written" list while the baseline is
being populated. It never produces errors.

Exit status: 0 when there are no errors, 1 when there are broken links (or
any warning with ``--strict``), 2 on usage error.

Standard library only. Python 3.8+.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import unquote

SKIP_DIR_NAMES = {".git", "node_modules", "build", "__pycache__", ".venv", "venv", ".pytest_cache"}
FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_RE = re.compile(r"(`+)(.+?)\1")
# [text](target "title") -- target may be wrapped in <>.
INLINE_LINK_RE = re.compile(r"!?\[(?:[^\[\]]|\[[^\[\]]*\])*\]\(\s*(<[^>]+>|[^)\s]+)(?:\s+[\"'(][^)]*[\"')])?\s*\)")
REF_DEF_RE = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)")
HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.*?)\s*#*\s*$")
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:", "ftp://")
# Inline code that looks like a repository path (used only with --code-paths).
CODE_PATH_RE = re.compile(
    r"^(?:\.{1,2}/)?[A-Za-z0-9_.\-]+(?:/[A-Za-z0-9_.\-]+)*/?$"
)
KNOWN_TOP_LEVEL = {
    "requirements", "planning", "docs", "mechanical", "hardware", "firmware",
    "communication", "software", "tests", "results", "audit", "scripts", ".github",
}


def github_slug(heading: str) -> str:
    """Approximate GitHub's heading anchor algorithm."""
    text = heading.strip()
    # Drop inline Markdown: links [x](y) -> x, emphasis and code markers.
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[`*_~]", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.lower()
    out = []
    for ch in text:
        if ch.isalnum() or ch in "-_":
            out.append(ch)
        elif ch == " ":
            out.append("-")
        else:
            cat = unicodedata.category(ch)
            if cat.startswith("L") or cat.startswith("N"):
                out.append(ch)
            # punctuation and symbols are dropped
    return "".join(out)


def heading_anchors(lines: List[str]) -> Set[str]:
    anchors: Set[str] = set()
    counts: Dict[str, int] = {}
    in_fence = False
    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING_RE.match(line)
        if not m:
            continue
        slug = github_slug(m.group(2))
        if slug in counts:
            counts[slug] += 1
            anchors.add(f"{slug}-{counts[slug]}")
        else:
            counts[slug] = 0
            anchors.add(slug)
    # Explicit HTML anchors: <a id="x"></a> or <a name="x">
    for line in lines:
        for m in re.finditer(r"<a\s+(?:id|name)=\"([^\"]+)\"", line):
            anchors.add(m.group(1))
    return anchors


def extract_links(lines: List[str]) -> Tuple[List[Tuple[int, str]], List[Tuple[int, str]]]:
    """Return (links, code_spans) as (line_number, text) lists, ignoring fenced code."""
    links: List[Tuple[int, str]] = []
    codes: List[Tuple[int, str]] = []
    in_fence = False
    for lineno, line in enumerate(lines, start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for m in INLINE_CODE_RE.finditer(line):
            codes.append((lineno, m.group(2).strip()))
        stripped = INLINE_CODE_RE.sub("", line)
        for m in INLINE_LINK_RE.finditer(stripped):
            links.append((lineno, m.group(1)))
        m = REF_DEF_RE.match(stripped)
        if m:
            links.append((lineno, m.group(1)))
    return links, codes


class Checker:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self._anchor_cache: Dict[Path, Set[str]] = {}
        self.link_count = 0

    def anchors_for(self, path: Path) -> Set[str]:
        if path not in self._anchor_cache:
            try:
                lines = path.read_text(encoding="utf-8").splitlines()
            except (OSError, UnicodeDecodeError):
                lines = []
            self._anchor_cache[path] = heading_anchors(lines)
        return self._anchor_cache[path]

    def check_target(self, src: Path, lineno: int, target: str) -> None:
        rel_src = src.relative_to(self.root).as_posix()
        where = f"{rel_src}:{lineno}"
        t = target.strip()
        if t.startswith("<") and t.endswith(">"):
            t = t[1:-1].strip()
        if not t or t.lower().startswith(EXTERNAL_PREFIXES) or re.match(r"^[a-z][a-z0-9+.-]*:", t, re.I):
            return
        self.link_count += 1
        if t.startswith("#"):
            anchor = unquote(t[1:])
            if anchor and anchor.lower() not in self.anchors_for(src):
                self.warnings.append(f"WARNING {where}: anchor '#{anchor}' not found in this file")
            return
        path_part, _, anchor = t.partition("#")
        path_part = path_part.split("?", 1)[0]
        path_part = unquote(path_part)
        if path_part.startswith("/"):
            resolved = (self.root / path_part.lstrip("/")).resolve()
        else:
            resolved = (src.parent / path_part).resolve()
        try:
            resolved.relative_to(self.root)
        except ValueError:
            self.errors.append(f"ERROR   {where}: link '{target}' points outside the repository")
            return
        if not resolved.exists():
            self.errors.append(f"ERROR   {where}: broken link '{target}' "
                               f"(no such file or directory: {resolved.relative_to(self.root).as_posix()})")
            return
        if anchor and resolved.is_file() and resolved.suffix.lower() == ".md":
            if unquote(anchor).lower() not in self.anchors_for(resolved):
                self.warnings.append(f"WARNING {where}: anchor '#{anchor}' not found in "
                                     f"{resolved.relative_to(self.root).as_posix()}")

    def check_code_path(self, src: Path, lineno: int, code: str) -> None:
        if " " in code or not CODE_PATH_RE.match(code) or "/" not in code:
            return
        first = code.lstrip("./").split("/", 1)[0]
        if first not in KNOWN_TOP_LEVEL:
            return
        candidates = [(self.root / code).resolve(), (src.parent / code).resolve()]
        if any(c.exists() for c in candidates):
            return
        rel_src = src.relative_to(self.root).as_posix()
        self.warnings.append(f"WARNING {rel_src}:{lineno}: path `{code}` cited in inline code "
                             "does not exist yet")


SUBMODULE_DIRS = ("embedded/kritva-actuator-embedded/", "mechanical/actuator-s/",
                  "mechanical/actuator-m/", "mechanical/actuator-l/")   # checked by the children's own CI


def iter_markdown(root: Path):
    for path in sorted(root.rglob("*.md")):
        rel_parts = path.relative_to(root).parts
        if any(part in SKIP_DIR_NAMES for part in rel_parts):
            continue
        if path.relative_to(root).as_posix().startswith(SUBMODULE_DIRS):
            continue
        if path.is_file():
            yield path


def default_root() -> Path:
    return Path(__file__).resolve().parents[2]


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Check relative links in Markdown files.")
    parser.add_argument("--root", type=Path, default=default_root(),
                        help="repository root (default: two levels above this script)")
    parser.add_argument("--code-paths", action="store_true",
                        help="also warn about repository paths in inline code that do not exist")
    parser.add_argument("--strict", action="store_true", help="treat warnings as errors")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    if not root.is_dir():
        print(f"ERROR   repository root '{root}' does not exist")
        return 2

    checker = Checker(root)
    files = 0
    for path in iter_markdown(root):
        files += 1
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeDecodeError) as exc:
            checker.errors.append(f"ERROR   {path.relative_to(root).as_posix()}: cannot read ({exc})")
            continue
        links, codes = extract_links(lines)
        for lineno, target in links:
            checker.check_target(path, lineno, target)
        if args.code_paths:
            for lineno, code in codes:
                checker.check_code_path(path, lineno, code)

    for line in checker.warnings:
        print(line)
    for line in checker.errors:
        print(line)
    print(f"check_links: {files} Markdown file(s), {checker.link_count} relative link(s) checked; "
          f"{len(checker.errors)} error(s), {len(checker.warnings)} warning(s).")
    if files == 0:
        print("check_links: no Markdown files found (nothing to check).")
    if checker.errors or (args.strict and checker.warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
