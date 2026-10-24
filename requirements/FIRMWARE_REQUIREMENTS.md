# Kritva Actuator: Firmware Requirements

| Field | Value |
|---|---|
| Document ID | KA-REQ-FW |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Electronics/Embedded Intern |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A0, A1, A2 |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** All rates, thresholds and timeouts in this document are **proposed targets pending approval**. They become binding only when the Project Lead approves them and records the approval in `planning/v1/DECISIONS.md`. Values marked TBC need confirmation during ACT-01-002/ACT-01-003. Values marked TBD are not yet set.

---

## 1. Purpose

This document defines **what the actuator firmware must do**: motor control (FOC), joint control, calibration, limits, the state machine, fault detection and reaction, telemetry, communication, parameter storage, update and logging. It also sets the engineering standards the firmware is developed and verified against.

It derives from `requirements/SYSTEM_REQUIREMENTS.md` (SYS-REQ IDs in the *Parent* column). It is consistent with:

- `requirements/INTERFACE_REQUIREMENTS.md`, which defines the externally visible state machine, return codes and fault vocabulary. This document does not redefine them; it requires the firmware to implement them.
- `requirements/SAFETY_REQUIREMENTS.md`, which defines hazards, safe states and reaction times.

The firmware design itself is in `docs/firmware/FIRMWARE_ARCHITECTURE.md`, `docs/firmware/MOTOR_CONTROL.md` and `docs/firmware/CALIBRATION_PROCEDURE.md`.

## 2. Scope

**In scope**

- Firmware running on the actuator's motor-control MCU: the A0 development board, then the A1 custom PCB.
- Every module under `firmware/`: `platform/`, `foc/`, `motor_control/`, `encoder/`, `joint_control/`, `diagnostics/`, `communication/`.
- CAN firmware support code shared with `communication/can/firmware/`.

**Out of scope**

- Host software (`software/`), apart from the firmware side of each protocol.
- KritvaOS Edge firmware.
- Hardware-only protection functions. Those are specified in `requirements/ELECTRICAL_REQUIREMENTS.md`, although the firmware must configure and supervise them.

## 3. References

| Ref | Document |
|---|---|
| [R1] | `requirements/SYSTEM_REQUIREMENTS.md` (parent) |
| [R2] | `requirements/ACTUATOR_SPECIFICATION.md` |
| [R3] | `requirements/ELECTRICAL_REQUIREMENTS.md` |
| [R4] | `requirements/INTERFACE_REQUIREMENTS.md` (state machine, return codes, fault set) |
| [R5] | `requirements/SAFETY_REQUIREMENTS.md` (hazards, safe state, reaction times) |
| [R6] | `docs/interfaces/CAN_PROTOCOL.md` |
| [R7] | `docs/interfaces/ACTUATOR_INTERFACE.md` (API, parameters, USB/UART framing) |
| [R8] | `docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md` |
| [R9] | `docs/firmware/FIRMWARE_ARCHITECTURE.md`, `MOTOR_CONTROL.md`, `CALIBRATION_PROCEDURE.md` |
| [R10] | `planning/v1/DECISIONS.md` (ACT-DEC-004 MCU family, ACT-DEC-005 A0 board) |
| [R11] | `audit/firmware/FIRMWARE_REVIEW.md`, `FIRMWARE_ACCEPTANCE_AUDIT.md` |

## 4. Conventions

- **Requirement IDs.** `FW-REQ-NNN` covers firmware structure, platform, communication, storage and engineering process. `CTRL-REQ-NNN` covers control behaviour, limits, faults and safety reactions. `CTRL-REQ-001` is reserved for the detection of encoder, overcurrent and overtemperature faults.
- **Verification methods:**
  - T: test, on host unit tests, hardware-in-the-loop (HIL) or the bench.
  - A: analysis, such as timing or worst-case analysis.
  - I: inspection or code review.
  - D: demonstration.
- **Priority:** M (mandatory for the phase exit), H (high), L (goal).
- **Status values** (traceability CSV): NOT_STARTED, IN_PROGRESS, PASS, PASS_WITH_ACTIONS, FAIL, NOT_VERIFIED.
- **Units** in firmware are SI base units, following [R8]: rad, rad/s, rad/s², A, V, N·m, °C, s. Output-side quantities are prefixed `q_` (joint) and motor-side quantities `m_` in design documents.
- **MCU.** The family is **not frozen**. The proposed default is STM32G4, with TI C2000 as the evaluated alternative (ACT-DEC-004, PROPOSED). Requirements are written to be MCU-neutral. Where a requirement assumes a peripheral, the peripheral is named generically (for example "PWM break input").

## 5. Firmware context

```
            +-------------------------- actuator MCU ---------------------------+
 USB/UART <-|-> communication/ (CLI + binary)                                    |
 CAN      <-|-> communication/ (CAN protocol v1)  --->  command arbitration      |
            |                                             |                      |
            |   diagnostics/ <---- faults/telemetry ----  joint_control/         |
            |   (fault manager, log, counters, WDG)       (position/velocity     |
            |          |                                   loops, limits,        |
            |          v                                   trajectory)           |
            |   state machine (BOOT .. ESTOP)                 | Iq*              |
            |          |                                      v                  |
            |          |                               motor_control/ + foc/     |
            |          |                               (current loops, SVPWM)    |
            |          v                                      |                  |
            |   platform/ (HAL: PWM, ADC, timers, SPI, CAN, NVM, WDG, GPIO)      |
            +----------|--------------------------------------|------------------+
                       v                                      v
             encoder/ (motor + output)              gate driver -> inverter -> motor
```

