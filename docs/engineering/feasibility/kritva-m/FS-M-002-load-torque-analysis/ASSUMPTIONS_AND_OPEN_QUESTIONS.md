---
study_id: FS-M-002
title: Load and Torque Analysis - Assumptions and Open Questions
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Independent Reviewer TBD
upstream_assumptions: ../FS-M-001-integrated-actuator-system/ASSUMPTIONS_AND_OPEN_QUESTIONS.md
canonical_requirements: requirements/SYSTEM_REQUIREMENTS.md
---

# FS-M-002 Assumptions and Open Questions

## 1. Purpose and Rules

This file records study-local assumptions and questions affecting FS-M-002. Upstream FS-M-001 assumptions `ASM-001..ASM-012` and open questions `OQ-001..OQ-014` remain authoritative in the upstream register; reference them by ID and do not duplicate or redefine them here.

- Study-local assumption IDs use `FS2-ASM-nnn`; question IDs use `FS2-OQ-nnn`.
- Every material assumption has a validation action, owner, linked input and affected study.
- Every open question has an owner, blocking classification and resolution evidence.
- Unresolved safety-critical inputs or missing mandatory independent review mean affected results remain `NOT_VERIFIED`.
- Proposed sensitivity values are not approved requirements or tolerances.

## 2. Study-Local Assumptions Register

| assumption_id | statement | basis | status | impact_if_wrong | validation_action | owner | linked_input | linked_study |
|---|---|---|---|---|---|---|---|---|
| FS2-ASM-001 | For the initial gravity model, 0° is the fully extended elbow pose and the horizontal pose gives maximum gravity torque under the defined geometry. | SYSTEM_REQUIREMENTS section 6 (joint angle 0° = fully extended; horizontal load case = maximum static gravity torque); to be reconciled with CAD. | PRELIMINARY | Wrong pose interpretation changes the torque curve, governing angle and downstream load cases. | Verify the canonical angle convention and CAD geometry; document any coordinate transformation; check the predicted maximum mathematically. | Mechanical Intern | FS2-IN-006 | FS-M-002; FS-M-003; FS-M-005; FS-M-006; FS-M-010 |
| FS2-ASM-002 | Initial CoM sensitivity uses 160, 180 and 200 mm forearm/hand CoM positions. | ±20 mm placeholder around upstream IN-002. | ASSUMED | Sensitivity may not cover real mass-property uncertainty. | Replace or supplement with CAD mass properties or measurement; keep the placeholder label until confirmed. | Mechanical Intern | FS2-IN-002 | FS-M-002; FS-M-003; FS-M-005; FS-M-006; FS-M-010 |
| FS2-ASM-003 | Payload-position sensitivity bounds will be selected around the 350 mm nominal using a documented exploratory range. | Upstream IN-004; range not yet established. | ASSUMED once bounds are selected | Unsupported bounds misrepresent sensitivity and governing load. | Determine bounds from CAD/configuration constraints and record rationale; otherwise mark payload sensitivity incomplete. | Mechanical Intern | FS2-IN-003; FS2-IN-009 | FS-M-002; FS-M-003; FS-M-005; FS-M-006; FS-M-010 |
| FS2-ASM-004 | A 1° increment is used for the initial 0–135° sweep. | Study calculation plan. | ASSUMED | A coarse sweep could miss a governing point if the model has discontinuities. | Verify the sweep captures the maximum; refine locally or use the analytical solution. | Mechanical Intern | FS2-IN-004 | FS-M-002; FS-M-003; FS-M-005; FS-M-006; FS-M-010 |
| FS2-ASM-005 | Gravity is modelled with g = 9.80665 m/s². | Explicit calculation convention (FS-M-001 IN-005 used 9.81). | ASSUMED | Small numerical differences; larger errors only from unit misuse. | Confirm project convention; keep SI units. | Mechanical Intern | FS2-IN-001 | FS-M-002; FS-M-003; FS-M-005; FS-M-006 |
| FS2-ASM-006 | The rigid-body dynamic model uses an explicitly stated equivalent inertia about the elbow output axis; no unverified inertia is silently added or omitted. | Standard torque balance; IN-017 source and axis not yet confirmed. | PRELIMINARY | Dynamic torque and reflected inertia may be wrong if bodies or axes differ. | Verify IN-017 provenance, included bodies and axis; list extra inertias separately. | Mechanical Intern | FS2-IN-007 | FS-M-002; FS-M-003; FS-M-004; FS-M-005; FS-M-006; FS-M-010 |
| FS2-ASM-007 | Friction and drivetrain losses are represented only by a documented model or explicit scenario, never silently zero in a final acceptance case. | Missing friction/loss characterisation. | PRELIMINARY | Required torque or motor-side demand may be under-estimated or double-counted. | Obtain supplier data, measurement or a reviewed model; separate output load from motor-side demand. | Mechanical Intern | FS2-IN-008 | FS-M-002; FS-M-003; FS-M-004; FS-M-008; FS-M-010 |
| FS2-ASM-008 | Any illustrative acceleration profile is for sensitivity only and is not evidence of compliance with SYS-REQ-013. | IN-032 and OQ-002 unresolved. | ASSUMED | Scenario results could be mistaken for required performance. | Obtain approved motion profiles; label scenario parameters and limits in every result file. | Mechanical Intern; Project Lead | FS2-IN-005; IN-032 | FS-M-002; FS-M-003; FS-M-004; FS-M-008; FS-M-010 |
| FS2-ASM-009 | IN-017 (0.171 kg·m²) is not treated as a verified equivalent inertia until included bodies and reference axis are established. | Upstream status PRELIMINARY; source details unconfirmed. | PRELIMINARY | Dynamic, energy and reflected-inertia results may use the wrong inertia. | Retrieve the original calculation or CAD report; document body inclusion and axis. | Mechanical Intern | FS2-IN-007; IN-017 | FS-M-002; FS-M-003; FS-M-004; FS-M-005; FS-M-006 |
| FS2-ASM-010 | IN-018 stop energy and IN-019 impact torque are comparison values only until their derivations are reproduced. | Upstream values PRELIMINARY (see OQ-012). | PRELIMINARY | Stop, shaft, bearing, gearbox or housing loads may be mischaracterised. | Recover source equations, inputs, boundary conditions and units; independently review the resulting impact case. | Mechanical Intern; Independent Reviewer TBD | IN-018; IN-019 | FS-M-002; FS-M-004; FS-M-005; FS-M-006; FS-M-010 |
| FS2-ASM-011 | The IN-036 single-contact hard-stop case is a provisional governing case, not proof that all real contact conditions are covered. | Upstream ASM-004 and IN-036. | ASSUMED | Actual contact distribution or load path may give different reactions and stresses. | Verify stop geometry, contact sequence, stiffness and load path; obtain independent review. | Mechanical Intern; Independent Reviewer TBD | IN-036 | FS-M-002; FS-M-005; FS-M-006; FS-M-010 |
| FS2-ASM-012 | The reflected-inertia model includes only traceable inertia data; unknown motor and gearbox inertia remain explicit gaps. | Upstream IN-010, IN-014, IN-035, IN-039. | PRELIMINARY | Total equivalent inertia and dynamic performance may be misestimated. | Obtain candidate-specific motor/gearbox data; document axis transformations. | Mechanical Intern | FS2-IN-007; IN-014; IN-035 | FS-M-002; FS-M-003; FS-M-004; FS-M-010 |

