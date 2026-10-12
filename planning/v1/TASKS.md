# Kritva Actuator v1: Master Task Register

| Field | Value |
|---|---|
| Document ID | KA-PLAN-TASKS |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead (maintains status); assignees update progress |
| Reviewer / Approver | Project Lead |
| Applies to | A0, A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** The task IDs, owners and weeks below are **proposed** and pending approval. A task folder is created only after the task's scope and dependencies are confirmed in this register. The Project Lead approves scope changes and records significant ones in `planning/v1/DECISIONS.md`.

---

## 1. Purpose

This register is the **canonical list of planned work** for Kritva Actuator v1. For every task it records:

- the owner and supporting roles;
- the schedule week(s);
- dependencies;
- deliverables and where they live;
- the acceptance reference;
- the status;
- the system requirements the task serves.

Milestone definitions are in `planning/v1/MILESTONE.md`, the timeline in `planning/v1/ROADMAP.md`, decisions in `planning/v1/DECISIONS.md`, and project risks in `planning/v1/RISKS_AND_DEPENDENCIES.md`.

## 2. Workstreams

| Workstream | Folder | Scope | Lead |
|---|---|---|---|
| **ACT-01** Electronics and motor control | `planning/v1/tasks/ACT-01/` | Electrical requirements, development board, FOC, encoders, joint control, diagnostics, custom PCB, CAN firmware | Electronics/Embedded Intern |
| **ACT-02** Mechanical | `planning/v1/tasks/ACT-02/` | Load cases, motor and gearbox selection, shaft, bearings, housing, CAD, fabrication, assembly, mechanical characterisation | Mechanical Intern |
| **ACT-03** Interface and integration | `planning/v1/tasks/ACT-03/` | Software interface, CAN protocol, KritvaOS driver, host tools, simulation, system validation | Project Lead / Integration Owner |

## 3. Task lifecycle

| State | Meaning | Who sets it |
|---|---|---|
| `PROPOSED` | Listed here; scope not yet confirmed | Project Lead |
| `READY` | Scope, dependencies and acceptance criteria approved; the task folder exists (for significant tasks) | Project Lead |
| `IN_PROGRESS` | The assignee is working on it | Assignee |
| `IN_REVIEW` | Deliverables submitted; review or audit under way | Assignee, then reviewer |
| `BLOCKED` | Waiting on a dependency or decision (the reason is recorded) | Assignee or Project Lead |
| `DONE` | Acceptance criteria met with evidence; review closed | Project Lead |
| `CANCELLED` | No longer needed (the reason is recorded) | Project Lead |