## 6. Proposed timing baseline (TBC)

| Function | Proposed rate | Minimum acceptable | Notes |
|---|---|---|---|
| PWM carrier | 20 kHz | 16 kHz | Above audible range. Chosen together with the power-stage switching losses ([R3]). |
| Current sampling and current loop (FOC) | 20 kHz (once per PWM period) | 10 kHz | ADC triggered synchronously with PWM (centre-aligned). |
| Motor encoder read | 20 kHz | 10 kHz | Must be synchronous with the current loop for the commutation angle. |
| Velocity loop | 2 kHz | 1 kHz | The velocity estimate is filtered. |
| Position loop (output encoder) | 1 kHz | 500 Hz | Joint loop. |
| Output encoder read | 1–2 kHz | 1 kHz | SPI absolute read with validity check. |
| Supervisory and fault checks (software thresholds) | 1 kHz | 1 kHz | Hardware overcurrent is independent of this rate (section 13). |
| Thermal model update | 100 Hz | 10 Hz | |
| Telemetry over USB/UART | ≥ 100 Hz | 50 Hz | A0 tuning and logging. |
| CAN command and feedback | 500 Hz target, 1 kHz goal | 200 Hz | A1; the rate is set by the host ([R6]). |
| Command timeout | 50 ms default | Configurable 10–1000 ms | Leads to the safe state ([R5]). |

**Worked CPU budget example (illustrative, to be measured).** At 20 kHz the current-loop ISR has a 50 µs period.

- If the FOC ISR (ADC read, Clarke/Park transforms, two PI controllers, inverse Park, SVPWM, encoder angle) takes 12 µs, it uses **24 %** of the CPU.
- Velocity (2 kHz × 10 µs = 2 %), position (1 kHz × 20 µs = 2 %) and supervision (1 kHz × 15 µs = 1.5 %) together add about 5.5 %.
- Communication and background work must fit within the remainder, so that total load stays within the **≤ 70 % budget** (FW-REQ-061).

## 7. Firmware structure and platform requirements

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| FW-REQ-001 | The firmware shall be organised into the modules `platform`, `foc`, `motor_control`, `encoder`, `joint_control`, `diagnostics` and `communication`, matching the `firmware/` directory structure. Each module shall have a documented public interface. | Independent testability and reuse. | I | Code review confirms the module boundaries; no module includes another module's private headers. | `audit/firmware/FIRMWARE_REVIEW.md` | SYS-REQ-006 | A0 | M |
| FW-REQ-002 | All MCU-specific code shall be confined to `platform/` (HAL). Control modules shall use platform-neutral interfaces only. | Supports a later STM32G4 ↔ C2000 or board change (ACT-DEC-004/005). | I | `grep` for vendor headers outside `platform/` returns none. | `audit/firmware/FIRMWARE_REVIEW.md` | SYS-REQ-006, SYS-REQ-055 | A0 | M |
| FW-REQ-003 | Motor-specific, gearbox-specific and joint-specific values shall be held in a **configuration parameter set**, not hard-coded. This covers pole pairs, Kt, phase R and L, gear ratio, encoder resolution and offsets, limits and gains. | "Build once, evolve": the same firmware runs with another motor or gearbox. | I, D | Changing the motor parameter set (simulated second motor) requires no code change. | `tests/firmware/` | SYS-REQ-006 | A0 | M |
| FW-REQ-004 | The firmware shall build from source with a documented, version-pinned toolchain (for example arm-none-eabi-gcc version X with CMake, TBC with ACT-DEC-004), using a single build command. | Reproducible builds. | D | A clean checkout builds on a second machine; the binary hash is recorded. | `firmware/README.md` | SYS-REQ-107 | A0 | M |
| FW-REQ-005 | Every firmware image shall embed its version (semantic versioning MAJOR.MINOR.PATCH), git commit hash, build date, and target hardware revision. This data shall be reportable over USB/UART and CAN. | Test-record traceability (SYS-REQ-103). | T | Version query returns values that match the build log. | `tests/firmware/` | SYS-REQ-067, SYS-REQ-103 | A0 | M |
| FW-REQ-006 | The firmware shall verify at boot that the **hardware revision** (strap pins or EEPROM ID, TBC) is supported. Otherwise it shall stay disabled with `HW_REVISION_UNSUPPORTED`. | Prevents running A1 power-stage settings on the wrong board. | T | An unsupported strap value results in a disabled state and the fault being reported. | `tests/firmware/` | SYS-REQ-067 | A1 | H |
| FW-REQ-007 | Dynamic memory allocation shall not be used after initialisation. No blocking calls shall be made in interrupt context or in the control loops. | Determinism. | I | Static analysis and code review. | `audit/firmware/FIRMWARE_REVIEW.md` | SYS-REQ-050 | A0 | M |
| FW-REQ-008 | Interrupt priorities shall be assigned and documented in this order: PWM break / hardware fault (highest), current loop, encoder, velocity and position, communication, background. | The control loop must not be pre-empted by communication. | I, A | The priority table in FIRMWARE_ARCHITECTURE matches the code. | `docs/firmware/FIRMWARE_ARCHITECTURE.md` | SYS-REQ-050 | A0 | M |
| FW-REQ-009 | The ADC conversions for phase currents shall be **hardware-triggered** by the PWM timer at the defined sampling instant (centre of the low-side ON period for low-side shunts). | Correct current measurement without switching noise. | T | Oscilloscope capture shows the ADC trigger aligned to PWM centre ±0.5 µs (TBC). | `results/motor_control/` | SYS-REQ-050 | A0 | M |
| FW-REQ-010 | PWM outputs shall be **complementary with hardware dead-time** at a configurable value (initial value from the gate driver and MOSFET datasheets, TBC). At reset, and before configuration, all gate outputs shall be held off. | Prevents shoot-through. | T, I | Scope capture of dead time; reset-state measurement shows gates low. | `results/motor_control/` | SYS-REQ-080 | A0 | M |

