---
study_id: FS-M-002
title: Load and Torque Analysis - Work Plan
product: Kritva-M
priority: P1
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Independent Reviewer TBD
planned_duration_working_days: 10
verification_status: NOT_STARTED
upstream_dependencies:
- FS-M-001
downstream_studies:
- FS-M-003
- FS-M-004
- FS-M-005
- FS-M-006
- FS-M-010
---

# FS-M-002 Work Plan

## 1. Purpose

Execute FS-M-002 to establish a traceable static, dynamic, continuous/RMS, peak, and stop-impact load baseline for the Kritva-M elbow actuator. Deliver reproducible calculations and controlled load cases to downstream studies.

## 2. Execution Rules

1. Follow `SPECIFICATION.md` and the current canonical `requirements/SYSTEM_REQUIREMENTS.md`.
2. Use upstream FS-M-001 input IDs exactly as defined in its `inputs/INPUTS.md`; use `FS2-IN-nnn` only for study-local inputs.
3. Preserve input statuses. Proposed values are preliminary; assumed scenarios are not approved requirements.
4. Define and document the joint-angle reference and torque sign convention before accepting calculations.
5. Do not infer missing duty-cycle, acceleration, peak-duration, or recovery requirements.
6. Keep gravity, inertial, friction/loss, external, and impact contributions distinguishable.
7. Peak-load and stop-impact cases require independent review. Results remain `NOT_VERIFIED` until the required review is recorded.
8. Track work using `NOT_STARTED`, `IN_PROGRESS`, `BLOCKED`, and `DONE`.
9. `DONE` means the specified evidence exists and has been checked; it does not automatically mean the study or its conclusions are accepted.
10. Record blockers, changes, evidence paths, and downstream impacts in the repository.

## 3. Work Packages

### WP-01 — Requirements, Inputs, and Geometry Baseline

**Objective:** Establish the controlled input set, coordinate convention, and geometry required for reproducible calculations.

**Tasks:**

- Confirm the canonical requirement revision and FS-M-001 input register.
- Verify applicable upstream input IDs, values, units, statuses, and source references.
- Define the joint axis, angle zero, positive rotation, gravity direction, and torque sign.
- Reconcile the 0–135° analysis range with the canonical 0–120° to 135° range and the defined fully extended pose.
- Verify the provenance and applicability of IN-017 and identify its included bodies and reference axis.
- Record unresolved inputs and assign owners.

**Inputs:** IN-001..IN-005, IN-027, IN-033, IN-035; FS2-IN-001, FS2-IN-004, FS2-IN-005, FS2-IN-006, FS2-IN-007.

**Outputs:** Reconciled input baseline, coordinate-convention record, updated `inputs/INPUTS.md`, and study-local assumptions/open questions.

**Effort:** 1 working day.

**Owner:** Mechanical Intern. Project Lead resolves requirement ambiguities.

**Done criteria:** Applicable input IDs and statuses match the authoritative source; coordinate convention is documented; discrepancies and blockers are recorded.

### WP-02 — Static Gravity Torque and Sensitivity

**Objective:** Calculate gravity torque over the complete range and quantify sensitivity to uncertain geometry.

**Tasks:**

- Calculate forearm/hand and payload torque separately and in combination.
- Generate a sweep from 0° to 135° using the documented angle increment.
- Identify the maximum absolute torque, governing angle, sign changes, and zero crossings.
- Cross-check the result against IN-005 without forcing agreement.
- Calculate the CoM cases at 160, 180, and 200 mm using the ASSUMED ±20 mm range.
- Define and justify a payload-position sensitivity interval; if not justified, mark the sensitivity incomplete.
- Record units, equations, geometry, assumptions, and source references.

**Inputs:** IN-001..IN-005, IN-027, IN-033; FS2-IN-001, FS2-IN-002, FS2-IN-003, FS2-IN-004, FS2-IN-006.

**Outputs:** `outputs/GRAVITY_TORQUE_SWEEP.csv`, static calculation files, sensitivity tables and plots as useful.

**Effort:** 2 working days.

**Owner:** Mechanical Intern.

**Done criteria:** Full range is covered; governing result is identified; CoM sensitivity is complete; payload sensitivity is justified or explicitly incomplete; IN-005 comparison is documented.

### WP-03 — Dynamic, Continuous/RMS, and Peak Loads

