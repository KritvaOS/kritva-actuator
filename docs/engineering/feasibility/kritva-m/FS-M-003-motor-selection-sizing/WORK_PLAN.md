---
study_id: FS-M-003
title: Motor Selection and Sizing - Work Plan
product: Kritva-M
priority: P1
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
contributors:
- Embedded Intern
reviewer: Project Lead
planned_duration_working_days: 10
verification_status: NOT_STARTED
upstream_dependencies:
- FS-M-001
- FS-M-002
peer_studies:
- FS-M-004
downstream_studies:
- FS-M-004
- FS-M-007
- FS-M-008
- FS-M-009
- FS-M-010
---

# FS-M-003 Work Plan

## 1. Execution Rules

1. Follow `SPECIFICATION.md` and the canonical `requirements/SYSTEM_REQUIREMENTS.md`.
2. Use upstream IN IDs unchanged; use `FS3-IN-nnn` only for study-local inputs.
3. Use actual datasheets and traceable sources. Never invent part numbers, prices, ratings, or availability.
4. Separate measured/published data, calculated values, assumptions, and unknowns.
5. Use FS-M-002 output load cases with their verification status visible.
6. Treat the 20% motor margin from IN-024 as a proposed screening margin and apply it only once.
7. Iterate motor and gearbox selection jointly with FS-M-004.
8. Track work with `NOT_STARTED`, `IN_PROGRESS`, `BLOCKED`, or `DONE`. `DONE` requires evidence, not just task execution.
9. Do not claim continuous, peak, voltage, or thermal feasibility while required inputs remain unresolved.
10. Record evidence paths and review findings in the repository.

## 2. Work Packages

### WP-01 — Requirements and Load-Case Baseline

**Objective:** Establish traceable motor-side operating requirements.

**Tasks:**

- Reconcile SYS-REQ-002, 004, 027, 028, 040, 041, 042, 043, 044, 090, and 105 with the current canonical file.
- Review FS-M-001 inputs, especially IN-006..IN-014, IN-024, IN-026, IN-028, IN-029, IN-031, IN-032, IN-035, IN-038, and IN-039.
- Review FS-M-002 `outputs/LOAD_CASES.csv`, `outputs/DYNAMIC_TORQUE_RESULTS.csv`, and `outputs/REFLECTED_INERTIA.csv`.
- Separate accepted cases from assumed/unverified cases and record missing duty, peak, voltage, and thermal inputs.

**Inputs:** Applicable IN-001..IN-039; FS3-IN-001..FS3-IN-009; FS-M-002 outputs.

**Outputs:** Input baseline, requirement traceability, initial motor-side load table, updated open questions.

**Effort:** 1 day. **Owner:** Mechanical Intern, with Embedded Intern input.

**Done criteria:** Sources and statuses reconciled; each motor-sizing case is traceable to an upstream load case or explicitly labelled scenario.

### WP-02 — Sizing Method and Ratio Operating Points

**Objective:** Establish reproducible motor torque, speed, power, and current calculation conventions.

**Tasks:**

- Define gearbox ratio convention and efficiency treatment.
- Calculate motor speed for 15:1, 20:1, and 25:1 at required output speed.
- Calculate idealized motor torque for relevant output load cases.
- Define units and torque-constant/current conventions.
- Document the proposed IN-024 margin convention and prevent double-counting.
- Identify required candidate motor data.

**Inputs:** IN-006..IN-012, IN-024, IN-039; FS3-IN-001, FS3-IN-006.

**Outputs:** Calculation sheets and ratio operating-point table.

**Effort:** 1 day. **Owner:** Mechanical Intern.

**Done criteria:** Equations, units, assumptions, and all three ratio cases are reproducible.

### WP-03 — Commercial Candidate Research

**Objective:** Create a traceable shortlist without inventing missing specifications.

**Tasks:**

