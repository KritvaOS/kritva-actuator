---
study_id: FS-M-003
title: Motor Selection and Sizing
product: Kritva-M
priority: P1
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
contributors:
- Embedded Intern
reviewer: Project Lead; Independent Reviewer TBD for safety-critical motor peak and thermal checks
upstream_dependencies:
- FS-M-001
- FS-M-002
downstream_studies:
- FS-M-004
- FS-M-007
- FS-M-008
- FS-M-009
- FS-M-010
peer_studies:
- FS-M-004
verification_status: NOT_STARTED
feasibility_category: NOT_YET_ASSESSED
---

# FS-M-003 — Motor Selection and Sizing

## 1. Purpose

Identify and technically screen commercially available BLDC/PMSM motor candidates for the Kritva-M elbow actuator. Establish motor torque-speed, current, voltage, thermal, feedback, mass, packaging, cost, and sourcing requirements for comparison with the gearbox and downstream drive architecture.

The initial motor power range is 75–100 W, but power rating alone is not an acceptance criterion. Candidates must be evaluated for continuous torque at the required motor speed, peak torque/current capability, operation from a 24 V nominal supply, thermal limits, and compatibility with field-oriented control (FOC).

## 2. Engineering Question

Can a commercially available BLDC/PMSM motor, operated from the proposed 24 V supply and paired with a feasible gearbox ratio, satisfy the load cases from FS-M-002 while meeting current, voltage, thermal, feedback, packaging, sourcing, and cost constraints?

The study must establish a traceable candidate shortlist and identify the motor data and system decisions required before a motor can be selected.

## 3. Background and Context

The authoritative requirement source is `requirements/SYSTEM_REQUIREMENTS.md`. Applicable requirements include SYS-REQ-002, SYS-REQ-004, SYS-REQ-027, SYS-REQ-028, SYS-REQ-040, SYS-REQ-041, SYS-REQ-042, SYS-REQ-043, SYS-REQ-044, SYS-REQ-090, and SYS-REQ-105. Reference these IDs; do not duplicate their requirement text.

Upstream sources:

- FS-M-001 `inputs/INPUTS.md`, authoritative IDs IN-001..IN-039.
- FS-M-001 `ASSUMPTIONS_AND_OPEN_QUESTIONS.md`, upstream ASM-001..ASM-012 and OQ-001..OQ-014.
- FS-M-002 `outputs/LOAD_CASES.csv`, `outputs/DYNAMIC_TORQUE_RESULTS.csv`, and `outputs/REFLECTED_INERTIA.csv`, subject to their actual availability and verification status.

Informative idealized baseline from SYSTEM_REQUIREMENTS section 10, using 85% assumed gearbox efficiency:

| Gearbox ratio | Motor speed at 45 RPM output | Ideal motor torque for 10 N·m output | Ideal motor torque for 25 N·m output |
|---|---:|---:|---:|
| 15:1 | 675 RPM | 0.78 N·m | 1.96 N·m |
| 20:1 | 900 RPM | 0.59 N·m | 1.47 N·m |
| 25:1 | 1125 RPM | 0.47 N·m | 1.18 N·m |

These are preliminary estimates, not candidate ratings or verified operating points. At 10 N·m output and 45 RPM, output mechanical power is approximately 47.1 W; with the assumed 85% gearbox efficiency, the corresponding motor mechanical power is approximately 55 W before other losses and margins.

IN-039 notes that 20:1 may require a low-Kv pancake motor, while approximately 37:1 is an initial estimate for a typical high-speed BLDC. Validate both statements against actual motor data and the jointly selected gearbox.

## 4. Scope

### 4.1 In Scope

- Define motor requirements from verified or clearly provisional FS-M-002 load cases.
- Screen commercial BLDC/PMSM candidates, including frameless/pancake and standard motor forms.
- Compare torque-speed curves, continuous and peak torque, torque constant, speed constant, winding resistance, current limits, and thermal ratings.
- Check operation at 24 V nominal and identify the allowable supply range and regeneration constraints requiring confirmation.
- Evaluate back-EMF and voltage headroom at the required motor speed, including drive voltage limitations and operating margin.
- Identify current requirements for continuous/RMS operation and peak events.
- Assess demagnetisation risk, winding/drive current limits, and peak-current duration.
- Check encoder/Hall feedback compatibility with FOC.
- Compare mass, envelope, shaft/interface, cooling, availability, India sourcing, and documented pricing.
- Iterate motor candidates jointly with FS-M-004 gearbox ratios.
- Produce motor-side operating points, current estimates, and power-stage implications for FS-M-008.
- Record candidate data provenance and unresolved items.

