---
study_id: FS-M-004
title: Gearbox Selection and Ratio Optimization - Work Plan
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Independent Reviewer TBD
priority: P1
specification: SPECIFICATION.md
inputs: inputs/INPUTS.md
assumptions_and_open_questions: ASSUMPTIONS_AND_OPEN_QUESTIONS.md
---

# FS-M-004 Work Plan

## 1. Objective

Produce an evidence-backed shortlist and ratio comparison for commercial planetary gearboxes for Kritva-M. Jointly iterate with FS-M-003; preserve all unknowns and distinguish catalogue ratings from demonstrated suitability. Do not freeze a part number or ratio.

## 2. Dependencies and Interfaces

**Upstream**

- FS-M-001: authoritative input IDs/statuses, assumptions and open questions.
- FS-M-002: `outputs/LOAD_CASES.csv`, `outputs/DYNAMIC_TORQUE_RESULTS.csv`, `outputs/REFLECTED_INERTIA.csv`, and `outputs/GRAVITY_TORQUE_SWEEP.csv` if present.
- FS-M-003: candidate motor torque-speed curves, operating points, current/thermal constraints, motor interface and package data.

**Downstream consumers:** FS-M-005, FS-M-006, FS-M-007, FS-M-008, FS-M-009 and FS-M-010.

If an upstream file is missing, stale or unreviewed, record the exact missing dependency and continue only with clearly labelled provisional screening. Do not fabricate its contents.

## 3. Work Packages

| WP | Activity | Outputs / evidence | Exit condition |
|---|---|---|---|
| WP-01 | Establish baseline and dependencies | Input traceability, upstream revision/commit record, gap list | All required IDs and available output files are checked |
| WP-02 | Research commercial candidates | `component_research/`, `references/SOURCE_REGISTER.csv` | Candidates have traceable manufacturer/model evidence or are marked unverified |
| WP-03 | Normalize candidate ratings | `outputs/GEARBOX_CANDIDATE_MATRIX.csv` | Rating definitions, conditions and unknowns are comparable |
| WP-04 | Optimize ratios jointly with FS-M-003 | `outputs/RATIO_OPTIMIZATION.csv`, calculations | 15:1, 20:1, 25:1 and comparison-only 37:1 assessed against shared operating points |
| WP-05 | Verify loads, interfaces and life | `outputs/LOAD_RATING_CHECK.csv`, `outputs/INTERFACE_COMPATIBILITY.csv`, `outputs/LIFE_RATING_ASSESSMENT.csv` | Torque, speed, bearing-load path, interfaces, life and environment are assessed or blocked explicitly |
| WP-06 | Review and close study | Updated outputs, decision record, `REVIEW.md` | AC table is dispositioned; independent impact/peak review is recorded |

## 4. Suggested Schedule

Planning estimate: 10 working days, dependent on upstream data availability and supplier response. This is a work estimate, not a committed delivery date.

| Day | Planned work | Checkpoint |
|---|---|---|
| 1 | Verify FS-M-001 inputs and FS-M-002 outputs; establish revision record | Missing/stale data logged |
| 2-3 | Search manufacturer catalogues and collect candidate evidence | Initial candidate shortlist and source register |
| 4 | Normalize ratings, stage count, speed, efficiency and backlash | Candidate matrix reviewed for comparability |
| 5-6 | Run ratio calculations and joint motor/gearbox iteration | Ratio matrix and assumptions reviewed |
| 7 | Check stop-impact, peak torque and load ratings | Independent-review package prepared |
| 8 | Check interfaces, bearing load path, life, lubrication and environment | Compatibility and life gaps recorded |
| 9 | Consolidate mass, replaceability, sourcing and cost evidence | Provisional recommendation drafted |
| 10 | Complete AC disposition and review | Review findings and residual blockers recorded |

If supplier data or upstream evidence is unavailable, revise the schedule and mark affected results as BLOCKED or PROVISIONAL rather than passing them by default.

## 5. Calculation and Evidence Controls

- Use SI units internally; record source units and conversions.
- Keep manufacturer ratings, calculated values, assumptions and unknowns distinct.
- Record source ID and input IDs for every numerical result.
- Preserve the definition and reference side of reflected inertia; do not silently combine incompatible conventions.
- Apply the IN-025 20% gearbox margin transparently and only once at the appropriate screening stage.
- Do not treat catalogue maximum torque as an emergency-stop rating without documented applicability.
- Record ratio, efficiency, speed and load point for every comparison.
- Never infer unavailable part numbers, prices, life ratings, backlash or supplier stock.

## 6. Acceptance Criteria Tracking

