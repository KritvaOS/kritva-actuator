# ACT-03-001: Define the Actuator Software Interface and KritvaOS Integration Contract

| Field | Value |
|---|---|
| Document ID | KA-TASK-ACT-03-001 |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead / Integration Owner |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** This task scope is proposed and pending approval.

## 1. Task summary

| Item | Value |
|---|---|
| Task ID | ACT-03-001 |
| Workstream | ACT-03 Interface and integration |
| Assignee | Project Lead / Integration Owner |
| Supporting | Electronics/Embedded Intern (firmware feasibility) |
| Reviewer | Independent Electrical/Firmware Reviewer |
| Weeks | 1–3 |
| Status | READY |

## 2. Objective

Define precise semantics for the standard actuator interface (configure, enable, command_position, command_velocity, command_torque, read_state, read_faults, disable, and fault acknowledgement), together with the configuration parameter set, units and the KritvaOS Edge/Nexus integration contract. The result lets SimulatedActuator, DevelopmentBoardActuator and CANActuator be implemented interchangeably.

## 3. Scope

1. Function signatures, types, units, preconditions, limits, timeout behaviour and return codes. These elaborate on `requirements/INTERFACE_REQUIREMENTS.md` §8.8.
2. The configuration parameter table: ID, unit, range, default, access and persistence.
3. The USB/UART framing used by host tools in A0.
4. The Edge joint-map contract: joint name, node ID, versions and configuration CRC.
5. A conformance-test outline for all implementations.

## 4. Deliverables

| # | Deliverable | Location |
|---|---|---|
| D1 | Actuator interface specification (API, parameters, USB/UART framing) | `docs/interfaces/ACTUATOR_INTERFACE.md` |
| D2 | Unit and sign conventions | `docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md` |
| D3 | Conformance-test outline | `tests/integration/` (README or plan) |
| D4 | Closed TBDs in INTERFACE_REQUIREMENTS | `requirements/INTERFACE_REQUIREMENTS.md` |

## 5. Dependencies

| Blocks | Why |
|---|---|
| ACT-03-002 | The CAN protocol maps the API onto frames |
| ACT-03-003 / 004 | Driver and simulator implement the API |

## 6. Linked requirements

SYS-REQ-062–067, IF-REQ §8.8–8.14.

## 7. Progress log

| Date | Who | Update |
|---|---|---|
| 2026-10-11 | Project Lead | Task created; status READY. |

## 8. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
