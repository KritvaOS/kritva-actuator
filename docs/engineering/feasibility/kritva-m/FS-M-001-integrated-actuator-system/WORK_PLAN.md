---
study_id: FS-M-001
title: "Integrated Actuator System Feasibility — Work Plan"
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Project Lead; Independent Reviewer TBD for safety-critical shaft, bearing and stop checks
planned_duration: 10 working days
---

# FS-M-001 — Work Plan

## 1. Purpose

Define the execution sequence, tasks, inputs, outputs, dependencies, effort and completion criteria for the integrated Kritva-M actuator feasibility study.

This plan follows `SPECIFICATION.md`, the applicable acceptance criteria AC-001 through AC-016, and the 10-working-day schedule. Day 1 through Day 10 are relative working-day labels; calendar dates will be added only when the schedule is authorized.

The plan does not convert proposed system requirements into approved requirements or waive mandatory technical reviews.

## 2. Execution rules

1. Use `inputs/INPUTS.md` as the study input index. Refer to inputs by their stable `IN-nnn` identifiers.
2. Use `requirements/SYSTEM_REQUIREMENTS.md` as the canonical requirements source.
3. Record calculations and evidence in their appropriate directories; link to evidence rather than duplicating it.
4. Update task status and evidence paths as work progresses.
5. Record blockers, changed assumptions and schedule impacts promptly.
6. A task is `DONE` only when its stated exit criteria are met and evidence is linked.
7. Safety-critical shaft, bearing and stop checks require independent review. If required independent review is incomplete, affected work remains `NOT_VERIFIED`.
8. If evidence cannot be completed within ten working days, record the blocker and remaining work rather than claiming completion.

### 2.1 Task status values

Use the following status values in the tracking table:

- `NOT_STARTED`
- `IN_PROGRESS`
- `BLOCKED`
- `DONE`

These are work-plan tracking values, not the study lifecycle or verification status.

## 3. Work packages

### WP-01 — Requirement and baseline reconciliation

**Objective:** Establish the requirement, input and evidence baseline for the study.

**Tasks:**

1. Read `requirements/SYSTEM_REQUIREMENTS.md` revision 0.2 and confirm the applicable `SYS-REQ-nnn` identifiers.
2. Verify that all applicable requirement values remain classified as proposed.
3. Reconcile the specification against `inputs/INPUTS.md`, including source, units and status labels.
4. Identify conflicts, missing acceptance conditions and unconfirmed inputs.
5. Establish a requirement-to-evidence mapping for AC-001 and AC-002.
6. Record unresolved issues in `ASSUMPTIONS_AND_OPEN_QUESTIONS.md`.

**Inputs:** IN-001 to IN-016, IN-020 to IN-022, IN-026 to IN-035, IN-038.

**Outputs:**

- Requirement-to-evidence mapping in `outputs/`.
- Updated `ASSUMPTIONS_AND_OPEN_QUESTIONS.md`.
- Input/source discrepancies and required decisions.
- Baseline reconciliation notes in `outputs/README.md`.

**Dependencies on other studies:** None required to start. Findings will feed FS-M-002 through FS-M-010.

**Effort:** 1 day.

**Owner:** Mechanical Intern.

**Done criteria:**

- Applicable requirement IDs and current status are reconciled against the canonical file.
- Material inputs have source, units and status labels.
- Open questions and discrepancies are recorded.
- AC-001 and AC-002 have evidence or explicit unresolved dispositions.

### WP-02 — Integrated load and operating envelope

**Objective:** Establish the preliminary load cases and identify the operating conditions needed for meaningful sizing.

**Tasks:**

1. Recalculate the gravity holding torque from the stated masses and moment arms.
2. Check dimensional consistency and unit conversions.
3. Identify static holding, continuous motion, acceleration, peak torque and stop-impact cases.
4. Identify the effect of the provisional forearm centre of mass.
5. Record missing duty cycle, acceleration, peak duration/repetition/recovery and other load conditions.
6. Establish which load results can be used now and which remain preliminary.
7. Identify required sensitivity cases for FS-M-002.

**Inputs:** IN-001 to IN-008, IN-017 to IN-019, IN-026, IN-027, IN-031, IN-032, IN-033, IN-036.

**Outputs:**

- Load-case table in `outputs/`.
- Torque calculation source in `calculations/`.
- Preliminary load and torque results CSV.
- Updated open questions and sensitivity requirements.

