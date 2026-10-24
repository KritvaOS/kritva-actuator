# Kritva Actuator: Material Selection

| Field | Value |
|---|---|
| Document ID | KA-DOC-MECH-MATERIAL |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Mechanical Intern |
| Reviewer / Approver | Independent Mechanical Reviewer / Project Lead |
| Applies to | A0, A1 |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** The material choices below are proposals. The property values are **indicative minima** for planning. Every load-bearing part must be checked against the governing standard (for example IS 1570 / IS 2062 / IS 733, EN 10083, EN 573/755) and the **supplier's mill certificate** before release.

---

## 1. Purpose

This document records the material and process choice for every mechanical part, together with the rationale, properties, surface treatment and availability. It supports MECH-REQ fabrication requirements and SAF-REQ-043 (no printed parts in the load path without justification).

## 2. Selection criteria

1. **Strength** in the governing load case, with the safety factor targets in the calculations.
2. **Stiffness**, for deflection and encoder alignment.
3. **Machinability** and availability in India (local stockists and workshops).
4. **Cost** within the prototype budget.
5. **Mass**, because the elbow mass loads the shoulder.
6. **Thermal behaviour**: a heat path for the motor; the operating temperature of polymers.
7. **Wear and fretting**, at interfaces such as couplings, stops and bearing seats.

## 3. Candidate materials (indicative properties)

| Material | Condition | S_y min (MPa) | S_u min (MPa) | E (GPa) | Density (g/cm³) | Notes |
|---|---|---|---|---|---|---|
| EN19 / 42CrMo4 | Q&T (T condition) | ≈ 650 | ≈ 850 | 205 | 7.85 | Alloy steel; readily available as bright bar; good for shafts and pins |
| EN8 / C45 | Normalised | ≈ 280 | ≈ 550 | 205 | 7.85 | Cheap and common; insufficient for the 12 mm shaft under LC-05 |
| EN8 / C45 | Hardened and tempered | ≈ 430 | ≈ 700 | 205 | 7.85 | Marginal for the shaft |
| EN24 / 34CrNiMo6 | Q&T | ≈ 680–800 | ≈ 850–1000 | 205 | 7.85 | Alternative to EN19 if available |
| SS304 | Annealed | ≈ 205 | ≈ 515 | 193 | 8.0 | Corrosion resistant; low yield; not for the shaft |
| Al 6061-T6 | T6 | ≈ 240–275 | ≈ 290–310 | 69 | 2.70 | Housing and plates; good machinability; hard anodise optional |
| Al 7075-T6 | T6 | ≈ 430–500 | ≈ 510–570 | 72 | 2.81 | Flange or brackets where higher strength is needed; harder to source |
| PETG (FDM) | As printed | ≈ 40–50 (tensile) | — | ≈ 2 | 1.27 | Covers and guides only |
| PA-CF / PA12-CF (FDM) | As printed | ≈ 60–90 (tensile, orientation-dependent) | — | ≈ 4–8 | 1.2 | Non-structural brackets, fixture accessories |
| Polyurethane | Shore 80–90A | — | — | — | 1.2 | Stop bumpers |

## 4. Part-by-part selection

| Part | Part number | Material / process | Treatment | Rationale | Load path? |
|---|---|---|---|---|---|
| Output shaft | KA-MEC-0003 | **EN19 / 42CrMo4 Q&T**, turned and ground at the bearing seats | Black oxide or zinc; ground seats k5/j5 | SF 2.0 under LC-05 at 12 mm (SHAFT_STRENGTH) | Yes |
| Joint housing | KA-MEC-0001 | **Al 6061-T6**, CNC machined | Optional clear or hard anodise; bearing bores left unanodised or masked | Light, stiff enough, machinable; heat path | Yes |
| Motor/gearbox plate | KA-MEC-0002 | Al 6061-T6, CNC | As above | Heat sink for the motor; precise pilots | Yes |
| Output flange | KA-MEC-0004 | Al 7075-T6 or EN8 H&T (TBC by calculation) | Anodise or black oxide | Carries the forearm and stop loads | Yes |
| Hard-stop pins | KA-MEC-0005 | EN19 Q&T or a hardened dowel pin (ISO 8734) | — | Impact and wear | Yes |
| Stop lugs | Part of the housing, or bolted EN8 lugs | Al 6061 (integral) or steel insert | — | Integral lugs need a bearing-stress check; use a steel insert if aluminium bearing stress is too high | Yes |
| Bumpers | — | Polyurethane Shore 80–90A | — | Replaceable energy absorber | Yes (compliant) |
| Coupling | — | Commercial (Al or steel hubs; Oldham disc in acetal or PEEK) | — | Bought in | Yes |
| Encoder mount | KA-MEC-0006 | Al 6061 (machined) or PA-CF print | — | Must be dimensionally stable for the air gap; not in the load path | No |
| Covers, cable guides | — | PETG or PA-CF print | — | Low cost, quick iteration | No |
| Fixture base and frame | KA-FIX-0001 | Steel plate or aluminium extrusion (40 × 40) | — | Rated ≥ 2 × the peak test torque | Yes (fixture) |
| Fasteners | — | ISO 4762 socket head cap screws, class 12.9 (steel threads) or 8.8 / A2-70 (into aluminium, with thread-length rules) | Medium-strength thread-locker | Standard | Yes |

## 5. Rules for 3D-printed parts

1. Printed parts **must not** be in the primary load path: shaft, bearing seats, gearbox and motor mounts, output flange or hard stops (SAF-REQ-043).
2. A0 fixture brackets may be printed only if the load is small and it is documented. Re-check them if they deform (RISK-009).
3. Polymer parts near the motor must be checked against the motor surface temperature. PETG softens at about 70–80 °C, so PA-CF or aluminium may be needed.
4. Record the print orientation, infill and material for every printed part in the drawing notes.

## 6. Aluminium-specific rules

- **Thread engagement:** at least 2 × d for steel screws into aluminium. Use helicoil inserts where screws are removed often.
- Avoid galvanic issues with stainless steel in humid environments (not critical indoors). Use anti-seize where needed.
- Bearing bores in aluminium: check the fit change with temperature, because aluminium expands about twice as much as steel. A steel bearing carrier is the fallback if the fits loosen in the thermal tests.

## 7. Certification and records

- Order the shaft and pin material **with a mill test certificate**, and keep it in `mechanical/assembly/` against the part serial.
- Record the heat-treatment condition (Q&T) on the drawing title block.

## 8. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | Confirm EN19 Q&T bar availability with a local stockist (12–16 mm bright bar) | Mechanical Intern | M2 |
| 2 | Flange material decision (7075 vs EN8 H&T) by calculation | Mechanical Intern | M2 |
| 3 | Stop-lug bearing stress check (integral aluminium vs steel insert) | Mechanical Intern | M2 |
| 4 | Motor surface temperature, for the selection of polymer parts | Electronics/Embedded Intern | A0 thermal test |

## 9. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
