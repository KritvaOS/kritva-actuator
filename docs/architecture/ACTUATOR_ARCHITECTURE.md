# Kritva Actuator: Actuator Module Architecture

| Field | Value |
|---|---|
| Document ID | KA-DOC-ARCH-ACTUATOR |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer; Independent Mechanical Reviewer / Project Lead |
| Applies to | A1 (A0 subset noted) |
| Classification | Proprietary and confidential |

> **Status note.** This document describes the proposed internal architecture of one actuator module. Component models are not selected. Rates and thresholds are proposed (TBC).

---

## 1. Purpose

This document decomposes the actuator module into its mechanical, electrical, sensing and firmware blocks. It defines the internal interfaces between those blocks, and shows how they are allocated to the repository folders and owners. The system-level context is in `SYSTEM_ARCHITECTURE.md`.

## 2. Block diagram

```
                     +---------------------------- ACTUATOR MODULE -----------------------------+
 24 V  ----------->  | [P1] Input protection: fuse, reverse polarity, TVS, bulk C               |
 E-stop/enable --->  | [P2] Logic power: 24 V -> 5 V -> 3.3 V                                   |
                     |                                                                          |
 CAN  <----------->  | [C1] CAN transceiver --+                                                 |
 USB/UART <------->  | [C2] USB/UART ---------+--> [M1] MCU (STM32G4-class, proposed)           |
                     |                              | PWM x6 (complementary, dead time)          |
                     |                              | ADC (phase currents, Vbus, NTCs)           |
                     |                              | SPI/ABI (encoders), FDCAN, UART/USB, WDG   |
                     |                              v                                            |
                     | [P3] Gate driver (enable from the e-stop chain) --> [P4] 3-phase inverter |
                     |        ^ nFAULT                                           |  phase U V W  |
                     | [S1] Current sensing (shunts + amplifiers) <--------------+               |
                     | [S2] HW overcurrent comparator --> MCU PWM break input                    |
                     |                                                           v               |
                     | [D1] BLDC/PMSM motor  <-- [S3] motor-side feedback (Halls / magnet+IC)    |
                     |        |                                                                 |
                     | [D2] commercial planetary gearbox (20:1 candidate)                       |
                     |        |                                                                 |
                     | [D3] coupling -> [D4] 12 mm shaft on bearing pair -> [D5] output flange   |
                     |                          |  magnet                                       |
                     |                  [S4] output absolute encoder (stationary PCB)  --SPI--> MCU
                     | [D6] balanced hard stops + bumpers         [S5] NTCs: board, MOSFET, motor|
                     +--------------------------------------------------------------------------+
```

## 3. Block allocation

| Block | Description | Requirements | Owner | Repository location |
|---|---|---|---|---|
| P1 | Input protection | ELEC-REQ power input; SAF-REQ-033/034 | Electronics/Embedded Intern | `hardware/power_stage/` |
| P2 | Logic power | ELEC-REQ | Electronics/Embedded Intern | `hardware/motor_controller/` |
| P3/P4 | Gate driver and inverter | ELEC-REQ power stage | Electronics/Embedded Intern | `hardware/power_stage/` |
| S1/S2 | Current sensing; hardware overcurrent | ELEC-REQ current sensing; SAF-REQ-030 | Electronics/Embedded Intern | `hardware/sensing/` |
| S3 | Motor-side feedback | CTRL-REQ-014 | Electronics/Embedded Intern | `hardware/sensing/`, `firmware/encoder/` |
| S4 | Output encoder | SYS-REQ-024; ACT-DEC-010 | Electronics (electrical), Mechanical (mount) | `hardware/sensing/`, `mechanical/cad/encoder_mount/` |
| S5 | Temperature sensors | SAF-REQ-032 | Electronics/Embedded Intern | `hardware/sensing/` |
| M1 | MCU and firmware | FIRMWARE_REQUIREMENTS | Electronics/Embedded Intern | `firmware/` |
| C1/C2 | Communication hardware | ELEC-REQ communication; IF-08/09 | Electronics/Embedded Intern | `hardware/connectors/` |
| D1/D2 | Motor and gearbox | ACT-DEC-003; GEARBOX_SELECTION | Both (joint) | BOM |
| D3–D6 | Coupling, shaft, bearings, flange, stops | MECHANICAL_REQUIREMENTS | Mechanical Intern | `mechanical/` |

