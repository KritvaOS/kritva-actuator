---
study_id: FS-M-010
title: Integrated Design Trade-off and Readiness
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Project Lead
reviewer: Independent Reviewer TBD
priority: P0
upstream: [FS-M-001, FS-M-002, FS-M-003, FS-M-004, FS-M-005, FS-M-006, FS-M-007, FS-M-008, FS-M-009]
downstream: []
---

# FS-M-010 Integrated Design Trade-off and Readiness

## 1. Purpose

Integrate evidence from FS-M-001 through FS-M-009 into a traceable Level-2 design trade-off and readiness assessment for the Kritva-M actuator.

The baseline concept is **Option C**: commercial BLDC motor, commercial planetary gearbox, output encoder, bearings, and in-house housing, shaft, controller, and firmware. This is the architecture to evaluate, not an approved final design or a commitment to specific components.

The study shall establish requirement coverage, cross-study consistency, evidence-backed trade-offs, rolled-up risks, readiness gates, and recommended next-phase actions. It must distinguish demonstrated results from preliminary inputs, assumptions, missing evidence, and decisions awaiting review.

## 2. Scope

- Integrate requirements, inputs, analyses, outputs, assumptions, open questions, and review records across FS-M-001 through FS-M-009.
- Produce a requirement-by-requirement coverage matrix with evidence, status, gaps, owners, and closure actions.
- Check consistency of motor and gearbox candidates, ratios, shaft, bearings, housing, encoder, controller, firmware, thermal paths, interfaces, and costs.
- Compare 15:1, 20:1, and 25:1 gearbox ratios using only verified evidence and explicit evaluation criteria.
- Compare candidate sets using traceable scores and documented evidence confidence; do not invent ratings.
- Consolidate unresolved risks, dependencies, and decisions from upstream studies.
- Evaluate go, conditional-go, and no-go readiness gates with explicit evidence and approval requirements.
- Recommend the next-phase A0 build-planning activities without selecting unverified parts or authorizing fabrication/testing.
- Record independent-review findings and a controlled readiness disposition.

## 3. Out of scope

This study does not independently authorize:

- Production release, procurement, fabrication, assembly, or powered testing.
- A final motor, gearbox, shaft, bearing, encoder, controller, MCU, material, or supplier selection without the required evidence and approval.
- Closure of upstream assumptions or questions without the responsible owner and evidence.
- Claims of shock-load, service-life, thermal, electrical-protection, loaded-cycle, or production-safety compliance based solely on integrated documentation.
- Numerical trade-off scores based on intuition where evidence is absent.
- A readiness GO decision before required independent review and safety-critical gates are satisfied.

## 4. Architecture baseline and authoritative sources

Option C is the architecture under evaluation:

- Commercial BLDC motor.
- Commercial planetary gearbox.
- Output-side encoder.
- Dedicated bearing/support arrangement.
- In-house housing and shaft.
- In-house controller and firmware.

The actual candidates, interfaces, and feasibility remain subject to upstream evidence. No particular part number or supplier is selected by this specification.

### 4.1 Authoritative baseline

FS-M-001 is located at `kritva-m/FS-M-001-integrated-actuator-system/`. Preserve upstream IDs, exact values, units, and statuses. Reference ASM-001 through ASM-012 and OQ-001 through OQ-014 by ID; do not redefine or silently close them.

Only use the following verified upstream inputs as specified here:

| ID | Input | Value/status |
|---|---|---|
| IN-006 | Continuous output torque | >= 10 N·m; PRELIMINARY |
| IN-007 | Peak output torque | 20 N·m minimum / 25 N·m stretch; PRELIMINARY |
| IN-008 | Output speed | 45 RPM; PRELIMINARY |
| IN-009 | Nominal supply | 24 V DC; PRELIMINARY |
| IN-010 | Gearbox ratio set | 15:1, 20:1, 25:1; PRELIMINARY |
| IN-011 | First ratio candidate | 20:1; PRELIMINARY |
| IN-012 | Gearbox efficiency | 85%; ASSUMED |
| IN-013 | Motor power starting range | 75-100 W; PRELIMINARY |
| IN-014 | Motor operating data | UNKNOWN |
| IN-024 | Motor margin | 20%; ASSUMED |
| IN-025 | Gearbox margin | 20%; ASSUMED |
| IN-026 | Duty cycle/continuous holding duration | UNKNOWN |
| IN-028 | Ambient temperature | UNKNOWN |
| IN-029 | Supply current limit | UNKNOWN |
| IN-030 | Service life | UNKNOWN |
| IN-031 | Peak duration/repetition | UNKNOWN |
| IN-034 | Output-side encoder required | PRELIMINARY |
| IN-037 | Shaft material candidates | EN19/42CrMo4 Q&T candidate; EN8 normalised reported strength factor about 0.86; PRELIMINARY |

