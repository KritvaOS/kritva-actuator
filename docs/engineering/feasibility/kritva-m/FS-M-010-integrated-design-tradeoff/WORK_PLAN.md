---
study_id: FS-M-010
title: Integrated Design Trade-off and Readiness - Work Plan
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Project Lead
reviewer: Independent Reviewer TBD
priority: P0
upstream: [FS-M-001, FS-M-002, FS-M-003, FS-M-004, FS-M-005, FS-M-006, FS-M-007, FS-M-008, FS-M-009]
downstream: []
specification: SPECIFICATION.md
inputs: inputs/INPUTS.md
assumptions_and_open_questions: ASSUMPTIONS_AND_OPEN_QUESTIONS.md
---

# FS-M-010 Work Plan

## 1. Objective

Integrate the evidence from FS-M-001 through FS-M-009 into a controlled Level-2 Option C design trade-off and readiness assessment. Produce requirement coverage, consistency findings, ratio/candidate comparison, risk roll-up, readiness gates, and recommended A0 planning actions.

This plan is governed by `SPECIFICATION.md`. Acceptance criteria AC-001 through AC-016 below must match the specification in ID and intent. No GO decision is permitted without the required independent review. Initial criterion status is `NOT_STARTED`.

## 2. Roles and decision authority

- **Owner - Project Lead:** control the integration, resolve cross-study issues, establish trade-off criteria, make the readiness recommendation, and record the decision.
- **Reviewer - Independent Reviewer TBD:** independently review the integrated evidence and applicable safety-critical conclusions.
- **Upstream owners:** confirm the accuracy, revision, status, and interpretation of their artifacts.
- **Study contributors:** supply traceable evidence, calculations, and issue dispositions.

The author cannot approve their own safety-critical work. If the Project Lead authors a safety-critical analysis, an independent reviewer must review it. Missing independent review means readiness remains NOT_VERIFIED.

## 3. Work breakdown

| Task | Activity | Evidence / output | Exit condition |
|---|---|---|---|
| WP-01 | Establish evidence baseline | Artifact manifest and input traceability | Exact paths, revisions, units, and review status recorded |
| WP-02 | Define Option C baseline | Architecture and ownership-boundary record | Purchased/in-house boundaries explicit; no unverified part selected |
| WP-03 | Build requirement coverage | Requirement coverage matrix | Evidence, status, gaps, owners, and gates recorded |
| WP-04 | Run consistency audit | Cross-study consistency matrix | Conflicts, missing artifacts, and incompatible assumptions logged |
| WP-05 | Compare ratios | Ratio comparison and sensitivity calculations | 15:1/20:1/25:1 compared with traceable evidence |
| WP-06 | Compare candidate sets | Weighted trade-off matrix | Criteria and weights documented; scores evidence-backed |
| WP-07 | Consolidate risks | Integrated risk register | Source IDs preserved; mitigation and ownership recorded |
| WP-08 | Reconcile cost/manufacturing | Budget and sourcing summary | FS-M-009 evidence and unresolved costs visible |
| WP-09 | Define readiness gates | Gate matrix and proposed disposition | Entry conditions, evidence, exclusions, and decision authority explicit |
| WP-10 | Recommend A0 planning | Action plan with dependencies and owners | Recommendations do not authorize unverified parts or unsafe work |
| WP-11 | Independent review | Review findings and disposition | Reviewer identity, date, revision, and findings recorded |
| WP-12 | Close and publish | Integrated report and evidence index | Status and limitations are traceable; no unsupported GO |

## 4. Required directory structure

Mandatory:

- `calculations/` - reproducible ratio/candidate scoring, weight sensitivity, and quantitative comparisons.
- `outputs/` - requirement coverage, artifact manifest, consistency findings, trade-off results, integrated risk register, readiness gates, and A0 actions.
- `references/SOURCE_REGISTER.csv` - traceable external source register.

Not applicable by default:

- `CAD/` - NOT_APPLICABLE; authoritative mechanical geometry remains in the relevant upstream study.
- `simulation/` - NOT_APPLICABLE unless a justified simulation is required to resolve a specific decision.
- `component_research/` - NOT_APPLICABLE unless new, sourced candidate research is needed.
- `cost_estimate/` - NOT_APPLICABLE as a separate directory when FS-M-009 cost outputs suffice; create only for a justified integrated model.
- `test_data/` - NOT_APPLICABLE for this desk study; validation testing is a separately planned activity.

Record the rationale if a conditional directory is created or applicability changes.

## 5. Work sequence and gates

### Gate A - Evidence integrity

Verify the authoritative FS-M-001 baseline and all relevant FS-M-002 through FS-M-009 artifacts. Record exact path, revision/commit, units, review status, provenance, and limitations. Confirm the verified upstream inputs and statuses listed in `inputs/INPUTS.md`.

Do not infer artifact existence or approval from expected filenames. Missing, stale, conflicting, or unreviewed evidence must be recorded as a blocker.

### Gate B - Architecture and requirement coverage

Document Option C as the evaluation baseline, distinguishing commercial components from in-house elements. Build a requirement coverage matrix with evidence, status, owner, and closure action. Verify requirement wording before describing a requirement beyond its supplied definition.

### Gate C - Cross-study consistency

Compare motor, ratio, gearbox, shaft, bearings, housing, encoder, controller, firmware, thermal paths, manufacturing interfaces, BOM, and cost. Track each discrepancy with source IDs and a resolution owner. Do not silently modify upstream assumptions or interface decisions.

### Gate D - Trade-off analysis

Compare 15:1, 20:1, and 25:1 using the verified operating points and candidate evidence. Establish criteria, weights, scale, and missing-data handling before scoring. Retain raw evidence and weighted contributions. Run weight sensitivity and show when evidence cannot distinguish candidates.

A critical failure or missing safety-critical evidence cannot be hidden by an aggregate score.

### Gate E - Risk and readiness assessment

Roll up upstream risks and open questions, preserving source references. Evaluate GO, CONDITIONAL-GO, and NO-GO entry criteria. Use NOT_VERIFIED as the default until evidence and required review support a disposition.

A conditional-go must name the permitted scope, prerequisites, exclusions, owners, and safeguards. It does not authorize activity beyond that scope.

### Gate F - Independent review and A0 handoff

Submit the integrated evidence revision to the independent reviewer. Record findings and disposition. Prepare the A0 action plan with explicit dependencies and approval gates. Do not select unverified components or imply authorization to procure, fabricate, assemble, or energize.

## 6. Acceptance criteria

