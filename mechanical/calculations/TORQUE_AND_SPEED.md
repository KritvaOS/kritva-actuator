# Kritva Actuator: Torque and Speed Calculations

| Field | Value |
|---|---|
| Document ID | KA-CALC-TORQUE |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Mechanical Intern |
| Reviewer / Approver | Independent Mechanical Reviewer; Electronics/Embedded Intern (motor electrical) / Project Lead |
| Applies to | A0, A1 |
| Classification | Proprietary and confidential |

> **Status note.** The targets (10 N·m continuous, 20–25 N·m peak, 45 RPM, η = 0.85) are proposed and pending approval (ACT-DEC-008). Motor values are illustrative until the motor datasheets are in hand. Nothing here selects a product.

---

## 1. Purpose

This document translates the output requirements into **motor-side torque, speed, power and electrical constants** for each candidate ratio. It is the input to the joint motor/gearbox selection (ACT-02-002, `GEARBOX_SELECTION.md`) and to the power-stage sizing (`docs/electronics/MOTOR_CONTROLLER_SPECIFICATION.md`).

The numbers are reproduced by:

```
python3 mechanical/calculations/actuator_sizing.py --section torque
```

## 2. Relationships

```
Output speed:     ω_out = 2π·n_out / 60           n_motor = N · n_out
Motor torque:     T_motor = T_out / (N · η)
Motor power:      P_motor = T_motor · ω_motor = T_out · ω_out / η
Kv (minimum):     Kv_min = n_motor / (V_bus · k_v · k_s)     k_v = 0.90 (SVPWM), k_s = 0.70 (load margin; same as ACTUATOR_SPECIFICATION §9)
Torque constant:  Kt ≈ 8.27 / Kv   [N·m/A, Kv in RPM/V, FOC phase-peak amps; approximate]
Phase current:    I_q = T_motor / Kt
Reflected inertia at the output:  J_reflected = J_rotor · N²
```

At 45 RPM, ω_out = 4.712 rad/s. At 10 N·m, the output mechanical power is **P_out = 47.1 W**. Because the output power is fixed, the motor mechanical power (≈ 55.4 W at η = 0.85) is the same for every ratio. The ratio only changes the split between motor speed and torque.

The **75–100 W continuous** motor candidate range covers the 55 W shaft power plus the motor's own copper and iron losses. It also gives thermal margin, because many datasheets rate continuous power at a speed well above 900 RPM. The continuous torque **at the operating speed** is what matters, not the advertised power.

## 3. Ratio comparison (η = 0.85)

| Ratio N | Motor speed at 45 RPM | Motor torque, hold (6.08 N·m) | Motor torque, continuous (10 N·m) | Motor torque, peak 20 N·m | Motor torque, peak 25 N·m | Motor power | Kv min at 24 V | Kt at Kv min | N² |
|---|---|---|---|---|---|---|---|---|---|
| 15:1 | 675 RPM | 0.477 N·m | 0.784 N·m | 1.569 N·m | 1.961 N·m | 55.4 W | 44.6 RPM/V | 0.185 N·m/A | 225 |
| **20:1** | **900 RPM** | **0.358 N·m** | **0.588 N·m** | **1.176 N·m** | **1.471 N·m** | **55.4 W** | **59.5 RPM/V** | **0.139 N·m/A** | **400** |
| 25:1 | 1 125 RPM | 0.286 N·m | 0.471 N·m | 0.941 N·m | 1.176 N·m | 55.4 W | 74.4 RPM/V | 0.111 N·m/A | 625 |

**Reading the table.**

- A motor with a **lower Kv** than Kv_min cannot reach 45 RPM at the output under load at 24 V.
- A **much higher Kv** reaches the speed easily but has a lower Kt, so it needs more phase current for the same torque (see section 4).
- The ideal motor has a Kv slightly above Kv_min.

## 4. Phase current versus Kt (20:1 case)

These figures are illustrative. Kt is not yet known. The values feed `requirements/ELECTRICAL_REQUIREMENTS.md` §5.

| Kt (N·m/A) | I_q, hold (0.358 N·m) | I_q, continuous (0.588 N·m) | I_q, peak 20 (1.176 N·m) | I_q, peak 25 (1.471 N·m) |
|---|---|---|---|---|
| 0.05 | 7.2 A | 11.8 A | 23.5 A | 29.4 A |
| 0.08 | 4.5 A | 7.4 A | 14.7 A | 18.4 A |
| 0.12 | 3.0 A | 4.9 A | 9.8 A | 12.3 A |
| 0.139 (at Kv min) | 2.6 A | 4.2 A | 8.5 A | 10.6 A |

