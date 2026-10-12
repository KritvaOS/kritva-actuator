# Kritva Actuator: Programme Roadmap (v1)

| Field | Value |
|---|---|
| Document ID | KA-PLAN-ROADMAP |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead |
| Reviewer / Approver | Project Lead (approver); Independent Mechanical Reviewer and Independent Electrical/Firmware Reviewer (review of gate placement) |
| Applies to | A0, A1, A2 and post-v1 planning |
| Classification | Proprietary and confidential (see `LICENSE`) |

> **Status note.** All dates, durations, budgets and technical values in this roadmap are **proposed targets pending approval**. They become binding only after the Project Lead approves them and records the approval in `planning/v1/DECISIONS.md`. Technical values are owned by `requirements/SYSTEM_REQUIREMENTS.md` (KA-REQ-SYS) and its child documents; this roadmap repeats them only as context and never overrides them.

---

## 1. Purpose and scope

This document is the top-level plan for version 1 (v1) of the Kritva Actuator Development Platform. It states:

1. the vision and the agreed development strategy (Option C);
2. the milestone roadmap A0 → A1 → A2, with objectives, scope, deliverables, exit gates and dependencies;
3. the order in which the repository is brought up, from foundation documents to A2 integration;
4. the 12-week timeline for both intern workstreams and the joint milestones;
5. the post-v1 evolution path;
6. the budget roadmap.

Detailed milestone definitions and gate checklists are in `planning/v1/MILESTONE.md` (KA-PLAN-MILESTONE). Tasks, owners and weeks are in `planning/v1/TASKS.md` (KA-PLAN-TASKS). Decisions are in `planning/v1/DECISIONS.md` (KA-PLAN-DECISIONS). Project risks and dependencies are in `planning/v1/RISKS_AND_DEPENDENCIES.md` (KA-PLAN-RISKS).

## 2. References

| Ref | Document | Relationship |
|---|---|---|
| [R1] | `requirements/SYSTEM_REQUIREMENTS.md` | Parent requirements (SYS-REQ IDs) |
| [R2] | `planning/v1/MILESTONE.md` | Milestone definitions, entry/exit criteria, gate reviews |
| [R3] | `planning/v1/TASKS.md` | Master task register, RACI, cadence, definition of done |
| [R4] | `planning/v1/DECISIONS.md` | Decision log ACT-DEC-001 to ACT-DEC-015 |
| [R5] | `planning/v1/RISKS_AND_DEPENDENCIES.md` | Project risk and dependency registers |
| [R6] | `docs/validation/VALIDATION_PLAN.md` | Verification approach and detailed gate criteria |
| [R7] | `docs/architecture/SYSTEM_ARCHITECTURE.md` | System architecture |
| [R8] | `mechanical/calculations/LOAD_CASES.md`, `TORQUE_AND_SPEED.md`, `GEARBOX_SELECTION.md` | Calculations behind the targets |

## 3. Vision

Kritvaos will build an **in-house smart rotary actuator** that becomes the reusable building block for KritvaOS humanoid joints. The v1 programme has three equal aims:

1. **Capability.** Teach and record the full actuator lifecycle (mechanical design, power electronics, field-oriented control, joint control, communication, software integration and validation) within a two-intern team led by the Project Lead.
2. **Reusable platform.** Leave behind assets that later revisions inherit without rework: controller hardware architecture, FOC and joint-control firmware, the versioned CAN protocol, the actuator software interface and KritvaOS driver, the test fixture, test procedures and the evidence and audit framework.
3. **Humanoid elbow.** Deliver a validated elbow actuator that carries the defined forearm and payload load case (SYS-REQ-010 to SYS-REQ-014) on a restrained, guarded, instrumented fixture, and that KritvaOS can command through a defined interface.

The guiding principle is **"build once, evolve through iterations"**. The first prototype is low-cost, but nothing in it is treated as disposable: interfaces, firmware structure, mounting geometry and tests are designed to be carried into the next iteration.

