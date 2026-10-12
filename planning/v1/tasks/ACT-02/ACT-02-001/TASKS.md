# ACT-02-001: Define Elbow Load Cases and Mechanical Requirements

| Field | Value |
|---|---|
| Document ID | KA-TASK-ACT-02-001 |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead (status); Mechanical Intern (progress) |
| Reviewer / Approver | Independent Mechanical Reviewer / Project Lead |
| Applies to | A1 (design basis used from A0 onwards) |
| Classification | Proprietary and confidential |

> **Status note.** The task scope is proposed, pending approval. Values quoted below are the current proposed baseline (ACT-DEC-008) and are not yet accepted.

## 1. Task summary

| Item | Value |
|---|---|
| Task ID | ACT-02-001 |
| Workstream | ACT-02 Mechanical |
| Assignee | Mechanical Intern |
| Supporting | Project Lead (load assumptions, dynamic requirements); Electronics/Embedded Intern (motor current and thermal implications) |
| Reviewer | Independent Mechanical Reviewer (gate M0) |
| Week | 1 |
| Status | READY |
| Milestone | Feeds A1 Gate A; M0 Requirements Review |

## 2. Objective

Turn the provisional elbow load model into a **complete, reviewed set of load cases** and close the TBDs in `requirements/MECHANICAL_REQUIREMENTS.md` that block the motor and gearbox selection (ACT-02-002).

## 3. Scope

**In scope**

1. Static gravity torque for the horizontal arm, using the baseline load model (1.5 kg forearm/hand at 180 mm, 1.0 kg payload at 350 mm). Worked result: T_g ≈ 6.08 N·m.
2. Sensitivity of T_g to the forearm centre of mass (150–210 mm) and the payload (0.5–2 kg).
3. A dynamic load case once the angular acceleration requirement is defined (SYS-REQ-013). This task must obtain a proposed value from the Project Lead.
4. Arm inertia estimate (point-mass baseline ≈ 0.171 kg·m², then the CAD value) and hard-stop impact energy (≈ 1.9 J at 45 RPM).
5. External load cases on the output: radial, axial and moment loads from the forearm weight, payload, acceleration and handling or impact. These feed BEARING_SELECTION.md and SHAFT_STRENGTH.md.
6. A duty-cycle definition: horizontal holding duration, motion profile and peak repetition.
7. Updating `requirements/MECHANICAL_REQUIREMENTS.md` with the closed values, or with explicit TBDs plus their owner and date.

**Out of scope:** selecting the motor, gearbox or bearings (ACT-02-002 and ACT-02-003).

## 4. Inputs

- `requirements/SYSTEM_REQUIREMENTS.md` sections 8.2–8.3
- `requirements/ACTUATOR_SPECIFICATION.md` section 5
- `requirements/MECHANICAL_REQUIREMENTS.md`
- Humanoid arm CAD or mass properties, if available (DEP-018)

## 5. Deliverables

| # | Deliverable | Location | Status |
|---|---|---|---|
| D1 | Load-case calculation document | `mechanical/calculations/LOAD_CASES.md` | Draft exists; to be completed |
| D2 | Updated mechanical requirements (TBD closure) | `requirements/MECHANICAL_REQUIREMENTS.md` | Not started |
| D3 | Proposed angular-acceleration and duty-cycle values for approval | Entry in `planning/v1/DECISIONS.md` (ACT-DEC-008 update) | Not started |
| D4 | Design notes | `DESIGN_NOTES.md` (this folder) | Template |
| D5 | Verification plan for the load cases | `TEST_PLAN.md` (this folder) | Template |

## 6. Dependencies

| Depends on | Why | Status |
|---|---|---|
| Project Lead input on acceleration and duty cycle | Dynamic load case | Open |
| Arm CAD (DEP-018) | Replace the 180 mm assumption | Open: the provisional value is used until it arrives |

| Blocks | Why |
|---|---|
| ACT-02-002 | Gearbox and motor sizing need the load cases |
| ACT-02-003 | Shaft and bearing loads |
| ACT-02-007 | Fixture load rating |

## 7. Linked requirements

SYS-REQ-010, 011, 012, 013, 014, 020, 021, 022, 023. MECH-REQ-001 and the MECH-REQ load-case section. ACT-REQ load-case section.

## 8. Progress log

| Date | Who | Update |
|---|---|---|
| 2026-10-11 | Project Lead | Task created; status READY. |

## 9. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
