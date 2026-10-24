# Kritva Actuator: Milestone Definitions (v1)

| Field | Value |
|---|---|
| Document ID | KA-PLAN-MILESTONE |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead |
| Reviewer / Approver | Project Lead (approver); Independent Mechanical Reviewer; Independent Electrical/Firmware Reviewer |
| Applies to | A0, A1, A2 |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** Milestone content, gate weeks and exit criteria are **proposed targets pending approval**. They become binding only after the Project Lead approves them and records the approval in `planning/v1/DECISIONS.md`. Technical limits are owned by `requirements/` and are referenced here by ID, not restated as new values.

---

## 1. Purpose

This document defines each v1 milestone (A0, A1, A2) precisely enough that its completion can be judged from evidence: the objective, entry criteria, deliverables with owner and canonical path, measurable exit criteria, the required evidence locations, the review gates that feed the milestone, and the sign-off record.

The programme view (timeline, strategy, budget) is in `planning/v1/ROADMAP.md`. Tasks are in `planning/v1/TASKS.md`. Detailed test criteria and procedures are in `docs/validation/VALIDATION_PLAN.md` and in each task's `ACCEPTANCE_CRITERIA.md`.

## 2. References

| Ref | Document |
|---|---|
| [R1] | `requirements/SYSTEM_REQUIREMENTS.md` (sections 5 and 9: milestones and Gates A/B/C) |
| [R2] | `planning/v1/ROADMAP.md` |
| [R3] | `planning/v1/TASKS.md` |
| [R4] | `planning/v1/DECISIONS.md` |
| [R5] | `planning/v1/RISKS_AND_DEPENDENCIES.md` |
| [R6] | `docs/validation/VALIDATION_PLAN.md` |
| [R7] | `requirements/SAFETY_REQUIREMENTS.md` |
| [R8] | `audit/requirements_traceability/REQUIREMENTS_TRACEABILITY.csv` |

## 3. Conventions

### 3.1 Status values

Every gate, criterion and milestone uses the project verification status values: `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `PASS_WITH_ACTIONS`, `FAIL`, `NOT_VERIFIED`.

- `PASS_WITH_ACTIONS` is allowed only when every open action is MEDIUM, LOW or OBSERVATION, has an owner and a due week, and does not affect safety.
- `NOT_VERIFIED` is recorded when no qualified independent reviewer was available or the evidence could not be checked. A `NOT_VERIFIED` gate **blocks** the dependent milestone (ACT-DEC-014).
- A criterion is never `PASS` because a document exists; it needs the specified evidence (SYSTEM_REQUIREMENTS section 6).

### 3.2 Finding severity

`CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `OBSERVATION`. Any open CRITICAL or HIGH finding blocks the gate. A safety-critical defect can never be reclassified as non-blocking to meet a deadline.

### 3.3 Gate record locations

Each review produces one record. The record is owned by the reviewer and lives under `audit/`. It references design documents and evidence by path and never copies them.

| Gate family | Record document (one section per gate) |
|---|---|
| Mechanical audit M0–M2 (requirements, component selection, CAD design) | `audit/mechanical/MECHANICAL_DESIGN_AUDIT.md` |
| Mechanical audit M3–M4 (prototype verification, final acceptance) | `audit/mechanical/MECHANICAL_ACCEPTANCE_AUDIT.md` (+ `MECHANICAL_RISK_REGISTER.md`, `MECHANICAL_RELEASE_CHECKLIST.md`) |
| Electronics review E0–E2 (requirements, board/component selection, schematic/PCB) | `audit/electronics/ELECTRONICS_DESIGN_AUDIT.md` |
| Electronics review E3–E4 (bring-up verification, final acceptance) | `audit/electronics/ELECTRONICS_ACCEPTANCE_AUDIT.md` |
| Firmware review F0–F2 (requirements, architecture, code) | `audit/firmware/FIRMWARE_REVIEW.md` |
| Firmware review F3–F4 (HIL/fault injection, release) | `audit/firmware/FIRMWARE_ACCEPTANCE_AUDIT.md` |
| Acceptance Gates A/B/C and milestone exits A0/A1/A2 | `audit/release/RELEASE_AUDIT.md` |
| Task-level review | `planning/v1/tasks/ACT-0X/ACT-0X-00Y/REVIEW.md` (feeds the gate record by link) |

Full planned names are listed in section 8.

## 4. Milestone summary

