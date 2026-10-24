# Kritva Actuator: Performance Characterisation

| Field | Value |
|---|---|
| Document ID | KA-DOC-VAL-PERF |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead (coordination); Mechanical Intern and Electronics/Embedded Intern (execution) |
| Reviewer / Approver | Independent reviewers / Project Lead |
| Applies to | A0 (MC tests), A1 (PC tests) |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** These are proposed procedures. Numeric pass limits marked "limit approved before test" must be recorded in the relevant task `ACCEPTANCE_CRITERIA.md` **before** execution. The results go to `results/`. This document holds procedures only, never results.

---

## 1. Purpose

This document defines the characterisation tests that measure the actuator's real performance against `requirements/ACTUATOR_SPECIFICATION.md`:

- A0: motor characterisation, MC-01 to MC-08;
- A1: integrated actuator characterisation, PC-01 to PC-14.

The results become the actuator's **measured datasheet**.

## 2. General conditions

| Condition | Requirement |
|---|---|
| Setup | Restrained fixture KA-FIX-0001 (TEST_EQUIPMENT §3), guard fitted for PC-04, PC-06 and impact tests |
| Supply | 24.0 V ± 0.2 V, unless the test says otherwise; PSU current limit recorded |
| Ambient | Recorded; reference 25 °C ± 5 °C (TBC) |
| Warm-up | State whether the test starts cold (soaked at ambient) or warm |
| Staging | Load increased per SAF-REQ-063 |
| People | Operator and observer for loaded tests (SAF-REQ-064) |
| Records | `results/<area>/YYYY-MM-DD_<ID>_<name>/` with a README (conditions), raw CSV data (columns `name_unit`) and plots |

## 3. A0: motor characterisation

| ID | Test | Method | Output |
|---|---|---|---|
| MC-01 | Phase resistance | DC injection (firmware C1) and a 4-wire measurement at ambient | R_ph (Ω) at T |
| MC-02 | Phase inductance | Voltage step or LCR meter at 1 kHz | L_d, L_q (H) |
| MC-03 | Back-EMF constant / Kv | Spin the motor with a drive motor or drill at a known speed; measure the line-to-line voltage | Ke, Kv |
| MC-04 | Torque constant Kt | Locked rotor on the lever arm: Iq steps versus measured torque | Kt (N·m/A), linearity, saturation onset |
| MC-05 | Cogging and friction torque | Slow speed sweep; Iq versus angle | Cogging ripple, friction |
| MC-06 | Rotor inertia | Acceleration test (known torque, measured α) or datasheet | J_rotor |
| MC-07 | Thermal: continuous current | Locked rotor at the current for 10 N·m output-equivalent torque (at the selected ratio) until stable | Winding/case temperature rise, time constant |
| MC-08 | Thermal: holding current | Locked rotor at the current for T_g (6.08 N·m output-equivalent) until stable | Holding thermal margin (TORQUE_AND_SPEED §6) |

## 4. A1: integrated actuator characterisation

