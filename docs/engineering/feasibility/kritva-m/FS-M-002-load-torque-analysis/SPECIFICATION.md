---
study_id: FS-M-002
title: Load and Torque Analysis
product: Kritva-M
priority: P1
version: 0.2
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Independent Reviewer TBD
independent_review_required:
- stop-impact load cases
- peak-load cases
upstream_dependencies:
- FS-M-001
downstream_studies:
- FS-M-003
- FS-M-004
- FS-M-005
- FS-M-006
- FS-M-010
canonical_requirements: requirements/SYSTEM_REQUIREMENTS.md
upstream_inputs: ../FS-M-001-integrated-actuator-system/inputs/INPUTS.md
upstream_assumptions: ../FS-M-001-integrated-actuator-system/ASSUMPTIONS_AND_OPEN_QUESTIONS.md
verification_status: NOT_STARTED
feasibility_category: NOT_YET_ASSESSED
---

# FS-M-002 — Load and Torque Analysis

## 1. Purpose

Establish a traceable mechanical load and torque baseline for the Kritva-M elbow actuator. Calculate static gravity torque, dynamic torque, continuous/RMS demand, peak loads, stop-impact cases, and reflected inertia. Deliver consistent output load cases to FS-M-003, FS-M-004, FS-M-005, FS-M-006, and FS-M-010.

All proposed requirements and preliminary values remain preliminary until verified or formally approved. This study does not constitute design release or safety sign-off.

## 2. Engineering Question

What output torque and associated mechanical loads must the Kritva-M elbow actuator withstand across its proposed operating range, motion profiles, duty cycles, and stop-impact scenarios, and what uncertainties prevent a defensible feasibility conclusion?

The study must distinguish calculated results, assumed scenarios, unverified source estimates, and approved requirements.

## 3. Background and Context

FS-M-001 establishes the integrated actuator concept and records the provisional inputs and unresolved questions. FS-M-002 uses those inputs to calculate a traceable load envelope for downstream component selection.

The authoritative requirement source is `requirements/SYSTEM_REQUIREMENTS.md`. Reference applicable requirements by ID; do not duplicate their requirement text here.

The upstream input source is `../FS-M-001-integrated-actuator-system/inputs/INPUTS.md`. Its authoritative IDs are IN-001 through IN-039. Use these IDs unchanged when referencing upstream inputs.

Relevant upstream open questions include OQ-001 (centre of mass), OQ-002 (duty, acceleration, and holding), OQ-003 (peak duration, repetition, and recovery), OQ-009 (shock loads), and OQ-012 (provenance of impact torque and reported strength factor). Relevant assumptions include ASM-001..ASM-012. Consult the upstream register for current wording and status rather than duplicating or redefining those records.

## 4. Scope

### 4.1 In Scope

1. Reconcile canonical requirements and FS-M-001 input IDs, values, units, and statuses.
2. Establish the joint-angle reference, coordinate system, and torque sign convention.
3. Calculate static gravity torque over the full provisional 0–135° range.
4. Evaluate forearm/hand CoM sensitivity using an explicitly ASSUMED ±20 mm range.
5. Evaluate payload-position sensitivity using a documented, explicitly ASSUMED range.
6. Calculate dynamic torque for defined acceleration and deceleration profiles.
7. Evaluate continuous and RMS torque for defined operating cycles.
8. Define peak torque cases and document limitations caused by unresolved peak duration, repetition, and recovery.
9. Assess hard-stop and impact loads, including the provisional single-contact governing case.
10. Calculate reflected inertia for gearbox ratios 15:1, 20:1, and 25:1.
11. Publish machine-readable load cases and traceable downstream handoff data.
12. Identify unresolved inputs, uncertainty, risks, and independent-review requirements.

### 4.2 Out of Scope

- Final motor selection and motor sizing: FS-M-003.
- Final gearbox selection and ratio optimization: FS-M-004.
- Final shaft sizing and material approval: FS-M-005.
- Final bearing selection and life assessment: FS-M-006.
- Detailed housing design, production release, and complete actuator safety certification.
- Physical validation testing in the initial desk-based study unless separately authorized.

