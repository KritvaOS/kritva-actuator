# Kritva Actuator: Mechanical Risk Register

| Field | Value |
|---|---|
| Document ID | KA-AUD-MECH-RISK |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.2 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Independent Mechanical Reviewer (with input from the Mechanical Intern) |
| Reviewer / Approver | Independent Mechanical Reviewer / Project Lead |
| Applies to | A1 |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** This is the initial set of mechanical failure modes, prepared with the documentation baseline. The reviewer must confirm the ratings, and they are re-assessed at M2 and M3. Ratings use the scale below: S × O, with a detection factor D for prioritisation.

---

## 1. Purpose and boundaries

This register records the **mechanical failure modes** of the actuator. For each one it gives the cause and consequence, the existing design controls, the required mitigation, the verification method, the residual risk and its review status.

- **Safety hazards** at system level (HAZ-NNN) are in `requirements/SAFETY_REQUIREMENTS.md`.
- **Project risks** (RISK-NNN) are in `planning/v1/RISKS_AND_DEPENDENCIES.md`.
- Entries here cross-reference those registers instead of repeating them.

## 2. Rating scale

| Score | Severity (S) | Occurrence (O) | Detection (D: ability to detect before harm) |
|---|---|---|---|
| 1 | Cosmetic | Very unlikely | Certain (inspection or test catches it) |
| 2 | Degraded performance | Unlikely | High |
| 3 | Loss of function, repairable | Possible | Moderate |
| 4 | Part failure or ejection; injury possible | Likely | Low |
| 5 | Serious injury possible | Very likely | None |

- **Priority** = S × O × D.
- **≥ 40:** a mitigation is required before Gate A.
- **20–39:** a mitigation is required before Gate B.

## 3. Register

