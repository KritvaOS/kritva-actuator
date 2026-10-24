# Kritva Actuator: Electronics Acceptance Audit (E3–E4)

| Field | Value |
|---|---|
| Document ID | KA-AUD-ELEC-ACCEPT |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Independent Electrical/Firmware Reviewer |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A0 (E3 on the development board), A1 (E3 on the PCB, E4) |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** This is the acceptance framework. No results have been recorded. Acceptance limits marked TBD are approved before testing.

---

## 1. Purpose

This document records, criterion by criterion, the verification of the electronics against `requirements/ELECTRICAL_REQUIREMENTS.md`, `docs/electronics/MOTOR_CONTROLLER_SPECIFICATION.md` and the electrical part of `requirements/SAFETY_REQUIREMENTS.md`, using the bring-up and fault-injection evidence.

## 2. E3: Bring-up verification

| # | Criterion | Req. | Evidence | Observed result | Status | Comment | Closure evidence |
|---|---|---|---|---|---|---|---|
| E3-01 | BU-00 to BU-06 passed (inspection, e-stop, logic, debug, sensing, PWM, protections) | HARDWARE_BRINGUP | `results/motor_control/` BU records | — | NOT VERIFIED | | |
| E3-02 | Hardware overcurrent trip time < 10 µs (TBC) | SAF-REQ-030 | FI-01 scope capture | — | NOT VERIFIED | | |
| E3-03 | E-stop removes motor power within ≤ 10 ms, independent of firmware | SAF-REQ-055/058 | FI-14 | — | NOT VERIFIED | | |
| E3-04 | Watchdog reset with the gates held off | SAF-REQ-024 | FI-13 | — | NOT VERIFIED | | |
| E3-05 | Current-sense accuracy: offset and gain against the current probe | ELEC current sensing | BU-04/BU-09 | — | NOT VERIFIED | | |
| E3-06 | Bus-voltage measurement within ±1 % (TBC) | ELEC sensing | BU-04 | — | NOT VERIFIED | | |
| E3-07 | Continuous phase current sustained thermally (BU-13); MOSFET and board temperatures within limits | MOTOR_CONTROLLER_SPEC §3 | BU-13 | — | NOT VERIFIED | | |
| E3-08 | Peak phase current for the defined duration (BU-14) | MOTOR_CONTROLLER_SPEC §3 | BU-14 | — | NOT VERIFIED | | |
| E3-09 | Regeneration: bus ≤ 32 V (TBC) | SAF-REQ-037 | BU-15 / FI-04 | — | NOT VERIFIED | | |
| E3-10 | Reverse-polarity test (A1 PCB) | SAF-REQ-034 | BU-A2 | — | NOT VERIFIED | | |
| E3-11 | CAN physical layer: termination, error-free operation at 1 Mbit/s | IF-REQ CAN | CAN-01 | — | NOT VERIFIED | | |
| E3-12 | Development-board limitations documented with mitigations (A0) | MOTOR_CONTROLLER_SPEC §7 | Compliance table | — | NOT VERIFIED | | |

## 3. E4: Final acceptance

| # | Criterion | Evidence | Status | Comment |
|---|---|---|---|---|
| E4-01 | All ELEC-REQ rows in the traceability CSV are PASS / PASS_WITH_ACTIONS (no safety-related actions) | Traceability CSV | NOT VERIFIED | |
| E4-02 | Schematic, PCB sources, manufacturing outputs and BOM released and consistent with the built hardware (revision tag) | `hardware/` | NOT VERIFIED | |
| E4-03 | Electrical BOM reconciled with purchases | `make bom-summary` | NOT VERIFIED | |
| E4-04 | All E-gate findings closed and verified | ELECTRONICS_DESIGN_AUDIT §4 | NOT VERIFIED | |
| E4-05 | Known limitations and improvement list for the next PCB revision | Report | NOT VERIFIED | |

## 4. Summary

| Gate | Criteria | PASS | PASS WITH ACTIONS | FAIL | NOT VERIFIED |
|---|---|---|---|---|---|
| E3 | 12 | 0 | 0 | 0 | 12 |
| E4 | 5 | 0 | 0 | 0 | 5 |

## 5. Sign-off

| Gate | Reviewer | Result | Date | Project Lead |
|---|---|---|---|---|
| E3 | | | | |
| E4 | | | | |

## 6. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft (framework) |