## 5. Requirements and Traceability

| Requirement ID | Application in this study | Required evidence |
|---|---|---|
| SYS-REQ-010 | Define the proposed load case. | Mass/geometry table and torque calculations. |
| SYS-REQ-011 | Establish the provisional forearm/hand CoM. | Input traceability and sensitivity results. |
| SYS-REQ-012 | Recalculate the provisional gravity-torque estimate. | Reproducible derivation and discrepancy analysis. |
| SYS-REQ-013 | Address acceleration, duty cycle, and holding requirements. | Motion-profile calculations and open-input record. |
| SYS-REQ-014 | Address shock loads where impacts are in scope. | Impact cases, assumptions, and independent review. |
| SYS-REQ-020 | Assess the continuous output-torque target. | Static/dynamic load envelope and continuous comparison. |
| SYS-REQ-021 | Assess peak output-torque targets. | Peak-case register, duration/repetition limitations, and review. |
| SYS-REQ-022 | Relate the output speed target to load cases. | Speed and acceleration profile definitions. |
| SYS-REQ-023 | Cover the proposed joint range. | Angle sweep over 0–135°. |
| SYS-REQ-027 | Evaluate reflected inertia and relevant drivetrain implications. | Ratio-specific inertia calculations and conventions. |

Confirm the exact wording and current status of these requirements in the canonical file before execution. Requirement IDs are references, not copies or substitutes for the source.

## 6. Inputs, Assumptions, and Constraints

### 6.1 Authoritative Upstream Inputs

The following IDs must be used exactly as defined in FS-M-001 `inputs/INPUTS.md`.

| Input ID | Parameter | Value or status | Use in FS-M-002 |
|---|---|---|---|
| IN-001 | Forearm and hand mass | 1.5 kg, PRELIMINARY | Gravity torque |
| IN-002 | Forearm/hand CoM | 180 mm, PRELIMINARY | Gravity torque and sensitivity |
| IN-003 | Payload mass | 1.0 kg, PRELIMINARY | Gravity torque |
| IN-004 | Payload centre distance | 350 mm, PRELIMINARY | Gravity torque and sensitivity |
| IN-005 | Gravity torque estimate | Approximately 6.1 N·m, PRELIMINARY | Cross-check only |
| IN-006 | Continuous output torque target | At least 10 N·m, PRELIMINARY | Continuous comparison |
| IN-007 | Peak torque targets | 20 N·m minimum / 25 N·m stretch, PRELIMINARY | Peak comparison |
| IN-008 | Output speed | 45 RPM, PRELIMINARY | Dynamic profile context |
| IN-009 | Nominal supply | 24 V DC, PRELIMINARY | Downstream motor/drive context |
| IN-010 | Gearbox ratios to evaluate | 15:1, 20:1, 25:1, PRELIMINARY | Reflected inertia |
| IN-011 | First gearbox candidate | 20:1, PRELIMINARY | Candidate comparison |
| IN-012 | Gearbox efficiency | 85%, ASSUMED | Motor-side power/torque context only |
| IN-013 | Motor power range | 75–100 W, PRELIMINARY | Downstream context |
| IN-014 | Motor data | UNKNOWN | Dynamic/drivetrain model dependency |
| IN-015 | Output shaft diameter | 12 mm, PRELIMINARY | Downstream shaft interface |
| IN-016 | Bearing arrangement | 6202 bearing on 15 mm seats; mismatch flagged; ASSUMED | Downstream interface awareness |
| IN-017 | Arm inertia | 0.171 kg·m², PRELIMINARY | Dynamic and reflected-inertia analysis; verify reference axis and included bodies |
| IN-018 | Stop energy | Approximately 1.9 J, PRELIMINARY | Impact investigation |
| IN-019 | Impact torque | Approximately 47.5 N·m, PRELIMINARY | Unverified estimate requiring source derivation |
| IN-020 | A0 BOM estimate | Approximately ₹22,000, PRELIMINARY | Context only |
| IN-021 | A0 budget | ₹10,000–₹15,000, PRELIMINARY | Context only |
| IN-022 | A1 budget | ₹20,000–₹30,000, PRELIMINARY | Context only |
| IN-023 | Static strength factor | 1.5, ASSUMED | Downstream structural assessment; not a physical torque multiplier |
| IN-024 | Motor margin | 20%, ASSUMED | Downstream component assessment |
| IN-025 | Gearbox margin | 20%, ASSUMED | Downstream component assessment |
| IN-026 | Duty cycle | UNKNOWN | RMS/continuous assessment |
| IN-027 | CoM uncertainty | UNKNOWN | Obtain evidence; use study-local sensitivity range below |
| IN-028 | Ambient conditions | UNKNOWN | Downstream thermal context |
| IN-029 | Supply current limit | UNKNOWN | Downstream motor/drive context |
| IN-030 | Required life | UNKNOWN | Downstream component assessment |
| IN-031 | Peak duration/repetition | UNKNOWN | Peak feasibility |
| IN-032 | Acceleration profile | UNKNOWN | Dynamic torque |
| IN-033 | Range of motion | 0° to 120–135°, PRELIMINARY | Angle sweep; resolve final upper limit |
| IN-034 | Output encoder | Required by upstream baseline; PRELIMINARY; confirm exact interface | Motion/control context |
| IN-035 | Reflected inertia/backdrivability | UNKNOWN | Reflected-inertia analysis and limitations |
| IN-036 | Hard-stop load-sharing assumption | Single-contact case governs, ASSUMED | Stop-impact assessment |
| IN-037 | Shaft material | EN19/42CrMo4 Q&T candidate; EN8 reported SF about 0.86; PRELIMINARY | Context for downstream structural analysis |
| IN-038 | Exact component part numbers | UNKNOWN | Downstream component studies |
| IN-039 | Ratio/motor-speed matching estimate | 20:1 may require a low-Kv pancake motor; approximately 37:1 estimated for a typical BLDC, PRELIMINARY | Ratio context; validate with actual motor data |

