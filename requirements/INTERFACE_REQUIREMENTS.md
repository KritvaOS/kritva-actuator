# Kritva Actuator: Interface Requirements

| Field | Value |
|---|---|
| Document ID | KA-REQ-IF |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead / Integration Owner |
| Contributors | Mechanical Intern, Electronics/Embedded Intern |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer and Independent Mechanical Reviewer (review); Project Lead (approval) |
| Applies to | Kritva Actuator Development Platform, milestones A0, A1, A2 |
| Classification | Proprietary and confidential (see `LICENSE`) |

> **Status note.** Every numerical value, identifier layout, rate, timeout and code in this document is a **proposed target pending approval**. Values marked **TBD** are not yet determined; values marked **TBC** are proposed and must be confirmed by analysis, datasheet or test. Nothing in this document is binding until the Project Lead approves it and records the approval in `planning/v1/DECISIONS.md`.

---

## 1. Purpose

This document is the **canonical source of the interface requirements** of the Kritva Actuator. It states **what** each interface must provide and **how well**, at requirement level. It covers:

- the external mechanical interfaces (mounting to the upper arm or fixture, output to the forearm or load arm);
- the electrical power interface (24 V DC input);
- the internal motor-phase and sensor interfaces between the controller and the commercial components;
- the communication interfaces: USB/UART (A0, and debug in all phases) and CAN (A1 onwards);
- the standard actuator software interface and its implementations;
- the KritvaOS Edge/Nexus integration contract;
- versioning and compatibility, units and sign conventions, configuration parameters, diagnostics and fault reporting, the safety I/O interface and the test-fixture interface.

Detailed designs are **not** held here. They live in their own canonical documents (section 4), which must satisfy these requirements. In particular, the frame-level CAN definition belongs in `docs/interfaces/CAN_PROTOCOL.md`, and the full unit and sign definitions belong in `docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md`.

## 2. Scope

**In scope:** every interface that crosses the actuator module boundary, plus the internal interfaces between the in-house controller and the purchased motor, gearbox and encoders (Level 2 boundary, ACT-DEC-002), because those interfaces decide whether the controller can be reused with other motors (SYS-REQ-006).