**Dependencies on other studies:** FS-M-002 provides the detailed load and torque analysis. WP-02 establishes the initial baseline for that study and must not wait for FS-M-002 to be completed.

**Effort:** 1.5 days.

**Owner:** Mechanical Intern.

**Done criteria:**

- Gravity torque is recalculated with documented assumptions and units.
- Dynamic and impact cases are distinguished from static holding.
- Missing operating conditions are explicitly listed.
- AC-003 has evidence or a documented blocker.

### WP-03 — Motor and gearbox operating-point screening

**Objective:** Evaluate whether the proposed motor power range and candidate gearbox ratios can plausibly support the required output operating point.

**Tasks:**

1. Calculate implied motor speed for 15:1, 20:1 and 25:1 ratios.
2. Calculate required motor torque for the applicable output cases using documented gearbox efficiency.
3. Check torque-speed and power consistency.
4. Compare the 75–100 W preliminary motor target with calculated requirements.
5. Identify required motor datasheet parameters and commercial candidate evidence.
6. Review continuous versus peak motor and gearbox ratings.
7. Document candidate gaps, sensitivity to efficiency and the need for iteration between motor and gearbox selection.

**Inputs:** IN-006 to IN-014, IN-026, IN-031, IN-032, IN-035, IN-039.

**Outputs:**

- Ratio comparison table in `outputs/`.
- Motor/gearbox calculation scripts in `calculations/`.
- Component source references and candidate comparison in `component_research/`.
- List of missing motor and gearbox operating data.

**Dependencies on other studies:** FS-M-002 supplies detailed load cases; FS-M-003 develops motor selection; FS-M-004 develops gearbox selection. These studies may proceed in parallel using the initial baseline, with results reconciled when available.

**Effort:** 1.5 days.

**Owner:** Mechanical Intern, with Embedded Intern input on electrical and motor data.

**Done criteria:**

- All three candidate ratios are evaluated using a consistent method.
- Torque, speed, power and efficiency assumptions are documented.
- Datasheet conditions and continuous/peak ratings are interpreted correctly.
- AC-004 and AC-005 have evidence or explicit unresolved limitations.

### WP-04 — Shaft, bearing and stop architecture review

**Objective:** Identify mechanical architecture blockers and define the evidence needed to establish shaft, bearing and stop feasibility.

**Tasks:**

1. Reconcile the 12 mm nominal shaft with the proposed 15 mm bearing seats.
2. Identify the actual shaft steps, bearing fits, shoulders, retention and interface requirements.
3. Retrieve and check the earlier EN8 normalised shaft-strength calculation and reported safety factor of approximately 0.86.
4. Review the EN19/42CrMo4 quenched-and-tempered material candidate without treating it as approved.
5. Review the dedicated bearing-pair architecture and external load path.
6. Review the reported 1.9 J stop energy and 47.5 N·m impact torque assumptions.
7. Identify the governing single-contact stop case and determine what evidence would be needed to demonstrate balanced load sharing.
8. Prepare the shaft, bearing and stop calculations for independent review.

**Inputs:** IN-005 to IN-008, IN-015 to IN-019, IN-023, IN-036, IN-037.

**Outputs:**

- Shaft/bearing interface assessment in `outputs/`.
- Mechanical-stop assumptions and risk record.
- Calculation evidence and source references.
- Independent-review request and findings record.
- Updated safety-critical open questions.

**Dependencies on other studies:** FS-M-002 supplies refined load cases; FS-M-004 supplies gearbox output interface information; FS-M-005 develops shaft feasibility; FS-M-006 develops bearing/support feasibility; FS-M-007 develops housing and stop integration.

**Effort:** 1.5 days.

**Owner:** Mechanical Intern.

**Required reviewers:** Project Lead and Independent Reviewer TBD for safety-critical shaft, bearing and stop checks.

**Done criteria:**

- The 12 mm/15 mm interface issue is resolved at the architecture level or explicitly blocked.
- Existing strength and impact findings are traceable to calculations or marked unverified.
- The single-contact stop case is addressed.
- Required independent review is requested and its status recorded.
- AC-006, AC-007 and AC-008 have evidence or an explicit unresolved disposition.

**Mandatory verification rule:** If the required independent review has not been completed, the affected safety-critical checks remain `NOT_VERIFIED`.

### WP-05 — Electrical, thermal and sensing interfaces

**Objective:** Identify the electrical, thermal and sensing constraints that affect integrated feasibility.

**Tasks:**

