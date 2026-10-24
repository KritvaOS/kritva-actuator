---
study_id: <FS-PRODUCT-NNN>
title: "<Study title>"
product: <Kritva-S | Kritva-M | Kritva-L | Kritva-System>
version: <0.1>
status: <PROPOSED | APPROVED>
lifecycle: <PROPOSED | APPROVED_TO_START | IN_PROGRESS | BLOCKED | SUBMITTED_FOR_REVIEW | REWORK_REQUIRED | ACCEPTED | CLOSED | CANCELLED>
owner: <Name or role>
reviewer: <Name or role>
---

# <Study ID> — <Study Title>

## 1. Purpose

<Describe the purpose of this feasibility study and the engineering problem it addresses.>

This specification defines the scope, required analysis, evidence, deliverables, schedule, and acceptance criteria for the study.

The study shall follow the canonical methodology defined in [FEASIBILITY_METHODOLOGY.md](FEASIBILITY_METHODOLOGY.md) (in `docs/engineering/feasibility/common/`); use the repository-relative path from the study directory when linking.

## 2. Engineering Question and Decision Supported

### 2.1 Engineering question

<State the specific engineering question that this study must answer.>

### 2.2 Decision supported

<Describe the engineering decision that the results are intended to support, such as selecting a component, establishing feasibility, choosing between alternatives, or determining whether further analysis is required.>

### 2.3 Decision boundaries

Identify what the study can establish and what remains outside its authority.

- **Decisions this study can support:** <List decisions.>
- **Decisions this study cannot authorize:** <List design approvals, requirement changes, safety approvals, or other decisions requiring separate authorization.>
- **Required decision authority:** <Name or role authorized to make the resulting engineering decision.>

## 3. Background and Motivation

<Describe the engineering context, current design approach, known constraints, prior findings, and reason for conducting the study.>

Identify relevant canonical documents and prior studies by linking to their authoritative locations.

Do not duplicate existing requirements, standards, design baselines, or accepted engineering decisions in this section.

## 4. Scope and Exclusions

### 4.1 In scope

- <Technical investigation 1>
- <Technical investigation 2>
- <Technical investigation 3>
- <Additional investigation, as applicable>

### 4.2 Out of scope

- <Excluded activity 1>
- <Excluded activity 2>
- <Excluded activity 3>

### 4.3 Constraints

- <Performance constraints>
- <Mechanical and electrical constraints>
- <Cost, schedule, manufacturing, or environmental constraints>
- <Applicable standards and design constraints>

Constraints shall be linked to their canonical sources wherever those sources exist.

## 5. Applicable Requirements

List all requirements that materially constrain the study or define its acceptance targets.

System requirements shall be referenced using their canonical `SYS-REQ-nnn` IDs from `requirements/SYSTEM_REQUIREMENTS.md`.

| Requirement ID | Canonical link | Status label | Applicability and interpretation |
|---|---|---|---|
| <SYS-REQ-nnn> | `<Requirement title>: <canonical repository-relative link>` | <APPROVED/PRELIMINARY/ASSUMED/UNKNOWN/MEASURED> | <Explain applicability to this study.> |
| <SYS-REQ-nnn> | `<Requirement title>: <canonical repository-relative link>` | <APPROVED/PRELIMINARY/ASSUMED/UNKNOWN/MEASURED> | <Explain applicability to this study.> |

Rules:

1. Use the actual requirement ID and canonical link. Do not invent requirement IDs.
2. Do not copy complete requirement text into the study specification.
3. Use the status label to describe the input's current status, not the verification result.
4. Record ambiguous, conflicting, or missing requirements in `ASSUMPTIONS_AND_OPEN_QUESTIONS.md`.
5. Identify the requirement baseline revision or commit used, where available.

If no applicable system requirement has been identified, state that explicitly and explain how the study's engineering constraints and acceptance criteria will be established.

## 6. Inputs and Baseline Data

List the inputs needed to execute the study.

| Input ID | Parameter or artefact | Value and unit | Status label | Source or canonical link | Notes and limitations |
|---|---|---|---|---|---|
| <IN-001> | <Parameter or artefact> | <Value and unit, or TBD> | <APPROVED/PRELIMINARY/ASSUMED/UNKNOWN/MEASURED> | <Source link or reference> | <Conditions, limitations, or rationale> |
| <IN-002> | <Parameter or artefact> | <Value and unit, or TBD> | <APPROVED/PRELIMINARY/ASSUMED/UNKNOWN/MEASURED> | <Source link or reference> | <Conditions, limitations, or rationale> |

