#!/usr/bin/env bash
# Migration Stage 4 (M), parent-side part: moves inside the parent and cleanup.
# Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved.
#
#  1. git mv the shared sizing engine and its reference to mechanical/common-sizing/ (ACT-DEC-026)
#  2. git rm the parent's CAD/drawings/assembly/mechanical-test placeholders (the S, M and L
#     repositories carry the skeleton)
#  3. update the migration manifest (KEEP rows become N/A; moved rows MIGRATED)
# Leaves the changes uncommitted. Run from anywhere inside the parent repo.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "Parent has uncommitted changes. Commit or stash them first."; exit 1
fi
mkdir -p mechanical/common-sizing
for f in actuator_sizing.py expected_results.json; do
  if [ -f "mechanical/calculations/$f" ]; then git mv "mechanical/calculations/$f" "mechanical/common-sizing/$f"; fi
done
python3 scripts/integration/stage4_tool.py list-skeleton | while read -r f; do
  [ -f "$f" ] && git rm -q "$f"
done
python3 scripts/integration/stage4_tool.py settle-m
echo "--- parent checks ---"
make check || true
echo
echo "Review with: git status"
echo "Then: git add -A && git commit -m \"Stage 4 (M): shared sizing engine to mechanical/common-sizing; remove mechanical placeholders (ACT-DEC-026)\""