## 4. Firmware architecture overview

The full description is in `docs/firmware/FIRMWARE_ARCHITECTURE.md`.

| Layer / module | Responsibility | Rate |
|---|---|---|
| `platform/` | HAL: clocks, PWM, ADC triggers, SPI, FDCAN, UART/USB, flash/NVM, watchdog, GPIO | — |
| `foc/` | Clarke/Park, PI current controllers, SVPWM, voltage limiting | 20 kHz |
| `encoder/` | Motor and output encoder drivers, validity checks, angle and velocity estimation | 20 kHz / 1–2 kHz |
| `motor_control/` | Motor parameters, calibration routines, torque estimate, I²t | 1–20 kHz |
| `joint_control/` | Position and velocity loops, trajectory limiter, soft limits, gravity feed-forward | 1–2 kHz |
| `diagnostics/` | Fault manager, state machine, telemetry, logs, counters, watchdog supervision | 1 kHz |
| `communication/` | USB/UART CLI and binary protocol; CAN protocol v1 | Event-driven |

## 5. Internal interfaces

| Internal interface | Between | Signals | Defined in |
|---|---|---|---|
| II-01 | MCU ↔ gate driver | 6 PWM, enable, nFAULT, (SPI configuration if a smart driver is used) | ELECTRICAL_REQUIREMENTS |
| II-02 | Shunt amplifiers ↔ MCU ADC | 2–3 phase currents, synchronous sampling | ELECTRICAL_REQUIREMENTS |
| II-03 | Comparator ↔ MCU break input | Overcurrent trip | ELECTRICAL_REQUIREMENTS; SAF-REQ-030 |
| II-04 | Motor encoder or Halls ↔ MCU | SPI or ABI / 3 Hall lines | INTERFACE_REQUIREMENTS IF-06 |
| II-05 | Output encoder ↔ MCU | SPI (cable from the stationary encoder PCB) | INTERFACE_REQUIREMENTS IF-07 |
| II-06 | NTCs ↔ MCU ADC | Board, MOSFET, motor temperatures | ELECTRICAL_REQUIREMENTS |
| II-07 | E-stop chain ↔ gate-driver enable and MCU input | Hardware enable plus a monitored input | SAFETY_REQUIREMENTS SAF-REQ-055 |
| II-08 | Gearbox output ↔ shaft | Coupling | MECHANICAL_DESIGN_SPECIFICATION |

## 6. A0 subset

A0 uses a commercial development board, which replaces P1–P4, S1, S2 and M1. The bench provides the following:

| Function | A0 realisation |
|---|---|
| Power | Current-limited bench PSU, plus an e-stop relay in the 24 V line (SAF-REQ-058) |
| Inverter, current sensing | On the development board |
| Hardware overcurrent | The board's own, if available; otherwise a recorded limitation, with the PSU current limit as mitigation |
| Feedback | Motor Halls and/or a motor encoder |
| Mechanics | Motor clamped on a fixture; optional gearbox for early ratio and backlash checks |
| Communication | USB/UART |

## 7. Physical integration (A1)

- The controller PCB sits at the **rear** of the actuator. It is thermally coupled to the aluminium motor plate, and its connectors face the non-rotating side.
- The output encoder PCB is a small **stationary** board near the output bearing, connected by a short shielded cable that runs inside the housing.
- No cable crosses the rotating output (SAF-REQ-048).
- The mechanical envelope for the PCB is agreed between the interns (DEP-009).

## 8. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