**Objective:** Calculate torque demand for defined motion profiles and characterize continuous and peak load cases.

**Tasks:**

- Obtain the approved acceleration/deceleration profile or define clearly labelled illustrative scenarios.
- Calculate inertial torque using verified inertia and a documented reference axis.
- Combine gravity and inertial torque using physically consistent signs.
- Identify friction and external-load terms; document missing data instead of silently assuming zero.
- Define an operating cycle and calculate RMS torque where the inputs support it.
- Compare continuous and peak cases with IN-006 and IN-007.
- Record limitations due to IN-026, IN-031, and IN-032.

**Inputs:** IN-005..IN-008, IN-014, IN-017, IN-026, IN-031, IN-032, IN-035; FS2-IN-001, FS2-IN-005, FS2-IN-006, FS2-IN-008, FS2-IN-009.

**Outputs:** Dynamic calculation files, `outputs/DYNAMIC_TORQUE_RESULTS.csv`, peak-case register, unresolved-input list.

**Effort:** 2 working days.

**Owner:** Mechanical Intern; coordinate motion-profile inputs with Project Lead and Embedded Intern.

**Done criteria:** Defined profiles are traceable; dynamic calculations are reproducible; RMS results have an explicit cycle definition; peak duration/repetition limitations are documented.

### WP-04 — Stop-Impact Assessment and Reflected Inertia

**Objective:** Assess stop-impact loads and calculate ratio-dependent reflected inertia.

**Tasks:**

- Reproduce or substantiate the IN-018 stop-energy estimate.
- Recover and verify the derivation behind IN-019 impact torque.
- Check the included masses, inertia axis, angular velocity, contact assumptions, and units.
- Evaluate the IN-036 single-contact assumption and document the reaction load path.
- Identify additional impact-model inputs needed to establish peak loads.
- Calculate reflected inertia for 15:1, 20:1, and 25:1.
- Document unavailable motor or gearbox inertia and backdrivability data.
- Submit peak and impact calculations for independent review.

**Inputs:** IN-007, IN-010..IN-012, IN-017..IN-019, IN-031, IN-035, IN-036, IN-039; FS2-IN-001, FS2-IN-005, FS2-IN-006, FS2-IN-007, FS2-IN-008.

**Outputs:** Impact calculation files, `outputs/REFLECTED_INERTIA.csv`, impact load cases, independent-review record.

**Effort:** 2 working days.

**Owner:** Mechanical Intern. Independent Reviewer TBD.

**Done criteria:** Calculations are reproducible or explicitly unverified with documented gaps; reflected-inertia comparisons are complete; mandatory independent review is recorded before accepting safety-critical results.

### WP-05 — Consolidated Load Cases and Downstream Handoff

**Objective:** Publish consistent load-case data for downstream component studies.

**Tasks:**

- Consolidate static, dynamic, continuous/RMS, peak, and impact cases.
- Include torque sign, angle, speed, acceleration, duration, repetition, and reaction loads where available.
- Distinguish physical output load from motor-side demand.
- Trace each case to inputs, assumptions, calculations, and review status.
- Prepare handoff notes for FS-M-003, FS-M-004, FS-M-005, FS-M-006, and FS-M-010.
- Flag provisional or blocked cases prominently.

**Inputs:** WP-01 through WP-04 outputs; applicable IN-001..IN-039 and FS2-IN-001..FS2-IN-009.

**Outputs:** `outputs/LOAD_CASES.csv`, downstream handoff notes, updated assumptions/open questions.

**Effort:** 1 working day.

**Owner:** Mechanical Intern.

**Done criteria:** Each required downstream study has traceable applicable load cases and limitations; output data are machine-readable and consistently unit-labelled.

### WP-06 — Review, Rework, and Study Submission

**Objective:** Complete evidence checks, independent review, documentation, and study disposition.

**Tasks:**

- Check all acceptance criteria AC-001..AC-016.
- Verify calculations and output files are reproducible.
- Resolve review findings or record them as open blockers.
- Obtain independent review for peak and stop-impact cases.
- Update `README.md`, `REVIEW.md`, risks, assumptions, open questions, and status tracking.
- Record the study disposition without overstating feasibility.

**Inputs:** All WP-01..WP-05 outputs; `SPECIFICATION.md`; AC-001..AC-016.