1. Identify motor voltage, torque-speed, current, loss and thermal data required for candidate evaluation.
2. Check the relation between motor power and the proposed output operating point.
3. Identify supply-current limits and power-stage peak/continuous sizing needs.
4. Record missing duty-cycle, peak-duration and ambient-temperature inputs.
5. Review output encoder location, alignment and load-related deflection requirements.
6. Identify unresolved MCU class, control and interface constraints.
7. Define the evidence needed by FS-M-008.

**Inputs:** IN-006 to IN-009, IN-012 to IN-014, IN-024, IN-026, IN-028, IN-029, IN-031, IN-032, IN-034, IN-035.

**Outputs:**

- Electrical/thermal interface summary in `outputs/`.
- Motor data requirements and source references.
- Open-question updates.
- Input requirements for FS-M-008.

**Dependencies on other studies:** FS-M-003 provides motor candidates; FS-M-004 provides gearbox efficiency and losses; FS-M-008 performs detailed electrical and thermal feasibility.

**Effort:** 1 day.

**Owner:** Embedded Intern, coordinated by the Mechanical Intern.

**Done criteria:**

- Electrical and thermal input gaps are documented.
- Continuous and peak conditions are distinguished.
- Encoder alignment and operating constraints are captured.
- AC-009 has evidence or an explicit blocker.

### WP-06 — Packaging, manufacturing and cost screening

**Objective:** Establish the preliminary packaging baseline and assess whether the proposed budget is credible.

**Tasks:**

1. Establish preliminary placement and interface constraints for motor, gearbox, shaft, bearings, encoder and stops.
2. Record known mass and envelope unknowns.
3. Review whether the available layout evidence is sufficient for initial integration feasibility.
4. Assemble a preliminary component-level BOM and cost estimate.
5. Identify exact part numbers where available and mark missing identities as unknown.
6. Separate quoted prices from estimates and document source dates, currency and quantity assumptions.
7. Compare the approximately ₹22,000 A0 BOM upper-bound allowance with the proposed ₹10,000–₹15,000 A0 budget.
8. Identify cost and manufacturing questions for FS-M-009.

**Inputs:** IN-009 to IN-011, IN-013, IN-015, IN-016, IN-020 to IN-022, IN-033, IN-034, IN-037, IN-038.

**Outputs:**

- Preliminary system layout or CAD evidence.
- `cost_estimate/BOM_COST_ESTIMATE.csv`.
- Packaging/interface constraints.
- Cost assumptions, exclusions and sourcing gaps.
- Manufacturing and cost follow-on actions.

**Dependencies on other studies:** FS-M-003 supplies motor candidates; FS-M-004 supplies gearbox candidates; FS-M-005 and FS-M-006 supply shaft/bearing constraints; FS-M-007 develops mechanical integration; FS-M-008 supplies electrical and thermal component needs; FS-M-009 performs detailed manufacturing/cost analysis.

**Effort:** 1.5 days.

**Owner:** Mechanical Intern, with Embedded Intern input for electrical components.

**Done criteria:**

- Preliminary layout and major interfaces are documented.
- BOM scope and cost basis are explicit.
- The A0 budget discrepancy is visible and investigated.
- Exact part-number gaps are recorded.
- AC-010 and AC-011 have evidence or explicit limitations.

### WP-07 — Integrated assessment and handoff

**Objective:** Consolidate evidence, review acceptance criteria and prepare the study conclusion and next actions.

**Tasks:**

1. Review the requirement-to-evidence mapping.
2. Consolidate calculations, component research, packaging evidence and cost results.
3. Review sensitivity, assumptions and risk register entries.
4. Assess AC-001 through AC-016.
5. Check all conditional deliverable applicability decisions.
6. Prepare a feasibility category and verification status consistent with the available evidence.
7. Record outstanding blockers, required independent reviews and proposed next actions.
8. Update `README.md`, `REVIEW.md` and relevant register references.
9. Submit the study package for Project Lead review and required independent safety-critical review.

**Inputs:** IN-001 through IN-039, where applicable, and all outputs from WP-01 through WP-06.

**Outputs:**

- Integrated feasibility conclusion in `outputs/`.
- Acceptance-criteria matrix.
- Updated risk and open-question records.
- Review-ready `REVIEW.md`.
- Updated study README and follow-on work recommendations.

**Dependencies on other studies:** FS-M-002 through FS-M-009 provide follow-on detailed evidence. FS-M-010 uses the integrated result for final candidate trade-off. This package must state which downstream results are still pending.

**Effort:** 1 day.

**Owner:** Mechanical Intern.

