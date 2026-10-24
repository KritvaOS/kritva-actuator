# Kritva Actuator: 12-Month Roadmap (Extension of the 24-Week Plan)

| Field | Value |
|---|---|
| Document ID | KA-PLAN-ROADMAP12 |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.4 |
| Date | 2026-10-18 |
| Document owner | Project Lead |
| Reviewer / Approver | Project Lead |
| Applies to | A0, A1, A2 |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** Accepted as the planning baseline for weeks 25 to 47 by ACT-DEC-028, and re-dated to a week-1 start of 14 Sep 2026 with the mechanical HOLD lifted by ACT-DEC-029 (both 2026-10-18, Project Lead). The other items in section 9 remain open. It extends `ROADMAP_24_WEEKS.md` (weeks 1 to 24, unchanged) to the kritva-program V2 horizon (14 Sep 2026 to 13 Sep 2027). Weeks 25 to 47 are the planning baseline only. Nothing here changes a gate, renumbers an ID, lifts the HOLD or creates program credit.

> **Reforecast.** `ACT-DEC-030`, `032` and `033` (2026-10-18) add a dated reforecast overlay (`ROADMAP_48_WEEKS.md` rev 0.2: P1 = 19 Oct 2026, A0 exit P12, M fabrication two weeks after Gate A, forecast end 28 Nov 2027, 58-week horizon proposed). This document is kept as the accepted baseline of ACT-DEC-028; where dates differ, the reforecast is the current planning forecast.

