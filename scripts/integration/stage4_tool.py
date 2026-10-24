#!/usr/bin/env python3
"""Helper for migration Stage 4 (used by stage4_migrate.sh).

Copyright (c) 2026 Kritvaos. Licensed under the Apache License, Version 2.0 (see LICENSE).

Subcommands (run from the parent repository root):
  list <key>   print "path<TAB>destination_path" for MOVE rows still PLANNED
  mark <key>   set those rows to MIGRATED in planning/v2/MIGRATION_MANIFEST.csv
  fixrefs <key>
               rewrite references to moved files so they point at the submodule path:
               the traceability CSV evidence_location and the BOM list in check_bom.py

  list-skeleton  print the parent placeholder files that the S/M/L scaffolds replace
  settle-m     after the M import: git-mv/git-rm bookkeeping in the parent. Rewrites manifest
               rows for the within-parent moves, the skeleton placeholders and the KEEP rows

<key> is one of: embedded, m.  Standard library only.
"""
import csv, os, re, sys
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


SKELETON_PREFIXES = ("mechanical/cad/", "mechanical/drawings/", "mechanical/assembly/",
                     "tests/mechanical/", "results/mechanical/")


M = "mechanical/actuator-m/"
SKELETON_MAP = {"mechanical/cad/": M + "cad/", "mechanical/drawings/": M + "drawings/",
                "mechanical/assembly/": M + "assembly/", "tests/mechanical/": M + "tests/",
                "results/mechanical/": M + "results/"}


def settle_m():
    """Update manifest rows after the within-parent moves and skeleton removal (scripts do the git work)."""
    fields, rs = rows()
    counts = {"moved": 0, "skeleton": 0, "kept": 0}
    for x in rs:
        p = x["path"]
        if x["status"] != "PLANNED":
            continue
        if x["action"] == "MOVE_WITHIN_PARENT":
            x["status"] = "MIGRATED"
            counts["moved"] += 1
        elif x["action"] == "COPY_TEMPLATE" and p.startswith(SKELETON_PREFIXES):
            x["status"] = "MIGRATED"
            x["note"] = "skeleton exists in the S, M and L repositories (scaffold); parent placeholder removed"
            counts["skeleton"] += 1
        elif x["action"] in ("COPY_TEMPLATE", "SPLIT"):
            x["action"], x["status"] = "KEEP", "N/A"
            x["destination_repo"], x["destination_path"] = "parent", p
            x["note"] = ("stays in the parent as the common/reference document; variant-specific "
                         "versions are created in the child repositories when their designs start")
            counts["kept"] += 1
        elif x["action"] == "KEEP":
            x["status"] = "N/A"
            counts["kept"] += 1
    # files that exist in the tree but not in the manifest become KEEP rows (parent-owned)
    listed = {x["path"] for x in rs} | {x["destination_path"] for x in rs if x["destination_repo"] == "parent"}
    added = 0
    for d, ds, fs in os.walk("."):
        ds[:] = [y for y in ds if y not in (".git", "__pycache__", "child-repos")
                 and os.path.relpath(os.path.join(d, y), ".").replace(os.sep, "/") not in (
                     "embedded/kritva-actuator-embedded", "mechanical/actuator-s",
                     "mechanical/actuator-m", "mechanical/actuator-l")]
        for fn in fs:
            q = os.path.relpath(os.path.join(d, fn), ".").replace(os.sep, "/")
            if (q in listed or fn == ".gitkeep" or fn.endswith(".pyc") or q.startswith(("docs/images/", "docs/training/", "Claude outputs/"))):
                continue
            rs.append({"path": q, "owner": "Integration Owner", "action": "KEEP", "destination_repo": "parent",
                       "destination_path": q, "status": "N/A", "note": "Parent-owned (added at Stage 4 M)"})
            added += 1
    counts["added"] = added
    with MANIFEST.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rs)
    # traceability evidence that pointed at the removed mechanical placeholders now points at the M repository
    n = 0
    if TRACE.is_file():
        with TRACE.open(newline="", encoding="utf-8") as f:
            r = csv.DictReader(f)
            tf, tr = r.fieldnames, list(r)
        tok = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_./-]*")
        order = sorted(SKELETON_MAP, key=len, reverse=True)

        def fix(m):
            t = m.group(0)
            for old in order:
                if t.startswith(old) and not Path(t).exists():
                    return SKELETON_MAP[old] + t[len(old):]
            return t

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
    counts["trace_rewritten"] = n
    print(f"settled: {counts}")
    return 0


def main(argv):
    if len(argv) == 2 and argv[1] == "settle-m":
        return settle_m()
    if len(argv) == 2 and argv[1] == "list-skeleton":
        for x in rows()[1]:
            if x["action"] == "COPY_TEMPLATE" and x["status"] == "PLANNED" and x["path"].startswith(SKELETON_PREFIXES):
                print(x["path"])
        return 0
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
        dirs = {}          # old directory token -> destination directory token inside the submodule
        for m, newp in moved.items():
            sp = m.split("/")
            dp = newp.split("/")[len(prefix.split("/")):]
            k = 0                                     # length of the unchanged path tail
            while k < min(len(sp), len(dp)) and sp[-1 - k] == dp[-1 - k]:
                k += 1
            for i in range(1, len(sp)):               # directories above the file
                rest = len(sp) - i                    # components below this directory
                if rest <= k:
                    d = dp[:len(dp) - rest]
                    dirs["/".join(sp[:i]) + "/"] = prefix + "/" + "".join(x + "/" for x in d)
        tok = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_./-]*")

        def fix(match):
            t = match.group(0)
            if t in moved:
                return moved[t]
            if t.endswith("/") and t in dirs and not Path(t).exists():
                return dirs[t]
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
