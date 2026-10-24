---
study_id: FS-M-007
title: Housing and Mechanical Integration - Work Plan
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Project Lead; Independent Reviewer TBD for safety-critical structural and hard-stop checks
priority: P2
specification: SPECIFICATION.md
inputs: inputs/INPUTS.md
assumptions_and_open_questions: ASSUMPTIONS_AND_OPEN_QUESTIONS.md
---

# FS-M-007 Work Plan

## 1. Objective

Create and assess a concept housing and mechanical assembly for Kritva-M, including mandatory CAD envelope/interference checks, load path, interfaces, hard stops, encoder mounting, serviceability and manufacturing constraints. Clearly distinguish concept geometry from verified design. Do not claim strength, mass/envelope compliance or serviceability without evidence.

## 2. Dependencies and Interfaces

**FS-M-001:** authoritative inputs, canonical requirements, ASM-001..ASM-012 and OQ-001..OQ-014. IN-019 provenance is unresolved under OQ-012.

**FS-M-003:** motor candidate data and operating points, mounting dimensions, envelope and thermal/electrical constraints.

**FS-M-004:** `outputs/GEARBOX_CANDIDATE_MATRIX.csv`, `outputs/RATIO_OPTIMIZATION.csv`, `outputs/LOAD_RATING_CHECK.csv`, `outputs/INTERFACE_COMPATIBILITY.csv` and `outputs/LIFE_RATING_ASSESSMENT.csv`.

**FS-M-005:** `outputs/SHAFT_LOAD_CASES.csv`, `outputs/SHAFT_STRENGTH_CHECK.csv`, `outputs/IMPACT_CHECK.csv`, `outputs/DEFLECTION_CHECK.csv`, `outputs/INTERFACE_CHECK.csv` and `outputs/MATERIAL_COMPARISON.csv`.

**FS-M-006:** `outputs/BEARING_LOAD_CASES.csv`, `outputs/BEARING_CANDIDATE_MATRIX.csv`, `outputs/BEARING_RATING_CHECK.csv`, `outputs/LIFE_ASSESSMENT.csv`, `outputs/IMPACT_BEARING_CHECK.csv`, `outputs/INTERFACE_DECISION.csv` and `outputs/SUPPORT_FEASIBILITY.csv`.

Verify paths, revisions, units and review status. Use the recorded FS-M-006 `outputs/INTERFACE_DECISION.csv` disposition for IN-015/IN-016; do not silently change either upstream input.

**Downstream:** FS-M-008 receives motor thermal, cable and mounting constraints; FS-M-009 receives process/sourcing constraints; FS-M-010 receives integration interfaces and unresolved risks.

## 3. Work Packages

| WP | Activity | Outputs / evidence | Exit condition |
|---|---|---|---|
| WP-01 | Establish requirements and input baseline | Dependency/revision register, open-gap list | Required upstream artifacts verified or blockers recorded |
| WP-02 | Define architecture and interfaces | `outputs/INTERFACE_REGISTER.csv`, `calculations/` | Load path and major interfaces documented |
| WP-03 | Build concept CAD | `CAD/` assembly, envelope and interference model | Concept status and unresolved dimensions labelled |
| WP-04 | Assess structure, hard stops and alignment | `outputs/STRUCTURAL_CHECK.csv`, `outputs/HARD_STOP_CHECK.csv`, `outputs/ALIGNMENT_CHECK.csv` | Hand estimates and upstream load cases traceable |
| WP-05 | Assess assembly, tolerance and manufacture | `outputs/TOLERANCE_STACK.csv`, `outputs/SERVICEABILITY_CHECK.csv`, `outputs/PROCESS_OPTIONS.csv` | Key interfaces and replacement sequence assessed |
| WP-06 | Consolidate, review and hand off | `outputs/MASS_ENVELOPE_STATUS.csv`, review record | AC table dispositioned; downstream constraints issued |

## 4. Suggested Schedule

Planning estimate: 10 working days, dependent on upstream model readiness and Project Lead review.

| Day | Planned work | Checkpoint |
|---|---|---|
| 1 | Verify canonical requirements and upstream artifact revisions | Dependency gaps recorded |
| 2 | Establish load path, architecture and interface register | Interface assumptions reviewed |
| 3-4 | Build concept CAD assembly, envelope and interference model | Concept geometry labelled and revisioned |
| 5 | Evaluate shaft/bearing/gearbox/motor interfaces and tolerance stack | Interface issues documented |
| 6 | Estimate housing stiffness, seat deformation and critical fastener loads | Hand calculations traceable |
| 7 | Assess hard stops and impact load path | Project Lead review package prepared |
| 8 | Assess encoder mount, cable routing, assembly and serviceability | Integration checklist updated |
| 9 | Review manufacturing options and mass/envelope status | Unknown budgets and process constraints explicit |
| 10 | Complete acceptance tracking and review | Findings and downstream handoffs recorded |

Replan if exact motor/gearbox/bearing dimensions or approved load cases are unavailable. Keep the concept model useful while marking affected interfaces provisional.

## 5. CAD and Calculation Controls

- CAD is mandatory. Label the assembly as concept geometry and annotate every assumed dimension or unresolved interface.
- Keep a consistent revision for CAD, calculations and output tables.
- Check interference, clearances, tool access, assembly/disassembly paths, cable routing and hard-stop travel.
- Use verified upstream geometry and load cases where available; do not invent dimensions.
- Use hand calculations for initial housing stiffness and deformation. Propose FEA only when a defined uncertainty warrants it.
- Separate the arm-load path from gearbox torque reaction and motor mounting loads.
- Record materials and manufacturing processes for every load-bearing seat/mount.
- Do not claim mass/envelope compliance without approved arm-layout budgets and component masses.
- Keep supplier prices, part numbers and availability tied to dated sources.