## 8. FOC and motor control requirements

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| CTRL-REQ-010 | The motor shall be controlled by **FOC**: Clarke and Park transforms, PI current controllers for Id and Iq, inverse Park, and space-vector (or equivalent third-harmonic-injection) PWM. | Smooth torque and efficient current control (SYS-REQ-050). | I, T | Code review; at constant Iq the measured Id stays within ±5 % of rated current (TBC) during rotation. | `results/motor_control/` | SYS-REQ-050 | A0 | M |
| CTRL-REQ-011 | The current loop shall run at ≥ 10 kHz (20 kHz proposed). Its closed-loop **bandwidth shall be ≥ 1 kHz (TBC)**, with PI gains derived from measured R and L (pole-zero cancellation method or equivalent, documented in `docs/firmware/MOTOR_CONTROL.md`). | A stiff inner loop is the basis of torque control. | T | Iq step response: 10–90 % rise ≤ 0.35 ms (TBC), overshoot ≤ 10 %. | `results/motor_control/` | SYS-REQ-050, SYS-REQ-051 | A0 | M |
| CTRL-REQ-012 | Id shall be regulated to **0 A** by default. Field weakening is **not** required in v1 and shall be disabled. | Simplicity. Speed is reached by ratio and Kv selection. | I | Parameter default is Id* = 0; there is no field-weakening code path enabled. | `firmware/foc/` | SYS-REQ-050 | A0 | H |
| CTRL-REQ-013 | The voltage vector magnitude shall be limited to the linear modulation range, with anti-windup on both current PI controllers. | Prevents integrator windup at voltage saturation. | T | At saturation (high speed, low bus voltage) there is no current overshoot greater than 10 % on recovery. | `results/motor_control/` | SYS-REQ-050 | A0 | M |
| CTRL-REQ-014 | The electrical angle for commutation shall come from motor-side feedback: a motor-shaft encoder and/or Hall sensors. The source shall be selectable in configuration. With Hall-only feedback, angle interpolation shall be used above a minimum speed (TBC). | Correct commutation. | T | Commutation-angle error ≤ 5° electrical (TBC) against the reference measurement. | `results/motor_control/` | SYS-REQ-050, SYS-REQ-052 | A0 | M |
| CTRL-REQ-015 | Dead-time compensation **may** be implemented. If implemented, it shall be parameterised and its effect recorded. | Improves low-speed current quality. | T | Current THD before and after recorded. | `results/motor_control/` | SYS-REQ-050 | A1 | L |
| CTRL-REQ-016 | Bus-voltage compensation shall normalise the duty cycle to the measured bus voltage every current-loop cycle. | Consistent loop gain across the 20–28 V range. | T | Current-step response at 20 V and 28 V within 10 % of each other. | `results/motor_control/` | SYS-REQ-040, SYS-REQ-041 | A0 | M |
| CTRL-REQ-017 | **Torque estimation:** output torque shall be estimated as τ_out = Kt · Iq · N · η_model. Kt, N and η_model are taken from configuration. The estimate shall be reported as an *estimate* (no torque sensor in v1). | Torque-mode commands and telemetry need a defined model. | I, T | The estimate is compared with the torque fixture measurement; error recorded across the range (acceptance limit TBD before test). | `results/motor_control/`, `results/mechanical/` | SYS-REQ-026, SYS-REQ-062 | A1 | M |
| CTRL-REQ-018 | The firmware shall support **regenerative bus-voltage limiting**. When the bus voltage exceeds a configurable threshold (proposed 30 V, TBC), braking current shall be limited or a brake chopper enabled (if fitted). | Laboratory PSUs cannot absorb regenerated energy ([R5] HAZ-012). | T | Deceleration from 45 RPM with the reference inertia keeps bus ≤ 32 V on the bench. | `results/motor_control/` | SYS-REQ-041 | A1 | M |

