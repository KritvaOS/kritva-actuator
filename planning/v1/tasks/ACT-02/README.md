# Workstream ACT-02: Mechanical

This folder holds the task-management records for workstream **ACT-02**. It is a folder guide; the canonical task register is [`planning/v1/TASKS.md`](../../TASKS.md).

| Item | Value |
|---|---|
| Workstream | ACT-02: Mechanical |
| Owner | Mechanical Intern |
| Supporting / reviewers | Project Lead; Independent Mechanical Reviewer |
| Scope | Elbow load cases and mechanical requirements, motor/gearbox interface and gearbox comparison, shaft/bearing/housing calculations, CAD and drawings, fabrication and assembly, test fixture, mechanical characterisation, CAD release. |
| Design outputs live in | mechanical/, docs/mechanical/, results/mechanical/ |

## Tasks

| ID | Title | Week(s) | Status |
|---|---|---|---|
| ACT-02-001 | Define elbow load cases and mechanical requirements | 1 | READY |
| ACT-02-002 | Motor/gearbox interface constraints and gearbox comparison | 2 | PROPOSED |
| ACT-02-003 | Shaft, bearing and housing calculations | 3–4 | PROPOSED |
| ACT-02-004 | Mechanical CAD assembly and fabrication drawings | 3–5 | PROPOSED |
| ACT-02-005 | Fabrication and assembly | 6–7 | PROPOSED |
| ACT-02-006 | Mechanical characterisation | 8–10 | PROPOSED |
| ACT-02-007 | Test fixture design and build | 4–6 | PROPOSED |
| ACT-02-008 | Mechanical fixes, CAD release and documentation | 11–12 | PROPOSED |

The status column mirrors `planning/v1/TASKS.md`. If the two disagree, TASKS.md is authoritative.

## Folder convention

A **significant** task gets its own sub-folder `ACT-02/<TASK-ID>/` with five files:

| File | Owner | Purpose |
|---|---|---|
| `TASKS.md` | Project Lead maintains the status; the assignee updates progress | Scope, owner, dependencies, deliverables, status, links, progress log |
| `ACCEPTANCE_CRITERIA.md` | Project Lead defines or approves; the technical owner contributes | Observable pass/fail criteria and release conditions |
| `DESIGN_NOTES.md` | Assignee | Design choices, assumptions, calculations (or links to them), alternatives |
| `TEST_PLAN.md` | Assignee; the Project Lead approves the scope | Setup, instrumentation, procedure, conditions, expected results |
| `REVIEW.md` | Reviewer (never the author) | Findings, severity, required actions, evidence reviewed, disposition |

Small tasks can use a GitHub Issue (`task` template) instead of a folder.

## How to create a task folder

1. Confirm the task's scope and dependencies in `planning/v1/TASKS.md`. The Project Lead sets the status to `READY`.
2. Copy the five files from [`ACT-02-001/`](ACT-02-001/) and replace the task-specific content.
3. Link every deliverable by its repository path. **Never** copy design outputs into the task folder.
4. Open a branch `feature/<TASK-ID>-short-name` and reference the task ID in commits and PRs (see `CONTRIBUTING.md`).
5. When the work is complete, ask the reviewer named in `REVIEW.md` to review it. The Project Lead sets `DONE` only when the acceptance criteria are met with evidence.
