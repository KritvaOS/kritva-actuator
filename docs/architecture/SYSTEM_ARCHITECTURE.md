# Kritva Actuator: System Architecture

| Field | Value |
|---|---|
| Document ID | KA-DOC-ARCH-SYSTEM |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer; Independent Mechanical Reviewer / Project Lead |
| Applies to | A0, A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** This architecture realises `requirements/SYSTEM_REQUIREMENTS.md`. Component choices still open (motor, gearbox, MCU family, A0 board, encoder ICs) are shown as roles, not products. Values are proposed until approved in `planning/v1/DECISIONS.md`.

---

## 1. Purpose

This document describes the Kritva Actuator **as a system**: its context within KritvaOS, its subsystems, the main data, power and mechanical flows, how the architecture evolves across A0, A1 and A2, and the key architectural decisions. The next level of detail is in:

- `ACTUATOR_ARCHITECTURE.md`: the inside of the actuator module;
- `SOFTWARE_HARDWARE_BOUNDARY.md`: which responsibilities sit in hardware, firmware and host software.

## 2. System context

```
 +------------------------------------------------------------------------------------------+
 |                                    KRITVA HUMANOID (A2)                                    |
 |                                                                                          |
 |   KritvaOS NEXUS ---- high-level planning, behaviours, perception (Linux)                |
 |        |  joint goals / trajectories                                                     |
 |        v                                                                                 |
 |   KritvaOS EDGE ----- real-time joint coordination, safety supervision, joint map        |
 |        |  CAN bus (classic CAN 1 Mbit/s baseline) - one node per actuator (node ID 1-63) |
 |        v                                                                                 |
 |   +-----------------------+   +-----------------------+   +-----------------------+      |
 |   | KRITVA ACTUATOR       |   | (future joints:       |   |  ...                  |      |
 |   | ELBOW (this project)  |   |  wrist, shoulder ...) |   |                       |      |
 |   +-----------------------+   +-----------------------+   +-----------------------+      |
 |        ^            ^                                                                    |
 |   24 V DC bus   E-stop / enable                                                          |
 +------------------------------------------------------------------------------------------+

 Bench (A0 / A1):  Linux PC (host tools, kritva_driver) --USB/UART or USB-CAN--> actuator on fixture
```

| External actor | Interaction | Interface (INTERFACE_REQUIREMENTS) |
|---|---|---|
| KritvaOS Edge | Commands, state, faults, configuration | IF-09 (CAN), IF-10 (software API), IF-11 (Edge contract) |
| Host PC (bench) | Bring-up, tuning, calibration, logging, firmware update | IF-08 (USB/UART), IF-09 (USB-CAN adapter) |
| 24 V supply (bench PSU or robot bus) | Power | IF-03 |
| E-stop / enable circuit | Hardware removal of motor power | IF-12 |
| Upper-arm structure or fixture | Mechanical mounting | IF-01 |
| Forearm or test load | Mechanical output | IF-02 |
| Operator | Lab procedures, safety | SAFETY_REQUIREMENTS |

## 3. Subsystems

| # | Subsystem | Responsibility | Owner | Repository |
|---|---|---|---|---|
| S1 | Mechanical | Motor and gearbox mounting, output shaft and bearings, housing, hard stops, encoder mounting, interfaces | Mechanical Intern | `mechanical/`, `docs/mechanical/` |
| S2 | Motor and gearbox (bought in) | Torque generation and multiplication | Both (joint selection) | BOM, `mechanical/calculations/` |
| S3 | Power electronics | 24 V input protection, 3-phase inverter, gate driver, current sensing, hardware protections | Electronics/Embedded Intern | `hardware/` |
| S4 | Sensing | Motor-side feedback, output-side absolute encoder, bus voltage, temperatures | Electronics/Embedded Intern (with Mechanical for mounting) | `hardware/sensing/`, `firmware/encoder/` |
| S5 | Embedded control | FOC, joint control, limits, state machine, diagnostics, communication | Electronics/Embedded Intern | `firmware/` |
| S6 | Communication | USB/UART protocol, CAN protocol v1, CAN tools | Project Lead (spec), Electronics Intern (firmware) | `communication/can/`, `docs/interfaces/` |
| S7 | Host software | Actuator interface, KritvaOS driver, host tools, simulation | Project Lead / Integration Owner | `software/` |
| S8 | Validation | Fixture, test procedures, evidence, traceability, audits | All, coordinated by the Project Lead | `tests/`, `results/`, `audit/` |

## 4. Main flows

### 4.1 Control and data flow (A1/A2)