Do not assign a new meaning to any upstream IN ID. If an input needs to be added specifically for FS-M-002, use the study-local namespace `FS2-IN-nnn`.

### 6.2 Proposed Study-Local Inputs

Record these in the study's own `inputs/INPUTS.md` or a clearly identified study-local input table. They are not upstream FS-M-001 inputs.

| Study-local input ID | Parameter | Proposed value/treatment | Status | Validation action |
|---|---|---|---|---|
| FS2-IN-001 | Gravitational acceleration | 9.80665 m/s² | ASSUMED | Use as the calculation convention unless the project specifies otherwise. |
| FS2-IN-002 | Forearm/hand CoM sensitivity | Nominal 180 mm ±20 mm | ASSUMED | Use only for sensitivity; replace with CAD or measurement evidence when available. |
| FS2-IN-003 | Payload-position sensitivity | Propose nominal 350 mm with a documented exploratory range | ASSUMED once a range is selected | Record the range and rationale; do not present it as an approved tolerance. |
| FS2-IN-004 | Angle-sweep increment | Propose 1° increments for the initial numerical sweep | ASSUMED | Confirm that resolution captures the governing result; refine if needed. |
| FS2-IN-005 | Illustrative acceleration profiles | Not yet defined | UNKNOWN | Define explicit scenarios only if approved motion profiles are unavailable; label them illustrative. |

These proposed inputs must be added to the study-local input record with owner, source/basis, units, status, and validation action before use.

### 6.3 Calculation Constraints

- Confirm the joint-angle zero reference and torque sign convention before calculating.
- Do not assume 0° is horizontal; use the canonical/CAD convention and document any transformation. (Note: SYSTEM_REQUIREMENTS defines 0° as the fully extended elbow, and the horizontal case gives the maximum static gravity torque.)
- Confirm whether IN-017 includes the forearm, hand, payload, and other moving bodies, and confirm its reference axis.
- Keep gravity torque, inertial torque, friction/loss torque, and impact loading identifiable as separate contributions.
- Do not treat assumed acceleration or duty scenarios as proof of requirement compliance.
- Gearbox efficiency affects motor-side demand and losses; it does not change the physical external-load torque required at the output.
- Do not use IN-019 as verified until its derivation is reproduced or independently substantiated.
- Do not apply IN-023, IN-024, or IN-025 as multipliers on physical load unless a specific calculation convention explicitly justifies it.
- Record all unresolved inputs and their effect on conclusions.
- The repository already holds reference calculations (`mechanical/calculations/LOAD_CASES.md`, `TORQUE_AND_SPEED.md`, `mechanical/common-sizing/actuator_sizing.py`, `expected_results.json`; all draft, pending approval). Recalculate independently first, then compare and record any difference. Do not edit the script or expected results from this study. The repository uses g = 9.81 m/s² (about 0.03 % different from FS2-IN-001).
- Use the sign convention in `docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md` section 3 and state the upper-arm orientation (FS2-IN-010) for every gravity-torque result.

