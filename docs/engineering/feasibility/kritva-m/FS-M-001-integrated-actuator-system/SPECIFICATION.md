---
study_id: FS-M-001
title: "Integrated Actuator System Feasibility"
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Project Lead; Independent Reviewer TBD for safety-critical shaft, bearing and stop checks
---

# FS-M-001 — Integrated Actuator System Feasibility

## 1. Purpose

Establish whether a commercially sourced motor and planetary gearbox, combined with an independent output shaft, dedicated bearing pair, output-side encoder, housing and mechanical stops, can form a feasible Kritva-M elbow actuator architecture against the current proposed system requirements.

This is the first integrated engineering feasibility study. It shall consolidate the existing requirements, preliminary calculations, known findings and unresolved inputs into a traceable system-level assessment.

The study is intended to establish a defensible baseline for subsequent focused studies. It is not intended to complete detailed design or release the actuator for manufacture.

## 2. Engineering question and decisions supported

### 2.1 Primary engineering question

Can a 24 V DC Kritva-M elbow actuator using a commercial BLDC/PMSM motor and commercial planetary gearbox meet the proposed output torque, speed, range-of-motion, mechanical-support, sensing, thermal and integration needs within the stated preliminary cost targets, or are requirement changes or architecture changes necessary?

### 2.2 Decisions this study must support

1. Whether the proposed integrated architecture is sufficiently plausible to proceed to focused design studies.
2. Whether the 15:1, 20:1 and 25:1 gearbox ratios merit further evaluation, with 20:1 as the first candidate rather than an approved selection.
3. Whether a commercially available motor can plausibly satisfy the torque-speed-power envelope at the candidate ratios.
4. Whether the independent shaft and bearing architecture is feasible in principle, considering known shaft-strength and bearing-interface concerns.
5. Whether mechanical-stop loads, impact energy and load paths introduce unresolved safety-critical blockers.
6. Whether the A0 budget is credible or requires an explicit budget or architecture review.
7. Which missing requirements, measurements, component data and independent reviews must be resolved before a detailed design baseline can be approved.

## 3. Background and baseline status

The canonical system requirements are maintained in `requirements/SYSTEM_REQUIREMENTS.md`, revision 0.2.

**All values in that revision are PROPOSED, not approved.** This study shall not silently convert proposed values into approved requirements.

Applicable requirement identifiers include:

- `SYS-REQ-001`: Elbow-joint application.
- `SYS-REQ-002`: Commercial BLDC/PMSM motor.
- `SYS-REQ-003`: Commercial planetary gearbox.
- `SYS-REQ-004`: Evaluate 15:1, 20:1 and 25:1 ratios; 20:1 is the first candidate.
- `SYS-REQ-010` through `SYS-REQ-014`: Load case, provisional forearm centre of mass, holding torque, duty-cycle and impact-load definition.
- `SYS-REQ-020` through `SYS-REQ-028`: Output torque, speed, range of motion, encoder, reflected inertia, backdrivability and preliminary efficiency.
- `SYS-REQ-030` through `SYS-REQ-040`: Output shaft, dedicated bearings, load-path separation, encoder alignment, stops, material justification, envelope and mass.
- `SYS-REQ-042` through `SYS-REQ-044`: Motor power, motor data and power-stage sizing.
- `SYS-REQ-055`: MCU class.
- `SYS-REQ-090` through `SYS-REQ-091`: Ambient conditions and gearbox/bearing life.
- `SYS-REQ-100`: A0 and A1 budget targets.
- `SYS-REQ-105`: Exact BOM part numbers.

The full requirement wording and acceptance status must be checked against the canonical file during execution. The list above is a navigation aid, not a replacement for the requirement source.

## 4. Scope

### 4.1 In scope

