# Kritva Actuator: Load Cases

| Field | Value |
|---|---|
| Document ID | KA-CALC-LOAD |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Mechanical Intern |
| Reviewer / Approver | Independent Mechanical Reviewer / Project Lead |
| Applies to | A1 (design basis), A0 (motor sizing) |
| Classification | Proprietary and confidential |

> **Status note.** Every input here is a proposed baseline (ACT-DEC-008) or an explicit assumption. The forearm centre of mass (180 mm) is **provisional** and must be replaced with a CAD or measured value (SYS-REQ-011). These results become binding only after approval recorded in `planning/v1/DECISIONS.md`.

---

## 1. Purpose

This document defines the **elbow load cases** that size the motor, gearbox, output shaft, bearings, hard stops, housing and test fixture. It is the canonical calculation behind MECH-REQ-001 and the load-case section of `requirements/MECHANICAL_REQUIREMENTS.md`.

All numbers are reproduced by:

```
python3 mechanical/calculations/actuator_sizing.py --section load
```

The script's `INPUTS` block holds the values. After changing any input, re-run the script and update this document in the same pull request.

## 2. Inputs and assumptions

| # | Quantity | Symbol | Value | Status | Source |
|---|---|---|---|---|---|
| I1 | Forearm + hand mass | m_a | 1.5 kg | PROPOSED | Approved elbow load selection (ACT-DEC-008) |
| I2 | Forearm/hand centre of mass from the elbow axis | r_a | 180 mm | **PROVISIONAL** | Explicit assumption; replace with CAD or measurement |
| I3 | Payload mass | m_p | 1.0 kg | PROPOSED | ACT-DEC-008 |
| I4 | Payload centre from the elbow axis | r_p | 350 mm | PROPOSED | ACT-DEC-008 |
| I5 | Gravitational acceleration | g | 9.81 m/s² | Fixed | — |
| I6 | Worst static orientation | — | Forearm horizontal | Fixed | Maximum gravity moment |
| I7 | Output speed target | n | 45 RPM (ω = 4.712 rad/s) | PROPOSED | ACT-DEC-008 |
| I8 | Angular acceleration requirement | α | **TBD** | OPEN | SYS-REQ-013 |
| I9 | Duty cycle and horizontal holding duration | — | **TBD** | OPEN | SYS-REQ-013 |
| I10 | Peak duration, repetition, recovery | — | ≤ 2 s, ≤ 10 % duty (planning placeholder, TBC) | OPEN | SYS-REQ-021 |
| I11 | Overhang from the forearm load line to the near output bearing | a | 20 mm | ASSUMED | Replace with CAD |
| I12 | Hard-stop contact radius | r_s | 25 mm | ASSUMED | Replace with CAD |

## 3. Static gravity torque (LC-01)

With the forearm horizontal:

```
T_g = m_a·g·r_a + m_p·g·r_p
    = 1.5 × 9.81 × 0.180 + 1.0 × 9.81 × 0.350
    = 2.649 + 3.434
    = 6.082 N·m   (≈ 6.1 N·m)
```

The continuous target of 10 N·m is **1.64 × T_g**. It gives a 64 % torque margin over the calculated gravity load, to cover friction, acceleration and modelling error.

### 3.1 Sensitivity of T_g

T_g in N·m:

| Forearm CoM \ Payload | 0.5 kg | 1.0 kg | 2.0 kg |
|---|---|---|---|
| 150 mm | 3.92 | 5.64 | 9.07 |
| **180 mm** | 4.37 | **6.08** | 9.52 |
| 210 mm | 4.81 | 6.52 | 9.96 |

**Interpretation.**

- A ±30 mm error in the forearm centre of mass changes T_g by about ±0.44 N·m (±7 %).
- Doubling the payload to 2 kg (9.5 N·m) would consume almost all of the 10 N·m continuous rating. The **payload is the dominant sensitivity**, and any change to it must go through a decision.

## 4. Arm inertia and kinetic energy

| Model | Expression | J (kg·m²) | E at 45 RPM |
|---|---|---|---|
| Point masses (baseline) | m_a·r_a² + m_p·r_p² | **0.1711** | **1.900 J** |
| Forearm as a uniform rod of length 2·r_a, plus a point payload | m_a·(2r_a)²/3 + m_p·r_p² | 0.1873 | 2.080 J |
| CAD (to be added) | from mass properties | TBD | TBD |

The motor rotor's **reflected inertia**, J_rotor·N² (N² = 225 / 400 / 625 for 15 / 20 / 25:1), adds to these values once the motor is selected. For example, a rotor of 1×10⁻⁵ kg·m² at 20:1 adds 0.004 kg·m², about 2 %. A larger pancake motor rotor can add more, so this must be checked.

## 5. Dynamic torque (illustrative until α is approved)

T_req = T_g + J·α + T_friction. Friction is excluded here and is measured in A1.

| α (rad/s²), **illustrative only** | Point-mass model | Rod model |
|---|---|---|
| 5 | 6.94 N·m | 7.02 N·m |
| 10 | 7.79 N·m | 7.96 N·m |
| 20 | 9.50 N·m | 9.83 N·m |

For reference, accelerating from rest to 45 RPM (4.71 rad/s) in 0.25 s needs about 19 rad/s². Even aggressive accelerations stay within the 20 N·m peak at the horizontal pose. The **continuous** rating is the limit if such motions are repeated frequently. This is why the duty cycle (I9) must be defined.

## 6. Forces on the output

