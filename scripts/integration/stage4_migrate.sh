#!/usr/bin/env bash
# Migration Stage 4: import the MOVE files of one workstream into its child repository
# (on a branch, for a pull request), then remove them from the parent working tree.
# Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved.
#
# Usage (from anywhere inside the parent repo):
#   scripts/integration/stage4_migrate.sh embedded
#
# Safe order: the child push happens first. If it fails, the parent is not touched.
# History: this is a documented import commit (source SHA recorded), not filter-repo.
# The parent changes are left UNCOMMITTED for you to review and commit.
set -euo pipefail
KEY="${1:?usage: stage4_migrate.sh embedded|m}"
case "$KEY" in
  embedded) REPO=kritva-actuator-embedded ;;
  m)        REPO=kritva-actuator-m ;;
  *) echo "unknown key $KEY"; exit 2 ;;
esac
cd "$(git rev-parse --show-toplevel)"
if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "Parent has uncommitted changes. Commit or stash them first."; exit 1
fi
SHA="$(git rev-parse HEAD)"
LIST="$(python3 scripts/integration/stage4_tool.py list "$KEY")"
[ -n "$LIST" ] || { echo "Nothing to migrate for $KEY (no PLANNED MOVE rows)."; exit 0; }
echo "Files to import into $REPO: $(echo "$LIST" | wc -l)"

WORK="$(mktemp -d)"
BASE="${KRITVA_REMOTE_BASE:-git@github.com:KritvaOS}"   # override only for testing
git clone "$BASE/$REPO.git" "$WORK/$REPO"
BR="stage4/import-from-parent"
git -C "$WORK/$REPO" checkout -b "$BR"
while IFS=$'\t' read -r SRC DST; do
  mkdir -p "$WORK/$REPO/$(dirname "$DST")"
  cp -p "$SRC" "$WORK/$REPO/$DST"
done <<< "$LIST"
(
  cd "$WORK/$REPO"
  git add -A
  git commit -m "Import $KEY content from kritva-actuator@${SHA:0:12} (migration Stage 4, ACT-DEC-024)

Source repository: KritvaOS/kritva-actuator
Source commit: $SHA
Method: documented import commit (history stays in the parent)."
  git push -u origin "$BR"
)
echo "Pushed branch $BR. Open a pull request: https://github.com/KritvaOS/$REPO/compare/main...$BR?expand=1"

# Parent: remove the moved files, update the manifest and references.
while IFS=$'\t' read -r SRC DST; do git rm -q "$SRC"; done <<< "$LIST"
python3 scripts/integration/stage4_tool.py mark "$KEY"
python3 scripts/integration/stage4_tool.py fixrefs "$KEY"
echo "--- parent checks ---"
make check-manifest check-docs check-links check-bom || true
echo
echo "Review with: git status"
echo "Merge the child pull request first, then commit the parent:"
echo "  git add -A && git commit -m \"Stage 4: migrate $KEY content to $REPO (ACT-DEC-024)\""
