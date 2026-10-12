# Kritva Actuator: Electrical Requirements

| Field | Value |
|---|---|
| Document ID | KA-REQ-ELEC |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Electronics/Embedded Intern |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | Milestones A0 (development board), A1 (custom controller PCB), A2 (integration support) |
| Classification | Proprietary and confidential (see `LICENSE`) |

> **Status note.** Every numerical value in this document is a **proposed target pending approval**. Values marked **TBD** are not yet determined; values marked **TBC** are working figures that must be confirmed (typically once the motor, gearbox ratio and controller hardware are selected). Nothing here is binding until the Project Lead approves it and records the approval in `planning/v1/DECISIONS.md`. Phase-current figures in particular are **illustrative** until the motor and its torque constant are selected (ACT-01-002, joint motor/gearbox selection).

---

## 1. Purpose and scope

This document is the canonical source of the **electrical and electronic hardware requirements** of the Kritva Actuator. It derives from `requirements/SYSTEM_REQUIREMENTS.md` (KA-REQ-SYS), specifically the requirements allocated to it in KA-REQ-SYS section 11: SYS-REQ-005, SYS-REQ-040 to SYS-REQ-045, SYS-REQ-055 and SYS-REQ-081. It also contributes to SYS-REQ-007, SYS-REQ-024, SYS-REQ-050, SYS-REQ-060, SYS-REQ-061, SYS-REQ-080, SYS-REQ-083, SYS-REQ-084, SYS-REQ-090, SYS-REQ-103 and SYS-REQ-105.

It covers:

- the DC power input, protection, bulk energy storage and regeneration handling;
- the 3-phase power stage, gate drive and current sensing;
- bus-voltage, temperature and position-sensor interfaces;
- the motor-control MCU and its peripherals;
- communication and safety hardware;
- selection criteria for the A0 motor-control development board;
- requirements for the A1 custom controller PCB, EMC/ESD, wiring, bench equipment and thermal limits.

It states **what** the electrical hardware must do and **how well**. Schematics, layouts, part selections and design calculations belong in `hardware/` and `docs/electronics/`. Firmware behaviour is specified in `requirements/FIRMWARE_REQUIREMENTS.md` (KA-REQ-FW). Hazards, safe-state policy and safety integrity are specified in `requirements/SAFETY_REQUIREMENTS.md`. Connector pin-outs and protocol content are specified in `requirements/INTERFACE_REQUIREMENTS.md` and the CAN protocol specification under `communication/can/protocol/`.

