---
study_id: FS-M-006
title: Bearing and Support Feasibility - Input Register
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
upstream_sources:
- FS-M-001 inputs/INPUTS.md
- FS-M-002 outputs/LOAD_CASES.csv
- FS-M-004 outputs/INTERFACE_COMPATIBILITY.csv
- FS-M-005 outputs/SHAFT_LOAD_CASES.csv
---

# FS-M-006 Input Register

## 1. Purpose and Rules

Record authoritative upstream inputs, study dependencies and the candidate-specific data needed for bearing/support feasibility.

- Preserve upstream IDs, values, units and statuses.
- Use `FS6-IN-nnn` for local inputs, `FS6-ASM-nnn` for assumptions and `FS6-OQ-nnn` for open questions.
- Reference upstream ASM-001..ASM-012 and OQ-001..OQ-014 by ID; do not redefine them.
- Use `UNKNOWN` for missing evidence. Do not infer a passing result from absent ratings or dimensions.
- Record exact manufacturer/model, source revision, units and operating conditions for each candidate claim.
- Do not silently change IN-015 or IN-016; the mismatch requires an explicit project decision.

## 2. Required FS-M-001 Inputs

Authoritative source: `kritva-m/FS-M-001-integrated-actuator-system/inputs/INPUTS.md`.

| Upstream ID | Value / meaning | Status | Use in FS-M-006 |
|---|---|---|---|
| IN-007 | Peak output torque: 20 N·m minimum / 25 N·m stretch | PRELIMINARY | Shaft and bearing load-case context; use approved FS-M-002/005 cases |
| IN-015 | Independent output shaft nominal diameter 12 mm | PRELIMINARY | Initial shaft/bearing interface |
| IN-016 | 6202 bearing associated with 15 mm seats | ASSUMED | Mismatch: 6202 has a 15 mm bore; cannot directly fit a 12 mm shaft |
| IN-018 | Hard-stop kinetic energy approximately 1.9 J | PRELIMINARY | Stop/impact case context; conditions must be verified |
| IN-019 | Estimated full-speed impact torque approximately 47.5 N·m | PRELIMINARY | Preliminary impact screening only; provenance unresolved |
| IN-023 | Static strength factor target 1.5 | ASSUMED | Context for structural checks; do not apply as an unsupported bearing factor |
| IN-026 | Duty cycle and continuous holding duration | UNKNOWN | Required for life and operating suitability |
| IN-030 | Expected service life | UNKNOWN | No life-compliance claim until resolved |
| IN-031 | Peak duration/repetition/recovery | UNKNOWN | Needed for transient and life assessment |
| IN-036 | Single-contact hard-stop load-sharing case governs | ASSUMED | Use as a provisional case pending validation |

The authoritative input register governs all statuses. This study must not independently promote PRELIMINARY or ASSUMED inputs to confirmed facts.

## 3. Bearing Bore and Interface Note

A 6202 bearing has a nominal 15 mm bore. This is incompatible with a nominal 12 mm shaft without a separately justified interface solution. A 6001 or 6201 series bearing has a nominal 12 mm bore and may be investigated as a candidate series, but neither is selected here.

Do not infer suitability from bore alone. Verify exact candidate dimensions, dynamic/static ratings, speed, combined-load capability, arrangement, fits and manufacturer limitations. The 6202/15 mm seat versus 12 mm shaft conflict must be resolved jointly with FS-M-005 and submitted to the Project Lead. Do not silently modify IN-015 or IN-016.

## 4. Upstream Assumptions and Open Questions

Use `kritva-m/FS-M-001-integrated-actuator-system/ASSUMPTIONS_AND_OPEN_QUESTIONS.md` for ASM-001..ASM-012 and OQ-001..OQ-014. In particular, OQ-009 concerns shock-load assumptions and OQ-012 concerns provenance of the impact estimate. Reference existing IDs rather than duplicating them.

Do not treat IN-018 kinetic energy as equivalent to a bearing force or IN-019 impact torque. Convert load cases only through a documented model with stated geometry, duration, load path and assumptions.

## 5. FS-M-002 Load Dependencies

Upstream study: `kritva-m/FS-M-002-load-torque-analysis/`.

| Artifact | Purpose | Required checks |
|---|---|---|
| `outputs/LOAD_CASES.csv` | Approved load-case definitions and conditions | Path, revision, units, directions and review status |
| `outputs/DYNAMIC_TORQUE_RESULTS.csv` | Dynamic torque and operating cases | Revision, assumptions and applicable operating points |
| `outputs/REFLECTED_INERTIA.csv` | Inertia context where relevant | Reference convention and axis; not a substitute for bearing reactions |

Record the exact source revision used. If a required load case is missing, do not reconstruct it from a summary without authorization.

## 6. FS-M-004 Gearbox Dependencies

Upstream study: `kritva-m/FS-M-004-gearbox-selection-ratio-optimization/`.

