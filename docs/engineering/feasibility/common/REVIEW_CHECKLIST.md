# Kritva Actuator Feasibility Studies — Review Checklist

**Document ID:** KRITVA-ENG-FS-REVIEW-CHK-001  
**Version:** 0.1  
**Status:** Proposed  
**Applies to:** Kritva-S, Kritva-M, Kritva-L and system-level actuator feasibility studies  
**Canonical location:** `docs/engineering/feasibility/common/REVIEW_CHECKLIST.md`

---

## 1. Purpose

Use this checklist to review feasibility-study scope, engineering correctness, evidence quality, risk, reproducibility and repository hygiene.

Study-specific acceptance criteria and applicable requirements take precedence over this generic checklist. Mark each item:

- `[x]` Satisfied with supporting evidence.
- `[ ]` Not satisfied, not checked or evidence missing.
- `N/A` Not applicable, with a brief justification in `REVIEW.md`.

A checked item should have a traceable basis. A completed checklist alone does not establish feasibility or authorize release.

## 2. Scope and requirements traceability

- [ ] The study ID, title, product variant and engineering question are clear.
- [ ] Scope and exclusions are explicitly documented.
- [ ] Applicable requirements reference canonical `SYS-REQ-nnn` identifiers.
- [ ] Requirements have not been duplicated or silently redefined.
- [ ] Each applicable requirement is linked to analysis, evidence or a documented disposition.
- [ ] Study-specific acceptance criteria are measurable and appropriate.
- [ ] Interfaces and dependencies on other studies are identified.
- [ ] Changes to scope or acceptance criteria are documented and reviewed.

**Reviewer notes / evidence:**

-

## 3. Inputs and status labels

- [ ] Material inputs have identifiable sources and explicit units.
- [ ] Inputs are classified appropriately as `APPROVED`, `PRELIMINARY`, `ASSUMED`, `UNKNOWN` or `MEASURED`.
- [ ] Preliminary targets are not presented as approved requirements.
- [ ] Assumptions and unresolved questions are recorded in `ASSUMPTIONS_AND_OPEN_QUESTIONS.md`.
- [ ] Input tolerances, operating conditions and applicable ranges are captured where relevant.
- [ ] Missing values are not silently replaced with zero or arbitrary defaults.
- [ ] Conflicting inputs are identified and resolved or explicitly bounded.
- [ ] Input revisions match those used in the reported results.

**Reviewer notes / evidence:**

-

## 4. Calculation correctness

- [ ] Calculation purpose, inputs, units, method, assumptions and version are documented.
- [ ] Equations are correct for the physical model and operating conditions.
- [ ] Dimensional consistency and unit conversions have been checked.
- [ ] Boundary conditions, signs, coordinate conventions and loading directions are correct.
- [ ] Relevant worst-case or limiting operating conditions are evaluated.
- [ ] Intermediate values and final results are plausible.
- [ ] Sanity checks are documented, including order-of-magnitude checks where appropriate.
- [ ] A material calculation has an independent hand check or equivalent independent verification appropriate to its risk.
- [ ] Calculation scripts or spreadsheets do not silently hide errors, invalid inputs or failed cases.
- [ ] Rounding and numerical precision do not change the acceptance outcome.
- [ ] Reported results can be traced to the calculation source and exact input revision.

For mechanical studies, consider the applicable checks for torque, speed, power, stress, deflection, fatigue, bearing life, thermal loading and duty cycle.

For electrical and thermal studies, consider voltage, current, power loss, driver limits, wiring, protection and thermal equilibrium.

**Reviewer notes / evidence:**

-

## 5. Evidence and sources

- [ ] Material claims are supported by traceable sources or clearly identified assumptions.
- [ ] The source register identifies the document, revision, source location and applicable claim.
- [ ] Datasheet values are used within the stated operating conditions.
- [ ] Continuous, intermittent and peak ratings are distinguished.
- [ ] Peak ratings include applicable duration, duty cycle, repetition and thermal conditions.
- [ ] Torque-speed, power, current and efficiency data are interpreted consistently.
- [ ] Gearbox ratings distinguish continuous output torque, peak torque, speed, efficiency and service-life conditions where applicable.
- [ ] Motor, gearbox, bearing and encoder interfaces are compatible with the intended application.
- [ ] Manufacturer claims are not treated as independently verified test results.
- [ ] Measurements identify test setup, conditions, equipment and calibration status where relevant.
- [ ] Simulation evidence identifies model assumptions, configuration and convergence status.
- [ ] Source limitations and unavailable information are disclosed.