Initial status is `NOT_STARTED` for all criteria. Allowed status values are `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `FAIL`, and `BLOCKED`. Change a status only when the evidence supports it.

| AC | Acceptance criterion | Evidence required | Initial status |
|---|---|---|---|
| AC-001 | All consumed FS-M-001 through FS-M-009 inputs and artifacts are traceable by exact path, revision, units, and review status; upstream IDs and statuses are not redefined. | Artifact manifest and input traceability | NOT_STARTED |
| AC-002 | The Option C architecture baseline and its purchased/in-house boundaries are documented, with no unsupported part selection. | Architecture/ownership record | NOT_STARTED |
| AC-003 | A requirement-by-requirement coverage matrix identifies evidence, status, gaps, owners, and readiness-gate relevance. | Requirement coverage matrix | NOT_STARTED |
| AC-004 | Cross-study consistency checks cover motor, gearbox ratio, shaft, bearings, housing, encoder, controller, firmware, thermal paths, interfaces, and cost. | Consistency matrix and issue log | NOT_STARTED |
| AC-005 | The 15:1, 20:1, and 25:1 ratios are compared using verified operating points and explicit assumptions; screening values are not treated as qualification evidence. | Ratio comparison and source links | NOT_STARTED |
| AC-006 | Candidate trade-off criteria, weights, score scale, evidence confidence, and scoring rationale are documented before final ranking. | Trade-off method and scoring rubric | NOT_STARTED |
| AC-007 | Every score and weighted contribution is evidence-backed; unknown data is not assigned a favourable score, and critical failures cannot be masked by aggregation. | Evidence-linked score sheet | NOT_STARTED |
| AC-008 | Score sensitivity and evidence limitations are documented; a winner is not declared if available evidence cannot distinguish candidates defensibly. | Sensitivity analysis and conclusion | NOT_STARTED |
| AC-009 | Integrated risks and open questions preserve source-study IDs, affected requirements, owners, mitigations, and readiness-gate relevance. | Integrated risk register | NOT_STARTED |
| AC-010 | SYS-REQ-091 life-versus-duty, SYS-REQ-092 post-loaded-cycle integrity, and SYS-REQ-014 shock loads are distinguished and correctly traced. | Requirement traceability and validation-gap record | NOT_STARTED |
| AC-011 | Cost and manufacturing conclusions are reconciled with FS-M-009 evidence, SYS-REQ-100 budget scope, sourced prices, and unresolved BOM exposure. | Cost reconciliation and budget status | NOT_STARTED |
| AC-012 | Electrical, thermal, shaft, bearing, and housing conclusions are reconciled with upstream evidence; unsupported performance or safety claims remain NOT_VERIFIED. | Technical consistency and evidence-gap report | NOT_STARTED |
| AC-013 | GO, CONDITIONAL-GO, and NO-GO gates have explicit entry criteria, evidence, conditions, exclusions, and decision authority; default status is NOT_VERIFIED. | Readiness-gate matrix | NOT_STARTED |
| AC-014 | A0 next-phase actions identify prerequisites, owners, dependencies, and review/validation gates without authorizing unverified parts or unsafe activities. | A0 action plan | NOT_STARTED |
| AC-015 | Mandatory calculations, outputs, and source registration are complete; all NOT_APPLICABLE and conditional directories are handled according to this specification. | Deliverable audit and source register | NOT_STARTED |
| AC-016 | Independent review is recorded against the evidence revision; the author cannot approve their own safety-critical work, and no GO decision is issued without required independent review. | Independent review and decision record | NOT_STARTED |

## 7. Trade-off and evidence controls

For every candidate, retain the underlying source evidence, operating conditions, score rationale, weight, weighted contribution, and missing-data status. Document the scoring scale before scoring and ensure weights total 100% where percentages are used.

Use NOT_VERIFIED for attributes lacking adequate evidence. If a critical attribute is a gate, do not replace it with a neutral score that permits an aggregate winner. Report no defensible winner when the evidence does not distinguish candidates.

Any screening calculations using IN-012 must retain its ASSUMED status. Do not elevate preliminary ratio or motor assumptions to approved design facts.

## 8. Readiness and review controls

A GO decision requires all mandatory gates to be satisfied and the required independent review completed. A conditional-go must have a bounded scope, explicit conditions, exclusions, and named owners. A NO-GO requires the blocking failure or risk to be documented.

If the independent reviewer is not assigned, review is incomplete, or safety-critical evidence is insufficient, readiness remains NOT_VERIFIED. Lifecycle status PROPOSED is distinct from the readiness disposition.

The Project Lead shall record the decision date, evidence revision, gate outcomes, conditions, reviewer findings, and unresolved risks.

## 9. Completion checklist

- [ ] Upstream evidence and revisions verified.
- [ ] Option C baseline and ownership boundaries documented.
- [ ] Requirement coverage matrix complete.
- [ ] Cross-study consistency audit complete.
- [ ] Ratio/candidate trade-off is evidence-backed.
- [ ] Score and weight sensitivity documented.
- [ ] Integrated risk register preserves source references.
- [ ] Requirement distinctions and qualification gaps correctly recorded.
- [ ] Cost/manufacturing and electrical/thermal evidence reconciled.
- [ ] Readiness gates and A0 action plan complete.
- [ ] Mandatory deliverables and source register complete.
- [ ] Independent review recorded.
- [ ] Readiness decision and authority documented.
- [ ] No unsupported GO or feasibility claim remains.