**Reviewers:** Project Lead and Independent Reviewer TBD for required safety-critical items.

**Done criteria:**

- AC-001 through AC-016 are individually dispositioned with evidence.
- All mandatory deliverables are present.
- All conditional deliverables have explicit applicability decisions.
- Safety-critical review status is explicit.
- Conclusion category, verification status and lifecycle status are consistent.
- The final handoff identifies limitations and next actions.
- AC-012 through AC-016 have evidence or an explicit blocker/disposition.

## 4. Ten-working-day schedule

The following schedule is relative to the first authorized working day. No calendar dates are assumed.

| Day | Main activities | Planned work packages | Milestone / evidence |
|---|---|---|---|
| Day 1 | Reconcile requirements, input register and source baseline | WP-01 | M1 — Requirement and input baseline |
| Day 2 | Recalculate gravity torque and establish load cases | WP-02 | M2 — Load-case and open-question table |
| Day 3 | Evaluate 15:1, 20:1 and 25:1 ratios; check torque, speed and power | WP-03 | M3 — Ratio screening calculations |
| Day 4 | Review commercial motor/gearbox data and continuous/peak ratings | WP-03 | M4 — Candidate evidence and gaps |
| Day 5 | Review shaft, bearing-seat interface, material and load paths | WP-04 | M5 — Mechanical interface and strength issues |
| Day 6 | Review stop energy, impact torque and safety-critical calculations | WP-04 | M6 — Independent-review package or explicit blocker |
| Day 7 | Review electrical, thermal, encoder and MCU interface gaps | WP-05 | M7 — Electrical/thermal input gap list |
| Day 8 | Prepare layout/CAD evidence and preliminary BOM/cost estimate | WP-06 | M8 — Packaging baseline and budget comparison |
| Day 9 | Consolidate risk, sensitivity, requirement mapping and draft conclusion | WP-07 | M9 — Review-ready draft |
| Day 10 | Address review comments where possible; record residual issues and handoff | WP-07 | M10 — Review package and follow-on actions |

The effort estimates total approximately nine working days, leaving limited contingency within the ten-day plan. Critical findings, missing supplier data or unavailable independent reviewers may extend the schedule.

## 5. Milestones and review points

| Milestone | Target day | Required evidence | Review / exit condition |
|---|---|---|---|
| M1 — Baseline reconciled | Day 1 | Requirement mapping and input/source reconciliation | Project Lead reviews discrepancies and baseline assumptions |
| M2 — Load baseline established | Day 2 | Gravity torque calculation, load-case table and unknowns | Units and equations checked; dynamic limitations documented |
| M3 — Ratio screening completed | Day 3 | Ratio calculations for 15:1, 20:1 and 25:1 | Torque-speed-power consistency checked |
| M4 — Candidate evidence reviewed | Day 4 | Datasheet/source register and candidate comparison | Continuous/peak ratings and operating conditions correctly interpreted |
| M5 — Mechanical interfaces reviewed | Day 5 | Shaft/bearing interface evidence and strength calculation provenance | Interface mismatch and material concern explicitly dispositioned |
| M6 — Safety-critical review point | Day 6 | Shaft, bearing and stop calculations, assumptions and review record | Independent review required; without it affected checks remain `NOT_VERIFIED` |
| M7 — Electrical/thermal gaps recorded | Day 7 | Motor data, current, ambient, duty-cycle and encoder gap list | Missing inputs and their consequences recorded |
| M8 — Packaging/cost baseline | Day 8 | Layout/CAD evidence and BOM/cost estimate | Cost basis and A0 budget discrepancy reviewed |
| M9 — Draft conclusion | Day 9 | Acceptance-criteria matrix, risk assessment and preliminary conclusion | Project Lead identifies remaining blockers and required changes |
| M10 — Study handoff | Day 10 | Finalized study package, review record and follow-on plan | Acceptance decision recorded only if all prerequisites are met |

### 5.1 Mandatory review gates

- **Gate G1 — Requirements and inputs:** proposed values remain `PRELIMINARY` until formally approved.
- **Gate G2 — Calculation quality:** material calculations have documented equations, units, assumptions and sanity checks.
- **Gate G3 — Safety-critical mechanical checks:** shaft, bearing and stop work receives required independent review.
- **Gate G4 — Integrated conclusion:** all material limitations, cost gaps and unresolved operating conditions are visible.
- **Gate G5 — Final study review:** mandatory deliverables and applicable acceptance criteria are checked before an acceptance decision.