### 4.2 Out of Scope

- Final gearbox selection and gearbox life assessment: FS-M-004.
- Final drive electronics and thermal design sign-off: FS-M-008.
- Final housing/mechanical integration: FS-M-007.
- Final procurement approval or production release.
- Controller firmware implementation and tuning.
- Physical qualification testing unless separately approved.

## 5. Requirements and Traceability

| Requirement ID | Study application | Required evidence |
|---|---|---|
| SYS-REQ-002 | Commercial BLDC/PMSM motor technology | Candidate datasheets and shortlist |
| SYS-REQ-004 | Gearbox ratio evaluation | Motor/ratio comparison for 15:1, 20:1, and 25:1 |
| SYS-REQ-027 | Reflected inertia/backdrivability context | Inertia compatibility assessment using FS-M-002 output |
| SYS-REQ-028 | Motor/drive efficiency context | Manufacturer efficiency data or documented unknown |
| SYS-REQ-040 | Nominal 24 V supply | Operating-point and voltage checks |
| SYS-REQ-041 | Supply voltage range and regeneration | Open-item tracking and drive compatibility review |
| SYS-REQ-042 | 75–100 W starting range | Power, continuous torque, speed, and peak capability assessment |
| SYS-REQ-043 | Motor constants, thermal data, voltage, and feedback for FOC | Datasheet evidence and control-interface assessment |
| SYS-REQ-044 | Power stage sized from motor current | Continuous/peak current estimates and FS-M-008 handoff |
| SYS-REQ-090 | Ambient operating conditions | Thermal-rating applicability and unresolved constraints |
| SYS-REQ-105 | Exact component part numbers | Candidate source register and traceable BOM identifiers |

Confirm current requirement wording and status in the canonical requirements file before acceptance. Do not treat the initial power range as overriding torque-speed or thermal requirements.

## 6. Inputs, Assumptions, and Constraints

### 6.1 Upstream Inputs

Use the authoritative FS-M-001 input register without changing upstream IDs.

- IN-006: continuous output torque target.
- IN-007: peak output torque targets.
- IN-008: output speed target.
- IN-009: nominal 24 V supply.
- IN-010: ratios 15:1, 20:1, 25:1.
- IN-011: initial 20:1 ratio candidate.
- IN-012: 85% gearbox efficiency, ASSUMED.
- IN-013: 75–100 W initial motor power range.
- IN-014: motor data UNKNOWN.
- IN-024: 20% motor margin, ASSUMED.
- IN-026: duty cycle UNKNOWN.
- IN-028: ambient conditions UNKNOWN.
- IN-029: supply current limit UNKNOWN.
- IN-031: peak duration/repetition UNKNOWN.
- IN-032: acceleration profile UNKNOWN.
- IN-035: reflected inertia/backdrivability UNKNOWN.
- IN-038: exact part numbers UNKNOWN.
- IN-039: preliminary motor-speed/ratio matching estimate.

Also consult applicable FS-M-002 output load cases, dynamic results, and reflected-inertia data. Preserve their statuses and do not use unverified cases as approved limits.

### 6.2 Study-Local Inputs

Record motor-specific candidate data in `inputs/INPUTS.md` using `FS3-IN-nnn`. Each candidate must reference a source document and revision. Unknown data must remain UNKNOWN; do not invent part numbers, prices, ratings, or availability.

### 6.3 Screening Constraints

- Use IN-024's 20% motor margin as a PROPOSED screening margin, subject to confirmation of the margin convention. Do not double-count margins.
- Size continuous capability using the FS-M-002 RMS/continuous load cases and actual motor torque-speed data.
- Evaluate peak torque/current against manufacturer peak duration, repetition, thermal, and demagnetisation limits.
- Confirm that the required motor speed is attainable with voltage headroom at the selected supply range.
- Treat gearbox ratio and motor selection as a joint iteration with FS-M-004.
- A motor's advertised power or stall torque alone is insufficient evidence of feasibility.