## 3. Upstream Assumptions and Open Questions to Track

Do not duplicate upstream entries; track their IDs and review the current source record.

- Upstream assumptions: `ASM-001..ASM-012`.
- Upstream open questions: `OQ-001..OQ-014`.
- Particularly relevant: `OQ-001` CoM; `OQ-002` duty, acceleration and holding; `OQ-003` peak duration, repetition and recovery; `OQ-009` shock loads; `OQ-012` provenance of the 47.5 N·m impact torque and the EN8 strength factor.
- Relevant assumptions include efficiency (ASM-001), CoM (ASM-002), bearing/shaft mismatch (ASM-003), hard-stop case (ASM-004), margins (ASM-005..007) and proposed-requirement treatment (ASM-012).

## 4. Study-Local Open Questions Register

| question_id | question | why_it_matters | blocking | affected_studies | owner | needed_by | status |
|---|---|---|---|---|---|---|---|
| FS2-OQ-001 | Does the canonical requirement and CAD convention define 0° as the fully extended pose, and does the horizontal pose give the maximum gravity torque for the actual geometry? | An incorrect angle convention invalidates the sweep and governing torque. | YES | FS-M-002; FS-M-003; FS-M-005; FS-M-006; FS-M-010 | Mechanical Intern; Project Lead for clarification | Before accepting gravity-torque results | OPEN |
| FS2-OQ-002 | Which bodies and payloads are included in IN-017 = 0.171 kg·m², and about which axis? | Dynamic torque, stop energy and reflected inertia depend on it. | YES | FS-M-002; FS-M-003; FS-M-004; FS-M-005; FS-M-006; FS-M-010 | Mechanical Intern | Before accepting dynamic and impact calculations using IN-017 | OPEN |
| FS2-OQ-003 | What friction model and drivetrain-loss data are appropriate, and which terms belong at the output versus the motor side? | Missing or double-counted losses misstate required torque and motor-side demand. | PARTIAL | FS-M-002; FS-M-003; FS-M-004; FS-M-008; FS-M-010 | Mechanical Intern; Embedded Intern for drive data | Before final motor-side demand and continuous assessment | OPEN |
| FS2-OQ-004 | What approved acceleration/deceleration profile applies if IN-032 stays UNKNOWN? | Dynamic and peak demand depend on acceleration, speed and duration. | YES | FS-M-002; FS-M-003; FS-M-004; FS-M-008; FS-M-010 | Project Lead; Mechanical Intern | Before dynamic/peak feasibility is concluded | OPEN |
| FS2-OQ-005 | What payload-position sensitivity range is justified around IN-004 = 350 mm? | Arbitrary bounds may not represent the real configuration. | PARTIAL | FS-M-002; FS-M-003; FS-M-005; FS-M-006; FS-M-010 | Mechanical Intern | Before sensitivity results are accepted as representative | OPEN |
| FS2-OQ-006 | Who is the named independent reviewer for peak-load and stop-impact calculations? | Required safety-critical review cannot be completed without one (see upstream OQ-014). | YES | FS-M-002; FS-M-003; FS-M-004; FS-M-005; FS-M-006; FS-M-010 | Project Lead | Before review submission | OPEN |
| FS2-OQ-007 | What is the source and derivation of the 47.5 N·m impact torque and 1.9 J stop energy (inertia, speed, contact stiffness, impact duration)? Progress: derivation located in `mechanical/calculations/LOAD_CASES.md` sections 4 and 8 (linear-spring model, 2 mm bumper at r_s = 25 mm). Remaining: reproduce independently and obtain the bumper force-deflection curve. | The values cannot establish stop, shaft, bearing, gearbox or housing adequacy without a traceable model (see upstream OQ-012). | YES | FS-M-002; FS-M-004; FS-M-005; FS-M-006; FS-M-010 | Mechanical Intern; Independent Reviewer TBD | Before accepting stop-impact load cases | OPEN |
| FS2-OQ-008 | What is the required operating cycle: duty cycle, holding duration, peak frequency and recovery? | RMS and thermal conclusions need a representative cycle (see upstream OQ-002, OQ-003). | YES | FS-M-002; FS-M-003; FS-M-004; FS-M-008; FS-M-010 | Project Lead; Mechanical Intern | Before final continuous/RMS conclusion | OPEN |
| FS2-OQ-009 | What payload and external-contact loads, if any, must be included beyond the nominal gravity load case? | Extra loads change governing torque and support reactions. | PARTIAL | FS-M-002; FS-M-003; FS-M-005; FS-M-006; FS-M-010 | Project Lead; Mechanical Intern | Before final load-case handoff | OPEN |
| FS2-OQ-010 | What is the final upper joint limit within the provisional 120–135° range, and what are the stop-angle tolerances? | Governing load and stop geometry may depend on it. | PARTIAL | FS-M-002; FS-M-005; FS-M-006; FS-M-007; FS-M-010 | Project Lead; Mechanical Intern | Before final range-dependent load-case acceptance | OPEN |
| FS2-OQ-011 | What upper-arm orientation(s) apply during elbow operation (see FS2-IN-010)? | The horizontal-forearm pose gives the documented 6.08 N·m only with a vertical upper arm; other orientations change the governing torque. | PARTIAL | FS-M-002; FS-M-003; FS-M-005; FS-M-010 | Project Lead; Mechanical Intern | Before the gravity sweep is accepted | OPEN |