- Consolidate proposed system requirements and identify conflicts or missing acceptance conditions.
- Establish a consistent system-level load and operating-case baseline.
- Review the relationship between continuous torque, peak torque, speed, power, duty cycle and gearbox ratio.
- Assess commercial motor and planetary gearbox availability at a preliminary level.
- Review the proposed 20:1 first-candidate ratio against 15:1 and 25:1 alternatives.
- Assess the system-level shaft, bearing and mechanical-stop architecture, including known findings.
- Identify electrical, thermal, sensing, control and mechanical interfaces.
- Establish preliminary packaging, mass, manufacturability and cost constraints.
- Identify critical risks, unresolved assumptions and required independent checks.
- Produce an integrated feasibility conclusion and a prioritized follow-on work plan.

### 4.2 Out of scope

- Final motor or gearbox part-number approval.
- Final shaft, bearing, housing or stop design.
- Production-ready CAD and manufacturing drawings.
- Detailed electromagnetic motor design or custom gearbox design.
- Final FOC firmware, MCU selection or control-loop tuning.
- Complete thermal qualification over a validated duty cycle.
- Validated impact, fatigue or lifetime qualification.
- Formal functional-safety certification or safety-integrity claims.
- Production BOM release, supplier commitment or manufacturing release.
- Final proof that the proposed budget is achievable without verified quotations and a complete cost basis.

## 5. Applicable requirements

The canonical source is `requirements/SYSTEM_REQUIREMENTS.md`, revision 0.2.

| Requirement ID | Subject | Current baseline | Study treatment |
|---|---|---|---|
| SYS-REQ-001 | Application | Elbow joint | Confirm application assumptions and load path |
| SYS-REQ-002 | Motor type | Commercial BLDC/PMSM | Evaluate commercially available candidates |
| SYS-REQ-003 | Gearbox type | Commercial planetary | Evaluate commercial gearbox candidates |
| SYS-REQ-004 | Gear ratios | 15:1, 20:1, 25:1; 20:1 first candidate | Compare all three ratios |
| SYS-REQ-010 | Load case | Forearm/hand 1.5 kg; payload 1.0 kg at 350 mm; forearm CoM 180 mm | Establish load model and identify missing mass properties |
| SYS-REQ-011 | Forearm CoM | 180 mm provisional | Retain as preliminary and run sensitivity |
| SYS-REQ-012 | Gravity holding torque | Approximately 6.1 Nm from the stated masses and moment arms | Recalculate and document assumptions |
| SYS-REQ-013 | Dynamic operating case | Acceleration, duty cycle and hold duration TBD | Identify as a blocker to final thermal and dynamic acceptance |
| SYS-REQ-014 | Impact loads | Required if impacts are in scope | Define stop and impact assumptions; identify missing specification |
| SYS-REQ-020 | Continuous output torque | At least 10 Nm | Evaluate against load and operating conditions |
| SYS-REQ-021 | Peak output torque | At least 20 Nm; 25 Nm stretch target; duration/repetition/recovery TBD | Separate baseline target from stretch target and flag incomplete conditions |
| SYS-REQ-022 | Output speed | 45 RPM | Evaluate motor/gearbox operating point |
| SYS-REQ-023 | Range of motion | 0 to 120–135 degrees | Identify ambiguity and required final range |
| SYS-REQ-024 | Position sensing | Output-side encoder | Include sensing location and alignment needs |
| SYS-REQ-027 | Dynamic transmission behavior | Reflected inertia and backdrivability | Identify required data and comparison method |
| SYS-REQ-028 | Gearbox efficiency | 85% preliminary sizing assumption | Use only as a provisional assumption; assess sensitivity |
| SYS-REQ-030 | Output shaft | Independent 12 mm output shaft | Review feasibility and existing strength finding |
| SYS-REQ-031 | Bearing support | Dedicated bearing pair | Evaluate preliminary support architecture |
| SYS-REQ-032 | Load path | External loads bypass gearbox/motor bearings | Verify intended architecture and interface assumptions |
| SYS-REQ-034 | Encoder alignment | Alignment maintained under load | Identify geometry and deflection evidence needed |
| SYS-REQ-035 | Mechanical stops | Hard stops required | Review stop loading and single-contact case |
| SYS-REQ-038 | Structural material | Load-bearing material justified by calculation | Record material and strength evidence needs |
| SYS-REQ-039 | Packaging | Mass and envelope TBD | Identify as unresolved system constraints |
| SYS-REQ-040 | Supply voltage | 24 V DC | Evaluate preliminary electrical architecture |
| SYS-REQ-042 | Motor power | 75–100 W preliminary target | Check consistency with output operating point |
| SYS-REQ-043 | Motor data | Motor operating data required | Identify minimum datasheet parameters |
| SYS-REQ-044 | Power stage | Sized from motor current | Identify current, peak and thermal data needs |
| SYS-REQ-055 | Controller | MCU class TBD | Record interface and control requirements still needed |
| SYS-REQ-090 | Ambient | TBD | Identify required environmental operating range |
| SYS-REQ-091 | Life | Gearbox and bearing life requirements | Identify required life targets and rating conditions |
| SYS-REQ-100 | Budget | A0 ₹10,000–₹15,000; A1 cumulative ₹20,000–₹30,000 | Compare scope-consistent cost estimates |
| SYS-REQ-105 | BOM | Exact part numbers required | Establish candidate identification and BOM completeness criteria |