## 7. Technical Tasks and Calculation Method

### 7.1 Geometry and Coordinate Convention

Document the elbow pivot axis, centre-of-mass positions, angle zero, positive rotation, gravity direction, and torque sign convention. Reconcile the convention with CAD and the canonical range.

Use SI units internally. Convert millimetres to metres and RPM to rad/s before calculation. Identify the reference axis for each inertia.

### 7.2 Static Gravity Torque

For each mass $m_i$ at radial distance $r_i$, if its angle $\theta_i$ is measured from the downward vertical, the gravity-torque magnitude is:

$$|\tau_{g,i}| = m_i\, g\, r_i\, |\sin\theta_i|$$

The signed expression must follow the chosen coordinate convention. Total gravity torque is the sum of signed contributions:

$$\tau_g(\theta) = \sum_i \tau_{g,i}(\theta)$$

Calculate the forearm/hand and payload contributions over the full 0–135° range, with the actual geometry and angle reference explicitly defined.

Report:

- Signed and absolute torque at each sweep point.
- Governing magnitude and corresponding angle.
- Zero crossings and sign changes.
- The result compared with IN-005.
- Differences caused by geometry, angle convention, mass inclusion, or rounding.

Do not force the calculation to match IN-005.

### 7.3 CoM and Payload-Position Sensitivity

For the forearm/hand CoM, evaluate 160 mm, 180 mm, and 200 mm as an ASSUMED ±20 mm sensitivity sweep around IN-002. This is not a tolerance or approved requirement.

For payload position, define and document an exploratory range around IN-004. Record the rationale and status. If no defensible range is available, report the nominal case and identify the sensitivity as incomplete.

For each case, recalculate the gravity-torque sweep and report the effect on peak torque and its angle.

### 7.4 Dynamic Torque

Use a consistent torque balance:

$$\tau_{act}(t) = \tau_g(\theta(t)) + J_{eq}\,\alpha(t) + \tau_{friction}(t) + \tau_{external}(t)$$

where $J_{eq}$ is the equivalent inertia at the output axis and $\alpha(t)$ is angular acceleration.

The equation is an accounting framework. Do not silently set unknown friction, external loads, or drivetrain terms to zero in a final acceptance case.

If IN-032 remains UNKNOWN, define explicitly labelled illustrative acceleration/deceleration profiles only when useful and technically justified. State the assumed angular acceleration, speed, duration, and motion boundaries. Report sensitivity to profile selection and identify what approved profile is needed to close the calculation.

### 7.5 Continuous and RMS Torque

For a defined cycle with torque $\tau_k$ over duration $t_k$:

$$\tau_{RMS} = \sqrt{\frac{\sum_k \tau_k^2\, t_k}{\sum_k t_k}}$$

The cycle must represent the intended motion and holding sequence. Include gravity holding torque and defined acceleration/deceleration phases. State how friction, drivetrain losses, and external loads are handled.

Because IN-026 is UNKNOWN, do not claim that a selected illustrative cycle establishes continuous or thermal feasibility. Compare the calculated envelope with IN-006 and clearly record the remaining duty-cycle dependency.

### 7.6 Peak Torque Cases

Define cases for maximum gravity torque, acceleration/deceleration, physically consistent combined loads, and applicable external or shock loads.

Each case must identify its pose, direction, speed, acceleration, torque contributions, resultant torque, duration, repetition, recovery, assumptions, and source evidence as applicable.

