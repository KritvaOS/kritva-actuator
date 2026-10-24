# FS-M-002 — Load and torque analysis

| Field | Value |
|---|---|
| Study ID | FS-M-002 |
| Product | Kritva-M (Level 2, Option C) |
| Priority | P1 |
| Lifecycle | PROPOSED |
| Verification status | NOT_STARTED |
| Review decision | PENDING |
| Owner | Mechanical Intern |
| Reviewer | Independent Reviewer TBD |
| Upstream studies | FS-M-001 |
| Standard | `../../FEASIBILITY_STUDIES_STANDARD.md` (v0.4, proposed) |
| Canonical requirements | `requirements/SYSTEM_REQUIREMENTS.md` (rev 0.2, proposed) |
| Upstream inputs | `../FS-M-001-integrated-actuator-system/inputs/INPUTS.md` |

## Question this study answers

What output torque and associated mechanical loads must the Kritva-M elbow actuator withstand across its proposed operating range, motion profiles, duty cycles and stop-impact scenarios, and what uncertainties prevent a defensible feasibility conclusion?

## Contents

| File or folder | Purpose | State |
|---|---|---|
| `SPECIFICATION.md` | Scope, requirements links, methods, acceptance criteria | Drafted, pending approval |
| `WORK_PLAN.md` | Work packages, 10-day schedule, milestones, status table | Drafted |
| `inputs/INPUTS.md` | Study-local inputs and index of upstream inputs used | Drafted |
| `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` | Study-local assumptions and open questions | Drafted |
| `REVIEW.md` | Review record skeleton (decision PENDING) | Skeleton |
| `calculations/`, `outputs/` | Mandatory evidence folders | Create when work starts; do not create empty folders to imply progress |
| `component_research/`, `references/`, `simulation/`, `CAD/`, `cost_estimate/`, `test_data/` | Conditional; see SPECIFICATION deliverable applicability | Per applicability decision |

## Start readiness (2026-10-24)

**Can start now (nominal, labelled ASSUMED/PRELIMINARY):** static gravity torque sweep 0–135° with a stated upper-arm orientation (FS2-IN-010); CoM and payload sensitivity; independent recalculation of arm inertia and stop energy; reflected inertia for 15:1, 20:1 and 25:1 with a parametric rotor-inertia range; reproduction of the 47.5 N·m screening estimate from `mechanical/calculations/LOAD_CASES.md` section 8.

**Needs a Project Lead decision before final conclusions:** acceleration profile (FS2-OQ-004), duty cycle, holding duration, peak duration and repetition (FS2-OQ-008), payload and external-contact loads and shock-load scope (FS2-OQ-009, upstream OQ-009), payload-position bounds (FS2-OQ-005), upper-arm orientation (FS2-OQ-011), final upper joint limit (FS2-OQ-010), independent reviewer (FS2-OQ-006). Until decided, dynamic, RMS and peak results are illustrative only.

**Needs CAD or a selected motor:** CAD centre of mass, mass properties, stop radius and overhang; rotor inertia (IN-014); friction model (FS2-OQ-003); bumper force-deflection curve. No CAD exists in the repository yet.

## How to start

1. Project Lead approves `SPECIFICATION.md` and records it in `registers/STUDY_REGISTER.csv`.
2. Assign the independent reviewer where the SPECIFICATION requires one. Without one, safety-critical results stay `NOT_VERIFIED`.
3. Run the work packages in `WORK_PLAN.md`, updating its status table and evidence paths.
4. Keep `inputs/INPUTS.md` current; use `FS<n>-IN-nnn` only for study-local inputs and never redefine upstream IN IDs.
5. Submit for review with `REVIEW.md` and `../../common/REVIEW_CHECKLIST.md`.

## Limits of this study

A positive result is a feasibility finding, not design approval, release approval or human-safety approval. All requirement values remain PROPOSED and are treated as PRELIMINARY.