### 5.1 Requirement handling

- All listed requirements remain proposed until approved through the repository's authorized process.
- If the canonical wording differs from this table, the canonical file takes precedence and the discrepancy must be recorded.
- No requirement may be marked satisfied merely because a calculation uses its value.
- Requirements with TBD operating conditions cannot be treated as fully verified where those conditions affect the result.
- Any proposed change to a requirement must be documented as a recommendation, not silently incorporated into the baseline.

## 6. Inputs and known findings

### 6.1 Preliminary numerical baseline

| Input | Value | Status | Use and limitation |
|---|---:|---|---|
| Supply voltage | 24 V DC | PRELIMINARY | Confirm motor and power-stage compatibility |
| Forearm/hand mass | 1.5 kg | PRELIMINARY | Confirm mass scope and measurement basis |
| Forearm centre of mass | 180 mm | PRELIMINARY | Sensitivity analysis required |
| Payload mass | 1.0 kg | PRELIMINARY | Confirm payload definition |
| Payload centre distance | 350 mm | PRELIMINARY | Confirm reference axis and measurement |
| Gravity holding torque | Approximately 6.1 Nm | PRELIMINARY | Recalculate from canonical load assumptions |
| Continuous output torque target | At least 10 Nm | PROPOSED | Operating conditions remain incomplete |
| Peak output torque target | At least 20 Nm | PROPOSED | Duration, repetition and recovery remain TBD |
| Stretch peak torque | 25 Nm | PRELIMINARY | Not a verified baseline requirement |
| Output speed | 45 RPM | PROPOSED | Check simultaneous torque and speed feasibility |
| Gear ratios | 15:1, 20:1, 25:1 | PROPOSED | 20:1 is the first candidate only |
| Gearbox efficiency | 85% | ASSUMED | Sensitivity analysis required |
| Motor power | 75–100 W | PRELIMINARY | Must be checked against simultaneous operating conditions |
| Output shaft diameter | 12 mm | PROPOSED | Existing material-strength concern requires independent verification |
| Preliminary bearing arrangement | 6202 bearing on 15 mm seats | ASSUMED | Confirm bearing bore, shaft interfaces, fits, loads and arrangement compatibility |
| Arm inertia | 0.171 kg·m² | PRELIMINARY | Verify derivation and applicable configuration |
| Stop energy at 45 RPM | Approximately 1.9 J | PRELIMINARY | Verify inertia basis and speed assumptions |
| Full-speed impact torque | Approximately 47.5 Nm | PRELIMINARY | Method, impact compliance and load path require validation |
| A0 BOM upper-bound allowance | Approximately ₹22,000 | PRELIMINARY | Exceeds the proposed ₹10,000–₹15,000 A0 budget |
| A1 cumulative budget | ₹20,000–₹30,000 | PROPOSED | Clarify whether this includes A0 costs and non-recurring costs |

