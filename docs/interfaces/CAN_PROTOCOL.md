# Kritva Actuator: CAN Protocol (v1)

| Field | Value |
|---|---|
| Document ID | KA-DOC-IF-CAN |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead / Integration Owner |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** This is protocol version **1.0, proposed**. The identifier layout follows INTERFACE_REQUIREMENTS IF-REQ-065. The payload encoding (scaled 16-bit integers) is **proposed under ACT-DEC-022** and is not yet accepted. Function codes are frozen only after the F1 review.

---

## 1. Purpose

This document is the **single canonical CAN definition** (IF-REQ-079) used by the actuator firmware (`firmware/communication/`, `communication/can/firmware/`), the KritvaOS driver (`software/kritva_driver/`) and the host tools (`communication/can/tools/`). A machine-readable form (DBC and a generated C header) will be generated from this document in `communication/can/protocol/` (ACT-03-002).

## 2. Physical and data-link layer

| Item | Value |
|---|---|
| Standard | ISO 11898-1/-2 classic CAN 2.0 (11-bit identifiers). Hardware should be CAN FD capable for future use |
| Bit rate | 1 Mbit/s (500 kbit/s selectable) |
| Sample point | 87.5 % (at both rates) |
| SJW | 1 time quantum (TBC, tuned per the MCU clock) |
| Termination | 120 Ω at the two physical bus ends only; selectable on the actuator, off by default (IF-REQ-063) |
| Byte order | Little-endian |
| Data length | 8 bytes for every frame in v1, unless stated otherwise |

## 3. Identifier

```
 bit: 10  9  8  7  6 | 5  4  3  2  1  0
      function code  |   node ID (0-63)
 ID = (function_code << 6) | node_id      node 0 = broadcast
```

Lower function codes win arbitration, so they have **higher priority**.

| FC | Name | Direction | Node 0 (broadcast) allowed? | Rate |
|---|---|---|---|---|
| 0 | `STOP_ALL` | Host → all | **Only** with node 0 (ID 0x000) | Event |
| 1 | `FAULT_EVENT` | Actuator → host | No | Event, within one feedback period |
| 2 | `NMT_COMMAND` (enable / disable / clear faults / set command source) | Host → actuator | Disable only | Event |
| 3 | `SETPOINT_POSITION` | Host → actuator | **No** (IF-REQ-077) | Up to 1 kHz |
| 4 | `SETPOINT_VELOCITY` | Host → actuator | No | Up to 1 kHz |
| 5 | `SETPOINT_TORQUE` | Host → actuator | No | Up to 1 kHz |
| 6 | `FEEDBACK` | Actuator → host | — | One per setpoint, or periodic |
| 7 | `FEEDBACK_EXT` (currents, motor velocity) | Actuator → host | — | Configurable, ≥ 10 Hz |
| 8 | `STATUS_HEARTBEAT` | Actuator → host | — | 10 Hz (all states) |
| 9 | `NMT_RESPONSE` | Actuator → host | — | Event |
| 10 | `PARAM_REQUEST` | Host → actuator | No | Event |
| 11 | `PARAM_RESPONSE` | Actuator → host | — | Event |
| 12 | `VERSION_REQUEST` | Host → actuator | Yes (discovery) | Event |
| 13 | `VERSION_RESPONSE` | Actuator → host | — | Event |
| 14 | `TIME_SYNC` | Host → all | Yes | 1–10 Hz (optional) |
| 15–29 | Reserved | | | |
| 30 | `BOOTLOADER` (future, A2 goal) | Both | No | |
| 31 | Reserved, never allocated (IF-REQ-067) | | | |

Examples for node 10:

| Frame | Calculation | ID |
|---|---|---|
| SETPOINT_POSITION | (3 << 6) \| 10 | 0x0CA |
| FEEDBACK | (6 << 6) \| 10 | 0x18A |
| STATUS_HEARTBEAT | (8 << 6) \| 10 | 0x20A |

## 4. Scaling (proposed, ACT-DEC-022)