**What v1 is not.** v1 is an experimental, bench-validated device. It is not a human-safe joint, not a certified product and not a full humanoid arm (SYS-REQ-083, SYS-REQ-085).

## 4. Strategy

### 4.1 Option C

The agreed strategy is **Option C: educational motor-control platform → smart actuator → humanoid joint actuator** (ACT-DEC-001).

| Stage | What it proves | Milestone |
|---|---|---|
| Educational motor-control platform | The team can drive a commercial BLDC/PMSM with FOC and phase-current sensing, read encoders, close loops and protect the hardware, on a commercial development board, with documented limits | A0 |
| Smart actuator | The motor, commercial planetary gearbox, independent output shaft on dedicated bearings, housing, output encoder, custom controller PCB and CAN interface work together as one module that meets its approved A1 requirements | A1 |
| Humanoid joint actuator | The actuator is commanded, monitored and fault-handled by KritvaOS (Edge and Nexus) through a standard actuator interface, with simulated and hardware implementations behind the same interface | A2 |

Options considered and rejected at programme start are recorded in ACT-DEC-001.

### 4.2 Development Level 2

Per ACT-DEC-002 the team **buys** the motor (commercial BLDC/PMSM), the gearbox (commercial planetary, ACT-DEC-003), the encoder ICs/modules and the bearings, and **develops in-house** the housing, output-shaft assembly, motor controller (development board in A0, custom PCB in A1), FOC firmware, joint control, CAN protocol and KritvaOS driver.

### 4.3 Things v1 does not attempt

| Not attempted in v1 | Reason | Revisit condition |
|---|---|---|
| Custom motor | Outside team capability and schedule; Level 2 | Post-v1, only with a measured torque-density shortfall |
| Custom harmonic or cycloidal drive | High precision-manufacturing risk (ACT-DEC-003) | Post-v1, only with measured evidence that the planetary gearbox limits performance |
| High-voltage inverter | Safety and cost; 24 V DC nominal (ACT-DEC-013) | Not planned |
| FOC before the sensing hardware is validated | FOC depends on correct current and position sensing | Never; sequencing rule in TASKS.md |
| Full humanoid before bench validation | Gate B and Gate C come first | After separate system-level safety review (SYS-REQ-085) |
| Collision detection from motor current alone | Gearbox friction and backlash mask external torque | Post-v1 with joint-side sensing evidence |
| Running an unvalidated actuator on a loaded humanoid | Safety | Never |

### 4.4 Contingency principle

If procurement or PCB fabrication slips, the **working development-board prototype has priority over an unfinished custom PCB**. A custom PCB is not a prerequisite for A0 success. A1 integration and A2 software integration may proceed on the development-board controller (the `DevelopmentBoardActuator` implementation) with the custom PCB delivered as a later increment; this fallback is recorded as a deviation with a decision entry and does not by itself fail A0 or A2. Whether A1 Gate C can be passed on the development board is a Project Lead decision recorded in DECISIONS.md.

## 5. Milestone roadmap

### 5.1 Overview

```
   Wk:   1    2    3    4    5    6    7    8    9   10   11   12
         |----|----|----|----|----|----|----|----|----|----|----|----|
   A0    [=========== A0 Educational Motor Control =====]
         (dev board, FOC, current sensing, encoders, closed loop)  A0 exit: end wk 6
   A1    [req]---[selection]---[CAD/PCB design]--GA--[fab/integrate]--GB--GC
                                                 wk5            wk10-11 wk11-12
   A2              [interface contract]......[sim]......[driver/CAN]==[A2 demo]
                                                                    wk 9-12
```

GA, GB, GC = Gates A, B, C. A1 begins its requirements and design work in week 1 in parallel with A0, because the mechanical design gate (Gate A) must be passed before fabrication in week 6.

### 5.2 A0: Educational Motor Control