**Reviewer notes / evidence:**

-

## 6. Sensitivity and uncertainty

- [ ] Material uncertain inputs are identified.
- [ ] Sensitivity analysis or a justified alternative is used where uncertainty may change the conclusion.
- [ ] Worst-case, nominal and relevant operating scenarios are distinguished.
- [ ] Duty-cycle uncertainty is considered where it affects thermal performance or life.
- [ ] Mass properties, centre of mass, geometry, tolerances and efficiency assumptions are considered where relevant.
- [ ] Uncertainty is not hidden by excessive numerical precision.
- [ ] The conclusion identifies assumptions that could reverse a candidate ranking or acceptance result.
- [ ] Additional measurements or analysis are identified where uncertainty remains decision-critical.

**Reviewer notes / evidence:**

-

## 7. Risk assessment

- [ ] Relevant technical, safety, reliability, manufacturing, sourcing and schedule risks are recorded.
- [ ] Risk causes, events and consequences are distinguishable.
- [ ] Likelihood and severity ratings follow the applicable risk policy.
- [ ] Risk scores and bands are calculated consistently.
- [ ] Existing controls are distinguished from proposed mitigations.
- [ ] Mitigation actions have owners and target dates where required.
- [ ] Residual risk is assessed after considering evidenced controls.
- [ ] High-consequence failure modes are not dismissed solely because of a low numerical score.
- [ ] Safety-critical risks have the required independent review and disposition.
- [ ] Open risks and their effects on the conclusion are visible.

**Reviewer notes / evidence:**

-

## 8. Conclusion category and verification status consistency

- [ ] The conclusion directly answers the engineering question.
- [ ] The selected feasibility category is supported by the evidence and acceptance criteria.
- [ ] Limitations, dependencies and unresolved assumptions are stated.
- [ ] The conclusion does not imply release approval or production readiness without the required evidence.
- [ ] The verification status is consistent with the work actually completed.
- [ ] `PASS` is used only when applicable criteria have been met and required evidence is available.
- [ ] `PASS_WITH_ACTIONS` identifies the outstanding actions and their ownership; it is not used to bypass mandatory safety or acceptance gates.
- [ ] `FAIL` is used when applicable criteria are demonstrably not met.
- [ ] `NOT_VERIFIED` is used when evidence or required verification is insufficient.
- [ ] Lifecycle status and verification status are recorded separately.

Use the feasibility categories defined in `FEASIBILITY_STUDIES_STANDARD.md`:

- `PROMISING`
- `PROMISING_WITH_CONDITIONS`
- `FEASIBILITY_NOT_ESTABLISHED`
- `POTENTIALLY_INFEASIBLE`

Use only these verification status values:

- `NOT_STARTED`
- `IN_PROGRESS`
- `PASS`
- `PASS_WITH_ACTIONS`
- `FAIL`
- `NOT_VERIFIED`

**Reviewer notes / evidence:**

-

## 9. Independent review for safety-critical work

- [ ] Safety-critical calculations, assumptions and conclusions are identified.
- [ ] The required independent reviewer is assigned and competent for the review scope.
- [ ] The author has not approved their own safety-critical work.
- [ ] The reviewer examined the underlying evidence, not only the executive summary.
- [ ] Review findings and closure evidence are recorded.
- [ ] Residual risks have the required authorization.
- [ ] Required safety gates and approvals are explicitly checked.
- [ ] Missing independent review is reflected as `NOT_VERIFIED` for the affected verification.

**Mandatory rule:** If required independent review has not occurred, the affected safety-critical work must not be represented as independently verified or approved. A missing review cannot be waived by checking this checklist.

**Reviewer notes / evidence:**

-

## 10. Deliverables completeness

- [ ] `README.md` provides navigation, status, results and reproduction instructions.
- [ ] `SPECIFICATION.md` contains the scope, requirements, inputs and acceptance criteria.
- [ ] `WORK_PLAN.md` reflects the actual work and links to evidence.
- [ ] `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` has current dispositions.
- [ ] `REVIEW.md` contains the review record and decision.
- [ ] Applicable evidence directories and their READMEs are present.
- [ ] All M deliverables are complete.
- [ ] All applicable C deliverables are complete.
- [ ] Every N/A conditional deliverable has a recorded justification.
- [ ] Required CSV files use the schemas in `DELIVERABLES_STANDARD.md`.
- [ ] Results, plots, comparison tables and cost estimates have traceable inputs and units.
- [ ] Study-specific Definition of Done items are satisfied or explicitly dispositioned.