## 6. Acceptance Criteria Tracking

Use the same AC IDs and requirements as `SPECIFICATION.md` section 15. Allowed statuses: `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `FAIL`, `BLOCKED`. A `PASS` requires committed evidence and the required review. `BLOCKED` is not a pass.

The second column is a short evidence/check label only; the criterion wording in `SPECIFICATION.md` governs.

| AC | Required evidence / check | Status | Evidence path / notes |
|---|---|---|---|
| AC-001 | Upstream IDs, values and statuses preserved | NOT_STARTED | |
| AC-002 | FS-M-003/004/005/006 artifacts and revisions verified | NOT_STARTED | |
| AC-003 | Shaft-to-bearing-to-housing-to-mounting load path documented | NOT_STARTED | |
| AC-004 | Mandatory CAD assembly/envelope/interference model labelled as concept | NOT_STARTED | |
| AC-005 | Motor, gearbox, bearing, shaft, encoder and arm interfaces reconciled | NOT_STARTED | |
| AC-006 | Housing material/process and load-bearing feature justification documented | NOT_STARTED | |
| AC-007 | Housing stiffness/deformation assessed or justified analysis proposed | NOT_STARTED | |
| AC-008 | Hard-stop geometry, range, load path and impact cases assessed | NOT_STARTED | |
| AC-009 | Encoder mounting, cable routing and loaded alignment coordinated | NOT_STARTED | |
| AC-010 | Assembly/disassembly and independent replacement assessed | NOT_STARTED | |
| AC-011 | Tolerance stacks, fits, fasteners, inserts and inspection needs documented | NOT_STARTED | |
| AC-012 | Mass/envelope status compared with approved budgets or left unresolved | NOT_STARTED | |
| AC-013 | Manufacturing/process and sourcing considerations traceable | NOT_STARTED | |
| AC-014 | Mandatory calculations, outputs and source register reproducible | NOT_STARTED | |
| AC-015 | Conditional and not-applicable deliverables handled correctly | NOT_STARTED | |
| AC-016 | Project Lead review and residual-risk disposition recorded | NOT_STARTED | |

## 7. Required Outputs

Mandatory:

- `CAD/`: assembly, envelope and interference model; concept geometry explicitly labelled.
- `calculations/`: structural hand estimates, tolerance stack, alignment and mass calculations when supported by data.
- `outputs/INTERFACE_REGISTER.csv`
- `outputs/STRUCTURAL_CHECK.csv`
- `outputs/HARD_STOP_CHECK.csv`
- `outputs/ALIGNMENT_CHECK.csv`
- `outputs/TOLERANCE_STACK.csv`
- `outputs/SERVICEABILITY_CHECK.csv`
- `outputs/PROCESS_OPTIONS.csv`
- `outputs/MASS_ENVELOPE_STATUS.csv`
- `references/SOURCE_REGISTER.csv`

Conditional:

- `simulation/`: housing stiffness FEA only when justified by hand estimates.
- `cost_estimate/`: only when component and process cost evidence is sufficient.
- `component_research/`: when candidate drawings, process information or supplier evidence is gathered.

Not applicable to the initial concept study:

- `test_data/`

## 8. Review Gates

**Gate A - Dependency validity:** upstream requirements, component data and load/interface outputs are verified.

**Gate B - Integration completeness:** concept CAD, load path, mounting interfaces, hard stops, encoder and replacement access are assessed.

**Gate C - Structural review:** Project Lead and an Independent Reviewer (to be assigned) review housing strength and hard-stop load path under peak and stop-impact cases. The author cannot self-approve; unreviewed results remain `NOT_VERIFIED`.

**Gate D - Handoff:** unresolved mechanical, electrical, manufacturing and envelope constraints are issued to FS-M-008, FS-M-009 and FS-M-010.

## 9. Risks and Escalation

Escalate if:

- Required upstream CAD/dimension data or load cases are missing.
- Arm loads cannot be shown to bypass gearbox and motor bearings.
- The FS-M-006 interface decision does not resolve the shaft/bearing seat geometry.
- Housing or bearing-seat deformation threatens encoder alignment.
- Hard-stop impact loads lack a defensible analysis or independent review.
- A printed load-bearing seat/mount lacks process and structural justification.
- Mass/envelope budgets remain unknown while compliance is requested.
- Independent component replacement cannot be demonstrated by the assembly concept.

Record each issue in `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` and link it to affected CAD, calculations, acceptance criteria and downstream handoffs.

## 10. Completion Checklist

- [ ] Upstream artifacts and revisions verified.
- [ ] Structural load path and interface register documented.
- [ ] Mandatory concept CAD assembly/envelope/interference model committed.
- [ ] Hard stops and peak/impact load path assessed.
- [ ] Housing stiffness, bearing-seat alignment and encoder mounting assessed.
- [ ] Tolerance stack, assembly sequence and replacement access documented.
- [ ] Load-bearing material/process justified or explicitly unresolved.
- [ ] Mass/envelope budget status reported without invented values.
- [ ] Mandatory calculations, outputs and source register committed.
- [ ] AC-001..AC-016 statuses match the specification.
- [ ] Project Lead review and downstream handoffs recorded.
