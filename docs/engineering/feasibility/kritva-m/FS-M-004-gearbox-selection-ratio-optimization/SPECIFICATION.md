---
study_id: FS-M-004
title: Gearbox Selection and Ratio Optimization
product: Kritva-M
priority: P1
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Independent Reviewer TBD
independent_review_required:
- stop-impact and peak-load applicability
upstream_dependencies:
- FS-M-001
- FS-M-002
- FS-M-003
peer_studies:
- FS-M-003
downstream_studies:
- FS-M-005
- FS-M-006
- FS-M-007
- FS-M-008
- FS-M-009
- FS-M-010
canonical_requirements: requirements/SYSTEM_REQUIREMENTS.md
upstream_inputs: ../FS-M-001-integrated-actuator-system/inputs/INPUTS.md
verification_status: NOT_STARTED
feasibility_category: NOT_YET_ASSESSED
---

# FS-M-004 — Gearbox Selection and Ratio Optimization

## 1. Purpose

Identify and compare commercially available planetary gearboxes suitable for the Kritva-M actuator. Evaluate 15:1, 20:1 and 25:1 ratios against the motor operating envelope, output loads, efficiency, backlash, speed, life, bearing-load constraints, integration and sourcing. Treat 20:1 as the first candidate, not a frozen design. Include approximately 37:1 only as a comparison prompted by upstream IN-039.

## 2. Scope

In scope:

- Commercial planetary gearbox candidate research using manufacturer documentation.
- Ratio and stage-count comparison, including input-speed and torque limits.
- Continuous, peak and emergency-stop/impact torque survival assessment.
- Efficiency across relevant speed/load conditions; use 85% as the upstream sizing assumption until candidate-specific data supersede it.
- Backlash, position-error implications, reflected inertia, backdrivability, life, thermal/lubrication and acoustic considerations.
- Output shaft/flange, bore/keyway, independent shaft and bearing-load interfaces.
- Mass, price when verifiable, India sourcing, replaceability and a traceable source register.
- Joint iteration with FS-M-003 motor selection.

Out of scope:

- Freezing motor or gearbox part numbers.
- Final shaft, bearing, housing, fastener or actuator structural design.
- Safety certification, production qualification or life-test claims.
- Treating catalogue peak torque as automatically equivalent to emergency-stop or impact capacity.

## 3. Requirements Traceability

Link to canonical requirements; do not redefine them here.

- SYS-REQ-003: documented continuous/peak torque, efficiency, backlash, life, input speed and permitted output-load ratings.
- SYS-REQ-004: compare 15:1, 20:1 and 25:1 against motor torque-speed, efficiency, backlash, backdrivability and rated input speed.
- SYS-REQ-025: backlash/position-error limits remain TBD pending canonical resolution.
- SYS-REQ-027: reflected inertia and backdrivability.
- SYS-REQ-028: efficiency documentation across the operating range; 85% is the current sizing assumption.
- SYS-REQ-032: arm loads bypass gearbox and motor bearings unless explicitly rated for those loads.
- SYS-REQ-033: gearbox output interface preferably at least 8 mm.
- SYS-REQ-036: independently replaceable gearbox.
- SYS-REQ-091: gearbox/bearing life assessed against duty.
- SYS-REQ-090: ambient conditions.
- SYS-REQ-105: verified part numbers.

## 4. Upstream Inputs and Authority

Use the authoritative FS-M-001 `inputs/INPUTS.md` values and statuses without changing them: IN-006, IN-007, IN-008, IN-010, IN-011, IN-012, IN-013, IN-014, IN-015, IN-016, IN-025, IN-026, IN-030, IN-031, IN-035, IN-038 and IN-039 (also IN-009 and IN-019 for context). Cite input IDs in calculations and candidate comparisons. Unknown or preliminary values remain so until approved evidence changes them.

Use FS-M-002 outputs by their exact names, especially `outputs/LOAD_CASES.csv`, `outputs/DYNAMIC_TORQUE_RESULTS.csv` and `outputs/REFLECTED_INERTIA.csv` (and `outputs/GRAVITY_TORQUE_SWEEP.csv` if present). Confirm the files and their revision/commit before using them. Use FS-M-003 motor candidate data and operating points as the jointly iterated motor envelope; do not invent missing candidate data.

Reference FS-M-001 `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` by ID for upstream ASM-001..ASM-012 and OQ-001..OQ-014. Do not redefine those records. Use FS-M-002 (`FS2-`) and FS-M-003 (`FS3-`) local IDs where applicable; do not copy upstream records into this study.

## 5. Engineering Baseline

- Nominal supply: 24 V (IN-009; motor/drive implications are owned jointly with FS-M-003 and FS-M-008).
- Output speed target: 45 RPM (IN-008).
- Candidate ratios: 15:1, 20:1 and 25:1 (IN-010); 20:1 is the initial candidate (IN-011), not a design freeze.
- Gearbox efficiency: 85% sizing assumption (IN-012); replace with manufacturer data only for the applicable speed/load conditions.
- Gearbox margin: 20% assumed screening margin (IN-025). Apply transparently and avoid double-counting margins already included in upstream load or motor calculations.
- Output torque requirements and impact cases come from authoritative FS-M-001 inputs and FS-M-002 outputs, including IN-006, IN-007 and IN-019.
- IN-039 motivates a roughly 37:1 comparison only; it does not establish a preferred ratio or a viable gearbox/motor combination.