**Reviewer notes / evidence:**

-

## 11. Repository hygiene

- [ ] File and directory names follow the feasibility-study conventions.
- [ ] Internal links and requirement references resolve correctly.
- [ ] The study does not duplicate canonical requirements or registers unnecessarily.
- [ ] Calculation scripts, models and output data are clearly distinguished.
- [ ] Source revisions and material tool versions are recorded.
- [ ] Reproduction instructions are practical and complete.
- [ ] Generated results correspond to the reviewed source revision.
- [ ] No credentials, tokens, passwords or other secrets are committed.
- [ ] Temporary files, caches and unrelated generated artefacts are excluded.
- [ ] Large external artefacts have stable references and integrity information where practical.
- [ ] Changes are traceable through version control.
- [ ] Any exceptions to this standard are documented and approved as required.

**Reviewer notes / evidence:**

-

## 12. Findings severity scale

Assign each finding a severity based on its consequence and effect on the study decision.

| Severity | Definition | Expected disposition |
|---|---|---|
| Critical | Potential serious safety hazard, invalidates a safety-critical conclusion, or reveals a fundamental failure that makes acceptance unsafe or indefensible | Stop acceptance; escalate immediately; resolve and independently review before acceptance |
| High | Material calculation, requirement, evidence or design issue that could change the feasibility conclusion or violate an important acceptance criterion | Rework and verify closure before acceptance, unless a formally authorized process explicitly permits a different disposition without bypassing mandatory gates |
| Medium | Significant weakness or missing evidence that reduces confidence, traceability or completeness but is not currently shown to invalidate the conclusion | Correct before acceptance, or record an explicitly approved action with owner, due date and impact assessment |
| Low | Limited defect with minor impact on interpretation, maintainability or documentation quality | Correct as agreed; document any accepted residual action |
| Observation | Improvement suggestion or noteworthy point that is not a demonstrated defect | Record for consideration; no mandatory correction unless accepted as an action |

Severity is not a substitute for risk assessment. A finding involving a mandatory safety review, legal obligation or approved requirement remains a blocker even if someone assigns it a low severity.

Each finding must have a unique ID, description, severity, evidence reference, required action, owner, status and closure evidence where applicable.

## 13. Review decision table

Use the following decision values in `REVIEW.md`. The decision applies to the reviewed study revision.

| Decision | Entry criteria | Required next step |
|---|---|---|
| `PENDING` | Review has not started, is incomplete, or required evidence/reviewers are still outstanding | Continue review or obtain missing evidence; do not treat as accepted |
| `REWORK_REQUIRED` | One or more findings require correction or additional evidence before acceptance | Assign actions, update affected artefacts, and submit the revised study for review |
| `ACCEPTED` | Applicable acceptance criteria are satisfied; mandatory deliverables are complete; findings are closed or have an explicitly authorized disposition; required independent reviews are complete | Record reviewer approval and the exact reviewed revision; update study status through the established process |
| `REJECTED` | The submission is fundamentally unsuitable for acceptance, the conclusion is unsupported, or the approach fails required criteria and cannot be accepted in its current form | Record the rationale and required next decision, such as redesign, rescope or cancellation |

### 13.1 Decision rules

1. A new or unreviewed submission starts at `PENDING`.
2. `REWORK_REQUIRED` means a revised submission is expected.
3. `REJECTED` is a formal negative decision on the reviewed submission; it does not automatically mean the engineering concept is permanently infeasible.
4. `ACCEPTED` means the study deliverables meet their acceptance basis. It does not automatically approve the actuator for production or release.
5. Critical findings prevent acceptance.
6. High findings normally prevent acceptance and require documented closure. Any exception must be explicitly authorized and must not bypass safety, legal or approved requirement gates.
7. Open findings cannot be hidden by changing the review decision.
8. A revised submission must identify the changed revision and the findings addressed.
9. The study verification status and lifecycle must be consistent with the review decision.
10. If required independent safety review is missing, the affected work remains `NOT_VERIFIED` and the study cannot be accepted where that review is an acceptance prerequisite.

## 14. `REVIEW.md` record skeleton