Use the same acceptance criteria and wording as `SPECIFICATION.md`. Set status to `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `FAIL` or `BLOCKED`. A criterion may be marked `PASS` only when its evidence is committed and review requirements are satisfied. `BLOCKED` is not a pass.

The second column is a short evidence/check label only; the criterion wording in `SPECIFICATION.md` governs.

| AC | Required evidence / check | Status | Evidence path / notes |
|---|---|---|---|
| AC-001 | Upstream input IDs and statuses preserved | NOT_STARTED | |
| AC-002 | FS-M-002 output files and revisions verified | NOT_STARTED | |
| AC-003 | FS-M-003 motor envelope reconciled | NOT_STARTED | |
| AC-004 | 15:1, 20:1, 25:1; 37:1 comparison-only | NOT_STARTED | |
| AC-005 | Manufacturer and exact model verified or lead flagged | NOT_STARTED | |
| AC-006 | Continuous, peak and emergency/impact ratings distinguished | NOT_STARTED | |
| AC-007 | Input-speed limits checked | NOT_STARTED | |
| AC-008 | Efficiency assumptions and sourced data distinguished | NOT_STARTED | |
| AC-009 | Backlash evidence and SYS-REQ-025 gap recorded | NOT_STARTED | |
| AC-010 | Reflected inertia and backdrivability assessed | NOT_STARTED | |
| AC-011 | Permitted loads and bearing-load path assessed | NOT_STARTED | |
| AC-012 | Interface checked against SYS-REQ-033, IN-015 and IN-016 | NOT_STARTED | |
| AC-013 | Life, duty, peak duration, lubrication and environment assessed | NOT_STARTED | |
| AC-014 | Mass, replaceability, sourcing and cost evidence compared | NOT_STARTED | |
| AC-015 | Mandatory deliverables and source register complete | NOT_STARTED | |
| AC-016 | Independent impact/peak review and residual blockers recorded | NOT_STARTED | |

## 7. Required Outputs

Create these files or folders as work progresses:

- `calculations/`: reproducible calculations with units, assumptions, source references and input IDs.
- `outputs/GEARBOX_CANDIDATE_MATRIX.csv`
- `outputs/RATIO_OPTIMIZATION.csv`
- `outputs/LOAD_RATING_CHECK.csv`
- `outputs/INTERFACE_COMPATIBILITY.csv`
- `outputs/LIFE_RATING_ASSESSMENT.csv`
- `component_research/`: candidate evidence and manufacturer documents.
- `references/SOURCE_REGISTER.csv`
- `REVIEW.md`: review record and findings.

Create `simulation/` only when a defined question justifies simulation. Create `cost_estimate/` when cost evidence is adequate. `test_data/` is not applicable to the initial desk-based study.

## 8. Review Gates

**Gate A - Evidence completeness:** candidate identity, source provenance and rating conditions are traceable.

**Gate B - Engineering compatibility:** ratios, torque/speed, efficiency, inertia, backlash, interface and load paths are checked against the shared baseline.

**Gate C - Independent impact review:** stop-impact and peak-torque assessment reviewed independently. Unsupported or ambiguous emergency ratings remain open.

**Gate D - Project disposition:** Project Lead reviews downstream implications, residual risks and provisional recommendation. Only authorized project approval can freeze a selection.

## 9. Risks and Escalation

Escalate immediately if:

- Required FS-M-002 load or inertia data is missing or inconsistent.
- A candidate lacks evidence for required continuous torque, input speed or permitted loads.
- Stop-impact or emergency rating is absent or its duration/duty is ambiguous.
- Gearbox output bearings would receive unapproved arm loads.
- The shaft/bearing interface cannot be reconciled without a custom design.
- Candidate efficiency, backlash, life or availability is asserted without traceable evidence.

Log each issue in `ASSUMPTIONS_AND_OPEN_QUESTIONS.md`; link it from calculations and review notes. Do not silently relax a requirement.

## 10. Completion Checklist

- [ ] All upstream dependencies and revisions recorded.
- [ ] Candidate sources and exact model identifiers checked.
- [ ] Ratio comparison jointly reviewed with FS-M-003.
- [ ] Load, speed, efficiency, inertia and backlash checks reproducible.
- [ ] Stop-impact/peak-load evidence independently reviewed.
- [ ] Bearing load path and mechanical interfaces documented.
- [ ] Life, duty, lubrication and ambient gaps explicitly tracked.
- [ ] Mandatory deliverables and source register committed.
- [ ] AC-001..AC-016 dispositions match the specification exactly.
- [ ] Review findings and residual blockers recorded.
- [ ] Recommendation clearly marked provisional unless all required approval gates are satisfied.