## 9. Joint control requirements

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| CTRL-REQ-020 | The firmware shall implement the control modes **TORQUE (current)**, **VELOCITY** and **POSITION**. Mode is selected by the command type, per [R4] section 8.8. | Required joint-control modes (SYS-REQ-026). | T | Each mode demonstrated on the fixture. | `results/motor_control/` | SYS-REQ-026, SYS-REQ-051 | A0 | M |
| CTRL-REQ-021 | **POSITION + feed-forward** (position setpoint with optional velocity and torque feed-forward, and configurable stiffness and damping) shall be supported as an A2 goal. | Compliant control for KritvaOS. | T | Impedance step test shows the configured stiffness within ±20 % (TBC). | `results/integration/` | SYS-REQ-027, SYS-REQ-064 | A2 | L |
| CTRL-REQ-022 | In A1, position control shall close the loop on the **output-side encoder**. Velocity shall be estimated from motor-side feedback divided by the gear ratio, with the output encoder used for low-frequency correction (TBC in MOTOR_CONTROL). | Joint position is measured after the gearbox (SYS-REQ-052). | I, T | Code review; position error is measured at the output encoder. | `results/mechanical/` | SYS-REQ-052, SYS-REQ-024 | A1 | M |
| CTRL-REQ-023 | In A0 (motor only, no gearbox or output encoder), position control shall close on the motor encoder. The same joint-control code shall be used with ratio = 1. | Reuse of the code path. | D | A0 position demonstration with ratio parameter = 1. | `results/motor_control/` | SYS-REQ-026 | A0 | M |
| CTRL-REQ-024 | Position commands shall be passed through a **trajectory limiter**: trapezoidal or S-curve, limited by the configured maximum velocity, acceleration and (optionally) jerk. | Smooth motion; protects the gearbox. | T | Position step at maximum distance follows the limited profile; the measured acceleration is within the configured limit. | `results/motor_control/` | SYS-REQ-051 | A0 | M |
| CTRL-REQ-025 | Mode changes and enabling shall be **bumpless**: controllers are initialised from the measured state, and enabling holds the measured position (per [R4] enable()). | Prevents a jump at enable ([R5] HAZ-001). | T | Enabling under the gravity load shows a position deviation ≤ 1° (TBC) and no torque step beyond the limit. | `tests/firmware/`, `results/motor_control/` | SYS-REQ-051 | A1 | M |
| CTRL-REQ-026 | A **gravity feed-forward** term (configurable mass-arm model: m_eq · g · r_eq · cos(q + q_offset)) **may** be applied in position mode. | Reduces steady-state error with the 6.1 N·m gravity load. | T | Steady-state error at the horizontal pose compared with and without the term. | `results/integration/` | SYS-REQ-012 | A1 | L |
| CTRL-REQ-027 | Position, velocity and current controller gains shall be configurable at runtime (in DISABLED, or in ENABLED with rate-limited changes, TBC) and storable in NVM. | Tuning (SYS-REQ-066). | D | Gain update via host tool takes effect and persists. | `tests/firmware/` | SYS-REQ-006, SYS-REQ-066 | A0 | M |

## 10. Limits

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| CTRL-REQ-030 | The firmware shall enforce configurable limits on **phase current, output torque, output velocity, output acceleration** and **position (soft limits)**, independent of the command source (USB/UART, CAN, or internal test functions). | Firmware limits on torque, speed and acceleration (SYS-REQ-051). | T | A command beyond each limit is clamped or rejected per [R4], and the limit is never exceeded in the measured response. | `tests/firmware/`, `results/motor_control/` | SYS-REQ-051 | A0 | M |
| CTRL-REQ-031 | Soft position limits shall lie **inside** the mechanical hard stops by a configurable margin (proposed ≥ 5°, TBC). Configuration with a soft limit outside the configured hard-stop angle shall be rejected (`E_CONFIG_REJECTED`). | Avoids routine hard-stop impact. | T | Invalid configuration is rejected; the joint stops before the soft limit. | `tests/firmware/` | SYS-REQ-035, SYS-REQ-082 | A1 | M |
| CTRL-REQ-032 | Velocity shall be ramped down near the soft limits. The commanded velocity towards a limit shall be capped at v_lim(d) = sqrt(2 · a_max · d), where d is the remaining distance. A further cap (proposed ≤ 50 % v_max within the last 10°, TBC) shall be applied to reduce stop energy. | Kinetic energy at 45 RPM is about 1.9 J (SYS-REQ-035). | T | Driving at maximum speed towards a limit stops before the limit with no overshoot greater than 0.5° (TBC). | `results/mechanical/` | SYS-REQ-035 | A1 | M |
| CTRL-REQ-033 | The torque limit shall never exceed the **approved peak rating** (20 N·m, or 25 N·m if adopted). A configurable **I²t (thermal) limit** shall reduce the available current to the continuous rating after the peak duration (TBD). | Enforces the peak definition (duration, repetition, recovery). | T | A sustained peak command is reduced to the continuous current after the configured time; repetition behaves as configured. | `results/thermal/` | SYS-REQ-021 | A1 | M |
| CTRL-REQ-034 | **Tracking error** (abs(q_cmd_profiled − q_meas) greater than a configurable threshold for longer than a configurable time) shall raise `TRACKING_ERROR`. | Detects a blocked joint or collision ([R5]). | T | Blocking the fixture output raises the fault within the configured time. | `tests/safety/` | SYS-REQ-080 | A1 | M |

## 11. Calibration

Procedures are in `docs/firmware/CALIBRATION_PROCEDURE.md`.

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| FW-REQ-020 | The firmware shall provide an automated **phase resistance and inductance measurement** routine, with results reported and storable. | FOC gain design. | T | R and L within 10 % (TBC) of LCR-meter or datasheet values. | `results/motor_control/` | SYS-REQ-053 | A0 | M |
| FW-REQ-021 | The firmware shall provide **motor encoder electrical offset alignment**: a d-axis current lock at a configured current, measured in both directions, with direction (phase order) detection and pole-pair verification. | Correct commutation (SYS-REQ-053). | T | Repeatability of the offset ≤ 2° electrical (TBC) over 5 runs. | `results/motor_control/` | SYS-REQ-053 | A0 | M |
| FW-REQ-022 | The firmware shall provide **output encoder zero calibration**. The joint is placed at the reference pose (0° = full extension, using a fixture datum) and the offset is stored. Direction shall be checked against motor rotation (positive = flexion). | Absolute joint angle and sign convention ([R8]). | T | After a power cycle the reported q at the datum is within the approved accuracy limit. | `results/mechanical/` | SYS-REQ-053, SYS-REQ-024 | A1 | M |
| FW-REQ-023 | Calibration shall be allowed only in a dedicated CALIBRATING sub-state of DISABLED, at a limited current (configurable, proposed ≤ 30 % of rated, TBC), with the output **mechanically free or on the fixture**, never with the arm load attached unless the procedure says so. | Calibration moves the motor ([R5] HAZ-015). | T, I | Calibration refuses to start while ENABLED; the current limit is observed. | `tests/firmware/` | SYS-REQ-053, SYS-REQ-083 | A0 | M |
| FW-REQ-024 | Calibration results shall be stored with a CRC and a **calibration validity flag**. If calibration data are missing or invalid, enable() shall return `E_NOT_CALIBRATED`, and `CALIBRATION_INVALID` shall be reported. | Prevents running uncalibrated. | T | Corrupted calibration block results in enable refusal. | `tests/firmware/` | SYS-REQ-053 | A0 | M |
| FW-REQ-025 | **Cogging and anti-cogging compensation** may be added later as a parameterised lookup table. | Improves low-speed smoothness. | T | Torque ripple before and after recorded. | `results/motor_control/` | SYS-REQ-050 | A2 | L |
| FW-REQ-026 | Calibration records (date, firmware version, operator, values) shall be exportable to the host and stored in `results/` against the actuator serial number. | Traceability. | I | Records present for each unit. | `results/motor_control/` | SYS-REQ-103 | A1 | H |