Compare with IN-007 without claiming feasibility from the nominal peak number alone. IN-031 remains a blocking dependency until peak duration, repetition, and recovery are defined sufficiently for the intended assessment.

**Independent review is required for peak-load cases.** Results remain `NOT_VERIFIED` until the required independent review is recorded.

### 7.7 Stop-Impact Loading

Assess stop-impact cases separately from commanded-motion torque.

For an idealized rotational event:

$$E_k = \tfrac{1}{2} J \omega^2$$

This estimates rotational kinetic energy, not peak impact torque. Peak torque depends on contact stiffness, deformation, damping, impact duration, stop geometry, and the actual load path.

Tasks:

1. Reproduce or substantiate IN-018 from its source inertia, speed, and included masses.
2. Recover and reproduce the derivation for IN-019.
3. If the derivation is unavailable, mark the estimate unverified and document any defensible bounded scenarios.
4. Assess IN-036's single-contact assumption and its implications for force and moment transfer.
5. Document stop geometry, contact sequence, reaction forces/moments, and affected shaft, bearing, gearbox, and housing interfaces.
6. Identify additional model or test evidence needed to support the result.

**Independent review is mandatory for stop-impact assumptions, calculations, and resulting safety-critical load cases.** Do not accept or hand off an unreviewed impact result as a verified design limit.

### 7.8 Reflected Inertia

Evaluate ratios of 15:1, 20:1, and 25:1 from IN-010. Define:

$$N = \frac{\omega_{motor}}{\omega_{output}}$$

For ideal gearing, motor-side inertia reflected to the output is:

$$J_{m,ref,out} = J_m N^2$$

Output-side load inertia reflected to the motor is:

$$J_{L,ref,motor} = \frac{J_L}{N^2}$$

Identify included inertias, reference axes, gearbox internal inertia, and source data. Do not assume missing motor or gearbox inertia values are zero where they materially affect the conclusion.

Publish the ratio comparison and explicitly identify unresolved dependencies on IN-014 and IN-035.

### 7.9 Load-Case Consolidation

Produce a machine-readable load-case table with:

- Unique load-case ID.
- Requirement and input references.
- Pose, angle convention, and torque sign.
- Speed and acceleration where applicable.
- Gravity, inertial, friction/loss, external, and impact contributions as applicable.
- Resultant output torque.
- Duration, repetition, and recovery status.
- Reaction forces/moments where calculated.
- Assumption and uncertainty references.
- Verification and independent-review status.

Keep physical output loads separate from motor-side demand. Clearly label provisional cases so downstream teams cannot mistake them for approved limits.

## 8. Evidence and Verification Method

Required evidence:

- Canonical requirement and input-register revisions.
- Geometry/coordinate diagram and mass-property source.
- Reproducible calculation sheets with equations, units, and assumptions.
- Full angle-sweep results and sensitivity tables.
- Dynamic profiles, torque calculations, and operating-cycle definition.
- Peak-load case register.
- Stop-impact derivations or explicit evidence gaps.
- Reflected-inertia calculations for all three ratios.
- Machine-readable output files and downstream handoff notes.
- Review record, including independent-review evidence for peak and impact cases.

A result is not verified if it cannot be reproduced from its cited inputs and calculation method. Assumed scenarios must remain distinguishable from requirement-based results.

## 9. Deliverables

### 9.1 Mandatory

| Deliverable | Minimum content |
|---|---|
| `SPECIFICATION.md` | Controlled scope, requirements, methods, acceptance criteria, and limitations |
| `WORK_PLAN.md` | Work packages, owners, schedule, milestones, and status |
| `inputs/INPUTS.md` | Study-local inputs and traceable upstream references |
| `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` | Study-specific assumptions and unresolved questions |
| `calculations/` | Reproducible static, dynamic, RMS, peak, impact, and inertia calculations |
| `outputs/LOAD_CASES.csv` | Traceable output load cases |
| `outputs/GRAVITY_TORQUE_SWEEP.csv` | Full-angle sweep and sensitivity data |
| `outputs/DYNAMIC_TORQUE_RESULTS.csv` | Dynamic/RMS results where calculable, with profile and status |
| `outputs/REFLECTED_INERTIA.csv` | Ratio comparison and inertia references |
| `README.md` | File index, execution instructions, inputs, and limitations |
| `REVIEW.md` | Review findings, disposition, and independent-review record |

