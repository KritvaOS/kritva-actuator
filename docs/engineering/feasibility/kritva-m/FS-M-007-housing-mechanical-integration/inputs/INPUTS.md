---
study_id: FS-M-007
title: Housing and Mechanical Integration - Input Register
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Project Lead; Independent Reviewer TBD for safety-critical structural and hard-stop checks
upstream_sources:
- FS-M-001 inputs/INPUTS.md
- FS-M-003 candidate motor data
- FS-M-004 outputs
- FS-M-005 outputs
- FS-M-006 outputs
---

# FS-M-007 Input Register

## 1. Purpose and Rules

This register captures upstream inputs, component-study dependencies and local inputs required for the housing and mechanical integration concept.

- Preserve upstream input IDs, values, units and statuses.
- Use `FS7-IN-nnn` for local inputs, `FS7-ASM-nnn` for assumptions and `FS7-OQ-nnn` for open questions.
- Reference FS-M-001 ASM-001..ASM-012 and OQ-001..OQ-014 by ID; do not redefine them.
- Treat concept CAD as concept geometry until interfaces and calculations have been reviewed.
- Use `UNKNOWN` for missing data. Do not invent dimensions, masses, prices, part numbers or budgets.
- Record source path, revision, units, calculation assumptions and evidence for each numerical claim.

## 2. Required FS-M-001 Inputs

Authoritative source: `kritva-m/FS-M-001-integrated-actuator-system/inputs/INPUTS.md`.

| Upstream ID | Value / meaning | Status | Use in FS-M-007 |
|---|---|---|---|
| IN-009 | 24 V nominal supply | PRELIMINARY | Electrical integration context; not a housing dimension |
| IN-014 | Motor data | UNKNOWN | Motor mounting, envelope, mass and thermal path require FS-M-003 candidate data |
| IN-015 | Independent output shaft nominal diameter 12 mm | PRELIMINARY | Shaft/bearing/housing integration; use FS-M-006 decision for interface resolution |
| IN-016 | 6202 bearing associated with 15 mm seats | ASSUMED | Mismatch with 12 mm shaft; use FS-M-006 `outputs/INTERFACE_DECISION.csv` |
| IN-018 | Hard-stop kinetic energy approximately 1.9 J | PRELIMINARY | Hard-stop concept and load-path screening; conditions must be verified |
| IN-019 | Estimated full-speed impact torque approximately 47.5 N·m | PRELIMINARY | Preliminary impact context only; provenance unresolved under OQ-012 |
| IN-023 | Static strength factor target 1.5 | ASSUMED | Structural calculation context; not an automatic housing design factor |
| IN-028 | Ambient conditions | UNKNOWN | SYS-REQ-090 environmental assessment |
| IN-033 | Range of motion 0° to 120-135° | PRELIMINARY | Hard-stop and clearance concept |
| IN-034 | Output-side encoder required | PRELIMINARY | Encoder mount, alignment and cable routing |
| IN-036 | Single-contact hard-stop load-sharing case governs | ASSUMED | Provisional load-path case pending validation |

The FS-M-001 register controls input statuses. Do not promote a PRELIMINARY or ASSUMED value to confirmed status within this study.

## 3. Canonical Requirements and Upstream Questions

Link to canonical requirements without redefining them:

- SYS-REQ-031: dedicated bearing pair in the joint housing.
- SYS-REQ-032: arm loads bypass gearbox and motor bearings through shaft, bearings and housing.
- SYS-REQ-034: encoder alignment under rated load, including shaft deflection.
- SYS-REQ-035: mechanical hard stops.
- SYS-REQ-036: independent replacement where practical.
- SYS-REQ-037: consistent mounting and output-shaft/flange interfaces.
- SYS-REQ-038: justified material and process for load-bearing parts.
- SYS-REQ-039: mass/envelope budgets from arm layout, TBD.
- SYS-REQ-023: joint range bounded by hard stops.
- SYS-REQ-090: indoor lab ambient range TBD.
- SYS-REQ-092: post-test integrity.
- SYS-REQ-100: A0/A1 cumulative budget limits.

Use `kritva-m/FS-M-001-integrated-actuator-system/ASSUMPTIONS_AND_OPEN_QUESTIONS.md` for ASM-001..ASM-012 and OQ-001..OQ-014. Reference the existing records by ID; do not create duplicate upstream definitions.

OQ-012 is relevant to the provenance of IN-019. SYS-REQ-014 is the canonical shock-load requirement, conditional on impacts being in scope (upstream OQ-009). SYS-REQ-092 concerns post-loaded-cycle-test integrity; do not classify it as a shock-load requirement.

## 4. FS-M-003 Motor Dependencies

Upstream study: `kritva-m/FS-M-003-motor-selection-sizing/`.

Required data:

- Exact candidate identity and source revision.
- Motor envelope, mass, mounting face/pilot, shaft interface and fastening.
- Torque-speed operating points and relevant operating speed.
- Thermal losses, cooling needs and allowable operating temperature where documented.
- Electrical/encoder connectors, cable exit direction, service access and routing constraints.

Use the actual motor candidate data and operating points. If these are not yet available, use placeholder CAD components only when clearly labelled, and mark affected clearances, mass and thermal conclusions provisional.

## 5. FS-M-004 Gearbox Dependencies

Upstream study: `kritva-m/FS-M-004-gearbox-selection-ratio-optimization/`.

Verify these exact outputs and their revisions:

| Artifact | Integration use |
|---|---|
| `outputs/GEARBOX_CANDIDATE_MATRIX.csv` | Candidate dimensions, mass and model identity |
| `outputs/RATIO_OPTIMIZATION.csv` | Provisional ratio/motor combination |
| `outputs/LOAD_RATING_CHECK.csv` | Permitted gearbox load conditions |
| `outputs/INTERFACE_COMPATIBILITY.csv` | Mounting, shaft/flange and torque-transfer interface |
| `outputs/LIFE_RATING_ASSESSMENT.csv` | Life and operating limitations |

Use manufacturer drawings for actual geometry. Do not invent a pilot diameter, bolt pattern, shaft dimension or mass from a gearbox family name. Keep gearbox torque reaction distinct from the arm-load path.

## 6. FS-M-005 Shaft Dependencies

Upstream study: `kritva-m/FS-M-005-output-shaft-feasibility/`.

| Artifact | Integration use |
|---|---|
| `outputs/SHAFT_LOAD_CASES.csv` | Load cases and support assumptions |
| `outputs/SHAFT_STRENGTH_CHECK.csv` | Critical shaft sections and strength constraints |
| `outputs/IMPACT_CHECK.csv` | Hard-stop/impact analysis and unresolved limits |
| `outputs/DEFLECTION_CHECK.csv` | Shaft deflection, slope and encoder alignment |
| `outputs/INTERFACE_CHECK.csv` | Shaft, bearing and gearbox interface constraints |
| `outputs/MATERIAL_COMPARISON.csv` | Shaft material/process context |

Verify source revisions and review status. Coordinate shaft shoulders, bearing spacing, encoder position and hard-stop features with FS-M-005. Shaft deflection alone does not establish total encoder alignment; housing and bearing support deformation may also matter.

## 7. FS-M-006 Bearing Dependencies

Upstream/peer study: `kritva-m/FS-M-006-bearing-support-feasibility/`.

| Artifact | Integration use |
|---|---|
| `outputs/BEARING_LOAD_CASES.csv` | Reactions and bearing support assumptions |
| `outputs/BEARING_CANDIDATE_MATRIX.csv` | Candidate dimensions and configuration |
| `outputs/BEARING_RATING_CHECK.csv` | Candidate load-rating checks |
| `outputs/LIFE_ASSESSMENT.csv` | Life-method status and limitations |
| `outputs/IMPACT_BEARING_CHECK.csv` | Stop-impact bearing checks |
| `outputs/INTERFACE_DECISION.csv` | Authoritative handoff for IN-015/IN-016 mismatch |
| `outputs/SUPPORT_FEASIBILITY.csv` | Support geometry and constraints |

Use the recorded `INTERFACE_DECISION.csv` disposition. Do not silently change IN-015 or IN-016. Confirm bearing dimensions and load-bearing housing-seat requirements before treating the CAD interface as resolved.

## 8. Mass, Envelope and Budget Inputs

Mass and envelope budgets remain UNKNOWN under SYS-REQ-039 and the applicable upstream open-question mapping. IN-039 is a ratio/motor-speed estimate and must not be used as a mass or envelope source.

Required when available:

- Approved humanoid arm/joint layout envelope and mounting datum.
- Allowable actuator mass and allocation method.
- Component masses from exact candidate datasheets or measured components.
- CAD-derived housing volume/mass using an identified material and density source.
- A0 budget: INR 10-15k.
- A1 cumulative budget: INR 20-30k.

Budget compliance requires a defined bill of materials, scope and current cost evidence. A concept mass estimate based on assumed geometry or material density must be labelled provisional.

## 9. Section A - Study-Local Inputs

Initial status is `UNKNOWN` unless evidence is available. Each candidate or interface may need its own source-linked record.