## 12. State machine

The firmware shall implement the externally visible state machine of `requirements/INTERFACE_REQUIREMENTS.md` section 8.8.1 exactly. Internal sub-states are allowed if they are invisible to the interface, or reported as detail.

```
            power-on / reset
                  |
                  v
               [BOOT] --self-test fail--> [FAULT] (CRITICAL)
                  | self-test pass
                  v
     [DISABLED_UNCONFIGURED] --configure() ok--> [DISABLED] <--------------+
                                                   |  ^   \               |
                                       enable() ok |  |    \ calibrate     |
                                                   v  |     v             |
                                              [ENABLED]  (DISABLED.CALIBRATING)
                                         POSITION / VELOCITY / TORQUE     |
                                             |        |                   |
                         fault / timeout     |        | e-stop input      |
                                             v        v                   |
                                         [FAULT]   [ESTOP] --released + ack-+
                                             |
                                 ack + cause removed
                                             +-----------------------> [DISABLED]
```

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| FW-REQ-030 | The firmware shall implement the states `BOOT`, `DISABLED_UNCONFIGURED`, `DISABLED`, `ENABLED` (POSITION, VELOCITY, TORQUE), `FAULT` and `ESTOP`, with exactly the transitions and accepted calls of [R4] section 8.8.1. | One behaviour across all implementations. | T | State/call matrix test: every pair is exercised; calls not accepted return `E_INVALID_STATE` without a state change. | `tests/firmware/` | SYS-REQ-063, SYS-REQ-064 | A1 | M |
| FW-REQ-031 | The PWM outputs shall be enabled **only** in `ENABLED` (and in the current-limited CALIBRATING sub-state). | Single point of power-stage enable. | I, T | Code review; probe shows gates off in all other states. | `tests/firmware/` | SYS-REQ-080 | A0 | M |
| FW-REQ-032 | Transitions to `FAULT` or `ESTOP` shall be possible from any state and shall take priority over any command in the same cycle. | Fault priority. | T | Fault injected during a command burst is honoured. | `tests/safety/` | SYS-REQ-080 | A0 | M |
| FW-REQ-033 | Leaving `FAULT` or `ESTOP` shall require an explicit acknowledgement with the cause removed, and shall always lead to `DISABLED`, never directly to `ENABLED`. | Deliberate recovery ([R4] IF-REQ-097). | T | Acknowledgement with cause present returns `E_FAULT_ACTIVE`. | `tests/safety/` | SYS-REQ-080 | A1 | M |
| FW-REQ-034 | The boot self-test shall check: clock configuration, RAM test (TBC), NVM CRCs (configuration and calibration), ADC offset (current sensors with PWM off), gate-driver status, encoder communication, bus-voltage range, and temperature sensors. | Detects faults before enable. | T | Each self-test failure is injected and the reported code verified. | `tests/firmware/` | SYS-REQ-080 | A1 | H |

## 13. Fault detection and reaction

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| CTRL-REQ-001 | The firmware shall **detect encoder faults** (motor and output), **overcurrent** (hardware trip supervision and software threshold) and **overtemperature** (motor and controller). On detection it shall enter the defined safe state and report the specific fault code. | Core protective function (SYS-REQ-080). | T | Fault-injection tests for each fault show detection within the reaction time of the table below and the correct code. | `tests/safety/`, `results/integration/` | SYS-REQ-080 | A0/A1 | M |
| CTRL-REQ-002 | The firmware shall detect and react to every fault in the table below with the specified detection method, threshold, reaction and severity class (WARNING / FAULT / CRITICAL per [R4] IF-REQ-150). | Complete fault coverage. | T | The fault-injection matrix in `docs/validation/VALIDATION_PLAN.md` passes. | `tests/safety/` | SYS-REQ-080, SYS-REQ-063 | A1 | M |
| CTRL-REQ-003 | The firmware shall configure the MCU's **hardware PWM break input** from the hardware overcurrent comparator and the gate-driver fault output, so that the PWM is disabled without software involvement. The firmware shall then read the latch, report `OVERCURRENT_HW` or `GATE_DRIVER_FAULT`, and enter `FAULT`. | Overcurrent faster than software ([R3]). | T | The injected comparator trip disables the gates within the hardware specification (target < 10 µs, TBC) and the fault is reported. | `tests/safety/` | SYS-REQ-080 | A0 | M |
| CTRL-REQ-004 | The independent watchdog shall be serviced only from a supervisor that confirms the current-loop ISR and the main loop both ran within their deadlines. A watchdog reset shall leave the gates off and record `WATCHDOG_RESET` as the reset cause. | Firmware hang protection. | T | A deliberate ISR stall causes a reset within the configured window (proposed ≤ 20 ms, TBC). | `tests/safety/` | SYS-REQ-080 | A0 | M |
| CTRL-REQ-005 | The output and motor positions shall be cross-checked: abs(q_out − m_pos/N) beyond the configured backlash plus compliance plus tolerance shall raise `ENCODER_MISMATCH`. | Detects encoder slip, gearbox failure or a wrong offset ([R5] HAZ-010). | T | An injected offset of the output encoder triggers the fault. | `tests/safety/` | SYS-REQ-080, SYS-REQ-052 | A1 | M |
| CTRL-REQ-006 | Faults shall be latched until acknowledged (except WARNING). The first fault after an acknowledgement shall be stored as the first-fault record ([R4] IF-REQ-151). | Root-cause analysis. | T | Cascade test: the first-fault record shows the originating fault. | `tests/safety/` | SYS-REQ-062 | A1 | M |

