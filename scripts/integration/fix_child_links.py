#!/usr/bin/env python3
"""Rewrite relative Markdown links in a child repository that point at parent-repo paths.

Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved.

Documents moved out of the parent (migration Stage 4) contain links such as
``../requirements/FIRMWARE_REQUIREMENTS.md``. In the child repository those targets
do not exist. For each relative link whose target is missing in the child, this tool
rewrites it to an absolute GitHub URL in the parent repository, when the target
exists in the parent layout (checked with --parent-root, a local parent checkout).

Usage: fix_child_links.py CHILD_ROOT --parent-root PARENT_ROOT [--base URL] [--dry-run]
Standard library only. Exit 0 always unless a usage error (2).
"""
import argparse, re, sys
from pathlib import Path

BASE = "https://github.com/KritvaOS/kritva-actuator"
LINK = re.compile(r"(\]\()([^)\s]+)(\))")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("child_root")
    ap.add_argument("--parent-root", required=True)
    ap.add_argument("--base", default=BASE)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    child, parent = Path(a.child_root).resolve(), Path(a.parent_root).resolve()
    changed = 0
    for md in sorted(child.rglob("*.md")):
        if ".git" in md.relative_to(child).parts:
            continue
        text = md.read_text(encoding="utf-8")

        def fix(m):
            nonlocal changed
            target = m.group(2)
            if re.match(r"^(https?:|mailto:|#)", target):
                return m.group(0)
            path, _, frag = target.partition("#")
            if not path:
                return m.group(0)
            resolved = (md.parent / path).resolve()
            if resolved.exists():
                return m.group(0)
            try:
                rel = resolved.relative_to(child)          # path in the parent layout
            except ValueError:
                return m.group(0)
            if not (parent / rel).exists():
                return m.group(0)
            kind = "tree" if (parent / rel).is_dir() else "blob"
            url = f"{a.base}/{kind}/main/{rel.as_posix()}" + (f"#{frag}" if frag else "")
            changed += 1
            return m.group(1) + url + m.group(3)

        new = LINK.sub(fix, text)
        if new != text:
            print(f"{md.relative_to(child)}")
            if not a.dry_run:
                md.write_text(new, encoding="utf-8")
    print(f"fix_child_links: {changed} link(s) rewritten")
    return 0


if __name__ == "__main__":
    sys.exit(main())
