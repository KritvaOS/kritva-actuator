# ACT-01-001: Acceptance Criteria

| Field | Value |
|---|---|
| Document ID | KA-TASK-ACT-01-001-AC |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A0, A1 |
| Classification | Proprietary and confidential |

> **Status note.** These criteria are proposed and pending approval.

| # | Criterion | Evidence | Verification | Status |
|---|---|---|---|---|
| AC-01 | Every ELEC-REQ and FW/CTRL-REQ has a measurable acceptance criterion, a verification method and an evidence location. | Requirement tables | Inspection by the reviewer | NOT_STARTED |
| AC-02 | Phase-current estimates (continuous and peak) are calculated for each candidate motor from its Kt for the 15/20/25:1 options. The power stage is sized from the motor current, not from the supply voltage (SYS-REQ-044). | MOTOR_CONTROLLER_SPECIFICATION.md table | Recalculation | NOT_STARTED |
| AC-03 | The supply voltage range, withstand voltage, reverse-polarity behaviour and regeneration strategy are each proposed, with a rationale. | ELECTRICAL_REQUIREMENTS.md | Inspection | NOT_STARTED |
| AC-04 | Development-board candidates are scored against defined criteria: current rating, current-sensing topology, CAN access, MCU peripherals, availability in India, price, documentation. | ELECTRONICS_ARCHITECTURE.md | Inspection | NOT_STARTED |
| AC-05 | The MCU peripheral checklist is complete: synchronised ADC, complementary PWM with dead time, break input, FPU, FDCAN, SPI/ABI, watchdog. | ELECTRICAL_REQUIREMENTS.md | Inspection | NOT_STARTED |
| AC-06 | The fault list and reaction times are consistent with `requirements/SAFETY_REQUIREMENTS.md` and `requirements/INTERFACE_REQUIREMENTS.md`. | Cross-reference table | Reviewer cross-check | NOT_STARTED |
| AC-07 | The A0 bench setup includes a current-limited PSU, a hardware e-stop path (SAF-REQ-058) and the instrument list. | HARDWARE_BRINGUP.md | Inspection | NOT_STARTED |
| AC-08 | Traceability rows for ELEC/FW/CTRL requirements are created or updated. | REQUIREMENTS_TRACEABILITY.csv | `make check-trace` | NOT_STARTED |
| AC-09 | E0 and F0 reviews are complete, with no open CRITICAL or HIGH findings. | REVIEW.md | Reviewer sign-off | NOT_STARTED |

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
