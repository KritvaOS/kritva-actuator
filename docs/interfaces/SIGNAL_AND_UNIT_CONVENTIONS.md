# Kritva Actuator: Signal and Unit Conventions

| Field | Value |
|---|---|
| Document ID | KA-DOC-IF-UNITS |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead / Integration Owner |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A0, A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** These conventions are proposed for approval under ACT-03-001. Once they are approved, every document, every firmware module and all host software must follow them.

---

## 1. Purpose

Sign and unit errors are a classic cause of runaway motion: a wrong sign creates positive feedback, and a gear-ratio mix-up creates a 20× error. This document defines **once** how every quantity is named, measured, signed and scaled. Other documents link here; they do not redefine these conventions.

## 2. Units

| Quantity | Documents (human-facing) | Firmware, API, protocol | Conversion |
|---|---|---|---|
| Angle | degrees (°) | rad | rad = ° × π/180 |
| Angular velocity | RPM | rad/s | rad/s = RPM × 2π/60 (45 RPM = 4.712 rad/s) |
| Angular acceleration | rad/s² | rad/s² | — |
| Torque | N·m | N·m | — |
| Current | A | A | — |
| Voltage | V | V | — |
| Temperature | °C | °C (agreed exception to SI base units) | — |
| Time | s, ms | s (float) or µs counts (uint) | — |
| Length | mm | m (only in models; mechanical drawings use mm) | — |
| Mass | kg | kg | — |
| Inertia | kg·m² | kg·m² | — |
| Stiffness | N·m/° (reports) | N·m/rad | N·m/rad = N·m/° × 180/π |

Rules:

- Host tools may **display** degrees and RPM, but convert at the display layer only (IF-REQ-130).
- No mixed-unit variables. A variable's name must not imply one unit while holding another.

## 3. Joint frame and sign convention

| Convention | Definition |
|---|---|
| Joint angle q | **q = 0 at full extension.** **Positive in the flexion direction** (the forearm moving towards the upper arm). Range ≈ 0 to 2.36 rad (0–135°) |
| Joint axis | Defined in CAD as a unit vector, so that positive flexion is a **right-handed rotation** about it. For left and right elbows the vector points in opposite directions in the robot frame, so **flexion is positive on both arms** |
| Velocity | Positive = moving into flexion |
| Torque (output) | Positive = torque that accelerates towards positive q |
| q-axis current | Positive Iq produces positive output torque, after the direction calibration (`motor_direction`, `output_direction`) |
| Gravity at the horizontal pose | With the upper arm vertical and the forearm horizontal (q = 90°), gravity produces a **negative** torque (towards extension). The actuator must supply ≈ +6.08 N·m to hold the pose |

**Verification.** After any motor, encoder or wiring change, the direction check must confirm that a positive velocity command moves into flexion, that the q reading increases, and that the torque estimate is positive while accelerating (IF-REQ-131/132/135).

## 4. Output-side versus motor-side quantities

| Prefix | Meaning | Example |
|---|---|---|
| none / `q`, `dq`, `tau` | Output (joint) side | `q`, `dq`, `tau_est` |
| `motor_` / `m_` | Motor side (before the gearbox) | `motor_vel`, `m_pos` |
| `_e` suffix | Electrical angle | `theta_e` |

Relationships (N = gear ratio, p = pole pairs):

```
q ≈ motor_pos / N            (plus backlash and compliance)
dq ≈ motor_vel / N
tau_out ≈ Kt · Iq · N · η
theta_e = p · motor_pos  (mod 2π)
```

Every reported or commanded quantity states which side it belongs to (IF-REQ-133).

## 5. Naming conventions in firmware and software

| Item | Convention | Example |
|---|---|---|
| Variables and fields | `snake_case`, with the unit implied by SI unless suffixed | `v_bus`, `t_motor`, `i_max_phase` |
| Non-SI exceptions | Explicit suffix | `t_motor_degc`, `timestamp_us`, `angle_deg` (display only) |
| Constants | `UPPER_SNAKE_CASE` | `PWM_FREQ_HZ` |
| Fault codes | `UPPER_SNAKE_CASE` from ACTUATOR_INTERFACE §6 | `ENCODER_MISMATCH` |
| Parameters | Names and IDs from ACTUATOR_INTERFACE §7 | `command_timeout` (0x0004) |

## 6. Fixed-point and protocol scaling

The canonical scaling is in `CAN_PROTOCOL.md` §4. Summary:

| Quantity | LSB | Range |
|---|---|---|
| Position | 1×10⁻⁴ rad | ±3.2767 rad |
| Velocity | 1×10⁻³ rad/s | ±32.767 rad/s |
| Torque | 1×10⁻³ N·m | ±32.767 N·m |
| Current | 1×10⁻² A | ±327.67 A |

Rules:

- **Rounding:** round to nearest, and saturate at the range limits, setting the SAT flag.
- **Byte order:** little-endian.

## 7. Time and timestamps

- Actuator timestamps are a monotonic µs counter from boot (uint32 or uint64; wraparound is handled by the host).
- If `TIME_SYNC` is used, the host clock offset is estimated by Edge. Firmware never changes its monotonic counter.

## 8. Data records

| Item | Convention |
|---|---|
| CSV column names | `name_unit`, for example `q_rad`, `tau_est_nm`, `t_motor_degc`, `time_s` |
| Results folder | `results/<area>/YYYY-MM-DD_<test-id>_<short-name>/` |
| Sample rate | Stated in the record header |
| Plots | Axes labelled with units; degrees and RPM may be used for readability |

## 9. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