| Quantity | Type | LSB | Range | Notes |
|---|---|---|---|---|
| Position q (output) | int16 | 1×10⁻⁴ rad (0.0057°) | ±3.2767 rad (±187.7°) | Covers −5° to 140° with margin |
| Velocity (output) | int16 | 1×10⁻³ rad/s | ±32.767 rad/s | Nominal max 4.71 rad/s |
| Torque (output) | int16 | 1×10⁻³ N·m | ±32.767 N·m | Peak 25 N·m plus headroom |
| Current (q/d) | int16 | 1×10⁻² A | ±327.67 A | |
| Motor velocity | int16 | 1×10⁻¹ rad/s | ±3 276.7 rad/s | 1 125 RPM × 2π/60 = 117.8 rad/s |
| Bus voltage | uint16 | 1×10⁻² V | 0–655.35 V | |
| Temperature | int8 | 1 °C | −128…127 °C | |
| Fault code | uint16 | — | ACTUATOR_INTERFACE §6 | |

A value that would exceed its field range saturates at the limit, and the frame's `SAT` flag is set.

## 5. Payload definitions

### 5.1 FC 3: SETPOINT_POSITION (8 bytes)

| Byte | Field | Type | Notes |
|---|---|---|---|
| 0–1 | q_target | int16 | rad × 10⁴ |
| 2–3 | dq_ff | int16 | rad/s × 10³ (0 if unused) |
| 4–5 | tau_ff | int16 | N·m × 10³ (0 if unused; A2) |
| 6 | alive counter | uint8 | Must advance by 1 (mod 256), else rejected (IF-REQ-076) |
| 7 | flags | uint8 | bit 0: request extended feedback; bits 1–7 reserved (0) |

### 5.2 FC 4: SETPOINT_VELOCITY / FC 5: SETPOINT_TORQUE (8 bytes)

| Byte | FC 4 | FC 5 |
|---|---|---|
| 0–1 | dq_target (int16, ×10³) | tau_target (int16, ×10³) |
| 2–3 | tau_ff (int16, ×10³) | reserved (0) |
| 4–5 | reserved (0) | reserved (0) |
| 6 | alive counter | alive counter |
| 7 | flags | flags |

### 5.3 FC 6: FEEDBACK (8 bytes)

| Byte | Field | Type |
|---|---|---|
| 0–1 | q | int16 (rad × 10⁴) |
| 2–3 | dq | int16 (rad/s × 10³) |
| 4–5 | tau_est | int16 (N·m × 10³) |
| 6 | status | uint8: bits 0–2 state (§3 State enum), bits 3–4 mode, bit 5 FAULT active, bit 6 WARNING active, bit 7 SAT |
| 7 | echo counter | uint8 (the alive counter of the setpoint answered, or a rolling counter if periodic) |

### 5.4 FC 7: FEEDBACK_EXT (8 bytes)

| Bytes | Field |
|---|---|
| 0–1 | iq (int16, A × 10²) |
| 2–3 | id (int16, A × 10²) |
| 4–5 | motor velocity (int16, rad/s × 10) |
| 6 | t_motor (int8, °C) |
| 7 | t_ctrl (int8, °C) |

### 5.5 FC 8: STATUS_HEARTBEAT (8 bytes)

| Bytes | Field |
|---|---|
| 0 | state (uint8) |
| 1 | mode (uint8) |
| 2–3 | highest-priority active fault code (uint16; 0 if none) |
| 4–5 | v_bus (uint16, V × 10²) |
| 6 | number of active faults (uint8) |
| 7 | rolling counter (uint8) |

### 5.6 FC 1: FAULT_EVENT (8 bytes)

| Bytes | Field |
|---|---|
| 0–1 | fault code (uint16; bit 15 = warning) |
| 2 | class (0 WARNING, 1 FAULT, 2 CRITICAL) |
| 3 | state after the reaction |
| 4–7 | timestamp (uint32, ms since boot) |

### 5.7 FC 2: NMT_COMMAND (8 bytes) and FC 9: NMT_RESPONSE

