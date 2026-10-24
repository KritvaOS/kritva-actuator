---
study_id: FS-M-005
title: Output Shaft Feasibility - Input Register
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
upstream_sources:
- FS-M-001 inputs/INPUTS.md
- FS-M-002 outputs/LOAD_CASES.csv
- FS-M-002 outputs/DYNAMIC_TORQUE_RESULTS.csv
- FS-M-004 outputs/INTERFACE_COMPATIBILITY.csv
---

# FS-M-005 Input Register

## 1. Purpose and Rules

This register defines the upstream and local inputs needed to assess output-shaft feasibility. It does not replace authoritative source registers or approve a shaft geometry.

- Preserve upstream IDs, values, units and statuses exactly.
- Use `FS5-IN-nnn` for local inputs, `FS5-ASM-nnn` for assumptions and `FS5-OQ-nnn` for questions.
- Reference upstream assumptions ASM-001..ASM-012 and questions OQ-001..OQ-014 by ID; do not redefine them.
- Mark unavailable data `UNKNOWN`. Do not turn missing evidence into a passing result.
- Record source, revision, units, method and applicable load case for every numerical calculation.
- Keep material handbook estimates separate from certified properties for the actual material condition.

## 2. Required FS-M-001 Inputs

Authoritative source: `kritva-m/FS-M-001-integrated-actuator-system/inputs/INPUTS.md`.

| Upstream ID | Value / meaning | Status | Use in FS-M-005 |
|---|---|---|---|
| IN-007 | Peak output torque: 20 N·m minimum / 25 N·m stretch | PRELIMINARY | Peak strength screening; reconcile with FS-M-002 cases |
| IN-015 | Output shaft nominal diameter 12 mm | PRELIMINARY | Starting geometry, not an adequacy conclusion |
| IN-016 | 6202 bearing associated with 15 mm seats | ASSUMED | Dimensional mismatch with 12 mm shaft; coordinate with FS-M-006 |
| IN-017 | Arm inertia 0.171 kg·m² | PRELIMINARY | Dynamic/stop analysis only with verified assumptions and applicable axis |
| IN-018 | Mechanical-stop kinetic energy approximately 1.9 J | PRELIMINARY | Hard-stop/impact screening; provenance and case conditions required |
| IN-019 | Estimated full-speed impact torque approximately 47.5 N·m | PRELIMINARY | Impact screening only; provenance unresolved |
| IN-023 | Static strength factor target 1.5 | ASSUMED | Screening target; document failure criterion and margin method |
| IN-031 | Peak duration/repetition/recovery | UNKNOWN | Needed for peak suitability and fatigue assessment |
| IN-036 | Single-contact hard-stop load-sharing case governs | ASSUMED | Analyze as an assumption until validated |
| IN-037 | EN19/42CrMo4 Q&T candidate; EN8 normalised reported safety factor approximately 0.86 | PRELIMINARY | Material comparison; reproduce calculation and source properties |

The authoritative register controls all statuses. Do not promote any preliminary value to verified status locally.

## 3. Upstream Assumptions and Open Questions

Use `kritva-m/FS-M-001-integrated-actuator-system/ASSUMPTIONS_AND_OPEN_QUESTIONS.md` as the authoritative source for ASM-001..ASM-012 and OQ-001..OQ-014.

Relevant questions include:

- OQ-009: shock-load assumptions.
- OQ-012: provenance of the approximately 47.5 N·m impact estimate and approximately 0.86 EN8 safety factor.

Use the other upstream records wherever they affect load geometry, duty, mass properties or material decisions. Reference the existing IDs; do not duplicate or redefine them.

## 4. FS-M-002 Load-Case Dependencies

Upstream study: `kritva-m/FS-M-002-load-torque-analysis/`.

| Artifact | Required use | Validation before use |
|---|---|---|
| `outputs/LOAD_CASES.csv` | Static, gravity, peak and stop/impact load cases | Verify path, revision, units, load directions and case definitions |
| `outputs/DYNAMIC_TORQUE_RESULTS.csv` | Dynamic torque and applicable continuous/RMS/peak conditions | Verify revision, assumptions and reviewer status |
| `outputs/REFLECTED_INERTIA.csv` | Relevant inertia conventions and ratio context | Verify reference axis and definitions; do not assume it contains shaft stress results |
| `outputs/GRAVITY_TORQUE_SWEEP.csv` | Optional gravity-versus-angle evidence if present | Verify file existence and approved revision |

