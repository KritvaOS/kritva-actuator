# ACT-03-001: Acceptance Criteria

| Field | Value |
|---|---|
| Document ID | KA-TASK-ACT-03-001-AC |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** These criteria are proposed and pending approval.

| # | Criterion | Evidence | Verification | Status |
|---|---|---|---|---|
| AC-01 | Every interface function has documented preconditions, inputs with units and ranges, validation, error behaviour, timeout and post-state. | ACTUATOR_INTERFACE.md | Inspection | NOT_STARTED |
| AC-02 | Return codes and fault codes have numeric values, and are identical across the API, USB/UART and CAN. | ACTUATOR_INTERFACE.md, CAN_PROTOCOL.md | Cross-check | NOT_STARTED |
| AC-03 | The state machine matches INTERFACE_REQUIREMENTS §8.8.1 and FIRMWARE_REQUIREMENTS §12. | Comparison table | Reviewer | NOT_STARTED |
| AC-04 | The parameter table is complete: every parameter has an ID, unit, range, default, access and persistence, and safety parameters are marked writable only when disabled. | ACTUATOR_INTERFACE.md | Inspection | NOT_STARTED |
| AC-05 | Units and signs are defined once (SI; q = 0 at full extension; positive = flexion) and referenced everywhere else. | SIGNAL_AND_UNIT_CONVENTIONS.md | Inspection | NOT_STARTED |
| AC-06 | A conformance-test outline exists that can be run against SimulatedActuator and the hardware. | tests/integration | Inspection | NOT_STARTED |
| AC-07 | The Edge integration contract (joint map, start-up verification, rates) is agreed with the KritvaOS owner. | Signed note in REVIEW.md | Review | NOT_STARTED |

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
