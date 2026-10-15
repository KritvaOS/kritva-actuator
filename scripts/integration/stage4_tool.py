#!/usr/bin/env python3
"""Helper for migration Stage 4 (used by stage4_migrate.sh).

Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved.

Subcommands (run from the parent repository root):
  list <key>   print "path<TAB>destination_path" for MOVE rows still PLANNED
  mark <key>   set those rows to MIGRATED in planning/v2/MIGRATION_MANIFEST.csv
  fixrefs <key>
               rewrite references to moved files so they point at the submodule path:
               the traceability CSV evidence_location and the BOM list in check_bom.py

<key> is one of: embedded, m.  Standard library only.
"""
import csv, re, sys
from pathlib import Path

TARGETS = {
    "embedded": ("kritva-actuator-embedded", "embedded/kritva-actuator-embedded"),
    "m": ("kritva-actuator-m", "mechanical/actuator-m"),
}
MANIFEST = Path("planning/v2/MIGRATION_MANIFEST.csv")
TRACE = Path("audit/requirements_traceability/REQUIREMENTS_TRACEABILITY.csv")
BOMCHK = Path("scripts/bom/check_bom.py")


def rows():
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def selected(key):
    repo = TARGETS[key][0]
    fields, rs = rows()
    return fields, rs, [x for x in rs if x["action"] == "MOVE"
                        and x["destination_repo"] == repo and x["status"] == "PLANNED"]


def main(argv):
    if len(argv) != 3 or argv[1] not in ("list", "mark", "fixrefs") or argv[2] not in TARGETS:
        print(__doc__)
        return 2
    cmd, key = argv[1], argv[2]
    fields, rs, sel = selected(key)
    prefix = TARGETS[key][1]
    if cmd == "list":
        for x in sel:
            print(f"{x['path']}\t{x['destination_path']}")
    elif cmd == "mark":
        for x in sel:
            x["status"] = "MIGRATED"
            x["note"] = (x["note"] + "; " if x["note"] else "") + f"now in {prefix}/{x['destination_path']}"
        with MANIFEST.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
            w.writeheader()
            w.writerows(rs)
        print(f"marked {len(sel)} row(s) MIGRATED")
    else:
        moved = {x["path"]: f"{prefix}/{x['destination_path']}" for x in rs
                 if x["action"] == "MOVE" and x["destination_repo"] == TARGETS[key][0]
                 and x["status"] == "MIGRATED"}
        dirs = set()
        for m in moved:
            parts = m.split("/")[:-1]
            for i in range(1, len(parts) + 1):
                dirs.add("/".join(parts[:i]) + "/")
        tok = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_./-]*")

        def fix(match):
            t = match.group(0)
            if t in moved:
                return moved[t]
            if t.endswith("/") and t in dirs and not Path(t).exists():
                return f"{prefix}/{t}"
            return t

        n = 0
        if TRACE.is_file():
            with TRACE.open(newline="", encoding="utf-8") as f:
                r = csv.DictReader(f)
                tf, tr = r.fieldnames, list(r)
            for row in tr:
                v = row.get("evidence_location", "")
                nv = tok.sub(fix, v)
                if nv != v:
                    row["evidence_location"] = nv
                    n += 1
            with TRACE.open("w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=tf, lineterminator="\n")
                w.writeheader()
                w.writerows(tr)
        print(f"traceability: {n} evidence_location value(s) rewritten")
        text = BOMCHK.read_text(encoding="utf-8")
        for old, new in moved.items():
            if old.endswith("BOM.csv") and f'("{old}"' in text:
                text = text.replace(f'("{old}"', f'("{new}"')
                print(f"check_bom.py: {old} -> {new}")
        BOMCHK.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
