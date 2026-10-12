# ACT-01-001: Test and Verification Plan

| Field | Value |
|---|---|
| Document ID | KA-TASK-ACT-01-001-TP |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Electronics/Embedded Intern |
| Reviewer / Approver | Project Lead (scope approval) |
| Applies to | A0, A1 |
| Classification | Proprietary and confidential |

> **Status note.** This plan is proposed. This task is requirements work, so it is verified mainly by review. The listed tests are the ones it **defines** for later tasks.

## 1. Verification of this task

| # | Activity | Method | Expected result | Record |
|---|---|---|---|---|
| V1 | Requirement completeness and measurability review | Inspection (reviewer) | Each requirement has a criterion, a method and evidence | REVIEW.md |
| V2 | Recalculate the phase currents | Analysis | Matches MOTOR_CONTROLLER_SPECIFICATION within rounding | REVIEW.md |
| V3 | Consistency check against SAFETY and INTERFACE requirements | Inspection | No conflicting thresholds, codes or states | REVIEW.md |

## 2. Tests defined for ACT-01-002 (preview)

| Test | Purpose | Key instrument |
|---|---|---|
| Phase R/L measurement | FOC gain design | LCR meter or firmware routine |
| Back-EMF / Kt measurement | Torque constant | Oscilloscope, drive motor or spin-down |
| Current-loop step | CTRL-REQ-011 | Firmware capture buffer, current probe |
| Hardware overcurrent trip timing | SAF-REQ-030 | Oscilloscope |
| E-stop removal of power | SAF-REQ-058 | Oscilloscope or DMM |

## 3. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
