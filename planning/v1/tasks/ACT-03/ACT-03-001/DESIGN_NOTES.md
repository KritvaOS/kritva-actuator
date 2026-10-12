# ACT-03-001: Design Notes

| Field | Value |
|---|---|
| Document ID | KA-TASK-ACT-03-001-DN |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead / Integration Owner |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** These are working notes; the canonical specification is `docs/interfaces/ACTUATOR_INTERFACE.md`.

## 1. Design principles

1. **One interface, several implementations.** Upper layers never know whether they are talking to SimulatedActuator, DevelopmentBoardActuator (USB/UART) or CANActuator.
2. **The actuator enforces safety; the host only adds to it.** Limits, timeout and state machine live in the firmware. The host checks are a second layer only.
3. **Explicit state.** Every call has preconditions tied to the state machine. A call that is not allowed in the current state returns `E_INVALID_STATE` and changes nothing.
4. **SI units on the wire and in the API.** Degrees and RPM are used in human-facing documents and tools only.
5. **Versioned and atomic.** The protocol is versioned, and configuration is applied atomically.

## 2. Options considered

| Topic | Options | Proposal |
|---|---|---|
| Enable behaviour | Hold the measured position, or start in zero torque | Hold the measured position (prevents a drop under gravity). Zero torque is TBC for compliance tests. |
| Command refresh | Every command refreshes the timeout, or a separate heartbeat | Only **valid motion commands** refresh the timeout. The heartbeat carries status only. |
| Number encoding | Float32, or scaled integers | Decided in CAN_PROTOCOL (ACT-DEC-022). The API always uses float/double SI values. |

## 3. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