> Note: `PROPOSED` appears in this table because the repository's requirements revision labels its values as proposed. The standard input status labels (`APPROVED`, `PRELIMINARY`, `ASSUMED`, `UNKNOWN`, `MEASURED`) do not include `PROPOSED`; `INPUTS.md` for this study maps every `PROPOSED` value to `PRELIMINARY`.

### 6.2 Known findings to carry forward

These are previously identified findings and must be checked against the underlying calculation or source before they are treated as verified facts.

1. **Bearing interface:** A 6202 bearing has a nominal 15 mm bore. The current preliminary baseline of a 12 mm shaft and 15 mm bearing seats therefore requires a defined shoulder, stepped shaft or other documented interface. A 12 mm shaft section cannot be assumed to directly fit a 15 mm bearing bore.
2. **Shaft material:** An earlier calculation reportedly gave a safety factor of approximately 0.86 for EN8 normalised steel on a 12 mm shaft, and identified EN19/42CrMo4 quenched-and-tempered material as a candidate. The original calculation, stress assumptions, material properties and independent review must be retrieved and checked before any material conclusion is accepted.
3. **Stop loading:** The single-contact mechanical-stop case is the governing preliminary case until a balanced two-contact load path is demonstrated with credible geometry and load-sharing evidence.
4. **Impact torque:** Approximately 47.5 Nm has been estimated for a full-speed impact case. Its derivation, contact compliance, stopping distance/time, inertia and force/torque transmission assumptions require validation.
5. **Stop energy:** Approximately 1.9 J has been estimated at 45 RPM. Verify the energy calculation and the inertia basis; do not equate energy directly to a unique peak torque without a defensible stopping model.
6. **Motor/gearbox ratio:** A 20:1 ratio may require a low-Kv pancake motor. A typical high-speed 24 V BLDC candidate may require approximately 37:1 to reach a comparable operating point. These are preliminary screening observations, not universal motor-selection conclusions.
7. **Budget:** An A0 BOM upper-bound allowance of approximately ₹22,000 exceeds the proposed A0 budget of ₹10,000–₹15,000. The cost basis, included components, sourcing evidence and exclusions must be reviewed.
8. **Dynamic operating conditions:** Acceleration, duty cycle, hold duration, peak duration/repetition/recovery and ambient temperature remain unresolved. The study must not claim final thermal or lifetime feasibility without a suitable operating envelope.

### 6.3 Required input classification

For every input used in a material conclusion, record:

- Input name and value.
- Units.
- Status label.
- Source or derivation.
- Applicable operating conditions.
- Uncertainty or range.
- Affected calculations and conclusions.

Use `APPROVED`, `PRELIMINARY`, `ASSUMED`, `UNKNOWN` or `MEASURED` as appropriate. These labels describe input status and do not replace the study lifecycle or verification status.

## 7. Technical approach and work packages

### WP-01 — Requirement and baseline reconciliation

- Read `requirements/SYSTEM_REQUIREMENTS.md` revision 0.2.
- Confirm the exact wording and status of applicable requirements.
- Identify missing or conflicting operating conditions.
- Establish the initial requirement-to-evidence mapping.
- Record proposed changes separately from the existing baseline.

**Output:** Requirement and open-question summary.

### WP-02 — Integrated load and operating envelope

- Recalculate gravity holding torque from the stated mass and centre-of-mass assumptions.
- Identify applicable gravity orientations and load cases.
- Separate continuous, peak, acceleration and stop-impact cases.
- Identify missing duty-cycle and duration parameters.
- Establish which conclusions can be made with current information.

**Output:** Load-case table and calculation evidence.

### WP-03 — Motor and gearbox operating-point screening

- Evaluate 15:1, 20:1 and 25:1 ratios.
- Calculate required motor speed and torque using documented gearbox efficiency assumptions.
- Check output power against motor power claims.
- Identify candidate motor torque-speed and current data requirements.
- Check whether commercially available candidate data support the proposed operating point.

**Output:** Candidate comparison and unresolved selection constraints.