Copy the following structure into the study's `REVIEW.md` and complete it for each formal review. Keep the review history traceable; do not overwrite earlier decisions without retaining the record.

```markdown
# Feasibility Study Review

Study ID: FS-<PRODUCT>-<NNN>
Study title: <Title>
Product: <Kritva-S | Kritva-M | Kritva-L | Kritva-System>
Reviewed version: <Version>
Reviewed commit or revision: <Commit or immutable revision>
Review date: <YYYY-MM-DD>
Author: <Name or role>
Reviewer: <Name or role>
Review type: <Technical | Safety | Independent calculation | Deliverables | Final acceptance>

## 1. Review scope

- Engineering question:
- Applicable requirements:
- Acceptance criteria:
- Artefacts reviewed:
- Exclusions or limitations:

## 2. Checklist results

- Scope and requirements traceability: <SATISFIED | FINDINGS | N/A>
- Inputs and status labels: <SATISFIED | FINDINGS | N/A>
- Calculation correctness: <SATISFIED | FINDINGS | N/A>
- Evidence and sources: <SATISFIED | FINDINGS | N/A>
- Sensitivity and uncertainty: <SATISFIED | FINDINGS | N/A>
- Risk assessment: <SATISFIED | FINDINGS | N/A>
- Conclusion and verification consistency: <SATISFIED | FINDINGS | N/A>
- Independent safety review: <COMPLETE | REQUIRED | NOT_APPLICABLE>
- Deliverables completeness: <SATISFIED | FINDINGS | N/A>
- Repository hygiene: <SATISFIED | FINDINGS | N/A>

## 3. Findings

| Finding ID | Severity | Description | Evidence reference | Required action | Owner | Due date | Status | Closure evidence |
|---|---|---|---|---|---|---|---|---|
| REV-001 | <Critical/High/Medium/Low/Observation> | <Description> | <Path or reference> | <Action> | <Owner> | <YYYY-MM-DD or N/A> | <Open/Closed> | <Evidence or N/A> |

If there are no findings, state: No findings identified for this review scope.

## 4. Independent review

- Safety-critical work in scope: <YES | NO>
- Independent reviewer required: <YES | NO>
- Independent reviewer completed review: <YES | NO | N/A>
- Independence confirmed: <YES | NO | N/A>
- Safety-gate references:
- Remaining safety concerns:
- Evidence or approval reference:

## 5. Technical assessment

- Calculation and unit-check summary:
- Independent hand-check or equivalent:
- Evidence quality and source limitations:
- Sensitivity and uncertainty:
- Risk assessment:
- Feasibility conclusion assessment:
- Outstanding assumptions and dependencies:

## 6. Decision

Review decision: <PENDING | REWORK_REQUIRED | ACCEPTED | REJECTED>

Feasibility category: <PROMISING | PROMISING_WITH_CONDITIONS | FEASIBILITY_NOT_ESTABLISHED | POTENTIALLY_INFEASIBLE | NOT_YET_ASSESSED>

Verification status: <NOT_STARTED | IN_PROGRESS | PASS | PASS_WITH_ACTIONS | FAIL | NOT_VERIFIED>

Lifecycle status: <PROPOSED | APPROVED_TO_START | IN_PROGRESS | BLOCKED | SUBMITTED_FOR_REVIEW | REWORK_REQUIRED | ACCEPTED | CLOSED | CANCELLED>

Decision rationale:
<Explain how the evidence and findings support the decision.>

Conditions or remaining actions:
<List authorized actions, owners and due dates, or state none.>

Restrictions on use:
<Identify any restriction on design selection, fabrication, testing, integration or release.>

## 7. Approval record

Reviewer: <Name or role>
Decision date: <YYYY-MM-DD>
Approval reference: <Commit, approval record or N/A>
Follow-up review required: <YES | NO>
Next review trigger: <Condition or N/A>
```

## 15. Final reviewer reminder

The purpose of this review is to determine whether the study's engineering question has been answered with evidence appropriate to the decision and risk.

Do not accept a study merely because its documents are complete, its calculations execute successfully, its plots look plausible or its author recommends acceptance. The evidence, assumptions, acceptance criteria, independent-review requirements and conclusion must be consistent.

**Document status:** Proposed. Apply alongside the governing feasibility-study standard and deliverables standard; obtain the required project approval before treating this checklist as an approved mandatory policy.