## 7. Technical Tasks and Sizing Method

### 7.1 Load-Case Reconciliation

1. Review the status and contents of FS-M-002 `LOAD_CASES.csv`, `DYNAMIC_TORQUE_RESULTS.csv`, and `REFLECTED_INERTIA.csv`.
2. Identify required continuous/RMS torque, peak torque, motor speed, acceleration, and event duration for each relevant ratio.
3. Separate accepted load cases from assumed or unverified scenarios.
4. Identify missing duty, peak-duration, ambient, and supply constraints.

### 7.2 Motor-Side Torque and Power

For a gearbox ratio $N = \omega_m/\omega_o$, an idealized motor torque estimate is:

$$T_m \approx \frac{T_o}{N\,\eta_g}$$

where $T_o$ is output torque and $\eta_g$ is gearbox efficiency. This estimate is preliminary; use a load-dependent efficiency model if available.

Motor speed is:

$$\omega_m = N\,\omega_o$$

Mechanical power at a motor operating point is:

$$P_m = T_m\,\omega_m$$

Use consistent units and actual operating points. Include other losses only where their model and location are defined.

### 7.3 Continuous/RMS Sizing

- Use FS-M-002 RMS torque and operating-cycle information.
- Convert output load cases to motor-side demand using the candidate gearbox ratio and documented efficiency assumptions.
- Apply the proposed 20% motor screening margin from IN-024 once, using a clearly documented convention.
- Compare the resulting required torque at the required speed against the manufacturer's continuous torque-speed curve and thermal rating.
- Check the continuous current corresponding to the operating point.
- If RMS duty or thermal data are missing, record the candidate as not yet verified for continuous operation.

### 7.4 Peak Torque and Current

- Use the FS-M-002 peak load cases and their duration/repetition status.
- Calculate motor-side peak torque and required current using candidate motor constants and the selected gearbox assumptions.
- Check peak current duration, recovery, winding temperature, drive current limit, and demagnetisation risk.
- Do not claim peak capability based on stall torque unless the manufacturer defines the applicable duration and conditions.
- Peak and stop-impact load cases remain subject to the independent-review status established by FS-M-002.

### 7.5 Torque Constant, Speed Constant, and Current

Use manufacturer definitions and units consistently. Where the motor constant is available, derive current using the manufacturer's torque-constant convention, accounting for whether the value is phase or line-based and whether it refers to peak or RMS quantities.

Do not mix electrical and mechanical conventions. Document the conversion used for each candidate and retain source references.

### 7.6 Voltage and Back-EMF Headroom

At the required motor speed, evaluate back-EMF using the manufacturer's speed constant or voltage model. Confirm that the available drive voltage at the specified supply range is sufficient for the required speed and torque, including winding resistance, inductive voltage, controller modulation limits, and appropriate operating margin.

SYS-REQ-041 voltage range and regeneration behaviour remain unresolved until defined. A nominal 24 V value alone is not a complete voltage-compatibility specification.

### 7.7 Thermal and Demagnetisation Assessment

For each candidate, assess:

- Continuous current and thermal rating.
- Winding resistance and copper loss.
- Manufacturer thermal limits and cooling assumptions.
- Ambient-temperature applicability under SYS-REQ-090.
- Peak current and duration restrictions.
- Demagnetisation risk at high current and temperature.
- Required heat transfer path and integration constraints.

Do not infer continuous capability from a short-duration test or a peak-current rating.

### 7.8 Feedback and FOC Compatibility

Document available feedback: encoder, Hall sensors, or other supported position/speed sensing. Assess resolution, electrical interface, commutation needs, mounting, and compatibility with the intended FOC control scheme.

Unknown feedback or thermal data must remain an explicit candidate limitation.

### 7.9 Candidate and Gearbox Iteration

Compare candidates at 15:1, 20:1, and 25:1, coordinating with FS-M-004. Record motor speed, required motor torque/current, continuous and peak capability, voltage headroom, inertia implications, package, cost, and source quality.