### WP-04 — Shaft, bearing and stop architecture review

- Reconcile 12 mm shaft sections with proposed 15 mm bearing seats.
- Review shaft material and strength findings.
- Review bearing load paths and the requirement to bypass motor/gearbox bearings.
- Examine single-contact and balanced-stop cases separately.
- Review the reported 47.5 Nm impact torque and 1.9 J stop energy.
- Define independent review requirements for safety-critical calculations.

**Output:** Mechanical feasibility summary, critical issues and follow-on checks.

### WP-05 — Electrical, thermal and sensing interfaces

- Identify motor voltage, current, speed, torque, efficiency and thermal data requirements.
- Check the relationship between motor power, output torque, output speed and gearbox ratio.
- Identify peak-current and power-stage implications.
- Review output encoder placement, alignment and load-related deflection concerns.
- Identify unresolved MCU, ambient-temperature and duty-cycle requirements.

**Output:** Interface and thermal-input summary.

### WP-06 — Packaging, manufacturing and cost screening

- Identify preliminary envelope and mass constraints that remain TBD.
- Establish a component-level cost estimate with exact candidate identities where available.
- Separate component cost, machining, assembly, testing, tooling and other non-recurring costs.
- Compare the A0 estimate against the proposed A0 budget.
- Identify the scope and assumptions behind the cumulative A1 budget.

**Output:** Preliminary BOM/cost estimate and manufacturing constraints.

### WP-07 — Integrated assessment and handoff

- Consolidate evidence and cross-study dependencies.
- Assess the architecture against each applicable acceptance criterion.
- Identify unresolved blockers, risks and assumptions.
- Recommend whether to proceed, rework the architecture, or obtain missing requirements and evidence.
- Prepare the next-study recommendations and review package.

**Output:** Integrated feasibility conclusion and prioritized action list.

## 8. Required deliverables

The following applicability decisions apply to FS-M-001.

| Deliverable or directory | Class | Applicability decision | Required content |
|---|---|---|---|
| `SPECIFICATION.md` | M | APPLICABLE | This controlled scope and acceptance basis |
| `WORK_PLAN.md` | M | APPLICABLE | Work packages, owners, milestones and evidence |
| `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` | M | APPLICABLE | All unresolved operating conditions, interfaces and assumptions |
| `REVIEW.md` | M | APPLICABLE | Review findings, independent-review status and decision |
| `README.md` | M | APPLICABLE | Navigation, status, results and reproduction instructions |
| `inputs/` | M | APPLICABLE | Canonical requirements reference, input inventory and source references |
| `calculations/` | C | APPLICABLE | Torque/power checks, ratio calculations, stop calculations and relevant sanity checks |
| `component_research/` | C | APPLICABLE | Commercial motor, gearbox, bearing, encoder and relevant interface evidence |
| `simulation/` | C | NOT_APPLICABLE for initial baseline unless analytical evidence is insufficient | Reconsider if impact, dynamic, thermal or other critical questions require simulation |
| `CAD/` | C | APPLICABLE | Preliminary system layout, shaft/bearing interface and stop/load-path packaging evidence; controlled 3D detail may be deferred if a documented layout is sufficient for the initial decision |
| `test_data/` | C | NOT_APPLICABLE for initial desk-based assessment | Reconsider if measurement is needed to resolve critical motor, thermal, impact or mechanical uncertainty |
| `outputs/` | M | APPLICABLE | Requirement mapping, load cases, candidate comparisons, risk register references and feasibility conclusion |
| `references/` | M | APPLICABLE | Source register and traceable source documents |
| `cost_estimate/` | C | APPLICABLE | BOM/cost estimate and cost-basis explanation |
| `CHANGELOG.md` | C | APPLICABLE if the study is revised after its initial controlled version | Record material revisions and their impact |

The initial study may use calculations, manufacturer evidence and preliminary CAD/layout artefacts without requiring physical testing or full simulation. Any conclusion dependent on missing simulation or test evidence must state the limitation and remain unverified where appropriate.

