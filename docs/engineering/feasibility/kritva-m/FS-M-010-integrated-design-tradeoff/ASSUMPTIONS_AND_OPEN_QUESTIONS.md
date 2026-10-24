---
study_id: FS-M-010
title: Integrated Design Trade-off and Readiness - Assumptions and Open Questions
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

# FS-M-010 Assumptions and Open Questions

## 1. Purpose and ID rules

This file captures local assumptions and unresolved questions for the integrated Option C trade-off and readiness assessment.

Upstream FS-M-001 input IDs IN-001 through IN-039, assumptions ASM-001 through ASM-012, and open questions OQ-001 through OQ-014 remain owned by FS-M-001. Reference upstream IDs and verify their exact wording/status; do not redefine or silently close them.

Local IDs use `FS10-IN-nnn`, `FS10-ASM-nnn`, and `FS10-OQ-nnn`. Assumptions are not approved design decisions. An unresolved critical input, interface, or review remains visible and blocks the affected conclusion.

## 2. Local assumptions register

| Local ID | Provisional assumption or method | Limitation | Resolution action |
|---|---|---|---|
| FS10-ASM-001 | Treat Option C as the architecture to evaluate: commercial BLDC, planetary gearbox, output encoder and bearings; in-house housing, shaft, controller, and firmware | This is a trade-off baseline, not a final design or selected BOM | Confirm boundaries against current upstream evidence |
| FS10-ASM-002 | Treat FS-M-001 as the authoritative source for system inputs and status | Downstream studies may contain copied or stale values | Check source IDs and record discrepancies rather than silently correcting them |
| FS10-ASM-003 | Treat a listed artifact as unverified until its path, revision, units, and review status are checked | Filename presence alone does not prove content or approval | Build the artifact manifest |
| FS10-ASM-004 | Use 15:1, 20:1, and 25:1 as the required ratio comparison set where supported by IN-010 | IN-010 is PRELIMINARY; no ratio is approved by this specification | Verify candidate-specific operating points and ratings |
| FS10-ASM-005 | Treat IN-011's 20:1 first candidate as a baseline for comparison, not a preferred final choice | A starting candidate does not establish feasibility or superiority | Compare all ratios with the same evidence-backed criteria |
| FS10-ASM-006 | Use IN-012's 85% gearbox efficiency only as a screening assumption | Actual candidate efficiency may vary with operating conditions | Validate or bound from FS-M-004 evidence |
| FS10-ASM-007 | Define trade-off weights before scoring and retain raw scores/evidence | Weights can materially change ranking; undocumented weights are not reproducible | Record rationale and run sensitivity analysis |
| FS10-ASM-008 | Treat missing critical evidence as NOT_VERIFIED rather than favourable | An aggregate score must not hide a critical feasibility or safety gap | Make critical requirements explicit gates |
| FS10-ASM-009 | Treat a cost subtotal with material TBD items as incomplete | Missing cost cannot be treated as zero | Show known subtotal and unpriced exposure using FS-M-009 evidence |
| FS10-ASM-010 | Treat readiness as NOT_VERIFIED until evidence and independent review support a decision | Lifecycle status PROPOSED is not a readiness approval | Complete gates and record review/disposition |
| FS10-ASM-011 | Treat planned validation as future evidence, not demonstrated compliance | A plan or calculation is not a completed test | Separate planned, executed, reviewed, and passed evidence |
| FS10-ASM-012 | Treat conditional-go as bounded permission for a specifically described activity only | It does not authorize procurement, fabrication, assembly, or powered testing by implication | Record scope, exclusions, prerequisites, owners, and approvals |
| FS10-ASM-013 | Preserve upstream risk ownership while recording integrated consequences | Duplicated risk entries can obscure source and closure authority | Link each integrated risk to source IDs and evidence |
| FS10-ASM-014 | Treat Option C purchased/in-house boundaries as provisional until interface and cost evidence are reconciled | Some functions may require redesign or a different sourcing approach | Record any proposed boundary change as an explicit decision |
| FS10-ASM-015 | Do not claim a ratio/candidate winner when the available evidence cannot distinguish candidates | Ranking incomplete candidates can create false confidence | Report no defensible winner and identify evidence needed |

## 3. Upstream assumptions and questions to preserve

The following records remain under upstream ownership:

- ASM-001 through ASM-012.
- OQ-001 through OQ-014.
- IN-006, IN-007, IN-008, IN-009, IN-010, IN-011, IN-012, IN-013, IN-014, IN-024, IN-025, IN-026, IN-028, IN-029, IN-030, IN-031, IN-034, and IN-037.