| Milestone | Name | Lead | Target exit | Exit gate(s) | Status |
|---|---|---|---|---|---|
| A0 | Educational Motor Control | Electronics/Embedded Intern | End of week 6 | A0 exit review (E1, F1, F2-A0 closed) | NOT_STARTED |
| A1 | Humanoid Smart Actuator | Mechanical Intern + Electronics/Embedded Intern (own workstreams) | Week 11–12 | Gates A, B, C (with M0–M4, E0–E4, F0–F3) | NOT_STARTED |
| A2 | KritvaOS Integration | Project Lead / Integration Owner | Week 12 | A2 exit review (F3, F4) | NOT_STARTED |

## 5. Milestone A0: Educational Motor Control

### 5.1 Objective

Prove motor operation, FOC with phase-current sensing, encoder feedback, basic closed-loop control and safe bench bring-up on a **commercial motor-control development board**, and characterise the motor's electrical and thermal limits (SYSTEM_REQUIREMENTS section 5).

### 5.2 Entry criteria

| # | Entry criterion | Evidence |
|---|---|---|
| A0-EN-01 | ACT-01-001 electrical and firmware requirements approved (E0, F0 at PASS or PASS_WITH_ACTIONS) | `audit/electronics/ELECTRONICS_DESIGN_AUDIT.md`, `audit/firmware/FIRMWARE_REVIEW.md` |
| A0-EN-02 | MCU family recorded (ACT-DEC-004) and development board selected (ACT-DEC-005) | `planning/v1/DECISIONS.md` |
| A0-EN-03 | Motor selected jointly with the gearbox and approved by the PL (M1/E1) | Joint selection record in ACT-02-002 / ACT-01-002 |
| A0-EN-04 | Motor, development board, encoder parts and current-limited PSU on the bench | BOM status column; goods-received note in `hardware/bom/ELECTRICAL_BOM.csv` |
| A0-EN-05 | Bench safety arrangement in place: guarded motor mount, current-limited PSU, accessible power disconnect, no loaded output | Bench safety checklist in `tests/safety/` (owner Electronics Intern; PL inspects) |
| A0-EN-06 | Licence check of any reused reference code (SimpleFOC, moteus, ODrive) completed | Licence note in `firmware/` (ACT-DEC-012, SYS-REQ-054) |

### 5.3 Deliverables

| # | Deliverable | Owner | Canonical path |
|---|---|---|---|
| A0-D-01 | Electrical requirements | Electronics Intern | `requirements/ELECTRICAL_REQUIREMENTS.md` |
| A0-D-02 | Firmware and control requirements | Electronics Intern | `requirements/FIRMWARE_REQUIREMENTS.md` |
| A0-D-03 | MCU and development-board selection record | Electronics Intern | `docs/electronics/ELECTRONICS_ARCHITECTURE.md` |
| A0-D-04 | Bench wiring and setup description | Electronics Intern | `docs/electronics/HARDWARE_BRINGUP.md` |
| A0-D-05 | Firmware: platform, FOC, motor control, encoder, joint control, diagnostics | Electronics Intern | `firmware/{platform,foc,motor_control,encoder,joint_control,diagnostics}/` |
| A0-D-06 | Host bring-up, tuning and logging tools | Electronics Intern (PL reviews) | `software/host_tools/` |
| A0-D-07 | Firmware unit tests and bench test procedures | Electronics Intern | `tests/firmware/`, `tests/hardware/` |
| A0-D-08 | Motor characterisation (Kt check, resistance, inductance, current-loop response, speed range, thermal rise at bench current) | Electronics Intern | `results/motor_control/` |
| A0-D-09 | Closed-loop control results (current, velocity, position) and documented limits | Electronics Intern | `results/motor_control/` |
| A0-D-10 | Fault-response results at bench level (overcurrent, overtemperature, encoder fault, stop) | Electronics Intern | `results/motor_control/`, `tests/safety/` |
| A0-D-11 | A0 exit review record | Project Lead | `audit/release/RELEASE_AUDIT.md` |

### 5.4 Exit criteria (measurable)

Numerical limits are taken from `requirements/FIRMWARE_REQUIREMENTS.md` and `ELECTRICAL_REQUIREMENTS.md` once approved. Where a limit is still TBD, it must be approved **before** the test is run (SYS-REQ-025 principle).

