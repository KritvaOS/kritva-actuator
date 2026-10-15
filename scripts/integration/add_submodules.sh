#!/usr/bin/env bash
# Add the four child repositories as submodules of the parent (migration Stage 5).
# Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved.
# Run from the parent repository root, after the children hold their content.
set -euo pipefail
git submodule add git@github.com:KritvaOS/kritva-actuator-embedded.git embedded/kritva-actuator-embedded
git submodule add git@github.com:KritvaOS/kritva-actuator-m.git mechanical/actuator-m
git submodule add git@github.com:KritvaOS/kritva-actuator-s.git mechanical/actuator-s
git submodule add git@github.com:KritvaOS/kritva-actuator-l.git mechanical/actuator-l
python3 scripts/integration/check_submodules.py --root . --require
echo "Review, then: git commit -m 'Add child repositories as submodules (pinned)'"
