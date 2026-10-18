# Kritva Actuator: Program Alignment (kritva-program V2)

| Field | Value |
|---|---|
| Document ID | KA-STD-PROGRAM |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 |
| Date | 2026-10-16 |
| Document owner | Project Lead / Integration Owner |
| Reviewer / Approver | Project Lead |
| Applies to | A0, A1 |
| Classification | Proprietary and confidential |

> **Status note.** Proposed (ACT-DEC-027), from the external program audit of 2026-10-16. kritva-program remains the authority for the program baseline, task weights, approvals and accepted progress. This repository reports task facts only.

---

## 1. What each actuator repository publishes

Each of the five repositories carries `status/tasks.csv` (task facts), `status/workstream.json`, the vendored `status/status.schema.json` (with its recorded SHA-256) and the generated `status/status.json` (schema 2.0). `scripts/status/gen_status.py` writes it and `make check-status` validates it. The generator fails closed on a missing, duplicate or unrecognised value; evidence stays empty until real evidence is recorded; `git_sync` is SYNCED only when a recorded implementation commit is an ancestor of `origin/main`. `source.commit` is the inspected revision, not the commit that contains the report.

| Repository | Provisional workstream ID | Tasks |
|---|---|---|
| `kritva-actuator` | ACT_INT | ACT-INT-001 to 007 |
| `kritva-actuator-embedded` | ACT_EMB | ACT-EMB-001 to 007 (with sub-tasks) |
| `kritva-actuator-s` | ACT_S | ACT-S-001 to 008 |
| `kritva-actuator-m` | ACT_M | ACT-M-001 to 008 |
| `kritva-actuator-l` | ACT_L | ACT-L-001 to 008 |

The workstream IDs are provisional: they are **not** registered in kritva-program `workstreams.json`, and the task IDs are not in its baseline. Nothing here is registered in `sources.json`; the program owner decides that (ONBOARDING.md). Until then absence from the program report is not zero progress. Readiness values are conservative: hardware-dependent tasks are HARDWARE-BLOCKED; the Project Lead reviews them.

## 2. Crosswalk

`planning/v2/PROGRAM_CROSSWALK.csv` maps each repository to a proposed program workstream, its local milestones and the program phase. Local milestone IDs (A0, A1, A2) stay authoritative; they are never relabelled as program phases P0 to P8. Where undecided the phase is `NOT_MAPPED`. The three mechanical repositories map to the program MECHANICAL workstream, which is on HOLD; one reporting owner (the Project Lead) avoids counting the same work twice.

## 3. Commit-message envelope (new work)

A subject that names the task or planning change, an atomic scope, evidence references where relevant, and no claim of a test, review or acceptance that did not happen. Suggested form: `<TASK-ID>: <imperative summary>` (for example `ACT-M-003: add shaft stress check inputs`) or `planning: <summary>` for planning-only changes. Do not rewrite historical commits or renumber legacy IDs; legacy `ACT-01/02/03` IDs are resolved through `planning/v2/TASK_ID_MAPPING.csv`. Stricter local rules (for example RaaS trailers) are extensions, not replaced.

## 4. Review pending

Pending independent reviews (mechanical, electrical/firmware, safety) are the open `NOT_VERIFIED` gates in `audit/release/RELEASE_AUDIT.md` and the open items in the dated external audit records. A generated program-level review-pending view is a kritva-program decision; until it exists, the audit records remain the list.

## 5. HOLD and safety

The mechanical HOLD (kritva-program D-003) was lifted for the actuator program in `ACT-DEC-029` (2026-10-18); recording the lift in kritva-program is still pending and cannot be done from this repository. Lifting the HOLD does not authorise procurement, fabrication or loaded testing by itself: Gate A, the pending decisions and independent review apply, and fabrication starts only after Gate A plus the release gap (`ACT-DEC-033`). The actuator roadmap (`ROADMAP_48_WEEKS.md`) remains a planning document. Program status never overrides the local safety rules: loaded or peak-torque tests only on a restrained, guarded, instrumented fixture (ACT-DEC-015), and CI never promotes a variant to Validated.

---

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-16 | Kritvaos Actuator Team | Initial draft from the external program audit |
