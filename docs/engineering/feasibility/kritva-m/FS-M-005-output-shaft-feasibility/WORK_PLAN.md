---
study_id: FS-M-005
title: Output Shaft Feasibility - Work Plan
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

# FS-M-005 Work Plan

## 1. Objective

Evaluate the independent output shaft against verified load cases, material evidence, combined strength, fatigue, impact, deflection, encoder alignment, bearing support and gearbox interface constraints. Produce a traceable feasibility result. Do not release a shaft design or self-approve safety-critical conclusions.

## 2. Dependencies and Interfaces

**FS-M-001:** authoritative input IDs and statuses; canonical requirements; ASM-001..ASM-012 and OQ-001..OQ-014. Pay particular attention to OQ-009 and OQ-012.

**FS-M-002:** verify `outputs/LOAD_CASES.csv` and `outputs/DYNAMIC_TORQUE_RESULTS.csv`, including revision, units and review status. Identify stop-impact cases and their assumptions before calculations.

**FS-M-004:** verify `outputs/INTERFACE_COMPATIBILITY.csv` and relevant candidate evidence. Use the exact gearbox candidate and torque-transfer interface only as far as supported by evidence.

**FS-M-006:** coordinate dedicated bearing pair, bearing-seat diameters, shaft support spacing, housing load path and the IN-016 mismatch.

**Downstream:** FS-M-007, FS-M-009 and FS-M-010 receive documented shaft geometry, loads, interfaces, mass implications and unresolved constraints as applicable.

If a dependency is missing or unreviewed, mark affected results `BLOCKED` or `PROVISIONAL`. Do not replace missing engineering evidence with an undocumented estimate.

## 3. Work Packages

| WP | Activity | Outputs / evidence | Exit condition |
|---|---|---|---|
| WP-01 | Establish requirements and input baseline | Input traceability; upstream revision record; gap list | Required IDs and artifacts verified or blockers recorded |
| WP-02 | Define shaft geometry and load cases | `calculations/`; `outputs/SHAFT_LOAD_CASES.csv` | Critical sections, supports, loads and assumptions documented |
| WP-03 | Compare material and manufacture options | `outputs/MATERIAL_COMPARISON.csv`; source register | Material properties and condition traceable; unknowns explicit |
| WP-04 | Calculate static, combined and fatigue strength | `outputs/SHAFT_STRENGTH_CHECK.csv`; calculations | Methods, concentration factors, margins and limitations documented |
| WP-05 | Evaluate impact, deflection and interfaces | `outputs/IMPACT_CHECK.csv`, `outputs/DEFLECTION_CHECK.csv`, `outputs/INTERFACE_CHECK.csv` | Critical cases reviewed or explicitly blocked |
| WP-06 | Consolidate and review | Feasibility summary; `REVIEW.md`; AC dispositions | Independent review recorded and residual risks identified |

## 4. Suggested Schedule

Planning estimate: 10 working days, subject to upstream readiness and independent reviewer availability. This is not a committed completion date.

| Day | Work | Checkpoint |
|---|---|---|
| 1 | Verify canonical requirements and upstream inputs | Input and dependency gaps recorded |
| 2 | Review FS-M-002 loads and FS-M-004 interface | Load/interface baseline agreed or blocked |
| 3 | Define candidate shaft geometry, bearing locations and critical sections | Assumptions and geometry version recorded |
| 4-5 | Compare materials and calculate torsion, bending, axial and combined stresses | Reproducible calculations available |
| 6 | Evaluate stress concentrations, static margin and fatigue | Missing material/duty data flagged |
| 7 | Evaluate hard-stop/impact cases | Independent-review package prepared |
| 8 | Calculate deflection, slope and encoder alignment; coordinate FS-M-006 | Support assumptions and interface gaps documented |
| 9 | Consolidate manufacture, inspection and sensitivity results | Provisional feasibility disposition drafted |
| 10 | Complete acceptance tracking and review | Findings, blockers and reviewer disposition recorded |

Replan if the FS-M-002 load envelope, FS-M-004 interface or FS-M-006 support geometry is unavailable. Do not pass a blocked criterion to meet the schedule.

## 5. Calculation Controls

- Use SI units internally and record all source-unit conversions.
- Use the exact approved load-case revisions where available.
- Distinguish nominal stress from local stress at notches and geometric transitions.
- Record shaft diameter, support spacing, lever arms, section properties and boundary conditions.
- Document the chosen static and fatigue criteria, material condition, concentration factors and assumptions.
- Treat handbook properties as `ASSUMED` or `PRELIMINARY` unless supported by the specified material condition and traceable evidence.
- Evaluate sensitivity to geometry, load uncertainty and material properties.
- Do not claim fatigue life where load spectrum, peak repetition or fatigue data are inadequate.
- Do not use FEA to conceal missing loads or unsupported boundary conditions.

