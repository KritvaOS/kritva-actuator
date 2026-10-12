# Kritva Actuator: Electronics Design Audit (E0–E2)

| Field | Value |
|---|---|
| Document ID | KA-AUD-ELEC-DESIGN |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Independent Electrical/Firmware Reviewer |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A0 (E0, E1), A1 (E2) |
| Classification | Proprietary and confidential |

> **Status note.** This is the audit framework. No gate has been reviewed. The Electronics/Embedded Intern must not be the sole approver of power-stage protection or motor-control safety (ACT-DEC-014). Without a qualified reviewer, the result is `NOT VERIFIED`.

---

## 1. Purpose

This document is the independent review of the electronics requirements (E0), the board and component selection (E1), and the schematic and PCB design (E2). It verifies that the design is safe, sized from the motor current, testable and consistent with the safety and interface requirements.

## 2. Audit areas

| Area | What is verified |
|---|---|
| Supply and protection | Voltage range, withstand voltage, reverse polarity, fusing, TVS, regeneration handling |
| Power stage | MOSFET and driver ratings against the motor current with margin; dead time; layout of the power loop; thermal path |
| Current sensing | Topology, range, resolution, bandwidth, synchronous sampling, Kelvin connections |
| Hardware protection | Overcurrent comparator to PWM break; gate-driver faults; pull-downs on the gate inputs; e-stop removing gate enable; watchdog |
| Sensing interfaces | Motor feedback and output encoder: supply, signal integrity, ESD, cable |
| MCU | Peripheral set (ACT-DEC-004), clocking, debug access, hardware revision ID |
| Communication | CAN transceiver, termination, ESD, connectors; USB/UART |
| Manufacturability and test | Test points, programming, BOM availability, DFM |

## 3. Gate records

### 3.1 E0: Electrical requirements review

| Item | Value |
|---|---|
| Evidence | `requirements/ELECTRICAL_REQUIREMENTS.md`; `planning/v1/tasks/ACT-01/ACT-01-001/` |
| Reviewer / date / result | TBD / — / NOT VERIFIED |

| # | Check | Result | Comment |
|---|---|---|---|
| E0-01 | Supply range, withstand voltage, reverse polarity and regeneration strategy specified | NOT VERIFIED | |
| E0-02 | Phase-current requirement derived from torque, ratio, efficiency and Kt (SYS-REQ-044) | NOT VERIFIED | |
| E0-03 | Hardware overcurrent and e-stop paths independent of firmware | NOT VERIFIED | |
| E0-04 | Measurable criteria for every ELEC-REQ | NOT VERIFIED | |
| E0-05 | Consistency with SAFETY (reaction times) and INTERFACE (connectors, CAN) | NOT VERIFIED | |

### 3.2 E1: Board and component selection review

| Item | Value |
|---|---|
| Evidence | `docs/electronics/ELECTRONICS_ARCHITECTURE.md` §6 (selection table); `MOTOR_CONTROLLER_SPECIFICATION.md` §7 (compliance); ACT-DEC-004/005; `hardware/bom/ELECTRICAL_BOM.csv` |
| Reviewer / date / result | TBD / — / NOT VERIFIED |

| # | Check | Result | Comment |
|---|---|---|---|
| E1-01 | Development board meets the gate criteria (24 V, current, sensing, encoder interfaces, debug, availability) | NOT VERIFIED | |
| E1-02 | Board limitations recorded with mitigations (for example no hardware overcurrent → PSU current limit) | NOT VERIFIED | |
| E1-03 | MCU peripheral checklist satisfied | NOT VERIFIED | |
| E1-04 | Firmware licence review for any board SDK or reference firmware | NOT VERIFIED | |
| E1-05 | Bench setup includes a hardware e-stop relay and fuse | NOT VERIFIED | |
| E1-06 | Cost and lead time acceptable; quotation attached | NOT VERIFIED | |

### 3.3 E2: Schematic and PCB design review (A1)

| Item | Value |
|---|---|
| Evidence | `hardware/motor_controller/custom_pcb/schematics/`, `pcb/` (sources + PDF); power-stage calculations (`hardware/power_stage/`); BOM |
| Reviewer / date / result | TBD / — / NOT VERIFIED |

| # | Check | Result | Comment |
|---|---|---|---|
| E2-01 | MOSFET V and I ratings ≥ margin; conduction and switching losses calculated; thermal path to the housing | NOT VERIFIED | |
| E2-02 | Gate driver: UVLO, dead time, bootstrap sizing, fault output wired to the MCU | NOT VERIFIED | |
| E2-03 | Hardware overcurrent comparator to the PWM break input; threshold calculation; response time estimate | NOT VERIFIED | |
| E2-04 | E-stop: hardware AND at the gate-driver enable; fail-safe (open loop = stop); monitored by the MCU | NOT VERIFIED | |
| E2-05 | Gate-input pull-downs; gates off with the MCU in reset | NOT VERIFIED | |
| E2-06 | Input fuse rating; reverse-polarity circuit; TVS; bulk and film capacitor ripple-current rating | NOT VERIFIED | |
| E2-07 | Regeneration clamp or brake chopper footprint; overvoltage threshold | NOT VERIFIED | |
| E2-08 | Shunt values, Kelvin routing, amplifier gain and offset; ADC range covers the peak + 20 % | NOT VERIFIED | |
| E2-09 | Encoder and Hall interfaces: ESD, filtering, supply, connector | NOT VERIFIED | |
| E2-10 | CAN: transceiver, selectable termination, ESD, twisted-pair connector pin-out | NOT VERIFIED | |
| E2-11 | Layout: power loop area, star ground, analog/power separation, creepage at 24 V (non-critical), copper weight for current | NOT VERIFIED | |
| E2-12 | Test points: rails, PWM, shunts, Vbus, SPI, CAN | NOT VERIFIED | |
| E2-13 | Hardware revision straps; SWD header | NOT VERIFIED | |
| E2-14 | PCB envelope and mounting agreed with the mechanical CAD | NOT VERIFIED | |
| E2-15 | BOM: availability, second sources for critical parts | NOT VERIFIED | |

## 4. Findings register

| ID | Gate | Severity | Finding | Required action | Owner | Due | Closure evidence | Reviewer verified | Status |
|---|---|---|---|---|---|---|---|---|---|
| — | | | | | | | | | |

## 5. Sign-off

| Gate | Reviewer | Result | Date | Project Lead |
|---|---|---|---|---|
| E0 | | | | |
| E1 | | | | |
| E2 | | | | |

## 6. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft (framework) |