**Outputs:** Complete study package, review evidence, disposition and handoff record.

**Effort:** 2 working days, including planned review/rework.

**Owner:** Mechanical Intern; Independent Reviewer for required safety-critical review.

**Done criteria:** Mandatory deliverables are complete, acceptance criteria have evidence-based dispositions, and all unresolved blockers are explicit. No safety-critical result is accepted without required independent review.

## 4. Ten-Day Schedule

| Day | Planned work | Work package | Expected result |
|---|---|---|---|
| Day 1 | Requirement/input reconciliation, geometry, coordinate convention | WP-01 | Controlled baseline |
| Day 2 | Gravity torque derivation and angle sweep | WP-02 | Initial sweep |
| Day 3 | CoM/payload sensitivity and static cross-check | WP-02 | Static results |
| Day 4 | Motion profiles and dynamic torque | WP-03 | Dynamic cases |
| Day 5 | Continuous/RMS and peak cases | WP-03 | RMS and peak results |
| Day 6 | Stop energy and impact derivation | WP-04 | Impact evidence/gaps |
| Day 7 | Stop reactions and reflected inertia | WP-04 | Impact cases and ratio comparison |
| Day 8 | Consolidate load cases and downstream handoff | WP-05 | Draft output package |
| Day 9 | Independent review and review-finding triage | WP-06 | Review record |
| Day 10 | Rework, evidence check, and submission | WP-06 | Final disposition package |

Schedule is in working days, not calendar dates. Missing source data or reviewer availability may block completion; revise the plan rather than marking incomplete work DONE.

## 5. Milestones and Gates

| Milestone | Target | Exit condition |
|---|---|---|
| M1 — Baseline established | Day 1 | Requirements, input IDs, and coordinate convention reconciled |
| M2 — Static load envelope | Day 3 | Gravity sweep and required sensitivity results available |
| M3 — Motion-load envelope | Day 5 | Dynamic, RMS, and peak cases documented or explicitly blocked |
| M4 — Impact/inertia analysis | Day 7 | Impact derivation status recorded; ratio comparison complete |
| M5 — Handoff prepared | Day 8 | Machine-readable load cases and downstream notes available |
| M6 — Independent review | Day 9 | Required peak/impact review completed or blocker recorded |
| M7 — Submission | Day 10 | Acceptance tracking and disposition complete |

**Gate G1 — Input and coordinate gate:** Do not accept gravity results until geometry, angle reference, and torque convention are documented.

**Gate G2 — Dynamic/peak gate:** Do not claim dynamic, continuous, or peak feasibility without the necessary profile, duty, and peak-duration inputs.

**Gate G3 — Safety-critical load gate:** Stop-impact and peak-load cases remain `NOT_VERIFIED` until independent review is recorded.

**Gate G4 — Handoff gate:** Downstream load cases must carry assumptions, units, source references, and verification status.

## 6. Schedule Risks

| Risk ID | Risk | Effect | Mitigation/trigger |
|---|---|---|---|
| SCH-001 | Canonical geometry or angle convention unresolved | Static results delayed or invalid | Resolve in WP-01 before accepting WP-02 |
| SCH-002 | IN-017 inertia source/axis unavailable | Dynamic and reflected-inertia results uncertain | Request source and document included bodies |
| SCH-003 | Duty/acceleration profile unavailable | RMS/dynamic conclusion blocked | Request approved profile; use scenarios only as labelled sensitivity |
| SCH-004 | Peak duration/repetition/recovery unresolved | Peak feasibility cannot be concluded | Track as blocker and notify Project Lead |
| SCH-005 | IN-018/IN-019 derivation unavailable | Impact case unverified | Recover source or retain explicit evidence gap |
| SCH-006 | Independent reviewer not assigned | Safety-critical gate blocked | Project Lead assigns reviewer before review submission |
| SCH-007 | Payload sensitivity range not justified | Sensitivity acceptance delayed | Obtain CAD/configuration basis or mark incomplete |
| SCH-008 | Friction/external-load model unavailable | Dynamic result may be incomplete | Separate terms and quantify limitations |
| SCH-009 | Downstream teams need data before acceptance | Risk of premature design decisions | Issue provisional data with explicit status and caveats |
| SCH-010 | Review findings require substantial rework | Day 10 submission delayed | Prioritize critical/high findings and revise schedule transparently |