| # | Exit criterion | Measure | Linked SYS-REQ | Evidence |
|---|---|---|---|---|
| A0-EX-01 | Phase-current measurement verified against an independent reference (current probe or calibrated shunt) | Current-sense error within the FW-REQ limit (TBD) over the bench current range | SYS-REQ-050, 044 | `results/motor_control/` |
| A0-EX-02 | FOC current loop runs at the approved rate (proposed 20 kHz, 10 kHz minimum) | Loop timing measured on a GPIO/oscilloscope | SYS-REQ-050, 055 | `results/motor_control/` |
| A0-EX-03 | Current/torque, velocity and position modes operate on the motor shaft; position mode on the output encoder if the gearbox is available | Step and tracking responses recorded for each mode; repeated ≥ 5 times with consistent results (repeatability criterion TBD in FW-REQ) | SYS-REQ-026, 051 | `results/motor_control/` |
| A0-EX-04 | Encoder alignment and calibration procedure works and is repeatable | Procedure executed ≥ 3 times from power-up; commutation offset spread within FW-REQ limit (TBD) | SYS-REQ-053 | `results/motor_control/`, `tests/hardware/` |
| A0-EX-05 | Firmware torque, speed and acceleration limits enforced | Commanded values above the limit are clamped or rejected as specified | SYS-REQ-051 | `tests/firmware/`, `results/motor_control/` |
| A0-EX-06 | Overcurrent, overtemperature, encoder-fault and stop responses verified by fault injection at low voltage with current limiting | Each injected fault reaches the defined safe state; reaction time recorded | SYS-REQ-080, 084 | `results/motor_control/`, `tests/safety/` |
| A0-EX-07 | USB/UART command, configuration and telemetry (proposed ≥ 100 Hz) working | Telemetry log captured at the approved rate | SYS-REQ-060, 062 | `results/motor_control/` |
| A0-EX-08 | Motor operating limits documented (continuous current at bench ambient, thermal rise, speed range) | Characterisation report with test-record fields per SYS-REQ-103 | SYS-REQ-042, 043, 103 | `results/motor_control/`, `results/thermal/` |
| A0-EX-09 | Reviews E1, F1 and F2 (A0 scope) closed with no open CRITICAL/HIGH findings | Review records | SYS-REQ-106 | `audit/electronics/`, `audit/firmware/` |
| A0-EX-10 | Traceability updated for all A0 requirements | CSV rows for A0 requirements carry evidence path and status | SYS-REQ-102 | `audit/requirements_traceability/REQUIREMENTS_TRACEABILITY.csv` |

### 5.5 Reviews feeding A0

E0, F0 (week 1); E1 (week 2); F1 (week 3); F2 A0 scope (week 6). See section 8.

## 6. Milestone A1: Humanoid Smart Actuator

### 6.1 Objective

Integrate the motor, commercial planetary gearbox, independent output shaft, dedicated bearing pair, housing, output encoder, **custom controller PCB** and CAN interface, and validate the defined elbow load case. The milestone is complete when the integrated actuator meets its approved A1 requirements and passes **Gates A, B and C**.

### 6.2 Entry criteria

| # | Entry criterion | Evidence |
|---|---|---|
| A1-EN-01 | Mechanical requirements and acceptance criteria approved at M0 (design gate in SYSTEM_REQUIREMENTS section 5) | `audit/mechanical/MECHANICAL_DESIGN_AUDIT.md` |
| A1-EN-02 | Motor/gearbox jointly selected (M1, E1), with the open items SYS-REQ-013 and SYS-REQ-021 (acceleration, duty, peak duration) closed or explicitly bounded by a PL decision before freeze | `audit/mechanical/MECHANICAL_DESIGN_AUDIT.md`, DECISIONS.md |
| A1-EN-03 | A0 firmware able to run current and position loops (A0 may still be closing; A1 design work starts in week 1 in parallel) | `results/motor_control/` |
| A1-EN-04 | Restrained, guarded, instrumented test fixture design approved before any loaded test | Fixture design in `tests/mechanical/`; review in M2 |

### 6.3 Deliverables

