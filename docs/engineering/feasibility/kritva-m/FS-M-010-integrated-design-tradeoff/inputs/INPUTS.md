---
study_id: FS-M-010
title: Integrated Design Trade-off and Readiness - Inputs
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

# FS-M-010 Inputs Register

## 1. Purpose and rules

This register identifies the verified baseline inputs, study artifacts, and local evidence required for integrated trade-off and readiness.

Upstream FS-M-001 input IDs, assumptions, and questions remain authoritative. Reference IN-001 through IN-039, ASM-001 through ASM-012, and OQ-001 through OQ-014 by ID; do not redefine or silently close them.

Local inputs use `FS10-IN-nnn`; local assumptions use `FS10-ASM-nnn`; local questions use `FS10-OQ-nnn`. Verify exact upstream records, values, units, statuses, artifact paths, and revisions before using them in a readiness decision.

## 2. Section A - Verified upstream input baseline

Authoritative baseline path: `kritva-m/FS-M-001-integrated-actuator-system/`.

| Upstream ID | Input | Value/status | Integrated-study use |
|---|---|---|---|
| IN-006 | Continuous output torque | >= 10 N·m; PRELIMINARY | Requirement coverage and continuous feasibility evidence |
| IN-007 | Peak output torque | 20 N·m minimum / 25 N·m stretch; PRELIMINARY | Peak capability and validation-gap assessment |
| IN-008 | Output speed | 45 RPM; PRELIMINARY | Ratio and motor operating-point comparison |
| IN-009 | Nominal supply | 24 V DC; PRELIMINARY | Electrical architecture and sourcing context |
| IN-010 | Gearbox ratio set | 15:1, 20:1, 25:1; PRELIMINARY | Ratio trade-off set |
| IN-011 | First candidate ratio | 20:1; PRELIMINARY | Baseline candidate only; not a final selection |
| IN-012 | Gearbox efficiency | 85%; ASSUMED | Screening calculations only; retain assumption status |
| IN-013 | Motor power starting range | 75-100 W; PRELIMINARY | Candidate search context, not proof of feasibility |
| IN-014 | Motor operating data | UNKNOWN | Critical blocker until candidate data is verified |
| IN-024 | Motor margin | 20%; ASSUMED | Confirm definition before use in candidate acceptance |
| IN-025 | Gearbox margin | 20%; ASSUMED | Confirm definition before use in candidate acceptance |
| IN-026 | Duty cycle/continuous holding duration | UNKNOWN | Blocks unconditional continuous thermal/life conclusions |
| IN-028 | Ambient operating temperature | UNKNOWN | Blocks unconditional ambient-dependent thermal conclusions |
| IN-029 | Supply current limit | UNKNOWN | Blocks final supply/controller readiness |
| IN-030 | Service life | UNKNOWN | Blocks unconditional service-life conclusion |
| IN-031 | Peak duration/repetition | UNKNOWN | Blocks unconditional peak thermal conclusion |
| IN-034 | Output-side encoder required | PRELIMINARY | Interface and feedback coverage |
| IN-037 | Shaft material candidates | EN19/42CrMo4 Q&T candidate; EN8 normalised reported strength factor about 0.86; PRELIMINARY | Material/interface trade-off context only; not an approved selection |

The status of every input remains as listed until changed by its owning process. Do not promote preliminary or assumed values to approved facts in the integrated report.

## 3. Option C architecture baseline

Evaluate the following architecture boundaries:

| Element | Baseline concept | Evidence needed before selection/closure |
|---|---|---|
| Motor | Commercial BLDC | FS-M-003 candidate data, torque-speed, current, thermal limits, feedback, sourcing |
| Gearbox | Commercial planetary gearbox | FS-M-004 candidate ratings, ratio, efficiency, backlash, life, interface, sourcing |
| Output encoder | Commercial component | IN-034 plus FS-M-005/007/008 interface and feedback evidence |
| Bearings/support | Purchased bearings with dedicated support arrangement | FS-M-006 candidate/rating/life/interface evidence |
| Shaft | In-house design/manufacture | FS-M-005 load, strength, impact, deflection, material and interface evidence |
| Housing | In-house design/manufacture | FS-M-007 structural/interface/mass-envelope evidence and FS-M-008 thermal constraints |
| Controller | In-house design | FS-M-008 current, voltage, power-stage, feedback, protection, and thermal evidence |
| Firmware | In-house implementation | Verified requirements, control/feedback interface, fault response, and validation plan |
| Manufacturing/sourcing | Mixed purchased and in-house | FS-M-009 dated cost, process, supplier, lead-time, and inspection evidence |