Verify these values and statuses against the authoritative source records before using them in a final decision. The table is a controlled reference for this study, not authorization to alter upstream records.

### 4.2 Upstream evidence requirements

For FS-M-002 through FS-M-009, record each consumed artifact's exact repository-relative path, revision or commit, units, review status, provenance, and limitations.

Key expected evidence includes:

- FS-M-002: `outputs/LOAD_CASES.csv`, `outputs/DYNAMIC_TORQUE_RESULTS.csv`.
- FS-M-003: candidate motor data and operating points; exact filenames must be verified.
- FS-M-004: `outputs/GEARBOX_CANDIDATE_MATRIX.csv`, `outputs/RATIO_OPTIMIZATION.csv`, `outputs/LOAD_RATING_CHECK.csv`, `outputs/LIFE_RATING_ASSESSMENT.csv`, `outputs/INTERFACE_COMPATIBILITY.csv`.
- FS-M-005: shaft load, strength, impact, deflection, interface, and material-comparison outputs.
- FS-M-006: bearing load, candidate, rating, life, impact, interface-decision, and support-feasibility outputs.
- FS-M-007: `outputs/INTERFACE_REGISTER.csv`, `outputs/MASS_ENVELOPE_STATUS.csv`, `outputs/STRUCTURAL_CHECK.csv`.
- FS-M-008: verified electrical/thermal outputs and source register; exact filenames must be verified.
- FS-M-009: BOM, manufacturing, sourcing, lead-time, and cost outputs; exact filenames must be verified.

Do not treat an expected filename as proof of existence, completeness, or approval. Missing or unreviewed evidence must remain visible.

## 5. Requirements coverage

Create a coverage matrix containing, for each applicable requirement:

- Requirement ID and verified requirement text/reference.
- Relevant upstream study and input/output evidence.
- Evidence revision and review status.
- Status: PASS, FAIL, BLOCKED, NOT_VERIFIED, or NOT_APPLICABLE.
- Remaining gap, owner, and closure action.
- Whether the requirement is a readiness gate.

Include system-level requirements and study-level acceptance criteria where applicable. Avoid inventing requirement text. If detailed wording has not been verified, reference the ID and mark applicability or interpretation for confirmation.

### 5.1 Special requirement distinctions

- SYS-REQ-091 concerns gearbox/bearing life versus duty.
- SYS-REQ-092 concerns post-loaded-cycle integrity: no unacceptable permanent deformation, loosening, bearing damage, or encoder misalignment.
- SYS-REQ-014 is the shock-load requirement, conditional on impacts being in scope; that scope decision is open (upstream OQ-009).

SYS-REQ-092 must not be used as a substitute for SYS-REQ-014. A planned test, calculation, or design intention is not evidence that the associated requirement has passed.

## 6. Cross-study consistency assessment

Evaluate consistency across the studies in at least these areas:

1. **Requirements and inputs:** IDs, values, units, status, assumptions, and open questions.
2. **Motor and gearbox:** candidate identity, motor operating data, ratio, speed, torque, efficiency, ratings, and life.
3. **Shaft and bearings:** output interface, shaft diameter/material, bearing bore and seats, load path, fits, life, impact, and deflection.
4. **Housing and integration:** mounting geometry, structural load path, hard-stop load path, encoder alignment, envelope, and mass.
5. **Electrical and thermal:** bus limits, motor current, controller sizing, feedback, protection, heat generation, thermal paths, and material temperature limits.
6. **Manufacturing and cost:** BOM completeness, component identity, sourcing, manufacturing route, tolerances, inspection, cost scope, and budget.
7. **Evidence integrity:** artifact revisions, source registration, independent reviews, and consistency of status reporting.

