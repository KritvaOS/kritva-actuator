#!/usr/bin/env bash
# Add the four child repositories as submodules of the parent (migration Stage 5).
# Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved.
# Run from the parent repository root, after the children hold their content and the
# Stage 4 and link-fix pull requests are merged.
#
# URLs are HTTPS without credentials, so CI and fresh clones work with a token
# (private) or without one (public). To push over SSH from your machine, once:
#   git config --global url."git@github.com:".pushInsteadOf "https://github.com/"
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
BASE="${KRITVA_SUBMODULE_BASE:-https://github.com/KritvaOS}"   # override only for testing
add() { git submodule add -b main "$BASE/$1.git" "$2"; }
add kritva-actuator-embedded embedded/kritva-actuator-embedded
add kritva-actuator-m        mechanical/actuator-m
add kritva-actuator-s        mechanical/actuator-s
add kritva-actuator-l        mechanical/actuator-l
python3 scripts/integration/check_submodules.py --root . --require
git submodule status
echo
echo "Next: make check ; then commit .gitmodules and the four submodule pointers:"
echo "  git add -A && git commit -m \"Stage 5: add child repositories as submodules (ACT-DEC-024)\" && git push"
