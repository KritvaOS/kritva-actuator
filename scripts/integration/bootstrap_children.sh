#!/usr/bin/env bash
# Push the child-repository scaffolds as the first commit of each KritvaOS child repo.
# Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved.
# Usage: scripts/integration/bootstrap_children.sh <path-to-child-repos-folder>
# Works for empty repos and for repos that already have a GitHub-created README/LICENSE
# (existing files are overwritten by the scaffold versions). Uses SSH URLs.
set -euo pipefail
SRC="${1:?path to the extracted child-repos folder}"
WORK="$(mktemp -d)"
for v in s m l embedded; do
  name="kritva-actuator-$v"
  [ -d "$SRC/$name" ] || { echo "missing $SRC/$name"; exit 1; }
  git clone "git@github.com:KritvaOS/$name.git" "$WORK/$name"
  cp -a "$SRC/$name/." "$WORK/$name/"
  ( cd "$WORK/$name"
    git checkout -B main
    git add -A
    if git diff --cached --quiet; then echo "$name: nothing to commit"; else
      git commit -m "Initial scaffold from kritva-actuator parent (ACT-DEC-024)"
      git push -u origin main
    fi )
done
echo "Done. Clones are in $WORK"