Ideal kinematic screening at 45 RPM output gives 675 RPM at 15:1, 900 RPM at 20:1, 1125 RPM at 25:1 and 1665 RPM at 37:1. These are arithmetic comparisons, not confirmation that any candidate permits the required input speed or torque. Ideal torque multiplication must not be substituted for verified catalogue ratings.

## 6. Candidate Research Method

For every candidate, record manufacturer, exact model/part number, source URL/document, revision/date, stage count, ratio, rated input speed, continuous output torque, intermittent/peak torque and its permitted duration/duty, emergency-stop or shock rating if explicitly specified, efficiency conditions, backlash, permissible radial/axial loads and tilting moment, output interface, mass, life rating basis, lubrication, operating temperature, availability, price evidence and India sourcing.

Separate manufacturer specifications, distributor claims, calculated values, assumptions and unknowns. Do not infer missing values from family-level marketing claims. Distinguish rated, intermittent, maximum, emergency and collision/impact loads. If the manufacturer does not publish a needed rating, mark it UNKNOWN and request written confirmation.

## 7. Ratio Optimization

Compare 15:1, 20:1 and 25:1 using a common set of operating points and load cases from FS-M-002 and motor candidates from FS-M-003. Add 37:1 as a non-primary comparison only. For each ratio assess:

- Input speed at target output speed and compatibility with each motor's continuous/peak torque-speed curve.
- Required motor torque and power using documented gearbox efficiency.
- Continuous/RMS, peak and emergency-stop torque capacity, including the applicable IN-025 screening margin.
- Efficiency at the relevant speed/load points, not a single unsupported nominal value.
- Backlash and positioning implications against the unresolved SYS-REQ-025 limit.
- Reflected inertia using the actual upstream `REFLECTED_INERTIA.csv` convention and data; state whether values are motor-side, output-side or otherwise referred.
- Backdrivability evidence and its limitations.
- Gearbox life and output-bearing suitability for the eventual duty profile.
- Package, interface, replacement and sourcing trade-offs.

No ratio may be selected on torque multiplication alone. Document why the preferred candidate is compatible with the motor and the system-level constraints; record unresolved evidence as a blocker.

## 8. Load Path and Interface Constraints

Assume arm bending, radial/axial forces and tilting moments are carried by a separately designed output support bearing arrangement unless the chosen gearbox manufacturer explicitly rates the gearbox output bearing for the calculated loads and duty. Do not use the motor bearings or gearbox bearings as structural supports by default.

Review the gearbox output interface against the preferred interface of at least 8 mm (SYS-REQ-033), the proposed independent 12 mm shaft (IN-015), and the 6202 bearing / 15 mm seat mismatch recorded as ASSUMED in IN-016. These are not automatically compatible. Document shaft/bore/flange dimensions, allowable fits, keyway or clamp details, axial retention, concentricity, fastening and service access. Flag any need for a custom adapter as an integration cost and risk, not as a solved interface.

## 9. Stop-Impact and Peak-Torque Assessment

Map the FS-M-002 stop-impact and peak-load cases to the manufacturer's explicitly applicable gearbox ratings. Verify torque direction, transient duration, repetition, operating speed and the manufacturer's definition of emergency or shock loading. Where only a maximum torque is published without a duration or duty definition, mark the rating applicability UNKNOWN.

The FS-M-002 impact cases require independent review. Do not conclude that a gearbox survives the estimated impact torque solely because a catalogue peak torque is numerically higher. Record the calculation, evidence and review decision separately.

## 10. Life, Lubrication and Operating Environment

Compare life ratings only after documenting the manufacturer's basis (for example operating hours, input speed, torque, load spectrum, lubrication and reliability assumptions). Upstream IN-030 life and IN-026 duty cycle are UNKNOWN; IN-031 peak duration/repetition is UNKNOWN. Do not claim an achieved service life until the duty and rating basis are reconciled.

Capture lubricant type, lubrication method, maintenance interval, allowable mounting orientation, ambient/temperature limits, thermal derating and noise/vibration data when available. SYS-REQ-090 ambient conditions remain a system constraint; unknown limits must remain open questions.

## 11. Deliverables and Repository Structure

Mandatory:

- `SPECIFICATION.md`, `WORK_PLAN.md`, `inputs/INPUTS.md`, `ASSUMPTIONS_AND_OPEN_QUESTIONS.md`, `README.md`, `REVIEW.md`.
- `calculations/`: reproducible ratio, torque, speed, efficiency, margin, inertia and life-screening calculations, with units and source IDs.
- `outputs/`: machine-readable comparison outputs, including `GEARBOX_CANDIDATE_MATRIX.csv`, `RATIO_OPTIMIZATION.csv`, `LOAD_RATING_CHECK.csv`, `INTERFACE_COMPATIBILITY.csv` and `LIFE_RATING_ASSESSMENT.csv`.
- `component_research/`: candidate datasheets, extracted evidence, manufacturer correspondence and candidate notes, with provenance.
- `references/SOURCE_REGISTER.csv`: all sources and the claims each supports.