Required artifact: `outputs/INTERFACE_COMPATIBILITY.csv`, plus exact-candidate manufacturer drawings and load-rating evidence.

Use this information to:

- Confirm the gearbox interface and torque-transfer arrangement.
- Identify any permitted radial, axial or tilting loads that are explicitly rated for the exact gearbox output bearing.
- Establish packaging and service access.
- Verify that arm loads bypass gearbox and motor bearings unless manufacturer limits explicitly allow the calculated loads.

Do not assume the gearbox output bearing is the actuator's dedicated arm-support bearing.

## 7. FS-M-005 Shaft Dependencies

Upstream/peer study: `kritva-m/FS-M-005-output-shaft-feasibility/`.

Use these exact outputs and verify each path, revision, units and review status:

| Artifact | Use |
|---|---|
| `outputs/SHAFT_LOAD_CASES.csv` | Shaft loads and reactions; source for bearing reaction analysis |
| `outputs/SHAFT_STRENGTH_CHECK.csv` | Critical sections and shaft-strength implications |
| `outputs/IMPACT_CHECK.csv` | Impact assumptions and applicable stop-load cases |
| `outputs/DEFLECTION_CHECK.csv` | Shaft deflection/slope and encoder alignment handoff |
| `outputs/INTERFACE_CHECK.csv` | Shaft/gearbox/bearing interface constraints |
| `outputs/MATERIAL_COMPARISON.csv` | Shaft material context relevant to fits and support |

If bearing reactions or support coordinates are not defined, coordinate an update with FS-M-005. Do not treat a shaft load summary as a bearing reaction calculation unless it explicitly contains the relevant reactions and support assumptions.

## 8. Section A - Study-Local Inputs

Initial status is `UNKNOWN` unless stated otherwise. Record each candidate separately; do not merge ratings from different models.

| ID | Input | Units / format | Initial status | Required evidence / handling |
|---|---|---|---|---|
| FS6-IN-001 | Bearing manufacturer and exact model | Text | UNKNOWN | Manufacturer catalogue or datasheet |
| FS6-IN-002 | Bearing type and internal design | Text | UNKNOWN | Exact model documentation |
| FS6-IN-003 | Bore, outside diameter and width | mm | UNKNOWN | Dimensioned manufacturer drawing |
| FS6-IN-004 | Basic dynamic load rating C | N | UNKNOWN | Exact model and catalogue revision |
| FS6-IN-005 | Basic static load rating C0 | N | UNKNOWN | Exact model and catalogue revision |
| FS6-IN-006 | Permitted radial/axial loads and combined-load method | N, method | UNKNOWN | Manufacturer data and applicable conditions |
| FS6-IN-007 | Limiting/reference speed | RPM | UNKNOWN | Manufacturer source, lubrication and load conditions |
| FS6-IN-008 | Equivalent dynamic/static load factors | Dimensionless | UNKNOWN | Applicable standard or manufacturer method |
| FS6-IN-009 | Required load spectrum and bearing reactions | N, N·m, time/cycles | UNKNOWN | Approved FS-M-005 load cases and support geometry |
| FS6-IN-010 | Bearing spacing and pair arrangement | mm, configuration | UNKNOWN | Coordinated shaft/housing concept |
| FS6-IN-011 | Locating/floating strategy | Text | UNKNOWN | Axial thermal expansion and assembly analysis |
| FS6-IN-012 | Preload or internal clearance | Class/value | UNKNOWN | Manufacturer guidance and tolerance/thermal analysis |
| FS6-IN-013 | Shaft-seat fit and tolerances | mm, fit designation | UNKNOWN | FS-M-005 shaft design and manufacturer guidance |
| FS6-IN-014 | Housing-seat fit and tolerances | mm, fit designation | UNKNOWN | Housing material/process and load direction |
| FS6-IN-015 | Housing material and manufacturing process | Text | UNKNOWN | Structural/stiffness justification and process evidence |
| FS6-IN-016 | Seat surface finish, roundness and coaxiality | Drawing tolerances | UNKNOWN | Manufacturer and assembly requirements |
| FS6-IN-017 | Static equivalent load and safety method | N, method | UNKNOWN | Applicable standard/manufacturer guidance |
| FS6-IN-018 | Dynamic equivalent load and L10 method | N, hours/cycles | UNKNOWN | Applicable method, speed and load spectrum |
| FS6-IN-019 | Life modification/reliability factors | Factors, basis | UNKNOWN | Traceable standard/manufacturer method |
| FS6-IN-020 | Hard-stop/impact bearing reaction | N, N·m, duration | UNKNOWN | Reviewed upstream impact case and reaction model |
| FS6-IN-021 | Lubrication and maintenance | Type, interval | UNKNOWN | Exact bearing/arrangement documentation |
| FS6-IN-022 | Sealing and contamination conditions | Text/IP or environmental data | UNKNOWN | Approved environment and candidate evidence |
| FS6-IN-023 | Operating ambient and bearing temperature | °C | UNKNOWN | SYS-REQ-090 and thermal assessment |
| FS6-IN-024 | Thermal expansion and clearance change | mm/°C or calculation | UNKNOWN | Material, geometry and operating range |
| FS6-IN-025 | Encoder alignment and support stiffness limits | Canonical/manufacturer limits | UNKNOWN | SYS-REQ-034 and FS-M-005 handoff |
| FS6-IN-026 | Replacement/serviceability constraints | Text/drawing | UNKNOWN | Assembly concept and independent replacement review |
| FS6-IN-027 | Candidate mass and envelope | kg, mm | UNKNOWN | Exact model datasheet |
| FS6-IN-028 | Exact part number and supplier | Text | UNKNOWN | Verified manufacturer/distributor source |
| FS6-IN-029 | Price, currency and quote/listing date | Currency, amount, date | UNKNOWN | Dated, traceable source |
| FS6-IN-030 | India sourcing and lead time | Supplier, location, lead time | UNKNOWN | Supplier evidence; distinguish stock from enquiry |
| FS6-IN-031 | Source provenance and revision | URL/path, date, page/table | UNKNOWN | Required for every numerical claim |