Report each finding with affected studies/IDs, evidence pointers, severity, owner, and resolution action. Do not silently resolve discrepancies or change upstream values. In particular, surface unresolved shaft/bearing interface decisions, missing motor data, unverified thermal limits, and unpriced BOM lines.

## 7. Ratio and candidate trade-off

Compare 15:1, 20:1, and 25:1 using verified candidate evidence. Evaluate at least:

- Required motor speed and torque.
- Continuous and peak torque/current feasibility.
- Motor torque-speed and thermal suitability.
- Gearbox torque/speed rating, efficiency, backlash, and life.
- Shaft, bearing, and support loads.
- Housing/envelope and encoder integration.
- Controller/current-sensing requirements.
- Sourcing, lead time, manufacturing complexity, and cost.
- Evidence maturity and unresolved risks.

IN-011 identifies 20:1 as the first candidate, not a final selection. A ratio must not win solely because it is the baseline candidate.

### 7.1 Screening references

At 45 RPM output, the nominal speed calculations are 675 RPM for 15:1, 900 RPM for 20:1, and 1125 RPM for 25:1.

Using the ASSUMED 85% gearbox efficiency, approximate motor torque for 10 N·m output is 0.78, 0.59, and 0.47 N·m for 15:1, 20:1, and 25:1, respectively. For 25 N·m output, the approximate values are 1.96, 1.47, and 1.18 N·m.

These are screening calculations, not evidence that any candidate meets the motor, thermal, gearbox, shaft, bearing, or controller constraints. Reconcile them with FS-M-002 through FS-M-008 before assigning scores.

### 7.2 Scoring rules

Define criteria, weights, scoring scale, and evidence-confidence rules before scoring. Weights must sum to 100% if percentage weighting is used. Score only evidence-backed attributes. For missing evidence, use NOT_VERIFIED or an explicitly defined neutral/unknown treatment; never give an unsupported candidate a favourable score.

Show raw evidence, score rationale, weight, weighted contribution, unknowns, and sensitivity to weights. If evidence is insufficient to distinguish candidates, report no defensible winner. Do not hide a critical safety or feasibility failure inside an aggregate score.

## 8. Risk integration

Consolidate open risks and questions from FS-M-001 through FS-M-009. Each risk entry shall include:

- Unique FS-M-010 risk ID.
- Source study and source risk/question/input IDs.
- Description, cause, consequence, and affected requirement/decision.
- Evidence status and severity rationale.
- Mitigation or closure action, owner, and dependency.
- Residual risk and readiness-gate relevance.
- Status and evidence for closure.

Do not duplicate an upstream risk as though it were a new independent finding. Preserve the source reference and identify any integrated impact. Missing motor data, duty/ambient/peak duration, unresolved shaft/bearing interfaces, unverified protection/thermal performance, supplier availability, and incomplete costs must be evaluated where applicable.

## 9. Readiness gates and decision semantics

The study shall evaluate GO, CONDITIONAL-GO, and NO-GO outcomes for the next phase.

- **GO:** all mandatory readiness gates have adequate evidence, required independent review is complete, no unresolved blocker prevents the proposed scope, and the Project Lead records an explicit decision.
- **CONDITIONAL-GO:** a narrowly defined next-phase activity may proceed with documented conditions, exclusions, owners, deadlines, and safeguards; it must not authorize activities whose safety-critical prerequisites are unmet.
- **NO-GO:** a critical failure, incompatible interface, unacceptable unresolved risk, or missing prerequisite prevents the proposed activity.
- **NOT_VERIFIED:** evidence is insufficient or review is incomplete. This is the default readiness state until the evidence and approval requirements are met.

No GO decision may be made without the required independent review. The reviewer must be independent of the author for safety-critical conclusions. The Project Lead owns the readiness recommendation and decision record, but cannot self-approve safety-critical work they authored.