## 9. Acceptance criteria

Each criterion shall be recorded with evidence, result, status and reviewer disposition. The criteria do not approve the proposed requirements themselves.

### AC-001 — Requirement traceability

All applicable requirements are linked to the canonical requirement source and mapped to analysis, evidence, an open question or a documented non-applicability rationale.

### AC-002 — Input status and provenance

Every material input has a unit, source or derivation, status label and known limitation. No proposed value is silently represented as approved.

### AC-003 — Load-case baseline

The gravity holding torque is independently recalculated from the stated masses and moment arms. The study identifies the limitations caused by unknown acceleration, duty cycle, hold duration and impact conditions.

### AC-004 — Motor/gearbox operating-point consistency

For all three candidate ratios, the study documents the implied motor speed and torque requirements using explicit equations and efficiency assumptions. Power and torque-speed consistency are checked.

### AC-005 — Candidate evidence quality

Commercial motor and gearbox candidates are identified with source-backed operating data, or the study records that adequate evidence is unavailable. Datasheet ratings are interpreted within their conditions.

### AC-006 — Shaft and bearing interface consistency

The proposed 12 mm shaft and 15 mm bearing-seat concept is resolved at the architecture level or recorded as an open design issue. The study does not assume incompatible interfaces are acceptable.

### AC-007 — Safety-critical mechanical checks

The shaft-strength, bearing-load and mechanical-stop findings are documented with source calculations or identified as requiring rework. An independent reviewer is assigned for the applicable safety-critical checks.

### AC-008 — Stop/impact limitations

The single-contact stop case, reported impact torque and stop energy are documented with assumptions and limitations. No stop safety conclusion is accepted without a defensible load model and required independent review.

### AC-009 — Electrical and thermal input adequacy

Required motor, current, power-stage, ambient and duty-cycle data are identified. Any missing data that prevent a valid thermal conclusion remain explicit.

### AC-010 — Packaging and interface assessment

The study records the preliminary motor, gearbox, shaft, bearing, encoder and housing interfaces and identifies unresolved envelope, mass and alignment constraints.

### AC-011 — Cost feasibility assessment

The cost estimate distinguishes sourced prices from estimates, identifies currency and scope, and compares the estimated A0 BOM against the proposed A0 budget. The reported approximately ₹22,000 upper-bound allowance is investigated and its basis is recorded.

### AC-012 — Uncertainty and risk

Material uncertainties and risks are documented, including the forearm CoM, duty cycle, impact case, motor/gearbox compatibility, shaft/bearing interface and budget gap.

### AC-013 — Reproducibility

Material calculations and comparison results can be reviewed and reproduced from identified inputs, equations/scripts, tool versions and source revisions, or the missing reproducibility evidence is recorded as a blocker.

### AC-014 — Deliverable completeness

All mandatory deliverables are complete and all conditional deliverables have an explicit applicability decision. Applicable conditional deliverables are provided or the study remains incomplete.

### AC-015 — Independent review

The required independent review for safety-critical shaft, bearing and stop checks is complete before those checks can be treated as verified. Missing required review means the affected work remains `NOT_VERIFIED`.

### AC-016 — Integrated conclusion

The final conclusion states the supported feasibility category, verification status, limitations, outstanding blockers and recommended next actions. It does not claim detailed design approval or production readiness.

## 10. Dependencies