| Item | Content |
|---|---|
| Objective | Prove motor operation, FOC with phase-current sensing, motor-side and output-side encoder reading, basic closed-loop current, velocity and position control, and safe bench bring-up on a **commercial motor-control development board**. Characterise the motor's electrical and thermal limits. |
| Lead | Electronics/Embedded Intern |
| Supporting | Mechanical Intern (motor fit, bench fixture, coupling), Project Lead (approvals) |
| Scope in | MCU family proposal (ACT-DEC-004) and development-board selection (ACT-DEC-005); commercial motor (selected jointly with the gearbox); current-limited bench supply; FOC bring-up; encoder alignment and calibration; current/velocity/position loops on the motor shaft and, when available, through the gearbox; firmware torque, speed and acceleration limits; overcurrent, overtemperature, encoder-fault and stop handling at bench level; USB/UART command and telemetry; host bring-up tools; characterisation records |
| Scope out | Custom PCB; CAN; loaded elbow testing; KritvaOS driver; human-interactive operation |
| Key deliverables | `requirements/ELECTRICAL_REQUIREMENTS.md`, `requirements/FIRMWARE_REQUIREMENTS.md`; `hardware/motor_controller/development_board/` selection record and wiring; `firmware/{platform,foc,motor_control,encoder,joint_control,diagnostics}/`; `software/host_tools/`; `results/motor_control/` bring-up and characterisation records; `tests/firmware/`, `tests/hardware/` procedures |
| Exit gate | Motor controlled repeatably on the bench; control behaviour and operating limits documented with evidence in `results/motor_control/`; review gates E1 and F1 closed; F2 (A0 code review) closed with no open CRITICAL/HIGH findings (details: MILESTONE.md section 5) |
| Target week | End of week 6 (motor-control validation in week 5, closed-loop position in week 6) |
| Dependencies | Motor and development board delivered (DEP-001, DEP-002); bench PSU and oscilloscope available (DEP-015, DEP-016); ACT-01-001 approved (E0/F0) |

### 5.3 A1: Humanoid Smart Actuator

| Item | Content |
|---|---|
| Objective | Integrate the motor, commercial planetary gearbox, independent 12 mm output shaft on a dedicated bearing pair, housing, output encoder, custom controller PCB and CAN interface into one actuator module, and validate it against the elbow load case. |
| Lead | Mechanical Intern (mechanical workstream ACT-02) and Electronics/Embedded Intern (electronics workstream ACT-01), each within their own workstream; Project Lead integrates |
| Scope in | Elbow load cases and mechanical requirements; motor and gearbox joint selection; shaft, bearing and housing calculations; CAD and drawings; fabrication and assembly; mechanical characterisation (backlash, repeatability, load, thermal); custom controller PCB; CAN firmware; output-encoder joint control; diagnostics and fault handling; restrained test fixture; Gates A, B and C |
| Scope out | Custom transmissions; human-interactive testing; deployment on a humanoid robot; EtherCAT; certification |
| Key deliverables | `requirements/MECHANICAL_REQUIREMENTS.md`; `mechanical/calculations/{LOAD_CASES,TORQUE_AND_SPEED,SHAFT_STRENGTH,BEARING_SELECTION,GEARBOX_SELECTION}.md`; `mechanical/cad/`, `mechanical/drawings/`, `mechanical/assembly/`; `mechanical/bom/MECHANICAL_BOM.csv`; `hardware/motor_controller/custom_pcb/`; `hardware/bom/ELECTRICAL_BOM.csv`; `firmware/communication/`, `communication/can/firmware/`; `results/{mechanical,thermal,motor_control}/`; gate records under `audit/` |
| Exit gate | Integrated actuator meets its approved A1 requirements and passes **Gate A** (design release, before fabrication), **Gate B** (bench validation) and **Gate C** (safety and release) as defined in SYSTEM_REQUIREMENTS section 9 and MILESTONE.md |
| Target weeks | Gate A end of week 5; Gate B weeks 10–11; Gate C weeks 11–12 |
| Dependencies | A0 control firmware (ACT-01-002, ACT-01-003); approved mechanical requirements (M0); component selection (M1); gearbox and bearing delivery (DEP-003, DEP-004); machining vendor (DEP-006); PCB fabrication (DEP-007); torque/load fixture (DEP-017); independent reviewers (DEP-020, DEP-021) |