Use the following status labels as defined in `FEASIBILITY_METHODOLOGY.md`:

- `APPROVED` — Formally approved input.
- `PRELIMINARY` — Provisional target or input awaiting confirmation.
- `ASSUMED` — Unverified value adopted for analysis.
- `UNKNOWN` — Value or condition not yet established.
- `MEASURED` — Value supported by traceable measurement evidence.

Rules:

1. Identify the source and units of every material input.
2. Distinguish requirements from assumptions and measured data.
3. Do not silently replace an approved input.
4. Do not present an assumed value as measured or approved.
5. Identify missing inputs that could materially change the study conclusion.
6. Use `inputs/` for study input artefacts and link to canonical sources instead of maintaining duplicate controlled records.

## 7. Assumptions and Open Questions

Record the assumptions and unknowns that could affect the analysis in `ASSUMPTIONS_AND_OPEN_QUESTIONS.md`.

At specification approval, identify the known material items.

| ID | Assumption or open question | Current treatment | Potential impact | Resolution method |
|---|---|---|---|---|
| <AQ-001> | <Description> | <Value, scenario, or TBD> | <Effect on calculations or conclusions> | <Measurement, analysis, clarification, or follow-up study> |
| <AQ-002> | <Description> | <Value, scenario, or TBD> | <Effect on calculations or conclusions> | <Measurement, analysis, clarification, or follow-up study> |

Describe how uncertainty will be bounded or evaluated. If an important unknown prevents a meaningful feasibility conclusion, state that the study may need to conclude `FEASIBILITY_NOT_ESTABLISHED`.

## 8. Technical Tasks

Define the technical work needed to answer the engineering question.

| Task ID | Technical task | Method or approach | Expected result or evidence | Dependencies |
|---|---|---|---|---|
| <TASK-001> | <Task description> | <Calculation, analysis, research, simulation, or test> | <Specific output> | <Prerequisite or None> |
| <TASK-002> | <Task description> | <Calculation, analysis, research, simulation, or test> | <Specific output> | <Prerequisite or None> |
| <TASK-003> | <Task description> | <Calculation, analysis, research, simulation, or test> | <Specific output> | <Prerequisite or None> |

Tasks shall emphasize engineering analysis and evidence generation rather than documentation activity alone.

For each task, define enough detail to establish what must be analyzed, how the result will be evaluated, and what evidence will demonstrate completion.

## 9. Required Technical Evidence

Specify the evidence needed to support the study conclusion.

| Evidence ID | Required evidence | Source or method | Acceptance condition | Output location |
|---|---|---|---|---|
| <EV-001> | <Calculation, datasheet, measurement, comparison, or other evidence> | <Method and source requirements> | <What makes the evidence adequate> | <Path under inputs/, calculations/, or outputs/> |
| <EV-002> | <Calculation, datasheet, measurement, comparison, or other evidence> | <Method and source requirements> | <What makes the evidence adequate> | <Path under inputs/, calculations/, or outputs/> |

Depending on the study scope, required evidence may include:

- Traceable requirements and baseline inputs.
- Reproducible engineering calculations.
- Manufacturer specifications with applicable rating conditions.
- Candidate comparisons.
- Sensitivity and uncertainty analysis.
- Simulation models and results.
- Measurements and test conditions.
- Cost sources and estimation assumptions.
- Risk assessment and proposed mitigations.
- Independent technical review.

Identify which evidence is mandatory for the engineering decision and which evidence is supporting or conditional.

Evidence shall be sufficient to reproduce or independently verify significant conclusions.

## 10. Expected Deliverables

Mark each deliverable as mandatory (`M`) or conditional (`C`).

