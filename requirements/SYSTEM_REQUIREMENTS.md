# Kritva Actuator: System Requirements

| Field | Value |
|---|---|
| Document ID | KA-REQ-SYS |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.2 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead |
| Contributors | Mechanical Intern, Electronics/Embedded Intern |
| Approver | Project Lead |
| Applies to | Kritva Actuator Development Platform, milestones A0, A1, A2 |
| Classification | Proprietary and confidential (see `LICENSE`) |

> **Status note.** Every numerical value in this document is a **proposed target pending approval**, not an accepted release specification. The values for continuous torque (10 N·m), peak torque (20–25 N·m), speed (45 RPM), gearbox ratio (20:1 first candidate) and output shaft (12 mm) may change. They depend on load calculations, component datasheets and prototype validation. They become binding only when the Project Lead approves them and records the approval in `planning/v1/DECISIONS.md`.

---

## 1. Purpose

This document is the **canonical source of what the Kritva Actuator must do** at system level. It covers:

- the actuator's mission, operating context and development milestones;
- the top-level functional, performance, physical, electrical, control, communication, safety, environmental, lifecycle and project requirements;
- how each requirement is verified, and where its evidence is kept;
- how requirements flow down to the child requirement documents.

It states **what** is required and **how well**. It does not state how the requirement is implemented. Implementation belongs in `docs/` and the engineering directories (`mechanical/`, `hardware/`, `firmware/`, `communication/`, `software/`). Implementation decisions are recorded in `planning/v1/DECISIONS.md`.

## 2. Project background

The Kritva Actuator Development Platform is a Kritvaos educational robotics R&D project. It develops an **in-house smart rotary actuator** that:

1. teaches the full actuator lifecycle (mechanical, electronics, motor-control firmware, communication, software integration and validation) to an engineering team of two interns led by a Project Lead;
2. produces a **reusable control platform**: controller hardware, FOC firmware, communication protocol, KritvaOS driver and validation framework;
3. evolves into a **humanoid elbow joint actuator** that carries a meaningful arm and payload load.

The agreed development strategy is **Option C**: *Educational motor-control platform → Smart actuator → Humanoid joint actuator*. The guiding principle is **"build once, evolve through iterations"**. The first prototype is low-cost, but its electrical interfaces, firmware structure, mechanical mounting and test framework must be reusable in later revisions. It must not be a disposable experiment.

The development level is **Level 2**. The team buys a commercial BLDC/PMSM motor, a commercial planetary gearbox, a commercial encoder and bearings. It develops in-house the housing, output-shaft assembly, motor controller, firmware, communication and KritvaOS integration. Custom motors, custom harmonic or cycloidal drives and high-voltage inverters are **out of scope** for v1.

## 3. Scope

### 3.1 In scope

- One **single-axis rotary actuator** for the **humanoid elbow** (flexion/extension).
- The commercial motor and planetary gearbox, the in-house output shaft, bearings and housing, the output-side and motor-side position sensing, and the motor controller (development board in A0, custom PCB in A1).
- Firmware (FOC, joint control, diagnostics, communication), the CAN protocol, the KritvaOS driver, host tools and simulation.
- Bench validation on a **restrained, instrumented test fixture**, and integration with Kritva Edge and KritvaOS.

### 3.2 Out of scope

