# ACT-03-001: Test and Verification Plan

| Field | Value |
|---|---|
| Document ID | KA-TASK-ACT-03-001-TP |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead / Integration Owner |
| Reviewer / Approver | Project Lead |
| Applies to | A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** This plan is proposed and pending approval.

## 1. Conformance test outline (applies to every implementation)

| # | Test | Expected result |
|---|---|---|
| CT-01 | Every state/call pair | Allowed calls succeed; disallowed calls return `E_INVALID_STATE` with no state change |
| CT-02 | configure() with a valid set, then with a partially invalid set | Valid set is accepted; invalid set is rejected whole, with the offending parameter ID; previous CRC is kept |
| CT-03 | enable() with each precondition missing in turn | The specific error code for each, and the actuator stays DISABLED |
| CT-04 | command_* out of range | `E_OUT_OF_RANGE`; previous setpoint held; timeout not refreshed |
| CT-05 | Command timeout | `COMM_TIMEOUT` → FAULT within timeout + 5 ms |
| CT-06 | Fault acknowledgement with the cause present, then removed | `E_FAULT_ACTIVE`, then DISABLED |
| CT-07 | Version mismatch | `E_VERSION_MISMATCH` |
| CT-08 | Units: command 1.0 rad | The joint moves 57.3° (checked on hardware with the output encoder) |

The tests run first against SimulatedActuator, then against hardware on the fixture (SAF-REQ-051).

## 2. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
