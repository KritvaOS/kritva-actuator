# Kritva Actuator: Actuator Interface Specification

| Field | Value |
|---|---|
| Document ID | KA-DOC-IF-ACTUATOR |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead / Integration Owner |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A0 (USB/UART), A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** This is the proposed interface definition produced under ACT-03-001. Function names, numeric codes, parameter defaults and limits are proposed and pending approval. Interface **version 1** is not frozen until the ACT-03-001 review passes.

---

## 1. Purpose and scope

This document is the canonical **language-level definition** of the standard Kritva actuator interface. It covers:

- the API functions, their semantics and numeric return codes;
- the fault-code table;
- the **configuration parameter table**;
- the **USB/UART protocol** (CLI and binary framing).

It implements `requirements/INTERFACE_REQUIREMENTS.md` §8.5, §8.8 and §8.13–8.14. The CAN mapping is in `CAN_PROTOCOL.md`. Units and signs are in `SIGNAL_AND_UNIT_CONVENTIONS.md`.

> In INTERFACE_REQUIREMENTS, the references [R9] (USB/UART protocol), [R10] (software interface) and [R11] (configuration parameters) all point to this document.

## 2. Implementations

```
                 +----------------------------------+
  KritvaOS /     |  IActuator (this specification)  |
  host tools --> +----------------------------------+
                    |               |              |
        SimulatedActuator  DevelopmentBoardActuator  CANActuator
        (software/simulation) (USB/UART, A0)        (CAN, A1/A2)
```

All implementations shall pass the same conformance suite (ACT-03-001 TEST_PLAN, CT-01 to CT-08).

## 3. Data types

| Type | Definition |
|---|---|
| `Result` | Return code (section 5) |
| `State` | `BOOT`=0, `DISABLED_UNCONFIGURED`=1, `DISABLED`=2, `ENABLED`=3, `FAULT`=4, `ESTOP`=5 |
| `Mode` | `NONE`=0, `POSITION`=1, `VELOCITY`=2, `TORQUE`=3 |
| `ActuatorState` | `{ state, mode, q [rad], dq [rad/s], tau_est [N·m], iq [A], id [A], motor_pos [rad], motor_vel [rad/s], v_bus [V], t_motor [°C], t_ctrl [°C], active_faults: set<FaultCode>, warnings: set<FaultCode>, timestamp_us: uint64 }` |
| `FaultReport` | `{ active: set<FaultCode>, latched: set<FaultCode>, first_fault: {code, timestamp_us, state, mode, q, dq, iq, v_bus, t_motor, t_ctrl}, counters: map<FaultCode,uint32>, reset_cause }` |
| `Config` | The parameter set in section 7, plus `schema_version`, plus a `crc32` computed over the set |
| `VersionInfo` | `{ hw_revision, fw_version (semver), fw_git_hash, protocol_version (major.minor), serial_number }` |

Floating-point values are IEEE-754 double in the host API, and float32 inside the firmware.

## 4. Functions

Preconditions follow the state machine in INTERFACE_REQUIREMENTS §8.8.1. A call that is not permitted in the current state returns `E_INVALID_STATE` and causes no state change.