| # | Deliverable | Owner | Canonical path |
|---|---|---|---|
| A1-D-01 | Mechanical requirements (MECH-REQ) | Mechanical Intern | `requirements/MECHANICAL_REQUIREMENTS.md` |
| A1-D-02 | Load cases | Mechanical Intern | `mechanical/calculations/LOAD_CASES.md` |
| A1-D-03 | Torque and speed analysis | Mechanical Intern (Electronics Intern reviews motor side) | `mechanical/calculations/TORQUE_AND_SPEED.md` |
| A1-D-04 | Gearbox selection and motor-class trade study | Mechanical Intern (Electronics Intern evaluates control implications) | `mechanical/calculations/GEARBOX_SELECTION.md` |
| A1-D-05 | Shaft strength (torsion, bending, combined, fatigue, deflection) | Mechanical Intern | `mechanical/calculations/SHAFT_STRENGTH.md` |
| A1-D-06 | Bearing selection (loads, life, fits, spacing, preload) | Mechanical Intern | `mechanical/calculations/BEARING_SELECTION.md` |
| A1-D-07 | CAD (housing, shafts, brackets, encoder mount, assembly) | Mechanical Intern | `mechanical/cad/{housing,shafts,brackets,encoder_mount,assembly}/` |
| A1-D-08 | Fabrication drawings | Mechanical Intern | `mechanical/drawings/` |
| A1-D-09 | Assembly procedure | Mechanical Intern | `mechanical/assembly/` |
| A1-D-10 | Mechanical BOM with part numbers, suppliers, quotations | Mechanical Intern | `mechanical/bom/MECHANICAL_BOM.csv` |
| A1-D-11 | Custom controller PCB (schematic, layout, manufacturing outputs) | Electronics Intern | `hardware/motor_controller/custom_pcb/{schematics,pcb,manufacturing}/` |
| A1-D-12 | Electrical BOM | Electronics Intern | `hardware/bom/ELECTRICAL_BOM.csv` |
| A1-D-13 | CAN firmware | Electronics Intern | `firmware/communication/`, `communication/can/firmware/` |
| A1-D-14 | Diagnostics and fault handling firmware | Electronics Intern | `firmware/diagnostics/` |
| A1-D-15 | Mechanical, performance and safety test procedures | Each intern for their domain | `tests/{mechanical,performance,safety}/` |
| A1-D-16 | Mechanical characterisation results (backlash, repeatability, load, deformation) | Mechanical Intern | `results/mechanical/` |
| A1-D-17 | Thermal results (10 N·m continuous test) | Mechanical Intern + Electronics Intern | `results/thermal/` |
| A1-D-18 | Gate A, B, C records | Project Lead (with reviewers' inputs) | `audit/release/GATE_{A,B,C}_*.md` |

### 6.4 Exit criteria

A1 exits when Gates A, B and C are all `PASS` or `PASS_WITH_ACTIONS`. The gate items below are those of SYSTEM_REQUIREMENTS section 9, each made measurable. Numerical limits marked TBD must be approved by the PL before the test is executed.

#### Gate A: Design release (before fabrication) — target end of week 5

| # | Criterion | Measure / evidence | Linked SYS-REQ | Evidence location |
|---|---|---|---|---|
| GA-01 | CAD assembly includes motor, gearbox, shaft, bearings, housing, encoder and a representative arm/link | CAD assembly inspected; interference check report | SYS-REQ-030–037 | `mechanical/cad/assembly/` |
| GA-02 | Forearm/hand centre of mass measured or taken from CAD; gravity torque recalculated | Updated T_g in LOAD_CASES.md with source of CoM | SYS-REQ-011, 012 | `mechanical/calculations/LOAD_CASES.md` |
| GA-03 | Combined bending/torsion, fatigue and deflection calculations for the shaft reviewed | Safety factors ≥ MECH-REQ limits (TBD in MECHANICAL_REQUIREMENTS); reviewer sign-off | SYS-REQ-030 | `mechanical/calculations/SHAFT_STRENGTH.md` |
| GA-04 | Bearing loads, life, fits, alignment and housing stiffness checked | Life ≥ MECH-REQ duty requirement (TBD); fits specified on drawings | SYS-REQ-031, 032, 091 | `mechanical/calculations/BEARING_SELECTION.md` |
| GA-05 | Gearbox continuous/peak torque, efficiency, backlash, life, input speed and output-load ratings confirmed from manufacturer data | Datasheet references in GEARBOX_SELECTION.md; peak definition verified | SYS-REQ-003, 004, 028 | `mechanical/calculations/GEARBOX_SELECTION.md` |
| GA-06 | Mechanical BOM has exact part numbers, suppliers and current quotations | No BOM line without part number, supplier and quotation date | SYS-REQ-105 | `mechanical/bom/MECHANICAL_BOM.csv` |
| GA-07 | Independent design audit has no unresolved CRITICAL or HIGH findings | M2 record status PASS / PASS_WITH_ACTIONS | SYS-REQ-106 | `audit/mechanical/MECHANICAL_DESIGN_AUDIT.md` |

#### Gate B: Bench validation — target weeks 10–11

| # | Criterion | Measure / evidence | Linked SYS-REQ | Evidence location |
|---|---|---|---|---|
| GB-01 | Actuator holds 1.5 kg arm + 1 kg payload in the horizontal orientation | Hold test duration per SYS-REQ-013 (TBD) without thermal limit exceedance | SYS-REQ-010, 012 | `results/mechanical/`, `results/thermal/` |
| GB-02 | ~6.1 N·m gravity load independently verified with final mass properties | Independent calculation or measurement by someone other than the author | SYS-REQ-011, 012 | `results/mechanical/` |
| GB-03 | 10 N·m continuous test on an instrumented fixture until the thermal-stability criterion is met | Temperature rate below the stability criterion (TBD in VALIDATION_PLAN) | SYS-REQ-020 | `results/thermal/` |
| GB-04 | Peak rating tested at its approved duration and duty cycle | 20 N·m (or 25 N·m if adopted) at approved duration/duty (placeholder ≤ 2 s, ≤ 10 %, TBC) | SYS-REQ-021 | `results/mechanical/`, `results/thermal/` |
| GB-05 | Speed measured across the load range, including the 45 RPM point | Speed–torque points recorded | SYS-REQ-022 | `results/motor_control/`, `results/mechanical/` |
| GB-06 | Position error, repeatability and backlash measured against pre-approved limits | Limits approved and recorded before testing (TBD) | SYS-REQ-025 | `results/mechanical/` |
| GB-07 | No unacceptable deformation, loosening, bearing damage or encoder misalignment after testing | Post-test inspection record against MECH-REQ criteria | SYS-REQ-092 | `results/mechanical/` |
| GB-08 | Test records complete (hardware revision, firmware version, load, supply voltage, ambient, instruments, results) | Record completeness check by reviewer | SYS-REQ-103 | all `results/` folders |

#### Gate C: Safety and release — target weeks 11–12

| # | Criterion | Measure / evidence | Linked SYS-REQ | Evidence location |
|---|---|---|---|---|
| GC-01 | Current limit, overtemperature, encoder-fault and emergency-stop behaviour tested | Fault-injection records on the integrated actuator | SYS-REQ-080, 081 | `tests/safety/`, `results/motor_control/` |
| GC-02 | Hard stops and pinch-point guarding reviewed | Review record; hard-stop energy (≈ 1.9 J basis, TBC) addressed | SYS-REQ-035, 082 | `audit/mechanical/MECHANICAL_ACCEPTANCE_AUDIT.md` |
| GC-03 | Peak-torque and failure behaviour documented | Failure behaviour description and test evidence | SYS-REQ-082 | `results/mechanical/`, `requirements/SAFETY_REQUIREMENTS.md` link |
| GC-04 | Every failure and deviation has a traceable disposition | Deviation list with disposition and owner | SYS-REQ-102 | `audit/release/RELEASE_AUDIT.md` |
| GC-05 | Qualified reviewer approved the safety evidence before any human-interactive testing | Signed review or `NOT_VERIFIED` (blocks) | SYS-REQ-083 | `audit/release/RELEASE_AUDIT.md` |

### 6.5 Reviews feeding A1

M0–M4, E0–E4, F0–F3, Gates A, B, C. See section 8.

## 7. Milestone A2: KritvaOS Integration

### 7.1 Objective

Integrate the actuator interface, driver, command and feedback path, diagnostics and system-level tests with KritvaOS Edge and KritvaOS Nexus, so that a host application commands the actuator through the defined software interface, observes its state and handles reported faults correctly.

### 7.2 Entry criteria

| # | Entry criterion | Evidence |
|---|---|---|
| A2-EN-01 | Actuator interface contract approved (ACT-03-001) | `requirements/INTERFACE_REQUIREMENTS.md`, `docs/interfaces/ACTUATOR_INTERFACE.md`; task REVIEW.md |
| A2-EN-02 | CAN protocol specification approved (ACT-03-002) | `docs/interfaces/CAN_PROTOCOL.md` |
| A2-EN-03 | Firmware CAN implementation conformant (ACT-01-006), or development-board fallback recorded | `tests/integration/` results; DECISIONS.md entry if fallback |
| A2-EN-04 | KritvaOS Edge integration point available (DEP-022) | Edge interface note from the KritvaOS team |
| A2-EN-05 | Actuator has passed fault-behaviour validation (A0-EX-06, and GC-01 for the integrated actuator) | `results/motor_control/`, `tests/safety/` |

### 7.3 Deliverables

| # | Deliverable | Owner | Canonical path |
|---|---|---|---|
| A2-D-01 | Interface requirements (IF-REQ) | Project Lead | `requirements/INTERFACE_REQUIREMENTS.md` |
| A2-D-02 | Actuator software interface specification | Project Lead | `docs/interfaces/ACTUATOR_INTERFACE.md` |
| A2-D-03 | Signal and unit conventions | Project Lead | `docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md` |
| A2-D-04 | CAN protocol specification | Project Lead (Electronics Intern co-author) | `docs/interfaces/CAN_PROTOCOL.md` |
| A2-D-05 | Interface library and implementations (`SimulatedActuator`, `CANActuator`, `DevelopmentBoardActuator`) | Project Lead | `software/actuator_interface/` |
| A2-D-06 | KritvaOS driver | Project Lead | `software/kritva_driver/` |
| A2-D-07 | Simulation model | Project Lead (Mechanical Intern supplies parameters) | `software/simulation/` |
| A2-D-08 | CAN host tools | Project Lead / Electronics Intern | `communication/can/tools/`, `software/host_tools/` |
| A2-D-09 | Integration tests | Project Lead | `tests/integration/` |
| A2-D-10 | Integration results and A2 demonstration record | Project Lead | `results/integration/`, `audit/release/RELEASE_AUDIT.md` |

### 7.4 Exit criteria

| # | Exit criterion | Measure | Linked SYS-REQ | Evidence |
|---|---|---|---|---|
| A2-EX-01 | All interface operations (configure, enable, command_position, command_velocity, command_torque, read_state, read_faults, disable) behave as specified on `SimulatedActuator` and on at least one hardware implementation | Integration test suite passes on both | SYS-REQ-064, 065 | `tests/integration/`, `results/integration/` |
| A2-EX-02 | Host observes position, velocity, current, temperature and fault status at the specified rate | Logged state at the IF-REQ rate (CAN 500 Hz target, 1 kHz goal, TBC) | SYS-REQ-062, 061 | `results/integration/` |
| A2-EX-03 | Command timeout (default 50 ms, TBC) causes the defined safe state, reported to the host | Timeout injection test | SYS-REQ-063 | `results/integration/` |
| A2-EX-04 | Invalid commands rejected with the specified error and no motion | Invalid-command test cases | SYS-REQ-063 | `results/integration/` |
| A2-EX-05 | Injected faults (overcurrent, overtemperature, encoder, communication loss, e-stop) reported through read_faults and handled by the host as specified | Fault-injection integration tests | SYS-REQ-080, 064 | `results/integration/` |
| A2-EX-06 | Hardware, firmware and protocol versions reported and checked by the driver | Version-mismatch test | SYS-REQ-067 | `results/integration/` |
| A2-EX-07 | Demonstration from KritvaOS Edge on the restrained fixture | Demonstration record (video reference and log) | SYS-REQ-065, 083 | `results/integration/`, `audit/release/RELEASE_AUDIT.md` |
| A2-EX-08 | F3 and F4 closed with no open CRITICAL/HIGH findings | Review records | SYS-REQ-106 | `audit/firmware/` |

Passing A2 does **not** establish human-interactive safety and does not authorise deployment on a humanoid robot (SYS-REQ-085).

## 8. Gate reviews

### 8.1 Mechanical audit gates (M0–M4)

| Gate | Name | Week | Reviewer | Inputs (author) | Record | Status |
|---|---|---|---|---|---|---|
| M0 | Requirements Review | 1 | Independent Mechanical Reviewer | `requirements/MECHANICAL_REQUIREMENTS.md`, `mechanical/calculations/LOAD_CASES.md`, ACT-02-001 ACCEPTANCE_CRITERIA (Mechanical Intern) | `audit/mechanical/MECHANICAL_DESIGN_AUDIT.md` | NOT_STARTED |
| M1 | Component Selection Review | 2 | Independent Mechanical Reviewer (Electrical/Firmware Reviewer for motor electrical side) | `GEARBOX_SELECTION.md`, `TORQUE_AND_SPEED.md`, motor/gearbox datasheets, BOM draft | `audit/mechanical/MECHANICAL_DESIGN_AUDIT.md` | NOT_STARTED |
| M2 | CAD Design Review | 4–5 | Independent Mechanical Reviewer | CAD, drawings, `SHAFT_STRENGTH.md`, `BEARING_SELECTION.md`, fixture design | `audit/mechanical/MECHANICAL_DESIGN_AUDIT.md` | NOT_STARTED |
| M3 | Prototype Verification | 7–10 | Independent Mechanical Reviewer | Fabricated-part inspection, assembly record, `results/mechanical/`, `results/thermal/` | `audit/mechanical/MECHANICAL_ACCEPTANCE_AUDIT.md` | NOT_STARTED |
| M4 | Final Acceptance Audit | 11–12 | Independent Mechanical Reviewer | All mechanical evidence; `audit/mechanical/MECHANICAL_RISK_REGISTER.md` | `audit/mechanical/MECHANICAL_ACCEPTANCE_AUDIT.md` | NOT_STARTED |

Finding classes for mechanical audits: PASS, PASS WITH ACTIONS, FAIL, NOT VERIFIED (recorded with the status values in section 3.1).

### 8.2 Electronics review gates (E0–E4)

| Gate | Name | Week | Reviewer | Inputs (author) | Record | Status |
|---|---|---|---|---|---|---|
| E0 | Electrical Requirements Review | 1 | Independent Electrical/Firmware Reviewer | `requirements/ELECTRICAL_REQUIREMENTS.md` (Electronics Intern) | `audit/electronics/ELECTRONICS_DESIGN_AUDIT.md` | NOT_STARTED |
| E1 | Component / Board Selection Review | 2 | Independent Electrical/Firmware Reviewer | MCU comparison, dev-board selection, motor electrical evaluation, ELECTRICAL_BOM draft | `audit/electronics/ELECTRONICS_DESIGN_AUDIT.md` | NOT_STARTED |
| E2 | Schematic / PCB Design Review | 5 (schematic), 6 (layout) | Independent Electrical/Firmware Reviewer | Custom PCB schematic, layout, power-stage and current-sense calculations, housing/connector constraints | `audit/electronics/ELECTRONICS_DESIGN_AUDIT.md` | NOT_STARTED |
| E3 | Bring-up Verification | 8–10 | Independent Electrical/Firmware Reviewer | PCB bring-up records, protection tests | `audit/electronics/ELECTRONICS_ACCEPTANCE_AUDIT.md` | NOT_STARTED |
| E4 | Final Electronics Acceptance | 11–12 | Independent Electrical/Firmware Reviewer | All electronics evidence | `audit/electronics/ELECTRONICS_ACCEPTANCE_AUDIT.md` | NOT_STARTED |

### 8.3 Firmware review gates (F0–F4)

| Gate | Name | Week | Reviewer | Inputs (author) | Record | Status |
|---|---|---|---|---|---|---|
| F0 | Firmware Requirements Review | 1 | Independent Electrical/Firmware Reviewer | `requirements/FIRMWARE_REQUIREMENTS.md` (Electronics Intern) | `audit/firmware/FIRMWARE_REVIEW.md` | NOT_STARTED |
| F1 | Firmware Architecture Review | 3 | Independent Electrical/Firmware Reviewer | `docs/firmware/` architecture, module boundaries, loop timing budget, state machine | `audit/firmware/FIRMWARE_REVIEW.md` | NOT_STARTED |
| F2 | Code Review | 6 (A0 scope), 9–10 (A1 scope: faults, CAN) | Independent Electrical/Firmware Reviewer | Firmware source, unit tests, static-analysis output | `audit/firmware/FIRMWARE_REVIEW.md` | NOT_STARTED |
| F3 | HIL / Fault-Injection Verification | 8–11 | Independent Electrical/Firmware Reviewer | Fault-injection and HIL records (`tests/safety/`, `tests/integration/`) | `audit/firmware/FIRMWARE_ACCEPTANCE_AUDIT.md` | NOT_STARTED |
| F4 | Firmware Release | 12 | Independent Electrical/Firmware Reviewer; PL approves release | Release notes, version tags, regression results | `audit/firmware/FIRMWARE_ACCEPTANCE_AUDIT.md` | NOT_STARTED |

### 8.4 Acceptance gates and milestone exit reviews

| Gate | Name | Week | Decision maker | Required closed inputs | Record | Status |
|---|---|---|---|---|---|---|
| Gate A | Design release | End of 5 | Project Lead | M0, M1, M2; E1; E2 schematic stage for housing/connector interfaces | `audit/release/RELEASE_AUDIT.md` | NOT_STARTED |
| A0 exit | A0 exit review | End of 6 | Project Lead | E0, E1, F0, F1, F2 (A0 scope) | `audit/release/RELEASE_AUDIT.md` | NOT_STARTED |
| Gate B | Bench validation | 10–11 | Project Lead | M3, E3, F3 (bench scope) | `audit/release/RELEASE_AUDIT.md` | NOT_STARTED |
| Gate C | Safety and release | 11–12 | Project Lead with qualified safety reviewer | M4, E4, F3; SAFETY_REQUIREMENTS verification | `audit/release/RELEASE_AUDIT.md` | NOT_STARTED |
| A1 exit | A1 exit review | 12 | Project Lead | Gates A, B, C | `audit/release/RELEASE_AUDIT.md` | NOT_STARTED |
| A2 exit | A2 exit review | 12 | Project Lead | F3, F4; A2-EX-01 to 08 | `audit/release/RELEASE_AUDIT.md` | NOT_STARTED |

### 8.5 Gate review procedure

1. **Request.** The author marks the inputs ready in the task's TASKS.md and asks the reviewer at least 3 working days before the review week (2 days for M0/E0/F0 in week 1).
2. **Pre-read.** The reviewer reads the inputs and records findings in the task's REVIEW.md with severity and requirement reference.
3. **Review meeting.** Author, reviewer and PL walk through the findings. ChatGPT may be used as an additional remote technical reviewer, but is not the sole authority for safety-critical approval.
4. **Disposition.** Each finding gets an owner, an action and a due week. The reviewer sets the gate status.
5. **Record.** The reviewer writes the gate record under `audit/`, linking to REVIEW.md and evidence.
6. **Closure.** The reviewer verifies closure of every action. Only the reviewer closes a finding.
7. **Block.** If the reviewer is unavailable or not qualified, the status is `NOT_VERIFIED` and the gate is blocked (ACT-DEC-014). The PL may not substitute self-review.

## 9. Milestone sign-off

| Milestone | Gate / review | Required status | Reviewer signature | Reviewer date | PL approval | PL date | Status |
|---|---|---|---|---|---|---|---|
| A0 | E0, F0, E1, F1, F2-A0 | PASS / PASS_WITH_ACTIONS | | | | | NOT_STARTED |
| A0 | A0 exit review | PASS / PASS_WITH_ACTIONS | | | | | NOT_STARTED |
| A1 | M0, M1, M2 | PASS / PASS_WITH_ACTIONS | | | | | NOT_STARTED |
| A1 | Gate A | PASS / PASS_WITH_ACTIONS | | | | | NOT_STARTED |
| A1 | M3, E2, E3, F2-A1, F3 | PASS / PASS_WITH_ACTIONS | | | | | NOT_STARTED |
| A1 | Gate B | PASS / PASS_WITH_ACTIONS | | | | | NOT_STARTED |
| A1 | M4, E4 | PASS / PASS_WITH_ACTIONS | | | | | NOT_STARTED |
| A1 | Gate C | PASS (safety items may not be PASS_WITH_ACTIONS if any action is safety-related) | | | | | NOT_STARTED |
| A2 | F3 (integration), F4 | PASS / PASS_WITH_ACTIONS | | | | | NOT_STARTED |
| A2 | A2 exit review | PASS / PASS_WITH_ACTIONS | | | | | NOT_STARTED |

## 10. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | Named reviewers for M, E and F gates and their availability calendar | Project Lead | Week 1 |
| 2 | Thermal-stability criterion for GB-03 | Project Lead / Mechanical Intern (in VALIDATION_PLAN) | Week 8 |
| 3 | Pre-approved position-error, repeatability and backlash limits for GB-06 | Project Lead | Before week 8 testing |
| 4 | Peak duration and duty for GB-04 (placeholder ≤ 2 s, ≤ 10 %) | Project Lead | Before motor/gearbox freeze (week 2) |
| 5 | Whether Gate C may be passed on the development-board controller (fallback) | Project Lead | Week 9 |
| 6 | Qualified safety reviewer for GC-05 | Project Lead | Week 10 |

## 11. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