- [ ] **M** — `SPECIFICATION.md` — Approved study scope and acceptance criteria.
- [ ] **M** — `WORK_PLAN.md` — Tasks, ownership, milestones, and checkpoints.
- [ ] **M** — `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` — Material assumptions and unresolved questions.
- [ ] **M** — `inputs/README.md` — Input inventory, sources, and limitations.
- [ ] **M** — `outputs/README.md` — Output inventory and traceability.
- [ ] **M** — `outputs/FINAL_REPORT.md` — Consolidated technical analysis and recommendation.
- [ ] **M** — `REVIEW.md` — Review findings, disposition, and acceptance record.
- [ ] **C** — `calculations/` — Working calculations, scripts, spreadsheets, and analysis notes, where applicable.
- [ ] **C** — `component_research/` — Candidate component and material research, where applicable.
- [ ] **C** — `references/SOURCE_REGISTER.csv` — Structured source register, where external evidence requires one.
- [ ] **C** — `outputs/calculations_results/` — Final numerical results, where applicable.
- [ ] **C** — `outputs/comparison_tables/` — Candidate comparisons and trade-off matrices, where applicable.
- [ ] **C** — `outputs/plots/` — Technical plots and figures, where applicable.
- [ ] **C** — `outputs/risk_assessment/` — Structured risk register, where applicable.
- [ ] **C** — `outputs/cost_estimate/` — Cost analysis and preliminary BOM, where applicable.
- [ ] **C** — `simulation/` — Simulation artefacts, where applicable.
- [ ] **C** — `CAD/` — CAD models and drawings, where applicable.
- [ ] **C** — `test_data/` — Test procedures, raw measurements, and test analysis, where applicable.
- [ ] **C** — `outputs/FINAL_PRESENTATION.pdf` — Final presentation, if required by the assignment.

Additional study-specific deliverables:

- [ ] <M or C> — <Deliverable description and canonical path>
- [ ] <M or C> — <Deliverable description and canonical path>

Rules:

1. `M` means mandatory for this study.
2. `C` means required only when applicable or explicitly selected in this specification.
3. Conditional deliverables that are not applicable shall be marked `N/A` with a brief rationale when their applicability is material to the study.
4. Do not create empty directories to satisfy a checklist.
5. Do not mark a deliverable complete solely because a file exists.

## 11. Study-Specific Acceptance Criteria

Define measurable or objectively reviewable criteria for accepting this study.

| Criterion ID | Acceptance criterion | Verification method | Required evidence | Responsible reviewer |
|---|---|---|---|---|
| <AC-001> | <Specific engineering acceptance condition> | <Calculation, inspection, comparison, test, or review> | <Evidence path or source> | <Reviewer role> |
| <AC-002> | <Specific engineering acceptance condition> | <Calculation, inspection, comparison, test, or review> | <Evidence path or source> | <Reviewer role> |
| <AC-003> | <Specific engineering acceptance condition> | <Calculation, inspection, comparison, test, or review> | <Evidence path or source> | <Reviewer role> |

Acceptance criteria shall:

1. Address the engineering question stated in Section 2.
2. Identify the applicable requirements and operating conditions.
3. Define the evidence needed to demonstrate satisfaction.
4. Identify checks that cannot be completed because of missing information.
5. Distinguish study acceptance from production readiness or formal safety approval.

A criterion shall not be considered satisfied merely because an analysis has been attempted. Its defined acceptance condition must be demonstrated by adequate evidence.

## 12. Dependencies

### 12.1 Prerequisite studies and artefacts

| Dependency ID | Study or artefact | Canonical link | Required information | Dependency status |
|---|---|---|---|---|
| <DEP-001> | <Study, requirement, standard, or other artefact> | <Canonical link> | <Input or decision required> | <Status> |
| <DEP-002> | <Study, requirement, standard, or other artefact> | <Canonical link> | <Input or decision required> | <Status> |

### 12.2 Downstream dependencies

Identify studies or decisions that may rely on the results of this study.

- <Dependent study or decision>
- <Dependent study or decision>

Record cross-study dependencies in the authoritative `registers/CROSS_STUDY_DEPENDENCIES.csv`.

If a prerequisite is unavailable, identify whether work can proceed using an explicitly bounded assumption or must remain blocked.

## 13. Schedule and Review Checkpoints

Define the planned duration, milestones, and review points.

| Milestone ID | Milestone | Planned date or relative day | Expected evidence | Review responsibility |
|---|---|---|---|---|
| <MS-001> | Study kickoff and input confirmation | <Date or day> | <Confirmed scope and input baseline> | <Role> |
| <MS-002> | Initial analysis checkpoint | <Date or day> | <Preliminary calculations and open issues> | <Role> |
| <MS-003> | Technical review checkpoint | <Date or day> | <Interim results and risk assessment> | <Role> |
| <MS-004> | Final submission | <Date or day> | <Required deliverables completed> | <Role> |
| <MS-005> | Acceptance review | <Date or day> | <Review findings and decision> | <Authorized reviewer> |