| Function | Allowed states | Inputs (units, range) | Behaviour | Errors | Timeout (host call) | Post-state |
|---|---|---|---|---|---|---|
| `connect(transport, node_id)` | — | Transport handle; node 1–63 | Opens the link; reads VersionInfo; checks protocol major = 1 | `E_COMM`, `E_VERSION_MISMATCH` | 500 ms | Unchanged |
| `configure(Config)` | DISABLED_UNCONFIGURED, DISABLED | Full parameter set | Atomic validation (ranges in §7 and the cross-checks in §7.2) then apply and store | `E_CONFIG_REJECTED` (+ parameter ID), `E_INVALID_STATE` | 500 ms (TBC, includes NVM) | DISABLED |
| `enable()` | DISABLED | — | Checks: configured, calibrated, no active or unacknowledged fault, e-stop released, v_bus in range, encoders valid. Then enables PWM, holding the **measured position** in POSITION mode, and starts the command timeout | `E_NOT_CONFIGURED`, `E_NOT_CALIBRATED`, `E_FAULT_ACTIVE`, `E_ESTOP_ACTIVE`, `E_INVALID_STATE` | 100 ms | ENABLED / POSITION |
| `command_position(q, dq_ff=0, tau_ff=0)` | ENABLED | q [rad] within the soft limits; dq_ff [rad/s] ≤ v_max; tau_ff [N·m] ≤ tau_max | Sets the position target through the trajectory limiter; refreshes the timeout | `E_OUT_OF_RANGE`, `E_INVALID_ARGUMENT` (no timeout refresh; previous setpoint held) | Must repeat within the timeout | POSITION |
| `command_velocity(dq)` | ENABLED | \|dq\| ≤ v_max [rad/s] | Velocity mode; soft limits still enforced | As above | As above | VELOCITY |
| `command_torque(tau)` | ENABLED (and torque mode permitted in the config) | \|tau\| ≤ tau_max [N·m, output side] | Torque mode (the torque is estimated from current); speed and position limits still enforced | As above, plus `E_UNSUPPORTED` if disabled in the config | As above | TORQUE |
| `read_state()` | Any | — | Returns ActuatorState | `E_COMM` | 20 ms (CAN), 50 ms (USB) | Unchanged |
| `read_faults()` | Any | — | Returns FaultReport | `E_COMM` | 50 ms | Unchanged |
| `clear_faults()` | FAULT, ESTOP | — | Succeeds only if every cause is removed (and the e-stop is released) | `E_FAULT_ACTIVE`, `E_ESTOP_ACTIVE` | 100 ms | DISABLED |
| `disable()` | Any except BOOT | — | PWM off (coast), or the configured stop behaviour | — | 50 ms | DISABLED (or the state is kept if FAULT/ESTOP) |
| `calibrate(kind)` | DISABLED | kind ∈ {`MOTOR_RL`, `MOTOR_OFFSET`, `OUTPUT_ZERO`, `DIRECTION_CHECK`} | Runs the routine in the current-limited CALIBRATING sub-state (FW-REQ-020 to 024) | `E_INVALID_STATE`, `E_BUSY`, `E_FAULT_ACTIVE` | Up to 30 s | DISABLED |
| `get_param(id)` / `set_param(id, value)` | Any / DISABLED for safety parameters | Parameter ID and value | Single-parameter access (set: validated, not persisted until `save_config()`) | `E_OUT_OF_RANGE`, `E_INVALID_STATE` | 50 ms | Unchanged |
| `save_config()` | DISABLED | — | Writes to NVM (two-copy, CRC) | `E_INVALID_STATE`, `E_BUSY` | 500 ms | Unchanged |
| `read_version()` | Any | — | Returns VersionInfo | `E_COMM` | 50 ms | Unchanged |

**Command-timeout rule.** Only **valid motion commands** refresh the command timeout. Reads, heartbeats and invalid commands do not refresh it (IF-REQ-070, FW-REQ-053).

## 5. Return codes

| Value | Code | Meaning |
|---|---|---|
| 0 | `OK` | Success |
| 1 | `E_INVALID_STATE` | Call not allowed in the current state |
| 2 | `E_INVALID_ARGUMENT` | Malformed argument (NaN, wrong type, bad length) |
| 3 | `E_OUT_OF_RANGE` | Argument outside the configured limits |
| 4 | `E_NOT_CONFIGURED` | No valid configuration |
| 5 | `E_NOT_CALIBRATED` | Calibration missing or invalid |
| 6 | `E_FAULT_ACTIVE` | Fault active or latched and not acknowledged |
| 7 | `E_ESTOP_ACTIVE` | E-stop asserted |
| 8 | `E_CONFIG_REJECTED` | Configuration failed validation (the response carries the parameter ID) |
| 9 | `E_TIMEOUT` | No response within the host timeout |
| 10 | `E_BUSY` | Operation in progress, or another interface holds command authority |
| 11 | `E_COMM` | Transport error (CRC, framing, bus-off) |
| 12 | `E_VERSION_MISMATCH` | Incompatible protocol major version |
| 13 | `E_UNSUPPORTED` | Function not supported by this implementation or configuration |

