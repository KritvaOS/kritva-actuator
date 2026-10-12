# ACT-01-001: Review Record (E0 / F0)

| Field | Value |
|---|---|
| Document ID | KA-TASK-ACT-01-001-RV |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Independent Electrical/Firmware Reviewer |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A0, A1 |
| Classification | Proprietary and confidential |

> **Status note.** This is a template to be completed by the reviewer, who must not be the author. If no qualified reviewer is available, the result is `NOT_VERIFIED`.

## 1. Review details

| Item | Value |
|---|---|
| Gates | E0 Electrical requirements; F0 Firmware requirements |
| Reviewer | TBD |
| Date | — |
| Evidence reviewed | ELECTRICAL_REQUIREMENTS.md rev —, FIRMWARE_REQUIREMENTS.md rev — |
| Overall result | NOT_STARTED |

## 2. Checklist

| # | Check | Result | Comment |
|---|---|---|---|
| 1 | Supply range, withstand voltage, reverse polarity and regeneration specified | NOT VERIFIED | |
| 2 | Power stage sized from the motor current, with margin | NOT VERIFIED | |
| 3 | Current-sensing topology, range and bandwidth specified | NOT VERIFIED | |
| 4 | Hardware overcurrent path independent of firmware | NOT VERIFIED | |
| 5 | Hardware e-stop / motor-power removal path defined | NOT VERIFIED | |
| 6 | MCU peripheral checklist complete; MCU and board decision path clear | NOT VERIFIED | |
| 7 | Loop rates and the CPU budget plausible | NOT VERIFIED | |
| 8 | Fault list, thresholds and reactions consistent with SAFETY and INTERFACE requirements | NOT VERIFIED | |
| 9 | State machine identical to INTERFACE_REQUIREMENTS §8.8.1 | NOT VERIFIED | |
| 10 | Licence review rule for reused code included | NOT VERIFIED | |

## 3. Findings

| ID | Severity | Finding | Required action | Owner | Due | Closure evidence | Status |
|---|---|---|---|---|---|---|---|
| — | | | | | | | |

## 4. Sign-off

| Role | Name | Decision | Date |
|---|---|---|---|
| Independent Electrical/Firmware Reviewer | | | |
| Project Lead | | | |

## 5. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft (template) |