Record detailed task scheduling and progress in `WORK_PLAN.md`.

If a milestone depends on an unknown input, identify the dependency and the action needed to resolve it.

## 14. Roles and Responsibilities

| Role | Assigned person or role | Responsibility |
|---|---|---|
| Study owner | <Name or role> | Conducts the analysis, maintains traceability, and produces deliverables. |
| Technical reviewer | <Name or role> | Reviews methods, calculations, evidence, and conclusions. |
| Independent safety-critical reviewer | <Name or role, or TBD if not applicable> | Independently reviews safety-critical work when required. |
| Engineering approver | <Name or authorized role> | Accepts or rejects the study and authorizes applicable engineering decisions. |
| Supporting contributor | <Name or role, if applicable> | Provides specialist analysis or supporting evidence. |

The author shall not approve their own safety-critical work.

If the required independent review has not been completed, the verification status shall remain `NOT_VERIFIED`.

A reviewer or approver shall be authorized and technically competent for the work being reviewed. Where a required reviewer has not been assigned, record the gap and resolve it before the affected approval.

## 15. Safety and Risk Notes

Identify safety considerations relevant to the study.

- **Safety-critical scope:** <Yes / No / To be determined, with rationale>
- **Applicable safety process or standard:** <Canonical link or TBD>
- **Known hazards:** <List or link to the authoritative hazard record>
- **Potential consequences of failure:** <Description>
- **Required controls:** <Engineering, procedural, testing, or review controls>
- **Prohibited activities or test conditions:** <Specify, or state None identified>
- **Independent review requirement:** <Describe the required review>

Use the shared likelihood and severity scales defined in `FEASIBILITY_METHODOLOGY.md` when a structured risk assessment is appropriate.

Record material study risks in the designated risk-assessment output or in `FINAL_REPORT.md` when a separate register is not warranted.

Do not treat an unresolved safety-critical risk as accepted merely because the study is preliminary.

## 16. Feasibility Conclusion and Verification Status

These fields shall be completed in the final study report and review record. Their presence in this template does not constitute a conclusion or approval.

### 16.1 Feasibility conclusion

**Initial status:** `NOT_ASSESSED`

**Final conclusion:** <PROMISING | PROMISING_WITH_CONDITIONS | FEASIBILITY_NOT_ESTABLISHED | POTENTIALLY_INFEASIBLE>

**Evidence-based rationale:** <Summarize the decisive evidence and limitations.>

**Conditions and unresolved issues:** <List required actions, missing evidence, and dependencies.>

**Recommended next decision:** <Proceed, proceed with conditions, obtain further evidence, perform a focused study, or reconsider the approach.>

### 16.2 Verification status

**Initial verification status:** `NOT_STARTED`

**Final verification status:** <NOT_STARTED | IN_PROGRESS | PASS | PASS_WITH_ACTIONS | FAIL | NOT_VERIFIED>

**Verification evidence:** <Link to the evidence demonstrating the applicable acceptance criteria.>

**Independent review status:** <Not required with rationale | Pending | Completed, with reviewer and reviewed revision>

**Reviewer decision:** <Pending | Accepted | Rework required | Rejected>

The verification status shall reflect the actual evidence and review state.

- `NOT_STARTED` — Verification has not begun.
- `IN_PROGRESS` — Verification is underway.
- `PASS` — Defined verification criteria have been satisfied with adequate evidence and required review.
- `PASS_WITH_ACTIONS` — Criteria are satisfied subject to documented, authorized follow-up actions that do not invalidate acceptance.
- `FAIL` — Evidence demonstrates that one or more applicable criteria are not satisfied.
- `NOT_VERIFIED` — Verification cannot be established because evidence, conditions, or required review are missing or insufficient.

The feasibility conclusion and verification status are independent. A promising conclusion does not imply a verification pass.

## 17. Specification Approval

Complete this section before the study is authorized to start.

| Approval item | Value |
|---|---|
| Specification version reviewed | <Version> |
| Study owner | <Name or role> |
| Technical reviewer | <Name or role> |
| Engineering approver | <Name or role> |
| Approval decision | <Pending / Approved to Start / Rework Required / Rejected> |
| Approval date | <YYYY-MM-DD or TBD> |
| Approval evidence | <Canonical record, review link, or commit reference> |

Approval of this specification authorizes the defined study work only. It does not approve the final design, accept unresolved risks, or authorize changes to controlled requirements.

**End of Specification Template**