Add new inputs with unused `FS6-IN-nnn` IDs as needed. Every input change must retain its provenance and downstream impact.

## 9. Calculation Conventions

Use a stated, applicable method for static equivalent load, dynamic equivalent load and bearing life. Document the exact bearing type, manufacturer factors, load directions, speed, lubrication, contamination, alignment and load spectrum assumptions. Do not apply a generic formula without checking whether its bearing-type assumptions are valid.

Life calculations must be treated as conditional while IN-026, IN-030 or IN-031 remains UNKNOWN. A catalogue C or C0 value alone is not a pass.

For impact cases, record the source load case, reaction distribution, duration/repetition assumptions, relevant static-rating comparison and independent review disposition. Do not assume an ordinary static rating proves impact survival.

## 10. Input Change Control

Change upstream values only in their authoritative source, with the required review and revision. Recalculate affected outputs and record how the change affects candidate ranking, life assessment, interfaces and downstream studies.

The IN-015/IN-016 conflict requires a documented Project Lead decision with FS-M-005 coordination. Do not silently substitute 6001/6201 for 6202 or change the shaft diameter.

## 11. Input Completeness Gate

Before a verified bearing suitability claim, confirm:

- Load cases and shaft reactions are traceable to reviewed upstream artifacts.
- Exact candidate ratings, dimensions, speed and permitted load conditions are sourced.
- Bearing type, spacing, fits, clearance/preload and retention are justified.
- Static and dynamic checks use an applicable method.
- Life requirements and duty are resolved, or the life claim is withheld.
- Impact reactions are assessed and independently reviewed.
- Shaft/housing seats, material/process and encoder alignment are coordinated.
- The IN-015/IN-016 mismatch is formally dispositioned.
- Mandatory outputs and source register are reproducible.

If any required safety-critical input remains unresolved, a preliminary comparison may proceed, but the result must not be presented as a verified design.

## 12. Repository starting evidence (as of 2026-10-24)

The repository already holds draft calculation and design documents that overlap this study. They are **starting points, not verified evidence**: each is a draft pending approval, none has been independently reviewed, and several figures were gathered by an AI reviewer session and not re-checked against vendor pages. Read them first, then reproduce or re-source what you rely on and register it in `references/SOURCE_REGISTER.csv`. They do not change the status of any upstream input.

| Source | What it gives | Limits |
|---|---|---|
| `mechanical/calculations/BEARING_SELECTION.md` (rev 0.3) | Bearing arrangement and reaction method (assumed bearing spacing L = 25 mm and overhang a = 20 mm), candidate deep-groove sizes with generic C and C0, static factor target s0 of at least 2.0 and life target L10h of at least 2,000 h (both TBC) | Generic catalogue values, not vendor-verified; geometry assumed; 6202 is a candidate, not a released part (BOM item MB-004, status CANDIDATE) |
| `mechanical/calculations/LOAD_CASES.md` section 8.2 | Governing single-sided stop reaction (1,000 N at 25 mm radius for a 25 N·m stall) | Screening estimate |

Proposed resolution of the 12 mm shaft versus 15 mm bearing bore mismatch (IN-016, OQ-011): `BEARING_SELECTION.md` section 9 proposes stepping the bearing seats to 15 mm with a 6202-size pair (s0 about 2.1) while the shaft stays 12 mm between the seats, and allows 6001/6201 on 12 mm seats only if a balanced stop is proven and decision ACT-DEC-019 is recorded. This is a proposal pending approval, not a decision. The axial and moment loads, the duty cycle (for life) and the vendor ratings remain open.
Child requirement documents also exist and are not yet reconciled with this study: `requirements/MECHANICAL_REQUIREMENTS.md` (MECH-REQ-nnn) and `requirements/ELECTRICAL_REQUIREMENTS.md` (ELEC-REQ-nnn). Check which IDs apply and cite them by ID.