### 9.2 Conditional

- `simulation/`: CONDITIONAL if a dynamic or contact simulation is used. Document model assumptions, inputs, and verification.
- `CAD/`: CONDITIONAL if new geometry or mass-property evidence is required.
- Additional plots, impact-model files, or calculation outputs: required when needed to substantiate acceptance.

### 9.3 Not Applicable to Initial Desk-Based Baseline

- `test_data/`: `NOT_APPLICABLE` unless physical tests are separately authorized. If tests are conducted, preserve raw data, setup, calibration, operating conditions, and analysis.

Do not create empty directories to imply completed work. Record conditional and not-applicable decisions in the README and review record.

## 10. Acceptance Criteria

| Criterion ID | Acceptance criterion | Evidence | Acceptance condition |
|---|---|---|---|
| AC-001 | Requirements and upstream input IDs are reconciled. | Traceability table and source revisions | IDs and values match authoritative files; discrepancies are resolved or recorded. |
| AC-002 | Coordinate, angle, and torque sign conventions are documented. | Geometry diagram and calculation notes | Independent engineer can reproduce the interpretation. |
| AC-003 | Gravity torque is calculated across 0–135°. | `GRAVITY_TORQUE_SWEEP.csv` | Full range covered; governing magnitude and angle identified. |
| AC-004 | IN-005 is checked against the gravity calculation. | Calculation and comparison note | Agreement or discrepancy explained without forcing a match. |
| AC-005 | CoM sensitivity is evaluated at 160, 180, and 200 mm. | Sensitivity results | Cases are marked ASSUMED and impacts reported. |
| AC-006 | Payload-position sensitivity is evaluated or its incompleteness documented. | Range rationale and sensitivity results | Range is traceable and not misrepresented as an approved tolerance. |
| AC-007 | Dynamic torque is calculated for defined profiles or the limitation is documented. | Profiles and calculations | Assumed scenarios are labelled; required motion inputs are identified. |
| AC-008 | Continuous/RMS torque is assessed for a defined cycle or remains explicitly incomplete. | Cycle definition and RMS calculation | Duty assumptions and included contributions are clear. |
| AC-009 | Peak torque cases are documented. | Peak-case register | Loads and duration/repetition dependencies are stated. |
| AC-010 | Impact estimates are reproduced or explicitly left unverified. | Impact calculations and source evidence | IN-018/IN-019 provenance and limitations are clear. |
| AC-011 | Peak and stop-impact cases receive independent review. | `REVIEW.md` or designated review record | Reviewer and disposition are recorded; otherwise affected results remain `NOT_VERIFIED`. |
| AC-012 | Reflected inertia is calculated for 15:1, 20:1, and 25:1. | `REFLECTED_INERTIA.csv` | Ratio convention, reference axes, and included inertias are stated. |
| AC-013 | Downstream load cases are traceable and usable. | `LOAD_CASES.csv` and handoff notes | Required torque/load data and limitations are identified for all downstream studies. |
| AC-014 | Calculations and outputs are reproducible. | Calculation files and README | Reviewer can reproduce principal results. |
| AC-015 | Assumptions and unresolved inputs are maintained. | Assumption/open-question register | Material uncertainties have owners and validation actions. |
| AC-016 | Conclusions do not exceed the evidence. | Review record and conclusion | No unsupported feasibility, compliance, or safety claim remains. |

## 11. Dependencies and Interfaces

### 11.1 Upstream

**FS-M-001 — Integrated Actuator System Feasibility**

Use its current `inputs/INPUTS.md` and `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` as authoritative for upstream IDs and status. Confirm that FS-M-001 is complete and that the relevant values and derivations are available. Completion of FS-M-001 does not automatically mean every input is verified or approved.

### 11.2 Downstream Handoff