Record the exact commit/revision used in calculation notes. If a required artifact is missing, do not reconstruct it from a summary without authorization. Mark dependent results provisional or blocked.

IN-017 arm inertia is not itself a shaft torque. Its use requires the relevant axis, acceleration/deceleration profile, load geometry and boundary conditions. IN-018 energy and IN-019 impact torque must not be treated as interchangeable inputs.

## 5. FS-M-004 Interface Dependency

Upstream study: `kritva-m/FS-M-004-gearbox-selection-ratio-optimization/`.

Required artifact: `outputs/INTERFACE_COMPATIBILITY.csv`, plus exact-model manufacturer drawings and source evidence.

Check:

- Gearbox output shaft/bore/flange and torque-transfer method.
- Key/keyway, clamp, D-shaft, coupling or other interface details.
- Dimensions, fits, retention and allowable transmitted torque.
- Space for the independent shaft, support bearings and encoder.
- Whether the gearbox interface can be connected without routing arm loads into gearbox or motor bearings.

Do not treat SYS-REQ-033's preferred gearbox output interface of at least 8 mm as proof that a 12 mm independent shaft will fit.

## 6. Section A - Study-Local Inputs

Initial status is `UNKNOWN` unless stated otherwise. Add candidate-specific values with exact model and source identity; do not merge different candidates into one row.

| ID | Input | Units / format | Initial status | Required evidence / handling |
|---|---|---|---|---|
| FS5-IN-001 | Shaft geometry and critical-section dimensions | mm, drawing/CAD revision | UNKNOWN | Dimensioned geometry; identify all shoulders, fillets, grooves and torque-transfer features |
| FS5-IN-002 | Bearing positions and support spacing | mm | UNKNOWN | FS-M-006 concept/drawing; assumptions identified |
| FS5-IN-003 | Applied torque per load case | N·m | UNKNOWN | Approved FS-M-002 load case and revision |
| FS5-IN-004 | Transverse forces, axial force and lever arms | N, mm | UNKNOWN | Load geometry and FS-M-002 evidence |
| FS5-IN-005 | Material grade, condition and heat treatment | Text | UNKNOWN | Specification and material source for actual condition |
| FS5-IN-006 | Yield and tensile properties | MPa | UNKNOWN | Applicable standard, certified data or labelled handbook assumption |
| FS5-IN-007 | Shear strength / applicable failure criterion | MPa, method | UNKNOWN | Traceable source and justified criterion |
| FS5-IN-008 | Fatigue data and mean-stress method | S-N data, MPa, method | UNKNOWN | Source, material condition, surface/size and reliability assumptions |
| FS5-IN-009 | Elastic modulus and Poisson ratio | GPa, dimensionless | UNKNOWN | Traceable material source and temperature/condition |
| FS5-IN-010 | Stress concentration and notch factors | Dimensionless | UNKNOWN | Geometry-based reference or calculation; applicability documented |
| FS5-IN-011 | Shaft surface finish and manufacturing process | Text, roughness units | UNKNOWN | Proposed process and source-supported fatigue adjustment, if used |
| FS5-IN-012 | Material size/heat-treatment effects | Text or factors | UNKNOWN | Evidence or explicit uncertainty |
| FS5-IN-013 | Hard-stop contact/load case | Torque, force, energy, duration | UNKNOWN | Approved FS-M-002 case; IN-018/IN-019 uncertainty recorded |
| FS5-IN-014 | Duty spectrum and peak repetition | Cycles, time, load spectrum | UNKNOWN | Resolution of IN-031 and relevant upstream OQs |
| FS5-IN-015 | Encoder alignment limits | Manufacturer/canonical limits | UNKNOWN | SYS-REQ-034 limits and mounting drawing |
| FS5-IN-016 | Encoder location and mounting geometry | mm, drawing revision | UNKNOWN | Proposed shaft/encoder geometry |
| FS5-IN-017 | Torsional twist and positioning tolerance | deg/rad or canonical units | UNKNOWN | Requirement, geometry and load cases |
| FS5-IN-018 | Bearing-seat dimensions and fits | mm, tolerances | UNKNOWN | Coordinated FS-M-006 design; resolve IN-016 mismatch |
| FS5-IN-019 | Gearbox output interface geometry | Drawing, dimensions and tolerances | UNKNOWN | FS-M-004 exact-candidate source |
| FS5-IN-020 | Shaft runout, coaxiality and surface-finish limits | Drawing tolerances | UNKNOWN | Encoder/bearing/manufacturing requirements |
| FS5-IN-021 | Corrosion and environmental exposure | Text/conditions | UNKNOWN | SYS-REQ-090 and project environment evidence |
| FS5-IN-022 | Critical speed and excitation range | RPM, Hz | UNKNOWN | Calculated estimate and operating-speed range |
| FS5-IN-023 | Material certificate or supplier traceability | Document ID | UNKNOWN | Required for final design verification, not presumed available |
| FS5-IN-024 | Calculation model and revision | Path, commit, version | UNKNOWN | Reproducible spreadsheet/script and input references |
| FS5-IN-025 | Independent review status | Reviewer, date, findings | UNKNOWN | Review record and commit; author cannot self-approve |