- Search commercial BLDC/PMSM frameless/pancake and standard motor families.
- Record manufacturer and exact part number only when source evidence supports it.
- Collect torque-speed curve, torque/speed constants, winding resistance, continuous/peak current, thermal limits, feedback, mass, envelope, and mounting data.
- Record India sourcing and price only when supported by dated supplier/manufacturer evidence.
- Populate `references/SOURCE_REGISTER.csv`.
- Mark missing data UNKNOWN.

**Inputs:** IN-013, IN-014, IN-038, IN-039; FS3-IN-002..FS3-IN-004, FS3-IN-007..FS3-IN-009.

**Outputs:** `component_research/` shortlist and source register.

**Effort:** 2 days. **Owner:** Mechanical Intern; Embedded Intern supports feedback/drive data review.

**Done criteria:** Candidate rows are source-backed and comparable; missing fields are explicit.

### WP-04 — Torque, Current, Voltage, and Thermal Screening

**Objective:** Evaluate candidates against continuous, peak, electrical, and thermal operating requirements.

**Tasks:**

- Compare continuous torque at required motor speed with FS-M-002 RMS/continuous loads.
- Apply the proposed 20% screening margin from IN-024 once and document the convention.
- Check peak torque/current, duration, repetition, recovery, and demagnetisation limits.
- Estimate current from candidate torque constants using the correct manufacturer convention.
- Evaluate back-EMF and voltage headroom at 24 V nominal, noting the unresolved SYS-REQ-041 range/regeneration.
- Assess winding loss, ambient limits, cooling assumptions, and thermal evidence.
- Identify required drive continuous/peak current for FS-M-008.

**Inputs:** IN-006..IN-009, IN-012, IN-014, IN-024, IN-026, IN-028, IN-029, IN-031, IN-032; FS3-IN-001, FS3-IN-005, FS3-IN-006, FS3-IN-008.

**Outputs:** Candidate calculation files and `outputs/MOTOR_SCREENING.csv`.

**Effort:** 2 days. **Owner:** Mechanical Intern; Embedded Intern reviews electrical/FOC aspects.

**Done criteria:** Candidates are evaluated at relevant operating points; assumptions and unknown thermal/current limits are visible.

### WP-05 — Joint Gearbox Iteration and System Handoff

**Objective:** Establish a comparable motor/ratio shortlist and deliver system interface data.

**Tasks:**

- Iterate motor candidates with FS-M-004 at 15:1, 20:1, and 25:1.
- Compare motor speed, continuous/peak torque, current, voltage headroom, inertia, package, and cooling.
- Record the consequences of the IN-039 motor-speed estimate and validate against actual candidate data.
- Provide current/voltage/feedback/thermal requirements to FS-M-008.
- Provide envelope/mass/mounting constraints to FS-M-007.
- Provide exact part-number and sourcing evidence to FS-M-009.
- Provide trade-off results and uncertainties to FS-M-010.

**Inputs:** WP-01..WP-04 outputs; IN-010, IN-011, IN-035, IN-039; relevant FS3-IN records.

**Outputs:** Motor/gearbox comparison, downstream handoff notes, updated candidate matrix.

**Effort:** 2 days. **Owner:** Mechanical Intern with FS-M-004 owner and Embedded Intern.

**Done criteria:** Ratio comparison is traceable; downstream requirements and limitations are documented; no unsupported final selection is made.

### WP-06 — Review, Rework, and Disposition

**Objective:** Complete evidence checks and record the study disposition.

**Tasks:**

- Track AC-001..AC-016.
- Check calculations and source-register completeness.
- Resolve review findings or retain them as blockers.
- Verify downstream handoff files and references.
- Update `README.md`, `REVIEW.md`, assumptions, open questions, and risks.
- Record a justified disposition and remaining limitations.

**Inputs:** WP-01..WP-05 outputs and `SPECIFICATION.md`.

**Outputs:** Complete reviewable study package and handoff record.

**Effort:** 2 days. **Owner:** Mechanical Intern; Project Lead reviewer.

**Done criteria:** Mandatory deliverables exist; every acceptance criterion has evidence or a documented blocker; conclusions remain within the evidence.