**Fault table (proposed thresholds, TBC with the selected components)**

| Fault code | Detection | Proposed threshold / time | Reaction (safe state per [R5]) | Class |
|---|---|---|---|---|
| `OVERCURRENT_HW` | Comparator → PWM break | Hardware level ≈ 1.2 × peak phase current (TBC) | PWM off immediately (hardware) → FAULT | FAULT |
| `OVERCURRENT_SW` | Measured phase-current magnitude | > 1.1 × configured current limit for 3 consecutive samples | PWM off → FAULT | FAULT |
| `GATE_DRIVER_FAULT` | Driver nFAULT pin | Any assertion | PWM off → FAULT | FAULT |
| `OVERVOLTAGE` | Bus ADC | > 32 V (TBC) for 1 ms; warning at 30 V | Regen limit at warning; PWM off at fault | FAULT |
| `UNDERVOLTAGE` | Bus ADC | < 18 V (TBC) for 10 ms; warning at 20 V | Controlled stop if possible, then PWM off | FAULT |
| `MOTOR_OVERTEMP` | Winding thermistor or thermal model | Warning at T_max − 15 °C, fault at T_max (from motor datasheet, TBD) | Derate at warning; controlled stop → FAULT | FAULT |
| `CONTROLLER_OVERTEMP` | Board/MOSFET NTC | Warning 80 °C, fault 95 °C (TBC) | As above | FAULT |
| `TEMP_SENSOR_FAULT` | Out-of-range reading (open or short) | Outside −30 … 150 °C | FAULT (no derating possible) | FAULT |
| `ENCODER_MOTOR_FAULT` | Communication error, magnet status bits, implausible jump | 3 consecutive invalid reads or a jump > max plausible step | PWM off immediately (no commutation possible) | FAULT |
| `ENCODER_OUTPUT_FAULT` | As above, at the joint encoder | 3 consecutive invalid reads | Controlled stop on the motor encoder, then safe state | FAULT |
| `ENCODER_MISMATCH` | Cross-check (CTRL-REQ-005) | Beyond backlash + tolerance for > 10 ms (TBC) | Safe state | FAULT |
| `POSITION_LIMIT` | q outside the soft limits by > margin | 1° beyond the soft limit (TBC) | Controlled stop; motion allowed only back inside the limits | WARNING or FAULT (configurable) |
| `VELOCITY_LIMIT` | Measured velocity | > 1.2 × v_max for 10 ms | Safe state | FAULT |
| `TRACKING_ERROR` | CTRL-REQ-034 | Threshold and time configurable | Safe state | FAULT |
| `COMM_TIMEOUT` | No valid command within the timeout while ENABLED | 50 ms default | Configured safe state | FAULT |
| `CAN_BUS_OFF` | CAN controller status | Bus-off while enabled | Same as `COMM_TIMEOUT` | FAULT |
| `INVALID_COMMAND_RATE` | Command rate above the configured maximum | > 2 × configured rate (TBC) | Commands ignored, warning | WARNING |
| `ESTOP_ACTIVE` | Safety input | Input asserted | Power stage disabled by hardware; firmware → ESTOP | FAULT |
| `WATCHDOG_RESET` | Reset-cause register | Any | Boot into DISABLED_UNCONFIGURED or DISABLED; reported | FAULT (reported at boot) |
| `CONFIG_INVALID` / `CALIBRATION_INVALID` | CRC or range check | Any | Stay disabled | FAULT |
| `HW_REVISION_UNSUPPORTED` | Strap/ID check | Any | Stay disabled | CRITICAL |
| `INTERNAL_ERROR` | Assertions, stack-overflow canary, ISR overrun | Any | PWM off → FAULT | CRITICAL |

## 14. Safe state behaviour

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| CTRL-REQ-040 | The default safe state shall be **PWM disabled (coast)**. A configurable alternative, **active damping (low-side phase short)**, shall be available where the hardware allows it and [R5] approves it. | Defined safe state. Without a brake, the arm falls under gravity when coasting ([R5] HAZ-009). | T | Both options demonstrated on the fixture; fall speed of the arm measured with damping. | `results/integration/` | SYS-REQ-080 | A1 | M |
| CTRL-REQ-041 | For faults where control is still possible (thermal warning, output encoder fault while motor feedback is valid, undervoltage warning), the firmware shall perform a **controlled stop**: a deceleration ramp at the configured maximum, then hold or safe state as configured. | Avoids an uncontrolled drop. | T | Controlled stop observed; maximum deceleration within the limit. | `tests/safety/` | SYS-REQ-080 | A1 | H |
| CTRL-REQ-042 | Faults that make control impossible (motor encoder fault, overcurrent, gate-driver fault, internal error) shall disable the PWM immediately, without a ramp. | Continued switching could cause damage. | T | Immediate PWM disable is confirmed by probe. | `tests/safety/` | SYS-REQ-080 | A0 | M |

