# FS-M-003 — Motor selection and sizing

| Field | Value |
|---|---|
| Study ID | FS-M-003 |
| Product | Kritva-M (Level 2, Option C) |
| Priority | P1 |
| Lifecycle | PROPOSED |
| Verification status | NOT_STARTED |
| Review decision | PENDING |
| Owner | Mechanical Intern |
| Reviewer | Project Lead; Independent Reviewer TBD for safety-critical motor peak and thermal checks |
| Upstream studies | FS-M-001, FS-M-002 |
| Standard | `../../FEASIBILITY_STUDIES_STANDARD.md` (v0.4, proposed) |
| Canonical requirements | `requirements/SYSTEM_REQUIREMENTS.md` (rev 0.2, proposed) |
| Upstream inputs | `../FS-M-001-integrated-actuator-system/inputs/INPUTS.md` |

## Question this study answers

Can a commercially available BLDC/PMSM motor, operated from the proposed 24 V supply and paired with a feasible gearbox ratio, satisfy the load cases from FS-M-002 while meeting current, voltage, thermal, feedback, packaging, sourcing and cost constraints?

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

## How to start

Read the section "Repository starting evidence" at the end of `inputs/INPUTS.md` first. It lists draft repository documents that already cover part of this study and the gaps that remain.

1. Project Lead approves `SPECIFICATION.md` and records it in `registers/STUDY_REGISTER.csv`.
2. Assign the independent reviewer where the SPECIFICATION requires one. Without one, safety-critical results stay `NOT_VERIFIED`.
3. Run the work packages in `WORK_PLAN.md`, updating its status table and evidence paths.
4. Keep `inputs/INPUTS.md` current; use `FS<n>-IN-nnn` only for study-local inputs and never redefine upstream IN IDs.
5. Submit for review with `REVIEW.md` and `../../common/REVIEW_CHECKLIST.md`.

## Limits of this study

A positive result is a feasibility finding, not design approval, release approval or human-safety approval. All requirement values remain PROPOSED and are treated as PRELIMINARY.