```
Edge: q_cmd, v_ff, tau_ff  --CAN 500 Hz (target)-->  firmware/communication
      -> command validation and arbitration -> joint_control (position loop 1 kHz on the output encoder)
      -> velocity loop 2 kHz -> Iq* -> foc (current loop 20 kHz) -> PWM -> inverter -> motor
      -> gearbox -> output shaft -> forearm
feedback: output encoder (SPI, 1-2 kHz) + motor encoder/Halls (20 kHz) + phase currents + Vbus + temperatures
      -> diagnostics (fault manager, telemetry) -> CAN feedback frames to Edge
```

### 4.2 Power flow

```
24 V bus -> fuse -> reverse-polarity protection -> bulk capacitance -> 3-phase inverter -> motor
                                     \-> logic supplies (5 V / 3.3 V) -> MCU, sensors, CAN transceiver
regeneration: motor -> inverter -> bus (limited by firmware current limiting + clamp / brake chopper)
E-stop: removes gate-driver enable and/or opens the motor-supply contactor (hardware path)
```

### 4.3 Mechanical load flow

Torque passes through motor → gearbox → coupling → 12 mm shaft → flange → forearm. External forearm loads pass through the flange, the shaft, the dedicated bearing pair, the housing and the mount, bypassing the gearbox and motor bearings (ACT-DEC-009). The full description is in `docs/mechanical/MECHANICAL_DESIGN_SPECIFICATION.md` §3.2.

## 5. Evolution across milestones

| Element | A0: Educational Motor Control | A1: Humanoid Smart Actuator | A2: KritvaOS Integration |
|---|---|---|---|
| Mechanics | Motor on a bench fixture (no gearbox required, or the gearbox only for early tests) | Full actuator: gearbox, output shaft, bearings, housing, stops, encoder mount | Mounted in the elbow (after a separate safety review) |
| Controller | Commercial motor-control development board (ACT-DEC-005) | Custom controller PCB (development board as fallback) | Same as A1 |
| MCU | STM32G4-class proposed (ACT-DEC-004) | Same family | Same |
| Feedback | Motor-side (Halls and/or motor encoder) | Plus the output-side absolute encoder | Same |
| Communication | USB/UART | Plus CAN | CAN to Edge |
| Host | Host tools on a Linux PC | Host tools plus a USB-CAN driver | KritvaOS driver on Edge; SimulatedActuator |
| Safety | Current-limited PSU, bench e-stop relay, software protections | Hardware overcurrent, hardware e-stop input, hard stops, full fault set | Plus host joint-map checks; system-level review before robot use |

## 6. Key architectural decisions

| Decision | Summary |
|---|---|
| ACT-DEC-001 | Option C: platform → smart actuator → humanoid joint |
| ACT-DEC-002 | Level 2: buy the motor, gearbox, encoder and bearings; build the controller, firmware, mechanics and integration |
| ACT-DEC-003 | Commercial planetary gearbox; 20:1 first |
| ACT-DEC-004/005 | STM32G4-class MCU; A0 development board (both proposed) |
| ACT-DEC-006 | USB/UART for A0, CAN for A1, EtherCAT deferred |
| ACT-DEC-009/010 | Independent output shaft on bearings; output-side encoder |
| — | The MCU sits **inside** the actuator (SYS-REQ-007). Fast loops are local; Edge coordinates joints |
| — | One actuator interface with several implementations (simulated, development board, CAN) |

## 7. Quality attributes and how the architecture addresses them

| Attribute | Approach |
|---|---|
| Safety | Hardware paths for overcurrent and e-stop; firmware limits independent of the host; watchdog; balanced hard stops; restrained-fixture testing |
| Reusability ("build once, evolve") | Motor- and joint-specific parameters in configuration; HAL isolation; a reusable mounting and flange interface; one software interface |
| Testability | Host unit tests, HIL, a simulator with the same interface, fault-injection hooks in test builds, a capture buffer |
| Determinism | Interrupt-driven fixed-rate loops; no dynamic memory; communication cannot block control |
| Traceability | Requirement IDs → implementation → tests → results → audit, in the traceability CSV |
| Low cost | Commercial components; development board first; prints for non-structural parts |

## 8. Open architectural questions

| # | Question | Decision ID | Needed by |
|---|---|---|---|
| 1 | MCU family confirmation | ACT-DEC-004 | A0 start |
| 2 | Encoder ICs (motor-side and output-side) | ACT-DEC-018 | ACT-01-003 |
| 3 | Safe-state option (coast vs active damping) per fault | ACT-DEC-020 | Before loaded tests |
| 4 | CAN payload encoding | ACT-DEC-022 | F1 |
| 5 | CAN isolation and grounding in the robot | — | A1 PCB |
| 6 | Edge hardware and RTOS readiness | DEP-017 | A2 |

## 9. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