A conditional-go is not blanket authorization to fabricate, procure, assemble, or energize the actuator. Its scope and exclusions must be explicit.

## 10. A0 next-phase planning

Recommend an A0 build-planning package only after defining what evidence and approvals remain necessary. Candidate activities may include:

- Freeze the candidate comparison inputs and document the chosen trade-off decision when evidence supports it.
- Resolve motor and gearbox compatibility with sourced operating data.
- Resolve shaft/bearing interfaces and housing mounting details.
- Define the controller, encoder, wiring, protection, and thermal design requirements.
- Finalize a traceable preliminary BOM and quote critical long-lead items.
- Define manufacturing routes, critical tolerances, inspection, assembly, and rework strategy.
- Create a separately reviewed validation plan for electrical protection, thermal performance, loaded-cycle integrity, and shock loads as applicable.
- Assign owners, deliverables, dependencies, and review gates.

These are recommendations for planning, not approvals to purchase, fabricate, or test. Do not select unverified parts to make the plan appear complete.

## 11. Deliverables

Mandatory:

- `calculations/` - reproducible trade-off scoring, weight sensitivity, and quantitative cross-study comparisons.
- `outputs/` - requirements coverage, artifact manifest, consistency findings, ratio/candidate comparison, integrated risk register, readiness-gate matrix, and A0 action recommendations.
- `references/SOURCE_REGISTER.csv` - traceable external sources used by the integrated study.

Not applicable by default:

- `CAD/` - NOT_APPLICABLE; this study integrates existing geometry evidence rather than creating authoritative mechanical geometry.
- `simulation/` - NOT_APPLICABLE unless a justified new simulation is required for a specific unresolved decision.
- `component_research/` - NOT_APPLICABLE unless new, sourced candidate research is explicitly needed.
- `cost_estimate/` - NOT_APPLICABLE as a separate directory if FS-M-009's cost outputs are sufficient; create only for a justified integrated cost model.
- `test_data/` - NOT_APPLICABLE for this readiness desk study. Validation testing must be separately planned and controlled.

Record a rationale if any applicability changes.

## 12. Acceptance criteria

Each criterion requires an evidence pointer, an explicit status, and an owner for unresolved actions.

- **AC-001:** All consumed FS-M-001 through FS-M-009 inputs and artifacts are traceable by exact path, revision, units, and review status; upstream IDs and statuses are not redefined.
- **AC-002:** The Option C architecture baseline and its purchased/in-house boundaries are documented, with no unsupported part selection.
- **AC-003:** A requirement-by-requirement coverage matrix identifies evidence, status, gaps, owners, and readiness-gate relevance.
- **AC-004:** Cross-study consistency checks cover motor, gearbox ratio, shaft, bearings, housing, encoder, controller, firmware, thermal paths, interfaces, and cost.
- **AC-005:** The 15:1, 20:1, and 25:1 ratios are compared using verified operating points and explicit assumptions; screening values are not treated as qualification evidence.
- **AC-006:** Candidate trade-off criteria, weights, score scale, evidence confidence, and scoring rationale are documented before final ranking.
- **AC-007:** Every score and weighted contribution is evidence-backed; unknown data is not assigned a favourable score, and critical failures cannot be masked by aggregation.
- **AC-008:** Score sensitivity and evidence limitations are documented; a winner is not declared if available evidence cannot distinguish candidates defensibly.
- **AC-009:** Integrated risks and open questions preserve source-study IDs, affected requirements, owners, mitigations, and readiness-gate relevance.
- **AC-010:** SYS-REQ-091 life-versus-duty, SYS-REQ-092 post-loaded-cycle integrity, and SYS-REQ-014 shock loads are distinguished and correctly traced.
- **AC-011:** Cost and manufacturing conclusions are reconciled with FS-M-009 evidence, SYS-REQ-100 budget scope, sourced prices, and unresolved BOM exposure.
- **AC-012:** Electrical, thermal, shaft, bearing, and housing conclusions are reconciled with upstream evidence; unsupported performance or safety claims remain NOT_VERIFIED.
- **AC-013:** GO, CONDITIONAL-GO, and NO-GO gates have explicit entry criteria, evidence, conditions, exclusions, and decision authority; default status is NOT_VERIFIED.
- **AC-014:** A0 next-phase actions identify prerequisites, owners, dependencies, and review/validation gates without authorizing unverified parts or unsafe activities.
- **AC-015:** Mandatory calculations, outputs, and source registration are complete; all NOT_APPLICABLE and conditional directories are handled according to this specification.
- **AC-016:** Independent review is recorded against the evidence revision; the author cannot approve their own safety-critical work, and no GO decision is issued without required independent review.