| Study | Handoff |
|---|---|
| FS-M-003 | Torque versus time/operating phase, continuous/RMS and peak cases, speed/acceleration assumptions, and uncertainty. |
| FS-M-004 | Output torque/speed envelope, duty information, peak/impact cases, and ratio-related inertia data. |
| FS-M-005 | Governing output torque, bending moments, impact reactions, and load combinations. |
| FS-M-006 | Relevant shaft/bearing reactions, moments, operating cycles, and impact cases. |
| FS-M-010 | Comparable load cases, sensitivity results, ratio comparison, and unresolved feasibility risks. |

Any load case handed downstream before acceptance must be explicitly labelled provisional. Missing inputs must be raised to the relevant owner, not replaced with invented values.

### 11.3 Change Control

Changes to mass, CoM, payload position, joint range, acceleration, duty cycle, peak-load definition, inertia, or stop geometry require an impact assessment.

Record the changed input, source, affected calculations and load cases, downstream studies requiring rerun, and review requirements.

## 12. Risks and Limitations

| Risk ID | Risk | Mitigation |
|---|---|---|
| R-001 | Angle convention differs from CAD or canonical requirements. | Establish and review the coordinate convention before calculations. |
| R-002 | CoM or payload location is inaccurate. | Sensitivity analysis and CAD/measurement confirmation. |
| R-003 | Acceleration and duty cycle remain unknown. | Use clearly labelled scenarios and retain limitations. |
| R-004 | Peak duration/repetition/recovery are unspecified. | Block final peak feasibility until adequately defined. |
| R-005 | Impact energy or torque provenance is missing. | Reproduce source calculations or mark unverified; independent review required. |
| R-006 | IN-017 inertia has an unclear axis or included mass. | Verify its source and reference axis. |
| R-007 | Payload sensitivity range lacks a justified basis. | Document an exploratory range and obtain agreement before relying on it. |
| R-008 | Friction/loss terms are ignored or double-counted. | Separate output load from motor-side demand and document the model. |
| R-009 | Single-contact stop assumption is not representative. | Assess the load path and obtain independent review. |
| R-010 | Preliminary values are mistaken for approved requirements. | Preserve statuses and source traceability. |
| R-011 | Downstream teams interpret loads inconsistently. | Publish controlled load-case data with units, signs, axes, and limitations. |
| R-012 | Independent reviewer is not assigned. | Project Lead to assign one before review submission. |

Update risks as new evidence becomes available.

## 13. Schedule and Milestones

Planned duration: 10 working days, dependent on input availability and independent-review scheduling.

| Day | Activity | Expected output |
|---|---|---|
| 1 | Requirements, inputs, geometry, and convention reconciliation | Reviewed baseline and open-input list |
| 2 | Static gravity torque calculation | Angle sweep and cross-check |
| 3 | CoM and payload-position sensitivity | Sensitivity results |
| 4 | Dynamic-profile definition and torque calculation | Dynamic scenarios |
| 5 | Continuous/RMS and peak-case assessment | RMS results and peak register |
| 6 | Stop-impact source review and energy calculation | Impact baseline and evidence gaps |
| 7 | Stop reactions and reflected-inertia analysis | Reaction cases and ratio comparison |
| 8 | Consolidate load cases and prepare outputs | Draft machine-readable handoff |
| 9 | Independent review of peak and impact cases | Review findings |
| 10 | Resolve findings and prepare study disposition | Submission package |

This is a plan, not evidence of completion. Blocked work must remain open and the schedule updated when required inputs or reviewers are unavailable.

## 14. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| Mechanical Intern — Owner | Perform calculations, maintain traceability, and prepare outputs. |
| Independent Reviewer — TBD | Independently review peak and stop-impact calculations and other designated safety-critical results. |
| Project Lead | Resolve requirement questions, assign reviewer, coordinate dependencies, and record decisions. |
| Embedded Intern | Provide motion/control inputs where available and coordinate downstream electrical/drive implications. |
| FS-M-003 owner | Consume torque/speed cases and identify motor-sizing gaps. |
| FS-M-004 owner | Consume output load cases and inertia data. |
| FS-M-005 owner | Consume governing shaft loads and moments. |
| FS-M-006 owner | Consume support reactions and relevant load cases. |
| FS-M-010 owner | Consume comparable load cases and sensitivity results. |

