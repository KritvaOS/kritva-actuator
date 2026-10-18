# Kritva Actuator: Tool Flow for Mechanical Users (ACT-S, ACT-M, ACT-L)

| Field | Value |
|---|---|
| Document ID | KA-STD-TOOLFLOW-MECH |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 |
| Date | 2026-10-18 |
| Document owner | Project Lead / Integration Owner |
| Reviewer / Approver | Project Lead |
| Applies to | A0, A1 |
| Classification | Proprietary and confidential |

> **Status note.** Proposed working guide, derived from `OPEN_SOURCE_TOOLFLOW.md` (KA-STD-TOOLFLOW), which holds the full reasoning, licence notes and the checked reference list. The toolchain is **not yet frozen**; versions and conventions below are placeholders until the owner records the freeze in `planning/v1/DECISIONS.md`. Tool outputs, exports, FEA runs and CI passes are evidence inputs only. They never close Gate A, B or C. The mechanical HOLD was lifted by ACT-DEC-029, but fabrication, procurement and loaded testing still need Gate A and independent review.

---

## 1. Who this is for and where you work

| Workstream | Repository | Parent path |
|---|---|---|
| ACT-M (reference, elbow) | `kritva-actuator-m` | `mechanical/actuator-m` |
| ACT-S | `kritva-actuator-s` | `mechanical/actuator-s` |
| ACT-L | `kritva-actuator-l` | `mechanical/actuator-l` |

Work in your own repository on a branch and open a pull request. Do not push to the parent. Do not edit the interface, CAN protocol or units: raise a design change request in the parent. M is the reference. S and L start only after M's sizing and Design review checklist pass, and reuse M's structure and checklists.

## 2. Tools

| Purpose | Tool | Status |
|---|---|---|
| Sizing and checks | Existing Python sizing engine, `check_calcs`, `make check` | Required, already in the repo |
| CAD, assemblies, drawings | FreeCAD | Proposed to freeze |
| Scripted or repeated geometry | CadQuery | Optional |
| Simple jigs and covers | OpenSCAD | Optional, non-load-bearing parts only |
| FEA | FreeCAD FEM with CalculiX | Optional, after load cases and boundary conditions are reviewed |
| BOM | Existing BOM CSV and `check_bom` | Required |
| Large binary files | Git LFS | Decide at freeze |

Do not use two tools as the master model of the same load-bearing part.

## 3. Step by step

1. **Set inputs.** Put the variant's inputs in `sizing/inputs.json` of your repository. Use the parent's requirements and load cases (`requirements/`, `mechanical/calculations/`). Units are explicit.
2. **Run sizing.** Run the shared sizing engine with your inputs (`--inputs mechanical/actuator-<m|s|l>/sizing/inputs.json`; see `mechanical/common-sizing/README.md`). Write variant results to `sizing/results/` in your repository. M's elbow documents in the parent stay the A0 reference.
3. **Select components.** Motor and gearbox are chosen together with the embedded engineer (hand-off in section 5). Tie every rating to a manufacturer datasheet and revision. A Python calculation does not replace checking that the gearbox supports the operating point.
4. **Model in FreeCAD.** Follow the CAD naming standard (`docs/standards/CAD_NAMING_STANDARD.md`) and the frozen units and templates. Model housing, output shaft, bearing seats, gearbox mount, encoder mount and the assembly.
5. **Check calculations.** Shaft (torsion, bending, combined, fatigue, deflection), bearings (loads, life, fits, spacing, preload), gearbox limits, fasteners and housing load paths. Document assumptions.
6. **Optional FEA.** Record material, constraints, loads, mesh and convergence, and compare with the analytical result. A finished solve does not show the model is right.
7. **Design review and Gate A.** Complete `docs/standards/DESIGN_REVIEW_CHECKLIST.md`. Fabrication starts only after Gate A passes with independent review (ACT-DEC-014) and the pending decisions (for example gearbox, motor, bearing, peak torque) are recorded.
8. **Drawings, assembly, BOM.** Export drawing PDFs and STEP, write the assembly procedure, and fill the BOM (`docs/standards/BOM_STANDARD.md`).
9. **Fabricate, inspect, test.** Loaded or peak-torque tests only on a restrained, guarded, instrumented fixture with a test-readiness record (ACT-DEC-015).
10. **Release.** Tag the child repository. The Project Lead pins that commit in the parent.

## 4. What the checks cover (and do not)

| Check | Proposed behaviour | Does not prove |
|---|---|---|
| `make check` | Calculations, BOM, docs, links, traceability | Design acceptance |
| BOM check | Required columns, unique IDs, part number, manufacturer, revision | The part is the right one |
| Export check | STEP, STL and PDF exist, are non-empty and parse | The geometry is correct |
| Geometry check | Valid solids, bounding box and volume in range | Strength or fit |
| FEA input check | Input present, solver runs, benchmark case matches | The load case is realistic |

Compare STEP files by geometry with tolerances, not byte hashes. A released STEP or drawing is tied to one commit and is never silently regenerated. Headless CAD export in CI must be qualified before it blocks merges.

## 5. Hand-offs with the embedded workstream

| You give ACT-EMB | You get from ACT-EMB |
|---|---|
| Motor choice, torque constant, pole pairs, gear ratio, encoder mount envelope, PCB envelope | Controller footprint, connector pinout, thermal limits |

Record each hand-off in the parent as a dependency with your child commit SHA.

## 6. Deliverables per variant

Native CAD and assembly, STEP, STL where applicable, drawing PDFs, BOM CSV, shaft/bearing/gearbox calculation report, FEA report if used, assembly and inspection procedure, and test report. Each names the commit, tool versions and the checksums of generated files. Keep them private; do not publish them as public CI artifacts.

## 7. References (checked 2026-10-18)

| Item | Link |
|---|---|
| FreeCAD source | https://github.com/FreeCAD/FreeCAD |
| FreeCAD documentation (named by external review, not opened here) | https://www.freecad.org/documentation/ |
| FreeCAD tutorial video: "FreeCAD Parametric Modelling Tutorial – Master the Basics of 3D Design", Open Source CNC | https://www.youtube.com/watch?v=LrFmUwd8HXs |
| CadQuery source | https://github.com/CadQuery/cadquery |
| CadQuery documentation (not opened here) | https://cadquery.readthedocs.io/ |
| OpenSCAD source | https://github.com/openscad/openscad |
| CalculiX (official site) | http://www.calculix.de/ |

Licences are listed in `OPEN_SOURCE_TOOLFLOW.md`. Tutorials teach concepts; use the manual for the frozen FreeCAD version.

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-18 | Kritvaos Actuator Team | Initial mechanical guide split from KA-STD-TOOLFLOW |