**Conclusions.**

- The controller's current rating is driven by the motor's Kt, **not** by the 24 V supply (SYS-REQ-044).
- A small development board rated at a few amps continuous may not support peak-torque tests with a high-Kv motor (RISK-005).

## 5. Motor-class versus ratio trade study

This addresses RISK-001: commercial 24 V BLDCs are commonly rated at high speed with low torque. The class values below are **typical orders of magnitude for each class, not data for any product**. Replace them with datasheet values in GEARBOX_SELECTION.md.

| Motor class (illustrative) | Typical continuous torque | Typical peak torque | Rated speed | Ratio needed for 10 N·m continuous | Ratio needed for 25 N·m peak | Maximum ratio that still gives 45 RPM | Feasible? |
|---|---|---|---|---|---|---|---|
| A: 57 mm inrunner BLDC, 24 V, ~100 W, ~3 000 RPM | 0.32 N·m | 0.95 N·m | 3 000 RPM | 36.8:1 | 31.0:1 | 66.7:1 | Yes, but needs **≈ 37–40:1** (two-stage planetary), giving higher friction and lower backdrivability |
| B: 60–70 mm low-Kv outrunner/pancake | 0.45 N·m | 1.30 N·m | 1 500 RPM | 26.1:1 | 22.6:1 | 33.3:1 | Yes, at **≈ 25–30:1** |
| C: 80–90 mm low-Kv pancake (8108-class) | 0.80 N·m | 2.20 N·m | 900 RPM | 14.7:1 | 13.4:1 | 20.0:1 | Yes, at **≈ 15–20:1** (best backdrivability; larger diameter and higher cost) |

**Key finding.** The 20:1 first candidate (ACT-DEC-003) works with a **low-Kv pancake-class motor** (class C, or the upper end of class B). A standard high-speed inrunner (class A) needs about 37:1 or more.

The ratio decision is therefore **coupled to the motor class**, and must be taken jointly in ACT-02-002 (joint selection rule). If only class-A motors are affordable or available in India, a recorded decision must either:

- extend the ratio set beyond 25:1, or
- reduce the continuous target.

## 6. Operating envelope (output side, 20:1, η = 0.85)

| Corner | Torque | Speed | Notes |
|---|---|---|---|
| Hold | 6.08 N·m | 0 RPM | Continuous holding; copper loss only (I²R), so it is thermally critical |
| Rated continuous | 10 N·m | 0–45 RPM | Thermal test, Gate B item 3 |
| Peak | 20 / 25 N·m | ≤ speed at which back-EMF plus IR drop stays below the bus voltage | ≤ 2 s (TBC) |
| No-load maximum | ≈ 0 N·m | ≥ 45 RPM | Kv margin check |

**Holding note.** At 0 RPM the motor produces no mechanical output, yet the full holding current flows continuously. The copper loss (I_q² · R_phase · 3/2) at 0.358 N·m must be checked against the motor's thermal rating. With a high-Kv motor this can be the limiting case, not the 45 RPM rated point.

## 7. Backdrivability and reflected inertia

- Reflected rotor inertia grows with N². Going from 15:1 to 25:1 multiplies it by **2.8×** (225 to 625).
- Backdrive torque at the output ≈ (motor cogging + friction) · N / η_back, plus gearbox no-load torque. It must be **measured** for each candidate (SYS-REQ-027).
- Higher ratios reduce motor size and current, but make the joint stiffer to backdrive and less transparent for compliant control.

## 8. Verification

| Item | Method | Record |
|---|---|---|
| Kt, R, L, Kv of the selected motor | Measurement in A0 (ACT-01-002b) | `results/motor_control/` |
| Gearbox efficiency over the range | Bench test (input/output torque or power) | `results/mechanical/` |
| 45 RPM at 10 N·m | Gate B test | `results/mechanical/` |
| Holding current and temperature | Thermal test | `results/thermal/` |

## 9. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | Datasheet values for the shortlisted motors (replace the class table) | Mechanical Intern + Electronics/Embedded Intern | M1 |
| 2 | Measured gearbox efficiency (replace η = 0.85) | Mechanical Intern | A1 |
| 3 | Rotor inertia of the selected motor | Mechanical Intern | M1 |
| 4 | Decision on the ratio range if only high-speed motors are available | Project Lead | M1 |

## 10. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