Verify the exact upstream source record before using any value. Do not change an upstream status within FS-M-010. If downstream studies conflict with the authoritative baseline, create an integrated consistency issue and obtain a controlled resolution from the owning study.

## 4. Open questions register

| Local ID | Open question | Impact if unresolved | Owner / closure evidence |
|---|---|---|---|
| FS10-OQ-001 | Are all FS-M-001 through FS-M-009 artifacts present, current, traceable, and reviewed at the required level? | Integrated readiness remains NOT_VERIFIED | Project Lead; artifact manifest and owner confirmations |
| FS10-OQ-002 | What is the exact requirement baseline and current coverage status for all applicable system requirements? | Requirement closure and gate decisions may be incomplete | Project Lead; verified requirement records and coverage matrix |
| FS10-OQ-003 | Which motor candidates have complete sourced torque-speed, current, resistance, efficiency, thermal, feedback, and supplier data? | Motor/ratio comparison remains conditional | FS-M-003/008 owners; verified candidate data and source register |
| FS10-OQ-004 | Which planetary gearbox candidates and ratios meet verified torque, speed, efficiency, backlash, life, and interface constraints? | No ratio/candidate selection can be justified | FS-M-004 owner; candidate matrix, ratings, and life evidence |
| FS10-OQ-005 | Is the shaft/bearing interface reconciled, including the 12 mm shaft (IN-015) versus the 6202 bearing on 15 mm seats (IN-016, ASSUMED) where applicable? | Mechanical compatibility and readiness remain blocked until the actual interface is resolved | FS-M-005/006 owners; reviewed interface decision and updated calculations |
| FS10-OQ-006 | Are shaft material, combined strength, impact, deflection, and fatigue conclusions supported and independently reviewed where required? | Shaft selection and shock/strength readiness remain NOT_VERIFIED | FS-M-005 owner and independent reviewer; reviewed evidence |
| FS10-OQ-007 | Are bearing load, rating, life, support, and impact conclusions supported under the required duty and load cases? | Bearing readiness and SYS-REQ-091 assessment remain incomplete | FS-M-006 owner; verified calculations and required review |
| FS10-OQ-008 | Are housing structure, hard-stop load path, encoder mounting, interfaces, and envelope sufficiently mature for A0 planning? | Housing integration and manufacturing scope remain uncertain | FS-M-007 owner; reviewed interface/structural outputs |
| FS10-OQ-009 | Are electrical voltage limits, current limits, motor-current requirements, controller sizing, feedback, and protection sufficiently defined? | Electrical architecture and powered-test readiness remain NOT_VERIFIED | FS-M-008 owner; sourced calculations and independent protection review |
| FS10-OQ-010 | Are continuous holding and peak thermal conditions established, including IN-026, IN-028, IN-031, and actual material/thermal-path data? | Thermal feasibility cannot be declared | FS-M-008/007 owners; verified thermal assessment and independent review |
| FS10-OQ-011 | Are the manufacturing process, tolerances, inspection plan, sourcing, lead times, and supplier qualification evidence adequate for A0 planning? | Manufacturing plan and delivery estimate remain provisional | FS-M-009 owner; dated sources and process/inspection matrix |
| FS10-OQ-012 | Is the A0/A1 BOM complete, and does its cost basis match SYS-REQ-100 scope and quantities? | Budget compliance cannot be determined if costs or scope remain TBD | FS-M-009 owner and Project Lead; reconciled cost roll-up |
| FS10-OQ-013 | Which requirements are critical readiness gates, and what evidence is required to close each? | GO/conditional-go criteria may be ambiguous | Project Lead; approved gate matrix with evidence and owners |
| FS10-OQ-014 | Which criteria and weights should govern ratio/candidate trade-offs, and are they approved before scoring? | Candidate rankings may be subjective or non-reproducible | Project Lead; recorded rubric, weights, and sensitivity results |
| FS10-OQ-015 | Can available evidence defensibly distinguish 15:1, 20:1, and 25:1 for the current candidate set? | No final ratio recommendation can be justified if data is incomplete | Project Lead with study owners; verified candidate comparisons |
| FS10-OQ-016 | What integrated risks remain open, who owns them, and which block A0 planning or later testing? | Readiness could understate critical dependencies | Project Lead; source-linked risk register |
| FS10-OQ-017 | Who is the independent reviewer, and are they independent of the authors of safety-critical work? | No GO decision is permitted | Project Lead; reviewer appointment and review record |
| FS10-OQ-018 | What exactly may proceed under any proposed conditional-go, and what is explicitly excluded? | Conditional permission may be misinterpreted as general build/test approval | Project Lead; bounded decision record with prerequisites and safeguards |
| FS10-OQ-019 | What validation plan and acceptance criteria are needed for SYS-REQ-014 shock loads and SYS-REQ-092 post-loaded-cycle integrity? | Neither shock nor post-cycle integrity can be claimed demonstrated | Project Lead and relevant engineering/test owners; separately reviewed plans |
| FS10-OQ-020 | What A0 actions are safe and useful before all component and thermal choices are closed? | Planning may accidentally commit to unverified parts or unsafe activity | Project Lead; staged action plan with entry/exit gates |
| FS10-OQ-021 | What source revisions and unresolved evidence gaps must be carried into the final readiness decision? | Decision could rely on stale or incomplete data | Project Lead; evidence-bound decision package |