## 6. Acceptance Criteria Tracking

Use the same AC IDs and requirements as `SPECIFICATION.md` section 15. Allowed status values: `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `FAIL`, `BLOCKED`. A criterion may be `PASS` only when its evidence is committed and required review is complete. A missing input is not a pass.

The second column is a short evidence/check label only; the criterion wording in `SPECIFICATION.md` governs.

| AC | Required evidence / check | Status | Evidence path / notes |
|---|---|---|---|
| AC-001 | Upstream input IDs, values and statuses preserved | NOT_STARTED | |
| AC-002 | FS-M-002 load outputs and revisions verified | NOT_STARTED | |
| AC-003 | FS-M-004 interface evidence reconciled | NOT_STARTED | |
| AC-004 | Geometry, supports and critical sections documented | NOT_STARTED | |
| AC-005 | Torsional, bending and axial stress calculated | NOT_STARTED | |
| AC-006 | Combined stress and concentrations assessed | NOT_STARTED | |
| AC-007 | Static strength and IN-023 target assessed | NOT_STARTED | |
| AC-008 | Fatigue method, inputs and limitations documented | NOT_STARTED | |
| AC-009 | Hard-stop/impact cases and IN-019 uncertainty assessed | NOT_STARTED | |
| AC-010 | Deflection, slope and twist checked against SYS-REQ-034 | NOT_STARTED | |
| AC-011 | Bearing pair and arm-load bypass path coordinated | NOT_STARTED | |
| AC-012 | Gearbox interface and IN-015/IN-016 mismatch assessed | NOT_STARTED | |
| AC-013 | Material, process, tolerances and inspection justified | NOT_STARTED | |
| AC-014 | Calculations, outputs and source register reproducible | NOT_STARTED | |
| AC-015 | Mandatory/conditional/not-applicable deliverables handled correctly | NOT_STARTED | |
| AC-016 | Independent review and residual-risk disposition recorded | NOT_STARTED | |

## 7. Required Outputs

Mandatory:

- `calculations/`: reproducible stress, fatigue, impact, deflection and sensitivity work.
- `outputs/SHAFT_LOAD_CASES.csv`
- `outputs/MATERIAL_COMPARISON.csv`
- `outputs/SHAFT_STRENGTH_CHECK.csv`
- `outputs/IMPACT_CHECK.csv`
- `outputs/DEFLECTION_CHECK.csv`
- `outputs/INTERFACE_CHECK.csv`
- `references/SOURCE_REGISTER.csv`

Conditional:

- `simulation/`: FEA only if hand calculations justify a specific unresolved question.
- `CAD/`: only when the geometry is mature enough to model meaningfully.

Not applicable to this initial study:

- `cost_estimate/`
- `test_data/`

Record conditional and not-applicable dispositions in the study README or review record. Do not create placeholder files that imply analysis or testing has been performed.

## 8. Review Gates

**Gate A - Input validity:** load cases, upstream revisions and interface data are verified.

**Gate B - Analytical completeness:** geometry, load path, critical sections, combined stress, static margin, fatigue limitations and deflection are documented.

**Gate C - Impact/strength review:** independent reviewer examines peak, stop-impact and shaft-strength evidence. The author cannot self-approve this work.

**Gate D - Integration disposition:** FS-M-006 bearing support and the gearbox interface are reconciled; downstream consumers are notified of constraints.

Any unresolved safety-critical question remains `OPEN`, `BLOCKED` or `NOT_VERIFIED`.

## 9. Risk and Escalation

Escalate if:

- FS-M-002 load cases or IN-019 provenance are missing or inconsistent.
- Material strength, heat treatment or fatigue properties cannot be substantiated.
- A critical notch, shoulder or keyway dominates stress and lacks defensible geometry.
- IN-031 prevents a defensible fatigue or peak-duration assessment.
- Deflection/slope limits or encoder alignment requirements are unavailable.
- The 12 mm shaft conflicts with bearing seats or gearbox interface geometry.
- Arm loads cannot be shown to bypass gearbox and motor bearings.
- Independent review is unavailable.

Record each issue in `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` and link it to affected calculations and acceptance criteria.

## 10. Completion Checklist

- [ ] Canonical requirements and input IDs checked.
- [ ] FS-M-002 load outputs and revisions verified.
- [ ] FS-M-004 interface and FS-M-006 bearing dependencies documented.
- [ ] Geometry and critical sections identified.
- [ ] Static, combined, fatigue and impact calculations reproducible.
- [ ] Deflection, slope and encoder alignment assessed or blocked.
- [ ] Material and manufacturing evidence traceable.
- [ ] Mandatory deliverables and source register committed.
- [ ] AC-001..AC-016 statuses match the specification.
- [ ] Independent review of critical strength and impact cases recorded.
- [ ] Recommendation and unresolved blockers explicitly documented.