| Quantity | Value | Note |
|---|---|---|
| Link weight (arm + payload) | 24.53 N | Acts at the combined centre of mass, 248 mm from the axis |
| Centripetal force at 45 RPM | 13.77 N | m·r_cm·ω² |
| Dynamic allowance (planning) | 2 × weight = 49.1 N | Covers the inertial loads of short accelerations; TBC with α |
| Single-sided hard-stop reaction at 25 N·m (stall into stop) | 1 000 N at r_s = 25 mm | F = T / r_s; **governs** the bearings and shaft bending (see SHAFT_STRENGTH and BEARING_SELECTION) |

## 7. Load-case register

| LC | Name | Definition | Output torque | Radial load at the flange | Governs |
|---|---|---|---|---|---|
| LC-01 | Static horizontal hold | Arm horizontal, 0 RPM, held continuously (duration TBD) | 6.08 N·m | 24.5 N | Holding, encoder alignment, thermal holding current |
| LC-02 | Continuous operation | 10 N·m, 0–45 RPM, until thermally stable | 10 N·m | 38.3 N (weight + centripetal) | Fatigue, thermal, bearing life |
| LC-03 | Peak | 20 N·m minimum / 25 N·m stretch, ≤ 2 s, ≤ 10 % duty (TBC) | 20 / 25 N·m | 49.1 N (2 × weight allowance) | Shaft static strength, gearbox peak, coupling |
| LC-04 | Hard-stop impact | The arm strikes a stop at speed; energy 1.90 J at 45 RPM (point mass) | T_stop = 2E/θ_stop (see §8) | F = T_stop / r_s if the stop is single-sided | Stops, bumper, bearings, housing |
| LC-05 | Stall into stop | A firmware fault drives the arm into a stop at the torque limit, held | 20 / 25 N·m | 800–1 250 N (r_s 20–30 mm, single-sided) | Bearings (static), shaft bending, stop lugs, fasteners |
| LC-06 | Handling and assembly | Lifting by the flange; bench knocks; clamping in the fixture | — | TBD (proposal: 50 N at the flange edge in any direction) | Housing, flange, encoder protection |
| LC-07 | External shock on the link | Only if impacts are in scope (SYS-REQ-014) | TBD | TBD | Shock specification (open) |
| LC-08 | Fixture test loads | Load lever with weights, or a torque-sensor rig | As tested, up to 25 N·m | Per fixture design | Fixture (rated ≥ 2 × peak, SAF-REQ-065) |
| LC-09 | Misalignment | Concentricity/angular error between the gearbox output and the output shaft | — | From coupling stiffness × misalignment | Coupling choice, gearbox output bearing |

## 8. Hard-stop energy and stop torque (LC-04)

For a stop with linear compliance, the peak torque is T_peak = 2E/θ_stop. The example uses a bumper stroke of 2 mm at r_s = 25 mm, so θ_stop = 0.08 rad (4.6°).

| Approach speed | Energy E | T_stop for the 2 mm / 25 mm bumper | θ needed for 20 N·m | θ needed for 25 N·m |
|---|---|---|---|---|
| 45 RPM | 1.900 J | **47.5 N·m** | 10.9° | 8.7° |
| 30 RPM | 0.844 J | 21.1 N·m | 4.8° | 3.9° |
| 20 RPM | 0.375 J | 9.4 N·m | 2.2° | 1.7° |
| 15 RPM | 0.211 J | 5.3 N·m | 1.2° | 1.0° |
| 10 RPM | 0.094 J | 2.3 N·m | 0.5° | 0.4° |

With this bumper, the **maximum approach speed that keeps T_stop ≤ 20 N·m is 29.2 RPM**.

**Conclusion.** A full-speed (45 RPM) impact into a compact stop exceeds the peak rating by about 2.4×. The design must combine three measures:

1. firmware approach-speed limiting in the last part of the travel (CTRL-REQ-032, proposed ≤ 50 % v_max within the last 10°);
2. a compliant bumper with enough stroke;
3. a stop reaction path through the housing, and preferably a **balanced (two-sided) stop** so that no net radial force reaches the bearings (BEARING_SELECTION §5).

## 9. Results summary

| Result | Value | Used by |
|---|---|---|
| T_g (horizontal) | 6.08 N·m | ACT-REQ, Gate B holding test |
| Continuous margin | 1.64 × T_g at 10 N·m | ACT-DEC-008 |
| Arm inertia | 0.171 kg·m² (point), 0.187 (rod) | Stops, control tuning, simulation |
| Stop energy at 45 RPM | 1.90 J (point), 2.08 J (rod) | Stops, SAF-REQ-041 |
| Governing radial load | LC-05: 1 000 N (single-sided stop at 25 N·m, r_s = 25 mm) | Bearings, shaft |
| Governing torque | LC-03 / LC-05: 25 N·m (stretch) | Shaft, gearbox, coupling |

## 10. Verification

| What | Method | When |
|---|---|---|
| Recalculation of T_g and J | Independent analysis | M0 (ACT-02-001 REVIEW.md) |
| Forearm centre of mass and mass | Measurement (two-scale or knife-edge balance) or CAD | Gate A |
| Holding torque at the horizontal pose | Bench test on the fixture (Gate B item 1–2) | Gate B |
| Stop impact | Staged impact test (FI-24) | Gate B/C |

## 11. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | Replace the 180 mm centre of mass with a CAD or measured value | Mechanical Intern | Gate A |
| 2 | Approved α and duty cycle | Project Lead | Before the motor/gearbox freeze |
| 3 | Peak duration and repetition | Project Lead | Before the motor/gearbox freeze |
| 4 | Overhang a and stop radius r_s from CAD | Mechanical Intern | M2 |
| 5 | LC-06 handling load value | Mechanical Intern | M2 |
| 6 | Shock specification, if in scope (LC-07) | Project Lead | Gate A |

## 12. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