### 5.4 A2: KritvaOS Integration

| Item | Content |
|---|---|
| Objective | Integrate the actuator software interface, KritvaOS driver, command and feedback path, diagnostics and system-level tests with KritvaOS Edge and Nexus, so that a host application commands the actuator, observes its state and handles reported faults correctly. |
| Lead | Project Lead / Integration Owner |
| Supporting | Electronics/Embedded Intern (CAN firmware, protocol conformance), Mechanical Intern (simulation parameters, fixture) |
| Scope in | Actuator interface contract (configure, enable, command_position, command_velocity, command_torque, read_state, read_faults, disable); `SimulatedActuator`, `CANActuator`, `DevelopmentBoardActuator`; CAN protocol specification; KritvaOS driver; host tools; simulation model; system validation and A2 demonstration on the restrained fixture |
| Scope out | `EtherCATActuator` (future); multi-joint whole-body control; physical deployment on a humanoid (needs separate safety review, SYS-REQ-085); impedance control is a goal, not an exit criterion |
| Key deliverables | `requirements/INTERFACE_REQUIREMENTS.md`; `docs/interfaces/` interface and unit-convention documents; `communication/can/protocol/`; `software/{actuator_interface,kritva_driver,host_tools,simulation}/`; `tests/integration/`; `results/integration/` |
| Exit gate | Host commands the actuator through the interface, observes state and handles faults (timeout, invalid command, injected faults) as specified; F3 and F4 closed (MILESTONE.md section 7) |
| Target weeks | Interface contract weeks 1–3; simulation from week 3; host-controlled actuator week 9; A2 demonstration week 12 |
| Dependencies | KritvaOS Edge readiness (DEP-022); CAN firmware (ACT-01-006); CAN adapter for the host (DEP-012); A1 hardware or development-board fallback |

### 5.5 Milestone dependency chain

```
ACT-01-001 (E0/F0) ----> ACT-01-002 (dev board, FOC) ----> ACT-01-003 (encoder, joint ctrl) --> A0 exit (wk 6)
                                   |                                    |
ACT-02-001 (M0) --> ACT-02-002 (M1, joint motor/gearbox selection) <----+
                                   |
                         ACT-02-003 + ACT-02-004 (M2) --> Gate A (wk 5) --> ACT-02-005 (fab/assy)
                                                                                |
ACT-01-005 (custom PCB, E2/E3) ----------------------------------------------->+--> integrated A1
ACT-01-004 (faults) + ACT-01-006 (CAN) ---------------------------------------->|
                                                                                v
                                                         ACT-02-006 (M3) --> Gate B --> Gate C (M4/E4/F4)
ACT-03-001 --> ACT-03-002 --> ACT-03-003 / ACT-03-004 ----------------------------------> ACT-03-005 (A2 demo)
```

## 6. Repository bring-up order

The repository is populated in a fixed order so that no artefact is produced before the document that governs it. ChatGPT's advice to create folders incrementally, rather than many empty ones, applies: a folder receives content when its stage starts, and its `.gitkeep` is then removed.

