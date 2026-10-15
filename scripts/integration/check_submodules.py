#!/usr/bin/env python3
"""Check the four-submodule layout of the parent repository.

Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved.

Reads ``.gitmodules`` (if present) and checks:
  * the four expected submodules are declared at the expected paths;
  * URLs are SSH or HTTPS and contain no credentials (user:token@);
  * with --require: every submodule directory exists and is populated.

Before Stage 5 of the migration there is no ``.gitmodules``; this is reported
as INFO and exits 0 unless --require is given.

Standard library only. Python 3.8+. Exit 0 ok, 1 errors.
"""
import argparse, configparser, re, sys
from pathlib import Path

EXPECTED = {
    "mechanical/actuator-s": "kritva-actuator-s",
    "mechanical/actuator-m": "kritva-actuator-m",
    "mechanical/actuator-l": "kritva-actuator-l",
    "embedded/kritva-actuator-embedded": "kritva-actuator-embedded",
}
CRED = re.compile(r"^https?://[^/@\s]+@", re.I)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=".")
    ap.add_argument("--require", action="store_true", help="fail when submodules are missing")
    a = ap.parse_args(argv)
    root = Path(a.root)
    gm = root / ".gitmodules"
    if not gm.is_file():
        print("INFO: no .gitmodules yet (before migration Stage 5)")
        return 1 if a.require else 0
    cp = configparser.RawConfigParser()
    cp.read(gm, encoding="utf-8")
    found = {}
    errors = []
    for sec in cp.sections():
        path = cp.get(sec, "path", fallback="")
        url = cp.get(sec, "url", fallback="")
        found[path] = url
        if CRED.match(url) or "token" in url.lower() or "password" in url.lower():
            errors.append(f"{path}: URL contains credentials")
        if not (url.startswith("git@") or url.startswith("https://") or url.startswith("ssh://")):
            errors.append(f"{path}: unsupported URL form")
    for path, repo in EXPECTED.items():
        if path not in found:
            errors.append(f"missing submodule {path}")
            continue
        u = found[path].rstrip("/")
        if u.endswith(".git"):
            u = u[:-4]
        if not u.endswith("/" + repo) and not u.endswith(":" + repo):
            errors.append(f"{path}: URL does not point to {repo}")
        d = root / path
        if a.require and not (d.is_dir() and any(d.iterdir())):
            errors.append(f"{path}: directory empty (run git submodule update --init)")
    for path in found:
        if path not in EXPECTED:
            errors.append(f"unexpected submodule {path}")
    for e in errors:
        print("ERROR:", e)
    print(f"submodules: {len(found)} declared, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
