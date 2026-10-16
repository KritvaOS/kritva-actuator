# Kritva Actuator: External Repository Audit (post-restructure), 2026-10-16

| Field | Value |
|---|---|
| Document ID | KA-AUD-EXT-20261016 |
| Repository | `KritvaOS/kritva-actuator` (parent) and four child repositories |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-16 |
| Document owner | Project Lead (record keeper); findings owned by the external reviewer |
| Reviewer / Approver | External reviewer: ChatGPT (remote documentary audit) / Project Lead |
| Applies to | Repository restructure Stages 1 to 5 |
| Classification | Proprietary and confidential |

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-16 | Kritvaos Actuator Team | Record of the external audit and the disposition of each finding |

## 1. Scope and result

Parent HEAD reviewed `461d7100e55361f9bbff22466e4bce9cd3840935`. Pinned submodule SHAs: actuator-s `2b633f1d`, actuator-m `e2bb9516`, actuator-l `adcc77a6`, embedded `34c38e92` (verified against each child by the reviewer).

Result: **Stage 5 NO-GO for completion** (implemented, not verified: the observed parent CI run failed at recursive checkout, so no substantive check executed). **Stage 6 NO-GO.** The reviewer did not run a clone-based history secrets scan, could not read branch-protection settings, and did not execute the test suite; those are unverified, not clean.

## 2. Findings and disposition

| # | Sev | Finding | Disposition |
|---|---|---|---|
| 1, 12 | HIGH | Repositories public while ACT-DEC-023 says private; README states Private | OPEN (owner action): return all five to private; history secrets scan; README unchanged until setting matches |
| 2 | HIGH | Parent CI fails fetching submodules | OPEN (owner action): confirm token can read children; add `CHILD_REPOS_TOKEN` when private; rerun and confirm all checks execute |
| 3 | MED | Gitlinks correct; integration not proven | OPEN: fresh `--recurse-submodules` clone + `make check`; record SHAs as Stage 6 evidence |
| 4 | HIGH | Variant sizing inputs not regression-tested; S/L placeholders | FIXED in tooling: `check_calcs.py` evaluates S/M/L `sizing/inputs.json` with the shared engine and compares with a per-variant `sizing/expected_results.json` when present; warns otherwise. S/L stay Concept; variant references still to be committed after input review |
| 5 | MED | Empty BOM can pass schema check | FIXED in tooling: `check_bom.py --require-items` (release mode). M README wording to be corrected after the BOM content check |
| 6 | MED | Child CODEOWNERS missing/unverified; parent CODEOWNERS paths stale; branch protection unreadable | PARTLY FIXED: parent CODEOWNERS paths updated. OPEN: real handles, child CODEOWNERS verification, branch protection on all five repos |
| 7 | MED | LFS policy inconsistent; CI uses `lfs: false`; embedded has no `.gitattributes` | OPEN: single reviewed LFS policy |
| 8 | MED | Moved-document links not revalidated | OPEN: child-local link check; parent link check over populated submodules after CI passes |
| 9 | MED | Status text says no files moved | FIXED: REPOSITORY_ARCHITECTURE and MIGRATION_PLAN status notes updated |
| 10 | MED | Shared sizing ownership unmapped | FIXED: `ACT-02-SIZING` to `ACT-INT-007` row added (shared work, not evidence of S/M/L completion) |
| 11 | MED | Part-number schemes (MB-NNN, MB-S/L, EB, KA-ELE, legacy KA-MEC) | OPEN: old-to-new mapping and cross-repo uniqueness check |
| 13 | n/a | Residual EXT-AUD items | EXT-AUD-002 to 007, 009, 012, 021 and blockers B1 to B6 remain OPEN design validation; 015/020 OPEN; 016/018 history scan OPEN; 010/011 not executed in CI yet |
| 14 | n/a | Safety/validation status | No change: loaded tests only on a restrained, guarded, instrumented fixture; CI never promotes to Validated |

## 3. Fix order (reviewer)

1. Visibility and history/secrets review. 2. Child checkout authentication and parent CI rerun. 3. Fresh-clone evidence. 4. Variant sizing checker and release-mode BOM (tooling done). 5. CODEOWNERS and branch protection. 6. Status text, part-number mapping, residual findings, release audit.