This table defines the evaluation boundary, not a selected bill of materials or approval to build.

## 4. Required upstream artifacts

For each consumed artifact, record exact repository-relative path, revision or commit, units, review status, provenance, and limitations. Confirm the file exists and its contents match the current architecture.

| Study | Expected evidence | Purpose |
|---|---|---|
| FS-M-001 | `INPUTS.md`, requirements, assumptions, open questions | Authoritative baseline and traceability |
| FS-M-002 | `outputs/LOAD_CASES.csv`, `outputs/DYNAMIC_TORQUE_RESULTS.csv` | Load cases, torque/speed calculations, operating assumptions |
| FS-M-003 | Candidate motor data and operating points; exact filenames to be verified | Motor feasibility and candidate comparison |
| FS-M-004 | `outputs/GEARBOX_CANDIDATE_MATRIX.csv`, `outputs/RATIO_OPTIMIZATION.csv`, `outputs/LOAD_RATING_CHECK.csv`, `outputs/LIFE_RATING_ASSESSMENT.csv`, `outputs/INTERFACE_COMPATIBILITY.csv` | Ratio, ratings, interfaces, life, candidate evidence |
| FS-M-005 | Shaft load, strength, impact, deflection, interface, and material-comparison outputs | Shaft feasibility and material/fit decisions |
| FS-M-006 | Bearing load, candidate, rating, life, impact, interface-decision, and support-feasibility outputs | Bearing/support feasibility and interface resolution |
| FS-M-007 | `outputs/INTERFACE_REGISTER.csv`, `outputs/MASS_ENVELOPE_STATUS.csv`, `outputs/STRUCTURAL_CHECK.csv` | Housing, mounting, envelope, structural, and thermal-path context |
| FS-M-008 | Electrical/thermal calculations and outputs, source register, protection and interface assessments | Supply, motor current, controller, thermal, and safety-related gaps |
| FS-M-009 | BOM, cost, manufacturing process, sourcing/lead-time, and inspection outputs; exact filenames to be verified | Budget, sourcing, process, and build-planning evidence |

Do not invent filenames for artifacts whose exact names have not been verified. Missing or unreviewed artifacts are blockers where required to support a conclusion.

## 5. Section B - Study-local inputs

Local inputs identify integrated evidence that must be collected, checked, or derived. Initial status is UNKNOWN or OPEN unless evidence is recorded.