## 15. Telemetry and diagnostics

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| FW-REQ-040 | The firmware shall report: output position q, output velocity, motor position and velocity, Iq, Id, Iq command, estimated output torque, bus voltage, controller temperature, motor temperature (measured or estimated), state, mode, active and latched faults, warnings, and timestamp. | State feedback (SYS-REQ-062). | D | All fields visible in the host tool at ≥ 100 Hz. | `results/motor_control/` | SYS-REQ-062 | A0 | M |
| FW-REQ-041 | A high-rate **capture buffer** (≥ 2 000 samples of 4–8 selectable signals at up to the current-loop rate, triggerable) shall be available for tuning and fault analysis. | Loop tuning and debugging. | D | Capture of an Iq step at 20 kHz exported to CSV. | `results/motor_control/` | SYS-REQ-066 | A0 | H |
| FW-REQ-042 | A **fault log** of at least the last 16 faults (code, timestamp/uptime, state, key measurements) shall be kept in NVM and survive power cycles. | Post-event analysis. | T | The log persists across a power cycle; wraps correctly. | `tests/firmware/` | SYS-REQ-062 | A1 | H |
| FW-REQ-043 | Counters shall be kept for: operating time, enable cycles, faults by code, CAN statistics ([R4] IF-REQ-153), and peak-torque events. | Reliability data. | D | Counters readable. | `tests/firmware/` | SYS-REQ-062 | A1 | L |
| FW-REQ-044 | **CPU load** and the worst-case ISR execution time shall be measured by the firmware and reported. | Timing evidence for FW-REQ-061. | T | Values reported and recorded. | `results/motor_control/` | SYS-REQ-050 | A0 | H |

## 16. Communication

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| FW-REQ-050 | The firmware shall provide a **USB/UART interface** with (a) a human-readable CLI for bring-up and (b) a framed binary protocol with CRC for host tools, as defined in [R7]. | A0 development (SYS-REQ-060). | D, T | CLI and binary protocol pass the host-tool conformance test. | `tests/firmware/` | SYS-REQ-060 | A0 | M |
| FW-REQ-051 | The firmware shall implement **CAN protocol v1** per [R6]: classic CAN 2.0B at 1 Mbit/s baseline, 11-bit identifiers (function code << 6 \| node ID), heartbeat, command, feedback, configuration and fault messages. | A1 robot bus (SYS-REQ-061). | T | Protocol conformance test with a CAN analyser and host driver. | `tests/integration/` | SYS-REQ-061 | A1 | M |
| FW-REQ-052 | Commands from different interfaces shall be **arbitrated**: only one interface may be the active command source at a time (selected on enable). The other interfaces remain read-only for motion commands. | Prevents conflicting commands. | T | A motion command on the non-active interface is rejected with `E_BUSY`. | `tests/firmware/` | SYS-REQ-063 | A1 | M |
| FW-REQ-053 | Every received command shall be validated (length, CRC where applicable, range, state) before use. An invalid command shall be rejected with the return codes of [R4], shall not refresh the command timeout, and shall be counted. | Invalid-command detection (SYS-REQ-063). | T | Fuzz test with malformed frames: no crash, no motion, counters increment. | `tests/firmware/` | SYS-REQ-063 | A1 | M |
| FW-REQ-054 | The firmware shall report its protocol version. If a host requests an incompatible major version, its commands shall be refused with `E_VERSION_MISMATCH`. | Compatibility (SYS-REQ-067). | T | Version-mismatch test. | `tests/integration/` | SYS-REQ-067 | A1 | M |
| FW-REQ-055 | Communication handling shall never block or delay the current loop. The worst-case communication ISR time shall be measured. | Determinism. | A, T | Current-loop jitter ≤ 1 µs (TBC) at maximum bus load. | `results/motor_control/` | SYS-REQ-050 | A1 | M |

## 17. Parameters, non-volatile storage and update

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| FW-REQ-060 | Configuration and calibration shall be stored in NVM in **versioned, CRC-protected** blocks, with factory defaults compiled in. Writing shall be power-fail-safe (two copies, or write-then-switch). | Data integrity. | T | Power is cut during a write: on reboot either the old or the new set is valid, never a corrupt mix. | `tests/firmware/` | SYS-REQ-006 | A1 | M |
| FW-REQ-061 | Total CPU load at maximum configured rates shall be **≤ 70 % (TBC)**, and current-loop ISR jitter **≤ 1 µs (TBC)**. | Margin for features and worst cases. | T, A | Measured by FW-REQ-044 at maximum CAN load. | `results/motor_control/` | SYS-REQ-050 | A1 | M |
| FW-REQ-062 | NVM writes shall not occur while ENABLED (or shall be deferred), so that flash-erase stalls cannot affect control. | Flash erase can stall the CPU on some MCUs. | I, T | Write request while ENABLED is deferred or rejected. | `tests/firmware/` | SYS-REQ-050 | A1 | M |
| FW-REQ-063 | **Firmware update** shall be possible over SWD (A0) and, as a goal, through a bootloader over USB/UART (A1) and CAN (A2). The bootloader shall verify image integrity (CRC/hash) before jumping, and shall keep the gates off. | Field update without disassembly. | D | Update cycle demonstrated; a corrupted image is refused. | `tests/firmware/` | SYS-REQ-066 | A1 | H |