Conditional:

- `simulation/`: only if a justified simulation is needed to answer a defined question; record assumptions, model limits and validation.
- `cost_estimate/`: when sufficiently sourced prices and integration costs are available; distinguish quoted, listed and estimated prices.

Not applicable to the initial desk-based study:

- `test_data/`: no physical test is required for the initial feasibility comparison. If later testing is authorized, create a separately scoped test record rather than implying existing test evidence.

## 12. Source and Evidence Rules

Use manufacturer datasheets, manuals, catalogues and written manufacturer confirmation as primary evidence. Distributor listings may support availability or indicative price, but must not replace missing engineering ratings. Record title, manufacturer/publisher, exact model, document revision/date, URL or local path, access date and relevant page/table/section. Preserve source files where permitted. Each numerical candidate claim must map to a source-register entry or a clearly labelled calculation.

## 13. Acceptance Criteria

| Criterion ID | Acceptance criterion |
|---|---|
| AC-001 | Upstream input IDs and their statuses are preserved and traceable. |
| AC-002 | FS-M-002 load-case outputs are located, versioned and used consistently; missing outputs are reported as blockers. |
| AC-003 | FS-M-003 motor candidates and torque-speed operating points are jointly reconciled with the gearbox comparison. |
| AC-004 | At least the 15:1, 20:1 and 25:1 ratios are compared; 37:1 is clearly labelled comparison-only. |
| AC-005 | Each candidate has a verified manufacturer and exact model/part number or is explicitly marked an unverified lead. |
| AC-006 | Continuous, peak and emergency-stop/impact torque ratings are distinguished, with duration/duty and evidence applicability documented. |
| AC-007 | Input-speed limits and required speeds are checked at the target output speed and relevant operating points. |
| AC-008 | Efficiency assumptions and sourced efficiency data are distinguished and applied consistently. |
| AC-009 | Backlash evidence and the unresolved SYS-REQ-025 limit are explicitly tracked. |
| AC-010 | Reflected inertia and backdrivability are assessed with stated data source, convention and limitations. |
| AC-011 | Permissible radial/axial loads and tilting moments are checked, or UNKNOWN; gearbox/motor bearing load-path assumptions are explicit. |
| AC-012 | Output interface compatibility is assessed against SYS-REQ-033, IN-015 and the IN-016 mismatch. |
| AC-013 | Life-rating basis, duty-cycle gaps, peak duration/repetition and lubrication/environment constraints are documented. |
| AC-014 | Mass, replaceability, sourcing and cost evidence are compared without invented part numbers or prices. |
| AC-015 | Required deliverables and `references/SOURCE_REGISTER.csv` are present, internally consistent and reproducible. |
| AC-016 | Stop-impact and peak-load conclusions receive independent review; all open blockers, deviations and the provisional recommendation are recorded without design freeze. |

## 14. Review and Approval

The Mechanical Intern prepares the study. The FS-M-003 owner provides motor-envelope input. The Project Lead checks completeness and cross-study consistency. The Independent Reviewer (TBD) reviews load-rating and stop-impact applicability. Record reviewer identity, date, evidence revision, findings, disposition and commit in `REVIEW.md`. Do not mark approval complete before the required review occurs. The author cannot approve their own safety-critical work.

## 15. Risks and Open Issues

Key risks include unavailable emergency-stop ratings, incompatible input speed/torque curves, inadequate efficiency or backlash evidence, unknown duty and life, output-bearing overload, shaft/bore mismatch, unclear peak torque duration, insufficient India availability and unsupported pricing. Track each in `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` and the project risk register as applicable. An UNKNOWN is not a pass.

## 16. Must NOT Conclude

This study must NOT conclude:

- That 20:1 is frozen or optimal before joint motor/gearbox evaluation.
- That a nominal or catalogue peak rating proves survival of stop-impact loads.
- That the 85% assumed efficiency is a verified candidate property.
- That backlash satisfies SYS-REQ-025 while its limit is TBD.
- That gearbox or motor bearings may carry arm loads without explicit ratings.
- That the proposed shaft and bearing arrangement is mechanically compatible while IN-016 remains unresolved.
- That life, backdrivability, thermal suitability or safety has been validated without supporting evidence.
- That a part number, price, stock status or Indian supplier is confirmed without a traceable source.
- That a candidate is approved for production or that the actuator is safe for human interaction.

## 17. Completion Definition

FS-M-004 is complete when AC-001..AC-016 are dispositioned with evidence, mandatory deliverables are committed, sources and calculations are reproducible, FS-M-003 iteration is documented, and independent review of impact/peak-load conclusions is recorded. The result is a feasibility recommendation with explicit residual risks, not a released design or safety approval.