| Stage | Name | Content brought up | Gate that closes the stage | Weeks |
|---|---|---|---|---|
| 0 | Foundation | `LICENSE` (ACT-DEC-012); repository structure and ownership rules (ACT-DEC-011); `requirements/SYSTEM_REQUIREMENTS.md`; `planning/v1/{ROADMAP,MILESTONE,TASKS,DECISIONS,RISKS_AND_DEPENDENCIES}.md`; task workstream READMEs; `.github/` issue and PR templates; `audit/requirements_traceability/REQUIREMENTS_TRACEABILITY.csv` skeleton | Project Lead approval of planning set | 0–1 |
| 1 | Requirements | Child requirement documents: `ACTUATOR_SPECIFICATION.md`, `MECHANICAL_REQUIREMENTS.md`, `ELECTRICAL_REQUIREMENTS.md`, `FIRMWARE_REQUIREMENTS.md`, `INTERFACE_REQUIREMENTS.md`, `SAFETY_REQUIREMENTS.md`; `docs/validation/VALIDATION_PLAN.md`; `docs/architecture/SYSTEM_ARCHITECTURE.md`; `docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md` | **Mechanical requirements gate (M0)**, E0, F0; interface contract review (ACT-03-001) | 1 |
| 2 | Component selection | `mechanical/calculations/{LOAD_CASES,TORQUE_AND_SPEED,GEARBOX_SELECTION}.md`; MCU and development-board selection records; draft BOMs (`mechanical/bom/MECHANICAL_BOM.csv`, `hardware/bom/ELECTRICAL_BOM.csv`) with quotations; decision entries for ACT-DEC-004/005 and the selected motor/gearbox | M1, E1 | 2 |
| 3 | A0 implementation | `hardware/motor_controller/development_board/`; `firmware/` modules; `software/host_tools/`; `tests/firmware/`, `tests/hardware/`; `results/motor_control/` | F1, F2 (A0 scope), A0 exit review | 3–6 |
| 4 | A1 integration | `mechanical/calculations/{SHAFT_STRENGTH,BEARING_SELECTION}.md`; `mechanical/cad/`, `drawings/`, `assembly/`; `hardware/motor_controller/custom_pcb/`; `communication/can/`; `tests/mechanical/`, `tests/safety/`, `tests/performance/`; `results/{mechanical,thermal}/`; `audit/{mechanical,electronics,firmware}/` gate records | M2 → Gate A → M3/E3 → Gate B → Gate C (M4, E4, F4) | 3–12 |
| 5 | A2 integration | `software/{actuator_interface,simulation,kritva_driver}/`; `tests/integration/`; `results/integration/`; `audit/release/` | F3, F4, A2 exit review | 3–12 (interface early; integration 9–12) |

Bring-up rules:

1. No CAD for release, BOM freeze or procurement of final A1 parts before M0 has approved the mechanical requirements and acceptance criteria (SYSTEM_REQUIREMENTS section 5, design gate). Evaluation samples for A0 may be bought after M1 as **candidates**, not frozen selections.
2. No FOC current-loop tuning before the current-sensing chain has been verified on the bench (sequencing rule, TASKS.md section 7).
3. No fabrication of load-bearing parts before Gate A.
4. No loaded test before fault behaviour has been validated at low voltage with current limiting (SYS-REQ-084).
5. Every new folder that receives a real file has its `.gitkeep` deleted in the same change.

## 7. Twelve-week timeline

Week 1 is the first week of the internship. The calendar start date is **TBC** by the Project Lead and will be recorded in DECISIONS.md; all plans use relative week numbers.

### 7.1 Week table (baseline from the design conversation)

