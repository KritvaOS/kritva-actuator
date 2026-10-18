# Kritva Actuator: 24-Week Roadmap (Four Workstreams)

| Field | Value |
|---|---|
| Document ID | KA-PLAN-ROADMAP24 |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.4 |
| Date | 2026-10-15 |
| Document owner | Project Lead |
| Reviewer / Approver | Project Lead |
| Applies to | A0, A1 |
| Classification | Proprietary and confidential |

> **Status note.** Proposed schedule (ACT-DEC-024/025). The 12-week A0 checkpoint is the existing v1 milestone applied to the M variant. Weeks are planning estimates, not commitments, and depend on motor and gearbox lead times (ACT-DEC-008 and the M0 blockers).

> **Update 2026-10-18 (ACT-DEC-029).** The mechanical HOLD was lifted and week 1 is Monday 14 Sep 2026 (week 12 = 30 Nov to 6 Dec 2026; week 24 ends 28 Feb 2027). The gates below still apply, and lifting the HOLD does not by itself authorise procurement, fabrication or loaded testing. The note that follows is the earlier state and is kept for history. See `ROADMAP_12_MONTHS.md`.

> **Reforecast (2026-10-18).** The week-12 "A0 checkpoint (M)" below is superseded as a planning target by `ROADMAP_48_WEEKS.md` rev 0.2: A0 exits at P12 (10 Jan 2027) and the M prototype checkpoint is P23, after Gate A and a two-week release gap (ACT-DEC-032, 033). This 24-week text is retained unchanged for traceability.

> **Program HOLD (2026-10-16, superseded).** kritva-program V2 keeps mechanical work on HOLD until the owner formally reopens it. Until then this schedule is **planning-only**: it does not authorise procurement, fabrication or loaded testing. Local safety gates (ACT-DEC-014/015, Gates A/B/C) apply independently of program status. See ACT-DEC-027.

---

## 1. Phases

| Weeks | Phase | ACT-M | ACT-S / ACT-L | ACT-EMB | ACT-INT |
|---|---|---|---|---|---|
| 1-2 | Setup and contracts | Re-run sizing in child repo | Scaffold, sizing inputs | Scaffold, toolchain | Migration Stages 1-3, ICD review |
| 3-4 | Sizing and selection | Motor/gearbox quotes, shaft and bearing | Sizing inputs, candidate list | Dev board bring-up | Standards approved |
| 5-8 | Design | CAD, drawings, Gate A | Concept CAD from M template | FOC current loop, encoder | Driver, CAN spec |
| **12** | **A0 checkpoint (M)** | **Fabricated and bench-tested M with embedded controller** | Concept reviewed | Joint control on M | A0 review |
| 13-16 | S and L design | Fixes, release | Design review checklist, Gate A | Variant config for S and L | Integration tests |
| 17-20 | S and L build | Characterisation | Fabrication, assembly | CAN, diagnostics | Integration on M |
| 21-24 | Validation and release | M release candidate | S and L bench tests | Firmware release | Audit and release note |

## 2. Gates

- A0 (week 12): M only. Exit criteria as in `planning/v1/MILESTONE.md`.
- S and L Gate A: after the Design review checklist is signed.
- Release (week 24): each variant carries its own status. A variant that did not reach Bench-tested is reported as Designed or Concept.

## 3. Assumptions

- Motor and gearbox for M are decided after the quote round (see `mechanical/calculations/MOTOR_GEARBOX_SHORTLIST.md`).
- S and L may use a different motor class; the embedded firmware is parameterised.
- Interns start on the same day. A late start moves the corresponding phase, not the gates.

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-15 | Kritvaos Actuator Team | Initial draft |
| 0.2 | 2026-10-16 | Kritvaos Actuator Team | Program HOLD note (ACT-DEC-027) |
| 0.3 | 2026-10-18 | Kritvaos Actuator Team | HOLD lifted and week 1 dated (ACT-DEC-029) |
| 0.4 | 2026-10-18 | Kritvaos Actuator Team | Reforecast note (ACT-DEC-032, 033) |