## 3. Ten-Day Schedule

| Day | Activity | Work package | Expected output |
|---|---|---|---|
| Day 1 | Requirements and FS-M-002 load-case reconciliation | WP-01 | Controlled baseline |
| Day 2 | Ratio operating points and calculation conventions | WP-02 | Sizing framework |
| Day 3 | Commercial candidate research | WP-03 | Initial candidate shortlist |
| Day 4 | Datasheet extraction and source register | WP-03 | Evidence-backed candidate data |
| Day 5 | Continuous and peak torque/current screening | WP-04 | Torque/current results |
| Day 6 | Voltage, feedback, and thermal screening | WP-04 | Electrical/thermal assessment |
| Day 7 | Joint motor/gearbox iteration | WP-05 | Ratio comparison |
| Day 8 | Downstream handoff preparation | WP-05 | Handoff data |
| Day 9 | Review and acceptance-criteria check | WP-06 | Review findings |
| Day 10 | Rework and disposition | WP-06 | Submission package |

## 4. Milestones and Gates

| Milestone | Target | Exit condition |
|---|---|---|
| M1 — Load baseline | Day 1 | Input IDs, load cases, and unresolved dependencies recorded |
| M2 — Sizing framework | Day 2 | Ratio equations and conventions checked |
| M3 — Candidate shortlist | Day 4 | Candidate sources and data gaps recorded |
| M4 — Technical screening | Day 6 | Continuous/peak, current, voltage, and thermal checks available |
| M5 — Joint ratio comparison | Day 7 | Motor/gearbox comparison ready for peer review |
| M6 — Handoff | Day 8 | Data prepared for FS-M-007/008/009/010 |
| M7 — Review and disposition | Day 10 | Acceptance tracking and review record completed |

**G1 — Load-data gate:** Do not treat unverified FS-M-002 cases as approved component limits.

**G2 — Continuous/peak gate:** Do not claim feasibility without relevant torque-speed, duty, current, and duration evidence.

**G3 — Electrical/thermal gate:** Voltage headroom, drive current, feedback, and thermal limitations must be visible before candidate acceptance.

**G4 — Joint-selection gate:** Do not finalize a motor independently of FS-M-004 gearbox ratio iteration.

## 5. Schedule Risks

| Risk ID | Risk | Impact | Mitigation |
|---|---|---|---|
| SCH-001 | FS-M-002 load cases or status unavailable | Motor sizing cannot be grounded | Coordinate with FS-M-002 owner; record provisional dependencies |
| SCH-002 | Candidate datasheets omit continuous/peak curves | Candidate comparison incomplete | Request manufacturer data; retain UNKNOWN fields |
| SCH-003 | Duty and peak duration remain unresolved | Continuous/peak claims blocked | Escalate required inputs; use labelled scenarios only |
| SCH-004 | Voltage range/regeneration undefined | Electrical compatibility incomplete | Resolve SYS-REQ-041 with Project Lead/Embedded Intern |
| SCH-005 | Motor constants use incompatible conventions | Current estimates invalid | Record manufacturer definitions and conversions |
| SCH-006 | Thermal data/cooling conditions unavailable | Thermal feasibility unverified | Record conditions and avoid unsupported acceptance |
| SCH-007 | Ratio decision changes motor candidate | Rework in motor/gearbox comparison | Iterate jointly with FS-M-004 |
| SCH-008 | Part number, price, or India availability unverified | Sourcing/cost handoff incomplete | Require dated traceable evidence |
| SCH-009 | Peak current exceeds candidate or drive limits | Candidate infeasible for target case | Screen duration and drive limits before shortlist acceptance |
| SCH-010 | Review findings need additional data | Day 10 disposition delayed | Prioritize critical gaps and revise schedule transparently |

## 6. Acceptance-Criteria Tracking