Do not lock a motor independently of the gearbox study when ratio changes materially affect speed, torque, current, or package feasibility.

## 8. Evidence and Verification

Required evidence includes:

- Manufacturer datasheet, revision, URL or source file, and date accessed.
- Torque-speed curve or tabulated operating data.
- Torque constant/speed constant definitions and units.
- Winding resistance and continuous/peak current data.
- Thermal ratings and cooling conditions.
- Voltage/back-EMF evidence at required speeds.
- Feedback and FOC compatibility information.
- Mass, envelope, interface drawings, and mounting constraints.
- Exact manufacturer part number and price/source evidence when available.
- Calculation files for all candidate operating points.
- Candidate comparison output and recorded data gaps.
- Review comments and dispositions.

Each candidate datum must be labelled `VERIFIED_FROM_DATASHEET`, `CALCULATED`, `ASSUMED`, or `UNKNOWN` (study-local labels for candidate data; they do not replace the standard input status labels). Do not claim verification when a source does not support the relevant condition.

## 9. Deliverables

### 9.1 Mandatory

| Deliverable | Applicability and minimum content |
|---|---|
| `SPECIFICATION.md` | Study scope, requirements, methods, criteria, and limitations |
| `WORK_PLAN.md` | Work packages, schedule, gates, risks, and status |
| `inputs/INPUTS.md` | Study-local input register and upstream input index |
| `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` | Study-local assumptions and open questions; upstream records referenced by ID |
| `calculations/` | Torque, current, speed, power, voltage, and thermal screening calculations |
| `outputs/` | Machine-readable candidate screening and operating-point results |
| `component_research/` | Candidate shortlist and evidence summaries |
| `references/SOURCE_REGISTER.csv` | Traceable source register for datasheets, drawings, quotations, and other candidate evidence |
| `README.md` | File index, instructions, candidate status, and known limitations |
| `REVIEW.md` | Review findings, disposition, and evidence references |

### 9.2 Conditional

- `simulation/`: CONDITIONAL if motor/drive, thermal, or dynamic simulation is performed. Document the model, source data, and verification.
- `cost_estimate/`: CONDITIONAL if candidate pricing or a comparative BOM is developed. Record currency, date, supplier, quantity, tax/shipping assumptions, and exclusions.

### 9.3 Not Applicable to Initial Desk-Based Study

- `test_data/`: `NOT_APPLICABLE` unless physical motor testing is separately approved. If tests occur, preserve raw data, setup, instrumentation, calibration, operating conditions, and analysis.

Do not create empty directories to imply that evidence exists. State conditional and not-applicable decisions in `README.md`.

## 10. Acceptance Criteria

| Criterion ID | Acceptance criterion | Required evidence |
|---|---|---|
| AC-001 | Applicable requirements and FS-M-001/FS-M-002 inputs are reconciled. | Traceability table and source revisions |
| AC-002 | Motor-side speed and torque calculations are reproducible for 15:1, 20:1, and 25:1. | Calculation sheets and ratio comparison |
| AC-003 | Commercial candidate shortlist uses traceable sources and exact part numbers where available. | `component_research/` and `SOURCE_REGISTER.csv` |
| AC-004 | Continuous torque is checked against the relevant speed and RMS load case. | Torque-speed comparison and duty assumptions |
| AC-005 | Peak torque/current and duration limitations are evaluated. | Peak calculations and manufacturer ratings |
| AC-006 | Torque constant, speed constant, and current conventions are documented. | Datasheet extracts/references and calculation method |
| AC-007 | Required current is estimated for continuous and peak operation. | Current calculations and units |
| AC-008 | Voltage/back-EMF headroom is assessed at required motor speed. | Voltage calculations and drive assumptions |
| AC-009 | Thermal capability is assessed or explicitly left unverified due to missing data. | Thermal ratings, conditions, and gap record |
| AC-010 | Demagnetisation and peak-current limits are considered. | Manufacturer limits and assessment notes |
| AC-011 | Feedback and FOC compatibility are evaluated. | Encoder/Hall data and interface assessment |
| AC-012 | Motor and gearbox ratio are jointly compared. | Candidate/ratio matrix and FS-M-004 interface record |
| AC-013 | Mass, envelope, price, availability, and India sourcing are recorded where evidence exists. | Candidate table and source references |
| AC-014 | Power-stage current implications are handed to FS-M-008. | Continuous/peak current envelope and caveats |
| AC-015 | Mandatory calculations, outputs, component research, and source register are complete and traceable. | Repository artifacts and README |
| AC-016 | Conclusions respect uncertainty and do not overstate feasibility. | `REVIEW.md`, open questions, and disposition |