| Wk | Electronics/Embedded stream (ACT-01) | Mechanical stream (ACT-02) | Interface/integration stream (ACT-03, PL) | Joint milestone | Reviews |
|---|---|---|---|---|---|
| 1 | Study motor-control architecture; ACT-01-001 electrical and firmware requirements | Study actuator mechanics; ACT-02-001 elbow load cases and mechanical requirements | ACT-03-001 interface contract draft | **Requirements baseline** | M0, E0, F0 |
| 2 | Evaluate MCU and motor driver; dev-board selection (ACT-01-002) | Evaluate motors and gearboxes (ACT-02-002) | Interface contract review; host-tool skeleton | **Component selection** (joint motor/gearbox, PL approves) | M1, E1 |
| 3 | Motor and encoder bring-up | Initial CAD; shaft/bearing calculations start (ACT-02-003) | Interface contract baselined; simulation model start (ACT-03-004) | **Hardware feasibility** | F1 |
| 4 | Basic motor operation; custom PCB architecture start (ACT-01-005) | Housing and mounting design | CAN protocol draft (ACT-03-002) | **Initial subsystem review** | M2 (part 1) |
| 5 | FOC and current measurement; PCB schematic | Detailed CAD and drawings | CAN protocol review | **Motor-control validation**; **Gate A** | M2 (part 2), Gate A |
| 6 | Closed-loop position control; PCB layout, E2 | Fabricate parts (ACT-02-005) | Simulation validated against A0 data | **First integrated assembly**; **A0 exit** | E2, F2 (A0) |
| 7 | Tune position control (output encoder) | Integrate gearbox and encoder | Driver skeleton on `SimulatedActuator` | **Controlled joint movement** | M3 starts |
| 8 | Diagnostics and fault handling (ACT-01-004); PCB bring-up | Mechanical inspection and testing (ACT-02-006) | `DevelopmentBoardActuator` working | **Integrated prototype** | E3, F3 starts |
| 9 | Communication interface (ACT-01-006 CAN) | Mechanical improvements | `CANActuator` working; KritvaOS Edge link | **Host-controlled actuator** | F2 (A1 code) |
| 10 | Firmware robustness; fault injection | Performance characterisation | System validation test execution (ACT-03-005) | **Validation testing**; Gate B | M3 closes, F3 |
| 11 | Fix defects, regression | Fix mechanical defects | Regression on interface | **Final validation**; Gate C | M4, E4 |
| 12 | Firmware release and docs | CAD release and docs | A2 demonstration; release record | **Final demonstration**; A2 exit | F4, release |

### 7.2 Gantt view

Legend: `#` planned work, `R` review gate, `G` acceptance gate, `D` demonstration, `.` buffer / float.

```
Task / gate                         W1  W2  W3  W4  W5  W6  W7  W8  W9  W10 W11 W12
----------------------------------  --- --- --- --- --- --- --- --- --- --- --- ---
ACT-01-001 Elec/FW requirements     ###  R
ACT-01-002 Dev board + FOC bring-up      ### ### ### ###
ACT-01-003 Encoder + joint control           ### ### ### ### ###
ACT-01-004 Diagnostics + faults                          ### ### ### ###
ACT-01-005 Custom PCB (A1)                       ### ### ###R ### ### ###  .
ACT-01-006 CAN firmware (A1)                                     ### ### ###
ACT-02-001 Load cases + mech req    ###  R
ACT-02-002 Interface + gearbox cmp       ###R
ACT-02-003 Shaft/bearing/housing calc        ### ### ###
ACT-02-004 CAD + drawings                    ### ###R###R
ACT-02-005 Fabrication + assembly                        ### ###  .
ACT-02-006 Mechanical characteris.                               ### ### ### ###
ACT-03-001 Interface contract       ### ### ###
ACT-03-002 CAN protocol spec                     ### ### ### ###
ACT-03-003 Driver + host tools           ### ### ###         ### ### ### ###
ACT-03-004 Simulation model                  ### ### ### ### ###
ACT-03-005 System validation + A2                                    ### ### ### ###
Gates M0/E0/F0 | M1/E1 | F1          R   R   R
Gate A (design release)                              G
A0 exit                                                  G
Gate B (bench validation)                                            G   G
Gate C (safety and release)                                              G   G
A2 demonstration                                                             D
```

### 7.3 Joint milestones

