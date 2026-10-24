# Kritva Actuator: Output Shaft Strength

| Field | Value |
|---|---|
| Document ID | KA-CALC-SHAFT |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.2 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Mechanical Intern |
| Reviewer / Approver | Independent Mechanical Reviewer / Project Lead |
| Applies to | A1 |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** The 12 mm diameter is the initial CAD candidate (ACT-DEC-009, proposed). It is not yet a validated design. Geometry values (overhang, free length) and stress-concentration factors are **assumed** until the CAD and detail design exist. Material properties are indicative minima that must be verified against the standard and the mill certificate. This calculation is safety-relevant and needs independent review (ACT-DEC-014).

---

## 1. Purpose

This document checks the independent output shaft for:

- static strength under combined torsion and bending, including stress concentration;
- fatigue under continuous operation;
- torsional and lateral stiffness;

for every load case in `LOAD_CASES.md`. It identifies the governing case and states the minimum material and diameter. It supports MECH-REQ-002, SYS-REQ-030 and Gate A item 3.

Numbers are reproduced by `python3 mechanical/common-sizing/actuator_sizing.py --section shaft`.

## 2. Shaft model

```
 gearbox output --[coupling]--> |=====[B_far]======[B_near]====|== flange --> forearm
                                      <------ L ------>  <- a ->
                                    bearing span (25 mm)  overhang (20 mm, assumed)
```

- The shaft is a solid round shaft, d = 12 mm, between the coupling and the output flange.
- Torque enters through the coupling (keyway, D-flat or spline: detail TBD) and leaves through the flange (bolted, or a keyed hub).
- The radial load F acts at the flange, a distance a beyond the near bearing. Bending moment at the near bearing: M = F·a.
- The stop reaction is applied at the flange (single-sided stop, worst case).

| Section property (d = 12 mm) | Value |
|---|---|
| Polar second moment J_p = πd⁴/32 | 2 036 mm⁴ |
| Bending section modulus Z_b = πd³/32 | 169.6 mm³ |
| Torsional section modulus Z_t = πd³/16 | 339.3 mm³ |