**Out of scope:** the internal design of KritvaOS Edge and Nexus, robot-level power distribution and robot-level emergency-stop circuits (only the actuator's side of those interfaces is covered), EtherCAT (deferred, ACT-DEC-006), and human-interactive operation (excluded by SYS-REQ-083 and `requirements/SAFETY_REQUIREMENTS.md`).

## 3. Interface owner and RACI

| Activity | Responsible | Consulted | Approves |
|---|---|---|---|
| This document and the interface control matrix (section 7) | Project Lead / Integration Owner | Both interns | Project Lead |
| Mechanical interfaces IF-01, IF-02, IF-16, IF-17 | Mechanical Intern | Electronics/Embedded Intern (connector and PCB envelope) | Project Lead after Independent Mechanical Reviewer |
| Power, motor-phase, sensor and safety I/O interfaces IF-03 to IF-07, IF-12 | Electronics/Embedded Intern | Mechanical Intern (cable routing, encoder mounting) | Project Lead after Independent Electrical/Firmware Reviewer |
| USB/UART and CAN interfaces IF-08, IF-09 | Electronics/Embedded Intern (firmware side), Project Lead (host side) | Both | Project Lead |
| Software interface, KritvaOS contract, versioning, parameters, diagnostics IF-10, IF-11, IF-13, IF-14 | Project Lead / Integration Owner | Electronics/Embedded Intern | Project Lead |
| Test-fixture interface IF-15 | Mechanical Intern | Electronics/Embedded Intern (instrumentation) | Project Lead |

ChatGPT may be used as an independent technical reviewer for remote audits of these interfaces. It is not the sole authority for approving any safety-relevant interface (IF-03, IF-09 timeout behaviour, IF-10 enable/disable semantics, IF-12). Qualified human review is required (ACT-DEC-014).

## 4. References

| Ref | Document | Relationship |
|---|---|---|
| [R1] | `requirements/SYSTEM_REQUIREMENTS.md` | Parent (SYS-REQ IDs) |
| [R2] | `requirements/ACTUATOR_SPECIFICATION.md` | Sibling: datasheet-level performance, mass and envelope budget |
| [R3] | `requirements/MECHANICAL_REQUIREMENTS.md` | Sibling: shaft, bearing and housing requirements behind IF-01/IF-02 |
| [R4] | `requirements/ELECTRICAL_REQUIREMENTS.md` | Sibling: supply range, protection and power-stage requirements behind IF-03/IF-04 |
| [R5] | `requirements/FIRMWARE_REQUIREMENTS.md` | Sibling: control modes, loop rates, fault detection (FW-REQ, CTRL-REQ) |
| [R6] | `requirements/SAFETY_REQUIREMENTS.md` | Sibling: hazards, safe states, reaction times, e-stop function |
| [R7] | `docs/interfaces/CAN_PROTOCOL.md` | Canonical CAN frame, identifier, payload, encoding and timing definition (ACT-03-002) |
| [R8] | `docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md` | Canonical units, scaling, sign and frame conventions |
| [R9] | `docs/interfaces/ACTUATOR_INTERFACE.md` §8 | USB/UART CLI and binary framing detail |
| [R10] | `docs/interfaces/ACTUATOR_INTERFACE.md` §3–6 | Language-level API definition (signatures, types, numeric return codes, fault codes) |
| [R11] | `docs/interfaces/ACTUATOR_INTERFACE.md` §7 | Parameter table (ID, unit, range, default, access, persistence) |
| [R12] | `docs/architecture/SYSTEM_ARCHITECTURE.md` | Architecture realising these interfaces |
| [R13] | `docs/validation/VALIDATION_PLAN.md` | Verification approach and gates |
| [R14] | `planning/v1/DECISIONS.md` | ACT-DEC-002, -006, -009, -010, -013, -014, -015 |
| [R15] | `audit/requirements_traceability/REQUIREMENTS_TRACEABILITY.csv` | Traceability and verification status |
| [R16] | ISO 11898-1 / ISO 11898-2 (CAN data link and high-speed physical layer) | Guidance; edition to be confirmed |

## 5. Definitions and conventions

| Term | Definition |
|---|---|
| Interface (IF-xx) | A defined boundary between two elements across which mechanical load, power, signals, data or software calls pass. Each IF-xx has one owner and one defining document (section 7). |
| Host | Any system that commands the actuator: a PC host tool (A0), KritvaOS Edge (A1/A2) or a test script. |
| Node ID | The actuator's CAN address, 1–63. 0 is the broadcast address. |
| Function code | The 5-bit field in the upper bits of the CAN identifier that identifies the message type. |
| Command refresh | A **valid** command that resets the actuator's command-timeout timer. Invalid or rejected commands are not refreshes. |
| Safe state | As defined in [R6] section 6. Default: PWM disabled, motor coasting. |
| Output side / motor side | Quantities measured at the joint output (after the gearbox) or at the motor shaft (before the gearbox). The interface reports output-side quantities unless the name says otherwise. |
| ICD | Interface control drawing (mechanical) or interface control description (electrical/data). |

**Requirement ID format:** `IF-REQ-NNN`, range 001–199. IDs are never reused after deletion.

**Verification methods:** **T** Test, **A** Analysis/calculation, **I** Inspection/review, **D** Demonstration.

**Priority:** **M** mandatory for the milestone exit, **H** high (a deviation needs a recorded decision), **L** goal.

**Phase:** the milestone by which the requirement must be verified (A0, A1, A2).

**Evidence location** gives the canonical folder where the verifying record shall be stored. Status is tracked only in [R15], never in this document.

## 6. Interface overview

```
             +--------------------+        IF-11 (software contract)
             |  KritvaOS NEXUS    |<---------------------------------+
             +---------+----------+                                  |
                       | joint trajectories / state                  |
             +---------v----------+   IF-10 actuator API             |
             |  KritvaOS EDGE     |  (SimulatedActuator /            |
             |  + actuator driver |   DevelopmentBoardActuator /     |
             +---------+----------+   CANActuator)                   |
                       |                                             |
         IF-09 CAN (A1+)        IF-08 USB/UART (A0, debug)   PC host tool
                       |                     |                        |
 IF-03 24 V DC ===>+---v---------------------v----------------------+ |
 IF-12 E-stop  --->|  ACTUATOR CONTROLLER (MCU, gate driver, inverter) |
                   |   IF-13 parameters   IF-14 diagnostics           |
                   +---+-----------+-----------+-----------+----------+
                 IF-04 |     IF-05 |     IF-07 |     IF-06 |
                 phases|  motor fb |  motor NTC|  output encoder
                   +---v-----------v-----------v--+        |
                   |  BLDC/PMSM motor             |        |
                   +---+--------------------------+        |
                 IF-16 | motor-gearbox mount               |
                   +---v--------------------------+        |
                   |  planetary gearbox           |        |
                   +---+--------------------------+        |
                 IF-17 | gearbox output coupling           |
                   +---v--------------------------+        |
 IF-01 housing --->|  output shaft on bearing pair|--------+
 mount to upper    +---+--------------------------+
 arm or fixture        | IF-02 output flange
                       v
               forearm / load arm  (IF-15 when on the test fixture)
```

## 7. Interface control matrix

### 7.1 Interface register

| Interface ID | Name | From | To | Type | Owner | Defining document | Phase |
|---|---|---|---|---|---|---|---|
| IF-01 | Housing mount | Actuator housing | Upper-arm structure or test fixture | Mechanical (load, location) | Mechanical Intern | Mechanical ICD in the CAD release (ACT-02-004); [R3] | A1 |
| IF-02 | Output flange / shaft | Output shaft | Forearm link or load arm | Mechanical (torque, load, location) | Mechanical Intern | Mechanical ICD (ACT-02-004); [R3] | A1 |
| IF-03 | DC power input | PSU or robot 24 V bus | Actuator controller | Electrical power | Electronics/Embedded Intern | [R4]; connector pinout in `hardware/` design files | A0 |
| IF-04 | Motor phases | Inverter | Motor windings U/V/W | Electrical power (internal) | Electronics/Embedded Intern | [R4] | A0 |
| IF-05 | Motor-side feedback | Motor Hall sensors and/or motor-shaft encoder | MCU | Signal (internal) | Electronics/Embedded Intern | [R4], [R5] | A0 |
| IF-06 | Output encoder | Output-side absolute encoder | MCU | Signal (internal) | Electronics/Embedded Intern (electrical), Mechanical Intern (mounting) | [R4], [R3] | A1 (A0 if bench fixture has one) |
| IF-07 | Temperature sensing | Motor winding sensor, power-stage sensor | MCU | Signal (internal) | Electronics/Embedded Intern | [R4] | A0 |
| IF-08 | USB/UART | PC host tool | Actuator controller | Data (bidirectional) | Electronics/Embedded Intern | [R9] | A0 |
| IF-09 | CAN | KritvaOS Edge / CAN host | Actuator controller | Data (bus) | Project Lead (protocol), Electronics/Embedded Intern (firmware) | [R7] | A1 |
| IF-10 | Actuator software interface | Application / KritvaOS | Actuator driver implementation | Software API | Project Lead / Integration Owner | [R10] | A2 (A0 subset) |
| IF-11 | KritvaOS integration contract | KritvaOS Nexus | KritvaOS Edge and actuator driver | Software contract | Project Lead / Integration Owner | Section 8.10 of this document; [R12] | A2 |
| IF-12 | Safety I/O (e-stop, enable) | E-stop circuit / robot safety chain | Actuator power stage and MCU | Electrical safety signal | Electronics/Embedded Intern | [R4], [R6] | A0 (bench e-stop), A1 |
| IF-13 | Configuration parameters | Host tool / Edge | Actuator NVM and RAM | Data | Project Lead (schema), Electronics/Embedded Intern (firmware) | [R11] | A0 |
| IF-14 | Diagnostics and faults | Actuator controller | Host / Edge | Data | Project Lead (schema), Electronics/Embedded Intern (firmware) | Section 8.13; numeric codes in [R7] | A0 |
| IF-15 | Test fixture | Actuator (via IF-01, IF-02) | Restrained test fixture and instruments | Mechanical, signal | Mechanical Intern | Section 8.15; `tests/mechanical/`, `tests/safety/` | A1 |
| IF-16 | Motor to gearbox | Motor flange and shaft | Gearbox input | Mechanical (internal) | Mechanical Intern | Manufacturer drawings; [R3] | A1 |
| IF-17 | Gearbox output to output shaft | Gearbox output shaft | Independent output shaft | Mechanical torque coupling (internal) | Mechanical Intern | [R3]; `mechanical/calculations/SHAFT_STRENGTH.md` | A1 |

### 7.2 N-squared matrix

The diagonal holds the elements. An off-diagonal cell lists the interfaces from the element in the row to the element in the column. A dash means no direct interface.

| | Nexus / Edge / host | Controller (MCU + power stage) | Motor | Gearbox | Output shaft + encoder | Upper arm / fixture | Forearm / load arm | PSU + e-stop |
|---|---|---|---|---|---|---|---|---|
| **Nexus / Edge / host** | **HOST** | IF-08, IF-09 commands; IF-10/IF-11 API; IF-13 parameters | - | - | - | - | - | - |
| **Controller** | IF-08, IF-09 feedback; IF-14 diagnostics | **CTRL** | IF-04 phase power | - | - | - | - | - |
| **Motor** | - | IF-05 motor feedback; IF-07 temperature | **MOTOR** | IF-16 torque and mount | - | - | - | - |
| **Gearbox** | - | - | IF-16 reaction | **GEAR** | IF-17 torque | - | - | - |
| **Output shaft + encoder** | - | IF-06 output position | - | IF-17 reaction | **OUT** | IF-01 (via housing) bearing loads | IF-02 torque and motion | - |
| **Upper arm / fixture** | - | - | - | - | IF-01 reaction | **MOUNT** | - | - |
| **Forearm / load arm** | - | - | - | - | IF-02 load | IF-15 fixture restraint | **LOAD** | - |
| **PSU + e-stop** | - | IF-03 power; IF-12 e-stop/enable | - | - | - | - | - | **SUPPLY** |

## 8. Interface requirements

### 8.1 General

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| IF-REQ-001 | Every interface crossing the actuator boundary, and every internal interface listed in section 7.1, shall have a single owner and a single defining document recorded in the interface register. | One canonical home per artefact; avoids conflicting copies. | I | Register complete; every IF-xx has an owner and a defining document that exists in the repository at the gate. | `audit/requirements_traceability/` | SYS-REQ-104 | A0 | M |
| IF-REQ-002 | An interface change that affects another owner's element shall be approved by the Project Lead before it is implemented, and the change shall be recorded in `planning/v1/DECISIONS.md` when it alters a released interface. | Prevents silent breaking changes between workstreams. | I | Each released-interface change has a decision record and a revision of the defining document. | `planning/v1/DECISIONS.md` | SYS-REQ-037, SYS-REQ-067 | A0 | M |
| IF-REQ-003 | All interface quantities shall use the units and sign conventions of section 8.12 and [R8]. | Unit and sign errors cause unexpected motion. | I | Review of [R7], [R9], [R10], [R11] finds no quantity without a unit or with a non-conforming sign. | `audit/firmware/` | SYS-REQ-062, SYS-REQ-064 | A0 | M |
| IF-REQ-004 | The same command semantics (modes, limits, timeout, error handling) shall apply over USB/UART, CAN and every software implementation of the actuator interface. A transport may support a subset of functions, but it shall not change the meaning of a function it supports. | Host code and test results must stay valid when the transport changes from A0 to A1. | I, T | The interface conformance test suite (IF-REQ-104) passes on each transport for the functions it supports. | `tests/integration/` | SYS-REQ-006, SYS-REQ-064 | A1 | M |
| IF-REQ-005 | Interface definitions shall not depend on a specific motor, gearbox or encoder part number. Motor-specific and transmission-specific values shall be carried as configuration parameters (section 8.14). | Reuse with other motors, gearboxes and joints. | I | No part-specific constant appears in [R7] or [R10]; such values are parameters in [R11]. | `audit/firmware/` | SYS-REQ-006, SYS-REQ-037 | A1 | H |

### 8.2 Mechanical interfaces (IF-01, IF-02, IF-16, IF-17)

Numerical geometry (bolt pattern, pitch circle diameter, fastener size, spigot diameter, flange thickness) is **TBD in CAD** (ACT-02-004) and shall be recorded on the mechanical ICD. The requirements below define what the ICD must contain and what the interfaces must withstand.

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| IF-REQ-010 | The actuator housing shall provide a **mounting interface (IF-01)** to the upper-arm structure and to the test fixture, defined on a mechanical ICD with datum features, bolt pattern, fastener size and grade, thread engagement, tightening torque and locating features. Values: **TBD in CAD**. | Consistent, reusable mounting (build once, evolve). | I | ICD released at Gate A with every listed item dimensioned and toleranced. | `mechanical/` CAD release; `audit/mechanical/` (M2) | SYS-REQ-037 | A1 | M |
| IF-REQ-011 | IF-01 shall locate the actuator positively (for example by spigot and dowel pins) so that the **joint reaction torque is not carried by bolt-clamp friction alone**. | Friction-only joints slip under peak and reversing torque. | A, I | Calculation shows the locating features carry the reaction torque at the peak rating with the safety factor of IF-REQ-013; drawing shows the features. | `mechanical/calculations/`; `audit/mechanical/` | SYS-REQ-032, SYS-REQ-037 | A1 | M |
| IF-REQ-012 | The output shaft shall provide an **output interface (IF-02)** (flange or shaft end) to the forearm link and load arm, defined on the ICD with a locating spigot or bore, bolt circle, fasteners and a **positive torque-transmission feature** (key, dowels, spline or flats; choice TBD in CAD). | Torque transmission must not depend on friction alone; reusable link interface. | I | ICD released at Gate A; torque feature dimensioned. | `mechanical/` CAD release | SYS-REQ-037, SYS-REQ-030 | A1 | M |
| IF-REQ-013 | IF-01 and IF-02 shall carry, without yield or slip, the **peak output torque (25 N·m stretch target)** combined with the radial, axial and bending loads of the elbow load case ([R2], `mechanical/calculations/LOAD_CASES.md`), with a static safety factor **≥ 2 (TBC)** on yield and a fatigue check for the duty cycle (TBD). | The interface must not be the weakest link in the load path. | A | Calculation reviewed at M2 with margins ≥ the approved factor. | `mechanical/calculations/SHAFT_STRENGTH.md`, `mechanical/calculations/BEARING_SELECTION.md` | SYS-REQ-021, SYS-REQ-030, SYS-REQ-032 | A1 | M |
| IF-REQ-014 | The angular position of the IF-02 output feature relative to joint angle q = 0 (full extension) shall be defined on the ICD, with a mechanical index mark visible on the assembled actuator. | Lets the arm be assembled at a known angle and supports calibration checks. | I | Index mark present; ICD states the indexed angle and its tolerance (TBD). | `mechanical/` CAD release; `results/mechanical/` | SYS-REQ-053, SYS-REQ-023 | A1 | H |
| IF-REQ-015 | IF-01 and IF-02 patterns shall be designed for **reuse** by later actuator revisions and by the test fixture. A pattern change after Gate A shall follow IF-REQ-002. | Avoids redesign of fixtures and arm parts for each revision. | I | M2 review records the reuse intent; fixture uses the same IF-01 pattern as the arm. | `audit/mechanical/` | SYS-REQ-037 | A1 | H |
| IF-REQ-016 | The **motor-to-gearbox interface (IF-16)** shall follow the gearbox manufacturer's mounting drawing (pilot, bolt pattern, input coupling and shaft insertion depth). The motor shaft shall be used as supplied. | Commercial-part integrity; avoids modifying the motor shaft. | I | Assembly drawing references the manufacturer drawing revision; no motor shaft rework. | `mechanical/` CAD release | SYS-REQ-033, SYS-REQ-003 | A1 | M |
| IF-REQ-017 | The **gearbox-output-to-output-shaft coupling (IF-17)** shall transmit torque only. It shall not transmit the arm's radial, axial or bending loads into the gearbox output bearing beyond the manufacturer's permitted output loads, and it shall tolerate the calculated misalignment between gearbox and output-bearing axes. | Load path bypasses the gearbox (ACT-DEC-009). | A, I | Calculation shows gearbox output loads within the manufacturer rating; coupling type justified. | `mechanical/calculations/BEARING_SELECTION.md`, `mechanical/calculations/GEARBOX_SELECTION.md` | SYS-REQ-032 | A1 | M |
| IF-REQ-018 | The housing shall provide defined mounting and keep-out envelopes for the controller PCB (A1), connectors, cable exits with strain relief, and the output encoder magnet/sensor pair, agreed between both interns. | Electronics constraints must be designed into the housing, not added later (RACI: housing, Mechanical leads, Electronics gives constraints). | I | M2 review shows agreed envelopes; Electronics/Embedded Intern signs the envelope check. | `audit/mechanical/`, `audit/electronics/` | SYS-REQ-007, SYS-REQ-034 | A1 | M |
| IF-REQ-019 | Fasteners at IF-01, IF-02 and IF-17 shall have a defined **thread-locking or preload-retention method** and a witness mark for inspection after loaded tests. | Loose fasteners are a recorded hazard ([R6] HAZ-017). | I, T | Method on the drawing; witness marks intact after the loaded-cycle test. | `results/mechanical/` | SYS-REQ-092 | A1 | M |

### 8.3 Electrical power interface (IF-03)

**Informative supply-current estimate (TBC until the motor is selected).** Output power at the continuous point is 10 N·m × 4.71 rad/s ≈ 47.1 W. With assumed efficiencies of 0.85 (gearbox), 0.80 (motor, TBC) and 0.95 (controller, TBC), the combined efficiency is about 0.65, so the input power is about 73 W, or **≈ 3.0 A at 24 V** (3.6 A at 20 V). At 25 N·m and 45 RPM, the output power is ≈ 118 W, the input power ≈ 182 W, and the input current **≈ 7.6 A at 24 V** (≈ 9.1 A at 20 V). The DC input current is lower than the motor phase current (6–10 A continuous, 15–25 A peak, TBC). The two must not be confused (SYS-REQ-044).

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| IF-REQ-030 | The actuator shall accept **24 V DC nominal** at IF-03. The operating range is proposed as **20–28 V (TBC)** and the withstand voltage as **≥ 32 V including regeneration (TBC)**, as specified in [R4]. | ACT-DEC-013; robot and bench supply. | T | Actuator operates across the approved range and survives the withstand test without damage. | `results/integration/`, `tests/hardware/` | SYS-REQ-040, SYS-REQ-041 | A1 (A0 dev board within its own rating) | M |
| IF-REQ-031 | The IF-03 connector shall be **polarised and keyed** so that it cannot be mated in reverse, and the actuator shall additionally include **reverse-polarity protection** that prevents damage if reverse voltage is applied at the conductors. | Reverse connection is a common bench error. | I, T | Connector cannot be reverse-mated; reverse-voltage test at the nominal voltage with a current-limited PSU causes no damage. | `tests/hardware/`, `results/integration/` | SYS-REQ-041 | A1 | M |
| IF-REQ-032 | The IF-03 connector, contacts and wiring shall be rated for at least **10 A continuous (TBC)** and for the peak input current with margin, derived from the selected motor's Kt and the peak torque duration. The rating basis shall be recorded in [R4]. | Contacts must not overheat at peak torque. | A, I | Datasheet rating ≥ calculated peak current × 1.5 (TBC); calculation recorded. | `hardware/` design files, `hardware/bom/ELECTRICAL_BOM.csv` | SYS-REQ-044 | A1 | M |
| IF-REQ-033 | IF-03 shall be protected by an **input fuse or electronic overcurrent protection** sized above the peak operating current and below the connector and wiring rating. | Limits fire risk on a power-stage short ([R6] HAZ-003, HAZ-004). | A, T | Fuse/eFuse selection recorded; short-circuit test on a current-limited PSU shows protection operates. | `hardware/`, `results/integration/` | SYS-REQ-080 | A1 | M |
| IF-REQ-034 | The actuator shall define its **regeneration behaviour** at IF-03: either it absorbs regenerated energy internally (bus capacitance plus brake/clamp circuit) so that the bus stays below the withstand voltage, or it states the minimum sink capability required from the supply. The bench PSU shall be assumed **unable to sink current** unless proven otherwise. | Typical laboratory PSUs cannot absorb regenerated energy ([R6] HAZ-012). | A, T | Deceleration test at the worst-case approved load and speed keeps the bus below the overvoltage trip threshold. | `results/integration/` | SYS-REQ-041 | A1 | M |
| IF-REQ-035 | The actuator shall limit **inrush current** at power-up to a value that does not trip the supply protection, or shall state the required supply behaviour. | Bus capacitance can cause hot-plug sparks and supply trips. | T | Measured inrush peak recorded and within the supply and connector rating. | `results/integration/` | SYS-REQ-041 | A1 | H |
| IF-REQ-036 | IF-03 shall report the measured **bus voltage** to the controller with an accuracy of **±2 % (TBC)** for use in protections and telemetry. | Needed for over/under-voltage detection and torque-to-voltage limits. | T | Comparison with a calibrated meter across the range. | `results/integration/` | SYS-REQ-062, SYS-REQ-080 | A0 | M |
| IF-REQ-037 | Logic and power grounds shall be defined so that the **CAN and USB/UART reference grounds** are consistent with IF-03 ground, with the grounding scheme (and any isolation) documented in [R4]. | Ground loops between host PC, PSU and actuator corrupt communication and can damage ports. | I | Grounding scheme reviewed at E2. | `audit/electronics/` | SYS-REQ-060, SYS-REQ-061 | A1 | H |

### 8.4 Motor-phase and sensor internal interfaces (IF-04 to IF-07)

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| IF-REQ-040 | The **motor-phase interface (IF-04)** shall be rated for the selected motor's continuous and peak phase current (proposed **6–10 A continuous, 15–25 A peak, TBC from Kt**), with phases labelled U, V and W at both ends and the phase order recorded. | Phase order defines rotation direction and commutation. | A, I | Rating ≥ calculated currents; labelling inspected. | `hardware/`, `results/motor_control/` | SYS-REQ-044, SYS-REQ-050 | A0 | M |
| IF-REQ-041 | Any change of motor or phase wiring shall require the **commutation alignment and direction check** of IF-REQ-135 to be repeated before closed-loop operation. | Swapped phases reverse the motor and can cause runaway. | D | Calibration record exists for each motor/wiring configuration. | `results/motor_control/` | SYS-REQ-053 | A0 | M |
| IF-REQ-042 | The **motor-side feedback interface (IF-05)** shall support the selected motor's feedback (Hall sensors and/or a motor-shaft magnetic encoder) with defined supply voltage, logic levels, pull-ups, filtering and connector pinout. | FOC needs reliable rotor-angle feedback. | I, T | Signals verified on an oscilloscope over the full speed range without missed or false edges. | `results/motor_control/` | SYS-REQ-043, SYS-REQ-050 | A0 | M |
| IF-REQ-043 | The **output-encoder interface (IF-06)** shall use a digital interface with integrity information (for example SPI with parity/CRC and magnetic-field status flags; candidate ICs AS5047P / AS5048A / MT6835, verify against datasheet), so that the controller can detect an invalid reading. | Encoder failure must be detectable ([R6] HAZ-010). | I, T | Interface supports a validity indication; disconnection and magnet-removal tests are detected. | `tests/firmware/`, `results/motor_control/` | SYS-REQ-024, SYS-REQ-080 | A1 | M |
| IF-REQ-044 | The output-encoder sensor-to-magnet **air gap and radial offset** shall be defined on the mechanical ICD within the encoder datasheet limits, including shaft deflection under rated load. | Alignment under load decides position accuracy. | A, I | Calculation and inspection show the limits are met at the peak load. | `mechanical/calculations/SHAFT_STRENGTH.md`; `results/mechanical/` | SYS-REQ-034 | A1 | M |
| IF-REQ-045 | Sensor cables (IF-05, IF-06, IF-07) shall be routed separately from phase cables or shielded, with a defined maximum length (TBD), and the encoder interface clock rate shall be chosen for that length. | Phase-switching noise corrupts encoder data. | I, T | No encoder errors during a full-current, full-speed run of at least 10 min (TBC). | `results/motor_control/` | SYS-REQ-052 | A1 | H |
| IF-REQ-046 | The **temperature interface (IF-07)** shall provide at least a **power-stage temperature** measurement and, if the motor provides a winding sensor, a **motor temperature** measurement. If the motor has no winding sensor, a motor-case sensor or a thermal model shall be used and the choice recorded. | Overtemperature detection ([R6] HAZ-003, HAZ-005). | I, T | Sensor reading compared with a reference thermocouple; offset recorded. | `results/thermal/` | SYS-REQ-062, SYS-REQ-080 | A0 | M |
| IF-REQ-047 | A disconnected or shorted temperature sensor shall read as an **invalid value** that the firmware detects (not as a plausible low temperature). | An open NTC that reads cold hides overheating. | T | Open and short tests raise a sensor fault. | `tests/firmware/` | SYS-REQ-080 | A0 | M |

### 8.5 USB/UART interface (IF-08, A0 and debug)

Detail (byte layouts, command list, CRC parameters) belongs in [R9].

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| IF-REQ-050 | The actuator shall provide a USB (virtual COM) or UART interface for **commands, configuration, telemetry and debugging** in A0, and shall keep it available as a debug interface in A1 and later. | ACT-DEC-006. | D | Host tool connects and exchanges commands and telemetry. | `results/motor_control/` | SYS-REQ-060, SYS-REQ-066 | A0 | M |
| IF-REQ-051 | The default serial settings shall be **115 200 baud, 8 data bits, no parity, 1 stop bit (8N1)**, no hardware flow control. A higher rate for binary telemetry, proposed **921 600 baud (TBC, verify with the development board's USB-UART bridge)**, may be selected by command or parameter. | 115 200 8N1 works with every terminal; telemetry needs more bandwidth. | T | Both rates demonstrated without framing errors over a 10 min (TBC) run. | `results/motor_control/` | SYS-REQ-060 | A0 | M |
| IF-REQ-052 | The interface shall provide a **human-readable CLI**: ASCII, one command per line, terminated by LF (CR LF accepted), each command answered by a response line starting `OK` or `ERR <code>`, using the return codes of section 8.8. | Bring-up and teaching without special tools. | D | Every CLI command in [R9] returns a defined response; an unknown command returns `ERR`. | `tests/firmware/` | SYS-REQ-060, SYS-REQ-066 | A0 | M |
| IF-REQ-053 | The interface shall provide a **binary framed mode** for telemetry and host-tool control, with a start-of-frame marker, length, message type, sequence counter, payload and a **CRC-16 (polynomial and parameters in [R9])**. Frames with a bad CRC or length shall be discarded and counted. | Reliable machine-to-machine data at high rate. | T | Injected corrupted frames are discarded and counted; none are executed. | `tests/firmware/` | SYS-REQ-060, SYS-REQ-063 | A0 | M |
| IF-REQ-054 | Switching between CLI and binary mode shall be **explicit** (a command), and the active mode shall be reportable. Binary data shall never be interpreted as CLI input, nor CLI text as binary commands. | Prevents accidental commands from stray bytes. | T | Mode-switch test; random bytes in each mode cause no motion. | `tests/firmware/` | SYS-REQ-063 | A0 | M |
| IF-REQ-055 | The interface shall stream telemetry (position, velocity, current, bus voltage, temperatures, state, fault flags, timestamp) at **≥ 100 Hz**. | Characterisation and tuning evidence. | T | Measured telemetry rate ≥ 100 Hz with no dropped sequence numbers over 10 min (TBC). | `results/motor_control/` | SYS-REQ-062 | A0 | M |
| IF-REQ-056 | Motion commands over USB/UART shall be subject to the **same command timeout** as CAN (section 8.7, IF-REQ-070). Loss of the USB connection while enabled shall lead to the safe state. | Unplugging the cable must not leave the motor running. | T | Cable-pull test while moving: safe state within the timeout + 10 ms (TBC). | `tests/safety/`, `results/motor_control/` | SYS-REQ-063 | A0 | M |
| IF-REQ-057 | While CAN is the active command interface (A1+), USB/UART motion commands shall be **rejected** unless an explicit, logged "debug control" mode is entered with the actuator disabled. Telemetry and read-only commands remain available. | Two simultaneous command masters cause conflicting motion. | T | Motion command on USB while CAN is master returns `ERR` and causes no motion. | `tests/integration/` | SYS-REQ-061, SYS-REQ-063 | A1 | M |

### 8.6 CAN interface: physical and data link (IF-09, A1)

This section states requirements only. Frame layouts, function-code allocation, payload encoding (little-endian scaled signed integers or IEEE-754 float, chosen by the [R7] author), bit timing and sequence diagrams are defined in [R7].

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| IF-REQ-060 | The actuator shall implement **classic CAN 2.0B at 1 Mbit/s** as the v1 baseline, using **standard 11-bit identifiers** (a CAN 2.0B controller that accepts both formats; extended frames are not used in protocol v1). | ACT-DEC-006; widely supported, adequate for one to a few joints. | T | Communication at 1 Mbit/s with the Edge host and a reference CAN analyser. | `results/integration/` | SYS-REQ-061 | A1 | M |
| IF-REQ-061 | The controller hardware **should be CAN FD capable** (MCU FDCAN peripheral and an FD-rated transceiver), so that a later protocol version can move to CAN FD without a hardware change. Use of CAN FD is **TBC** and not part of protocol v1. | Headroom for multi-joint rates (see the bus-load calculation below). | I | BOM shows FD-capable MCU and transceiver, or a recorded decision not to. | `hardware/bom/ELECTRICAL_BOM.csv`; `planning/v1/DECISIONS.md` | SYS-REQ-061, SYS-REQ-006 | A1 | H |
| IF-REQ-062 | The physical layer shall be ISO 11898-2 high-speed CAN. The actuator connector shall carry at least **CAN_H, CAN_L and CAN ground (reference)**; the pinout shall be defined in [R7] and on the connector drawing. | Interoperability and a defined reference potential. | I | Pinout documented; continuity check. | `hardware/`; [R7] | SYS-REQ-061 | A1 | M |
| IF-REQ-063 | The bus shall be terminated with **120 Ω at each of the two physical ends only**. The actuator shall provide a **selectable termination** (jumper, switch or solder bridge), off by default (TBC), whose state is visible on inspection. | Correct termination is needed for 1 Mbit/s; a node in mid-bus must not terminate. | I, T | Measured resistance between CAN_H and CAN_L with power off ≈ 60 Ω on the assembled bus. | `results/integration/` | SYS-REQ-061 | A1 | M |
| IF-REQ-064 | Bit timing (sample point, synchronisation jump width) shall be defined once in [R7] and used identically by all nodes. | Mismatched sample points cause errors at 1 Mbit/s. | I, T | Error counters stay at zero over a 30 min (TBC) run at maximum bus load. | `results/integration/` | SYS-REQ-061 | A1 | M |
| IF-REQ-065 | The **11-bit identifier** shall be composed as **ID = (function code << 6) \| node ID**, with a **5-bit function code (0–31)** in bits 10–6 and a **6-bit node ID** in bits 5–0. Node IDs **1–63** address individual actuators; node ID **0 is broadcast**. | ACT-03-002 proposed scheme: lower function codes win arbitration, so priority is set by function code. | I, T | [R7] allocates function codes consistently with this layout; analyser decode matches. | [R7]; `results/integration/` | SYS-REQ-061 | A1 | M |
| IF-REQ-066 | Function-code allocation in [R7] shall assign the **lowest function codes to the highest-priority messages**. Function code 0 with node ID 0 (identifier 0x000, the highest-priority frame on the bus) shall be reserved for a **broadcast disable / stop-all command**. | Safety-relevant frames must win arbitration. | I | [R7] allocation table reviewed at F1. | `audit/firmware/` | SYS-REQ-061, SYS-REQ-063 | A1 | M |
| IF-REQ-067 | Function code **31 shall not be allocated** in protocol v1 (reserved). With node IDs 48–63 it produces identifiers 0x7F0–0x7FF, which some legacy CAN 2.0A controllers do not accept. | Avoids interoperability problems with older tools and analysers. | I | [R7] marks function code 31 reserved. | [R7] | SYS-REQ-061 | A1 | H |
| IF-REQ-068 | The node ID shall be **configurable**, stored in non-volatile memory, readable over CAN and USB/UART, and changeable only while the actuator is disabled. A factory-default node ID (TBC) shall be documented. The host shall detect **duplicate node IDs** at start-up (no two heartbeats with the same node ID). | Duplicate IDs send commands to the wrong joint ([R6] HAZ-019). | T | Node ID change persists across power cycles; duplicate-ID test is detected by the host and enabling is refused. | `tests/integration/` | SYS-REQ-061 | A1 | M |
| IF-REQ-069 | **Bus-off and error-passive** states shall be reported. Entry to bus-off while enabled shall be treated as communication loss (safe state). Automatic bus-off recovery policy (on/off, delay) shall be defined in [R7] (TBC). | A node that leaves the bus can no longer be commanded. | T | Shorting CAN_H to CAN_L while enabled leads to the safe state within the command timeout. | `tests/safety/` | SYS-REQ-063 | A1 | M |

### 8.7 CAN interface: messages, rates and timeout (IF-09, A1)

**Informative bus-load calculation.** A classic CAN data frame with an 11-bit identifier and 8 data bytes has 111 bits before stuffing plus 3 bits of interframe space; with worst-case bit stuffing it is about **135 bits**, i.e. 135 µs at 1 Mbit/s. One command frame plus one feedback frame per actuator per cycle gives:

| Cycle rate per actuator | Bits per second per actuator | Bus load per actuator | Actuators at ≤ 70 % load (TBC) |
|---|---|---|---|
| 500 Hz (target) | 2 × 135 × 500 = 135 000 | 13.5 % | 5 (with heartbeat margin) |
| 1 kHz (goal) | 2 × 135 × 1000 = 270 000 | 27 % | 2 |

Multi-frame feedback or extra diagnostics reduce these numbers. This is why CAN FD capability is preferred (IF-REQ-061). The figures are for the single-elbow v1 and are rechecked in [R7].

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| IF-REQ-070 | The actuator shall enforce a **command timeout**, default **50 ms (TBC)**, configurable within limits defined in [R11]. If no valid command refresh is received within the timeout while enabled, the actuator shall enter the safe state and report a `COMM_TIMEOUT` fault. | ACT-DEC-006 and SYS-REQ-063; runaway on comm loss ([R6] HAZ-002). | T | Stopping the host while moving: safe state reached within timeout + 1 position-loop period (TBC); fault reported. | `tests/safety/`, `results/integration/` | SYS-REQ-063 | A1 | M |
| IF-REQ-071 | The actuator shall support command and feedback exchange at **500 Hz per actuator (target)** and **1 kHz (goal)**. | Joint coordination rate for Edge. | T | Sustained rate for 30 min (TBC) with no missed feedback and bus error counters at zero. | `results/integration/` | SYS-REQ-061 | A1 | M (500 Hz), L (1 kHz) |
| IF-REQ-072 | The actuator shall transmit a **feedback frame** for every command frame received (or at a configured periodic rate), containing at least output position, output velocity, torque or q-axis current, and a compact state/fault summary. Temperatures and bus voltage may be sent at a lower rate (≥ 10 Hz, TBC). | State feedback for the joint coordinator. | T | Analyser log shows the required content at the required rates. | `results/integration/` | SYS-REQ-062 | A1 | M |
| IF-REQ-073 | **Latency** from reception of a command frame to the setpoint being applied by the joint controller shall be **≤ 1 ms (TBC)**, and from a measurement sample to the start of the feedback frame transmission **≤ 1 ms (TBC)**. | Closed-loop coordination at Edge level. | T | Measured with GPIO markers and the analyser; 99.9th percentile within limit. | `results/integration/` | SYS-REQ-061 | A1 | H |
| IF-REQ-074 | The actuator shall transmit a **heartbeat/status frame** at a fixed rate, proposed **10 Hz (TBC)**, in every state including DISABLED and FAULT, carrying the state, active fault summary and a rolling counter. | Host detects a silent or reset actuator. | T | Heartbeat present in all states; counter increments; the host detects heartbeat loss within 3 periods (TBC). | `results/integration/` | SYS-REQ-061, SYS-REQ-062 | A1 | M |
| IF-REQ-075 | Fault events shall be transmitted as an **event-driven fault frame** within **one feedback period** of detection, in addition to the fault summary in feedback and heartbeat frames. | Fast fault propagation to Edge. | T | Fault-injection tests show the fault frame within the limit. | `tests/safety/` | SYS-REQ-062, SYS-REQ-080 | A1 | M |
| IF-REQ-076 | Command frames shall carry a **rolling sequence or alive counter (TBC, subject to payload budget)**, and the actuator shall reject a command whose counter does not advance (stale or duplicated frame), counting the rejection. | Detects a stuck host that repeats the same frame. | T | Repeated-frame injection is rejected and does not refresh the timeout. | `tests/firmware/` | SYS-REQ-063 | A1 | H |
| IF-REQ-077 | **Broadcast (node ID 0)** shall be limited to functions that are safe for every node to execute at once (for example disable/stop-all, time sync, heartbeat request). Motion setpoints shall **not** be accepted by broadcast. | A broadcast setpoint would move every joint to the same value. | I, T | [R7] lists permitted broadcast functions; a broadcast setpoint is ignored and counted. | [R7]; `tests/firmware/` | SYS-REQ-063 | A1 | M |
| IF-REQ-078 | Configuration writes and other non-real-time services over CAN shall use a **request/response** pattern with an explicit acknowledgement or error code, and shall not disturb the real-time command/feedback timing beyond the latency limit of IF-REQ-073. | Mixed traffic must not starve control frames. | T | Parameter writes during 500 Hz operation keep latency within limits. | `results/integration/` | SYS-REQ-061, SYS-REQ-064 | A1 | H |
| IF-REQ-079 | [R7] shall be maintained as the single CAN definition used by the firmware, the KritvaOS driver and the host tools. A machine-readable form (for example a DBC or generated header, TBC) should be generated from it. | One canonical home; avoids divergence between firmware and driver. | I | Firmware and driver reference the same protocol revision. | [R7]; `communication/can/protocol/` | SYS-REQ-067, SYS-REQ-104 | A1 | H |

### 8.8 Standard actuator software interface (IF-10)

#### 8.8.1 Actuator state machine

| State | PWM | Accepted calls | Exit |
|---|---|---|---|
| `BOOT` | Off | read_state, read_faults | Self-test passes → `DISABLED_UNCONFIGURED` (or `DISABLED` if a valid stored configuration exists and the host has confirmed it) |
| `DISABLED_UNCONFIGURED` | Off | configure, read_state, read_faults, disable | Valid configure() → `DISABLED` |
| `DISABLED` | Off (coast) | configure, enable, read_state, read_faults, disable | enable() success → `ENABLED`; fault → `FAULT` |
| `ENABLED` (mode: POSITION, VELOCITY or TORQUE) | On | command_*, read_state, read_faults, disable | disable() → `DISABLED`; fault or timeout → `FAULT`; e-stop → `ESTOP` |
| `FAULT` | Off (safe state per [R6]) | read_state, read_faults, disable, fault acknowledgement (IF-REQ-097) | Acknowledged and cause removed → `DISABLED` |
| `ESTOP` | Power stage disabled by hardware | read_state, read_faults, disable | E-stop released **and** explicit acknowledgement → `DISABLED` (never directly to `ENABLED`) |

#### 8.8.2 Return codes

All functions return one of these codes (numeric values in [R10] and [R7]):

| Code | Meaning |
|---|---|
| `OK` | Accepted and executed (or, for commands, accepted as the new setpoint). |
| `E_INVALID_ARGUMENT` | Malformed argument: NaN, infinity, wrong type, unknown mode or parameter ID. |
| `E_OUT_OF_RANGE` | Argument finite but outside the configured limit. |
| `E_INVALID_STATE` | Call not permitted in the current state (for example a command while `DISABLED`). |
| `E_NOT_CONFIGURED` | No valid configuration. |
| `E_NOT_CALIBRATED` | Calibration data missing or invalid for the requested mode. |
| `E_FAULT_ACTIVE` | A fault is active or latched and not acknowledged. |
| `E_ESTOP_ACTIVE` | The hardware emergency stop is active. |
| `E_TIMEOUT` | No response within the call timeout (host side). |
| `E_COMM` | Transport error (CRC, bus-off, disconnected). |
| `E_UNSUPPORTED` | Function or mode not supported by this implementation or firmware version. |
| `E_VERSION_MISMATCH` | Protocol or configuration schema incompatible (section 8.11). |
| `E_CONFIG_REJECTED` | Configuration set failed validation (range, consistency or CRC). |
| `E_BUSY` | A non-real-time operation (for example NVM write) is in progress. |

#### 8.8.3 Function semantics

| Function | Preconditions | Arguments and units | Limits | Behaviour on invalid input | Timeout | Result and state change |
|---|---|---|---|---|---|---|
| `configure(config)` | State `DISABLED_UNCONFIGURED` or `DISABLED`; not `ENABLED` | Parameter set per [R11] (limits, gains, gear ratio, encoder offsets, timeout, node ID, safe-state option), schema version, CRC | Every parameter within its [R11] min/max; cross-checks (soft limits inside hard stops, torque limit ≤ rated peak) | Whole set rejected with `E_CONFIG_REJECTED` and the offending parameter ID; previous configuration kept (atomic) | Host call timeout 500 ms (TBC) including NVM write | `OK` → `DISABLED`; configuration CRC readable |
| `enable()` | State `DISABLED`; configured and calibrated; no active or unacknowledged fault; e-stop released; bus voltage in range; encoders valid | None (mode is set by the first command; see below) | - | Returns the precondition that failed (`E_NOT_CONFIGURED`, `E_NOT_CALIBRATED`, `E_FAULT_ACTIVE`, `E_ESTOP_ACTIVE`, `E_INVALID_STATE`) and stays `DISABLED` | 100 ms (TBC) | `OK` → `ENABLED` in POSITION mode **holding the measured position** (proposed; zero-torque alternative TBC in ACT-03-001); command timeout timer starts |
| `command_position(q, [v_ff], [tau_ff])` | `ENABLED` | q in rad (output), optional velocity feed-forward rad/s and torque feed-forward N·m (feed-forward is an A2 goal) | q within [q_min_soft, q_max_soft]; motion profiled within configured velocity, acceleration and torque limits | `E_INVALID_ARGUMENT` / `E_OUT_OF_RANGE`; previous valid setpoint held; **does not refresh** the command timeout | Must be refreshed within the command timeout | `OK`; mode → POSITION (bumpless: controller initialised from measured state) |
| `command_velocity(v)` | `ENABLED` | v in rad/s (output) | \|v\| ≤ v_max (configured, ≤ 4.71 rad/s nominal, TBC); position soft limits still enforced (velocity forced to zero towards a limit) | As above | As above | `OK`; mode → VELOCITY |
| `command_torque(tau)` | `ENABLED`; torque mode enabled in configuration | tau in N·m (output side; converted using Kt, gear ratio and efficiency model) | \|tau\| ≤ tau_max (configured, ≤ approved peak rating); speed limit and position soft limits still enforced | As above | As above | `OK`; mode → TORQUE. Torque is an **estimate from current** unless a torque sensor is fitted; this shall be stated in [R10] |
| `read_state()` | Any state (including `BOOT`, `FAULT`, `ESTOP`) | None | - | - | 10 ms over CAN, 50 ms over USB (TBC) | State record: timestamp, sequence, state, mode, q (rad), q̇ (rad/s), torque estimate (N·m), q-axis current (A), bus voltage (V), motor and controller temperatures (°C), fault summary, data age |
| `read_faults()` | Any state | None | - | - | As read_state | Active fault set, latched fault set, first-fault record (code, timestamp, state and key measurements), counters |
| `disable()` | **Any state; always accepted** | None | - | Never rejected; idempotent | Must take effect within 1 ms (TBC) of reception on the actuator | `OK` → `DISABLED` (or stays `FAULT`/`ESTOP`); PWM off. **Warning:** without a holding brake, the arm falls under gravity when disabled ([R6] HAZ-009) |

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| IF-REQ-080 | The actuator interface shall provide the functions **configure(), enable(), command_position(), command_velocity(), command_torque(), read_state(), read_faults() and disable()** with the semantics of section 8.8.3. | Standard interface concept agreed for the project. | I, T | [R10] defines all eight; conformance suite (IF-REQ-104) passes. | `software/`, `tests/integration/` | SYS-REQ-064 | A2 (A0 subset) | M |
| IF-REQ-081 | The actuator shall implement the state machine of section 8.8.1. Calls not permitted in a state shall return `E_INVALID_STATE` and cause no state change. | Predictable behaviour for host software. | T | State-transition test covering every state/call pair. | `tests/firmware/`, `tests/integration/` | SYS-REQ-064 | A1 | M |
| IF-REQ-082 | Every function shall return one of the codes of section 8.8.2. No function shall fail silently. | Error handling must be explicit. | T | Conformance suite triggers each code at least once. | `tests/integration/` | SYS-REQ-063, SYS-REQ-064 | A2 | M |
| IF-REQ-083 | Commands outside the configured limits shall be **rejected (`E_OUT_OF_RANGE`), not silently clamped**, and the previous valid setpoint shall be held. Independently, the firmware shall saturate all internal setpoints to the configured limits (defence in depth, [R5]). | A clamped command hides host bugs; saturation protects against firmware path errors. | T | Out-of-range command test; internal saturation verified by unit test. | `tests/unit/`, `tests/firmware/` | SYS-REQ-051, SYS-REQ-063 | A1 | M |
| IF-REQ-084 | NaN, infinity and malformed arguments shall always be rejected with `E_INVALID_ARGUMENT`, in every mode and implementation. | Floating-point garbage must never reach the controller. | T | Fuzz test with NaN/Inf/extreme values causes no motion and no state change. | `tests/unit/`, `tests/firmware/` | SYS-REQ-063 | A1 | M |
| IF-REQ-085 | **Rejected or invalid commands shall not refresh the command timeout.** | A host stuck sending invalid data must still time out to the safe state. | T | Stream of invalid commands while enabled leads to `COMM_TIMEOUT` safe state. | `tests/safety/` | SYS-REQ-063 | A1 | M |
| IF-REQ-086 | The number of rejected commands shall be counted and reported. A rejection rate above a configurable threshold (TBC) within a window (TBC) should raise a warning. | Diagnoses host or link problems. | T | Counter visible in read_faults()/diagnostics. | `tests/firmware/` | SYS-REQ-062 | A1 | H |
| IF-REQ-087 | A change of control mode by a command of a different type shall be **bumpless**: the new controller shall be initialised from the measured state so that no torque or velocity step larger than the configured limits occurs. | Mode switches must not jerk the arm. | T | Mode-switch test on the fixture shows no torque step beyond limits. | `results/integration/` | SYS-REQ-051 | A1 | H |
| IF-REQ-088 | enable() shall check all its preconditions and return the first failing one. Enabling shall never cause a step in output torque beyond the configured limit. | Unexpected motion at enable ([R6] HAZ-001). | T | Enable test at several arm angles on the fixture: no jump beyond the approved threshold (TBD). | `tests/safety/` | SYS-REQ-063, SYS-REQ-080 | A1 | M |
| IF-REQ-089 | disable() shall be **accepted in every state and from every transport and implementation**, shall be idempotent, and shall take effect within **1 ms (TBC)** of reception on the actuator. | Disable is the primary software stop. | T | Disable latency measured with GPIO marker; 1000 repetitions. | `tests/safety/` | SYS-REQ-063, SYS-REQ-080 | A1 | M |
| IF-REQ-090 | read_state() and read_faults() shall be available in **every state**, including `FAULT` and `ESTOP`, and shall not change the actuator state. | Diagnosis must be possible after a fault. | T | Calls succeed in every state. | `tests/integration/` | SYS-REQ-062 | A1 | M |
| IF-REQ-091 | Every state record shall carry a **timestamp** (actuator time base, µs resolution, TBC) and a **data age or sequence number**, so the host can detect stale data. | Control on stale data is unsafe. | T | Host detects frozen feedback within 2 feedback periods. | `tests/integration/` | SYS-REQ-062 | A1 | H |
| IF-REQ-092 | Host-side calls shall have a defined **call timeout** (section 8.8.3) and return `E_TIMEOUT` when it expires. The host driver shall not block indefinitely. | Host software must remain responsive. | T | Disconnected-actuator test returns `E_TIMEOUT` within the limit. | `tests/integration/` | SYS-REQ-064 | A2 | M |
| IF-REQ-093 | configure() shall be **atomic**: either the whole parameter set is accepted, or none of it is. Safety-relevant parameters (limits, timeout, safe-state option, node ID) shall be writable only in `DISABLED` or `DISABLED_UNCONFIGURED`. | A half-applied configuration is undefined behaviour. | T | Partially invalid set is rejected and the previous set remains active (CRC unchanged). | `tests/firmware/` | SYS-REQ-064 | A1 | M |
| IF-REQ-094 | command_torque() shall be rejected with `E_UNSUPPORTED` if torque mode is disabled in the configuration or not supported by the hardware. | Torque control only where the hardware supports it (SYS-REQ-026). | T | Test with torque mode disabled. | `tests/integration/` | SYS-REQ-026 | A1 | H |
| IF-REQ-095 | Position soft limits shall be enforced in **every** mode: in velocity and torque modes the actuator shall stop driving towards a soft limit once reached. | Torque or velocity mode must not drive into the hard stop. | T | Torque-mode test towards a limit on the fixture stops before the hard stop. | `tests/safety/` | SYS-REQ-035, SYS-REQ-051 | A1 | M |
| IF-REQ-096 | The API shall expose a **calibration service** (encoder offset capture, commutation alignment, direction check) available only through the host tool in `DISABLED`, separate from normal motion commands. | Calibration must not be triggered accidentally by an application. | D | Calibration available in the host tool and refused while enabled. | `results/motor_control/` | SYS-REQ-053 | A0 | M |
| IF-REQ-097 | A **fault-acknowledgement** function shall be provided (proposed `clear_faults()`, final name TBC in ACT-03-001). It shall succeed only when the cause is no longer present, and shall return the actuator to `DISABLED`, never to `ENABLED`. | Latched faults need explicit, deliberate recovery. | T | Acknowledge with cause present → `E_FAULT_ACTIVE`; with cause removed → `DISABLED`. | `tests/safety/` | SYS-REQ-063, SYS-REQ-080 | A1 | M |

### 8.9 Implementations behind one interface

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| IF-REQ-100 | The interface shall be implemented by **SimulatedActuator**, **DevelopmentBoardActuator** (USB/UART, A0 hardware) and **CANActuator** (A1 hardware), all behind the same abstract interface. EtherCATActuator is a future implementation and not required for v1. | Simulation-first development; host code independent of the transport. | I, D | The same host test program runs unmodified against all three implementations. | `software/`, `tests/integration/` | SYS-REQ-065 | A2 | M |
| IF-REQ-101 | **SimulatedActuator** shall reproduce the state machine, limits, timeout, return codes and fault behaviour of the real actuator, and shall use a dynamic model of the motor, gearbox and arm load (ACT-03-004) with parameters taken from the selected components. | Simulation is only useful if its failure behaviour matches the hardware. | T | Conformance suite passes on the simulator; model response compared with hardware step tests (agreement criterion TBD). | `tests/integration/`, `results/integration/` | SYS-REQ-065 | A2 | M |
| IF-REQ-102 | SimulatedActuator shall support **fault injection** (encoder fault, overcurrent, comm loss, overtemperature) through a test-only API. | Host fault-handling must be testable without hardware damage. | D | Each injectable fault produces the same fault codes as the hardware. | `tests/integration/` | SYS-REQ-065, SYS-REQ-080 | A2 | H |
| IF-REQ-103 | **DevelopmentBoardActuator** shall support the A0 subset (configure, enable, command_position/velocity/torque, read_state, read_faults, disable). In A0 without an output encoder, the gear ratio parameter shall be 1 and reported quantities shall be explicitly flagged as **motor-side**. | A0 runs on the bare motor; values must not be mistaken for joint values. | I, T | State record carries a "measurement side" flag; A0 tests pass. | `results/motor_control/` | SYS-REQ-060, SYS-REQ-064 | A0 | M |
| IF-REQ-104 | An **interface conformance test suite** shall exercise every function, state transition, return code, limit and timeout case of section 8.8, and shall be run against every implementation before each release. | Proves the three implementations are interchangeable. | T | Suite passes on all implementations at A2 exit. | `tests/integration/` | SYS-REQ-064, SYS-REQ-065 | A2 | M |
| IF-REQ-105 | Implementations shall report their **type and version** (implementation name, driver version, firmware and protocol version where applicable) through the interface. | Test records must identify what was run (SYS-REQ-103). | T | Values appear in every test log header. | `results/integration/` | SYS-REQ-067, SYS-REQ-103 | A2 | H |

### 8.10 KritvaOS Edge / Nexus integration contract (IF-11)

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| IF-REQ-110 | **KritvaOS Nexus** shall command joints only through **KritvaOS Edge**; it shall never send real-time setpoints directly to the actuator. Edge owns the real-time CAN loop and the actuator driver. | Clear real-time ownership (architecture Nexus → Edge → CAN → actuator). | I | Architecture review in [R12]; no Nexus code path to the CAN bus. | `docs/architecture/SYSTEM_ARCHITECTURE.md`; `audit/` | SYS-REQ-065 | A2 | M |
| IF-REQ-111 | Edge shall run its own **command-stream supervision**: if Nexus stops supplying trajectories, Edge shall bring the joint to a defined state (hold or disable, TBC) **before** the actuator's own timeout is relied on. The actuator timeout remains the independent last line. | Two independent supervision layers. | T | Nexus-stop test: Edge reacts within its configured time (TBD) and the actuator remains in a defined state. | `results/integration/` | SYS-REQ-063, SYS-REQ-065 | A2 | M |
| IF-REQ-112 | Edge shall propagate actuator faults to Nexus with the fault code, joint name and timestamp, and shall not re-enable a faulted actuator automatically. | Fault visibility and no hidden auto-restart. | T | Injected faults appear at Nexus; re-enable requires an explicit operator or application action. | `results/integration/` | SYS-REQ-062, SYS-REQ-065 | A2 | M |
| IF-REQ-113 | Edge shall maintain a **joint map** (joint name ↔ node ID ↔ expected firmware/protocol version ↔ configuration CRC) and shall verify it at start-up before enabling any actuator. | Prevents the wrong configuration or node from being commanded. | T | Mismatch in any field blocks enabling with `E_VERSION_MISMATCH` or `E_CONFIG_REJECTED`. | `tests/integration/` | SYS-REQ-065, SYS-REQ-067 | A2 | M |
| IF-REQ-114 | Edge shall convert between KritvaOS joint conventions and the actuator conventions of section 8.12 in one place (the driver) and shall document any offset or sign mapping per joint. | Left/right arm mirroring and offsets must not be scattered across code. | I | Single mapping table in the driver; review at A2. | `software/` | SYS-REQ-064 | A2 | H |
| IF-REQ-115 | A **time-synchronisation** mechanism between Edge and the actuators (TBC: periodic broadcast time frame or host-side timestamp correlation) shall allow feedback timestamps to be related to Edge time within **±0.5 ms (TBC)**. | Multi-joint state estimation. | T | Measured offset after synchronisation within limit. | `results/integration/` | SYS-REQ-062 | A2 | L |
| IF-REQ-116 | The A2 exit demonstration shall show a host application commanding the actuator through IF-10, observing state and handling at least the injected faults `COMM_TIMEOUT`, `ENCODER_OUTPUT_FAULT`, `OVERCURRENT` and `ESTOP_ACTIVE` correctly. | A2 exit criterion. | D | Demonstration record with logs for each fault. | `results/integration/` | SYS-REQ-064, SYS-REQ-065 | A2 | M |

### 8.11 Versioning and compatibility

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| IF-REQ-120 | The actuator shall report its **hardware revision**, **firmware version**, **protocol version**, **configuration schema version** and a **unique device identifier** (for example the MCU unique ID) over every command interface. | Compatibility management and test traceability. | T | Values readable over USB/UART and CAN. | `results/integration/` | SYS-REQ-067 | A1 | M |
| IF-REQ-121 | Firmware and host driver versions shall follow **semantic versioning MAJOR.MINOR.PATCH**, plus the source-control commit identifier and a "modified working tree" flag for development builds. | Every test must be reproducible against a known build. | I | Version string format checked in CI/release review. | `audit/firmware/`, `.github/` | SYS-REQ-067, SYS-REQ-103 | A0 | M |
| IF-REQ-122 | The protocol version shall be **MAJOR.MINOR**. A MAJOR change means incompatible frames or semantics; a MINOR change adds backward-compatible functions only. | Defined compatibility rule. | I | [R7] and [R9] revision history state the version class of each change. | [R7], [R9] | SYS-REQ-067 | A1 | M |
| IF-REQ-123 | The host shall read the actuator protocol version before enabling. A **MAJOR mismatch** shall block enabling (`E_VERSION_MISMATCH`). A higher actuator MINOR version is accepted; functions the host does not know are not used. A lower actuator MINOR version is accepted only if all functions the host needs are present. | Prevents misinterpretation of frames. | T | Version-mismatch test with a modified firmware or simulator. | `tests/integration/` | SYS-REQ-067 | A1 | M |
| IF-REQ-124 | The stored configuration shall carry its **schema version** and a **CRC**. A configuration with an unknown schema version or bad CRC shall not be used; the actuator shall stay in `DISABLED_UNCONFIGURED` and report `CONFIG_INVALID`. | Corrupt or foreign configurations must not drive the motor. | T | CRC-corruption and schema-mismatch tests. | `tests/firmware/` | SYS-REQ-067, SYS-REQ-063 | A1 | M |
| IF-REQ-125 | Hardware revision shall be **readable by firmware** (for example board ID resistors or OTP, TBC), and firmware shall refuse to enable on an unsupported hardware revision. | Prevents firmware built for one board from driving another with different current scaling. | T | Mismatched-revision test. | `tests/hardware/` | SYS-REQ-067, SYS-REQ-006 | A1 | H |

### 8.12 Units and sign conventions (summary)

The canonical definition, including scaling of integer protocol fields, is in [R8]. Summary:

| Quantity | Interface unit | Notes |
|---|---|---|
| Joint position q | rad | q = 0 at **full extension**; positive in the **flexion** direction |
| Joint velocity | rad/s | Positive in flexion |
| Joint torque | N·m (output side) | Positive torque accelerates towards flexion |
| Current | A | q-axis current; positive produces positive (flexion) torque after the direction calibration |
| Voltage | V | Bus voltage |
| Temperature | °C | Interface exception to SI base units, as agreed |
| Time | s (timestamps in µs counts, TBC) | |

**Right-hand-rule note.** The joint axis unit vector is defined in CAD so that positive flexion is a right-handed rotation about that vector. For a left and a right elbow, the axis vector points in opposite directions in the robot frame, so that **flexion stays positive on both arms**. Any conversion to a robot-frame convention is done once, in the KritvaOS driver (IF-REQ-114).

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| IF-REQ-130 | All interfaces shall use **SI units** (rad, rad/s, N·m, A, V) with °C for temperature, as defined in [R8]. Human-facing tools may display degrees and RPM, but shall convert at the display layer only. | Unit consistency. | I | Review of [R7], [R9], [R10], [R11]. | `audit/firmware/` | SYS-REQ-062 | A0 | M |
| IF-REQ-131 | Joint angle **q = 0 shall correspond to full extension**, with **positive values in the flexion direction**. | Agreed joint convention. | T | Fixture test: commanding positive velocity moves into flexion; q reads 0 ± tolerance (TBD) at the extension index. | `results/integration/` | SYS-REQ-023, SYS-REQ-053 | A1 | M |
| IF-REQ-132 | Torque, velocity and current signs shall be consistent with the position sign: positive torque and positive current produce acceleration towards positive q. | Sign errors cause positive feedback and runaway. | T | Direction-consistency test in each mode. | `results/motor_control/`, `results/integration/` | SYS-REQ-051 | A1 | M |
| IF-REQ-133 | Every reported or commanded quantity shall state whether it is **output-side or motor-side**. Motor-side quantities shall carry an explicit prefix or flag (for example `motor_velocity`). | Ratio confusion produces 20× errors. | I | [R7], [R10] naming review. | `audit/firmware/` | SYS-REQ-052 | A1 | M |
| IF-REQ-134 | Scaling of integer protocol fields (if [R7] chooses scaled integers) shall be defined with resolution and range for each field, covering at least ±2π·(range/360°) margin for position, the maximum velocity and the peak torque with headroom. | Overflow or poor resolution would corrupt commands. | A | [R7] scaling table with resolution and range checked against the limits. | [R7] | SYS-REQ-061 | A1 | M |
| IF-REQ-135 | After any motor, encoder or wiring change, a **direction and offset calibration** shall verify the sign conventions of IF-REQ-131 and IF-REQ-132 before closed-loop operation under load. | Incorrect calibration is a recorded hazard ([R6] HAZ-015). | D | Calibration record with date, firmware version and result. | `results/motor_control/` | SYS-REQ-053 | A0 | M |

### 8.13 Diagnostics and fault-reporting interface (IF-14)

**Minimum fault set** (symbolic names; numeric codes in [R7]; reaction and safe state in [R6]):

| Fault | Category |
|---|---|
| `OVERCURRENT_HW`, `OVERCURRENT_SW`, `GATE_DRIVER_FAULT` | Power stage |
| `OVERVOLTAGE`, `UNDERVOLTAGE` | Supply |
| `MOTOR_OVERTEMP`, `CONTROLLER_OVERTEMP`, `TEMP_SENSOR_FAULT` | Thermal |
| `ENCODER_OUTPUT_FAULT`, `ENCODER_MOTOR_FAULT`, `ENCODER_MISMATCH` | Feedback |
| `POSITION_LIMIT`, `VELOCITY_LIMIT`, `TRACKING_ERROR` | Motion |
| `COMM_TIMEOUT`, `CAN_BUS_OFF`, `INVALID_COMMAND_RATE` | Communication |
| `ESTOP_ACTIVE` | Safety input |
| `WATCHDOG_RESET`, `CONFIG_INVALID`, `CALIBRATION_INVALID`, `HW_REVISION_UNSUPPORTED`, `INTERNAL_ERROR` | System |

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| IF-REQ-150 | The actuator shall report at least the **minimum fault set** above, each with a unique code, a severity class (**WARNING**: no state change; **FAULT**: safe state, cleared by acknowledgement; **CRITICAL**: safe state, cleared only by power cycle, TBC) and a latching flag. | Uniform fault handling across implementations. | I, T | [R7] code table complete; each fault injectable (see [R6] fault-injection list). | [R7]; `tests/safety/` | SYS-REQ-062, SYS-REQ-080 | A1 | M |
| IF-REQ-151 | The actuator shall keep a **first-fault record** (code, timestamp, state, mode, q, velocity, current, bus voltage, temperatures) for the first fault after the last acknowledgement, readable via read_faults(). | Root-cause analysis when several faults cascade. | T | First-fault record matches the injected fault in cascade tests. | `tests/safety/` | SYS-REQ-062 | A1 | H |
| IF-REQ-152 | The actuator shall keep **fault counters** and a **reset-cause** record (power-on, watchdog, brown-out, software) that survive a watchdog reset (TBC: also a power cycle). | Detects intermittent faults and hangs. | T | Watchdog test shows `WATCHDOG_RESET` cause after restart. | `tests/firmware/` | SYS-REQ-062, SYS-REQ-080 | A1 | H |
| IF-REQ-153 | Diagnostics shall include **communication statistics**: received, rejected and CRC-error frame counts, CAN error counters and bus state. | Link-quality evidence. | T | Counters readable and consistent with analyser logs. | `results/integration/` | SYS-REQ-062 | A1 | H |
| IF-REQ-154 | **Warnings** (for example thermal derating start, bus voltage near limit) shall be reported before the corresponding fault threshold is reached, with thresholds configurable in [R11]. | Gives the host a chance to reduce load. | T | Thermal test shows warning before fault. | `results/thermal/` | SYS-REQ-062 | A1 | H |
| IF-REQ-155 | The same fault codes shall be used over USB/UART, CAN, the software interface and SimulatedActuator. | One fault vocabulary. | I, T | Conformance suite compares codes across implementations. | `tests/integration/` | SYS-REQ-062, SYS-REQ-065 | A2 | M |

### 8.14 Configuration-parameter interface (IF-13)

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| IF-REQ-140 | Each configuration parameter shall be defined in [R11] with: ID, name, unit, data type, default, minimum, maximum, access (read-only / read-write), persistence (volatile / NVM), **safety-relevant flag** and owner. | Complete, reviewable parameter definition. | I | [R11] table complete at F1 review. | [R11]; `audit/firmware/` | SYS-REQ-006, SYS-REQ-064 | A0 | M |
| IF-REQ-141 | The parameter set shall include at least: gear ratio; motor pole pairs, Kt, phase resistance/inductance (as used); encoder offsets and directions; soft position limits; velocity, acceleration, torque and current limits; command timeout; safe-state option (coast / active damping, TBC); thermal warning and fault thresholds; voltage thresholds; node ID; CAN termination state (read-only if hardware); control gains. | Motor and joint independence of the generic firmware. | I | Parameter list review. | [R11] | SYS-REQ-006 | A1 | M |
| IF-REQ-142 | Parameter writes shall be **range-checked** against [R11] and **cross-checked** (for example soft limits inside the hard stops with a margin, current limit ≤ power-stage and motor rating, torque limit ≤ approved peak). Failing writes shall be rejected with `E_CONFIG_REJECTED` and the parameter ID. | Prevents unsafe configurations ([R6] HAZ-020). | T | Out-of-range and inconsistent writes rejected. | `tests/firmware/` | SYS-REQ-051, SYS-REQ-063 | A1 | M |
| IF-REQ-143 | Safety-relevant parameters shall be writable only in `DISABLED`/`DISABLED_UNCONFIGURED`, and every change of a safety-relevant parameter shall be logged with timestamp and source interface. | Prevents limit changes during motion; audit trail. | T | Write while enabled returns `E_INVALID_STATE`; log entry present after a change. | `tests/firmware/` | SYS-REQ-063 | A1 | M |
| IF-REQ-144 | Parameters shall be stored in NVM with a **CRC and schema version** (IF-REQ-124), written atomically (for example double-buffered), and a power loss during the write shall leave a valid previous set. | NVM corruption must not create a dangerous configuration. | T | Power interruption during write test, 20 repetitions (TBC). | `tests/firmware/` | SYS-REQ-063 | A1 | H |
| IF-REQ-145 | The host tool shall be able to **export and import** the full parameter set as a text file with the schema version and CRC, so that a configuration can be stored with test records. | Test reproducibility (SYS-REQ-103). | D | Exported file attached to a test record and re-imported with an identical CRC. | `results/` | SYS-REQ-066, SYS-REQ-103 | A0 | H |

### 8.15 Safety I/O interface (IF-12)

The safety function (stop category, reaction times, restart rules) is defined in [R6]. This section defines the interface.

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| IF-REQ-160 | The actuator shall provide a **hardware emergency-stop input** that removes the drive capability of the power stage (gate-driver enable or equivalent safe-torque-off concept) **independently of the MCU firmware**. | ACT-DEC-015 and SYS-REQ-081. | T, I | With the MCU forced to command PWM, activating the input stops gate drive; schematic review at E2. | `tests/safety/`, `audit/electronics/` | SYS-REQ-081 | A1 (A0: bench e-stop on the supply, see [R6]) | M |
| IF-REQ-161 | The e-stop input shall be **fail-safe**: a normally-closed loop or energise-to-run signal, so that a broken wire, disconnected connector or loss of the signal supply stops the drive. | Wire breaks must not disable the stop. | T | Connector-pull and wire-cut tests stop the drive. | `tests/safety/` | SYS-REQ-081 | A1 | M |
| IF-REQ-162 | The e-stop state shall also be **readable by the MCU**, which shall report `ESTOP_ACTIVE`, enter `ESTOP` and keep PWM commands off. | Firmware and host must know why the motor stopped. | T | State and fault reported within one feedback period. | `tests/safety/` | SYS-REQ-062, SYS-REQ-081 | A1 | M |
| IF-REQ-163 | Release of the e-stop shall **not restart motion**. The actuator shall remain in `ESTOP`/`DISABLED` until an explicit acknowledgement and enable() sequence. | No automatic restart after a stop. | T | E-stop release test: no motion until enable(). | `tests/safety/` | SYS-REQ-080, SYS-REQ-081 | A1 | M |
| IF-REQ-164 | The safety I/O connector, its voltage level (proposed 24 V logic, TBC), pinout and the option to chain the input with a robot-level safety circuit shall be documented in [R4]. | Integration with the bench e-stop and later the robot safety chain. | I | Documented at E2. | `hardware/`; `audit/electronics/` | SYS-REQ-081 | A1 | H |
| IF-REQ-165 | An **enable/ready output or status signal** (TBC) should indicate to the host or fixture that the power stage is energised. | External indication for the fixture operator and interlocks. | I | Decision recorded. | `planning/v1/DECISIONS.md` | SYS-REQ-081 | A1 | L |

### 8.16 Test-fixture interface (IF-15)

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| IF-REQ-170 | The test fixture shall mount the actuator through the **same IF-01 pattern** as the upper-arm structure, and the load arm through the **same IF-02 pattern** as the forearm. | Fixture results must represent the arm installation. | I | M2/M3 review. | `audit/mechanical/` | SYS-REQ-037, SYS-REQ-083 | A1 | M |
| IF-REQ-171 | The fixture load arm shall provide mass-mounting positions that reproduce the design load case (1.5 kg forearm/hand equivalent at its centre of mass, 1.0 kg payload at 350 mm), with **adjustable or stepped load** for staged testing. | Gate B horizontal load and staged load increase ([R6]). | I, A | Fixture drawing shows positions; calculated torque at each step recorded. | `tests/mechanical/`; `results/mechanical/` | SYS-REQ-010, SYS-REQ-012 | A1 | M |
| IF-REQ-172 | The fixture shall restrain the load arm with **guarding** and **external catch stops** independent of the actuator's own hard stops, so that loss of torque or a shaft failure cannot release the load outside the guarded zone. | Restrained-fixture rule (ACT-DEC-015); falling arm and ejection hazards. | I, T | Safety review at M3; drop test of the load arm onto the catch stops with the actuator disabled. | `tests/safety/`, `audit/mechanical/` | SYS-REQ-083 | A1 | M |
| IF-REQ-173 | The fixture shall provide an interface for **torque measurement** (in-line torque sensor or reaction load cell, TBD) and an independent **angle reference** (TBD) for backlash, position-error and repeatability measurement. | Independent verification of encoder and torque estimates. | I | Instrument interface and calibration certificates recorded. | `results/mechanical/` | SYS-REQ-025, SYS-REQ-020 | A1 | H |
| IF-REQ-174 | The actuator shall provide a **synchronisation output** (GPIO trigger, TBC) or a timestamped event that test instruments can use to align logged data. | Aligning oscilloscope, DAQ and actuator logs. | D | Trigger visible on the oscilloscope and logged event time correlated. | `results/integration/` | SYS-REQ-103 | A1 | L |
| IF-REQ-175 | The fixture e-stop shall be wired to IF-12 and placed within reach of the operator outside the clear zone. | Safe test procedure ([R6]). | I | Pre-test checklist record. | `tests/safety/` | SYS-REQ-081, SYS-REQ-083 | A1 | M |

IF-REQ-180 to IF-REQ-199 are reserved.

## 9. Verification summary

| Interface | Requirements | Main verification activity | Gate / review |
|---|---|---|---|
| IF-01, IF-02, IF-16, IF-17 | IF-REQ-010 to 019 | Calculations, ICD review, post-load inspection | M2, M3, Gate A, Gate B |
| IF-03 | IF-REQ-030 to 037 | Supply range, reverse polarity, inrush, regeneration tests | E2, E3, Gate B |
| IF-04 to IF-07 | IF-REQ-040 to 047 | Signal integrity, calibration, sensor-fault tests | E3, F3 |
| IF-08 | IF-REQ-050 to 057 | Protocol tests, cable-pull test | A0 exit, F3 |
| IF-09 | IF-REQ-060 to 079 | Analyser logs, bus-load, latency, timeout, bus-off tests | F3, Gate C |
| IF-10 | IF-REQ-080 to 105 | Conformance suite on all implementations | F2, F3, A2 exit |
| IF-11 | IF-REQ-110 to 116 | A2 integration demonstration | A2 exit |
| Versioning, units, parameters, diagnostics | IF-REQ-120 to 155 | Review and tests | F1, F3 |
| IF-12 | IF-REQ-160 to 165 | E-stop and wire-break tests | E3, Gate C |
| IF-15 | IF-REQ-170 to 175 | Fixture safety review, drop test | M3, Gate B, Gate C |

## 10. Allocation check against the parent

| SYS-REQ | Covered by |
|---|---|
| SYS-REQ-037 | IF-REQ-002, 005, 010–015, 170 |
| SYS-REQ-060 | IF-REQ-050–055, 103 |
| SYS-REQ-061 | IF-REQ-060–079 |
| SYS-REQ-062 | IF-REQ-036, 046, 055, 072, 074, 075, 090, 091, 150–155 |
| SYS-REQ-063 | IF-REQ-053, 054, 056, 057, 069, 070, 076, 077, 083–085, 093, 097, 124, 142, 143 |
| SYS-REQ-064 | IF-REQ-004, 080–097, 104, 140 |
| SYS-REQ-065 | IF-REQ-100–102, 110–116 |
| SYS-REQ-066 | IF-REQ-050, 052, 096, 145 |
| SYS-REQ-067 | IF-REQ-079, 105, 113, 120–125 |
| Supporting: SYS-REQ-006, 024, 030–034, 040, 041, 044, 053, 080, 081, 083, 103, 104 | As listed in the Parent column |

## 11. Open items

| # | Item | Requirement | Owner | Needed by |
|---|---|---|---|---|
| 1 | IF-01 and IF-02 geometry (bolt pattern, spigot, torque feature) | IF-REQ-010, 012 | Mechanical Intern | Gate A (M2) |
| 2 | Interface safety factor and fatigue duty cycle | IF-REQ-013 | Mechanical Intern, PL approves | M2 |
| 3 | Supply operating range, withstand voltage, connector and fuse rating | IF-REQ-030–033 | Electronics/Embedded Intern | E2 / A1 PCB start |
| 4 | Regeneration handling (brake/clamp circuit or supply sink requirement) | IF-REQ-034 | Electronics/Embedded Intern | E2 |
| 5 | High-rate UART baud (921 600 TBC) and CRC-16 parameters | IF-REQ-051, 053 | Electronics/Embedded Intern | A0 bring-up |
| 6 | CAN FD adoption for a later protocol version | IF-REQ-061 | Project Lead | A1 PCB start (hardware choice) |
| 7 | Default termination state and factory-default node ID | IF-REQ-063, 068 | Electronics/Embedded Intern | F1 |
| 8 | Function-code allocation, payload encoding (scaled integer vs float), bit timing | IF-REQ-064–067, 134 | Project Lead (ACT-03-002) | F1 |
| 9 | Command timeout value (50 ms TBC), heartbeat rate (10 Hz TBC), latency limits | IF-REQ-070, 073, 074 | Project Lead | F1 |
| 10 | Bus-off auto-recovery policy | IF-REQ-069 | Project Lead | F1 |
| 11 | Alive counter in command frames (payload budget) | IF-REQ-076 | Project Lead | F1 |
| 12 | enable() initial behaviour: hold measured position (proposed) vs zero torque | Section 8.8.3, IF-REQ-088 | Project Lead (ACT-03-001) | F1 |
| 13 | Name and exact semantics of the fault-acknowledgement function (`clear_faults()` proposed) | IF-REQ-097 | Project Lead (ACT-03-001) | F1 |
| 14 | CRITICAL fault class clearing rule (power cycle) | IF-REQ-150 | Project Lead with Independent Electrical/Firmware Reviewer | F1 |
| 15 | Edge supervision reaction (hold vs disable) and time-sync method | IF-REQ-111, 115 | Project Lead | A2 |
| 16 | Hardware revision detection method | IF-REQ-125 | Electronics/Embedded Intern | E2 |
| 17 | Fixture torque and angle reference instruments | IF-REQ-173 | Mechanical Intern | M3 |
| 18 | Create the proposed documents [R9], [R10], [R11] | Section 4 | Project Lead (ACT-03-001), Electronics/Embedded Intern | F1 |

## 12. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft. |