Out of scope: high-voltage inverters (not attempted in v1), robot-level power distribution and robot-level emergency-stop circuits (only the actuator's interface to them is in scope), and formal product certification.

## 2. References

| Ref | Document | Relationship |
|---|---|---|
| [P1] | `requirements/SYSTEM_REQUIREMENTS.md` | Parent (SYS-REQ IDs) |
| [S1] | `requirements/ACTUATOR_SPECIFICATION.md` | Sibling: datasheet-level targets, ambient range, mass/envelope |
| [S2] | `requirements/MECHANICAL_REQUIREMENTS.md` | Sibling: housing envelope, PCB mounting space, thermal path to housing |
| [S3] | `requirements/FIRMWARE_REQUIREMENTS.md` | Sibling: firmware use of the hardware defined here (loop rates, faults, calibration) |
| [S4] | `requirements/INTERFACE_REQUIREMENTS.md` | Sibling: connector pin-outs, protocol, signal conventions |
| [S5] | `requirements/SAFETY_REQUIREMENTS.md` | Sibling: hazards (HAZ-NNN), safe state, e-stop policy |
| [D1] | `planning/v1/DECISIONS.md` | ACT-DEC-004 (MCU family, PROPOSED), ACT-DEC-005 (A0 board, PROPOSED), ACT-DEC-006 (USB/UART A0, CAN A1), ACT-DEC-013 (24 V nominal), ACT-DEC-014 (independent review), ACT-DEC-015 (restrained fixture) |
| [D2] | `planning/v1/tasks/ACT-01/` | ACT-01-001 (this document), ACT-01-002 (board/MCU selection, bring-up), ACT-01-005 (custom PCB), ACT-01-006 (CAN firmware) |
| [C1] | `mechanical/calculations/TORQUE_AND_SPEED.md`, `GEARBOX_SELECTION.md` | Motor torque and speed per ratio (source of section 5.1 inputs) |
| [H1] | `hardware/motor_controller/development_board/` | A0 board records and modifications |
| [H2] | `hardware/motor_controller/custom_pcb/{schematics,pcb,manufacturing}/` | A1 PCB design data |
| [H3] | `hardware/power_stage/`, `hardware/sensing/`, `hardware/connectors/` | Sub-circuit design notes and calculations |
| [H4] | `hardware/bom/ELECTRICAL_BOM.csv` | Electrical BOM (exact part numbers, suppliers, quotations) |
| [V1] | `docs/validation/VALIDATION_PLAN.md` | Test gates and procedures |
| [T1] | `audit/requirements_traceability/REQUIREMENTS_TRACEABILITY.csv` | Traceability and verification status |
| [A1] | `audit/electronics/` | Independent electrical review records (gates E0 to E4) |

## 3. Conventions

**Requirement ID format.** `ELEC-REQ-NNN`, range 001 to 199. IDs are grouped by section with gaps reserved for future additions. IDs are never reused after deletion; a deleted requirement keeps its row with the text "Deleted (rev X.Y): reason".

**Columns.**

| Column | Meaning |
|---|---|
| ID | Unique requirement ID |
| Requirement | What is required. "Shall" = mandatory, "should" = recommended, "may" = permitted |
| Rationale | Why it is required |
| Verification | T Test, A Analysis/calculation, I Inspection/review, D Demonstration (as KA-REQ-SYS section 6) |
| Acceptance criterion | The objective pass condition. Where a numeric limit is TBD, the criterion states who sets it and when |
| Evidence location | Repository path where the evidence will be kept |
| Parent SYS-REQ | SYS-REQ IDs this requirement derives from |
| Phase | A0, A1, A2 (first milestone at which it must be met) |
| Priority | M mandatory for milestone exit, H high (deviation needs a recorded decision), L goal |

**Verification status** is tracked in [T1] using `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `PASS_WITH_ACTIONS`, `FAIL`, `NOT_VERIFIED`. A requirement is never marked `PASS` because a document exists; the specified evidence is required.

**Units.** SI. Voltages in V, currents in A, temperatures in °C, torque in N·m, speed in RPM in this document. Unless stated otherwise, **phase current is quoted as the peak (amplitude) of the sinusoidal phase current**, which equals the q-axis current magnitude under amplitude-invariant Clarke/Park transforms. RMS phase current = amplitude / √2. Every motor datasheet Kt must be converted to this convention before use (datasheets variously quote Kt per A RMS, per A peak, or per A DC for trapezoidal drive); the conversion shall be recorded in the motor evaluation (ACT-01-002).

**Bus voltage notation.** V_bus,nom = 24 V; V_bus,op = operating range; V_bus,wst = withstand (no damage, not necessarily operating).

## 4. Electrical architecture overview

### 4.1 Block diagram (A1 target; A0 uses a development board with equivalent functions)

```
  24 V DC in ----+-> [Fuse] -> [Reverse-polarity protection] -> [Inrush limit] --+--> V_BUS
  (PSU / robot   |                                                               |
   bus)          |                                       [Bulk + HF capacitors]--+
                 |                                       [Bus TVS / clamp]-------+
                 |                                       [Brake chopper (opt.)]--+
                 |                                                               |
  E-stop/ENABLE ----> [Hardware enable path] ---> gate-driver enable / supply    |
                 |              |                                                |
                 |              v                                                v
                 |     +------------------+    PWM x6     +-----------+   +----------------+
                 |     |  MCU (STM32G4-   |-------------->| 3-phase   |-->| 3-phase MOSFET |--> U V W --> Motor
                 |     |  class proposed) |<--nFAULT------| gate      |   | inverter       |
                 |     |                  |<--BREAK-------| driver    |   +----------------+
                 |     |  ADC (sync PWM)  |<--------------+-----------+          |
                 |     |                  |<-- shunt amps <-- shunts (low side or inline)
                 |     |                  |<-- V_BUS divider
                 |     |                  |<-- NTC (MOSFET/board), motor thermistor (if fitted)
                 |     |                  |<-- motor Hall / motor encoder (ABI/SPI)
                 |     |                  |<-- output absolute encoder (SPI and/or ABI)
                 |     |                  |<-> USB/UART (A0, debug always)
                 |     |                  |<-> FDCAN -> CAN transceiver -> CAN bus (A1)
                 |     |                  |<-> SWD debug header
                 |     |  IWDG/WWDG       |--> status LEDs
                 |     +------------------+
                 |              ^
                 +--> [Logic supply: buck 24 V -> 5 V / 3.3 V] (from V_BUS, ahead of power-stage enable)
                                                                 |
  Comparator (hardware OC) -------------------------------------> MCU timer BREAK input (PWM off, no firmware)
```

### 4.2 Electrical interface summary

Pin-outs and connector part numbers are owned by [S4] and [H3]; this table states the electrical characteristics required here.

| Interface | Direction | Signals | Electrical characteristics (proposed, TBC) | Connector requirement | Phase | Related ELEC-REQ |
|---|---|---|---|---|---|---|
| DC power input | In | V_BUS+, GND | 24 V nom; 20–28 V operating; ≥ 32 V withstand; reverse-polarity protected; fused | Locking, polarised, rated ≥ input fuse rating | A0 (bench), A1 | 001–015 |
| Motor phases | Out | U, V, W | Up to V_BUS line-to-line PWM; phase current per section 5.2 (continuous ≈ 5–12 A, peak ≈ 12–29 A amplitude, TBC) | Locking, rated ≥ peak phase current, or soldered/crimped leads on A1 | A0, A1 | 030–045, 175–181 |
| Motor Hall sensors | In | H_A, H_B, H_C, 5 V or 3.3 V, GND | Open-collector or push-pull per motor datasheet; pull-ups and RC filter on controller | Locking, keyed | A0 (if used), A1 | 070–074 |
| Motor-side encoder | In | A, B, I (ABI) and/or SPI; supply; GND | 3.3 V logic (or 5 V with level shift); max count rate ≥ 1.2 × max motor speed | Locking, keyed, shielded if > 150 mm (TBC) | A0, A1 | 070–079 |
| Output absolute encoder | In | SPI (CSn, SCK, MISO, MOSI) and/or ABI; supply; GND | 3.3 V logic; SPI clock ≤ encoder limit (verify datasheet) | Locking, keyed; cable length per ELEC-REQ-077 | A1 (A0 optional) | 075–084 |
| Motor winding thermistor | In | NTC/PTC or KTY/PT1000, GND | Per motor datasheet (if fitted) | Shared with Hall connector permitted | A1 | 063 |
| USB / UART | Bidir | USB D+/D− or UART TX/RX, GND | USB 2.0 FS or 3.3 V UART; ESD protected | USB connector on A0 board; header or USB on A1 | A0, A1 | 100–102 |
| CAN | Bidir | CANH, CANL, GND (CAN_SHLD optional) | ISO 11898-2 transceiver; 1 Mbit/s classic CAN baseline, CAN FD-capable preferred; 120 Ω termination selectable | Locking, two connectors (daisy chain) on A1 (TBC) | A1 | 103–109 |
| E-stop / ENABLE input | In | ENABLE+, ENABLE− (or ENABLE, GND) | Active-high enable (loss of signal = disabled); 24 V tolerant (TBC) | Locking, separate from comms (TBC) | A0 (bench e-stop), A1 | 111–114 |
| Fault output (optional) | Out | nFAULT_OUT | Open-drain, active-low (TBC) | Shared with ENABLE connector (TBC) | A1 | 118 |
| SWD debug | Bidir | SWDIO, SWCLK, NRST, 3.3 V ref, GND, SWO (opt.) | 3.3 V | Standard header (e.g. 10-pin 1.27 mm Cortex Debug, TBC) | A1 | 143 |
| Status LEDs | Out | Power, status, fault | Visible from outside the housing or through a light pipe (TBC) | n/a | A1 | 119 |

## 5. Design basis calculations (informative; inputs TBC)

These calculations give the sizing basis for the requirements in section 6. They are not results. Each will be repeated with selected-component data in `hardware/power_stage/` and `docs/electronics/` and reviewed at gate E1/E2. All figures were computed with Python from the stated inputs.

### 5.1 Motor-side torque and speed (from KA-REQ-SYS section 10)

Sizing assumptions: gearbox efficiency η_g = 0.85, output speed 45 RPM (4.712 rad/s).

| Ratio | Motor speed at 45 RPM out | Motor torque, 10 N·m out | Motor torque, 20 N·m out | Motor torque, 25 N·m out | Motor torque, 6.08 N·m hold |
|---|---|---|---|---|---|
| 15:1 | 675 RPM | 0.78 N·m | 1.57 N·m | 1.96 N·m | 0.48 N·m |
| **20:1 (first candidate)** | **900 RPM** | **0.59 N·m** | **1.18 N·m** | **1.47 N·m** | **0.36 N·m** |
| 25:1 | 1 125 RPM | 0.47 N·m | 0.94 N·m | 1.18 N·m | 0.29 N·m |

Formula: T_motor = T_out / (N · η_g). The hold column uses the static gravity torque T_g = 6.08 N·m; holding torque through a planetary gearbox may differ from the driving-direction value because of friction direction, so it is shown only for orientation.

### 5.2 Worked phase-current estimate (20:1 case, illustrative Kt, TBC)

For a sinusoidally commutated PMSM under FOC with I_d = 0:

- T_motor = Kt · I_q, so **I_q = T_motor / Kt**;
- with amplitude-invariant transforms, the phase-current amplitude I_ph,pk = I_q, and I_ph,rms = I_q / √2.

Inputs: T_motor,cont = 0.59 N·m and T_motor,peak = 1.47 N·m (20:1, η_g = 0.85, 10 N·m and 25 N·m output). Kt values below are **illustrative only** to bracket the range of 24 V motors in the 75–100 W class; the real value comes from the selected motor's datasheet or measurement (back-EMF constant Ke in V·s/rad, line-to-line peak, gives Kt ≈ (3/2)·(Ke,ph,pk) in amplitude-invariant form; the derivation shall be recorded).

| Kt (N·m/A, amplitude) | I_cont amplitude (A) | I_cont RMS (A) | I_peak amplitude (A) | I_peak RMS (A) | Current-sense full-scale (1.25 × I_peak) (A) | MOSFET continuous rating guide (≥ 2 × I_peak) (A) |
|---|---|---|---|---|---|---|
| 0.05 | 11.8 | 8.3 | 29.4 | 20.8 | ±36.8 | ≥ 59 |
| 0.08 | 7.4 | 5.2 | 18.4 | 13.0 | ±23.0 | ≥ 37 |
| 0.12 | 4.9 | 3.5 | 12.3 | 8.7 | ±15.3 | ≥ 25 |

Worked example, Kt = 0.08 N·m/A: I_cont = 0.59 / 0.08 = 7.4 A amplitude (5.2 A RMS); I_peak = 1.47 / 0.08 = 18.4 A amplitude (13.0 A RMS). This sits inside the baseline brief's expected range of roughly 6–10 A continuous and 15–25 A peak. A low-Kt motor (0.05 N·m/A) pushes the peak to ≈ 29 A, beyond the brief range, which drives power-stage, shunt, connector and wiring sizing. A high-Kt motor (0.12 N·m/A) lowers current but generally implies a lower Kv and therefore lower maximum speed at 24 V; the motor's no-load speed at the minimum operating voltage (20 V) must exceed 900 RPM (20:1) with margin for the back-EMF and the I·R drop at rated current (check in ACT-01-002).

Notes:

1. The peak case uses 25 N·m (stretch). If 20 N·m is adopted, I_peak scales by 20/25 = 0.8.
2. Kt falls with magnetic saturation at high current and with magnet temperature (typically 0.1–0.2 %/°C for ferrite/NdFeB, verify for the selected motor). The current ratings shall include this effect, or the peak-torque test (Gate B) will reveal a shortfall.
3. Supply (DC bus) current is much lower than phase current at low speed; see 5.3. **The power stage is sized from phase current, not from supply current** (SYS-REQ-044).

### 5.3 Power budget (continuous and peak, illustrative)

Assumed efficiencies (TBC with selected components): gearbox 0.85; motor 0.80 at the continuous point and 0.75 at peak; inverter 0.95; logic, sensors and communication overhead 3 W (TBC).

| Stage | Continuous: 10 N·m at 45 RPM | Peak: 20 N·m at 45 RPM | Peak: 25 N·m at 45 RPM |
|---|---|---|---|
| Output mechanical power | 47.1 W | 94.2 W | 117.8 W |
| Motor shaft power (÷ 0.85) | 55.4 W | 110.9 W | 138.6 W |
| Motor electrical input (÷ 0.80 cont / 0.75 peak) | 69.3 W | 147.8 W | 184.8 W |
| Inverter DC input (÷ 0.95) | 72.9 W | 155.6 W | 194.5 W |
| Plus logic overhead (3 W) | **≈ 76 W** | **≈ 159 W** | **≈ 198 W** |
| Supply current at 24 V | 3.2 A | 6.6 A | 8.2 A |
| Supply current at 20 V (min operating) | 3.8 A | 7.9 A | 9.9 A |

Interpretation:

- A bench PSU of **≥ 24 V / 10 A** covers the illustrative 25 N·m peak at 45 RPM with no margin; **≥ 15 A capability (with adjustable current limit) is recommended** for headroom, used with the current limit set low during bring-up (ELEC-REQ-165).
- At stall or low speed and peak torque, supply current is small but **phase current is at its maximum**, so motor copper loss (≈ 1.5 · I_ph,pk² · R_ph, with R_ph phase-to-neutral) and MOSFET conduction loss dominate. The thermal requirements (section 6.15) use phase current.
- Motor copper loss is not computed here because phase resistance is unknown; it shall be computed in ACT-01-002 once R_ph is measured (KA-REQ-FW calibration).

### 5.4 Regeneration energy and power (illustrative)

Two regeneration cases matter for a gravity-loaded elbow:

1. **Deceleration of the arm.** Arm kinetic energy at 45 RPM with J = 0.171 kg·m² is ≈ 1.9 J (KA-REQ-SYS section 10). Returned through the gearbox (back-driving efficiency taken as 0.85, TBC) and the motor acting as a generator (0.85, TBC), up to ≈ 1.37 J reaches the DC bus, plus the motor rotor's own kinetic energy (TBD from rotor inertia).
2. **Lowering the arm under gravity at speed.** Lowering the 6.08 N·m gravity load at 45 RPM is 28.7 W of mechanical power into the actuator; after the same efficiencies, about **20.7 W of continuous regenerative power** can return to the bus for the duration of the motion (less motor copper losses).

Bus capacitance alone cannot absorb this energy within the 32 V withstand limit:

- Energy stored between 24 V and 32 V in C: E = ½ · C · (32² − 24²) = 224 · C. For 470 µF this is 0.105 J; for 1 000 µF it is 0.224 J.
- Absorbing 1.37 J between 24 V and 32 V would need ≈ **6.1 mF**, which is impractical on the actuator PCB.

Consequences, reflected in section 6.2:

- Most laboratory bench PSUs **cannot sink current**; regenerated energy raises the bus voltage. A bus-voltage limit in firmware (regen current limiting), a hardware clamp, and either a sink-capable supply or a **brake chopper** are needed.
- An illustrative brake resistor for 20 W continuous at a 30 V chopper threshold is ≈ 45 Ω (P = V²/R); a 4.7 Ω resistor at 30 V absorbs up to ≈ 191 W peak at full duty. Values are TBD in `hardware/power_stage/`.
- Disabling PWM (coast) does **not** stop regeneration if the motor's line-to-line back-EMF exceeds the bus voltage (the MOSFET body diodes rectify it). At the planned speeds (≤ 1 125 RPM motor) back-EMF should be well below 24 V for a correctly selected motor; this shall be confirmed from Ke and the maximum back-driven speed (including a falling arm) in ACT-01-002.

### 5.5 Bulk capacitance and ripple current (illustrative)

- Capacitor RMS ripple current for a 3-phase two-level inverter is roughly 0.46–0.5 × the RMS phase current at worst-case modulation. For I_ph,pk = 11.8 A (Kt 0.05, continuous) this is ≈ 4.2 A RMS; for the 29.4 A peak case ≈ 10.4 A RMS (short duration).
- Simple ripple-voltage estimate, ΔV ≈ I_ph,pk · D(1−D) / (f_PWM · C), with D(1−D) ≤ 0.25, f_PWM = 20 kHz, ΔV = 0.5 V: C ≈ 295 µF (Kt 0.05 continuous), 460 µF (Kt 0.08 peak), 735 µF (Kt 0.05 peak).
- Proposed starting point (TBC): **≥ 470 µF total bulk** (low-ESR electrolytic and/or polymer, voltage rating ≥ 50 V) plus ≥ 1 µF to 10 µF of X7R ceramic per half-bridge placed at the power loop, refined at E2 by ripple-current analysis. Supply-cable inductance can resonate with ceramics during hot-plug; this is managed by the inrush and TVS requirements.

### 5.6 Current-shunt sizing example (illustrative)

| R_shunt | Voltage at 11.8 A | Voltage at 29.4 A | Upper-bound dissipation at 11.8 A amplitude (I_rms² · R) | Upper-bound dissipation at 29.4 A amplitude |
|---|---|---|---|---|
| 1 mΩ | 11.8 mV | 29.4 mV | 0.07 W | 0.43 W |
| 2 mΩ | 23.6 mV | 58.8 mV | 0.14 W | 0.86 W |
| 3 mΩ | 35.4 mV | 88.2 mV | 0.21 W | 1.30 W |

Example chain (Kt 0.05): 2 mΩ shunt, full-scale ±36.8 A → ±73.6 mV; a gain of ≈ 20 V/V centred at 1.65 V maps this to ≈ ±1.5 V in a 3.3 V, 12-bit ADC (0.81 mV/LSB), giving ≈ 20 mA/LSB. Low-side shunts conduct only while the low-side switch is on, so the dissipation shown is an upper bound. The real shunt value is set in E2 after the motor is selected.

### 5.7 MOSFET conduction loss example (illustrative)

Per half-bridge, conduction loss ≈ I_ph,rms² · R_DS(on),hot. With an illustrative R_DS(on) of 5 mΩ at 25 °C and a hot multiplier of 1.5: 0.52 W per leg (1.6 W total) at 11.8 A amplitude continuous, and 3.2 W per leg (9.7 W total) at 29.4 A amplitude peak. Switching loss, reverse-recovery and dead-time diode conduction losses are added in the E2 thermal analysis. These figures motivate the thermal-path requirements (ELEC-REQ-140, 185–192).

## 6. Requirements

### 6.1 Power input

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| ELEC-REQ-001 | The controller shall operate from a **24 V DC nominal** supply. | ACT-DEC-013; robot and bench standard. | T | Full functional test (enable, current loop, motion) passes at 24.0 V ± 0.2 V. | `results/motor_control/` | SYS-REQ-040 | A0 | M |
| ELEC-REQ-002 | The controller shall meet all performance requirements over a **proposed operating range of 20–28 V** (TBC). | Covers PSU tolerance, cable drop and robot battery/bus variation. | T | Functional and torque tests pass at 20 V, 24 V and 28 V. Range confirmed by Project Lead decision before A1 PCB start. | `results/motor_control/`, `tests/hardware/` | SYS-REQ-041 | A1 | M |
| ELEC-REQ-003 | The controller shall **withstand ≥ 32 V** on the DC bus (including regeneration transients) without damage, whether enabled or disabled. | Regeneration and supply transients (section 5.4). | A, T | Analysis shows every bus-connected component rated ≥ 32 V with derating (ELEC-REQ-031); bench test at 32 V for 60 s (TBC) with power stage disabled shows no damage and normal operation afterwards. | `hardware/power_stage/`, `results/motor_control/` | SYS-REQ-041 | A1 | M |
| ELEC-REQ-004 | The controller shall be **protected against reverse polarity** of the DC input up to −28 V (TBC) without damage. Preferred implementation: low-loss active protection (e.g. P-MOSFET or ideal-diode controller) rather than a series diode at the full input current. | Wiring errors on a bench are likely; a series diode at ≈ 10 A dissipates several watts. | A, T | Applying −24 V for 10 s from a current-limited PSU (limit ≤ 1 A) causes no damage; normal operation afterwards. Loss of protection element at 10 A ≤ TBD W by analysis. | `hardware/power_stage/`, `tests/hardware/` | SYS-REQ-041 | A1 | M |
| ELEC-REQ-005 | Reverse-polarity protection shall not prevent **regenerative current flowing back to the bus capacitors**; if the protection blocks reverse current to the supply, the bus clamp and braking provisions (section 6.2) shall be sized assuming no supply sink. | An ideal diode blocks regen to the PSU, increasing bus over-voltage. | A | Design analysis records the regen path and the assumption used. | `hardware/power_stage/` | SYS-REQ-041 | A1 | M |
| ELEC-REQ-006 | The controller shall limit **inrush current** at hot-plug or power-on to ≤ TBD A (proposed ≤ 10 A peak, TBC) using a pre-charge, soft-start or hot-swap circuit. | Bulk capacitance (section 5.5) causes connector arcing, PSU trips and voltage overshoot from cable inductance. | T | Oscilloscope capture of input current at hot-plug with a 1 m (TBC) supply cable shows peak ≤ limit and bus overshoot ≤ 32 V. | `results/motor_control/`, `tests/hardware/` | SYS-REQ-041 | A1 | H |
| ELEC-REQ-007 | The DC bus shall include **bulk capacitance** sized for the ripple current and ripple voltage of section 5.5 (proposed ≥ 470 µF, rated ≥ 50 V, TBC), plus local ceramic decoupling at each half-bridge. | Ripple, stability of the bus, and local commutation loop. | A, T | Ripple-current analysis at E2 shows capacitor RMS current ≤ 80 % of rating at max ambient. Measured bus ripple at continuous current ≤ 1 V p-p (TBC). | `hardware/power_stage/`, `results/motor_control/` | SYS-REQ-044 | A1 | M |
| ELEC-REQ-008 | The DC input shall be protected by a **fuse** (or electronic fuse) rated above the peak supply current of section 5.3 and below the current rating of the input wiring and connector. Proposed: 15 A (TBC), time-lag class selected so that the peak-torque duty (≤ 2 s, ≤ 10 %, TBC placeholder) does not cause nuisance operation. | Protection of wiring and of the PSU from a shorted power stage. | A, I | Fuse selection calculation recorded; fuse I²t coordinates with wire and connector ratings. | `hardware/power_stage/` | SYS-REQ-041, SYS-REQ-080 | A1 | M |
| ELEC-REQ-009 | The A0 bench setup shall include an **inline fuse** in the PSU positive lead (rating TBD from the selected A0 board's maximum current). | The A0 development board may have no input fuse. | I | Bench inspection checklist shows fuse fitted and rating recorded. | `results/motor_control/` (bench setup record) | SYS-REQ-045, SYS-REQ-084 | A0 | M |
| ELEC-REQ-010 | A **transient voltage suppressor or clamp** shall be fitted on the DC bus with a clamping voltage below the lowest absolute-maximum rating of any bus-connected component and a stand-off voltage above 28 V (proposed stand-off ≈ 30 V, clamp ≤ 45 V, TBC). | Protects against hot-plug ringing and short regen spikes. | A | Datasheet values recorded; clamp voltage < lowest abs-max on bus. | `hardware/power_stage/` | SYS-REQ-041 | A1 | M |
| ELEC-REQ-011 | The logic supply (MCU, sensors, transceivers) shall be derived from the DC input **upstream of the power-stage enable**, so that the MCU stays powered and can report faults when the motor power path is removed. | Fault reporting and logging after an e-stop. | I, T | With ENABLE deasserted, MCU, CAN and USB/UART remain operational and report status. | `tests/hardware/` | SYS-REQ-081, SYS-REQ-062 | A1 | M |
| ELEC-REQ-012 | The logic supply shall operate from **≥ 9 V to ≥ 32 V** (TBC) at the input, so that the MCU remains alive during bus dips and regen spikes. | Avoids brown-out resets during motion transients. | T | MCU does not reset when the bus is stepped between 12 V and 32 V; brown-out detector set to a recorded threshold. | `tests/hardware/` | SYS-REQ-041 | A1 | H |
| ELEC-REQ-013 | Logic supply rails (e.g. 5 V, 3.3 V, analogue 3.3 V reference) shall have ripple ≤ TBD mV and the ADC reference shall be filtered separately from the digital rail. | Current-sense and encoder accuracy. | T | Measured rail ripple ≤ limit during 20 kHz PWM at continuous current. | `results/motor_control/` | SYS-REQ-050 | A1 | H |
| ELEC-REQ-014 | The controller shall provide a measurable **input power path voltage drop** budget: total drop from input connector to bus capacitors ≤ 0.3 V at 10 A (TBC). | Keeps operating range usable at 20 V input. | A, T | Measured drop ≤ budget. | `results/motor_control/` | SYS-REQ-041 | A1 | L |
| ELEC-REQ-015 | Under-voltage at the input shall not cause uncontrolled motion. Below the under-voltage threshold (proposed 18 V, TBC) the power stage shall be disabled by firmware, and the gate driver's own UVLO shall prevent partial gate drive. | Partial gate drive leads to linear-mode MOSFET operation and failure. | T | Ramping the input from 24 V to 0 V and back with the motor enabled causes a clean disable and fault flag, no MOSFET failure, no unexpected motion. | `tests/hardware/`, `tests/safety/` | SYS-REQ-080 | A1 | M |

### 6.2 Regeneration and braking

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| ELEC-REQ-020 | The design shall include a documented **regeneration analysis** covering arm deceleration, gravity-driven lowering, back-driving by external load and e-stop during motion, using the selected motor, gearbox and arm data (section 5.4 is the starting point). | Regenerated energy exceeds what bus capacitance can absorb. | A | Analysis reviewed at E2; states peak bus voltage in each case with and without a brake chopper. | `hardware/power_stage/` | SYS-REQ-041 | A1 | M |
| ELEC-REQ-021 | The hardware shall provide the bus-voltage measurement needed for **firmware bus-voltage limiting** (regen current limiting) with accuracy ≤ ±2 % of reading (TBC) and bandwidth ≥ 1 kHz. | Primary means of keeping the bus below the withstand limit (KA-REQ-FW). | T | Calibration against a reference meter at 20, 24, 28, 32 V within accuracy. | `results/motor_control/` | SYS-REQ-041 | A0 | M |
| ELEC-REQ-022 | The A1 PCB should include provision for an **optional brake chopper** (switch + external or on-board resistor), controlled by an MCU output with a **hardware over-voltage trigger** independent of firmware (proposed threshold 30 V, TBC). Fitting it is decided at E2 from ELEC-REQ-020. | Bench PSUs normally cannot sink current; gravity lowering gives continuous regen of ≈ 20 W (section 5.4). | A, T | If fitted: bus held ≤ 32 V during a lowering test at 45 RPM with full payload on the fixture and during an e-stop at 45 RPM. If not fitted: decision recorded with justification. | `hardware/power_stage/`, `results/motor_control/`, `planning/v1/DECISIONS.md` | SYS-REQ-041 | A1 | H |
| ELEC-REQ-023 | The brake resistor (if fitted) shall be rated for the continuous regen power and the peak energy of ELEC-REQ-020 with ≥ 2× margin, and shall be mounted so that its surface temperature cannot ignite or damage adjacent parts. | Fire and burn hazard. | A, T | Thermal test on the fixture: resistor temperature ≤ its rating and ≤ TBD °C at accessible surfaces. | `results/thermal/` | SYS-REQ-080, SYS-REQ-082 | A1 | H |
| ELEC-REQ-024 | During A0/A1 bench testing without a brake chopper, the PSU shall be either sink-capable or paired with a **bench regen clamp** (e.g. a shunt regulator or a diode into a resistive load), and the arm deceleration limits shall be set so that the measured bus voltage stays ≤ 30 V (TBC). | Protects the PSU and controller during bring-up. | T, I | Bench record shows bus voltage capture during the most severe deceleration test ≤ 30 V. | `results/motor_control/` | SYS-REQ-045, SYS-REQ-084 | A0 | M |
| ELEC-REQ-025 | The over-voltage response chain shall be: (1) firmware regen current limiting above V_regen,limit (proposed 29 V, TBC); (2) brake chopper (if fitted) above 30 V (TBC); (3) firmware over-voltage fault and PWM disable above V_OV (proposed 31 V, TBC); (4) TVS clamp. The thresholds shall be ordered and recorded. | Layered protection; a single layer failing does not exceed 32 V. | A, T | Threshold table recorded; fault-injection test with a programmable source confirms each layer's threshold within ±0.5 V. | `hardware/power_stage/`, `tests/safety/` | SYS-REQ-041, SYS-REQ-080 | A1 | M |

### 6.3 Power stage

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| ELEC-REQ-030 | The power stage shall be a **3-phase, two-level MOSFET voltage-source inverter** (six switches) driven by complementary PWM. | Standard topology for FOC of a 24 V PMSM. | I | Schematic inspection. | `hardware/motor_controller/custom_pcb/schematics/` | SYS-REQ-050 | A0/A1 | M |
| ELEC-REQ-031 | MOSFET **V_DS rating shall be ≥ 60 V** (proposed; ≥ 1.5 × the 32 V withstand plus switching-ringing margin) and the measured peak V_DS during switching at peak current shall be ≤ 80 % of the rating. | Derating against ringing and regen. | A, T | Datasheet rating recorded; oscilloscope capture of switch-node ringing at peak current shows ≤ 48 V on a 60 V part. | `hardware/power_stage/`, `results/motor_control/` | SYS-REQ-044 | A1 | M |
| ELEC-REQ-032 | MOSFET continuous drain current rating at a case/board temperature of 100 °C shall be **≥ 2 × the peak phase current** of the selected motor (section 5.2), and the transient thermal impedance shall keep T_j ≤ 125 °C (TBC) for the approved peak duration. | Datasheet I_D at 25 °C is optimistic; the peak profile is TBD. | A | Calculation with selected MOSFET and motor recorded; T_j estimate for continuous and peak profiles. | `hardware/power_stage/` | SYS-REQ-044 | A1 | M |
| ELEC-REQ-033 | The power stage shall be sized from the **selected motor's peak and continuous phase current** (section 5.2) and the approved peak-torque duty profile, not from the supply voltage or supply current. | SYS-REQ-044 (common sizing error). | A, I | E2 review checklist item: sizing calculation uses motor Kt, current amplitude convention and duty profile. | `hardware/power_stage/`, `audit/electronics/` | SYS-REQ-044 | A0/A1 | M |
| ELEC-REQ-034 | The A0 development board shall be rated for the selected motor's continuous and peak phase current, or the firmware current limit shall be set to the board's rating and the resulting torque limit recorded. | An under-rated A0 board fails or limits tests. | A, I | Board rating vs motor current recorded in the A0 selection record; firmware current limit ≤ board rating. | `hardware/motor_controller/development_board/` | SYS-REQ-005, SYS-REQ-044 | A0 | M |
| ELEC-REQ-035 | A **3-phase gate driver** (integrated or three half-bridge drivers) shall be used, with: under-voltage lockout; a fault output (nFAULT) connected to the MCU; adequate source/sink current for the selected MOSFET gate charge at 20 kHz (switching transition ≤ TBD ns); and bootstrap or charge-pump supply capable of 100 % duty for ≥ the peak-torque duration (or firmware duty limit if bootstrap-only). | Reliable switching; defined behaviour on supply loss. | A, T | Gate waveforms captured: no shoot-through, transitions within design value, bootstrap does not collapse at maximum duty. | `results/motor_control/` | SYS-REQ-050 | A1 | M |
| ELEC-REQ-036 | Gate drive shall default to **all switches OFF** whenever the MCU is in reset, unprogrammed, its PWM outputs are high-impedance, or the ENABLE input is deasserted (pull-downs on gate inputs, driver enable defaulting to disabled). | Prevents motion or shoot-through during boot and programming. | T | Power-up, reset and SWD programming with motor connected cause no phase current (current probe trace ≤ noise floor). | `tests/hardware/` | SYS-REQ-080, SYS-REQ-081 | A0/A1 | M |
| ELEC-REQ-037 | **Dead time** shall be inserted in hardware (MCU timer dead-time generator and/or gate-driver dead time) with a value ≥ the worst-case MOSFET turn-off delay plus driver propagation skew plus margin (proposed 200–500 ns, TBC from datasheets), and shall be verified on the switch node. | Shoot-through protection. | A, T | Calculation recorded; measured dead time at hot temperature ≥ design minimum; no shoot-through current spikes. | `hardware/power_stage/`, `results/motor_control/` | SYS-REQ-055 | A0/A1 | M |
| ELEC-REQ-038 | The gate driver or MCU shall provide **shoot-through interlock** (hardware prevention of both switches of a leg being on). | Defence against firmware or configuration errors. | I, T | Datasheet feature or logic recorded; test with deliberately overlapping PWM commands (on a current-limited supply) shows interlock. | `tests/hardware/` | SYS-REQ-080 | A1 | H |
| ELEC-REQ-039 | PWM frequency shall be configurable with **20 kHz** as the proposed default (TBC) and ≥ 16 kHz minimum (above most audible range), and the power stage thermal design shall be valid at the selected frequency. | Matches loop rates in KA-REQ-FW; acoustic noise. | A, T | Thermal test at 20 kHz meets section 6.15. | `results/thermal/` | SYS-REQ-050 | A0 | H |
| ELEC-REQ-040 | The power stage shall support a **minimum duty / sampling window** compatible with the chosen current-sensing scheme (e.g. low-side shunt on-time ≥ ADC sampling + settling, proposed ≥ 1.5 µs, TBC). | Low-side shunts read only while the low switch is on. | A, T | Measured amplifier settling + ADC sample time ≤ minimum low-side on-time; firmware maximum modulation index set accordingly. | `hardware/sensing/`, `results/motor_control/` | SYS-REQ-050 | A0/A1 | M |
| ELEC-REQ-041 | Switch-node slew rate shall be controlled (gate resistors or driver settings) to balance switching loss against EMI and ringing; turn-on and turn-off gate resistors shall be independently adjustable on the A1 PCB. | Bring-up tuning of EMI and ringing. | I, T | Footprints present; chosen values recorded with ringing captures. | `hardware/motor_controller/custom_pcb/` | SYS-REQ-044 | A1 | H |
| ELEC-REQ-042 | The power stage shall survive a **phase-to-phase short and a phase-to-ground short** at the motor connector while enabled, by hardware overcurrent shutdown (ELEC-REQ-110). | Wiring faults during bring-up. | T | Fault-injection test on a current-limited supply first, then at full supply with a fused short fixture: no MOSFET failure; fault reported. | `tests/safety/`, `results/motor_control/` | SYS-REQ-080 | A1 | H |
| ELEC-REQ-043 | Motor phase outputs shall have provision for **phase-voltage sensing** (divider per phase) on the A1 PCB (fit optional). | Enables back-EMF measurement, flying start and dead-time compensation characterisation. | I | Footprints present on schematic. | `hardware/motor_controller/custom_pcb/schematics/` | SYS-REQ-053 | A1 | L |
| ELEC-REQ-044 | The power stage shall be rated for a **motor with up to TBD pole pairs** and a maximum electrical frequency of ≥ 1.5 × (max motor speed × pole pairs / 60) at 20 kHz PWM (≥ 10 PWM periods per electrical cycle at maximum speed, TBC). | Adequate PWM resolution at the highest motor speed (≈ 1 125 RPM at 25:1, plus overspeed margin). | A | Calculation recorded with selected motor. | `hardware/power_stage/` | SYS-REQ-050 | A0 | H |

### 6.4 Current sensing

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| ELEC-REQ-050 | The controller shall measure **phase current** for FOC using **three low-side shunts (preferred)**, two low-side shunts, or two/three inline phase-current sensors. The A1 choice is recorded at E2 with the trade-offs (cost, sampling windows at high modulation, common-mode requirements for inline sensing). | SYS-REQ-050 requires phase-current sensing. Three shunts permit reconstruction at high modulation and a sum-check. | I | Topology recorded in design notes with trade study. | `docs/electronics/`, `hardware/sensing/` | SYS-REQ-050 | A0/A1 | M |
| ELEC-REQ-051 | The current-sense **full-scale range** shall be **≥ 1.25 × the peak phase current** of the selected motor (section 5.2; e.g. ±23 A for Kt = 0.08, ±37 A for Kt = 0.05, TBC) and shall cover the hardware overcurrent threshold without saturation. | Control headroom and fault visibility. | A, T | Calculation; injected DC current test at full-scale without amplifier saturation. | `hardware/sensing/`, `results/motor_control/` | SYS-REQ-044 | A0/A1 | M |
| ELEC-REQ-052 | Current-sense **accuracy** after offset calibration shall be ≤ ±2 % of reading ±1 % of full-scale (TBC) across 0–70 °C board temperature, and phase-to-phase gain mismatch ≤ 1 % (TBC). | Torque accuracy and torque ripple. | T | Calibration against a reference current (DC through each phase with known shunt/meter) at 25 °C and hot. | `results/motor_control/` | SYS-REQ-050 | A1 | H |
| ELEC-REQ-053 | Current-sense signal-chain **bandwidth** shall be ≥ 10 × the current-loop bandwidth target and ≥ 100 kHz small-signal (TBC), with settling to 1 % within the sampling window of ELEC-REQ-040. | The current loop at 20 kHz needs an undistorted sample. | A, T | Step-response capture of amplifier output. | `results/motor_control/` | SYS-REQ-050 | A0/A1 | M |
| ELEC-REQ-054 | Current samples shall be taken **synchronously with the PWM** (ADC triggered by the PWM timer at the centre of the low-side on-time), with all phases sampled simultaneously or within ≤ 1 µs (TBC). | Avoids switching noise and phase skew; needed for SVPWM. | I, T | Oscilloscope capture of ADC trigger (debug GPIO) vs PWM shows sampling at the intended point. | `results/motor_control/` | SYS-REQ-055 | A0 | M |
| ELEC-REQ-055 | Shunt resistors shall be **Kelvin-connected** (four-terminal or Kelvin pads), low-inductance (≤ TBD nH), and rated for ≥ 2 × the dissipation of section 5.6 at the peak profile. | Accuracy and reliability. | I, A | Layout inspection at E2; dissipation calculation. | `hardware/motor_controller/custom_pcb/pcb/` | SYS-REQ-044 | A1 | M |
| ELEC-REQ-056 | Current-sense amplifiers shall have a common-mode range covering the shunt position (low-side: −1 V to +1 V transient, TBC; inline: −2 V to V_bus + 2 V, TBC) and input filtering sized against the sampling window. | Low-side shunt nodes ring below ground during switching. | A | Datasheet comparison recorded. | `hardware/sensing/` | SYS-REQ-050 | A1 | M |
| ELEC-REQ-057 | The current-sense chain shall provide a **zero-current offset** measurement opportunity at every enable (PWM off or all low-side on with zero current), and offsets beyond ±TBD mV shall be detectable by firmware. | Offset drift causes torque error and DC injection. | T | Firmware reads offsets at enable; deliberately biased input is flagged. | `tests/firmware/` | SYS-REQ-050 | A0 | H |
| ELEC-REQ-058 | The hardware overcurrent comparator (ELEC-REQ-110) shall take its input from the **same shunts** (or an independent DC-link shunt) such that a phase-to-phase or phase-to-ground short is detected. | Detection coverage. | A | Coverage analysis per fault location recorded. | `hardware/sensing/` | SYS-REQ-080 | A1 | M |
| ELEC-REQ-059 | DC-link (supply) current should be measurable (shunt or reconstruction) for the power budget and efficiency characterisation. | Efficiency and thermal characterisation (Gate B). | T | Measured supply current agrees with a reference meter within ±3 % (TBC). | `results/motor_control/` | SYS-REQ-042 | A1 | L |

### 6.5 Bus-voltage and temperature sensing

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| ELEC-REQ-060 | The controller shall measure **DC bus voltage** over 0–40 V (TBC) with ≤ ±2 % accuracy (TBC), sampled at ≥ the current-loop rate or ≥ 10 kHz. | Voltage feed-forward in FOC, OV/UV protection, regen limiting. | T | Calibration at 0, 12, 20, 24, 28, 32 V against a reference meter. | `results/motor_control/` | SYS-REQ-041, SYS-REQ-080 | A0 | M |
| ELEC-REQ-061 | The bus-voltage divider shall be protected so that a 45 V transient (TVS clamp level) does not damage the ADC input (series resistance, clamp to the ADC supply). | ADC pin protection. | A | Calculation recorded. | `hardware/sensing/` | SYS-REQ-041 | A1 | M |
| ELEC-REQ-062 | The controller shall measure **power-stage temperature** with at least one NTC (or equivalent) thermally coupled to the MOSFETs (within ≤ 5 mm, TBC) and should measure board temperature near the MCU/shunts. Range −20 °C to 125 °C; accuracy ≤ ±3 °C (TBC) in 25–100 °C. | Controller overtemperature protection (CTRL-REQ-001). | T | Comparison with thermocouple at MOSFET case during thermal test; offset/lag recorded. | `results/thermal/` | SYS-REQ-080 | A0/A1 | M |
| ELEC-REQ-063 | If the selected motor has a **winding thermistor**, the controller shall provide a matching input (NTC/PTC/KTY/PT1000, TBC). If it has none, a motor-surface sensor shall be fitted for characterisation and firmware shall rely on a validated thermal model (KA-REQ-FW). | Motor overtemperature protection (CTRL-REQ-001). | I, T | Input implemented and calibrated, or thermal model validated against surface/winding measurement. | `results/thermal/` | SYS-REQ-080 | A1 | M |
| ELEC-REQ-064 | Temperature sensor inputs shall be **open- and short-circuit detectable** (reading outside the plausible range). | A disconnected NTC must not read as "cool". | T | Open and short each sensor; firmware reports sensor fault. | `tests/safety/` | SYS-REQ-080 | A1 | H |
| ELEC-REQ-065 | An **ambient/fixture temperature** measurement (external thermocouple or sensor) shall be recorded in every thermal and loaded test. | SYS-REQ-090, SYS-REQ-103 test record content. | I | Test records contain ambient temperature. | `results/thermal/` | SYS-REQ-090, SYS-REQ-103 | A0 | M |

### 6.6 Position-sensing interfaces

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| ELEC-REQ-070 | The controller shall provide a **motor-side feedback** input suitable for FOC commutation: Hall sensors (if the motor has them) and/or a motor-shaft magnetic encoder via **ABI (quadrature + index)** and/or **SPI**. | SYS-REQ-052: motor-side feedback for commutation. | I, T | Interface functional with selected motor/encoder at max motor speed. | `results/motor_control/` | SYS-REQ-050, SYS-REQ-052 | A0 | M |
| ELEC-REQ-071 | Motor-side encoder resolution shall give an electrical-angle resolution of ≤ 1° electrical (TBC) at the motor's pole-pair count; for p pole pairs this requires ≥ 360·p counts per mechanical revolution. | Commutation accuracy and torque ripple. | A | Calculation with selected motor/encoder. | `hardware/sensing/` | SYS-REQ-050 | A0 | H |
| ELEC-REQ-072 | The motor-side encoder interface shall support count/update rates ≥ 1.2 × the maximum motor speed (≈ 1 350 RPM for 25:1 with margin, TBC) with **position latency ≤ 1 current-loop period (50 µs at 20 kHz)**, or the latency shall be known and compensated. | Commutation error grows with latency × electrical speed. | A, T | Latency measured or from datasheet and recorded; compensation in firmware. | `results/motor_control/` | SYS-REQ-050 | A0 | M |
| ELEC-REQ-073 | Hall inputs shall have pull-ups, RC filtering (time constant ≤ 1/10 of the minimum Hall period at max speed, TBC) and ESD protection; they shall connect to timer inputs capable of Hall-interface capture. | Noise immunity. | I, T | Clean edges captured with motor running at max speed and PWM active. | `results/motor_control/` | SYS-REQ-050 | A0/A1 | H |
| ELEC-REQ-074 | Encoder supply shall be filtered, current-limited or fused, and **switched or monitored** so that firmware can detect a supply failure. | Encoder faults must be detected (CTRL-REQ-001). | T | Removing encoder supply yields an encoder fault report. | `tests/safety/` | SYS-REQ-080 | A1 | H |
| ELEC-REQ-075 | The controller shall provide an **output-side absolute magnetic encoder** interface via **SPI** (with parity/CRC and diagnostic word read-back) and optionally ABI. Candidate ICs: AS5047P, AS5048A, MT6835 (candidate: verify against datasheet). | ACT-DEC-010; SYS-REQ-024, SYS-REQ-052 (joint loop on the output encoder). | I, T | SPI reads at ≥ 1 kHz (position loop) with error flags and parity checked; diagnostic flags available to firmware. | `results/motor_control/` | SYS-REQ-024, SYS-REQ-052 | A1 | M |
| ELEC-REQ-076 | Output encoder resolution shall be ≥ 14 bit (≈ 0.022° per count) (TBC; final value set by the position-error and repeatability limits of SYS-REQ-025) with documented integral non-linearity after calibration. | Joint position accuracy. | A, T | Datasheet resolution recorded; INL characterised on the fixture against a reference (method TBD in `docs/validation/`). | `results/mechanical/`, `results/motor_control/` | SYS-REQ-025 | A1 | H |
| ELEC-REQ-077 | Encoder signal integrity shall be ensured for the cable length used: on-board (≤ 50 mm) direct connection; ≤ 300 mm with twisted pairs and series termination (TBC); > 300 mm requires differential signalling (RS-422 ABI or an SPI-over-differential buffer) or relocation of the encoder interface. SPI clock rate shall be derated for cable propagation and capacitance. | Long single-ended SPI cables near motor phases fail intermittently. | A, T | Eye/timing capture at the chosen clock rate and length with the motor running at peak current; zero CRC/parity errors over ≥ 10⁶ reads (TBC). | `results/motor_control/` | SYS-REQ-024 | A1 | M |
| ELEC-REQ-078 | Encoder cables shall be routed away from motor phase wiring, or shielded with the shield terminated at the controller end (single-point, TBC). | EMI from PWM edges. | I | Inspection at assembly; harness drawing. | `hardware/connectors/` | SYS-REQ-024 | A1 | H |
| ELEC-REQ-079 | Encoder interfaces shall tolerate hot-unplug and connector intermittency without damage, and the loss of signal shall be detectable (ABI line-break detection or SPI read-back timeout/flags). | Encoder fault detection (CTRL-REQ-001). | T | Unplug test during operation on fixture: fault detected, PWM disabled per KA-REQ-FW, no damage. | `tests/safety/` | SYS-REQ-080 | A1 | M |
| ELEC-REQ-080 | Absolute output position should be available at power-up without motion (TBC). | Avoids homing motion into a hard stop with the arm attached. | D | Power-up report gives joint angle within tolerance of a reference. | `results/motor_control/` | SYS-REQ-053 | A1 | H |
| ELEC-REQ-081 | The output encoder magnet and IC placement constraints (air gap, radial offset, magnet grade) shall be provided to the Mechanical Intern and recorded as an interface constraint; mechanical mounting is owned by [S2]. | RACI: Electronics leads electrical side, Mechanical leads mounting. | I | Constraint recorded in [S4]/[S2]; M2 and E2 reviews confirm. | `docs/electronics/`, `requirements/INTERFACE_REQUIREMENTS.md` | SYS-REQ-034 | A1 | M |

### 6.7 Motor-control MCU

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| ELEC-REQ-085 | The motor-control MCU shall be an **STM32G4-family device (proposed default, e.g. STM32G431/G474, candidate: verify)**, with **TI C2000** as the evaluated alternative. The selection shall be recorded in ACT-DEC-004 (currently PROPOSED). | SYS-REQ-055; intern skill set; moteus reference is STM32G4-based. | I | ACT-DEC-004 accepted with evaluation record. | `planning/v1/DECISIONS.md`, `planning/v1/tasks/ACT-01/ACT-01-002/` | SYS-REQ-055 | A0 | M |
| ELEC-REQ-086 | The MCU shall provide **advanced-control timers** with ≥ 3 complementary PWM pairs, hardware dead-time insertion, centre-aligned mode and ADC trigger outputs. | Complementary PWM with dead time (SYS-REQ-055). | I | Datasheet check in selection record. | `planning/v1/tasks/ACT-01/ACT-01-002/` | SYS-REQ-055 | A0 | M |
| ELEC-REQ-087 | The MCU timer shall have a **hardware break/fault input** that forces all PWM outputs to a defined safe level (all switches off) within ≤ 1 µs (TBC) without firmware intervention, and that is latched until cleared by firmware. | Hardware overcurrent and e-stop path (ELEC-REQ-110, 112). | I, T | Test: assert break input while switching; PWM outputs inactive within limit (scope). | `tests/hardware/` | SYS-REQ-055, SYS-REQ-081 | A0 | M |
| ELEC-REQ-088 | The MCU shall provide **≥ 2 ADCs capable of simultaneous/injected sampling triggered by the PWM timer**, ≥ 12-bit resolution, conversion time compatible with ELEC-REQ-040. | Synchronised phase-current sampling. | I, T | Datasheet; measured trigger-to-result latency. | `results/motor_control/` | SYS-REQ-055 | A0 | M |
| ELEC-REQ-089 | The MCU shall have a hardware **FPU** (single precision minimum) or equivalent fixed-point performance sufficient to run the FOC current loop at 20 kHz with total CPU load ≤ 70 % (TBC, KA-REQ-FW). Analogue comparators and op-amps on chip (as in STM32G4) may be used for current sense and overcurrent. | FOC compute; SYS-REQ-055 "adequate compute". | A, T | Measured ISR execution time and CPU load on hardware (KA-REQ-FW timing budget). | `results/motor_control/` | SYS-REQ-055 | A0 | M |
| ELEC-REQ-090 | The MCU shall provide **CAN/FDCAN** (A1), **SPI** (output encoder), **timer encoder mode** (ABI) and **Hall-interface capture**, **USB or UART** (A0/debug), and an **independent watchdog** clocked from an independent oscillator. | Required peripherals per baseline. | I | Pin and peripheral allocation table with no conflicts. | `docs/electronics/` | SYS-REQ-055, SYS-REQ-061 | A0/A1 | M |
| ELEC-REQ-091 | The MCU shall have sufficient **non-volatile memory** for firmware, calibration and parameters with CRC (≥ 2 pages/sectors reserved for parameters, TBC), and a unique device ID for serialisation. | Parameter storage (KA-REQ-FW). | I | Memory map recorded. | `docs/firmware/` | SYS-REQ-053 | A0 | H |
| ELEC-REQ-092 | The MCU clock shall use an **external crystal or oscillator** with ≤ ±0.5 % total tolerance (≤ ±50 ppm recommended, TBC) when CAN is used. | CAN bit-timing tolerance at 1 Mbit/s. | A | Clock tolerance analysis against CAN bit timing. | `docs/electronics/` | SYS-REQ-061 | A1 | M |
| ELEC-REQ-093 | Spare GPIOs (≥ 2, TBC) shall be brought out to test points for timing measurement (ISR toggling) and debug. | Timing verification in KA-REQ-FW. | I | Test points present on A1 PCB; A0 board pins identified. | `hardware/motor_controller/custom_pcb/pcb/` | SYS-REQ-055 | A0/A1 | H |
| ELEC-REQ-094 | The MCU's peripheral and pin allocation on the A0 board should be reproducible on the A1 PCB (same MCU family and, where practical, the same timer/ADC/pin assignments), to maximise firmware reuse. | "Build once, evolve"; SYS-REQ-006. | I | Pin-map comparison A0 vs A1 recorded at E2. | `docs/electronics/` | SYS-REQ-006 | A1 | H |

### 6.8 Communication hardware

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| ELEC-REQ-100 | The controller shall provide a **USB (full-speed) or UART** interface for commands, configuration, telemetry ≥ 100 Hz and debugging in A0, retained as a debug port in A1. | SYS-REQ-060; ACT-DEC-006. | D | Host tool connects and streams telemetry at ≥ 100 Hz without frame loss over 10 min (TBC). | `results/motor_control/` | SYS-REQ-060 | A0 | M |
| ELEC-REQ-101 | The USB/UART port shall be ESD-protected (IEC 61000-4-2 contact ±4 kV minimum, TBC) and shall not back-power the controller's power stage. | Bench robustness. | I, T | ESD device fitted; with only USB connected, the power stage cannot be enabled. | `tests/hardware/` | SYS-REQ-060, SYS-REQ-080 | A1 | H |
| ELEC-REQ-102 | Ground loops between the host PC (USB) and the motor power ground shall be addressed: either a **USB isolator** is used on the bench or the A1 design provides isolation of the debug port (decision TBD at E1). | PC USB ports can be damaged by motor ground shifts. | I | Bench setup record states isolator used, or design decision recorded. | `results/motor_control/`, `planning/v1/DECISIONS.md` | SYS-REQ-060 | A0 | H |
| ELEC-REQ-103 | The A1 controller shall include an **ISO 11898-2 CAN transceiver** connected to the MCU FDCAN peripheral, supporting **classic CAN 2.0B at 1 Mbit/s** (baseline) and preferably **CAN FD** data rates (TBC), with bus-fault protection (CANH/CANL to ±40 V or better, TBC). | SYS-REQ-061; baseline CAN definition. | I, T | Datasheet recorded; 1 Mbit/s communication over the reference harness at 500 Hz command/feedback per node with zero error frames over 10 min (TBC). | `results/integration/` | SYS-REQ-061 | A1 | M |
| ELEC-REQ-104 | **120 Ω termination** shall be selectable on the controller (jumper, solder bridge or switch), optionally split termination (2 × 60 Ω with a capacitor to ground). | Only bus ends are terminated. | I, T | Measured CANH–CANL resistance with termination on/off. | `tests/hardware/` | SYS-REQ-061 | A1 | M |
| ELEC-REQ-105 | The CAN connector arrangement shall support a **daisy-chained bus** (two connectors or a pass-through) with a stub length ≤ 0.3 m (TBC) at 1 Mbit/s. | Multi-joint humanoid bus. | I | Harness design inspected. | `hardware/connectors/` | SYS-REQ-061 | A1 | H |
| ELEC-REQ-106 | The **CAN isolation decision** (galvanically isolated transceiver vs non-isolated with common ground) shall be made at E1 and recorded in DECISIONS.md, considering ground shift between actuators, cost and the robot power architecture. Status: **TBD**. | Isolation affects robustness and BOM. | I | Decision recorded. | `planning/v1/DECISIONS.md` | SYS-REQ-061 | A1 | H |
| ELEC-REQ-107 | CAN lines shall have ESD protection and common-mode filtering provision (footprint for a common-mode choke, fit optional). | EMC robustness. | I | Footprints present. | `hardware/motor_controller/custom_pcb/schematics/` | SYS-REQ-061 | A1 | H |
| ELEC-REQ-108 | The node ID (1–63) should be settable by firmware parameter; a hardware strap is optional (TBC). | Multiple actuators on one bus. | D | Two nodes on one bus with different IDs operate correctly. | `results/integration/` | SYS-REQ-061 | A1 | L |
| ELEC-REQ-109 | The CAN transceiver shall have a **standby/silent control** from the MCU and shall not disturb the bus when the controller is unpowered (dominant-timeout feature and unpowered-node high-impedance). | Bus availability for the other joints. | I, T | Powering down one node does not stop communication between others. | `results/integration/` | SYS-REQ-061 | A1 | H |

### 6.9 Safety hardware

Safe-state policy and hazard analysis are owned by [S5]. This section defines the hardware means.

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| ELEC-REQ-110 | A **hardware overcurrent comparator** shall monitor phase (or DC-link) current and drive the MCU **timer break input** directly, disabling all PWM outputs without firmware involvement. Threshold proposed at 1.2–1.5 × the configured peak phase-current limit and below the MOSFET and shunt safe limits (TBC). | SYS-REQ-080, SYS-REQ-081. Firmware alone is too slow or may be hung. | A, T | Injected overcurrent (pulse test or short fixture) disables PWM within ≤ 2 µs from threshold crossing (TBC) with firmware in a busy loop. | `tests/safety/`, `results/motor_control/` | SYS-REQ-080, SYS-REQ-081 | A0/A1 | M |
| ELEC-REQ-111 | A **hardware ENABLE (e-stop) input** shall remove motor drive **independent of firmware**: deasserting it shall (a) disable the gate driver (enable pin and/or gate-driver supply) and (b) assert the PWM break input. Re-assertion shall not by itself re-enable motion; firmware shall require an explicit enable command. | SYS-REQ-081 hardware means to remove motor power. | T | With firmware deliberately commanding torque (test build) or hung (debugger halt), deasserting ENABLE stops phase current within ≤ 10 ms (TBC); re-asserting does not restart motion. | `tests/safety/` | SYS-REQ-081 | A1 | M |
| ELEC-REQ-112 | The ENABLE input shall be **fail-safe**: open circuit, broken wire or loss of supply on the input shall result in the disabled state. | Fail-safe e-stop wiring. | T | Disconnecting the ENABLE connector disables drive. | `tests/safety/` | SYS-REQ-081 | A1 | M |
| ELEC-REQ-113 | The ENABLE state shall be readable by the MCU (separate from the hardware path) so that firmware can report it and enter SAFE_STOP/FAULT. | Diagnostics and state reporting. | T | Telemetry shows ENABLE state change within one telemetry period. | `tests/firmware/` | SYS-REQ-062, SYS-REQ-081 | A1 | M |
| ELEC-REQ-114 | In A0, where the development board lacks a hardware enable path, an **external bench e-stop** shall remove motor power (by interrupting the DC supply to the board, or the motor phases via a suitably rated contactor, TBC) and its operation shall be checked before each session. | SYS-REQ-081 (bench); SYS-REQ-084. | I, T | Bench e-stop check recorded in each session log. | `results/motor_control/` | SYS-REQ-081, SYS-REQ-084 | A0 | M |
| ELEC-REQ-115 | The design shall include an **independent watchdog** (MCU IWDG, optionally an external window watchdog) whose expiry resets the MCU, with gate drive defaulting to OFF during and after reset (ELEC-REQ-036). | Firmware hang protection. | T | Forced firmware hang (test build) → reset within watchdog period; no phase current during reset; reset cause readable. | `tests/safety/` | SYS-REQ-080 | A0 | M |
| ELEC-REQ-116 | The gate driver's **nFAULT** output (UVLO, overtemperature, V_DS monitor if present) shall connect to the MCU and should also be routed to the timer break input (via logic). | Hardware fault coverage. | I, T | Forced driver UVLO reported to firmware and PWM disabled. | `tests/safety/` | SYS-REQ-080 | A1 | H |
| ELEC-REQ-117 | The safe state hardware shall support both **coast** (all switches off, default) and **active short / phase short** (all low-side switches on) as configurable by firmware (choice TBC in [S5]); hardware break shall always result in **all switches off**. | Baseline safe state default: disable PWM (coast), optional active damping. | I, T | Both modes demonstrated on the fixture; break input always yields all-off. | `tests/safety/` | SYS-REQ-080 | A1 | H |
| ELEC-REQ-118 | The A1 controller should provide an **open-drain fault output** for the robot-level safety chain (TBC). | Lets the robot see an actuator fault without the bus. | T | Output asserts on FAULT. | `tests/safety/` | SYS-REQ-080 | A1 | L |
| ELEC-REQ-119 | The controller shall provide **status LEDs**: power present (hardware-driven), firmware heartbeat/state, and fault. LED codes are defined in KA-REQ-FW. | Bench diagnostics. | I, D | LEDs visible and behaving as specified. | `tests/hardware/` | SYS-REQ-062 | A0/A1 | H |
| ELEC-REQ-120 | Safety-relevant hardware (ELEC-REQ-110 to 117) shall be reviewed at E2 by the **Independent Electrical/Firmware Reviewer**; if none is available the review is recorded `NOT_VERIFIED` and gate E2 is blocked. | ACT-DEC-014. | I | Review record in `audit/electronics/` with reviewer distinct from author. | `audit/electronics/` | SYS-REQ-106 | A1 | M |

### 6.10 A0 development board

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| ELEC-REQ-125 | The A0 motor-control **development board shall be selected in ACT-01-002** using the criteria of section 7, and recorded in ACT-DEC-005 (currently PROPOSED). | SYS-REQ-005; decision not yet taken. | I | Completed scoring table and decision record. | `planning/v1/tasks/ACT-01/ACT-01-002/`, `planning/v1/DECISIONS.md` | SYS-REQ-005 | A0 | M |
| ELEC-REQ-126 | The selected A0 board shall support **24 V** input and the selected motor's continuous current with margin, phase-current sensing suitable for FOC, an encoder/Hall input, a UART/USB link and SWD debug access. | Minimum A0 functionality. | I, D | Checklist completed against board documentation; bring-up demonstrates each function. | `hardware/motor_controller/development_board/` | SYS-REQ-005, SYS-REQ-050 | A0 | M |
| ELEC-REQ-127 | Any modification made to the A0 board (component changes, wires, added protection) shall be recorded with photos and a schematic note. | Reproducibility (SYS-REQ-103). | I | Record exists for each board serial. | `hardware/motor_controller/development_board/` | SYS-REQ-103 | A0 | M |
| ELEC-REQ-128 | A **spare A0 board** should be procured (budget permitting) because bring-up faults may destroy the power stage. | Schedule risk. | I | BOM entry or recorded decision not to. | `hardware/bom/ELECTRICAL_BOM.csv` | SYS-REQ-100 | A0 | L |
| ELEC-REQ-129 | Licences of any vendor firmware or motor-control libraries supplied with the A0 board shall be recorded before code is copied into the repository. | ACT-DEC-012 proprietary repository. | I | Licence record. | `docs/firmware/` | SYS-REQ-054 | A0 | M |

### 6.11 A1 custom controller PCB

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| ELEC-REQ-135 | The A1 controller PCB shall **fit at the rear of the actuator** (behind the motor) within the envelope allocated in [S2]/[S1] (outline and height TBD, proposed circular or rounded outline sized to the motor diameter), with mounting holes agreed with the Mechanical Intern. | SYS-REQ-007 (MCU inside the actuator). | I | Board outline matches the CAD envelope; fit check at M2/E2 using a 3D model export. | `hardware/motor_controller/custom_pcb/pcb/`, `mechanical/` CAD | SYS-REQ-007 | A1 | M |
| ELEC-REQ-136 | The PCB 3D model (STEP) shall be provided to the Mechanical Intern before M2, and connector positions, keep-outs and cable exits shall be agreed in [S4]. | RACI: Electronics provides PCB/connector constraints. | I | STEP file and interface record exist before M2. | `hardware/motor_controller/custom_pcb/pcb/` | SYS-REQ-037 | A1 | M |
| ELEC-REQ-137 | The PCB shall use **locking, keyed connectors** for power, motor phases, encoders, CAN and ENABLE; connector types shall be rated for the currents of section 5.2 and the thermal environment. | Vibration and mis-mating. | I | Connector datasheets in BOM; rating check. | `hardware/bom/ELECTRICAL_BOM.csv` | SYS-REQ-037 | A1 | M |
| ELEC-REQ-138 | The **high-current commutation loop** (bus capacitor → high-side MOSFET → low-side MOSFET → shunt → back to capacitor) shall be minimised in area, with ceramic capacitors placed adjacent to each half-bridge and a solid return plane on the adjacent layer. | Ringing, EMI, V_DS overshoot (ELEC-REQ-031). | I, T | Layout review checklist item; measured ringing within ELEC-REQ-031. | `audit/electronics/`, `results/motor_control/` | SYS-REQ-044 | A1 | M |
| ELEC-REQ-139 | Grounding shall follow a documented strategy: power ground and analogue/signal ground joined at a **single star point** (typically at the shunt/bulk-capacitor return), with Kelvin sense traces routed as differential pairs from the shunt pads to the amplifier. | Current-sense accuracy and noise. | I | Layout review; grounding note in design notes. | `docs/electronics/`, `audit/electronics/` | SYS-REQ-050 | A1 | M |
| ELEC-REQ-140 | The PCB shall have a defined **thermal path** from the MOSFETs to the actuator housing (thermal vias, exposed pads, thermal interface material, clamping), designed with the Mechanical Intern; copper weight ≥ 2 oz outer layers (TBC). | Section 5.7 losses must reach the housing. | A, T | Thermal analysis at E2; thermal test (section 6.15). | `hardware/motor_controller/custom_pcb/`, `results/thermal/` | SYS-REQ-020, SYS-REQ-044 | A1 | M |
| ELEC-REQ-141 | Copper widths and via counts for high-current paths shall be sized for the continuous current with a temperature rise ≤ 20 °C (TBC) per IPC-2152 (or equivalent) and checked for the peak profile. | Trace heating. | A | Calculation recorded. | `hardware/motor_controller/custom_pcb/` | SYS-REQ-044 | A1 | M |
| ELEC-REQ-142 | The PCB shall provide **test points** for: V_BUS, logic rails, each phase switch node, each shunt-amplifier output, gate signals of at least one leg, the break input, PWM/ADC trigger debug GPIOs, encoder signals, CANH/CANL and ground (several, near measurement points). | Bring-up and E3 verification. | I | Test-point list checked against layout. | `hardware/motor_controller/custom_pcb/` | SYS-REQ-103 | A1 | M |
| ELEC-REQ-143 | The PCB shall provide an **SWD programming/debug header** (with NRST and SWO, proposed 10-pin 1.27 mm Cortex Debug, TBC) accessible with the actuator assembled or through a service opening. | Firmware update and debug without disassembly. | I, D | Programming demonstrated on the assembled actuator. | `results/integration/` | SYS-REQ-066 | A1 | M |
| ELEC-REQ-144 | Each PCB shall carry a **hardware revision and serial number** (silkscreen and readable by firmware via straps, ID resistor or OTP, TBC). | SYS-REQ-067 report hardware version; SYS-REQ-103 test records. | I, D | Firmware reports hardware revision. | `tests/hardware/` | SYS-REQ-067, SYS-REQ-103 | A1 | H |
| ELEC-REQ-145 | Design data (schematic, layout source, Gerbers or fabrication outputs for the release, assembly drawing, BOM) shall be stored under `hardware/motor_controller/custom_pcb/` per the repository rules; generated outputs are attached to releases rather than committed when large. | SYS-REQ-107. | I | Repository inspection. | `hardware/motor_controller/custom_pcb/` | SYS-REQ-107 | A1 | M |
| ELEC-REQ-146 | The schematic shall pass an **ERC** and the layout a **DRC** against the selected fabricator's capabilities, with waivers documented. | Design quality. | I | Reports archived with the E2 review. | `audit/electronics/` | SYS-REQ-102 | A1 | M |
| ELEC-REQ-147 | Creepage and clearance on the 24–32 V bus shall be ≥ fabricator minimum and ≥ 0.5 mm (TBC); conformal coating is not required for the laboratory environment (TBC). | Low voltage, indoor lab. | I | DRC rule set recorded. | `hardware/motor_controller/custom_pcb/` | SYS-REQ-090 | A1 | L |
| ELEC-REQ-148 | The A1 PCB bring-up shall follow a staged procedure: unpowered inspection and resistance checks; logic rails only (current-limited ≤ 100 mA, TBC); MCU programming; gate signals with power stage unpowered; power stage at low voltage (≈ 12 V) and current limit ≤ 1 A with no motor; then motor at low current. | SYS-REQ-084 staged risk reduction. | I, D | Completed bring-up checklist per board. | `tests/hardware/`, `results/motor_control/` | SYS-REQ-084 | A1 | M |
| ELEC-REQ-149 | The A1 PCB shall be **pin- and peripheral-compatible with the A0 firmware** where practical (ELEC-REQ-094), and differences shall be isolated in the firmware platform layer (KA-REQ-FW). | Firmware reuse. | I | Board-support differences listed. | `docs/electronics/` | SYS-REQ-006 | A1 | H |
| ELEC-REQ-150 | If PCB fabrication or procurement slips, the A0 development board shall remain usable as the A1 controller for mechanical integration testing (externally mounted), and this fallback shall be recorded. | Schedule rule: a custom PCB is not a prerequisite for A0 success. | I | Fallback documented in task plan. | `planning/v1/tasks/ACT-01/ACT-01-005/` | SYS-REQ-005 | A1 | H |

### 6.12 EMC and ESD

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| ELEC-REQ-155 | External connectors (USB, CAN, ENABLE, encoder) shall have ESD protection rated ≥ ±4 kV contact (IEC 61000-4-2 level 2, TBC). | Laboratory handling. | I, T | Protection devices present; informal ESD gun test if equipment is available (otherwise NOT_VERIFIED recorded). | `tests/hardware/` | SYS-REQ-090 | A1 | H |
| ELEC-REQ-156 | Motor phase wiring shall be twisted (three-phase twist) and kept as short as practical; the motor frame and housing bonding to controller ground shall be defined (TBC). | Radiated emissions and common-mode currents. | I | Harness inspection; bonding decision recorded. | `hardware/connectors/` | SYS-REQ-090 | A1 | H |
| ELEC-REQ-157 | The controller shall operate without communication errors, encoder errors or spurious resets while switching at peak current in its final assembly (functional EMC). Formal EMC compliance testing is out of scope for A0–A2. | Self-compatibility. | T | 30 min (TBC) peak-duty run on the fixture with zero encoder CRC errors, zero CAN error frames, no resets. | `results/integration/` | SYS-REQ-080 | A1 | M |
| ELEC-REQ-158 | The DC input should include provision for a common-mode/differential filter (footprints) to reduce conducted emissions onto the robot bus. | Multi-actuator robot bus. | I | Footprints present. | `hardware/motor_controller/custom_pcb/schematics/` | SYS-REQ-090 | A1 | L |

### 6.13 Bench equipment and test setup

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| ELEC-REQ-165 | All bring-up and testing shall use a **current-limited bench DC supply** (proposed ≥ 30 V, ≥ 10 A, adjustable current limit; ≥ 15 A recommended, see 5.3), with the current limit set to the lowest value that permits the test, until protection functions are verified. | SYS-REQ-045, SYS-REQ-084. | I | Each test record states PSU model, voltage and current limit. | `results/motor_control/` | SYS-REQ-045, SYS-REQ-084 | A0 | M |
| ELEC-REQ-166 | A **bench emergency stop** (latching, mushroom head, clearly marked) shall be within reach of the operator and shall remove motor power (ELEC-REQ-114 in A0, ELEC-REQ-111 in A1). | SYS-REQ-081. | I, T | Pre-session check recorded. | `results/motor_control/` | SYS-REQ-081 | A0 | M |
| ELEC-REQ-167 | Initial motor tests shall be at **reduced voltage (≈ 12 V, TBC) and low current limit (≤ 2 A, TBC)** with the motor unloaded and clamped, before stepping to 24 V and higher currents. | SYS-REQ-084. | I | Session log shows staged steps. | `results/motor_control/` | SYS-REQ-084 | A0 | M |
| ELEC-REQ-168 | Minimum instruments: digital multimeter, oscilloscope (≥ 100 MHz, ≥ 4 channels recommended, ≥ 2 minimum), and preferably a DC current probe or a calibrated shunt for phase-current measurement; a USB isolator for the host (ELEC-REQ-102). Laboratory equipment is outside the project budget (baseline section 4). | Verification of timing, ringing, current. | I | Instrument list and calibration status in each test record. | `results/motor_control/` | SYS-REQ-103 | A0 | H |
| ELEC-REQ-169 | All loaded and peak-torque tests shall be performed **only on a restrained, guarded, instrumented fixture**; manually resisting the actuator or attaching it to a person is prohibited. | ACT-DEC-015; SYS-REQ-083. | I | Test records reference the fixture and guard. | `results/` | SYS-REQ-083 | A0–A2 | M |
| ELEC-REQ-170 | Every electrical test record shall include hardware revision/serial, firmware version, supply voltage and limit, load, ambient temperature, instruments and measured results. | SYS-REQ-103. | I | Record template used. | `results/` | SYS-REQ-103 | A0 | M |

### 6.14 Wiring and connectors

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| ELEC-REQ-175 | Motor phase wiring and DC power wiring shall be sized for the **continuous phase/supply current with ≤ 20 °C rise (TBC)** and verified for the peak profile. Proposed starting point: **≥ 16 AWG (≈ 1.3 mm²) silicone-insulated** for phase and DC leads at currents up to ≈ 15 A continuous; reassess if the selected motor exceeds this (Kt = 0.05 case: 11.8 A amplitude continuous, 29.4 A amplitude peak). Motor leads supplied by the manufacturer may be used as supplied if their rating covers the current. | Wire heating and voltage drop. | A, I | Calculation recorded with selected motor; inspection. | `hardware/connectors/` | SYS-REQ-044 | A0/A1 | M |
| ELEC-REQ-176 | Power and phase connectors shall be **locking** (positive latch or screw retention), rated ≥ 1.25 × the continuous current at the maximum internal temperature, and polarised/keyed so that power cannot be mated to a signal connector. | Mis-mating and vibration. | I | Datasheet rating and keying check. | `hardware/bom/ELECTRICAL_BOM.csv` | SYS-REQ-037 | A1 | M |
| ELEC-REQ-177 | Bench power leads shall be ≤ 1 m (TBC) twisted pair, with a fuse at the PSU end (ELEC-REQ-009). Long leads add inductance and inrush overshoot. | Hot-plug overshoot. | I | Bench record. | `results/motor_control/` | SYS-REQ-045 | A0 | H |
| ELEC-REQ-178 | All crimp terminations shall use the manufacturer's specified crimp tool or be inspected (pull test sample); soldered joints on stranded phase wires shall be strain-relieved. | Connector reliability. | I | Harness inspection checklist. | `hardware/connectors/` | SYS-REQ-092 | A1 | H |
| ELEC-REQ-179 | The harness shall accommodate the full joint range (0–135°) where any cable crosses the rotating interface (e.g. to an output encoder on a rotating part), with a defined bend radius and no strain at end stops. | Cable fatigue at the elbow. | I, T | Range-of-motion cycling test with continuity monitoring (cycles TBD). | `results/mechanical/` | SYS-REQ-023 | A1 | H |
| ELEC-REQ-180 | Wire colours and labels shall follow a documented convention (e.g. red V+, black GND, phases U/V/W labelled), defined in [S4]. | Wiring errors. | I | Inspection. | `hardware/connectors/` | SYS-REQ-037 | A0 | H |
| ELEC-REQ-181 | Encoder and CAN cables shall use twisted pairs (CANH/CANL pair, 120 Ω nominal characteristic impedance for CAN), separated from phase wiring by ≥ 20 mm where routed in parallel (TBC). | Signal integrity. | I | Harness inspection. | `hardware/connectors/` | SYS-REQ-061 | A1 | H |

### 6.15 Thermal limits and derating

| ID | Requirement | Rationale | Verification | Acceptance criterion | Evidence location | Parent SYS-REQ | Phase | Priority |
|---|---|---|---|---|---|---|---|---|
| ELEC-REQ-185 | The controller shall have defined thermal limits: **maximum power-stage (NTC) temperature T_ctrl,max = TBD °C**, with a warning/derating threshold T_ctrl,derate = TBD °C below it. Placeholder for A0 bring-up only: derate from 80 °C, fault at 95 °C (TBC), subject to the selected components' ratings and housing-touch limits. | Component life and safety; baseline: controller ≤ TBD °C. | A, T | Values approved at E2; thermal test confirms NTC-to-junction offset so that T_j ≤ 125 °C (TBC) at T_ctrl,max. | `results/thermal/` | SYS-REQ-080, SYS-REQ-020 | A1 | M |
| ELEC-REQ-186 | The hardware shall support continuous operation at the continuous phase current of section 5.2 at the reference ambient (TBD in [S1]) with the NTC temperature stabilising below T_ctrl,derate. | Continuous torque (SYS-REQ-020) must not be limited by the controller. | T | Thermal-stability test (criterion in `docs/validation/VALIDATION_PLAN.md`, e.g. < 1 °C change over 10 min, TBC) passes at 10 N·m on the fixture. | `results/thermal/` | SYS-REQ-020 | A1 | M |
| ELEC-REQ-187 | The hardware shall support the approved **peak profile** (20 or 25 N·m, ≤ 2 s, ≤ 10 % duty placeholder, TBC) without exceeding T_ctrl,max or MOSFET junction limits. | Peak torque (SYS-REQ-021). | A, T | Peak-profile test with temperature logging. | `results/thermal/` | SYS-REQ-021 | A1 | M |
| ELEC-REQ-188 | Firmware **current derating** between T_ctrl,derate and T_ctrl,max shall be possible using the hardware temperature measurement (implementation in KA-REQ-FW). | Graceful degradation instead of abrupt fault. | T | Derating curve demonstrated. | `tests/firmware/` | SYS-REQ-080 | A1 | H |
| ELEC-REQ-189 | Components shall be derated: capacitors ≤ 80 % voltage and ripple rating; resistors ≤ 60 % power; MOSFETs per ELEC-REQ-031/032; connectors per ELEC-REQ-176. | Reliability. | A | Derating table in the E2 package. | `hardware/motor_controller/custom_pcb/` | SYS-REQ-044 | A1 | H |
| ELEC-REQ-190 | **Accessible surface temperature** of the controller enclosure/housing shall be ≤ TBD °C (proposed ≤ 60 °C for lab handling, TBC in [S5]). | Burn hazard. | T | Thermal test measures housing hot spot. | `results/thermal/` | SYS-REQ-082 | A1 | H |
| ELEC-REQ-191 | Motor winding temperature limit shall be taken from the selected motor's insulation class/datasheet with ≥ 10 °C margin (TBC), and monitored per ELEC-REQ-063. | Motor protection. | A, T | Limit recorded; validated in thermal test. | `results/thermal/` | SYS-REQ-043, SYS-REQ-080 | A1 | M |
| ELEC-REQ-192 | Ambient temperature for rating is the reference ambient of [S1] (TBD); the controller shall be characterised at that ambient and the result extrapolated to the maximum ambient by analysis. | SYS-REQ-090. | A, T | Test ambient recorded; extrapolation documented. | `results/thermal/` | SYS-REQ-090 | A1 | H |

## 7. A0 development board selection criteria

ACT-DEC-005 is **PROPOSED**; the board is chosen in ACT-01-002. This table defines the **evaluation criteria and candidates, not a decision**. All candidate data must be verified against current vendor documentation and availability in India. No prices are given here; quotations go into `hardware/bom/ELECTRICAL_BOM.csv`.

### 7.1 Candidates (to be evaluated)

| Candidate | Class | Notes for evaluation (verify) |
|---|---|---|
| ST **B-G431B-ESC1** | Compact STM32G431-based ESC-style board with integrated power stage | Matches the proposed MCU family (ACT-DEC-004). Verify voltage and current rating against section 5.2, current-sensing topology, encoder/Hall connectivity, available debug access, thermal capacity, and whether CAN is exposed. |
| ST **NUCLEO-G474RE + X-NUCLEO-IHM08M1-class** power board | Two-board MCU + power-stage combination | Flexible pin access, full STM32G474, debugger on board. Verify power board voltage/current rating and shunt configuration, wiring robustness at high current, and suitability of the combination for encoder + output encoder + CAN. |
| **ODrive-class** controller | Commercial reference platform | Mature reference for FOC behaviour and tuning; useful as a **reference** to compare against in-house firmware. Verify the hardware version, licence of firmware and documentation, MCU family (may differ from ACT-DEC-004), and whether in-house firmware can be run on it. |

### 7.2 Evaluation criteria

Score each criterion 0 (fails), 1 (partially), 2 (meets), 3 (exceeds). "Gate" criteria must score ≥ 2 or the candidate is rejected.

| # | Criterion | Weight | Gate? | Evidence required |
|---|---|---|---|---|
| 1 | 24 V supply compatibility with margin to ≥ 28 V operating and regen transients | 3 | Yes | Board user manual / schematic |
| 2 | Continuous and peak phase-current rating vs selected motor (section 5.2), including thermal capability | 3 | Yes | Rating and thermal notes; calculation |
| 3 | Phase-current sensing suitable for FOC (topology, range, synchronous sampling) | 3 | Yes | Schematic, MCU ADC configuration |
| 4 | MCU family alignment with ACT-DEC-004 (STM32G4 proposed) and peripheral set (ELEC-REQ-086–090) | 3 | No | Datasheet |
| 5 | Encoder/Hall interface availability (motor-side ABI/SPI and an SPI for output encoder) | 3 | Yes | Pin availability table |
| 6 | Hardware overcurrent/break path and gate-driver fault reporting | 2 | No | Schematic |
| 7 | Debug access (SWD, ideally on-board debugger) and UART/USB | 2 | Yes | Board documentation |
| 8 | CAN availability (transceiver on board or easy addition) for A1 fallback | 1 | No | Schematic |
| 9 | Documentation quality and open reference firmware; licence compatibility (ACT-DEC-012) | 2 | No | Licence record |
| 10 | Availability and lead time in India; spare-board feasibility | 2 | Yes | Supplier quotation (BOM) |
| 11 | Cost within the A0 board item target (₹3–5k, provisional) | 2 | No | Supplier quotation (BOM) |
| 12 | Physical robustness for bench wiring (connectors, mounting holes, heat sinking) | 1 | No | Inspection |
| 13 | Transferability of pin map and firmware to the A1 custom PCB (ELEC-REQ-094) | 2 | No | Pin-map comparison |
| 14 | Community/learning value for the intern (examples, tooling) | 1 | No | Assessment |

The selection record shall include the completed score table, the total weighted score per candidate, gate-criterion failures, risks, and the proposed decision text for ACT-DEC-005. It is reviewed at E1.

## 8. Review gates (electronics)

Each gate review is recorded in `audit/electronics/` with findings classed CRITICAL, HIGH, MEDIUM, LOW or OBSERVATION and an outcome PASS, PASS_WITH_ACTIONS, FAIL or NOT_VERIFIED. A gate with an unresolved CRITICAL or HIGH finding, or with no independent reviewer (ACT-DEC-014), does not pass. A safety-critical defect is never treated as non-blocking to meet a deadline.

| Gate | Name | Indicative week | Entry criteria | Requirements reviewed | Exit evidence |
|---|---|---|---|---|---|
| **E0** | Requirements review | 1 | This document at rev ≥ 0.1; KA-REQ-SYS approved baseline | All ELEC-REQ: completeness, parent trace, verifiability, TBD list | Review record; open items assigned; traceability rows created in [T1] |
| **E1** | Component and board selection review | 2 | Motor shortlist with Kt/R/L/thermal data; A0 board scoring (section 7); MCU evaluation | 033, 034, 044, 050, 070–076, 085–092, 102, 106, 125–129, 165–168 | ACT-DEC-004 and ACT-DEC-005 decision proposals; section 5 recomputed with real Kt; isolation decision (106) |
| **E2** | Schematic and PCB design review | 5–7 (A1) | Schematic, layout, BOM, calculations (power stage, regen, thermal, shunts, wiring), STEP fit check with Mechanical | 001–015, 020–025, 030–044, 050–065, 075–081, 100–120, 135–158, 175–192 | ERC/DRC reports; derating table; independent review record; fabrication release |
| **E3** | Bring-up verification | 6–9 | Fabricated/assembled boards (or A0 board for A0 scope); bring-up procedure | 001–007, 015, 021, 024, 031, 035–040, 051–054, 060–064, 070–079, 087–089, 100–104, 110–119, 148, 157 | Bring-up checklists, scope captures, calibration records in `results/motor_control/`; fault-injection results in `tests/safety/` |
| **E4** | Final acceptance | 11–12 | All E3 actions closed; integrated actuator thermal and EMC-functional tests | All M and H requirements; thermal 185–192; Gate B/C electrical items | Traceability [T1] updated with status per requirement; acceptance record feeding Gates B and C |

A0 uses E0, E1 and E3 (development-board scope). E2 applies to the A1 custom PCB and to any A0 add-on hardware (e.g. external e-stop, regen clamp, encoder adapter board).

## 9. Flow-down coverage check

| SYS-REQ (allocated in KA-REQ-SYS section 11) | Covered by ELEC-REQ |
|---|---|
| SYS-REQ-005 (dev board A0, custom PCB A1) | 034, 125–129, 135–150 |
| SYS-REQ-040 (24 V nominal) | 001 |
| SYS-REQ-041 (range, withstand, reverse polarity) | 002–006, 010, 012, 014, 020–025, 060, 061 |
| SYS-REQ-042 (75–100 W motor) | Section 5.3, 059 (power budget; motor selection itself is in ACT-01-002) |
| SYS-REQ-043 (Kt, thermal data, 24 V, feedback) | Section 5.2, 063, 191 |
| SYS-REQ-044 (size from motor current) | 007, 031–033, 051, 055, 138, 140, 141, 175, 189 |
| SYS-REQ-045 (current-limited PSU) | 009, 024, 165, 177 |
| SYS-REQ-055 (motor-control MCU peripherals) | 037, 054, 085–094 |
| SYS-REQ-081 (power removal independent of firmware) | 011, 036, 087, 110–117, 166 |

## 10. Open items

| # | Item | Requirement(s) | Owner | Needed by |
|---|---|---|---|---|
| 1 | Motor selection and its Kt (amplitude convention), R_ph, L_d/L_q, pole pairs, Ke, thermal data; recompute section 5 | 032–034, 044, 051, 071, 175 | Electronics Intern (with Mechanical, PL approves) | E1 |
| 2 | Confirm operating range 20–28 V and withstand ≥ 32 V | 002, 003 | Electronics Intern / PL | E1, before A1 PCB start |
| 3 | Peak-torque duty profile (20 vs 25 N·m, duration, repetition, recovery) | 008, 032, 187 | Project Lead | E1 |
| 4 | Regeneration analysis with real data; brake chopper fit decision | 020, 022, 023 | Electronics Intern | E2 |
| 5 | MCU family decision ACT-DEC-004 | 085 | Electronics Intern / PL | E1 |
| 6 | A0 board decision ACT-DEC-005 | 125 | Electronics Intern / PL | E1 |
| 7 | Current-sensing topology for A1 (3-shunt vs 2-shunt vs inline) | 050 | Electronics Intern | E2 |
| 8 | CAN isolation decision; connector types; daisy-chain arrangement | 105, 106 | Electronics Intern / PL | E1 |
| 9 | Controller thermal limits T_ctrl,derate and T_ctrl,max; accessible-surface limit | 185, 190 | Electronics Intern with Safety reviewer | E2 |
| 10 | Reference ambient temperature range | 192 | Project Lead ([S1]) | Gate B |
| 11 | PCB envelope, mounting and thermal interface with the housing | 135, 140 | Electronics + Mechanical Interns | M2 / E2 |
| 12 | Safe-state choice (coast vs active short) for the gravity-loaded elbow | 117 | Project Lead ([S5]) | E2 |
| 13 | Encoder cable lengths and whether the output encoder is on a rotating or stationary part | 077, 079 | Mechanical + Electronics Interns | M2 / E2 |
| 14 | Hardware overcurrent threshold value | 110 | Electronics Intern | E2 |
| 15 | Inrush limit value and topology | 006 | Electronics Intern | E2 |

## 11. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