## 11. Dependencies and Interfaces

### 11.1 Upstream

- **FS-M-001:** Integrated architecture and authoritative IN-001..IN-039 input register.
- **FS-M-002:** Output load cases, dynamic/RMS results, and reflected-inertia outputs. Confirm actual file status and independent-review status before using results as accepted constraints.

### 11.2 Peer Iteration

**FS-M-004 — Gearbox Selection and Ratio Optimization.** Motor and gearbox selection must be iterated jointly. Share candidate speed/torque operating points, efficiency assumptions, package constraints, peak ratings, and inertia considerations. Record changes when ratio selection alters motor feasibility.

### 11.3 Downstream Handoff

| Study | Required handoff |
|---|---|
| FS-M-004 | Candidate motor speed/torque/current envelope, package constraints, and ratio-dependent findings |
| FS-M-007 | Motor envelope, mass, mounting interfaces, shaft/interface constraints, and cooling needs |
| FS-M-008 | Continuous/peak current, voltage/back-EMF, winding resistance, feedback interfaces, and thermal data |
| FS-M-009 | Exact part numbers, sourcing evidence, quotations, and cost limitations |
| FS-M-010 | Candidate/ratio comparison, constraints, uncertainties, and evidence quality |

Provisional data must be labelled and must not be represented as approved component limits.

## 12. Risks and Limitations

| Risk ID | Risk | Mitigation |
|---|---|---|
| R-001 | Power rating is used instead of torque-speed capability. | Require torque-speed checks at actual operating points. |
| R-002 | Continuous duty or thermal data are unavailable. | Keep continuous feasibility unverified until supported. |
| R-003 | Peak duration/repetition are undefined. | Track upstream OQ-003 and IN-031; do not claim peak feasibility. |
| R-004 | 24 V supply range or regeneration constraints are unresolved. | Track SYS-REQ-041 and request system definition. |
| R-005 | Motor constants use incompatible conventions. | Document phase/line, RMS/peak, and unit conventions. |
| R-006 | Back-EMF leaves inadequate voltage headroom. | Evaluate voltage at the selected speed and supply range. |
| R-007 | Motor/gearbox ratio mismatch. | Iterate with FS-M-004 rather than choosing independently. |
| R-008 | Candidate part number or source is unverifiable. | Require source-register evidence and retain UNKNOWN fields. |
| R-009 | Motor/drive peak current exceeds component limits. | Compare motor and drive limits for duration and thermal conditions. |
| R-010 | Ambient/cooling conditions are unknown. | Record the gap against SYS-REQ-090 and avoid thermal sign-off. |

## 13. Schedule and Milestones

Planned duration: 10 working days, coordinated with FS-M-004.

| Day | Activity | Expected output |
|---|---|---|
| Day 1 | Reconcile requirements and FS-M-002 load cases | Controlled sizing baseline |
| Day 2 | Define sizing equations and ratio operating points | Calculation framework |
| Day 3 | Research commercial BLDC/PMSM candidates | Initial shortlist and source register |
| Day 4 | Evaluate continuous torque-speed and power | Continuous candidate screening |
| Day 5 | Evaluate peak torque/current and duration limits | Peak screening |
| Day 6 | Check voltage, back-EMF, current, and FOC feedback | Electrical compatibility assessment |
| Day 7 | Evaluate thermal, mass, envelope, and sourcing data | Candidate comparison update |
| Day 8 | Iterate motor candidates with FS-M-004 | Joint motor/gearbox matrix |
| Day 9 | Prepare FS-M-008/007/009/010 handoff and review | Handoff package and review findings |
| Day 10 | Resolve findings and record disposition | Submission package |

