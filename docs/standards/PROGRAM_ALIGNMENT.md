# Kritva Actuator: Program Alignment (kritva-program V2)

| Field | Value |
|---|---|
| Document ID | KA-STD-PROGRAM |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.2 |
| Date | 2026-10-18 |
| Document owner | Project Lead / Integration Owner |
| Reviewer / Approver | Project Lead |
| Applies to | A0, A1 |
| Classification | Proprietary and confidential |

> **Status note.** Proposed (ACT-DEC-027), from the external program audit of 2026-10-16; sections 1, 2, 3 and 5 updated 2026-10-18 to match kritva-program decisions D-034 and D-052. kritva-program remains the authority for the program baseline, task weights, approvals and accepted progress. This repository reports task facts only.

---

## 1. What each actuator repository publishes

Each of the five repositories carries `status/tasks.csv` (task facts), `status/workstream.json`, the vendored `status/status.schema.json` (with its recorded SHA-256) and the generated `status/status.json` (schema 2.0). `scripts/status/gen_status.py` writes it and `make check-status` validates it. The generator fails closed on a missing, duplicate or unrecognised value; evidence stays empty until real evidence is recorded; `git_sync` is SYNCED only when a recorded implementation commit is an ancestor of `origin/main`. `source.commit` is the inspected revision, not the commit that contains the report.

| Repository | Workstream ID (registered, D-034) | Tasks |
|---|---|---|
| `kritva-actuator` | ACT_INT | ACT-INT-001 to 007 |
| `kritva-actuator-embedded` | ACT_EMB | ACT-EMB-001 to 007 (with sub-tasks) |
| `kritva-actuator-s` | ACT_S | ACT-S-001 to 008 |
| `kritva-actuator-m` | ACT_M | ACT-M-001 to 008 |
| `kritva-actuator-l` | ACT_L | ACT-L-001 to 008 |

The workstream IDs are registered in kritva-program (decision D-034, 2026-10-17). Registration is only identity: the task IDs are planning-inventory entries, not baseline tasks, and carry no weight, acceptance or credit. The actuator repositories are not yet listed in `sources.json`; the program owner decides that (ONBOARDING.md). Until then absence from the program report is not zero progress, and planning-only tasks are reported as NEEDS_HUMAN by the PR gate, not as accepted progress. Readiness values are conservative: hardware-dependent tasks are HARDWARE-BLOCKED; the Project Lead reviews them.

## 2. Crosswalk

`planning/v2/PROGRAM_CROSSWALK.csv` maps each repository to its program workstream, its local milestones and the program phase. Its older calendar rows are historical; the current schedule is the reforecast in `planning/v2/ROADMAP_48_WEEKS.md`. Local milestone IDs (A0, A1, A2) stay authoritative; they are never relabelled as program phases P0 to P8. Where undecided the phase is `NOT_MAPPED`. The three mechanical repositories map to the program MECHANICAL workstream, whose HOLD (D-003) is lifted for the actuator workstreams by D-052 (section 5); one reporting owner (the Project Lead) avoids counting the same work twice.

## 3. Commit-message envelope (new work)

A Conventional Commit header (for example `docs(status): cite D-052 in workstream note`), an atomic scope, evidence references where relevant, no claim of a test, review or acceptance that did not happen, and exactly one footer line `Task: <TASK-ID>` (for example `Task: ACT-M-008`) naming a task in the registry; this is what the kritva-program PR gate (rules R01 and R02) checks. Do not add session URLs or `Claude-Session` trailers. Do not rewrite historical commits or renumber legacy IDs; legacy `ACT-01/02/03` IDs are resolved through `planning/v2/TASK_ID_MAPPING.csv`. Stricter local rules (for example RaaS trailers) are extensions, not replaced.

## 4. Review pending

Pending independent reviews (mechanical, electrical/firmware, safety) are the open `NOT_VERIFIED` gates in `audit/release/RELEASE_AUDIT.md` and the open items in the dated external audit records. A generated program-level review-pending view is a kritva-program decision; until it exists, the audit records remain the list.

## 5. HOLD and safety

The mechanical HOLD (kritva-program D-003) was lifted for the actuator workstreams (ACT_S, ACT_M, ACT_L, ACT_EMB, ACT_INT) in `ACT-DEC-029` (2026-10-18) and is recorded in kritva-program as D-052; D-003 stays in force for everything else it covers. The kritva-program decision log is the authority for the owner-confirmation status of D-052. D-052 changed text only: the machine-readable flags (`workstreams.json`, V2-M6, `on_hold` in `repo-pipeline.json`) and generated status files are updated by the program owner's tooling, so the central status view can still show HOLD until that is run. Lifting the HOLD does not authorise procurement, fabrication or loaded testing by itself: Gate A, the pending decisions and independent review apply, and fabrication starts only after Gate A plus the release gap (`ACT-DEC-033`). The actuator roadmap (`ROADMAP_48_WEEKS.md`) remains a planning document. Program status never overrides the local safety rules: loaded or peak-torque tests only on a restrained, guarded, instrumented fixture (ACT-DEC-015), and CI never promotes a variant to Validated.

---

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-16 | Kritvaos Actuator Team | Initial draft from the external program audit |
| 0.2 | 2026-10-18 | Kritvaos Actuator Team | Workstream IDs registered (D-034); HOLD lift recorded as D-052; commit envelope aligned with the PR gate; crosswalk calendar marked historical |