A task is **not** `DONE` just because its documents exist. It needs the specified evidence, and an independent review where required. Verification status for individual requirements is tracked separately in `audit/requirements_traceability/REQUIREMENTS_TRACEABILITY.csv`, using `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `PASS_WITH_ACTIONS`, `FAIL` and `NOT_VERIFIED`.

## 4. Task-folder convention

A **significant** task gets a folder `planning/v1/tasks/ACT-0X/ACT-0X-00Y/` containing:

| File | Owner | Purpose |
|---|---|---|
| `TASKS.md` | Project Lead maintains status; assignee updates progress | Scope, task ID, owner, dependencies, deliverables, status, links, progress log |
| `ACCEPTANCE_CRITERIA.md` | Project Lead defines or approves; technical owner contributes | Observable pass/fail criteria and release conditions |
| `DESIGN_NOTES.md` | Assignee | Design choices, assumptions, calculations (or links to them) and alternatives |
| `TEST_PLAN.md` | Assignee; Project Lead approves the scope | Setup, instrumentation, procedure, test conditions, expected results |
| `REVIEW.md` | Reviewer (never the author) | Findings, severity, required actions, evidence reviewed, disposition |

**Small tasks** (for example a typo fix, a minor script change or a single datasheet lookup) can be tracked with a GitHub Issue that uses the `task` template. Do not create all five files for minor changes.

**Rule:** task folders **link** to design outputs in `mechanical/`, `hardware/`, `firmware/`, `docs/`, `tests/` and `results/`. They never hold a second copy of them.

## 5. RACI for joint activities

R = Responsible, A = Approves, C = Contributes, S = Supports.

| Activity | Electronics/Embedded Intern | Mechanical Intern | Project Lead |
|---|---|---|---|
| Define joint requirements | C | C | A |
| Select motor | R (electrical evaluation) | C (mechanical fit) | A |
| Select gearbox | C (control implications) | R (mechanical evaluation) | A |
| Select encoder | R (electrical interface) | R (mounting design) | Review |
| Design controller | R | C (mechanical constraints) | Review |
| Design housing | C (PCB and connector constraints) | R | Review |
| Develop firmware | R | S (integration) | Review |
| Assemble actuator | S (electrical integration) | R (mechanical assembly) | Review |
| Validate actuator | R (electrical tests) | R (mechanical tests) | A |
| KritvaOS integration | S (communication) | S (mechanical demonstration) | R (architecture) |

**The motor and gearbox must be selected jointly.** A gearbox that fits mechanically can still be unsuitable because of its backlash, efficiency, rated torque or effect on control performance.

## 6. Master task register

Weeks refer to the 12-week schedule in `planning/v1/ROADMAP.md`. All statuses are `PROPOSED` at revision 0.1, except where noted.

### 6.1 ACT-01: Electronics and motor control

| ID | Title | Owner | Supporting | Week(s) | Depends on | Deliverables (paths) | Acceptance reference | Linked SYS-REQ | Status |
|---|---|---|---|---|---|---|---|---|---|
| ACT-01-001 | Define electrical and motor-control requirements | Electronics/Embedded Intern | Project Lead | 1 | — | `requirements/ELECTRICAL_REQUIREMENTS.md`, `requirements/FIRMWARE_REQUIREMENTS.md` (review and complete TBDs) | `tasks/ACT-01/ACT-01-001/ACCEPTANCE_CRITERIA.md`; E0 and F0 gates | SYS-REQ-040–045, 050–055 | READY |
| ACT-01-002 | Select the MCU and development board; bring up the motor and FOC on the development board | Electronics/Embedded Intern | Mechanical Intern (motor fit), Project Lead | 2–5 | ACT-01-001, ACT-02-002 (motor choice) | ACT-DEC-004/005 entries; `hardware/motor_controller/development_board/`; `firmware/foc/`, `firmware/platform/`; `docs/electronics/HARDWARE_BRINGUP.md` records; `results/motor_control/` | E1 gate; A0 exit criteria (MILESTONE.md) | SYS-REQ-005, 050, 055, 045, 084 | PROPOSED |
| ACT-01-002a | Development board evaluation and decision | Electronics/Embedded Intern | Project Lead | 2 | ACT-01-001 | Comparison table in `docs/electronics/ELECTRONICS_ARCHITECTURE.md`; ACT-DEC-005 | E1 | SYS-REQ-005, 055 | PROPOSED |
| ACT-01-002b | Motor characterisation (R, L, Kt, pole pairs, thermal) | Electronics/Embedded Intern | Mechanical Intern | 3–4 | ACT-01-002a, motor delivered | `results/motor_control/` characterisation report | `docs/validation/PERFORMANCE_CHARACTERIZATION.md` | SYS-REQ-042, 043 | PROPOSED |
| ACT-01-002c | FOC current loop and calibration | Electronics/Embedded Intern | — | 4–5 | ACT-01-002b | `firmware/foc/`, calibration records | CTRL-REQ-010–016, FW-REQ-020–024 | SYS-REQ-050, 053 | PROPOSED |
| ACT-01-003 | Integrate encoder feedback and implement joint control | Electronics/Embedded Intern | Mechanical Intern (encoder mount) | 5–7 | ACT-01-002, ACT-02-004 (encoder mount) | `firmware/encoder/`, `firmware/joint_control/`; tuning records | CTRL-REQ-020–034 | SYS-REQ-024, 026, 051, 052 | PROPOSED |
| ACT-01-004 | Diagnostics and fault handling | Electronics/Embedded Intern | Independent Electrical/Firmware Reviewer | 8 | ACT-01-003 | `firmware/diagnostics/`; `tests/safety/` fault-injection results | CTRL-REQ-001–006; SAF fault-injection list FI-01–FI-20 | SYS-REQ-062, 063, 080 | PROPOSED |
| ACT-01-005 | Custom controller PCB (A1) | Electronics/Embedded Intern | Mechanical Intern (envelope, mounting), Project Lead | 6–11 (if the schedule permits) | ACT-01-002 results, ACT-02-004 envelope | `hardware/motor_controller/custom_pcb/`; `hardware/bom/ELECTRICAL_BOM.csv` | E2 and E3 gates; `audit/electronics/` | SYS-REQ-005, 041, 081 | PROPOSED |
| ACT-01-006 | CAN communication firmware (A1) | Electronics/Embedded Intern | Project Lead (protocol) | 9 | ACT-03-002 | `firmware/communication/`, `communication/can/firmware/` | IF-REQ CAN section; FW-REQ-051 | SYS-REQ-061, 063, 067 | PROPOSED |
| ACT-01-007 | Firmware robustness, regression and release | Electronics/Embedded Intern | Independent Electrical/Firmware Reviewer | 10–12 | ACT-01-004, ACT-01-006 | Release package; `audit/firmware/FIRMWARE_ACCEPTANCE_AUDIT.md` | F3 and F4 gates | SYS-REQ-102, 103 | PROPOSED |

### 6.2 ACT-02: Mechanical

| ID | Title | Owner | Supporting | Week(s) | Depends on | Deliverables (paths) | Acceptance reference | Linked SYS-REQ | Status |
|---|---|---|---|---|---|---|---|---|---|
| ACT-02-001 | Define elbow load cases and mechanical requirements | Mechanical Intern | Project Lead | 1 | — | `mechanical/calculations/LOAD_CASES.md`; `requirements/MECHANICAL_REQUIREMENTS.md` (TBD closure) | `tasks/ACT-02/ACT-02-001/ACCEPTANCE_CRITERIA.md`; M0 gate | SYS-REQ-010–014, 020–023 | READY |
| ACT-02-002 | Motor/gearbox interface constraints and gearbox candidate comparison | Mechanical Intern | Electronics/Embedded Intern, Project Lead | 2 | ACT-02-001 | `mechanical/calculations/GEARBOX_SELECTION.md`, `TORQUE_AND_SPEED.md`; datasheets; `mechanical/bom/MECHANICAL_BOM.csv` candidates | M1 gate; ACT-DEC-003 release gate | SYS-REQ-002–004, 027, 028, 042 | PROPOSED |
| ACT-02-003 | Shaft, bearing and housing calculations | Mechanical Intern | Independent Mechanical Reviewer | 3–4 | ACT-02-002 | `mechanical/calculations/SHAFT_STRENGTH.md`, `BEARING_SELECTION.md` | M2 (calculation part); Gate A items 3–4 | SYS-REQ-030–032, 091 | PROPOSED |
| ACT-02-004 | Mechanical CAD assembly and fabrication drawings | Mechanical Intern | Electronics/Embedded Intern (PCB envelope), Project Lead | 3–5 | ACT-02-003 | `mechanical/cad/`, `mechanical/drawings/`, `docs/mechanical/MECHANICAL_DESIGN_SPECIFICATION.md` | M2 gate; Gate A | SYS-REQ-030–039 | PROPOSED |
| ACT-02-005 | Fabrication and assembly | Mechanical Intern | Electronics/Embedded Intern | 6–7 | ACT-02-004 approved (Gate A) | Fabricated parts; `docs/mechanical/ASSEMBLY_PROCEDURE.md` (as-built); inspection records in `results/mechanical/` | M3 gate (assembly) | SYS-REQ-036, 038 | PROPOSED |
| ACT-02-006 | Mechanical characterisation (backlash, repeatability, load, thermal support) | Mechanical Intern | Electronics/Embedded Intern | 8–10 | ACT-02-005, ACT-01-003 | `results/mechanical/`; contribution to `docs/validation/PERFORMANCE_CHARACTERIZATION.md` results | Gate B items; M3 gate | SYS-REQ-025, 092 | PROPOSED |
| ACT-02-007 | Test fixture design and build | Mechanical Intern | Project Lead | 4–6 | ACT-02-001 | Fixture CAD in `mechanical/cad/brackets/`; review record | SAF-REQ-065 | SYS-REQ-083 | PROPOSED |
| ACT-02-008 | Mechanical fixes, CAD release and documentation | Mechanical Intern | Independent Mechanical Reviewer | 11–12 | ACT-02-006 | Released CAD and drawings; `audit/mechanical/MECHANICAL_RELEASE_CHECKLIST.md` | M4 gate | SYS-REQ-104, 105 | PROPOSED |

### 6.3 ACT-03: Interface and integration

| ID | Title | Owner | Supporting | Week(s) | Depends on | Deliverables (paths) | Acceptance reference | Linked SYS-REQ | Status |
|---|---|---|---|---|---|---|---|---|---|
| ACT-03-001 | Define the actuator software interface and KritvaOS integration contract | Project Lead / Integration Owner | Electronics/Embedded Intern | 1–3 | — | `docs/interfaces/ACTUATOR_INTERFACE.md`; `requirements/INTERFACE_REQUIREMENTS.md` closure | `tasks/ACT-03/ACT-03-001/ACCEPTANCE_CRITERIA.md` | SYS-REQ-064, 065, 067 | READY |
| ACT-03-002 | CAN protocol specification | Project Lead / Integration Owner | Electronics/Embedded Intern | 3–8 | ACT-03-001 | `docs/interfaces/CAN_PROTOCOL.md`; `communication/can/protocol/` | F1 (allocation review) | SYS-REQ-061, 063, 067 | PROPOSED |
| ACT-03-003 | KritvaOS driver and host tools | Project Lead / Integration Owner | Electronics/Embedded Intern | 5–10 | ACT-03-001, ACT-03-002 | `software/actuator_interface/`, `software/kritva_driver/`, `software/host_tools/`, `communication/can/tools/` | A2 exit | SYS-REQ-064–066 | PROPOSED |
| ACT-03-004 | Simulation model (SimulatedActuator) | Project Lead / Integration Owner | Mechanical Intern (parameters) | 6–10 | ACT-03-001, motor/gearbox data | `software/simulation/` | IF-REQ-101 | SYS-REQ-065 | PROPOSED |
| ACT-03-005 | System validation and A2 demonstration | Project Lead | Both interns | 10–12 | ACT-01-007, ACT-02-006, ACT-03-003 | `docs/validation/VALIDATION_PLAN.md` execution; `results/integration/`; `audit/release/RELEASE_AUDIT.md` | Gates B and C; A2 exit | SYS-REQ-063–065, 080–085 | PROPOSED |
| ACT-03-006 | Traceability and audit coordination | Project Lead | Independent reviewers | 1–12 (continuous) | — | `audit/requirements_traceability/REQUIREMENTS_TRACEABILITY.csv`; gate records | SYS-REQ-102, 106 | SYS-REQ-102, 106 | IN_PROGRESS |

## 7. Critical path (summary)

```
ACT-02-001 -> ACT-02-002 (motor + gearbox jointly) -> procurement lead time
     -> ACT-01-002 (bring-up) -> ACT-01-003 (encoder + joint control)