## 5. Trade-off and scoring controls

1. Establish evaluation criteria, weights, scoring scale, and evidence-confidence rules before assigning candidate scores.
2. Use verified candidate data for the 15:1, 20:1, and 25:1 comparison; preserve preliminary/assumed input statuses.
3. Record raw values, source references, assumptions, scores, weights, weighted contributions, and unknowns.
4. Run sensitivity analysis for plausible weight changes. If ranking changes materially, state that the conclusion is weight-sensitive.
5. Treat missing critical evidence as NOT_VERIFIED or BLOCKED. Do not award a favourable score merely because a candidate has less documentation.
6. Do not allow a high aggregate score to compensate for a critical failure or incompatible interface.
7. If the evidence cannot distinguish candidates, report no defensible winner and identify the additional evidence required.

## 6. Readiness decision controls

The readiness state starts as NOT_VERIFIED.

- **GO:** permitted only after mandatory gates have adequate evidence and the required independent review is complete.
- **CONDITIONAL-GO:** allowed only for a bounded activity with explicit conditions, exclusions, prerequisites, owners, and safeguards. It does not automatically authorize purchasing, fabrication, assembly, or energized testing.
- **NO-GO:** record the critical failure, incompatible interface, or unacceptable risk that blocks the proposed activity.
- **NOT_VERIFIED:** retain when evidence, independent review, or decision authority is incomplete.

The Project Lead owns the readiness decision record. The reviewer must be independent for safety-critical work; an author cannot approve their own safety-critical conclusions. If independent review is missing or incomplete, GO is prohibited.

## 7. Requirement distinction controls

Keep the following requirements separate in the coverage and risk matrices:

- SYS-REQ-091 - gearbox/bearing life versus duty.
- SYS-REQ-092 - post-loaded-cycle integrity: no unacceptable permanent deformation, loosening, bearing damage, or encoder misalignment.
- SYS-REQ-014 - conditional shock-load requirement (applies only if impacts are in scope; scope open, upstream OQ-009).

Do not infer compliance from a planned test, a calculation with unresolved inputs, or an unrelated requirement's closure.

## 8. Must-not-conclude list

Without adequate evidence and required review, FS-M-010 must not conclude that:

- Option C is fully feasible, production-ready, or approved.
- A particular ratio or candidate set is definitively superior when evidence is insufficient.
- Continuous 10 N·m torque, 20-25 N·m peak operation, or 45 RPM performance is demonstrated.
- Motor, gearbox, shaft, bearing, housing, encoder, controller, firmware, or thermal system selection is approved.
- Electrical protection, thermal limits, shock-load performance, service life, or post-loaded-cycle integrity has been demonstrated.
- A0/A1 is within budget while material costs or budget scope remain unresolved.
- Supplier availability, price, lead time, or manufacturing capability is guaranteed without evidence.
- A GO decision is authorized without required independent review.
- A conditional-go authorizes activities outside its documented scope.
- A desk study or planned test constitutes completed validation.

## 9. Closure and handoff

For each open question, record the answer or unresolved disposition, evidence path, source revision, owner, date, and affected readiness gate. Do not close questions solely through verbal agreement where technical evidence or a controlled decision is required.

The final integrated record shall state:

- Evidence revision and artifact-manifest status.
- Requirement coverage and unresolved critical gates.
- Trade-off method, scores, limitations, and sensitivity.
- Integrated risks and assigned owners.
- Readiness disposition and its decision authority.
- Independent reviewer findings and unresolved conditions.
- Recommended A0 planning scope, exclusions, and prerequisites.

Until the necessary evidence and independent review are complete, the study remains PROPOSED and readiness remains NOT_VERIFIED.