## 5. Blocking Classification

- `YES`: the affected result cannot be accepted until resolved.
- `PARTIAL`: preliminary analysis may proceed on clearly identified assumptions, but the conclusion stays qualified.
- `NO`: does not block the current stage, but needs an owner and closure evidence.

Blocking applies to the affected result, not every task in the study.

## 6. How to Close an Assumption or Question

### 6.1 Close an assumption

1. Identify the assumption and its linked study-local or upstream input IDs.
2. Obtain evidence: canonical requirement, CAD or mass-properties report, calculation, datasheet or measurement.
3. Update the appropriate input register; never overwrite an upstream value in this study-local file.
4. Recalculate affected results and assess downstream impact.
5. Record the evidence reference and resolution on the assumption.
6. Obtain review. Stop-impact and peak-load cases need independent review.
7. Keep a record of the change and its effect on conclusions.

### 6.2 Close an open question

1. Confirm the question and owner.
2. Obtain the technical answer or project decision.
3. Record it in its authoritative location and update the applicable input or requirement record.
4. Recalculate affected results and tell downstream studies that must rerun.
5. Reference the evidence in `REVIEW.md` or a supporting file.
6. Change status from `OPEN` only after the responsible reviewer accepts the resolution.
7. If unresolved, record the limitation, next action, owner and whether conclusions stay blocked.

### 6.3 Evidence and traceability

Use repository-relative paths to real files: `inputs/INPUTS.md`, `calculations/`, `outputs/`, `REVIEW.md`, `README.md`. Never invent paths, approvals, measurements, reviewer identities or closure dates. Results awaiting mandatory independent review remain `NOT_VERIFIED`.

## 7. Maintenance

Review this file when an input changes, a new load case appears, canonical requirements change, a calculation exposes new uncertainty, or a review finding affects the load envelope.

The Mechanical Intern maintains the technical records. The Project Lead resolves requirement-level questions and assigns the independent reviewer. Cross-study impacts are communicated to FS-M-003, FS-M-004, FS-M-005, FS-M-006 and FS-M-010.