| Local ID | Required input | Status | Source/action |
|---|---|---|---|
| FS10-IN-001 | Complete artifact manifest for FS-M-001 through FS-M-009 | UNKNOWN | Record paths, revisions, units, review status, and limitations |
| FS10-IN-002 | Requirement list and authoritative requirement wording | UNKNOWN | Verify applicable system requirement records and study acceptance criteria |
| FS10-IN-003 | Current Option C component/candidate inventory | UNKNOWN | Reconcile candidate identities across FS-M-003 through FS-M-009 |
| FS10-IN-004 | Verified motor torque-speed, current, resistance, efficiency, feedback, and thermal data | UNKNOWN | FS-M-003/008 evidence; IN-014 remains UNKNOWN until upstream resolution |
| FS10-IN-005 | Verified gearbox ratio, ratings, efficiency, backlash, life, and interface data | UNKNOWN | FS-M-004 candidate evidence |
| FS10-IN-006 | Shaft geometry/material/load/strength/impact/deflection and interface evidence | UNKNOWN | FS-M-005 outputs and review record |
| FS10-IN-007 | Bearing candidate, bore/seat compatibility, loads, life, and support evidence | UNKNOWN | FS-M-006 outputs and interface decision |
| FS10-IN-008 | Housing geometry, structural checks, mounting, mass/envelope, and thermal paths | UNKNOWN | FS-M-007 outputs |
| FS10-IN-009 | Controller/firmware, bus, feedback, current sensing, protection, and thermal evidence | UNKNOWN | FS-M-008 outputs and verified requirements |
| FS10-IN-010 | BOM completeness and cost evidence for purchased/custom items | UNKNOWN | FS-M-009 outputs and source register |
| FS10-IN-011 | A0/A1 budget scope, quantities, inclusions, exclusions, and TBD exposure | UNKNOWN | SYS-REQ-100 and Project Lead clarification |
| FS10-IN-012 | Evidence-backed criteria, weights, score scale, and confidence treatment | OPEN | Define before scoring and record rationale |
| FS10-IN-013 | Integrated risk register with source IDs and owners | UNKNOWN | Roll up upstream risks and open questions |
| FS10-IN-014 | Independent-reviewer identity and review scope | OPEN | Project Lead to arrange independent review |
| FS10-IN-015 | Readiness-gate evidence, exclusions, conditions, and decision record | UNKNOWN | Build gate matrix and preserve NOT_VERIFIED where appropriate |
| FS10-IN-016 | A0 planning scope, dependencies, owners, and validation prerequisites | UNKNOWN | Project Lead planning decision; not authorization to build |
| FS10-IN-017 | Ratio-by-load-case motor/gearbox operating-point comparison | UNKNOWN | Verified FS-M-002/003/004 data and reproducible calculations |
| FS10-IN-018 | Cross-study issue log with severity, impact, and disposition | UNKNOWN | Consistency audit across all studies |
| FS10-IN-019 | Traceable external-source register for integrated claims | UNKNOWN | `references/SOURCE_REGISTER.csv` |
| FS10-IN-020 | Independent-review findings and evidence-bound disposition | UNKNOWN | Reviewer record linked to the exact evidence revision |

## 6. Requirement and status conventions

Use PASS, FAIL, BLOCKED, NOT_VERIFIED, and NOT_APPLICABLE in integrated evidence matrices. The work-plan criterion status vocabulary is NOT_STARTED, IN_PROGRESS, PASS, FAIL, and BLOCKED; do not confuse task progress with technical verification.

Every coverage entry shall include evidence, source revision, owner, remaining gap, and readiness-gate relevance. A requirement without evidence must not be reported as met.

## 7. Trade-off input rules

For the 15:1, 20:1, and 25:1 comparison:

- Verify actual candidate data and load cases before assigning scores.
- Preserve IN-010 and IN-011 statuses.
- Use IN-012's 85% efficiency only as an assumption until validated.
- Keep motor/gearbox ratings, life, shaft/bearing compatibility, thermal limits, controller capability, cost, and sourcing separate as appropriate criteria.
- Record score rationale and evidence confidence.
- Treat missing critical evidence as NOT_VERIFIED, not as a favourable score.
- Do not claim a winning ratio or candidate set if the evidence cannot distinguish candidates defensibly.

## 8. Requirement distinctions

- SYS-REQ-091: gearbox/bearing life versus duty.
- SYS-REQ-092: post-loaded-cycle integrity - no unacceptable permanent deformation, loosening, bearing damage, or encoder misalignment.
- SYS-REQ-014: conditional shock-load requirement (applies only if impacts are in scope; scope open, upstream OQ-009).

Keep these requirements separate in coverage, risk, and readiness matrices. Do not infer that satisfying one demonstrates another.

## 9. Change control

Changes to upstream candidate data, requirements, interface decisions, material assumptions, thermal results, BOM prices, or source revisions must identify affected comparisons, scores, risks, and readiness gates. Preserve upstream IDs and source revisions. New integrated-study inputs use the next available `FS10-IN-nnn` identifier.

## 10. Initial readiness

The study starts PROPOSED with integrated readiness NOT_VERIFIED. No GO decision is implied by the existence of upstream studies or preliminary calculations. Readiness depends on artifact verification, cross-study consistency, required evidence, closure of critical blockers, and independent review.
