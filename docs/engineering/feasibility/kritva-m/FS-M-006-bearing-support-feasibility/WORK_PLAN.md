---
study_id: FS-M-006
title: Bearing and Support Feasibility - Work Plan
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Independent Reviewer TBD
priority: P2
specification: SPECIFICATION.md
inputs: inputs/INPUTS.md
assumptions_and_open_questions: ASSUMPTIONS_AND_OPEN_QUESTIONS.md
---

# FS-M-006 Work Plan

## 1. Objective

Evaluate candidate bearing pairs and housing support for Kritva-M using traceable shaft reactions, static and dynamic bearing ratings, life methods, fit/interface requirements and stop-impact cases. Coordinate with FS-M-005 and escalate the IN-015/IN-016 mismatch for Project Lead disposition. Do not release a bearing or housing design.

## 2. Dependencies and Interfaces

**FS-M-001:** authoritative inputs and statuses, canonical requirements, ASM-001..ASM-012 and OQ-001..OQ-014. OQ-012 is particularly relevant to the preliminary impact estimate.

**FS-M-002:** verify `outputs/LOAD_CASES.csv` and `outputs/DYNAMIC_TORQUE_RESULTS.csv` and record their revisions.

**FS-M-004:** verify `outputs/INTERFACE_COMPATIBILITY.csv`, exact gearbox candidate and permitted-load evidence.

**FS-M-005:** verify `outputs/SHAFT_LOAD_CASES.csv`, `outputs/SHAFT_STRENGTH_CHECK.csv`, `outputs/IMPACT_CHECK.csv`, `outputs/DEFLECTION_CHECK.csv`, `outputs/INTERFACE_CHECK.csv` and `outputs/MATERIAL_COMPARISON.csv`. Use approved revisions and coordinate updates to bearing locations, shaft seats and support geometry.

**Downstream:** FS-M-007, FS-M-009 and FS-M-010 receive the bearing envelope, load path, interfaces, serviceability constraints and open risks.

Missing or unreviewed dependencies must be recorded as `BLOCKED` or `PROVISIONAL`; do not invent reactions or ratings.

## 3. Work Packages

| WP | Activity | Outputs / evidence | Exit condition |
|---|---|---|---|
| WP-01 | Verify requirements, inputs and upstream revisions | Dependency record and gap list | Required input IDs and source artifacts checked |
| WP-02 | Establish bearing loads and support geometry | `calculations/`; `outputs/BEARING_LOAD_CASES.csv` | Reactions traceable to FS-M-005 load cases and support assumptions |
| WP-03 | Research candidate bearing types and exact models | `component_research/`; source register | Candidate ratings and dimensions sourced or marked unknown |
| WP-04 | Compare arrangements, ratings, fits and life | `outputs/BEARING_CANDIDATE_MATRIX.csv`, `outputs/BEARING_RATING_CHECK.csv`, `outputs/LIFE_ASSESSMENT.csv` | Calculations and limits documented; no unsupported life claim |
| WP-05 | Assess impact, interface and housing support | `outputs/IMPACT_BEARING_CHECK.csv`, `outputs/INTERFACE_DECISION.csv`, `outputs/SUPPORT_FEASIBILITY.csv` | Critical checks reviewed or explicitly blocked |
| WP-06 | Consolidate and review | Feasibility summary, AC disposition, `REVIEW.md` | Independent review recorded; residual risks handed off |

## 4. Suggested Schedule

Planning estimate: 10 working days, dependent on FS-M-005 geometry/load readiness and reviewer availability.

| Day | Planned work | Checkpoint |
|---|---|---|
| 1 | Verify inputs, requirements and upstream artifacts | Missing/stale data logged |
| 2 | Establish load cases and bearing support assumptions with FS-M-005 | Reaction model reviewed |
| 3-4 | Research bearing types and exact catalogue candidates | Initial candidate matrix and sources |
| 5 | Calculate equivalent loads and static rating checks | Rating assumptions traceable |
| 6 | Evaluate life methods, duty gaps and speed limits | Life conclusions conditional where needed |
| 7 | Assess hard-stop/impact loads and prepare independent review | Critical check package ready |
| 8 | Resolve seat, fit, retention and encoder alignment dependencies | Interface decision and FS-M-005 handoff |
| 9 | Evaluate housing process, lubrication, thermal expansion and serviceability | Support feasibility summary |
| 10 | Complete acceptance tracking and review | Findings, blockers and disposition recorded |

Replan if load cases, support geometry or candidate documentation are unavailable. Schedule pressure must not convert an unresolved safety-critical check into a pass.

## 5. Calculation and Evidence Controls

- Use SI units and record source-unit conversions.
- Trace each bearing reaction to a specific FS-M-005 load case and support geometry revision.
- Verify exact manufacturer/model, C0, C, limiting speed and permitted load conditions.
- Use a stated method for equivalent loads, static checks and L10 life; cite the applicable method and manufacturer guidance.
- Account for combined radial/axial loads and moment effects only within the verified bearing arrangement's capabilities.
- Keep manufacturer ratings, calculated values, assumptions and unknowns distinct.
- Do not claim life compliance while IN-026, IN-030 or IN-031 remain unresolved.
- Treat hard-stop/impact checks as safety-critical and independently review them.
- Do not accept a printed bearing seat solely because its nominal dimensions fit.
- Do not invent part numbers, ratings, prices, stock status or supplier lead times.