## 18. Engineering process requirements

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| FW-REQ-070 | Code shall be written in C (C11) or C++ (C++17 subset without exceptions or RTTI, TBC) following a documented **MISRA-inspired coding standard**: no recursion, bounded loops in ISRs, explicit fixed-width types, no undefined behaviour, all warnings enabled and treated as errors. | Embedded robustness. | I | Compiler warnings = 0; checklist in FIRMWARE_REVIEW. | `audit/firmware/FIRMWARE_REVIEW.md` | SYS-REQ-107 | A0 | M |
| FW-REQ-071 | Static analysis (for example cppcheck or clang-tidy) shall run in CI with zero unresolved high-severity findings at release. | Defect prevention. | I | CI report. | `.github/workflows/` | SYS-REQ-107 | A1 | H |
| FW-REQ-072 | Platform-independent modules (`foc`, `joint_control`, fault manager, protocol parsers, trajectory) shall have **host unit tests** in `tests/unit/`, with ≥ 80 % (TBC) statement coverage for those modules. | Verify maths and logic off-target. | T | Coverage report. | `tests/unit/` | SYS-REQ-006 | A1 | H |
| FW-REQ-073 | **HIL and bench tests** shall verify timing, fault injection and control performance, with records per SYS-REQ-103. | Evidence on real hardware. | T | Test reports in `results/`. | `results/` | SYS-REQ-103 | A0 | M |
| FW-REQ-074 | Code reused from open-source references (for example **SimpleFOC**, MIT; **moteus**, Apache-2.0) shall be identified file by file, with the licence notice retained. The use shall be approved by the Project Lead after a licence-compatibility review against the Apache-2.0 licence of this repository. Copyleft code shall not be included without explicit approval. | Legal and IP hygiene (SYS-REQ-054). | I | Third-party register in `firmware/README.md`. | `firmware/README.md` | SYS-REQ-054 | A0 | M |
| FW-REQ-075 | Every firmware release shall have release notes, a tag, the binary and its hash, the configuration defaults, and the passed test list. A release shall be approved at gate F4. | Release control. | I | `audit/firmware/FIRMWARE_ACCEPTANCE_AUDIT.md` signed. | `audit/firmware/` | SYS-REQ-102 | A1 | M |
| FW-REQ-076 | Safety-relevant firmware (fault manager, limits, state machine, watchdog supervision) shall be reviewed by the **Independent Electrical/Firmware Reviewer**, not only by the author. | Independent-review rule (ACT-DEC-014). | I | Review record exists with reviewer ≠ author. | `audit/firmware/FIRMWARE_REVIEW.md` | SYS-REQ-106 | A1 | M |

## 19. Firmware review gates

| Gate | Timing (week) | Scope | Entry evidence | Reviewer |
|---|---|---|---|---|
| F0 Firmware requirements | 1–2 | This document is complete, measurable and consistent with [R4]/[R5] | This document, traceability rows | Independent Electrical/Firmware Reviewer |
| F1 Architecture review | 3–4 | FIRMWARE_ARCHITECTURE, timing plan, state machine, CAN allocation | docs/firmware/*, docs/interfaces/CAN_PROTOCOL.md | Same |
| F2 Code review | 6–9 (rolling) | Module code, coding standard, static analysis, unit tests | PRs, CI reports | Same |
| F3 HIL / fault-injection verification | 8–10 | Timing, fault matrix, control performance | `results/motor_control/`, `tests/safety/` | Same |
| F4 Release | 11–12 | Release package (FW-REQ-075) | Release notes, test summary | Same, plus Project Lead approval |

## 20. Allocation check against the parent

| SYS-REQ | Covered by |
|---|---|
| SYS-REQ-006 | FW-REQ-001, 002, 003, 060, 072 |
| SYS-REQ-026 | CTRL-REQ-017, 020, 023 |
| SYS-REQ-050 | CTRL-REQ-010 to 016, FW-REQ-007 to 009, 044, 055, 061, 062 |
| SYS-REQ-051 | CTRL-REQ-011, 020, 024, 025, 030 |
| SYS-REQ-052 | CTRL-REQ-014, 022, 005 |
| SYS-REQ-053 | FW-REQ-020 to 024 |
| SYS-REQ-054 | FW-REQ-074 |
| SYS-REQ-062 | FW-REQ-040 to 043, CTRL-REQ-006 |
| SYS-REQ-063 | FW-REQ-030, 052, 053, CTRL-REQ-002 |
| SYS-REQ-080 | CTRL-REQ-001 to 006, 040 to 042, FW-REQ-031 to 034 |

## 21. Open items

| # | Item | Affects | Owner | Needed by |
|---|---|---|---|---|
| 1 | MCU family and A0 board (ACT-DEC-004/005) | FW-REQ-002, 004 | Electronics/Embedded Intern | F1 |
| 2 | Final loop rates and the CPU budget measured on target | Section 6, FW-REQ-061 | Electronics/Embedded Intern | F3 |
| 3 | Motor feedback type (Hall / encoder / both) | CTRL-REQ-014 | Both interns | Motor selection |
| 4 | Thermal thresholds from the selected motor and MOSFETs | Fault table | Electronics/Embedded Intern | F1 |
| 5 | Safe-state option (coast vs active damping) approval | CTRL-REQ-040 | Project Lead with reviewer | Gate C |
| 6 | Peak duration and I²t parameters | CTRL-REQ-033 | Project Lead | Before motor/gearbox freeze |
| 7 | Language choice (C vs C++ subset) | FW-REQ-070 | Electronics/Embedded Intern | F1 |
| 8 | Bootloader scope for A1 | FW-REQ-063 | Project Lead | F1 |

## 22. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