| Byte | Command | Response |
|---|---|---|
| 0 | command: 1 ENABLE, 2 DISABLE, 3 CLEAR_FAULTS, 4 SET_COMMAND_SOURCE_CAN, 5 SAVE_CONFIG, 6 CALIBRATE | echo of the command |
| 1 | argument (calibration kind; 0 otherwise) | return code (ACTUATOR_INTERFACE §5) |
| 2–7 | reserved | detail (for example the failing parameter ID, bytes 2–3) |

### 5.8 FC 10/11: PARAM_REQUEST / PARAM_RESPONSE (8 bytes)

| Byte | Request | Response |
|---|---|---|
| 0 | op: 1 READ, 2 WRITE | op echo |
| 1 | transaction ID (uint8) | transaction ID |
| 2–3 | parameter ID (uint16) | parameter ID |
| 4–7 | value (float32 or int32 per the parameter type; ignored for READ) | value (READ) or return code in byte 4 (WRITE) |

Configuration writes over CAN are allowed only in DISABLED for RWD parameters. They do not disturb real-time timing (IF-REQ-078).

### 5.9 FC 12/13: VERSION_REQUEST / VERSION_RESPONSE

The request is empty (DLC 0). Broadcast is allowed, for discovery. The response is 8 bytes:

| Bytes | Field |
|---|---|
| 0 | protocol major |
| 1 | protocol minor |
| 2 | firmware major |
| 3 | firmware minor |
| 4 | firmware patch |
| 5 | hardware revision code |
| 6–7 | serial number (lower 16 bits) |

### 5.10 FC 0: STOP_ALL (ID 0x000)

The payload is byte 0 = 0xA5 (guard), with bytes 1–7 = 0. Every actuator performs `disable()` and holds DISABLED. It is used by Edge on any system-level fault. It does not replace the hardware e-stop.

## 6. Timing and rates

| Item | Value |
|---|---|
| Setpoint/feedback rate | 500 Hz target, 1 kHz goal (IF-REQ-071) |
| Command-to-application latency | ≤ 1 ms (TBC) |
| Measurement-to-feedback latency | ≤ 1 ms (TBC) |
| Heartbeat | 10 Hz in every state; the host flags a lost node after 3 missed periods |
| Command timeout | 50 ms default (parameter 0x0004) |
| Fault event | Within one feedback period |

**Bus load** (single elbow at 500 Hz): one setpoint (≈ 135 bits worst case) plus one feedback frame gives ≈ 13.5 %. Adding FEEDBACK_EXT at 50 Hz and the heartbeat at 10 Hz gives ≈ 14.3 %. This leaves room for about 4–5 actuators per bus at 500 Hz below 70 % load. Recompute this for each robot configuration.

## 7. Behaviour rules

1. Motion setpoints are accepted only in ENABLED, and only when CAN is the active command source. Otherwise the actuator replies with an NMT_RESPONSE carrying `E_INVALID_STATE` or `E_BUSY` (at a limited rate) and counts the event.
2. A setpoint whose alive counter has not advanced is rejected and does not refresh the timeout.
3. Bus-off while ENABLED leads to `CAN_BUS_OFF` and the safe state (IF-REQ-069). Automatic bus-off recovery happens after 100 ms (TBC), and the actuator stays DISABLED until it is re-enabled.
4. The first frame after boot is the heartbeat in BOOT/DISABLED state, followed by a VERSION_RESPONSE when one is requested.

## 8. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | ACT-DEC-022 encoding decision (scaled int16 vs float32 with multi-frame) | Project Lead | F1 |
| 2 | SJW and bit timing per the MCU clock | Electronics/Embedded Intern | F1 |
| 3 | DBC and header generation tooling | Project Lead | ACT-03-002 |
| 4 | CAN FD migration plan (v2) | Project Lead | A2 |
| 5 | Bus-off recovery policy | Electronics/Embedded Intern | F1 |

## 9. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft (protocol v1.0, proposed) |