## 6. Fault codes

These are the same in every transport (IF-REQ-155). Reactions are in FIRMWARE_REQUIREMENTS §13.

| Code | Name | Class | Code | Name | Class |
|---|---|---|---|---|---|
| 0x0101 | `OVERCURRENT_HW` | FAULT | 0x0501 | `POSITION_LIMIT` | WARNING/FAULT (configurable) |
| 0x0102 | `OVERCURRENT_SW` | FAULT | 0x0502 | `VELOCITY_LIMIT` | FAULT |
| 0x0103 | `GATE_DRIVER_FAULT` | FAULT | 0x0503 | `TRACKING_ERROR` | FAULT |
| 0x0201 | `OVERVOLTAGE` | FAULT (warning at threshold W) | 0x0601 | `COMM_TIMEOUT` | FAULT |
| 0x0202 | `UNDERVOLTAGE` | FAULT (warning at threshold W) | 0x0602 | `CAN_BUS_OFF` | FAULT |
| 0x0301 | `MOTOR_OVERTEMP` | FAULT (warning first) | 0x0603 | `INVALID_COMMAND_RATE` | WARNING |
| 0x0302 | `CONTROLLER_OVERTEMP` | FAULT (warning first) | 0x0701 | `ESTOP_ACTIVE` | FAULT |
| 0x0303 | `TEMP_SENSOR_FAULT` | FAULT | 0x0801 | `WATCHDOG_RESET` | FAULT |
| 0x0401 | `ENCODER_OUTPUT_FAULT` | FAULT | 0x0802 | `CONFIG_INVALID` | FAULT |
| 0x0402 | `ENCODER_MOTOR_FAULT` | FAULT | 0x0803 | `CALIBRATION_INVALID` | FAULT |
| 0x0403 | `ENCODER_MISMATCH` | FAULT | 0x0804 | `HW_REVISION_UNSUPPORTED` | CRITICAL |
| | | | 0x0805 | `INTERNAL_ERROR` | CRITICAL |

Warnings use the same code with the warning bit set: bit 15 of the 16-bit code, so `0x8301` is the motor-overtemperature warning.

## 7. Configuration parameters

Access:

- **R**: read only.
- **RW**: writable in any state; it only takes effect on save if it is a persistent parameter.
- **RWD**: writable only in DISABLED or DISABLED_UNCONFIGURED. This covers the safety parameters.

Units are SI. Defaults are proposed and TBC with the selected components.

### 7.1 Parameter table

