# Kritva Actuator: Software/Hardware Boundary

| Field | Value |
|---|---|
| Document ID | KA-DOC-ARCH-SWHW |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A0, A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** This allocation is proposed and pending approval. Reaction times are TBC with the selected hardware.

---

## 1. Purpose

This document defines **which function is implemented where**: in hardware, actuator firmware, KritvaOS Edge, or host/Nexus software. It also states which layer is the **authority** for each safety-relevant function. Without this split, protections tend to be assumed rather than implemented, or duplicated inconsistently.

## 2. Layers

| Layer | Contents | Owner |
|---|---|---|
| L0 Mechanical | Hard stops, bumpers, guarding, load path | Mechanical Intern |
| L1 Hardware (electronics) | Fuse, reverse polarity, hardware overcurrent comparator → PWM break, gate-driver UVLO and faults, e-stop removal of motor power, pull-downs on gate inputs, watchdog peripheral | Electronics/Embedded Intern |
| L2 Actuator firmware | FOC, joint control, limits, state machine, fault manager, calibration, telemetry, protocol | Electronics/Embedded Intern |
| L3 Edge (real-time host) | Multi-joint coordination, joint map, command timing, start-up checks | Project Lead / Integration Owner |
| L4 Nexus / host tools | Planning, user tools, logging, tuning UI, simulation | Project Lead / Integration Owner |

## 3. Allocation table

| Function | L0 | L1 HW | L2 FW | L3 Edge | L4 Host | Authority | Reaction time (proposed) |
|---|---|---|---|---|---|---|---|
| Over-travel protection | Hard stops | — | Soft limits, approach-speed limit | Joint-limit check of trajectories | Planning respects limits | **L0 (final), L2 (primary)** | — |
| Overcurrent | — | Comparator → PWM break | Software threshold, I²t | — | — | **L1** | < 10 µs (HW), 3 samples (SW) |
| Emergency stop | — | Removes motor power (gate enable / contactor) | Detects and reports `ESTOP_ACTIVE`; latches the state | Broadcasts disable; stops trajectories | Operator button | **L1** | ≤ 10 ms |
| Firmware hang | — | Independent watchdog; gates default off | Supervised servicing | Heartbeat loss detection | — | **L1** | ≤ 20 ms |
| Communication loss | — | — | Command timeout → safe state | Detects missing feedback | — | **L2** | Timeout + 5 ms |
| Over- and under-voltage | Fuse | Gate-driver UVLO; clamp or brake | Thresholds, regeneration limiting | — | — | **L2** (L1 backup) | 1–10 ms |
| Overtemperature | — | (Optional HW thermal cut-out) | Warning, derate, fault | Load reduction on warning | Display | **L2** | 10–100 ms |
| Encoder fault | — | — | Validity checks, cross-check | — | — | **L2** | 3 samples |
| Torque, velocity and acceleration limits | — | — | Enforced on every command source | Trajectory limits | UI limits | **L2** | Every cycle |
| Commutation and current control | — | Inverter | FOC | — | — | L2 | 20 kHz |
| Joint position and velocity control | — | — | Joint loops | Setpoints | — | L2 | 1–2 kHz |
| Trajectory generation | — | — | Limiter / profiler | Multi-joint trajectories | Planning | L3 (for robot motion), L2 (single joint) | — |
| Gravity compensation | — | — | Optional feed-forward term | Full arm model (A2) | — | L3 (A2) | — |
| Calibration | — | — | Routines and storage | — | Host tool initiates | L2 | — |
| Configuration validity | — | — | Atomic validated configure() | Joint-map and CRC verification | Tool | **L2** | — |
| Duplicate node ID | — | — | Reports its ID | Detects duplicates; refuses enable | — | **L3** | Start-up |
| Logging and diagnostics | — | — | Fault log, counters, capture | Aggregation | Storage, analysis | L2 / L4 | — |
| Simulation | — | — | — | — | SimulatedActuator | L4 | — |

## 4. Principles

1. **The most severe hazards have hardware authority.** Overcurrent, e-stop and firmware hang are handled in L1. The firmware reports them but is not relied on to act.
2. **The actuator protects itself.** L2 limits apply regardless of what L3/L4 command (SAF-REQ-050). Host-side limits are additional, never a replacement.
3. **No safety function depends on communication.** Loss of communication is itself a fault, handled locally.
4. **One fault vocabulary.** The same fault codes are used in L2, the protocol, L3 and L4 (IF-REQ-155).
5. **Test builds only.** Fault-injection hooks (for example disabling the firmware e-stop reaction, to prove the L1 path) exist only in clearly marked test builds. They are never in release firmware.

## 5. A0 differences

On the development board:

- L1 functions depend on the board's capabilities. Missing hardware overcurrent or enable inputs are **recorded limitations**, mitigated by the PSU current limit and the bench e-stop relay (SAF-REQ-058).
- L3 does not exist. The host PC talks directly to the firmware over USB/UART.

## 6. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
