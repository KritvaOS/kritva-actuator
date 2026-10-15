#!/usr/bin/env bash
# Stage 5 prep: make the moved documents' links valid in a child repository.
# Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved.
# Usage (from anywhere inside the parent repo):  scripts/integration/stage5_fix_child_links.sh embedded
# Pushes branch stage5/fix-links to the child; open and merge the pull request.
set -euo pipefail
KEY="${1:?usage: stage5_fix_child_links.sh embedded|m|s|l}"
case "$KEY" in
  embedded) REPO=kritva-actuator-embedded ;;
  m|s|l)    REPO="kritva-actuator-$KEY" ;;
  *) echo "unknown key $KEY"; exit 2 ;;
esac
PARENT="$(git rev-parse --show-toplevel)"
BASE="${KRITVA_REMOTE_BASE:-git@github.com:KritvaOS}"   # override only for testing
WORK="$(mktemp -d)"
git clone "$BASE/$REPO.git" "$WORK/$REPO"
git -C "$WORK/$REPO" checkout -b stage5/fix-links
python3 "$PARENT/scripts/integration/fix_child_links.py" "$WORK/$REPO" --parent-root "$PARENT"
cd "$WORK/$REPO"
if git diff --quiet; then echo "No links to fix in $REPO."; exit 0; fi
git add -A
git commit -m "Point links to parent-repository documents at GitHub (migration Stage 5)"
git push -u origin stage5/fix-links
echo "Open a pull request: https://github.com/KritvaOS/$REPO/compare/main...stage5/fix-links?expand=1"