> **Program HOLD lifted.** The Project Lead lifted the mechanical HOLD (kritva-program D-003, not to be confused with the actuator's `ACT-DEC-003`, the gearbox decision) in `ACT-DEC-029`. Mechanical work may proceed, but only through the existing gates: Gate A design release before fabrication, the decisions still pending in `planning/v1/DECISIONS.md` section 5, independent review (ACT-DEC-014) and restrained-fixture testing (ACT-DEC-015). Lifting the HOLD does not authorise procurement, fabrication or loaded testing by itself. `ACT-DEC-027` is still **PROPOSED**. The lift must also be recorded in kritva-program, which this repository cannot do.

---

## 1. Week numbering and dates

Actuator week 1 begins **Monday 14 September 2026**, the program start, so actuator weeks equal program weeks (`ACT-DEC-029`). Dates are indicative until the owner approves a calendar (section 3.2).

This is a retroactive start. On 18 October 2026 the project was already in week 5, and weeks 1 to 5 were spent on planning, governance and repository migration, not on the actuator work the 24-week plan assigns to those weeks (setup, sizing and selection). The week-12 checkpoint now falls on 30 Nov to 6 Dec 2026, about six weeks after today, with motor and gearbox quotes, Gate A and migration verification still open. Treat weeks 1 to 12 as at risk (section 8, risk 8).

Weeks 1 to 47 end on 8 Aug 2027. Weeks 48 to 52 (9 Aug to 12 Sep 2027) are an **unallocated schedule reserve** inside the program horizon. The owner decides whether to use it as recovery time (section 9).

## 2. Phases

| Weeks | Indicative dates | Phase | Exit gate | Source |
|---|---|---|---|---|
| 1-12 | 14 Sep - 6 Dec 2026 | Setup, sizing, design, A0 checkpoint (M) | A0 checkpoint (M, week 12) | Existing, unchanged |
| 13-24 | 7 Dec 2026 - 28 Feb 2027 | S and L design/build, M characterisation, validation, release candidate | S/L Gate A; release note | Existing, unchanged |
| 25-36 | 1 Mar - 23 May 2027 | Hardware integration (A2-HW), with first-integration and one correction cycle | A2-HW acceptance | Proposed |
| 37-42 | 24 May - 4 Jul 2027 | Qualification and hardening | Qualification exit (target week 42) | Proposed |
| 43-44 | 5 - 18 Jul 2027 | Retest and recovery allowance | Qualification closed | Proposed |
| 45-47 | 19 Jul - 8 Aug 2027 | Release and closure (package and audit a qualified configuration only) | Release-readiness decision | Proposed |
| 48-52 | 9 Aug - 12 Sep 2027 | Unallocated reserve | None | Owner to decide |

Qualification is planned to exit at week 42, ahead of the 8-week window's end, so weeks 43-44 are held as retest and recovery time. Release does not absorb development or design change. Any open CRITICAL or HIGH finding, or missing required review, blocks release.

## 3. Milestones and the two calendars

`A0`, `A1`, `A2` and Gates A/B/C keep the definitions, entry and exit criteria of `planning/v1/MILESTONE.md`. They are not relabelled as program phases P0 to P8. The additional planning layer in this document is called the **Program Planning Overlay (PPO)**. It uses no `M0`-`M6` labels, because `M0`-`M4` already name the mechanical audit gates.

### 3.1 A2 is one milestone with two staged gates

| Gate | Target | Scope | Required before it can pass |
|---|---|---|---|
| **A2-SW** (software integration checkpoint) | Week 12, if the owner approves it | Interface, driver and command/feedback/fault tests against the approved simulator or mock (`SimulatedActuator`, development board) | Stated simulation boundary: what is mocked, interface version under test, hardware-dependent requirements deliberately excluded; tested software commit recorded |
| **A2-HW** (hardware integration acceptance) | Weeks 25-36 | End-to-end command and feedback path with real actuator, embedded controller and the Kritva software integration | Relevant A1 exit and Gates A/B/C `PASS` or `PASS_WITH_ACTIONS`; test-readiness review (section 4); pinned child SHAs; independent reviews |

A2 stays open until A2-HW passes. A2-SW is a checkpoint: it records "software contract verified, physical integration not yet demonstrated". It must not be read as satisfying the A2 exit criteria `A2-EX-*`, which stay as written in v1. A2-HW does not start because week 25 (1 Mar 2027) arrives; it starts when its entry conditions are met.

`ROADMAP_24_WEEKS.md` does not currently list an A2-SW checkpoint, and its week-12 checkpoint expects a fabricated, bench-tested M with embedded controller. Adding A2-SW at week 12 would also assign the Project Lead software work to that week. The owner must approve whether to add it.

### 3.2 v1 and v2 target-date crosswalk (for owner decision)

| Milestone | v1 target (`MILESTONE.md`) | v2 target (`ROADMAP_24_WEEKS.md`) | This proposal | Status |
|---|---|---|---|---|
| A0 | End of week 6 (electronics) | Week 12 checkpoint, M only | Keep v2 week 12 for M; v1 week 6 electronics scope to be confirmed | Conflict, owner to decide |
| A1 | Weeks 11-12 (Gates A/B/C) | Weeks 5-24 across variants | No change proposed | Conflict, owner to decide |
| A2 | Week 12 | Not scheduled | A2-SW week 12 (optional), A2-HW weeks 25-36 | Proposed |

Until the owner records a decision that states which calendar applies, all dates remain proposed. Definitions and acceptance criteria stay authoritative; only target dates change, and only through an owner-approved decision.

## 4. Entry conditions (tracked separately)

Three conditions are independent. Satisfying one does not satisfy another.

| Condition | Meaning | Evidence |
|---|---|---|
| **Migration readiness** | Stage 5 verified (fresh recursive clone, child access, pinned SHAs, manifest, `make check`); Stage 6 audit and release note done | `MIGRATION_PLAN.md`, CI run, clone log |
| **Mechanical authorisation** | **Satisfied in this repository** by `ACT-DEC-029` (2026-10-18). Still to be recorded in kritva-program | `ACT-DEC-029`; kritva-program record pending |
| **Physical test readiness** (before each test stage) | Approved fixture and guarding, calibrated instrumentation, e-stop and overcurrent protection, power and regeneration handling, approved procedure, independent reviewer available (ACT-DEC-015) | Test-readiness record under `audit/` |

The qualification window does not begin on the assumption that test infrastructure will appear during it.

## 5. Proposed work for weeks 25-47 (by workstream)

| Workstream | Weeks 25-36 | Weeks 37-44 | Weeks 45-47 |
|---|---|---|---|
| ACT-INT | Driver and Kritva Motion adapter on M hardware; version-mismatch, timeout, invalid-command and fault-injection integration tests; compatibility matrix | Integration regression on pinned child SHAs; fault-injection and recovery campaign | Evidence audit, release note, program status consolidation |
| ACT-EMB | Variant configuration for S and L; CAN conformance on hardware; diagnostics | Firmware regression, sensor fault detection, release candidate | Firmware release, tagged |
| ACT-M | Support integration; release M | Thermal duty profiles, repeated operation on the guarded fixture | M release record |
| ACT-S, ACT-L | Bench tests per Gate B equivalents | Variant validation against own requirements | Per-variant status in the release note |

Hardware integration separates first integration from corrections allowed before the qualification baseline freezes. Requirements, test limits, cycle counts and tolerances come from `requirements/` and `docs/validation/VALIDATION_PLAN.md`, and are defined before testing.

## 6. Gates (summary)

| Gate | Decision | Closes only when |
|---|---|---|
| A0 checkpoint (week 12, M) | Motor-control fundamentals demonstrated | v1 A0 exit criteria met with evidence |
| Gates A/B/C | Design release, bench validation, safety and release | v1 criteria and independent reviews (ACT-DEC-014) are `PASS` or `PASS_WITH_ACTIONS`; a `NOT_VERIFIED` gate blocks |
| A2-SW | Software contract verified | Section 3.1 conditions |
| A2-HW (A2 exit) | Integration verified on hardware | v1 `A2-EX-*` met on simulator and hardware |
| Qualification exit | Mandatory tests and reviews passed | No open CRITICAL/HIGH finding; failed safety-critical tests are not waived |
| Release readiness | Reproducible, documented, evidenced | Pinned SHAs, CI run IDs, test reports and review records |

A green CI run never closes a safety gate and never promotes a variant to Validated.

## 7. Task and status reporting

- Task IDs are the existing `ACT-EMB/M/S/L/INT-nnn` set, resolved through `TASK_ID_MAPPING.csv`. No new IDs are listed here. The owner adds weeks 25-47 tasks to `status/tasks.csv` in each repository.
- `status/tasks.csv` keeps its current columns. Dependencies and effort stay in planning records keyed by task ID; verification methods stay in requirements, acceptance criteria and the validation plan.
- Evidence is not a new CSV column. The schema already has an `evidence` array, but the generator emits it empty. Evidence ownership and flow must be agreed with the kritva-program schema owner before any generator or schema change. Do not hand-edit `status/status.json`.
- Local task completion is not program acceptance. Workstream IDs ACT_INT, ACT_EMB, ACT_S, ACT_M and ACT_L are registered in kritva-program (D-034) but progress here does not count as program credit.

## 8. Risks

| # | Risk | Mitigation |
|---|---|---|
| 1 | v1 and v2 calendars conflict (high) | Owner-approved crosswalk (3.2); dates stay proposed |
| 2 | Migration readiness and HOLD treated as one gate (high) | Separate entry conditions (section 4) |
| 3 | Release-critical requirements unresolved (peak-torque duration, duty cycle, centre of mass, angular acceleration, final peak torque) | Traceability matrix; unresolved items are milestone blockers; resolve through the decision process |
| 4 | Physical test readiness not a separate gate | Test-readiness record before each stage |
| 5 | One embedded workstream is the shared bottleneck across S, M and L | Explicit M-to-variant hand-off: reusable functions, variant parameters, per-variant regression |
| 6 | Program credit and published evidence diverge | Central registration of workstreams and tasks; agree evidence flow; audit status output against commits, CI and approvals |
| 7 | No recovery allowance before the deadline | Qualification exit at week 42; weeks 43-44 held for retest; weeks 48-52 reserve |
| 8 | Retroactive week-1 start: weeks 1-5 are gone and week 12 is about six weeks away with sizing, quotes, Gate A and Stage 5 verification open (high) | Owner reviews whether week-12 A0 and weeks 13-24 hold, or uses the reserve to shift later phases; no gate is relaxed to meet a date |

## 9. Open decisions for the owner

Decided by ACT-DEC-028: this roadmap is the planning baseline for weeks 25-47. Still open:

1. ~~When does mechanical authorisation lift, and when does week 1 start?~~ Decided by ACT-DEC-029: lifted, week 1 = 14 Sep 2026. Follow-up: record the lift in kritva-program.
2. Which calendar applies: v1, v2 or the crosswalk in 3.2? Is the optional A2-SW checkpoint at week 12 approved?
3. Should the 12-month horizon be registered in `planning/v2/PROGRAM_CROSSWALK.csv`, and who proposes it to kritva-program?
4. Who resources weeks 25 to 47, and is the week 48-52 reserve held for recovery or released?
5. Is `ACT-DEC-027` to be accepted, amended or rejected?

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-18 | Kritvaos Actuator Team | Initial proposal extending weeks 25-47 |
| 0.4 | 2026-10-18 | Kritvaos Actuator Team | HOLD lifted and week 1 = 14 Sep 2026 (ACT-DEC-029); dates re-based; reserve weeks 48-52; risk 8 |
| 0.3 | 2026-10-18 | Kritvaos Actuator Team | Accepted as planning baseline (ACT-DEC-028); open decisions listed |
| 0.2 | 2026-10-18 | Kritvaos Actuator Team | A2 as one milestone with A2-SW/A2-HW gates, v1/v2 crosswalk, separate entry conditions, risks, recovery allowance, PPO naming, status-field guidance |