Add rows using new `FS5-IN-nnn` IDs when needed. Do not reuse an ID or imply a value has been measured when it is only estimated.

## 7. Initial Stress Reference

For a solid circular shaft under pure torsion:

    tau_max = 16 T / (pi d^3)

At d = 12 mm, nominal shear is approximately 29.5 MPa at 10 N·m, 58.9 MPa at 20 N·m and 73.7 MPa at 25 N·m. This reference excludes bending, axial stress, notches, fatigue, impact dynamics and material variability. It is a check on arithmetic only, not a design pass.

For combined loading, document the selected stress/failure criterion and its applicability to the material and load case. For fatigue, state the method, mean and alternating stresses, relevant material data and uncertainty. Do not report a life result without the required duty and fatigue inputs.

## 8. Input and Evidence Change Control

Any changed upstream value must be updated in its authoritative source, reviewed and tied to a new revision. Recalculate affected results and record the effect on the feasibility recommendation. Keep prior results and decisions traceable; do not silently replace inputs.

Every material property, load, geometry dimension and allowable limit used in a conclusion must have a source-register entry or be explicitly identified as an assumption with its impact explained.

## 9. Input Completeness Gate

Before concluding that a shaft configuration is feasible, verify:

- Approved FS-M-002 load cases and impact assumptions are available.
- FS-M-004 interface geometry is available for the applicable gearbox candidate.
- FS-M-006 bearing support geometry and load path are sufficiently defined.
- Material properties represent the proposed grade and condition.
- Critical sections, combined loading and fatigue assumptions are documented.
- Encoder alignment limits are available for a signoff claim.
- The IN-015/IN-016 mismatch is resolved or the result remains blocked.
- Independent review evidence is recorded for critical strength and impact cases.

A preliminary feasibility calculation can proceed with explicit assumptions, but unresolved safety-critical inputs prevent a verified design conclusion.

## 10. Repository starting evidence (as of 2026-10-24)

The repository already holds draft calculation and design documents that overlap this study. They are **starting points, not verified evidence**: each is a draft pending approval, none has been independently reviewed, and several figures were gathered by an AI reviewer session and not re-checked against vendor pages. Read them first, then reproduce or re-source what you rely on and register it in `references/SOURCE_REGISTER.csv`. They do not change the status of any upstream input.

| Source | What it gives | Limits |
|---|---|---|
| `mechanical/calculations/SHAFT_STRENGTH.md` | 12 mm shaft check at the governing single-sided stop case LC-05: EN8 normalised safety factor 0.86 (not acceptable), EN8 hardened and tempered 1.33, EN19/42CrMo4 Q&T 2.00, with minimum diameters per material | Conditional on assumed geometry, an assumed Kt and indicative material data; the document itself says the shaft is not frozen |
| `mechanical/calculations/LOAD_CASES.md` sections 7 and 8 | Load-case register (LC-01..LC-09) and the stop model behind the governing load | Idealised screening model; the single-sided case governs until a balanced stop is proven |
| `docs/mechanical/MATERIAL_SELECTION.md` and `docs/mechanical/MECHANICAL_DESIGN_SPECIFICATION.md` section 4.4 | Material candidates and the proposed shaft design | Indicative properties; certificates not available |

Points to resolve, not assume: reproduce the 0.86 and 2.00 results independently (IN-037); confirm geometry (overhang, stop radius) from CAD, which does not exist yet; the bearing seats may step to 15 mm (see FS-M-006), so section-by-section checks are needed.
Child requirement documents also exist and are not yet reconciled with this study: `requirements/MECHANICAL_REQUIREMENTS.md` (MECH-REQ-nnn) and `requirements/ELECTRICAL_REQUIREMENTS.md` (ELEC-REQ-nnn). Check which IDs apply and cite them by ID.