- Design or manufacture of the motor itself, or of a custom precision transmission (harmonic or strain-wave, cycloidal). These are deferred per decision ACT-DEC-003.
- The humanoid arm structure beyond the actuator's mounting and output interfaces.
- Whole-body control, motion planning and robot-level power and emergency-stop circuits (only the actuator's interfaces to them are in scope).
- **Human-interactive operation.** The actuator is an **experimental device** and is not a human-safe joint. Human-interactive use needs a separate, approved safety review (SYS-REQ-083).
- Formal product certification during A0–A2.

## 4. References

| Ref | Document | Relationship |
|---|---|---|
| [R1] | `requirements/ACTUATOR_SPECIFICATION.md` | Child: datasheet-level targets and the elbow load model |
| [R2] | `requirements/MECHANICAL_REQUIREMENTS.md` | Child |
| [R3] | `requirements/ELECTRICAL_REQUIREMENTS.md` | Child |
| [R4] | `requirements/FIRMWARE_REQUIREMENTS.md` | Child |
| [R5] | `requirements/INTERFACE_REQUIREMENTS.md` | Child |
| [R6] | `requirements/SAFETY_REQUIREMENTS.md` | Child |
| [R7] | `planning/v1/ROADMAP.md`, `MILESTONE.md`, `TASKS.md` | Planning, ownership and milestones |
| [R8] | `planning/v1/DECISIONS.md` | Approved decisions (e.g. ACT-DEC-003 reduction mechanism) |
| [R9] | `planning/v1/RISKS_AND_DEPENDENCIES.md` | Risks and open dependencies |
| [R10] | `docs/architecture/SYSTEM_ARCHITECTURE.md` | Architecture realising these requirements |
| [R11] | `docs/validation/VALIDATION_PLAN.md` | Verification approach and test gates |
| [R12] | `mechanical/calculations/LOAD_CASES.md`, `TORQUE_AND_SPEED.md` | Calculations behind the numerical targets |
| [R13] | `audit/requirements_traceability/REQUIREMENTS_TRACEABILITY.csv` | Requirement → implementation → verification → evidence → audit status |

## 5. Milestones and ownership

| Milestone | Name | Objective | Lead | Exit gate |
|---|---|---|---|---|
| **A0** | Educational Motor Control | Prove motor operation, FOC, current sensing, encoder feedback, basic closed-loop control and safe bench bring-up on a **motor-control development board**. Characterise the motor's electrical and thermal limits. | Electronics/Embedded Intern | The motor is controlled repeatably on a test bench, and its control behaviour and operating limits are documented with evidence in `results/motor_control/`. |
| **A1** | Humanoid Smart Actuator | Integrate the motor, planetary gearbox, output shaft, bearings, housing, output encoder, **custom controller PCB** and CAN interface. Validate the defined elbow load case. | Mechanical Intern and Electronics/Embedded Intern, each within their workstream | The assembled actuator meets its approved A1 requirements and passes acceptance **Gates A, B and C** (section 9). |
| **A2** | KritvaOS Integration | Integrate the actuator interface, driver, command and feedback path, diagnostics and system-level tests with Kritva Edge and KritvaOS. | Project Lead / Integration Owner | A host application commands the actuator through the defined software interface, observes its state and handles reported faults correctly. |

**Design gate (before A1 procurement and fabrication).** The motor, gearbox, shaft, bearings and fabrication drawings must not be frozen until the mechanical requirements and acceptance criteria have been reviewed and approved (Gate A).

**Responsibility rule.**

- The Project Lead owns the system specification, planning and release coordination.
- The Mechanical Intern owns the mechanical design and its evidence.
- The Electronics/Embedded Intern owns the electronics and motor-control implementation.
- Independent reviewers own audit findings and verify that they are closed.
- No author may be the sole approver of their own safety-critical design. If no qualified independent reviewer is available, the review is recorded as `NOT_VERIFIED`, and the related release gate stays blocked.

## 6. Definitions and conventions

| Term | Definition |
|---|---|
| Output | The actuator's final rotating member (the 12 mm output shaft and flange) that drives the forearm. |
| Joint angle (q) | Output angle relative to the actuator housing. 0° is the fully extended elbow (sign convention in `docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md`). |
| Horizontal load case | The forearm held horizontal with payload. This orientation gives the maximum static gravity torque at the elbow. |
| Continuous torque | Output torque the actuator can deliver indefinitely at the reference ambient without exceeding any motor, controller or gearbox thermal limit. It is demonstrated by a loaded thermal test. |
| Peak torque | Output torque deliverable for a **defined duration, repetition rate and recovery period**. A peak rating without those three values is incomplete. |
| Restrained fixture | A rigid, guarded test fixture that holds the actuator and load. No person holds or wears the actuator during testing. |
| Safe state | The defined actuator state after a fault (see [R6]). |
| Shall / should / may | Mandatory / recommended / permitted. |
| TBD / TBC | To be determined / to be confirmed. |

**Requirement ID format:** `SYS-REQ-NNN`. Child documents use `ACT-REQ`, `MECH-REQ`, `ELEC-REQ`, `FW-REQ` (with `CTRL-REQ` for control behaviour), `IF-REQ` and `SAF-REQ`. IDs are never reused after deletion.

**Verification methods:** **T** Test, **A** Analysis/calculation, **I** Inspection/review, **D** Demonstration.

**Priority:** **M** mandatory for the milestone exit, **H** high (a deviation needs a recorded decision), **L** goal.

**Verification status values** (used in [R13]): `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `PASS_WITH_ACTIONS`, `FAIL`, `NOT_VERIFIED`. A requirement is never marked `PASS` just because documentation exists. It needs the specified evidence.

**Units:** SI throughout. Documents use N·m, RPM, degrees and °C. Firmware and protocol use rad, rad/s, N·m and A (see the conventions document).

## 7. System context

```
                     KRITVAOS — NEXUS (high-level computing, motion planning)
                                  |
                                  | joint commands / state
                                  v
                     KRITVAOS — EDGE (real-time joint coordination)
                                  |
                 CAN (A1+)        |        USB/UART (A0, debug in all phases)
                                  v
 24 V DC  ---->  +-----------------------------------------------+
 E-stop / -----> |              KRITVA ACTUATOR (elbow)          |
 enable          |  MCU controller: FOC, current sensing,        |
                 |  encoder processing, joint control, faults    |
                 |      |                                        |
                 |  gate driver + 3-phase inverter               |
                 |      |                                        |
                 |  BLDC/PMSM motor (+ motor-side feedback)      |
                 |      |                                        |
                 |  commercial planetary gearbox                 |
                 |      |                                        |
                 |  12 mm output shaft on dedicated bearings     |
                 |      |------> output-side encoder ------------+--> feedback
                 +------|----------------------------------------+
                        v
           forearm + hand (1.5 kg) + payload (1.0 kg @ 350 mm)
```

External interfaces:

1. Mechanical mounting to the upper-arm structure, or to the test fixture.
2. Mechanical output to the forearm or link.
3. DC power input, 24 V nominal.
4. Communication: USB/UART (A0 and debug); CAN (A1 onwards). EtherCAT may be considered later if multi-joint determinism requires it.
5. A safety input (emergency stop / enable) that removes motor power.
6. Operators and developers working at a guarded bench.

## 8. System requirements

### 8.1 Mission and configuration

| ID | Requirement | Rationale | Verif. | Phase | Prio |
|---|---|---|---|---|---|
| SYS-REQ-001 | The actuator shall provide **one rotary degree of freedom** for a **humanoid elbow joint** carrying a meaningful arm and payload load, as defined in section 8.2. | The project's target application (option C, humanoid elbow). | I | A1 | M |
| SYS-REQ-002 | The actuator shall use a **commercially available BLDC/PMSM motor**. | Level-2 approach: buy the motor, develop the control. | I | A0 | M |
| SYS-REQ-003 | For A0/A1 the actuator shall use a **commercially available planetary gearbox** with documented continuous and peak torque, efficiency, backlash, life, input-speed and permitted output-load ratings. Custom cycloidal and harmonic transmissions are deferred (ACT-DEC-003). | Reduces mechanical risk and lets the team focus on control and integration. | I | A0 | M |
| SYS-REQ-004 | Gearbox ratios **15:1, 20:1 and 25:1** shall be evaluated against the motor torque-speed curve, efficiency, backlash, backdrivability and rated input speed. **20:1 is the first evaluation candidate** and shall not be frozen until those data are available. | The ratio trades motor torque against speed, friction and backdrivability. | A, T | A1 | M |
| SYS-REQ-005 | The actuator shall use an **in-house motor controller**: a commercial motor-control development board in A0, and a custom controller PCB in A1. | Validates control on proven hardware before taking on PCB risk. | I | A0/A1 | M |
| SYS-REQ-006 | The controller hardware, firmware and software interface shall be **reusable with other suitable motors, gearboxes and housings**. Motor-specific configuration shall be separated from generic control logic. | "Build once, evolve" strategy; reuse for wrist, shoulder and other joints. | I, D | A1 | H |
| SYS-REQ-007 | The motor-control MCU shall be located **inside the actuator module**. | Lets the actuator be developed and tested on its own before robot integration. | I | A1 | H |

### 8.2 Elbow load model (design basis)

| ID | Requirement | Rationale | Verif. | Phase | Prio |
|---|---|---|---|---|---|
| SYS-REQ-010 | The design load case shall be: **forearm + hand mass 1.5 kg**, **payload 1.0 kg**, **payload centre 350 mm** from the elbow axis, and a **forearm/hand centre of mass 180 mm** from the elbow axis. | Approved elbow load selection. | I | A1 | M |
| SYS-REQ-011 | The 180 mm centre-of-mass distance is a **provisional assumption**. It shall be replaced by a value from CAD mass properties or physical measurement, and the gravity-torque calculation shall then be updated. | Stops an unverified assumption from becoming a design value. | A, I | A1 | M |
| SYS-REQ-012 | The actuator shall hold the **horizontal load case**, with a calculated static gravity torque of **T_g = 1.5·9.81·0.18 + 1.0·9.81·0.35 ≈ 6.1 N·m**, continuously without exceeding any thermal limit. | This is the minimum function of the elbow. | A, T | A1 | M |
| SYS-REQ-013 | The **required angular acceleration**, **motion duty cycle** and the **continuous horizontal holding duration** shall be defined before the motor and gearbox are frozen. | Dynamic and thermal sizing depend on these values (open item). | I | A1 | M |
| SYS-REQ-014 | If the arm must catch falling objects, absorb impacts or move aggressively, a **dynamic model and a separate shock-load specification** shall be produced. | Peak-torque values alone do not cover impacts. | A | A1 | H |

### 8.3 Performance

All values are at the output and the 24 V nominal supply, at the reference ambient, unless stated otherwise.

| ID | Requirement | Rationale | Verif. | Phase | Prio |
|---|---|---|---|---|---|
| SYS-REQ-020 | **Continuous output torque** shall be **≥ 10 N·m** (target), demonstrated thermally. | About 1.64× the 6.1 N·m static gravity torque, giving margin for friction, acceleration and modelling error. | T | A1 | M |
| SYS-REQ-021 | **Peak output torque** shall be **≥ 20 N·m** (minimum target) with a **25 N·m stretch target**, for a duration, repetition rate and recovery period that shall be defined (**TBD**). | Dynamic reserve for acceleration and disturbances. | T | A1 | M |
| SYS-REQ-022 | **Output speed** shall reach **45 RPM** (4.71 rad/s) under the defined load range, with the 45 RPM operating point demonstrated at the continuous-torque load (TBC). | Approved speed target. | T | A1 | M |
| SYS-REQ-023 | **Joint range of motion** shall be **approximately 0–120° to 0–135°**, bounded by mechanical hard stops. The final range is set by the arm geometry. | Human elbow range. | I, T | A1 | M |
| SYS-REQ-024 | **Output position** shall be measured by an **encoder on the joint/output side** of the gearbox. | Measures the true joint position, including gearbox effects. | I, T | A1 | M |
| SYS-REQ-025 | Output **position error, repeatability and gearbox backlash** shall be measured against **numerical limits approved before testing** (TBD). | Acceptance must use pre-agreed limits, not limits chosen after the results. | T | A1 | M |
| SYS-REQ-026 | The actuator shall support **closed-loop position and velocity control**, and **torque control where the hardware supports it**. | Required joint-control modes. | T | A0 (motor), A1 (joint) | M |
| SYS-REQ-027 | **Reflected inertia, backdrivability and the effect of gearbox friction on compliant/force control** shall be evaluated and recorded for each candidate ratio. | Needed for humanoid compliant control. | A, T | A1 | H |
| SYS-REQ-028 | The gearbox **efficiency** shall be documented across the intended operating range. **85 %** is used for preliminary sizing. | Motor sizing and thermal budget. | A, T | A1 | H |

### 8.4 Physical and mechanical

| ID | Requirement | Rationale | Verif. | Phase | Prio |
|---|---|---|---|---|---|
| SYS-REQ-030 | The final **output shaft** shall be an **independent shaft with a 12 mm nominal initial CAD diameter**. Torsion, bending, combined stress, fatigue, stress concentrations and deflection shall be validated before release. | The 12 mm value is a starting geometry, not a guarantee of strength. | A, I | A1 | M |
| SYS-REQ-031 | The output shaft shall be supported by a **dedicated bearing pair** in the joint housing. Bearing type, spacing, fits, preload/clearance and life shall be chosen from the load calculations. | Arm loads must not be assumed to be carried by the gearbox output bearing. | A, I | A1 | M |
| SYS-REQ-032 | External radial, axial and bending loads from the arm shall pass through the shaft, bearings and housing, **bypassing the gearbox and motor bearings**, unless their manufacturers' rated loads explicitly allow otherwise. | Protects the commercial components. | A, I | A1 | M |
| SYS-REQ-033 | The **motor shaft** shall be used as supplied (typically 5–6 mm). The **gearbox output interface** should preferably be ≥ 8 mm. | Avoids needless modification of commercial parts. | I | A0 | H |
| SYS-REQ-034 | The output encoder mounting shall keep the encoder within its alignment limits under rated load, including shaft deflection. | Position accuracy under load. | A, T | A1 | M |
| SYS-REQ-035 | The actuator shall provide **mechanical hard stops** at the ends of the joint range. | Last line of over-travel protection. | I, T | A1 | M |
| SYS-REQ-036 | The motor, gearbox, bearings and encoder should be **replaceable independently** where practical. | Serviceability for an educational prototype. | I | A1 | H |
| SYS-REQ-037 | The actuator shall present a **consistent mounting interface** and **output-shaft/flange interface**, so that later revisions and other joints can reuse the fixture and arm parts. | Reusability. | I | A1 | H |
| SYS-REQ-038 | A0/A1 mechanical parts may use **3D printing and simple machining**. Load-bearing parts (shaft, bearing seats, gearbox and motor mounts) shall be made in a material and process that are justified by calculation. | Low cost without compromising the load path. | A, I | A0/A1 | H |
| SYS-REQ-039 | Actuator **mass and envelope** budgets shall be defined from the humanoid arm layout and recorded in [R1] (TBD). | Elbow mass loads the shoulder. | I | A1 | H |

### 8.5 Electrical and power

| ID | Requirement | Rationale | Verif. | Phase | Prio |
|---|---|---|---|---|---|
| SYS-REQ-040 | The actuator shall operate from a **24 V DC nominal** supply. | Robot and bench supply standard. | T | A0 | M |
| SYS-REQ-041 | The **operating voltage range**, **maximum withstand voltage** (including regeneration) and **reverse-polarity behaviour** shall be specified in [R3] (TBD). | Supply tolerance and regenerative braking. | T | A1 | M |
| SYS-REQ-042 | The motor shall be selected for **75–100 W continuous mechanical output** at the intended operating point as the starting candidate range. It must also provide sufficient continuous torque at the calculated motor speed and enough peak torque/current for the 20–25 N·m joint peak. | Output power at 10 N·m × 45 RPM ≈ 47 W, plus gearbox, motor and controller losses and thermal margin. | A | A0 | M |
| SYS-REQ-043 | The selected motor shall have a published **torque constant** (or data to derive it), **thermal data**, **24 V compatibility** and feedback suitable for the chosen FOC implementation. | Needed for controller sizing and FOC. | I | A0 | M |
| SYS-REQ-044 | The controller power stage and current sensing shall be sized from the **motor's current requirements**, not from the 24 V supply voltage alone. | A frequent sizing error. | A | A0/A1 | M |
| SYS-REQ-045 | Bench testing shall use a **current-limited DC power supply** until protection functions are verified. | Bench safety during bring-up. | I | A0 | M |

### 8.6 Control and firmware

| ID | Requirement | Rationale | Verif. | Phase | Prio |
|---|---|---|---|---|---|
| SYS-REQ-050 | The motor shall be driven by **field-oriented control (FOC)** with **phase-current sensing**. | Smooth, efficient torque and current control. | I, T | A0 | M |
| SYS-REQ-051 | The firmware shall implement **position, velocity and current/torque control**, with **torque, speed and acceleration limits** enforced in firmware. | Safe, stable motion. | T | A0/A1 | M |
| SYS-REQ-052 | Position control shall use the **output-side encoder**. Motor-side feedback shall be used for commutation and motor-side measurement. | Accounts for transmission effects. | I, T | A1 | M |
| SYS-REQ-053 | The firmware shall provide **encoder alignment and calibration** for the motor and output encoders. | Correct commutation and absolute joint angle. | D | A0/A1 | M |
| SYS-REQ-054 | Development **may start from a proven motor-control library or reference** (for example SimpleFOC or moteus as references), progressively replaced or adapted in-house. Licences of reused code shall be compatible with Kritvaos's proprietary licence. | Reduces A0 risk; supports learning. | I | A0 | H |
| SYS-REQ-055 | The motor-control MCU shall have motor-control-grade peripherals: synchronised ADC sampling, complementary PWM with dead-time insertion, a hardware fault/break input and enough processing capacity for FOC. The MCU family (STM32G4-class or TI C2000 recommended) shall be selected and recorded in DECISIONS.md. | Not every MCU or board is suitable for FOC. | I, A | A0 | M |

### 8.7 Communication and software integration

| ID | Requirement | Rationale | Verif. | Phase | Prio |
|---|---|---|---|---|---|
| SYS-REQ-060 | The actuator shall support **USB/UART** for commands, configuration, telemetry and debugging. | A0 development. | D | A0 | M |
| SYS-REQ-061 | The actuator shall support **CAN** for real-time commands, feedback and diagnostics. | Robot multi-joint bus (A1). | D, T | A1 | M |
| SYS-REQ-062 | The actuator shall return **position, velocity, current and temperature** measurements, plus fault status. | State feedback and health monitoring. | D | A0/A1 | M |
| SYS-REQ-063 | The actuator shall detect **invalid commands** and **communication timeout**, and enter a defined safe state. | Protects against loss of link or bad commands. | T | A1 | M |
| SYS-REQ-064 | A **standard actuator interface** (configure, enable, command position/velocity/torque, read state, read faults, disable) shall be defined with precise semantics: modes, limits, timeout behaviour and error handling. | Upper layers stay independent of the motor-control implementation. | I, D | A2 | M |
| SYS-REQ-065 | A **KritvaOS actuator driver** shall integrate the actuator with Kritva Edge and KritvaOS, with simulated and hardware implementations behind the same interface. | A2 integration and simulation-first development. | D | A2 | M |
| SYS-REQ-066 | **Host tools** shall support bring-up, tuning, calibration and logging from a PC. | Development productivity. | D | A0 | H |
| SYS-REQ-067 | The communication protocol shall be **versioned**. The actuator shall report hardware, firmware and protocol versions. | Compatibility management. | D | A1 | H |

### 8.8 Safety

Detailed requirements are in [R6].

| ID | Requirement | Rationale | Verif. | Phase | Prio |
|---|---|---|---|---|---|
| SYS-REQ-080 | The actuator shall detect and safely respond to **overcurrent, overtemperature, encoder faults** and an **emergency-stop command**. Each response shall be verified by fault-injection testing. | Prevents damage and uncontrolled motion. | T | A0/A1 | M |
| SYS-REQ-081 | A **means to remove motor power** independent of normal firmware commands shall be provided. | Emergency stop. | T | A1 | M |
| SYS-REQ-082 | Mechanical **hard stops** and **pinch-point guarding** shall be reviewed. **Peak-torque and failure behaviour** shall be documented. | Mechanical safety. | I | A1 | M |
| SYS-REQ-083 | Loaded and peak-torque tests shall be performed **only on a restrained, guarded, instrumented fixture**. Testing by manually resisting the actuator, or by attaching it to a person, is prohibited. A qualified human reviewer shall approve the mechanical and electrical safety evidence **before any human-interactive testing**. | The actuator is experimental, not human-safe. | I | A0–A2 | M |
| SYS-REQ-084 | Initial testing shall be at **low voltage with current limiting**. Fault behaviour shall be validated before testing under significant mechanical load. | Staged risk reduction. | I | A0 | M |
| SYS-REQ-085 | Physical deployment on a humanoid robot shall require a **separate system-level safety review**. Passing the A2 software exit gate does not establish human-interactive safety. | Clear safety boundary. | I | A2 | M |

### 8.9 Environment and lifecycle

| ID | Requirement | Rationale | Verif. | Phase | Prio |
|---|---|---|---|---|---|
| SYS-REQ-090 | The actuator shall operate in an **indoor laboratory environment**. The ambient temperature range shall be defined in [R1] (TBD) and recorded in every test record. | Rating basis. | T | A1 | H |
| SYS-REQ-091 | **Gearbox life and bearing life** shall be checked against the intended duty cycle. | Durability. | A | A1 | H |
| SYS-REQ-092 | After loaded-cycle testing, there shall be **no unacceptable permanent deformation, loosening, bearing damage or encoder misalignment**. | Mechanical integrity. | I, T | A1 | M |

### 8.10 Project, documentation and traceability

| ID | Requirement | Rationale | Verif. | Phase | Prio |
|---|---|---|---|---|---|
| SYS-REQ-100 | The indicative budget is **₹10,000–₹15,000 for A0** and **₹20,000–₹30,000 cumulative for A1** (provisional, not supplier-verified). The actual cost shall be tracked in the BOMs with real vendor quotations. | Low-cost prototype objective. | I | A0/A1 | H |
| SYS-REQ-101 | The initial development target is **12 weeks** for the educational prototype programme. | Internship duration. | I | A0–A2 | H |
| SYS-REQ-102 | Every requirement shall have a unique ID and be traced to its implementation, verification procedure, evidence location and audit status in [R13]. | Traceability. | I | A0 | M |
| SYS-REQ-103 | **Every test record** shall identify the hardware revision, firmware version, load, supply voltage, ambient temperature, instruments and measured results. | Reproducible evidence. | I | A0 | M |
| SYS-REQ-104 | Each artefact shall have **one canonical home** in the repository. Task folders and audits link to design records and never duplicate them. | Avoids conflicting copies. | I | A0 | M |
| SYS-REQ-105 | Mechanical and electrical **BOMs** shall include exact part numbers, suppliers and current quotations, with sourcing available in India where practical. | Reproducibility and cost control. | I | A1 | M |
| SYS-REQ-106 | Independent reviews shall be performed by someone other than the design's author. Audit findings stay owned by the reviewer, who verifies their closure. | Independent verification. | I | A1 | M |
| SYS-REQ-107 | Generated build outputs and unnecessary large binaries shall not be committed. Source CAD and neutral exports for review shall be stored according to an agreed versioned approach. | Repository hygiene. | I | A0 | H |

## 9. Acceptance gates (summary)

Detailed criteria are in `docs/validation/VALIDATION_PLAN.md` and each task's `ACCEPTANCE_CRITERIA.md`.

**Gate A: Design release (before fabrication)**

1. The CAD assembly includes the motor, gearbox, shaft, bearings, housing, encoder and a representative arm/link.
2. The forearm/hand centre of mass has been measured or taken from CAD, and the gravity torque has been recalculated (SYS-REQ-011).
3. Combined bending/torsion, fatigue and deflection calculations for the shaft have been reviewed.
4. Bearing loads, life, fits, alignment and housing stiffness have been checked.
5. The gearbox continuous/peak torque, efficiency, backlash, life, input speed and output-load ratings have been confirmed from manufacturer data.
6. The mechanical BOM has exact part numbers, suppliers and current quotations.
7. The independent design audit has no unresolved critical or high-severity findings.

**Gate B: Bench validation**

1. The actuator holds the 1.5 kg arm plus 1 kg payload in the horizontal orientation.
2. The ~6.1 N·m gravity load has been independently verified with the final mass properties.
3. A 10 N·m continuous test has been run on an instrumented fixture until the thermal-stability criterion is met.
4. The peak rating has been tested at its approved duration and duty cycle.
5. Speed has been measured across the load range, including the 45 RPM point.
6. Position error, repeatability and backlash have been measured against the pre-approved limits.
7. There is no unacceptable deformation, loosening, bearing damage or encoder misalignment after testing.
8. Test records are complete (SYS-REQ-103).

**Gate C: Safety and release**

1. Current limit, overtemperature, encoder-fault and emergency-stop behaviour have been tested.
2. Hard stops and pinch-point guarding have been reviewed.
3. Peak-torque and failure behaviour have been documented.
4. Every failure and deviation has a traceable disposition.
5. A qualified reviewer has approved the safety evidence before any human-interactive testing.

## 10. Derived design basis (informative)

These figures are for consistency checks only. The requirements in section 8 are binding once approved. Preliminary sizing assumptions: 85 % gearbox efficiency, 45 RPM output, 10 N·m continuous, 25 N·m peak (stretch).

| Quantity | 15:1 | **20:1 (first candidate)** | 25:1 |
|---|---|---|---|
| Motor speed at 45 RPM output | 675 RPM | **900 RPM** | 1 125 RPM |
| Motor torque for 10 N·m output | 0.78 N·m | **0.59 N·m** | 0.47 N·m |
| Motor torque for 25 N·m output | 1.96 N·m | **1.47 N·m** | 1.18 N·m |
| Motor mechanical power at 10 N·m / 45 RPM | ≈ 55 W | **≈ 55 W** | ≈ 55 W |
| Reflected rotor inertia factor (N²) | 225 | **400** | 625 |

Other derived values:

- Output mechanical power at 10 N·m and 45 RPM: 10 × 4.71 ≈ **47.1 W**.
- Nominal torsional shear in a 12 mm solid shaft: **29.5 MPa** at 10 N·m, **58.9 MPa** at 20 N·m and **73.7 MPa** at 25 N·m. These figures exclude bending, stress concentration and fatigue.
- Approximate arm inertia about the elbow (point-mass estimate): 1.5·0.18² + 1.0·0.35² ≈ **0.17 kg·m²**. That gives ≈ **1.9 J** of kinetic energy at 45 RPM, which is the input for hard-stop design (TBC with CAD).

## 11. Flow-down to child documents

| Child document | Owner | Allocated system requirements |
|---|---|---|
| ACTUATOR_SPECIFICATION.md | Project Lead | SYS-REQ-001, 010–014, 020–028, 039, 040, 042, 090 |
| MECHANICAL_REQUIREMENTS.md | Mechanical Intern (Project Lead approves) | SYS-REQ-003, 004, 027, 030–039, 082, 091, 092 |
| ELECTRICAL_REQUIREMENTS.md | Electronics Intern (Project Lead approves) | SYS-REQ-005, 040–045, 055, 081 |
| FIRMWARE_REQUIREMENTS.md | Electronics Intern (Project Lead approves) | SYS-REQ-006, 050–054, 062, 063, 080 |
| INTERFACE_REQUIREMENTS.md | Project Lead / Integration Owner | SYS-REQ-037, 060–067 |
| SAFETY_REQUIREMENTS.md | Project Lead with independent reviewer | SYS-REQ-035, 080–085 |
| planning/v1/* and audit/* | Project Lead / reviewers | SYS-REQ-100–107 |

## 12. Open items

| # | Item | Requirement | Owner | Needed by |
|---|---|---|---|---|
| 1 | Measured or CAD forearm/hand centre of mass (replace 180 mm) | SYS-REQ-011 | Mechanical Intern | Gate A |
| 2 | Required angular acceleration, duty cycle and horizontal holding duration | SYS-REQ-013 | Project Lead | Before the motor/gearbox freeze |
| 3 | Peak torque duration, repetition rate and recovery period; adopt 20 or 25 N·m | SYS-REQ-021 | Project Lead | Before the motor/gearbox freeze |
| 4 | Final gearbox ratio (20:1 vs 15:1 / 25:1) | SYS-REQ-004 | Mechanical + Electronics Interns | After datasheet comparison |
| 5 | Position-error, repeatability and backlash limits | SYS-REQ-025 | Project Lead | Before Gate B testing |
| 6 | Mass and envelope budget | SYS-REQ-039 | Project Lead + Mechanical Intern | Gate A |
| 7 | Voltage range, withstand voltage and regeneration handling | SYS-REQ-041 | Electronics Intern | A1 PCB start |
| 8 | MCU family and A0 development board selection | SYS-REQ-055, 005 | Electronics Intern | A0 start |
| 9 | Shock-load specification, if impacts are in scope | SYS-REQ-014 | Project Lead | Gate A |
| 10 | Reference ambient temperature range | SYS-REQ-090 | Project Lead | Gate B |

## 13. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft (6–8 N·m / 60 RPM basis). |
| 0.2 | 2026-10-11 | Kritvaos Actuator Team | Aligned with the agreed project direction: Option C; commercial planetary gearbox (ACT-DEC-003); elbow load model (1.5 kg forearm/hand at 180 mm, 1 kg payload at 350 mm, T_g ≈ 6.1 N·m); 10 N·m continuous, 20–25 N·m peak, 45 RPM; 20:1 first candidate with 15:1/25:1; 75–100 W motor; independent 12 mm shaft on dedicated bearings; acceptance Gates A/B/C; roles and independent-review rule; verification status values; A0/A1 budgets; restrained-fixture testing rule. |