## 14. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| Mechanical Intern — Owner | Load reconciliation, motor sizing, candidate research, calculations, and documentation |
| Embedded Intern | Current/voltage constraints, FOC feedback, drive compatibility, regeneration, and thermal/electrical interface input |
| Project Lead — Reviewer | Review methods, assumptions, candidate evidence, and study disposition |
| Independent Reviewer (TBD) | Independent review of safety-critical motor peak-torque, current and thermal conclusions; without it those results stay NOT_VERIFIED |
| FS-M-004 owner | Joint gearbox ratio iteration and interface feedback |
| FS-M-008 owner | Consume current, voltage, feedback, and thermal handoff |
| FS-M-007 owner | Consume package, mass, mounting, and cooling constraints |
| FS-M-009 owner | Consume part numbers and sourcing/cost evidence |
| FS-M-010 owner | Consume candidate/ratio trade-off results |

## 15. Safety and Review

- Do not exceed manufacturer continuous or peak current, voltage, temperature, or demagnetisation limits.
- Do not assume a motor can provide stall torque continuously.
- Review peak operating points against the upstream FS-M-002 review status.
- Record all source revisions and calculation assumptions.
- Escalate unresolved supply, regeneration, and thermal requirements before accepting the candidate.
- A motor candidate passing desk-based screening is not proof of integrated actuator safety or validated operation.
- The author cannot approve their own safety-critical work; where peak load cases feed this study, their independent-review status from FS-M-002 applies.

## 16. Conclusion and Feasibility Disposition

### 16.1 Initial Status

- Verification status: `NOT_STARTED`
- Lifecycle: `PROPOSED`
- Feasibility category: `NOT_YET_ASSESSED`
- Candidate selection: Not yet established
- Final motor/gearbox pairing: Pending joint iteration with FS-M-004

### 16.2 Must NOT Conclude

This study must not conclude:

- That a 75–100 W nameplate rating alone proves suitability.
- That the motor meets continuous torque without checking its torque-speed curve, RMS load, duty cycle, and thermal conditions.
- That peak torque is feasible without current, duration, repetition, recovery, and demagnetisation checks.
- That 24 V nominal guarantees sufficient voltage headroom at the required motor speed.
- That assumed gearbox efficiency or ideal calculations are verified component performance.
- That a candidate is available or priced in India without traceable evidence.
- That FOC compatibility is established without feedback, motor-constant, and drive-interface data.
- That a motor can be finalized independently of the gearbox ratio.
- That missing motor constants, thermal data, or part numbers can be filled with guessed values.
- That desk-based candidate screening establishes production readiness, safety, or validated performance.

## 17. Definition of Done and Approval

### 17.1 Definition of Done

- [ ] Requirements and FS-M-001/FS-M-002 inputs reconciled.
- [ ] Ratio-dependent motor speed and torque calculations completed.
- [ ] Candidate shortlist and source register completed.
- [ ] Continuous torque and RMS cases assessed.
- [ ] Peak torque/current and duration limitations assessed.
- [ ] Voltage/back-EMF headroom assessed.
- [ ] Thermal and demagnetisation constraints reviewed.
- [ ] Feedback/FOC compatibility reviewed.
- [ ] Joint motor/gearbox iteration recorded.
- [ ] Required current/voltage/thermal handoff to FS-M-008 completed.
- [ ] Mass/envelope and sourcing evidence recorded where available.
- [ ] Mandatory deliverables and acceptance-criteria evidence completed.
- [ ] Review findings, open questions, and final disposition recorded.

### 17.2 Approval Record

| Field | Value |
|---|---|
| Study owner | Mechanical Intern |
| Embedded input | Embedded Intern |
| Reviewer | Project Lead; Independent Reviewer TBD for safety-critical motor peak and thermal checks |
| Review decision | PENDING |
| Review evidence | TBD |
| Approval date | TBD |
| Accepted lifecycle status | TBD |
| Outstanding blockers | Load/duty inputs, peak duration/repetition, voltage range/regeneration, candidate-specific data, thermal conditions, and joint gearbox decision |

Do not populate approval fields until the review and decision have actually occurred.