**Assumed stress-concentration factors** (to be replaced with values for the actual detail, from Peterson's charts or FEA):

- Kt = 2.0 at the keyway or flat, applied to torsion;
- Kt = 1.7 at the bearing shoulder fillet (r/d ≈ 0.05), applied to bending.

## 3. Formulae

```
τ = T / Z_t                         σ_b = M / Z_b          (M = F · a)
σ_vM = sqrt(σ_b² + 3 τ²)            (nominal)
σ_vM,Kt = sqrt((Kt_b σ_b)² + 3 (Kt_t τ)²)   (conservative: peaks assumed coincident)
θ = T · L_free / (G · J_p)          G = 80 GPa
SF_yield = S_y / σ_vM,Kt
```

## 4. Static results

| Load case | T (N·m) | F at flange (N) | M (N·mm) | τ (MPa) | σ_b (MPa) | σ_vM nominal (MPa) | σ_vM with Kt (MPa) | Twist over 30 mm |
|---|---|---|---|---|---|---|---|---|
| LC-01 hold | 6.08 | 24.5 | 491 | 17.9 | 2.9 | 31.2 | 62.3 | 0.064° |
| LC-02 continuous | 10.0 | 38.3 | 766 | 29.5 | 4.5 | 51.2 | 102.4 | 0.106° |
| LC-03 peak 20 | 20.0 | 49.1 | 981 | 58.9 | 5.8 | 102.3 | 204.4 | 0.211° |
| LC-03 peak 25 | 25.0 | 49.1 | 981 | 73.7 | 5.8 | 127.8 | 255.4 | 0.264° |
| **LC-05 stall into a single stop at 25 N·m (r_s = 25 mm)** | 25.0 | **1 000** | **20 000** | 73.7 | **117.9** | 173.7 | **324.5** | 0.264° |

**Governing case: LC-05.** A single-sided stop puts a large radial force on the flange, and therefore a large bending moment on the shaft. Without that force (LC-03), torsion and stress concentration dominate and bending is small.

### 4.1 Safety factor on yield (governing case, with Kt)

| Material (indicative minimum S_y) | S_y (MPa) | SF at LC-05 | Verdict |
|---|---|---|---|
| EN8 / C45, normalised | 280 | 0.86 | **Not acceptable** for LC-05 |
| EN8 / C45, hardened and tempered | 430 | 1.33 | Marginal: below the proposed 2.0 |
| **EN19 / 42CrMo4, Q&T (T condition)** | 650 | **2.00** | Meets SF 2.0 (proposed minimum, TBC) |
| SS304, annealed | 205 | 0.63 | Not acceptable |
| Al 6061-T6 | 275 | 0.85 | Not acceptable for the shaft |

### 4.2 Minimum diameter for SF = 2.0 at LC-05 (same Kt assumptions)

| Material | d_min |
|---|---|
| EN8 / C45, normalised | 15.9 mm |
| EN19 / 42CrMo4, Q&T | 12.0 mm |

## 5. Fatigue check (LC-02, continuous operation)

The model is fully reversed bending (the shaft rotates under a fixed radial load), with steady torsion over each revolution, using the Modified Goodman criterion. The endurance limit is S_e ≈ 0.5·S_u × k_surface (0.8, machined) × k_size (0.9) × k_reliability (0.9). These factors are indicative.

| Material | S_e (MPa) | σ_a (Kt·σ_b) | σ_m,eq (√3·Kt·τ) | n (Goodman) |
|---|---|---|---|---|
| EN8 / C45, normalised | 178 | 7.7 | 102.1 | 4.4 |
| EN19 / 42CrMo4, Q&T | 275 | 7.7 | 102.1 | 6.8 |

Fatigue is **not** governing at the continuous load. Repeated peak or stop events (LC-03/LC-05) should be treated as a low-cycle fatigue case once their count is known (the duty cycle is TBD).

## 6. Stiffness

- **Torsional:** 0.26° of twist over 30 mm at 25 N·m. This is small compared with typical planetary gearbox backlash, but it is included in the stiffness budget (SYS-REQ-025).
- **Lateral deflection at the flange** (cantilever beyond the near bearing, E = 205 GPa, I = πd⁴/64 = 1 018 mm⁴): under LC-05, δ ≈ F·a³/(3EI) = 1000 × 20³ / (3 × 205 000 × 1018) ≈ 0.013 mm. This excludes bearing clearance, and is acceptable for the encoder alignment if the encoder sits near the bearing. The encoder air-gap and runout tolerance must be checked against the encoder IC datasheet (MECH encoder section).

## 7. Recommendations

1. **Material:** specify **EN19 / 42CrMo4 Q&T** (or an equivalent alloy steel with S_y ≥ 650 MPa certified) for the 12 mm shaft. Do not use normalised EN8 at 12 mm unless the single-sided stop load is removed.
2. **Reduce the governing load at its source:** prefer a **balanced, two-sided hard stop** (two stop pins 180° apart reacting against the housing), or place the stop reaction close to the near bearing. **The LC-05 single-sided case remains the design case** until simultaneous engagement is proven (LOAD_CASES §8.2, EXT-AUD-004). The SF 2.0 result for EN19 at 12 mm is therefore the governing result. It is conditional on the assumed geometry, the assumed Kt and indicative material data, so the shaft is **not frozen** on this result (EXT-AUD-005).
3. **Detail design:** avoid a keyway at the maximum-moment section. Prefer a **D-flat or spline at the coupling end** and a **bolted flange** for torque transfer. Use generous shoulder fillets (r ≥ 0.5 mm, TBC with the bearing chamfer).
4. **Recompute** with the CAD values of a, r_s, the free length and the actual Kt, and with **certified** material properties. Record the final SF in this document before Gate A.
5. **Treat repeated stop and impact events as a separate fatigue case** once their count per lifetime is defined (the duty cycle is open). Use the stop torque from the characterised bumper model (LOAD_CASES §8.1), not the idealised linear value.

## 8. Verification

| Item | Method | Gate |
|---|---|---|
| Independent recalculation | Analysis by the Independent Mechanical Reviewer | M2 / Gate A |
| Material certificate | Inspection (mill certificate with S_y and S_u) | M3 |
| Dimensional inspection (diameter, fillets, flat or spline) | Inspection | M3 |
| Post-test inspection for permanent set or cracks (dye penetrant, TBC) | Inspection after Gate B loaded tests | Gate B |

## 9. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | Overhang a, free length and r_s from CAD | Mechanical Intern | M2 |
| 2 | Actual Kt values for the detail features | Mechanical Intern | M2 |
| 3 | Confirm SF target (proposed ≥ 2.0 on yield at the governing case) | Project Lead + reviewer | M2 |
| 4 | Decide the stop configuration (single vs balanced) | Mechanical Intern | M2 |
| 5 | Peak and stop event counts, for low-cycle fatigue | Project Lead (duty cycle) | Gate A |

## 10. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
| 0.2 | 2026-10-12 | Kritvaos Actuator Team | External audit fixes: LC-05 remains design case; result conditional, not frozen; stop fatigue case (EXT-AUD-005/012) |
