# Kritva Actuator: Test Equipment

| Field | Value |
|---|---|
| Document ID | KA-DOC-VAL-EQUIP |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead |
| Reviewer / Approver | Independent reviewers / Project Lead |
| Applies to | A0, A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** This is a proposed equipment list. Laboratory equipment is **not** included in the prototype budget (₹10–15k A0, ₹20–30k A1 cumulative). Availability is tracked as RISK-016. Specifications are minimum recommendations, TBC.

---

## 1. Purpose

This document lists the equipment needed to execute `VALIDATION_PLAN.md` safely and with traceable results. For each item it gives the minimum specification, its use, its calibration status and its availability. It also specifies the **restrained test fixture**.

## 2. Equipment list

| # | Item | Minimum specification | Used for | Calibration | Status |
|---|---|---|---|---|---|
| EQ-01 | Bench DC power supply | 0–30 V, ≥ 10 A (≥ 15 A recommended), adjustable current limit, over-voltage protection; ideally able to sink current, or used with a clamp | All powered tests | Display checked against a DMM | TBD |
| EQ-02 | Latching e-stop and DC-rated relay | Rated ≥ 30 V DC / ≥ 20 A | All powered tests (SAF-REQ-055/058) | Function test before each session | To be built (EB-003) |
| EQ-03 | Oscilloscope | ≥ 4 channels, ≥ 100 MHz, ≥ 1 GS/s | PWM, dead time, trip timing, latency | Per the manufacturer | TBD |
| EQ-04 | Differential or isolated probe | ≥ 50 V differential, ≥ 25 MHz | Switch nodes, high-side gates | — | TBD |
| EQ-05 | DC current probe (clamp) | DC to ≥ 100 kHz, ≥ 30 A | Phase-current verification | — | TBD |
| EQ-06 | Digital multimeter | True RMS; 0.5 % DC | Rails, Vbus, continuity | Valid certificate preferred | TBD |
| EQ-07 | LCR meter (or a firmware routine) | 100 Hz–10 kHz | Motor R and L (C1) | — | Optional |
| EQ-08 | Thermocouple reader (≥ 4 channels) and K-type thermocouples | ±1 °C | Motor, housing, MOSFET, ambient | — | TBD |
| EQ-09 | IR thermometer or camera | — | Quick checks only (not evidence) | — | TBD |
| EQ-10 | USB-CAN adapter with analyser software | Classic CAN at 1 Mbit/s; timestamps | CAN tests | — | EB-015 |
| EQ-11 | Dial indicator with a magnetic base | 0.01 mm | Runout, backlash (with a lever arm) | — | TBD |
| EQ-12 | Micrometer, bore gauge, vernier | 0.001 / 0.002 / 0.02 mm | Inspection | — | Workshop |
| EQ-13 | Torque screwdriver and wrench | 0.5–6 N·m | Assembly | Valid | TBD |
| EQ-14 | Torque measurement for the output | **Option A:** reaction torque sensor ≥ 50 N·m. **Option B:** calibrated lever arm with known weights and a load cell or spring scale | PC-01–PC-04, PC-11, gearbox checks | Weights or load cell calibrated | TBD (option B is low cost) |
| EQ-15 | Speed measurement | Output encoder (primary) plus an optical tachometer for cross-check | PC-05 | — | TBD |
| EQ-16 | Calibrated weights | 0.5 kg, 1 kg, 2 kg sets | Payload simulation, lever-arm torque | Mass checked on a scale | TBD |
| EQ-17 | Digital scales | ±1 g (two units for the centre-of-mass balance method) | Mass properties | — | TBD |
| EQ-18 | Inclinometer or protractor | ±0.1° | Joint angle reference, stop angles | — | TBD |
| EQ-19 | ESD mat and wrist strap | — | PCB handling (SAF-REQ-072) | — | TBD |
| EQ-20 | CO₂ or dry-powder extinguisher, non-flammable bench surface | — | SAF-REQ-070 | Per the lab | TBD |
| EQ-21 | Safety glasses (≥ 2), transparent guard panel | — | SAF-REQ-062 | — | TBD |

## 3. Restrained test fixture (KA-FIX-0001)

### 3.1 Requirements

| # | Requirement | Reference |
|---|---|---|
| FX-01 | Rigidly clamps the actuator housing through the same mounting interface as the upper arm (IF-01) | SYS-REQ-037 |
| FX-02 | Rated for ≥ 2 × the peak test torque, i.e. ≥ 50 N·m design (TBC), with no yielding | SAF-REQ-065 |
| FX-03 | Provides a **representative arm**: a lever with adjustable mass (to reproduce 1.5 kg at 180 mm, or the measured value) and a payload position at 350 mm | Gate B item 1 |
| FX-04 | Provides a **mechanical rest or catch** at the low position, so that the arm cannot fall onto anything (power loss, coast) | SAF-REQ-045 |
| FX-05 | Provides an **output lock** (pin or brake) for locked-rotor current tests and backlash measurement | PC-09, BU-09 |
| FX-06 | Provides a mount for the torque sensor, or a lever-arm load path for EQ-14 | PC-01–PC-04 |
| FX-07 | A transparent **guard** around the arm's sweep for peak and impact tests | SAF-REQ-062 |
| FX-08 | Marked clear zone (≥ arm reach + 0.5 m) | SAF-REQ-060 |
| FX-09 | Accessible e-stop for the operator | SAF-REQ-055 |
| FX-10 | Cable management that keeps cables away from the sweep | SAF-REQ-048 |

### 3.2 Concept

```
   [steel base plate / extrusion frame, clamped to the bench]
        |
   [mounting block with the IF-01 pattern] -- actuator housing
                                              | output flange
                                              v
                              [lever arm 400 mm, slotted for mass positions]
                                  |-- adjustable forearm-equivalent mass
                                  |-- payload mass at 350 mm
                              [rest/catch at the low position]   [output lock pin hole]
   [polycarbonate guard around the sweep]     [optional reaction torque sensor between the block and the housing]
```

The fixture design is reviewed before first use (ACT-02-007) and recorded in `audit/mechanical/MECHANICAL_DESIGN_AUDIT.md`.

## 4. Calibration and records

- Every instrument used for evidence is identified in the test record by its ID and calibration status.
- Weights and the lever-arm length are measured and recorded once, then re-verified every quarter (TBC).
- Instruments without valid calibration may be used for development, but **not** for Gate B evidence, unless they are cross-checked against a calibrated reference.

## 5. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | Confirm availability of EQ-03, EQ-04, EQ-05 and EQ-14 (borrow, rent or buy) | Project Lead | Week 4 |
| 2 | Fixture design and review | Mechanical Intern | Week 6 |
| 3 | Decide on torque measurement option A or B | Project Lead | Week 5 |

## 6. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
