# FS-M-001 — Integrated Actuator System Feasibility

| Field | Value |
|---|---|
| Study ID | FS-M-001 |
| Product | Kritva-M (Level 2, Option C) |
| Priority | P0 |
| Lifecycle | PROPOSED |
| Verification status | NOT_STARTED |
| Review decision | PENDING |
| Owner | Mechanical Intern |
| Reviewer | Project Lead; Independent Reviewer TBD for safety-critical checks |
| Standard | `../../FEASIBILITY_STUDIES_STANDARD.md` (v0.3, proposed) |
| Canonical requirements | `requirements/SYSTEM_REQUIREMENTS.md` (rev 0.2, proposed) |

## Question this study answers

Can a Kritva-M actuator built from a commercial BLDC motor, commercial planetary gearbox, commercial encoder and bearings, with an in-house housing, 12 mm output shaft and controller, plausibly meet the proposed elbow load case (about 6.1 N·m gravity torque, 10 N·m continuous, 20–25 N·m peak, 45 RPM, 24 V) within the proposed A0 budget? It establishes the integrated baseline and the evidence gaps that FS-M-002 to FS-M-010 then close.

## Contents

| File or folder | Purpose | State |
|---|---|---|
| `SPECIFICATION.md` | Scope, requirements links, work packages, acceptance criteria AC-001..016 | Drafted, pending approval |
| `WORK_PLAN.md` | WP-01..07, 10-day schedule, milestones, schedule risks, status table | Drafted |
| `inputs/INPUTS.md` | Input register IN-001..IN-039 with status labels | Drafted |
| `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` | ASM-001..012 and OQ-001..014 | Drafted |
| `REVIEW.md` | Review record skeleton (decision PENDING) | Skeleton |
| `calculations/` | Gravity torque, ratio screening, shaft and stop checks | Not yet created (create when work starts) |
| `outputs/` | Requirement-to-evidence map, load cases, conclusion, risk register | Not yet created |
| `component_research/` | Motor and gearbox candidate datasheets and comparison | Conditional, create when needed |
| `cost_estimate/` | `BOM_COST_ESTIMATE.csv` | Conditional, create when needed |
| `references/`, `CAD/` | Source register, preliminary layout | Conditional |
| `simulation/`, `test_data/` | Not applicable for the initial baseline (see SPECIFICATION deliverable applicability) | NOT_APPLICABLE |

## How to start

1. Project Lead approves `SPECIFICATION.md` and records it in `registers/STUDY_REGISTER.csv`.
2. Assign an independent reviewer for shaft, bearing and stop checks (OQ-014). Without one, those checks stay `NOT_VERIFIED`.
3. Run WP-01 through WP-07 in order from `WORK_PLAN.md`, updating its status table and evidence paths.
4. Keep `inputs/INPUTS.md` current. Change inputs only with a recorded source and status.
5. Submit for review using `REVIEW.md` and `../../common/REVIEW_CHECKLIST.md`.

## Known issues carried in from earlier work

- 12 mm shaft versus 6202 bearing with a 15 mm bore (IN-016, OQ-011).
- EN8 normalised shaft safety factor about 0.86, so EN19 / 42CrMo4 Q&T is under consideration. The underlying calculation is not yet located (IN-037, OQ-012).
- A0 BOM about ₹22,000 against ₹10,000–₹15,000 budget (IN-020, IN-021).
- 20:1 needs a low-Kv pancake motor; about 37:1 suits a typical BLDC (IN-039).
- Duty cycle, peak duration, acceleration profile, ambient and life are undefined (IN-026 to IN-032).

## Related studies

Feeds FS-M-002 (load and torque), FS-M-003 (motor), FS-M-004 (gearbox), FS-M-005 (shaft), FS-M-006 (bearings), FS-M-007 (housing), FS-M-008 (electrical and thermal), FS-M-009 (cost) and FS-M-010 (integrated trade-off). See `../../registers/CROSS_STUDY_DEPENDENCIES.csv`.

## Limits of this study

A positive result is a feasibility finding, not design approval, release approval or human-safety approval. All requirement values remain PROPOSED and are treated as PRELIMINARY.