A schedule milestone may be completed as an administrative checkpoint while technical verification remains open. It must not be used to imply that a technical check has passed.

## 6. Risks to the schedule

| Risk ID | Schedule risk | Likely impact | Mitigation / response | Owner |
|---|---|---|---|---|
| SCH-001 | Canonical requirement wording or status differs from working notes | Rework of requirement mapping and calculations | Verify the source file on Day 1 and record discrepancies before calculations proceed | Mechanical Intern |
| SCH-002 | Motor datasheets lack continuous/peak operating conditions | Candidate comparison cannot establish feasibility | Request manufacturer data; record gaps and use clearly bounded preliminary screening | Mechanical Intern / Embedded Intern |
| SCH-003 | Duty cycle and peak duration remain undefined | Thermal and dynamic acceptance blocked | Raise requirement clarification early; keep affected conclusions unverified | Project Lead |
| SCH-004 | Original shaft-strength calculation cannot be located or reproduced | Safety-critical mechanical conclusion delayed | Retrieve the source, rebuild the calculation with traceable inputs or mark it unverified | Mechanical Intern |
| SCH-005 | Independent reviewer is unavailable within the planned window | Shaft, bearing and stop checks cannot be accepted | Assign reviewer early; escalate scheduling; do not bypass independent review | Project Lead |
| SCH-006 | Bearing bore and shaft-seat mismatch requires architecture change | CAD/layout and bearing assessment rework | Resolve interface geometry before detailed packaging is treated as stable | Mechanical Intern |
| SCH-007 | Stop-impact model lacks defensible contact assumptions | Stop safety conclusion blocked | Document the model gap and define the required test or validated analysis | Mechanical Intern / Independent Reviewer |
| SCH-008 | Cost evidence is incomplete or inconsistent | A0 budget conclusion remains uncertain | Record source dates, exact parts, currency and exclusions; preserve the known budget discrepancy | Mechanical Intern |
| SCH-009 | Packaging constraints are not defined | CAD feasibility cannot be finalized | Produce a preliminary layout and list required envelope/mass decisions | Mechanical Intern |
| SCH-010 | Downstream study results change the baseline | Rework of integrated conclusion | Version inputs and outputs; record dependency links and rerun affected checks | Project Lead / Study Owner |

## 7. Acceptance-criteria tracking

Track the specification acceptance criteria AC-001 through AC-016 using the following table. Replace each evidence reference with the actual repository path when available.

| Criterion | Required evidence | Initial disposition | Owner |
|---|---|---|---|
| AC-001 | Requirement-to-evidence mapping | NOT_STARTED | Mechanical Intern |
| AC-002 | Input provenance and status audit | NOT_STARTED | Mechanical Intern |
| AC-003 | Gravity torque and load-case calculations | NOT_STARTED | Mechanical Intern |
| AC-004 | Ratio calculations and operating-point consistency | NOT_STARTED | Mechanical Intern |
| AC-005 | Candidate datasheets and source register | NOT_STARTED | Mechanical Intern |
| AC-006 | Shaft/bearing interface assessment | NOT_STARTED | Mechanical Intern |
| AC-007 | Shaft, bearing and stop checks plus independent review | NOT_STARTED | Mechanical Intern / Independent Reviewer TBD |
| AC-008 | Stop-energy/impact model and assumptions | NOT_STARTED | Mechanical Intern / Independent Reviewer TBD |
| AC-009 | Electrical/thermal input gap assessment | NOT_STARTED | Embedded Intern |
| AC-010 | Packaging/interface evidence | NOT_STARTED | Mechanical Intern |
| AC-011 | BOM/cost estimate and budget comparison | NOT_STARTED | Mechanical Intern |
| AC-012 | Sensitivity analysis and risk register | NOT_STARTED | Mechanical Intern |
| AC-013 | Reproducible calculations and source revisions | NOT_STARTED | Mechanical Intern |
| AC-014 | Deliverable inventory and applicability decisions | NOT_STARTED | Mechanical Intern |
| AC-015 | Independent-review evidence | NOT_STARTED | Project Lead / Independent Reviewer TBD |
| AC-016 | Integrated conclusion and limitations | NOT_STARTED | Mechanical Intern / Project Lead |

Initial status is `NOT_STARTED` for every criterion. Allowed values are the verification values in standard v0.4 section 15.4. Update the table only when supporting evidence or a justified disposition exists.

