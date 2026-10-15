#!/usr/bin/env python3
"""Check planning/v2/MIGRATION_MANIFEST.csv against the working tree.

Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved.

Rules (ERROR unless stated)
---------------------------
* required columns present; action and status values are from the allowed sets;
* a path appears at most once;
* KEEP rows must exist in the parent tree (any status);
* rows with status PLANNED must still exist in the parent tree (nothing is
  moved before its row is updated);
* rows with status MIGRATED must NOT exist at the old path;
* files absent from the manifest are a WARNING, except .gitkeep placeholders and
  docs/images/, docs/training/ (user-owned assets kept in the parent)
  
  (an ERROR with --strict).

Standard library only. Python 3.8+. Exit 0 when no errors, 1 on errors.
"""
import argparse, csv, os, sys
from pathlib import Path

COLUMNS = ["path", "owner", "action", "destination_repo", "destination_path", "status", "note"]
ACTIONS = {"KEEP", "MOVE", "SPLIT", "COPY_TEMPLATE", "MOVE_WITHIN_PARENT"}
STATUSES = {"PLANNED", "IN_PROGRESS", "MIGRATED", "N/A"}
SKIP_DIRS = {".git", "__pycache__", "child-repos"}
# Not listed in the manifest on purpose: placeholders and user-owned assets (kept in the parent).
IGNORE_UNLISTED_PREFIXES = ("docs/images/", "docs/training/")
IGNORE_UNLISTED_NAMES = (".gitkeep", ".gitmodules")


SUBMODULE_DIRS = ("embedded/kritva-actuator-embedded", "mechanical/actuator-s",
                  "mechanical/actuator-m", "mechanical/actuator-l")


def tree(root):
    out = set()
    for d, ds, fs in os.walk(root):
        ds[:] = [x for x in ds if x not in SKIP_DIRS
                 and os.path.relpath(os.path.join(d, x), root).replace(os.sep, "/") not in SUBMODULE_DIRS]
        for f in fs:
            if f.endswith(".pyc"):
                continue
            out.add(os.path.relpath(os.path.join(d, f), root).replace(os.sep, "/"))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=".")
    ap.add_argument("--manifest", default="planning/v2/MIGRATION_MANIFEST.csv")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args(argv)
    root = Path(a.root)
    mf = root / a.manifest
    if not mf.is_file():
        print(f"ERROR: manifest not found: {a.manifest}")
        return 1
    errors, warnings = [], []
    with mf.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        if r.fieldnames != COLUMNS:
            print(f"ERROR: header must be {COLUMNS}, found {r.fieldnames}")
            return 1
        rows = list(r)
    present = tree(root)
    seen = set()
    dests = {r["destination_path"] for r in rows if r["destination_repo"] == "parent"}
    for i, row in enumerate(rows, start=2):
        p = row["path"]
        where = f"{a.manifest}:{i} ({p})"
        if p in seen:
            errors.append(f"{where}: duplicate path")
        seen.add(p)
        if row["action"] not in ACTIONS:
            errors.append(f"{where}: unknown action {row['action']!r}")
        if row["status"] not in STATUSES:
            errors.append(f"{where}: unknown status {row['status']!r}")
        exists = p in present
        if row["action"] == "KEEP" and not exists:
            errors.append(f"{where}: KEEP row but file is missing")
        elif row["status"] == "PLANNED" and not exists:
            errors.append(f"{where}: PLANNED row but file is already gone (update the status first)")
        elif row["status"] == "MIGRATED" and exists:
            errors.append(f"{where}: MIGRATED row but file still exists at the old path")
    for p in sorted(present - seen - dests):
        if p.startswith(IGNORE_UNLISTED_PREFIXES) or os.path.basename(p) in IGNORE_UNLISTED_NAMES:
            continue
        warnings.append(f"{p}: not listed in the manifest")
    for m in errors:
        print("ERROR:", m)
    for m in warnings:
        print("WARNING:", m)
    print(f"manifest: {len(rows)} rows, {len(errors)} errors, {len(warnings)} warnings")
    if errors or (warnings and a.strict):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