| Upstream study | Dependency | Impact on FS-M-001 |
|---|---|---|
| FS-M-002 — Load and torque analysis | Detailed load cases, dynamic assumptions and sensitivity | Feeds the integrated load baseline; detailed results may be developed in parallel and incorporated by revision |
| FS-M-003 — Motor selection and sizing | Candidate motor data and operating point | Refines motor/gearbox feasibility and cost |
| FS-M-004 — Gearbox selection and ratio optimization | Candidate gearbox ratings, efficiency and ratio comparison | Refines ratio feasibility and transmission losses |
| FS-M-005 — Output shaft feasibility | Shaft geometry, material and stress checks | Resolves the shaft-strength concern |
| FS-M-006 — Bearing and support feasibility | Bearing selection, loads, life and support arrangement | Resolves bearing and load-path concerns |
| FS-M-007 — Housing and mechanical integration | Packaging, alignment, stops and assembly | Refines the integrated mechanical architecture |
| FS-M-008 — Electrical and thermal feasibility | Current, losses, operating temperature and sensing interfaces | Refines electrical and thermal feasibility |
| FS-M-009 — Manufacturing and cost feasibility | Detailed sourcing, process and cost assumptions | Refines A0/A1 cost and manufacturability assessment |
| FS-M-010 — Integrated design trade-off | Consolidated candidate evidence and cost comparison | Uses this study as the initial system-level baseline |

FS-M-001 is the initial integration study and shall not wait for every focused study to finish before identifying current blockers. Any interim conclusion must identify which downstream results remain preliminary and must be updated when material evidence changes.

## 11. Ten-working-day plan

| Day | Planned work | Milestone / exit evidence |
|---|---|---|
| Day 1 | Read canonical requirements revision 0.2; reconcile IDs, status and scope; establish source inventory | M1: Requirement and input baseline created |
| Day 2 | Recalculate gravity holding torque; list static, dynamic and impact load cases; identify TBDs | M2: Load-case and open-question table |
| Day 3 | Calculate motor speed, torque and power implications for 15:1, 20:1 and 25:1 ratios | M3: Ratio screening calculations reviewed for units and consistency |
| Day 4 | Review motor/gearbox candidate evidence and datasheet operating conditions | M4: Preliminary component comparison and evidence gaps |
| Day 5 | Review shaft diameter, 15 mm bearing-seat interface, material finding and load path | M5: Shaft/bearing architecture issues documented |
| Day 6 | Review stop energy, reported impact torque, single-contact case and independent-review needs | M6: Stop-risk package prepared for independent review |
| Day 7 | Assess electrical/thermal inputs, motor current, encoder alignment and MCU/interface TBDs | M7: Electrical and thermal interface gap list |
| Day 8 | Prepare preliminary CAD/layout evidence and BOM/cost estimate; investigate A0 budget gap | M8: Packaging baseline and cost comparison |
| Day 9 | Consolidate risk, sensitivity, requirement mapping and preliminary conclusion | M9: Integrated draft submitted for review |
| Day 10 | Address review findings where feasible; record unresolved actions and decision; prepare focused-study handoff | M10: Review-ready study package and next-action plan |

The ten-day duration is a planning target, not permission to bypass required evidence or independent review. If a critical dependency cannot be resolved in that period, record the study as blocked, incomplete or submitted for review with explicit limitations.

## 12. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Mechanical Intern — Study Owner | Maintain the study files, perform assigned mechanical and integration analyses, document sources and assumptions, and prepare the review package |
| Embedded Intern | Provide motor electrical data analysis, current/power-stage implications, encoder interface inputs and thermal-related contributions |
| Project Lead — Reviewer | Review scope, requirement traceability, integrated architecture, prioritization and overall conclusion |
| Independent Reviewer TBD | Independently review safety-critical shaft, bearing and stop calculations and their evidence |
| Project Lead / authorized approver | Decide whether the study may proceed to the next phase, subject to required independent reviews and repository approval rules |

The study author must not approve their own safety-critical work. If the independent reviewer has not been assigned or the required review has not occurred, the affected checks remain `NOT_VERIFIED`.

## 13. Safety and risk notes

The following are mandatory review topics:

1. **Shaft strength:** Verify the 12 mm shaft calculations and material properties. The previously reported EN8 normalised safety factor of approximately 0.86 is a warning requiring confirmation, not an approved final result.
2. **Bearing interface:** Resolve the 12 mm shaft versus 15 mm bearing-seat interface. Document the actual shaft steps, fits, shoulders, retention and load path.
3. **Stop impact:** Treat the single-contact stop case as governing until balanced load sharing is demonstrated. Verify impact torque and energy assumptions.
4. **Peak torque:** The 20 Nm minimum peak target and 25 Nm stretch target lack duration, repetition and recovery requirements. Do not claim peak capability until the operating conditions are defined.
5. **Thermal performance:** The 75–100 W motor target and 85% gearbox efficiency assumption do not establish thermal feasibility without duty-cycle, loss and ambient data.
6. **Gearbox and bearing life:** Obtain the required life targets and confirm ratings under actual load and speed conditions.
7. **Budget:** The preliminary A0 cost allowance exceeds the stated budget range. The discrepancy requires explicit treatment rather than optimistic substitution of unverified prices.
8. **Motion and control:** Range of motion, hard stops, encoder alignment, reflected inertia and backdrivability must be considered together.
9. **Material and manufacturing:** Load-bearing materials and processes must be justified by the applicable calculations, material data and manufacturing assumptions.

Do not fabricate, assemble or operate a prototype on the assumption that this preliminary feasibility study establishes safe operating limits.

## 14. Feasibility conclusion and verification status

Complete this section after the evidence and review are available.

**Feasibility category:** `NOT_YET_ASSESSED`

Select one final category only when supported by the study evidence:

- `PROMISING`
- `PROMISING_WITH_CONDITIONS`
- `FEASIBILITY_NOT_ESTABLISHED`
- `POTENTIALLY_INFEASIBLE`

**Verification status:** `NOT_STARTED`

Use only the governing values:

- `NOT_STARTED`
- `IN_PROGRESS`
- `PASS`
- `PASS_WITH_ACTIONS`
- `FAIL`
- `NOT_VERIFIED`

**Current baseline assessment:**

The proposed architecture has enough definition to justify a structured feasibility investigation, but several issues remain unresolved. These include the motor/gearbox operating point, incomplete dynamic and thermal requirements, shaft/bearing interface compatibility, material-strength evidence, mechanical-stop loading and the A0 budget discrepancy.

This initial assessment is not a final feasibility decision. The study must establish which issues can be resolved from available evidence and which require a requirement decision, focused engineering study, supplier data, measurement or independent review.

## 15. What FS-M-001 must NOT conclude

This study must not:

- Declare the 20:1 gearbox ratio approved merely because it is the first candidate.
- Claim that any motor or gearbox meets the requirements without checking operating conditions and credible source data.
- Treat the 85% gearbox efficiency or 75–100 W motor target as verified component capability.
- Treat the 180 mm forearm centre of mass as approved or exact.
- Claim thermal feasibility without a defined duty cycle, hold duration, peak duration and ambient range.
- Claim that the 12 mm shaft is safe based only on a nominal diameter or unreviewed calculation.
- Claim that the 6202 bearing arrangement is compatible without resolving the 15 mm bearing-seat interface and actual shaft geometry.
- Declare the mechanical stops safe without resolving the governing single-contact case, impact assumptions and required independent review.
- Treat the reported 47.5 Nm impact torque or 1.9 J stop energy as validated without checking the underlying model.
- Declare gearbox or bearing lifetime acceptable without approved life targets and applicable rating conditions.
- Claim that the A0 budget is met while the cost basis indicates an approximately ₹22,000 upper-bound allowance against a proposed ₹10,000–₹15,000 target.
- Convert proposed system requirements into approved requirements.
- Treat a complete document set as proof of technical feasibility.
- Approve detailed design, prototype operation, production, or release.
- Mark safety-critical work verified before required independent review is complete.

## 16. Specification approval

**Specification status:** Proposed

| Approval role | Name / role | Decision | Date | Reference |
|---|---|---|---|---|
| Study owner | Mechanical Intern | Prepared for review | TBD | TBD |
| Project reviewer | Project Lead | TBD | TBD | TBD |
| Independent safety-critical reviewer | Independent Reviewer TBD | TBD | TBD | TBD |
| Authorized approver, if separately required | TBD | TBD | TBD | TBD |

The specification is not approved to start until the required approval process is completed. Safety-critical independent review remains mandatory at the applicable technical review gates even if the overall study specification is approved.