| ID | Failure mode | Cause | Consequence | Existing controls | S | O | D | RPN | Required mitigation | Verification | Residual (S·O·D) | Link | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MR-01 | Output shaft yields or fractures | Single-sided stop stall load (≈ 1 000 N); EN8 normalised; keyway Kt | Arm drops; parts ejected | 12 mm EN19 Q&T proposal; SF analysis | 5 | 3 | 3 | 45 | Balanced stop; EN19 Q&T with certificate; no keyway at the peak-moment section | SHAFT_STRENGTH review (M2); material certificate (M3) | 5·1·2 = 10 | HAZ-008; PO-01/02 | Open |
| MR-02 | Output bearing brinelling or overload | Stop or impact radial load; s0 < 2 | Play, noise, encoder misalignment | Bearing analysis | 3 | 3 | 3 | 27 | Balanced stop; span ≥ 25 mm; s0 ≥ 2 | BEARING_SELECTION (M2); post-test inspection | 3·1·2 = 6 | PO-01 | Open |
| MR-03 | Gearbox tooth damage | Impact torque > rating; peak above rating | Loss of holding; backlash growth | Torque limit ≤ the lower of the approved peak and the gearbox rating | 4 | 3 | 3 | 36 | Approach-speed limit; compliant bumper; I²t | FI-24; GB re-check after impacts | 4·1·2 = 8 | HAZ-018; PO-03 | Open |
| MR-04 | Gearbox output bearing overloaded by external loads | Rigid connection to the shaft; misalignment | Gearbox failure | Independent shaft and coupling (ACT-DEC-009) | 3 | 2 | 3 | 18 | Coupling selected for offset; concentricity tolerance | M2 tolerance check | 3·1·2 = 6 | LC-09 | Open |
| MR-05 | Coupling slip or failure | Under-rated coupling; clamp torque | Loss of joint control | Coupling rated ≥ peak + margin | 4 | 2 | 3 | 24 | Rating check; clamp torque; witness marks | M2; post-test inspection | 4·1·2 = 8 | — | Open |
| MR-06 | Encoder magnet slips or debonds | Poor bonding; heat; impact | Wrong position (HAZ-010) | Cross-check fault (CTRL-REQ-005) | 4 | 3 | 2 | 24 | Keyed seat plus a qualified adhesive; post-test check | C5 repeatability after DU-03 | 4·1·1 = 4 | HAZ-010 | Open |
| MR-07 | Encoder air gap out of tolerance | Shaft deflection; bearing clearance; tolerance stack | Noisy or invalid angle | Stationary encoder PCB near the bearing | 3 | 3 | 2 | 18 | Tolerance stack analysis | M2; magnet-status bits logged | 3·1·1 = 3 | — | Open |
| MR-08 | Hard-stop lug fracture or bumper failure | Impact energy too high; aluminium bearing stress | Over-travel; parts ejected | Soft limits; approach-speed limit | 4 | 3 | 3 | 36 | Steel insert lugs if needed; bumper sizing; spare bumpers | FI-24; inspection | 4·1·2 = 8 | HAZ-007 | Open |
| MR-09 | Fasteners loosen | Vibration; no thread-locker; aluminium threads | Misalignment, separation | Torque table, thread-locker, witness marks | 3 | 3 | 2 | 18 | Engagement ≥ 2d in aluminium; inserts where screws are removed often | Post-test inspection | 3·1·1 = 3 | HAZ-017 | Open |
| MR-10 | Housing bearing bore wear or fretting | Aluminium bore; thermal expansion loosening the fit | Play; noise | Fits per BEARING_SELECTION | 3 | 2 | 3 | 18 | Steel carrier if the fit loosens in the thermal test | PC-03; post-test inspection | 3·1·2 = 6 | — | Open |
| MR-11 | Housing deflection under load | Thin walls; long overhang | Misalignment; encoder error | Stiffness check | 3 | 2 | 3 | 18 | Housing analysis or FEA at M2 | M2; M3-14 | 3·1·2 = 6 | — | Open |
| MR-12 | 3D-printed part in the load path fails | Mis-specification | Part failure | SAF-REQ-043 rule | 4 | 2 | 2 | 16 | Drawing review: material check | M2 | 4·1·1 = 4 | RISK-009 | Open |
| MR-13 | Motor mount slips | Torque reaction at peak motor torque | Misalignment; gearbox input damage | Manufacturer pattern and pilot | 3 | 2 | 3 | 18 | Torque check of the mount screws; dowel | M2 | 3·1·2 = 6 | MECH-REQ-084 | Open |
| MR-14 | Cable chafe at the joint | Cable crossing the moving parts | Short circuit; signal loss | No cables across the output (SAF-REQ-048) | 3 | 2 | 2 | 12 | Routing review | M2; inspection | 3·1·1 = 3 | HAZ-021 | Open |
| MR-15 | Thermal softening of polymer parts near the motor | Motor surface > 70 °C | Deformation | MATERIAL_SELECTION rules | 2 | 3 | 2 | 12 | PA-CF or aluminium near the motor | PC-03 | 2·1·1 = 2 | — | Open |
| MR-16 | Fixture moves or fails during peak tests | Under-rated fixture | Load falls; injury | Fixture rated ≥ 2 × peak (SAF-REQ-065) | 5 | 2 | 2 | 20 | Fixture review before first use | TEST_EQUIPMENT §3 | 5·1·1 = 5 | HAZ-016 | Open |
| MR-17 | Pinch or crush at the joint | Fingers in the sweep or the stops | Injury | Guarding, clear zone, hands-off rule | 5 | 2 | 2 | 20 | Pinch-point marking; guard | Gate C review | 5·1·1 = 5 | HAZ-006 | Open |
| MR-18 | Arm drops on power loss | No brake; coast safe state | Impact on the fixture or a hand | Fixture rest; optional damping | 4 | 3 | 1 | 12 | Rest or catch at the low position | FI-23 | 4·1·1 = 4 | HAZ-009 | Open |

## 4. Top mechanical risks (initial)

1. **MR-01 (45):** shaft under single-sided stop stall. Mitigate with the EN19 Q&T shaft, design for single-contact engagement, and the balanced stop credited only after proof (LOAD_CASES §8.2).
2. **MR-03 (36):** gearbox overload by impact.
3. **MR-08 (36):** stop lug or bumper failure.
4. **MR-02 (27):** bearing static overload.

## 5. Review history

| Date | Gate | Reviewer | Changes |
|---|---|---|---|
| 2026-10-11 | — | (baseline) | Initial register |

## 6. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
| 0.2 | 2026-10-12 | Kritvaos Actuator Team | MR-01 mitigation updated per EXT-AUD-004 |
