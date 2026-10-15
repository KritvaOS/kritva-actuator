# Kritva Actuator: 24-Week Roadmap (Four Workstreams)

| Field | Value |
|---|---|
| Document ID | KA-PLAN-ROADMAP24 |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 |
| Date | 2026-10-15 |
| Document owner | Project Lead |
| Reviewer / Approver | Project Lead |
| Applies to | A0, A1 |
| Classification | Proprietary and confidential |

> **Status note.** Proposed schedule (ACT-DEC-024/025). The 12-week A0 checkpoint is the existing v1 milestone applied to the M variant. Weeks are planning estimates, not commitments, and depend on motor and gearbox lead times (ACT-DEC-008 and the M0 blockers).

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