## 6. Acceptance Criteria Tracking

Use the same AC IDs and criteria as `SPECIFICATION.md` section 15. Allowed statuses: `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `FAIL`, `BLOCKED`. `PASS` requires committed evidence and completion of required review. `BLOCKED` is not a pass.

The second column is a short evidence/check label only; the criterion wording in `SPECIFICATION.md` governs.

| AC | Required evidence / check | Status | Evidence path / notes |
|---|---|---|---|
| AC-001 | Upstream IDs, values and statuses preserved | NOT_STARTED | |
| AC-002 | FS-M-002 and FS-M-005 artifacts/revisions verified | NOT_STARTED | |
| AC-003 | FS-M-004 interface and permitted-load evidence reconciled | NOT_STARTED | |
| AC-004 | Candidate manufacturer/model verified or lead flagged | NOT_STARTED | |
| AC-005 | Bearing type, pair arrangement, spacing and fit rationale documented | NOT_STARTED | |
| AC-006 | Reactions derived from load cases and support geometry | NOT_STARTED | |
| AC-007 | C0, C, speed and permitted-load ratings sourced and checked | NOT_STARTED | |
| AC-008 | Equivalent loads and life method documented | NOT_STARTED | |
| AC-009 | Life claim withheld while required duty/life inputs remain unresolved | NOT_STARTED | |
| AC-010 | Hard-stop/impact checks and IN-019 uncertainty assessed | NOT_STARTED | |
| AC-011 | IN-015/IN-016 mismatch assessed and escalated | NOT_STARTED | |
| AC-012 | Seats, fits, retention, material/process and thermal expansion assessed | NOT_STARTED | |
| AC-013 | Deflection, support stiffness and encoder alignment coordinated | NOT_STARTED | |
| AC-014 | Lubrication, sealing, environment, replaceability and sourcing documented | NOT_STARTED | |
| AC-015 | Mandatory deliverables/source register complete; optional deliverables handled correctly | NOT_STARTED | |
| AC-016 | Independent peak/impact review and residual-risk disposition recorded | NOT_STARTED | |

## 7. Required Outputs

Mandatory:

- `calculations/`: reaction, equivalent load, static rating, life, fit/tolerance, thermal and stiffness calculations.
- `outputs/BEARING_LOAD_CASES.csv`
- `outputs/BEARING_CANDIDATE_MATRIX.csv`
- `outputs/BEARING_RATING_CHECK.csv`
- `outputs/LIFE_ASSESSMENT.csv`
- `outputs/IMPACT_BEARING_CHECK.csv`
- `outputs/INTERFACE_DECISION.csv`
- `outputs/SUPPORT_FEASIBILITY.csv`
- `component_research/`
- `references/SOURCE_REGISTER.csv`

Conditional:

- `simulation/`: when justified by a defined support, contact or housing question.
- `CAD/`: when geometry is mature enough for a meaningful assembly/clearance model.
- `cost_estimate/`: when sourced prices and integration costs support a defensible estimate.

Not applicable to the initial desk-based study:

- `test_data/`

Record the disposition of conditional and not-applicable deliverables in the study review record. Do not imply that simulation, CAD, cost estimation or testing occurred when it did not.

## 8. Review Gates

**Gate A - Input validity:** upstream loads, geometry, revisions and candidate evidence verified.

**Gate B - Bearing suitability:** arrangement, reactions, static/dynamic ratings, speed and life method documented.

**Gate C - Critical load review:** independent review of peak-load and stop-impact bearing checks. The author cannot self-approve.

**Gate D - Integration:** IN-015/IN-016 interface decision escalated; shaft, housing, encoder and replacement constraints coordinated with FS-M-005 and downstream owners.

Any unresolved safety-critical rating or impact question remains `OPEN`, `BLOCKED` or `NOT_VERIFIED`.

## 9. Risk and Escalation

Escalate if:

- Shaft reactions or support coordinates are unavailable or inconsistent.
- Candidate load ratings do not cover the required load direction, speed or conditions.
- IN-019 remains unsupported for a conclusion about stop-impact survival.
- Life, duty or peak repetition is unresolved but a life claim is being requested.
- The 12 mm shaft conflicts with the 6202's 15 mm bore.
- Housing-seat material/process cannot be justified for the calculated loads.
- Encoder alignment limits are unavailable.
- Independent review is unavailable.

Record the issue in `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` and link it to affected calculations, acceptance criteria and downstream handoffs.

## 10. Completion Checklist

- [ ] Canonical requirements and upstream input IDs checked.
- [ ] FS-M-002, FS-M-004 and FS-M-005 artifacts/revisions verified.
- [ ] Bearing reactions and support assumptions documented.
- [ ] Candidate ratings, dimensions and source register complete.
- [ ] Static, dynamic and conditional life calculations reproducible.
- [ ] Stop-impact check independently reviewed or marked NOT_VERIFIED.
- [ ] IN-015/IN-016 mismatch escalated for Project Lead decision.
- [ ] Housing seats, fits, thermal effects and load path assessed.
- [ ] Encoder alignment and serviceability coordinated with FS-M-005.
- [ ] AC-001..AC-016 statuses match the specification.
- [ ] Residual risks and downstream constraints recorded.