| JM | Week | Joint milestone | Evidence of completion | Owner |
|---|---|---|---|---|
| JM-01 | 1 | Requirements baseline | Child requirement documents approved at M0/E0/F0 | Project Lead |
| JM-02 | 2 | Component selection | Joint motor/gearbox selection record (ACT-02-002 + ACT-01-002), decision entry, BOM with quotations; M1/E1 | Both interns; PL approves |
| JM-03 | 3 | Hardware feasibility | Motor spins open-loop on the dev board; initial CAD shows motor + gearbox + shaft + bearings fit | Both interns |
| JM-04 | 4 | Initial subsystem review | M2 part 1 (layout review); firmware structure review | Both interns |
| JM-05 | 5 | Motor-control validation; Gate A | Current loop verified; Gate A record in `audit/release/` | Electronics Intern; PL for Gate A |
| JM-06 | 6 | First integrated assembly; A0 exit | Motor + gearbox + shaft assembly on fixture; A0 exit record | Both interns |
| JM-07 | 7 | Controlled joint movement | Position control on the output encoder, unloaded, on the fixture | Both interns |
| JM-08 | 8 | Integrated prototype | Integrated actuator with faults handled at low voltage | Both interns |
| JM-09 | 9 | Host-controlled actuator | Host commands via `CANActuator` or `DevelopmentBoardActuator` | Project Lead |
| JM-10 | 10 | Validation testing | Gate B test execution under way | All |
| JM-11 | 11 | Final validation | Gate B passed; Gate C review | All; reviewers |
| JM-12 | 12 | Final demonstration | A2 demonstration record; release record | Project Lead |

### 7.4 Schedule buffers and slip rules

1. Weeks 11–12 are deliberately defect-fix and documentation weeks; they are the schedule buffer for Gates B and C. They are not a reserve for new features.
2. If the gearbox or motor delivery slips by more than one week (RISK-012), A0 continues on the motor alone and Gate A moves; fabrication moves with it. The PL re-baselines and records the change in DECISIONS.md.
3. If the custom PCB is not brought up by end of week 9 (RISK-008, RISK-013), A1 integration and A2 continue on the development board (section 4.4).
4. A safety-critical defect can never be treated as non-blocking to meet a deadline. If a gate cannot be passed, the gate is held and the schedule moves.

## 8. Budget roadmap

All figures are **provisional and not supplier-verified** (SYS-REQ-100). Actual cost is tracked in `mechanical/bom/MECHANICAL_BOM.csv` and `hardware/bom/ELECTRICAL_BOM.csv` with real quotations. Laboratory equipment (oscilloscope, current probe, torque fixture instrumentation) is **excluded**.

### 8.1 Milestone budgets

| Milestone | Budget (provisional) | Notes |
|---|---|---|
| A0 | ₹10,000–₹15,000 | Development board, motor, encoder parts, PSU/wiring/protection, misc |
| A1 | ₹20,000–₹30,000 **cumulative** (including A0) | Adds gearbox, bearings, shaft/housing fabrication, custom PCB, CAN parts |
| A2 | TBD | Expected to be mainly host-side (CAN adapter, cabling); to be estimated in ACT-03-001 and approved by PL |
| Post-v1 | TBD | Set per iteration in a new planning version |

### 8.2 Item targets (initial prototype)

| Item | Target (₹) | Milestone first needed | BOM home |
|---|---|---|---|
| Motor | 2,000–4,000 | A0 | `hardware/bom/ELECTRICAL_BOM.csv` (motor is shared; mechanical fit tracked in mechanical BOM by reference) |
| Planetary gearbox | 2,000–4,000 | A0 (evaluation) / A1 | `mechanical/bom/MECHANICAL_BOM.csv` |
| Development board | 3,000–5,000 | A0 | `hardware/bom/ELECTRICAL_BOM.csv` |
| Output encoder | 500–1,500 | A0/A1 | `hardware/bom/ELECTRICAL_BOM.csv` |
| Fabrication | 1,500–3,000 | A1 | `mechanical/bom/MECHANICAL_BOM.csv` |
| PSU, wiring, protection | 1,500–2,500 | A0 | `hardware/bom/ELECTRICAL_BOM.csv` |
| Miscellaneous | 1,000–2,000 | A0/A1 | Either BOM, by domain |
| **Initial prototype total** | **11,500–22,000** | | |