## 7. Acceptance-Criteria Tracking

Statuses below are initial planning statuses. Update evidence paths and statuses as work progresses. Criterion descriptions match `SPECIFICATION.md`.

| Criterion ID | Acceptance criterion | Evidence path | Status | Notes |
|---|---|---|---|---|
| AC-001 | Requirements and upstream input IDs are reconciled. | TBD | NOT_STARTED | Verify authoritative IDs and source revisions |
| AC-002 | Coordinate, angle, and torque sign conventions are documented. | TBD | NOT_STARTED | Include geometry reference |
| AC-003 | Gravity torque is calculated across 0–135°. | TBD | NOT_STARTED | Full sweep and governing angle |
| AC-004 | IN-005 is checked against the gravity calculation. | TBD | NOT_STARTED | Explain discrepancy if any |
| AC-005 | CoM sensitivity is evaluated at 160, 180, and 200 mm. | TBD | NOT_STARTED | ASSUMED range |
| AC-006 | Payload-position sensitivity is evaluated or its incompleteness documented. | TBD | NOT_STARTED | Justify range |
| AC-007 | Dynamic torque is calculated for defined profiles or the limitation is documented. | TBD | NOT_STARTED | Do not imply assumed profile is approved |
| AC-008 | Continuous/RMS torque is assessed for a defined cycle or remains explicitly incomplete. | TBD | NOT_STARTED | Duty-cycle dependency |
| AC-009 | Peak torque cases are documented. | TBD | NOT_STARTED | Include duration/repetition dependencies |
| AC-010 | Impact estimates are reproduced or explicitly left unverified. | TBD | NOT_STARTED | IN-018 and IN-019 provenance |
| AC-011 | Peak and stop-impact cases receive independent review. | TBD | NOT_STARTED | Mandatory independent review |
| AC-012 | Reflected inertia is calculated for 15:1, 20:1, and 25:1. | TBD | NOT_STARTED | Reference axes and included inertias |
| AC-013 | Downstream load cases are traceable and usable. | TBD | NOT_STARTED | All five downstream studies |
| AC-014 | Calculations and outputs are reproducible. | TBD | NOT_STARTED | Independent reproducibility check |
| AC-015 | Assumptions and unresolved inputs are maintained. | TBD | NOT_STARTED | Owners and validation actions |
| AC-016 | Conclusions do not exceed the evidence. | TBD | NOT_STARTED | Review disposition |

## 8. Status Tracking

Use one row per work package. Update status and evidence path during execution.

| wp_id | task | owner | planned_start | planned_end | status | evidence_path |
|---|---|---|---|---|---|---|
| WP-01 | Requirements, inputs, and geometry baseline | Mechanical Intern | Day 1 | Day 1 | NOT_STARTED | TBD |
| WP-02 | Static gravity torque and sensitivity | Mechanical Intern | Day 2 | Day 3 | NOT_STARTED | TBD |
| WP-03 | Dynamic, continuous/RMS, and peak loads | Mechanical Intern | Day 4 | Day 5 | NOT_STARTED | TBD |
| WP-04 | Stop-impact assessment and reflected inertia | Mechanical Intern; Independent Reviewer TBD | Day 6 | Day 7 | NOT_STARTED | TBD |
| WP-05 | Consolidated load cases and downstream handoff | Mechanical Intern | Day 8 | Day 8 | NOT_STARTED | TBD |
| WP-06 | Review, rework, and study submission | Mechanical Intern; Independent Reviewer TBD | Day 9 | Day 10 | NOT_STARTED | TBD |

Allowed statuses: `NOT_STARTED`, `IN_PROGRESS`, `BLOCKED`, `DONE`. If blocked, document the reason, responsible party, and next action in the work-package notes or study issue log.

## 9. Handoff Requirements

Before handoff:

- Publish `outputs/LOAD_CASES.csv` and associated sweep, dynamic, and reflected-inertia outputs.
- Include units, torque sign, angle convention, profile, duration/repetition status, and input references.
- Identify preliminary, assumed, unverified, and independently reviewed cases.
- Notify FS-M-003, FS-M-004, FS-M-005, FS-M-006, and FS-M-010 of applicable load cases and unresolved dependencies.
- Do not label provisional cases as approved design limits.
- Record acceptance criteria status, reviewer disposition, and remaining blockers in `REVIEW.md`.