ACT-02-002 -> ACT-02-003 -> ACT-02-004 -> Gate A -> ACT-02-005 -> integration
     -> ACT-02-006 / ACT-01-004 -> ACT-03-005 (Gates B, C)
```

Motor and gearbox procurement is the main schedule driver. The development-board prototype has priority over the custom PCB (ACT-01-005). The detailed analysis is in `planning/v1/RISKS_AND_DEPENDENCIES.md`.

## 8. Weekly cadence

| Event | When | Participants | Output |
|---|---|---|---|
| Weekly planning and review | Monday | Project Lead and both interns | Updated statuses in this register; blockers recorded |
| Mid-week technical sync | Wednesday (30 min) | Both interns | Interface questions (motor/gearbox/encoder/PCB envelope) |
| Weekly demo | Friday | All | Short demo of progress; results filed in `results/` |
| Gate reviews | Per MILESTONE.md | Reviewers, owners and Project Lead | Gate records in `audit/` |

## 9. Definition of done (for any task)

1. Deliverables are committed in their canonical locations and linked from the task record.
2. Acceptance criteria are met **with evidence** (calculation, inspection record or test record including hardware revision, firmware version, supply voltage, load, ambient temperature, instruments and results).
3. Traceability CSV rows are updated for the affected requirements.
4. Review completed by someone other than the author, where the task is safety-critical or design-releasing; otherwise peer review in the pull request.
5. Open findings are dispositioned; no CRITICAL or HIGH finding remains open.
6. Project Lead sets the status to `DONE`.

## 10. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | Confirm names for each role (interns, reviewers) | Project Lead | Week 1 |
| 2 | Confirm whether ACT-01-005 (custom PCB) is in the 12-week scope or moves to the second iteration | Project Lead | Week 6 |
| 3 | Confirm the procurement lead times for the motor and gearbox, and adjust the weeks | Mechanical Intern | Week 2 |

## 11. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
