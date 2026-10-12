# ACT-01-001: Define Electrical and Motor-Control Requirements

| Field | Value |
|---|---|
| Document ID | KA-TASK-ACT-01-001 |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead (status); Electronics/Embedded Intern (progress) |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A0, A1 |
| Classification | Proprietary and confidential |

> **Status note.** This task scope is proposed and pending approval.

## 1. Task summary

| Item | Value |
|---|---|
| Task ID | ACT-01-001 |
| Workstream | ACT-01 Electronics and motor control |
| Assignee | Electronics/Embedded Intern |
| Supporting | Project Lead; Mechanical Intern (motor fit, thermal path, PCB envelope) |
| Reviewer | Independent Electrical/Firmware Reviewer (gates E0 and F0) |
| Week | 1 |
| Status | READY |

## 2. Objective

Review the draft electrical and firmware requirements, then complete them so they are measurable, consistent and ready to drive the MCU, development-board and motor-electrical selection in ACT-01-002.

## 3. Scope

1. Review `requirements/ELECTRICAL_REQUIREMENTS.md` and `requirements/FIRMWARE_REQUIREMENTS.md` against SYS-REQ-040 to 055 and SYS-REQ-080 to 081.
2. Close the TBDs where possible:
   - voltage range;
   - phase-current estimates from candidate Kt values;
   - loop rates;
   - thermal thresholds;
   - fault reaction times.
3. Produce the development-board evaluation criteria and shortlist the candidates for ACT-01-002a. The candidates are B-G431B-ESC1, a NUCLEO-G474RE with an X-NUCLEO-IHM08M1-class board, and an ODrive-class reference.
4. Define the A0 bench setup:
   - current-limited PSU;
   - e-stop relay;
   - instruments.
5. Write the electrical-interface constraints for the Mechanical Intern: board envelope, connector positions, thermal path.

**Out of scope:** buying the board (ACT-01-002a).

## 4. Deliverables

| # | Deliverable | Location |
|---|---|---|
| D1 | Reviewed and updated electrical requirements | `requirements/ELECTRICAL_REQUIREMENTS.md` |
| D2 | Reviewed and updated firmware requirements | `requirements/FIRMWARE_REQUIREMENTS.md` |
| D3 | Development-board shortlist with criteria | `docs/electronics/ELECTRONICS_ARCHITECTURE.md` (board-selection section) |
| D4 | Phase-current and power estimate for the motor candidates | `docs/electronics/MOTOR_CONTROLLER_SPECIFICATION.md` |
| D5 | Bench setup definition | `docs/electronics/HARDWARE_BRINGUP.md` |
| D6 | Proposed entries for ACT-DEC-004/005 | `planning/v1/DECISIONS.md` |

## 5. Dependencies

| Depends on | Why |
|---|---|
| ACT-02-001 (load cases) | Torque requirements, which drive the motor current |
| ACT-02-002 candidate motors | Kt, phase resistance and voltage rating |

| Blocks | Why |
|---|---|
| ACT-01-002 | Board selection and bring-up |

## 6. Linked requirements

SYS-REQ-005, 040–045, 050–055, 080, 081.

## 7. Progress log

| Date | Who | Update |
|---|---|---|
| 2026-10-11 | Project Lead | Task created; status READY. |

## 8. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