> Note: the second column is a short evidence/check label only; the criterion wording in `SPECIFICATION.md` governs. The labels were reconciled against the AC-001..016 titles in `SPECIFICATION.md` on 2026-10-24 (all sixteen match).

## 8. Status-tracking table

Use `Day 1` through `Day 10` for planned start and end. Do not enter calendar dates until the schedule is authorized.

| wp_id | task | owner | planned_start | planned_end | status | evidence_path |
|---|---|---|---|---|---|---|
| WP-01 | Reconcile requirements and inputs | Mechanical Intern | Day 1 | Day 1 | NOT_STARTED | |
| WP-01 | Create requirement-to-evidence mapping | Mechanical Intern | Day 1 | Day 1 | NOT_STARTED | |
| WP-01 | Record baseline discrepancies and open questions | Mechanical Intern | Day 1 | Day 1 | NOT_STARTED | |
| WP-02 | Recalculate gravity holding torque | Mechanical Intern | Day 2 | Day 2 | NOT_STARTED | |
| WP-02 | Establish static, dynamic and impact load cases | Mechanical Intern | Day 2 | Day 2 | NOT_STARTED | |
| WP-02 | Identify sensitivity and missing load inputs | Mechanical Intern | Day 2 | Day 2 | NOT_STARTED | |
| WP-03 | Calculate 15:1, 20:1 and 25:1 operating points | Mechanical Intern | Day 3 | Day 3 | NOT_STARTED | |
| WP-03 | Review motor/gearbox candidate evidence | Mechanical Intern / Embedded Intern | Day 3 | Day 4 | NOT_STARTED | |
| WP-03 | Check continuous/peak ratings and power consistency | Mechanical Intern | Day 4 | Day 4 | NOT_STARTED | |
| WP-04 | Reconcile shaft and bearing-seat interfaces | Mechanical Intern | Day 5 | Day 5 | NOT_STARTED | |
| WP-04 | Retrieve and check shaft-strength evidence | Mechanical Intern | Day 5 | Day 6 | NOT_STARTED | |
| WP-04 | Review stop-impact assumptions and prepare review package | Mechanical Intern | Day 6 | Day 6 | NOT_STARTED | |
| WP-04 | Independently review safety-critical calculations | Independent Reviewer TBD | Day 6 | Day 10 | NOT_STARTED | |
| WP-05 | Compile electrical and thermal input requirements | Embedded Intern | Day 7 | Day 7 | NOT_STARTED | |
| WP-05 | Review encoder alignment and interface constraints | Mechanical Intern / Embedded Intern | Day 7 | Day 7 | NOT_STARTED | |
| WP-06 | Prepare preliminary layout/CAD evidence | Mechanical Intern | Day 8 | Day 8 | NOT_STARTED | |
| WP-06 | Prepare BOM/cost estimate and budget comparison | Mechanical Intern | Day 8 | Day 8 | NOT_STARTED | |
| WP-07 | Consolidate risks, sensitivity and acceptance criteria | Mechanical Intern | Day 9 | Day 9 | NOT_STARTED | |
| WP-07 | Prepare integrated conclusion and review package | Mechanical Intern | Day 9 | Day 10 | NOT_STARTED | |
| WP-07 | Review final disposition and follow-on actions | Project Lead | Day 10 | Day 10 | NOT_STARTED | |

### 8.1 Status update rules

- `NOT_STARTED`: work has not begun.
- `IN_PROGRESS`: work is active.
- `BLOCKED`: work cannot proceed because a required input, decision, resource or review is unavailable.
- `DONE`: the task's exit criteria are satisfied and the evidence path is recorded.

For safety-critical tasks, `DONE` may mean that the assigned calculation or review package has been prepared; it does not mean the technical check is verified unless the required independent review and acceptance are complete.

## 9. Handoff requirements

At the end of the planned execution window, the study owner shall ensure:

1. `README.md` provides navigation and reproduction instructions.
2. `SPECIFICATION.md` reflects the approved or proposed scope and acceptance basis accurately.
3. `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` identifies unresolved inputs and their impacts.
4. `REVIEW.md` records findings, decision and independent-review status.
5. Calculation and comparison outputs identify source inputs and revisions.
6. Conditional deliverables have explicit applicability decisions.
7. The cost estimate clearly states its basis and limitations.
8. Safety-critical items without required independent review remain `NOT_VERIFIED`.
9. Follow-on work is linked to FS-M-002 through FS-M-010 where applicable.
10. The final feasibility category, verification status and lifecycle status are consistent with the evidence.

The ten-day target does not override any of these requirements.