The custom PCB, bearings, CAN transceiver/adapter and fixture consumables must fit within the A1 cumulative envelope; if quotations show they do not, the PL records a budget decision before purchase.

### 8.3 Budget controls

1. No purchase without a BOM line carrying the exact part number, supplier and current quotation.
2. The PL approves each purchase above ₹2,000 (threshold TBC) and any purchase that would exceed the milestone envelope.
3. Spares: one spare of each low-cost, damage-prone item (gate driver, MOSFETs, encoder IC) is planned within "miscellaneous"; the motor and gearbox are not spared in v1 unless the PL approves (RISK-021).
4. Budget status is reported at every weekly review (TASKS.md section 9).

## 9. Post-v1 evolution

v1 ends at A2. The next iterations are planned in a new planning version (`planning/v2/`), not by editing v1. Every evolution step requires its own requirements, validation and gate reviews; no v1 evidence is assumed to transfer without analysis.

| Theme | Direction | Entry condition |
|---|---|---|
| Second iteration of the elbow | Improve **torque density** (N·m/kg and N·m/litre), mass and envelope against the humanoid arm budget | v1 Gate B data and mass/envelope budget (SYS-REQ-039) |
| Transmission improvements | Better planetary options (lower backlash, higher rating), improved output support and stiffness | v1 backlash, efficiency and stiffness measurements |
| Cycloidal / harmonic reconsideration | Re-examine only with **measured evidence** that the planetary gearbox limits required performance (ACT-DEC-003 deferral) | Measured shortfall in backlash, torque density or backdrivability, recorded as a new decision |
| Custom PCB refinement | Second PCB spin: integration into the housing, thermal path, connector rationalisation, improved sensing and protection | v1 E3/E4 findings |
| KritvaOS Edge integration | Deeper Edge integration: multi-joint coordination, synchronised command cycles, impedance / position + feed-forward torque modes | A2 exit; Edge roadmap |
| More joint sizes | Wrist, shoulder, hip and knee variants reusing the controller, firmware, protocol and interface; **each needs its own load cases, requirements and validation** | Approved per-joint load case |
| EtherCAT | Evaluate if multi-joint determinism or bandwidth requires it (`EtherCATActuator` behind the same interface) | Measured CAN limits in multi-joint operation |
| Human-interactive use | Only after a separate, qualified system-level safety review | SYS-REQ-083, SYS-REQ-085 |

## 10. Roadmap governance

| Activity | Frequency | Owner | Output |
|---|---|---|---|
| Weekly review | Weekly | Project Lead | Status update in `planning/v1/TASKS.md`; risk review (RISKS_AND_DEPENDENCIES.md) |
| Re-baseline | On a slip of ≥ 1 week on the critical path, or at a failed gate | Project Lead | Updated ROADMAP and a DECISIONS.md entry |
| Milestone exit review | At A0, A1, A2 exit | Project Lead with independent reviewers | Sign-off in MILESTONE.md and record in `audit/release/` |

## 11. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | Calendar start date for week 1 | Project Lead | Before week 1 |
| 2 | A2 budget estimate (host CAN adapter, cabling) | Project Lead | Week 3 |
| 3 | Purchase approval threshold (₹2,000 proposed) | Project Lead | Week 1 |
| 4 | Whether Gate C may be passed on the development-board controller if the custom PCB slips | Project Lead | Week 9 |
| 5 | Named independent reviewers (mechanical; electrical/firmware) and availability | Project Lead | Week 1 (M0) |
| 6 | KritvaOS Edge readiness date for A2 | Project Lead | Week 4 |

## 12. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