The author cannot approve their own safety-critical calculations.

## 15. Safety and Independent Review

Stop-impact and peak-load calculations are safety-critical inputs to the actuator architecture and component-sizing studies.

- Identify load paths, equations, units, input sources, and assumptions.
- Independently review peak and stop-impact cases.
- Record review comments and dispositions.
- Re-review material changes to inertia, impact energy, stop geometry, peak duration, or governing load cases.
- Mark results `NOT_VERIFIED` until mandatory independent review is completed.
- Do not infer overall actuator safety or certification from this study alone.
- Do not substitute a nominal safety factor for defining the actual load case.

## 16. Conclusion and Feasibility Disposition

### 16.1 Initial Status

- Verification status: `NOT_STARTED`
- Lifecycle: `PROPOSED`
- Feasibility category: `NOT_YET_ASSESSED`
- Independent reviewer: TBD
- Final downstream handoff: Not yet accepted

### 16.2 Conditions for Conclusion

A defensible conclusion requires traceable geometry, a complete static torque sweep, documented sensitivity analysis, sufficient dynamic/duty inputs for the claimed operating conditions, defined peak cases, reproducible or bounded impact calculations, reflected-inertia results, independent review, and controlled downstream load-case data.

Where required inputs remain unresolved, conclusions must be limited to the scenarios actually analyzed.

### 16.3 Must NOT Conclude

FS-M-002 must not conclude:

- That continuous feasibility is established merely because the gravity estimate is approximately 6.1 N·m.
- That peak feasibility is established without peak duration, repetition, recovery, and relevant component capability.
- That thermal feasibility is established without a representative duty cycle and operating conditions.
- That IN-018 or IN-019 is correct without reproducible source derivations.
- That the single-contact assumption covers every stop-contact condition.
- That IN-017 is valid for every calculation without verifying included bodies and reference axis.
- That the assumed CoM or payload sensitivity range is an approved tolerance.
- That reflected inertia is complete when material motor or gearbox inertia data are missing.
- That gearbox efficiency changes the physical output torque demanded by the external load.
- That a calculated torque below a nominal component rating proves the shaft, bearings, gearbox, housing, or stop is safe.
- That provisional load cases are approved design limits.
- That safety-critical results are accepted before required independent review.
- That the actuator is fully validated, safe for human interaction, production-ready, or externally certified based on this study alone.

## 17. Definition of Done and Approval

### 17.1 Definition of Done

- [ ] Canonical requirements and authoritative upstream input IDs are reconciled.
- [ ] Coordinate convention and geometry are documented.
- [ ] Static gravity torque is calculated across 0–135°.
- [ ] IN-005 is checked and discrepancies explained.
- [ ] CoM sensitivity at 160, 180, and 200 mm is calculated.
- [ ] Payload-position sensitivity is calculated or explicitly left incomplete.
- [ ] Dynamic cases are calculated for defined profiles or limitations are recorded.
- [ ] Continuous/RMS assessment is completed for a defined cycle or its blocking inputs are recorded.
- [ ] Peak-load cases and their duration/repetition dependencies are documented.
- [ ] IN-018 and IN-019 are reproduced or remain explicitly unverified.
- [ ] Independent review of peak and stop-impact cases is recorded.
- [ ] Reflected inertia is calculated for all three ratios.
- [ ] Mandatory calculation files and output tables are complete.
- [ ] Downstream handoff data and limitations are traceable.
- [ ] Assumptions, open questions, and risks are updated.
- [ ] `README.md` and `REVIEW.md` are complete.
- [ ] Review disposition and lifecycle status are recorded.

### 17.2 Approval Record

| Field | Value |
|---|---|
| Study owner | Mechanical Intern |
| Independent reviewer | TBD |
| Review decision | PENDING |
| Review evidence | TBD |
| Approval date | TBD |
| Accepted lifecycle status | TBD |
| Outstanding blockers | Motion/duty profile; peak duration/repetition/recovery; CoM and payload-position evidence; impact calculation provenance; independent review; other open items identified during execution |

Do not populate approval fields until the corresponding review or decision has actually occurred.