| Criterion ID | Acceptance criterion | Evidence path | Status | Notes |
|---|---|---|---|---|
| AC-001 | Applicable requirements and FS-M-001/FS-M-002 inputs are reconciled. | TBD | NOT_STARTED | Source revisions and load status |
| AC-002 | Motor-side speed and torque calculations are reproducible for 15:1, 20:1, and 25:1. | TBD | NOT_STARTED | Include equations and units |
| AC-003 | Commercial candidate shortlist uses traceable sources and exact part numbers where available. | TBD | NOT_STARTED | No invented data |
| AC-004 | Continuous torque is checked against the relevant speed and RMS load case. | TBD | NOT_STARTED | Include duty limitations |
| AC-005 | Peak torque/current and duration limitations are evaluated. | TBD | NOT_STARTED | Include manufacturer peak ratings |
| AC-006 | Torque constant, speed constant, and current conventions are documented. | TBD | NOT_STARTED | Datasheet definitions |
| AC-007 | Required current is estimated for continuous and peak operation. | TBD | NOT_STARTED | Correct motor-constant convention |
| AC-008 | Voltage/back-EMF headroom is assessed at required motor speed. | TBD | NOT_STARTED | Supply range and drive assumptions |
| AC-009 | Thermal capability is assessed or explicitly left unverified due to missing data. | TBD | NOT_STARTED | Ambient/cooling conditions |
| AC-010 | Demagnetisation and peak-current limits are considered. | TBD | NOT_STARTED | Manufacturer limits |
| AC-011 | Feedback and FOC compatibility are evaluated. | TBD | NOT_STARTED | Encoder/Hall evidence |
| AC-012 | Motor and gearbox ratio are jointly compared. | TBD | NOT_STARTED | FS-M-004 peer iteration |
| AC-013 | Mass, envelope, price, availability, and India sourcing are recorded where evidence exists. | TBD | NOT_STARTED | Source-backed only |
| AC-014 | Power-stage current implications are handed to FS-M-008. | TBD | NOT_STARTED | Continuous/peak current |
| AC-015 | Mandatory calculations, outputs, component research, and source register are complete and traceable. | TBD | NOT_STARTED | Repository evidence |
| AC-016 | Conclusions respect uncertainty and do not overstate feasibility. | TBD | NOT_STARTED | Review disposition |

## 7. Status Tracking

Allowed statuses: `NOT_STARTED`, `IN_PROGRESS`, `BLOCKED`, `DONE`.

| wp_id | task | owner | planned_start | planned_end | status | evidence_path |
|---|---|---|---|---|---|---|
| WP-01 | Requirements and load-case baseline | Mechanical Intern; Embedded Intern input | Day 1 | Day 1 | NOT_STARTED | TBD |
| WP-02 | Sizing method and ratio operating points | Mechanical Intern | Day 2 | Day 2 | NOT_STARTED | TBD |
| WP-03 | Commercial candidate research | Mechanical Intern; Embedded Intern input | Day 3 | Day 4 | NOT_STARTED | TBD |
| WP-04 | Torque/current/voltage/thermal screening | Mechanical Intern; Embedded Intern input | Day 5 | Day 6 | NOT_STARTED | TBD |
| WP-05 | Joint gearbox iteration and system handoff | Mechanical Intern; FS-M-004 owner | Day 7 | Day 8 | NOT_STARTED | TBD |
| WP-06 | Review, rework, and disposition | Mechanical Intern; Project Lead | Day 9 | Day 10 | NOT_STARTED | TBD |

## 8. Handoff Requirements

- Publish the candidate shortlist, calculation outputs, and `references/SOURCE_REGISTER.csv`.
- Label each candidate field as sourced, calculated, assumed, or unknown.
- Deliver continuous/peak current and voltage/back-EMF findings to FS-M-008.
- Deliver motor envelope, mass, mounting, and cooling constraints to FS-M-007.
- Deliver traceable part numbers and sourcing/cost evidence to FS-M-009.
- Deliver the motor/gearbox comparison and unresolved trade-offs to FS-M-004 and FS-M-010.
- Do not claim final motor selection until the required evidence and review are complete.
