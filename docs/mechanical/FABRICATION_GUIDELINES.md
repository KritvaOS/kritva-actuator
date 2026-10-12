# Kritva Actuator: Fabrication Guidelines

| Field | Value |
|---|---|
| Document ID | KA-DOC-MECH-FAB |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Mechanical Intern |
| Reviewer / Approver | Independent Mechanical Reviewer / Project Lead |
| Applies to | A0 (fixture and prints), A1 |
| Classification | Proprietary and confidential |

> **Status note.** These are proposed guidelines for prototype fabrication in local workshops. Tolerance values are proposals until confirmed by the tolerance analysis at M2. **No part is released for fabrication before Gate A.**

---

## 1. Purpose

This document sets out how drawings are prepared, which processes are used for which parts, the tolerances and surface finishes required, how parts are inspected, and how to work with workshops. It supports SYS-REQ-038, SYS-REQ-104/105 and the M2/M3 gates.

## 2. Release rules

1. Parts are fabricated only from **released drawings** in `mechanical/drawings/`, which carry a revision letter, are approved at Gate A, and are referenced in the BOM.
2. A drawing change after release needs a design change request (DCR) and a new revision letter. The workshop always gets the current revision **PDF**, plus the **STEP** for CNC programming.
3. Request a quotation from **two workshops** for critical parts (RISK-013). Record the quotes in the BOM (`cost_status = QUOTED`).

## 3. Drawing standard

| Item | Rule |
|---|---|
| Standard | ISO 128 / ISO 129 for presentation, ISO 1101 for GD&T, ISO 2768-mK for general tolerances, unless noted otherwise |
| Projection | First-angle (ISO E), stated in the title block |
| Units | mm |
| Title block | Part number (KA-MEC-NNNN), name, revision, material **and condition** (for example EN19 Q&T), finish or treatment, mass, drawn/checked/approved names and dates, "Proprietary and confidential – Kritvaos" |
| Datums | Bearing bores (housing) and bearing seats (shaft) are the primary datums |
| Critical features | Marked with a symbol and listed on the inspection sheet |
| Notes | Deburr all edges 0.2–0.5 × 45°; break sharp edges; remove all swarf; no tool marks on bearing seats |

## 4. Process selection

| Part | Process | Workshop capability needed |
|---|---|---|
| Output shaft (EN19 Q&T) | CNC turning; cylindrical grinding of the bearing seats (or fine turning to tolerance if grinding is unavailable, TBC); milling of the D-flat | Lathe with ±0.005 mm capability on seats |
| Housing and plate (Al 6061-T6) | 3-axis CNC milling; both bearing bores **in one set-up** (or line-boring) | CNC mill, bore gauge |
| Output flange | CNC turning plus milling | — |
| Stop pins | Standard hardened dowel pins (bought) or turned EN19 | — |
| Encoder mount, covers | FDM print (PETG / PA-CF) or CNC aluminium | — |
| Fixture | Aluminium extrusion plus machined plates, or a welded steel frame | — |

## 5. Tolerances and finishes (proposed)

| Feature | Tolerance | Surface finish (Ra) | Rationale |
|---|---|---|---|
| Shaft bearing seats, Ø12 | k5 (+0.001/+0.009) or j5 (TBC per the bearing vendor) | ≤ 0.4 µm | Rotating inner-ring fit |
| Housing bearing bores (located / floating) | K7 / H7 (TBC) | ≤ 0.8 µm | Stationary outer ring; the floating bearing slides |
| Coaxiality of the two bearing bores | ≤ 0.01–0.02 mm (TBC) | — | Bearing life, encoder runout |
| Gearbox pilot to output bore | Concentricity ≤ 0.05 mm (TBC) | — | Coupling misalignment (LC-09) |
| Shaft runout at the flange seat relative to the bearing seats | ≤ 0.01 mm | — | Encoder and flange |
| Bearing shoulder perpendicularity | ≤ 0.01 mm | — | Bearing alignment |
| Encoder magnet seat to shaft axis | Concentricity per the encoder IC (typically ≤ 0.05–0.1 mm, TBC) | — | Encoder accuracy |
| Stop-lug positions | ±0.1 mm, with the slots adjustable | — | Balanced contact |
| General | ISO 2768-mK | 3.2 µm | — |

## 6. Heat treatment and materials

- Order shaft material as **EN19 bar in the Q&T (T) condition**, with a mill certificate. If heat treatment is done after rough machining, specify the hardness (for example 248–302 HB, TBC) and finish-machine afterwards.
- Do not weld or heat-straighten load-path parts without approval.
- Material substitution by a workshop needs written approval from the Mechanical Intern **and** the Project Lead, and a re-check of the calculations.

## 7. 3D printing guidelines

| Parameter | Recommendation |
|---|---|
| Materials | PETG for covers; PA-CF for brackets near warm parts; never in the load path (SAF-REQ-043) |
| Wall / perimeters | ≥ 4 perimeters for any part with screws |
| Infill | ≥ 40 % gyroid for brackets |
| Orientation | Load in the XY plane; avoid loading between layers in tension |
| Holes for screws | Print undersize and drill or ream; use heat-set inserts for repeated assembly |
| Records | Material, printer, nozzle, layer height, orientation, infill — noted on the drawing |

## 8. Inspection

Every critical part gets an **inspection sheet**, stored in `mechanical/assembly/` against the part serial. The sheet records:

- part number and revision, and the workshop;
- the measured value of every critical feature, with the instrument used;
- material certificate reference (shaft, pins);
- visual check: burrs, damage, finish;
- accept/reject, inspector and date.

| Instrument | Use |
|---|---|
| Micrometer (0.001 mm) | Shaft seats |
| Bore gauge (0.002 mm) | Bearing bores |
| Dial indicator + V-blocks | Runout |
| Height gauge / CMM (if available) | Positions |
| Surface roughness tester (if available) or comparator | Seats and bores |

Non-conforming parts get a non-conformance record (`test_failure` Issue template). The disposition is one of: rework, use-as-is with an approved rationale (**not** for safety-critical features), or scrap.

## 9. Working with workshops

1. Send the PDF drawing, the STEP file, the quantity, the material and its condition, the required certificates and the target date.
2. Ask the workshop to confirm that they can hold the critical tolerances **before** ordering.
3. Agree that out-of-tolerance parts are reported, not reworked silently.
4. Respect confidentiality: share only the files needed for the part, and mark them "Proprietary and confidential – Kritvaos".

## 10. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | Tolerance analysis (stack-up for the encoder gap and the coupling misalignment) | Mechanical Intern | M2 |
| 2 | Bearing-vendor fit recommendations | Mechanical Intern | M2 |
| 3 | Workshop shortlist (2 minimum) | Mechanical Intern | Week 4 |
| 4 | Grinding availability for the shaft seats | Mechanical Intern | M2 |

## 11. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
