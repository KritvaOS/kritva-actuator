# Workstream ACT-03: Interface and integration

This folder holds the task-management records for workstream **ACT-03**. It is a folder guide; the canonical task register is [`planning/v1/TASKS.md`](../../TASKS.md).

| Item | Value |
|---|---|
| Workstream | ACT-03: Interface and integration |
| Owner | Project Lead / Integration Owner |
| Supporting / reviewers | Electronics/Embedded Intern; Mechanical Intern (parameters) |
| Scope | Actuator software interface and KritvaOS integration contract, CAN protocol, KritvaOS driver and host tools, simulation model, system validation and the A2 demonstration, traceability and audit coordination. |
| Design outputs live in | docs/interfaces/, communication/can/, software/, results/integration/, audit/ |

## Tasks

| ID | Title | Week(s) | Status |
|---|---|---|---|
| ACT-03-001 | Define the actuator software interface and KritvaOS integration contract | 1–3 | READY |
| ACT-03-002 | CAN protocol specification | 3–8 | PROPOSED |
| ACT-03-003 | KritvaOS driver and host tools | 5–10 | PROPOSED |
| ACT-03-004 | Simulation model (SimulatedActuator) | 6–10 | PROPOSED |
| ACT-03-005 | System validation and A2 demonstration | 10–12 | PROPOSED |
| ACT-03-006 | Traceability and audit coordination | 1–12 | IN_PROGRESS |

The status column mirrors `planning/v1/TASKS.md`. If the two disagree, TASKS.md is authoritative.

## Folder convention

A **significant** task gets its own sub-folder `ACT-03/<TASK-ID>/` with five files:

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
2. Copy the five files from [`ACT-03-001/`](ACT-03-001/) and replace the task-specific content.
3. Link every deliverable by its repository path. **Never** copy design outputs into the task folder.
4. Open a branch `feature/<TASK-ID>-short-name` and reference the task ID in commits and PRs (see `CONTRIBUTING.md`).
5. When the work is complete, ask the reviewer named in `REVIEW.md` to review it. The Project Lead sets `DONE` only when the acceptance criteria are met with evidence.