| ID | Name | Unit | Range | Default (proposed) | Access | Persist |
|---|---|---|---|---|---|---|
| 0x0001 | `schema_version` | — | — | 1 | R | Yes |
| 0x0002 | `node_id` | — | 1–63 | 10 (TBC) | RWD | Yes |
| 0x0003 | `can_bitrate` | bit/s | {500 000, 1 000 000} | 1 000 000 | RWD | Yes |
| 0x0004 | `command_timeout` | s | 0.010–1.000 | 0.050 | RWD | Yes |
| 0x0005 | `command_source` | enum {USB, CAN} | — | USB (A0) / CAN (A1) | RWD | Yes |
| 0x0010 | `gear_ratio` | — | 1–100 | 20 | RWD | Yes |
| 0x0011 | `gear_efficiency_model` | — | 0.5–1.0 | 0.85 | RWD | Yes |
| 0x0012 | `motor_pole_pairs` | — | 1–50 | TBD (from the motor) | RWD | Yes |
| 0x0013 | `motor_kt` | N·m/A | 0.01–1.0 | TBD | RWD | Yes |
| 0x0014 | `motor_phase_resistance` | Ω | 0.01–10 | Measured | RWD | Yes |
| 0x0015 | `motor_phase_inductance` | H | 1e-6–1e-2 | Measured | RWD | Yes |
| 0x0016 | `motor_feedback_source` | enum {HALL, ENCODER, HALL+ENCODER} | — | TBD | RWD | Yes |
| 0x0020 | `motor_encoder_offset` | rad (electrical) | −π…π | Calibrated | RWD | Yes |
| 0x0021 | `motor_direction` | ±1 | — | Calibrated | RWD | Yes |
| 0x0022 | `output_encoder_offset` | rad | −π…π | Calibrated | RWD | Yes |
| 0x0023 | `output_direction` | ±1 | — | Calibrated | RWD | Yes |
| 0x0024 | `backlash_tolerance` | rad | 0–0.1 | 0.02 (TBC, from measurement) | RWD | Yes |
| 0x0030 | `q_min_soft` | rad | ≥ q_hard_min + margin | 0.0873 (5°, TBC) | RWD | Yes |
| 0x0031 | `q_max_soft` | rad | ≤ q_hard_max − margin | 2.269 (130°, TBC) | RWD | Yes |
| 0x0032 | `q_hard_min` / `q_hard_max` | rad | From the mechanical design | −0.087 / 2.443 (−5° / 140°, TBC) | RWD | Yes |
| 0x0033 | `v_max` | rad/s | 0–6.0 | 4.712 (45 RPM) | RWD | Yes |
| 0x0034 | `a_max` | rad/s² | 0–100 | 10 (TBC, SYS-REQ-013) | RWD | Yes |
| 0x0035 | `v_limit_zone` / `v_limit_zone_angle` | rad/s / rad | — | 2.36 (50 %) / 0.1745 (10°) | RWD | Yes |
| 0x0036 | `tau_max` | N·m | 0–the approved peak | 20 (TBC) | RWD | Yes |
| 0x0037 | `tau_cont` | N·m | 0–15 | 10 | RWD | Yes |
| 0x0038 | `i2t_peak_time` | s | 0–10 | 2 (TBC) | RWD | Yes |
| 0x0039 | `i_max_phase` | A | 0–hardware limit | TBD (from the motor and board) | RWD | Yes |
| 0x003A | `tracking_error_threshold` / `time` | rad / s | — | 0.1 / 0.2 (TBC) | RWD | Yes |
| 0x003B | `torque_mode_enabled` | bool | — | false (A0), TBC (A1) | RWD | Yes |
| 0x0040 | `kp_pos`, `kd_pos` / `kp_vel`, `ki_vel` | SI | — | Tuned | RW | Yes |
| 0x0041 | `kp_cur`, `ki_cur` | V/A, V/(A·s) | — | Derived from R and L | RW | Yes |
| 0x0042 | `gravity_ff_enabled`, `gravity_ff_mgr`, `gravity_ff_offset` | —, N·m, rad | — | false / 6.08 / 0 | RW | Yes |
| 0x0050 | `v_bus_overvoltage` / warning | V | 26–34 | 32 / 30 (TBC) | RWD | Yes |
| 0x0051 | `v_bus_undervoltage` / warning | V | 12–22 | 18 / 20 (TBC) | RWD | Yes |
| 0x0052 | `t_motor_fault` / warning | °C | — | TBD from the datasheet | RWD | Yes |
| 0x0053 | `t_ctrl_fault` / warning | °C | — | 95 / 80 (TBC) | RWD | Yes |
| 0x0060 | `safe_state_option` | enum {COAST, ACTIVE_DAMPING} | — | COAST (until ACT-DEC-020) | RWD | Yes |
| 0x0061 | `position_limit_class` | enum {WARNING, FAULT} | — | FAULT | RWD | Yes |
| 0x0070 | `telemetry_rate_usb` | Hz | 10–1000 | 100 | RW | Yes |
| 0x0071 | `heartbeat_rate` | Hz | 1–50 | 10 | RWD | Yes |
| 0x0072 | `can_termination` | bool | — | Read from hardware | R | — |

### 7.2 Cross-checks in configure()