## 13. Review and approval

The owner is the Project Lead; the reviewer is Independent Reviewer TBD. The Project Lead shall assign an independent reviewer for safety-critical evidence and readiness conclusions.

The reviewer shall assess evidence integrity, cross-study consistency, trade-off methodology, risk treatment, and readiness-gate compliance. Record reviewer identity, date, evidence revision, findings, dispositions, and unresolved conditions.

The author cannot approve their own safety-critical work. If independent review is absent, incomplete, or not independent, readiness remains NOT_VERIFIED and GO is prohibited.

## 14. Status semantics

- **PASS:** evidence demonstrates the criterion and required review is complete.
- **FAIL:** evidence demonstrates that the criterion is not met.
- **BLOCKED:** a required input, dependency, or decision is missing.
- **NOT_VERIFIED:** evidence or required review is insufficient.
- **NOT_APPLICABLE:** the criterion or deliverable does not apply, with rationale.

The study lifecycle remains PROPOSED until changed through the controlled review process. Readiness status is reported separately from lifecycle status.

## 15. Must-not-conclude list

Without adequate evidence and required review, this study must not conclude that:

- Option C is fully feasible or ready for production.
- A particular gearbox ratio or candidate set is definitively superior when evidence is incomplete.
- Continuous 10 N·m output torque, 20-25 N·m peak operation, or 45 RPM performance is demonstrated.
- The motor, gearbox, shaft, bearing, housing, controller, firmware, encoder, or thermal system is approved.
- Electrical protection, thermal limits, shock-load performance, service life, or post-loaded-cycle integrity has been demonstrated.
- A0/A1 is within budget if material BOM costs or scope items remain unpriced or excluded without approval.
- Supplier stock, lead time, pricing, or manufacturing capability is guaranteed without suitable evidence.
- A readiness GO has been approved without required independent review.
- A conditional-go authorizes fabrication, procurement, assembly, or powered testing outside its explicit scope.
- Planned tests, calculations, or documents constitute measured qualification evidence.

## 16. Safety and test boundary

This is an integrated desk study. It does not authorize procurement, fabrication, assembly, or powered testing. Each subsequent phase requires its own defined scope, prerequisites, safety controls, acceptance criteria, and approvals.

Any electrical bench activity must follow applicable verified requirements, including SYS-REQ-045 and SYS-REQ-084 where relevant. Shock-load and post-loaded-cycle validation must use their correct requirement definitions: SYS-REQ-014 and SYS-REQ-092, respectively. Thermal, electrical-protection, life, and loaded-cycle verification must not be claimed without applicable evidence.

Unresolved safety-critical risks block the relevant activity. Independent review is mandatory before a GO readiness decision.

## 17. Completion checklist

- [ ] Upstream artifacts and revisions verified.
- [ ] Option C architecture and ownership boundaries documented.
- [ ] Requirement coverage matrix complete.
- [ ] Cross-study consistency checks complete.
- [ ] Ratio/candidate trade-off uses evidence-backed scoring.
- [ ] Weight and evidence sensitivity documented.
- [ ] Integrated risk register preserves source references.
- [ ] SYS-REQ-091, SYS-REQ-092, and SYS-REQ-014 correctly distinguished.
- [ ] Manufacturing/cost and electrical/thermal conclusions reconciled.
- [ ] Readiness gates and A0 action recommendations documented.
- [ ] Mandatory outputs and source register complete.
- [ ] Independent review recorded.
- [ ] Readiness status and decision authority explicitly recorded.
- [ ] No unsupported GO, part-selection, safety, or feasibility claim remains.