| ID | Input | Units / format | Initial status | Required evidence / handling |
|---|---|---|---|---|
| FS7-IN-001 | Assembly architecture and datum scheme | Drawing/CAD revision | UNKNOWN | Explicit reference datums and load path |
| FS7-IN-002 | Motor mounting geometry | mm, drawing revision | UNKNOWN | FS-M-003 exact-candidate documentation |
| FS7-IN-003 | Gearbox mounting and output interface | mm, drawing revision | UNKNOWN | FS-M-004 exact-candidate documentation |
| FS7-IN-004 | Shaft/bearing support geometry | mm, drawing revision | UNKNOWN | FS-M-005/006 coordinated interface |
| FS7-IN-005 | Housing material and process | Text | UNKNOWN | Material/process evidence and structural rationale |
| FS7-IN-006 | Housing-seat stiffness and deformation | mm, degrees, calculation | UNKNOWN | Hand estimate; FEA only if justified |
| FS7-IN-007 | Fastener types and load assumptions | Text, N, N·m | UNKNOWN | Verified geometry, material and calculation |
| FS7-IN-008 | Hard-stop contact geometry and travel | Degrees, mm, drawing | UNKNOWN | IN-033, SYS-REQ-023 and load-case evidence |
| FS7-IN-009 | Stop-load path and housing reactions | N, N·m | UNKNOWN | FS-M-005/006 load outputs and impact review |
| FS7-IN-010 | Encoder mounting datum and alignment limits | mm, degrees | UNKNOWN | SYS-REQ-034 and encoder manufacturer data |
| FS7-IN-011 | Cable routing and connector clearances | CAD/text | UNKNOWN | Motor/encoder candidate data and service access |
| FS7-IN-012 | Assembly/disassembly sequence | Steps/CAD | UNKNOWN | Component replacement and tool-access review |
| FS7-IN-013 | Tolerance stack-up | mm, degrees | UNKNOWN | Drawing tolerances and assembly datum scheme |
| FS7-IN-014 | Thread/insert retention in printed features | N, N·m, geometry | UNKNOWN | Manufacturer data and justified calculation |
| FS7-IN-015 | Thermal path from motor to housing | W, °C, geometry | UNKNOWN | FS-M-003/008 inputs and material data |
| FS7-IN-016 | Housing and assembly mass | kg | UNKNOWN | CAD geometry, source-backed density and component masses |
| FS7-IN-017 | Allowed envelope and mounting interface | mm, CAD | UNKNOWN | Approved arm-layout definition; otherwise UNKNOWN |
| FS7-IN-018 | Allowed actuator mass | kg | UNKNOWN | Approved SYS-REQ-039 allocation; otherwise UNKNOWN |
| FS7-IN-019 | A0/A1 bill of materials and cost basis | INR, dated source | UNKNOWN | Dated quotes/listings and explicit scope |
| FS7-IN-020 | Manufacturing process and India sourcing | Text, supplier evidence | UNKNOWN | Process capability and sourced availability |
| FS7-IN-021 | Inspection datums and critical tolerances | Drawing/tolerances | UNKNOWN | Encoder, shaft and bearing alignment requirements |
| FS7-IN-022 | Pinch-point and guarding review | Text/CAD | UNKNOWN | Identified hazards and appropriate safety review |
| FS7-IN-023 | CAD model revision and interference status | File path, commit | UNKNOWN | Reproducible model and documented check scope |
| FS7-IN-024 | Post-test integrity criteria and evidence plan | Requirement/test reference | UNKNOWN | SYS-REQ-092; do not invent pass thresholds |
| FS7-IN-025 | Independent review record | Reviewer, date, commit | UNKNOWN | Project Lead review of strength and stop-load conclusions |

Add new inputs with unused `FS7-IN-nnn` IDs when needed. Do not reuse an ID or treat a placeholder as a verified dimension.

## 10. CAD and Calculation Conventions

The mandatory CAD model must show the assembly envelope, principal interfaces, bearing supports, motor/gearbox mounts, output flange, encoder mount, hard-stop travel and cable/service clearances to the extent data are available. Clearly mark concept geometry, assumed dimensions and unverified interfaces.

Record CAD revision, units, source drawing revisions and the scope of interference checks. CAD fit is not proof of structural adequacy. Record hand-estimate assumptions and load cases in calculation files; every material property and numerical claim must have a source-register entry or be explicitly marked assumed.

## 11. Input Change Control

Change upstream values only in their authoritative source and preserve revision history. Re-run affected CAD checks and calculations when shaft, bearing, gearbox, motor, encoder, hard-stop or mounting geometry changes. Record impacts on FS-M-008, FS-M-009 and FS-M-010.

## 12. Input Completeness Gate

Before claiming integration feasibility, confirm:

- Required upstream outputs and revisions are verified.
- Motor, gearbox, shaft and bearing interfaces are sourced or explicitly provisional.
- The arm-load path bypasses gearbox and motor bearings.
- Hard-stop geometry and load path are assessed against applicable load cases.
- Encoder alignment includes shaft and housing/bearing support deformation.
- Load-bearing materials and processes are justified or remain open.
- CAD interference, assembly and service access have been checked.
- Mass/envelope and budget status reflect approved data, not invented values.
- Mandatory calculations, outputs and source register are reproducible.

Unresolved safety-critical inputs must remain `BLOCKED`, `PROVISIONAL` or `NOT_VERIFIED`.