| ID | Test | Procedure | Measurement | Pass criterion | Requirement |
|---|---|---|---|---|---|
| PC-01 | Horizontal holding | Fit the representative arm (1.5 kg at the measured centre of mass) plus 1 kg at 350 mm; command q = 90° (horizontal); hold for the approved duration | Position error, Iq, temperatures | Holds within the position-error limit; no thermal fault; temperatures stabilise | SYS-REQ-012; Gate B-1 |
| PC-02 | Gravity-torque verification | At the horizontal pose, measure the holding torque with the lever and load cell (output locked, motor off) and estimate it from Iq (motor on) | T_measured vs T_g calculated with the final mass properties | Agreement within the limit approved before the test | SYS-REQ-011/012; Gate B-2 |
| PC-03 | Continuous torque, thermal | Apply 10 N·m at the output (lever plus weights, or a brake) at the rated speed and duty until thermally stable (rate of change < 1 °C per 10 min, TBC) | Temperatures (motor, MOSFET, housing, surface), current, voltage | All below their limits; surface ≤ 60 °C (TBC) | SYS-REQ-020; Gate B-3 |
| PC-04 | Peak torque | Staged: 15 → 20 → 25 N·m (if adopted) for the approved duration and repetition, on the locked output with the torque sensor | Torque, current, temperatures, any permanent change | Reaches the approved peak; no damage; recovery as defined | SYS-REQ-021; Gate B-4 |
| PC-05 | Speed–torque curve | At 0, 2.5, 5, 7.5 and 10 N·m, measure the maximum speed at 24 V (and at 20 V and 28 V) | Speed versus torque | ≥ 45 RPM at the defined load range | SYS-REQ-022; Gate B-5 |
| PC-06 | Range of motion and stops | Slowly to each soft limit; record the angles; verify the hard-stop margin | Angles | Range ≥ 0–120° (target 135°); margins as configured | SYS-REQ-023 |
| PC-07 | Position accuracy | Command 10 positions across the range, approach from both directions; compare the output encoder with the external reference (inclinometer) | Error per point | ≤ the limit approved before the test | SYS-REQ-024/025; Gate B-6 |
| PC-08 | Repeatability | 30 repeats to 3 targets, from alternating directions | Spread (±3σ) | ≤ the limit approved before the test | SYS-REQ-025 |
| PC-09 | Backlash | Lock the output; apply ±1 N·m (TBC) at the input side (motor torque); measure motor_pos − N·q hysteresis. Alternatively, lock the motor and apply ±T at the output with a dial indicator on the lever | Backlash (arc-min) | ≤ the limit approved before the test | SYS-REQ-025; Gate B-6 |
| PC-10 | Control performance | Step responses (position 10°, velocity 1 rad/s) and sine tracking 0.5–5 Hz with the arm | Rise time, overshoot, settling, bandwidth | Per FIRMWARE CTRL targets (TBC) | SYS-REQ-026, 051 |
| PC-11 | Backdrivability | Powered off: slowly rotate the output via the lever and spring scale; measure the breakaway and running torque in both directions | Backdrive torque (N·m) | Recorded; compared across ratios | SYS-REQ-027 |
| PC-12 | Reflected inertia and friction | Torque-mode chirp or step; fit J and friction (Coulomb + viscous) | J_out, friction | Recorded (feeds SimulatedActuator) | SYS-REQ-027; IF-REQ-101 |
| PC-13 | Efficiency | Measure input electrical power and output mechanical power at 4 torques × 3 speeds | η_total, η_gearbox (estimated) | ≥ 85 % gearbox (assumption check) | SYS-REQ-028 |
| PC-14 | Torque-estimate accuracy | Compare τ_est (Kt·Iq·N·η) with the torque sensor across the range | Error versus torque | Recorded; limit approved before test if used for control | CTRL-REQ-017 |

## 5. Data analysis rules

1. Report the mean, standard deviation and minimum/maximum. State the number of samples.
2. Measurement uncertainty: list the instrument accuracy and estimate the combined uncertainty for the torque and angle results.
3. Plots: label the axes with units; include the test ID and date.
4. Compare each result with its requirement and pass limit in a summary table.
5. Every deviation becomes a non-conformance (VALIDATION_PLAN §9).

## 6. Measured datasheet (template, filled from the results)

| Parameter | Requirement | Measured | Test | Status |
|---|---|---|---|---|
| Continuous torque | 10 N·m | — | PC-03 | NOT_STARTED |
| Peak torque | 20 N·m (25 stretch) | — | PC-04 | NOT_STARTED |
| Speed at the continuous torque | 45 RPM target | — | PC-05 | NOT_STARTED |
| Holding at the horizontal pose | 6.08 N·m (calculated) | — | PC-01/02 | NOT_STARTED |
| Range | 0–120/135° | — | PC-06 | NOT_STARTED |
| Position accuracy | TBD | — | PC-07 | NOT_STARTED |
| Repeatability | TBD | — | PC-08 | NOT_STARTED |
| Backlash | TBD | — | PC-09 | NOT_STARTED |
| Backdrive torque | Record | — | PC-11 | NOT_STARTED |
| Efficiency | ≥ 85 % (gearbox) | — | PC-13 | NOT_STARTED |
| Mass | TBD | — | MI-09 | NOT_STARTED |

## 7. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
