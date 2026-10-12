# ACT-02-001: Acceptance Criteria

| Field | Value |
|---|---|
| Document ID | KA-TASK-ACT-02-001-AC |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead |
| Reviewer / Approver | Independent Mechanical Reviewer / Project Lead |
| Applies to | A1 |
| Classification | Proprietary and confidential |

> **Status note.** These criteria are proposed, pending Project Lead approval. Numerical limits that are not yet set must be approved **before** the related verification. They are never chosen after the results are known.

## 1. Task acceptance criteria

Each criterion is auditable: it states what evidence proves it. Weak criteria such as "load cases should be complete" are not used.

| # | Criterion | Evidence | Verification | Status |
|---|---|---|---|---|
| AC-01 | The static gravity torque is calculated with every assumption stated explicitly (masses, centre-of-mass distances, g, orientation). The result reproduces T_g = 6.08 N·m for the baseline inputs. | LOAD_CASES.md section with a worked calculation | Independent recalculation by the reviewer | NOT_STARTED |
| AC-02 | The 180 mm centre of mass is labelled provisional, with an owner and date for replacement by a CAD or measured value. Alternatively, it has already been replaced, with the source cited. | LOAD_CASES.md assumption table | Inspection | NOT_STARTED |
| AC-03 | A sensitivity table covers centre of mass 150/180/210 mm × payload 0.5/1.0/2.0 kg. | LOAD_CASES.md | Recalculation of at least 2 cells | NOT_STARTED |
| AC-04 | A dynamic load case is defined using an **approved** angular acceleration value. If none is approved yet, the item is recorded as an open TBD with owner and date, and ACT-02-002 is warned. | LOAD_CASES.md; DECISIONS.md entry | Inspection | NOT_STARTED |
| AC-05 | External output loads (radial, axial and moment at the bearing reference point) are tabulated for each load case, with the geometry stated (overhang distance, bearing reference). | LOAD_CASES.md load table | Reviewer cross-check with free-body diagrams | NOT_STARTED |
| AC-06 | The duty cycle is defined: horizontal holding duration, motion profile, peak duration, repetition and recovery. Undecided items are listed as TBD with an owner. | LOAD_CASES.md; DECISIONS.md | Inspection | NOT_STARTED |
| AC-07 | The arm inertia and hard-stop energy are calculated (point-mass baseline 0.171 kg·m² and ≈ 1.9 J at 45 RPM). The difference from the CAD value is noted when CAD becomes available. | LOAD_CASES.md | Recalculation | NOT_STARTED |
| AC-08 | `requirements/MECHANICAL_REQUIREMENTS.md` has been updated. Every load-related TBD is either closed or carries an owner and a needed-by date. | Diff in PR | Inspection | NOT_STARTED |
| AC-09 | Traceability CSV rows for MECH-REQ-001 and the load-case requirements are updated. | REQUIREMENTS_TRACEABILITY.csv | `make check-trace` passes | NOT_STARTED |
| AC-10 | The M0 review is complete, with no open CRITICAL or HIGH findings. | REVIEW.md | Reviewer sign-off (reviewer ≠ author) | NOT_STARTED |

## 2. Related mechanical gate criteria (context)

These project-level criteria depend on this task's output. They are listed so the assignee knows how the load cases will be used later. They are **not** closed by this task.

**Gate A: Design release**

- The CAD assembly includes the motor, gearbox, shaft, bearings, housing, encoder and a representative arm/link.
- The forearm/hand centre of mass has been measured or extracted from CAD, and the gravity torque has been recalculated (**this task provides the method**).
- The shaft combined bending/torsion, fatigue and deflection calculations have been reviewed.
- Bearing loads, life, fits, alignment and housing stiffness have been checked (**using this task's load table**).
- The gearbox ratings have been confirmed from manufacturer data.
- The mechanical BOM has exact part numbers, suppliers and current quotations.
- The independent design audit has no unresolved CRITICAL or HIGH findings.

**Gate B: Bench validation**

- The actuator holds the representative 1.5 kg arm plus 1 kg payload in the horizontal orientation.
- The ≈ 6.1 N·m gravity load has been independently verified using the final mass properties.

## 3. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