1. q_hard_min < q_min_soft < q_max_soft < q_hard_max, each with ≥ the configured margin.
2. tau_max ≤ the approved peak, and ≤ the gearbox peak rating (SAF-REQ-027).
3. i_max_phase ≤ the hardware current rating of the board or PCB (read from the hardware revision).
4. tau_cont ≤ tau_max. v_max ≤ the speed achievable at 24 V (warning only).
5. command_timeout is within its range; it cannot be 0 or disabled.
6. v_bus_overvoltage is below the component voltage rating minus margin.

## 8. USB/UART protocol (A0 and debug)

### 8.1 Physical and link

- USB CDC virtual COM, or UART **115 200 8N1** by default. **921 600 baud** can be selected for binary telemetry (TBC with the board's bridge).
- No flow control.

### 8.2 CLI mode (default at power-up)

- ASCII, one command per line, LF-terminated (CR LF accepted).
- Responses are `OK [data]` or `ERR <code> <text>`.

| Command | Example | Notes |
|---|---|---|
| `help` | `help` | Lists the commands |
| `version` | `version` → `OK hw=A1-r1 fw=0.3.0+g1a2b3c proto=1.0 sn=KA0001` | |
| `state` | `state` → `OK DISABLED q=0.1234 dq=0.000 iq=0.00 vbus=24.1 tm=31 tc=29` | |
| `faults` / `clear` | | |
| `enable` / `disable` | | Subject to the command-source rules (IF-REQ-057) |
| `pos <rad>` / `vel <rad/s>` / `tor <N·m>` | `pos 0.5` | Motion commands refresh the timeout; a host tool must resend them |
| `get <param>` / `set <param> <value>` / `save` | `set v_max 3.0` | Names as in §7 |
| `cal <kind>` | `cal MOTOR_OFFSET` | |
| `capture <signals> <rate> <n>` | `capture iq,id 20000 2000` | Capture buffer (FW-REQ-041) |
| `mode binary` | | Switches to binary mode (IF-REQ-054) |

### 8.3 Binary mode

The frame layout is little-endian:

| Field | Size | Value |
|---|---|---|
| SOF | 2 | 0xA5 0x5A |
| Length | 1 | Payload length N (0–250) |
| Type | 1 | Message type |
| Sequence | 1 | Rolling 0–255 |
| Payload | N | Per type |
| CRC-16 | 2 | CRC-16/CCITT-FALSE (poly 0x1021, init 0xFFFF, no reflection, xorout 0x0000) over Length..Payload |

| Type | Direction | Payload |
|---|---|---|
| 0x01 | Host → actuator | Command: function ID (uint8) plus arguments, float32 each |
| 0x02 | Actuator → host | Response: function ID, return code (uint8), data |
| 0x10 | Actuator → host | Telemetry: timestamp_us (uint32), q, dq, tau_est, iq, id, v_bus, t_motor, t_ctrl (float32), state, mode (uint8), active-fault bitmap (uint32) |
| 0x11 | Actuator → host | Capture data block |
| 0x20 | Actuator → host | Fault event: code (uint16), class (uint8), timestamp_us (uint32) |
| 0x7F | Host → actuator | Return to CLI mode |

Frames with a bad CRC or length are discarded and counted (IF-REQ-053).

## 9. Versioning

- **Interface/protocol version:** MAJOR.MINOR. MAJOR changes break compatibility, and the host must refuse a mismatched major version (`E_VERSION_MISMATCH`). MINOR changes add optional content only.
- **Firmware version:** semantic versioning, plus the git hash.
- This document's revision history records each interface version change.

## 10. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | Freeze function names and the numeric codes | Project Lead | ACT-03-001 review |
| 2 | Default node ID and the factory configuration | Electronics/Embedded Intern | F1 |
| 3 | Defaults depending on the motor (Kt, pole pairs, current limits) | Both interns | After motor selection |
| 4 | Enable behaviour: hold position vs zero torque (compliance tests) | Project Lead | ACT-03-001 |
| 5 | USB/UART high baud rate verification | Electronics/Embedded Intern | A0 bring-up |

## 11. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft (interface version 1.0, proposed) |
