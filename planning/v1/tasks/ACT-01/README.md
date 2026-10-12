# Workstream ACT-01: Electronics and motor control

This folder holds the task-management records for workstream **ACT-01**. It is a folder guide; the canonical task register is [`planning/v1/TASKS.md`](../../TASKS.md).

| Item | Value |
|---|---|
| Workstream | ACT-01: Electronics and motor control |
| Owner | Electronics/Embedded Intern |
| Supporting / reviewers | Project Lead; Independent Electrical/Firmware Reviewer |
| Scope | Electrical and motor-control requirements, MCU and development-board selection, motor bring-up and FOC, encoder integration, joint control, diagnostics and fault handling, custom controller PCB (A1), CAN firmware (A1), firmware release. |
| Design outputs live in | hardware/, firmware/, communication/can/firmware/, docs/electronics/, docs/firmware/, results/motor_control/, results/thermal/ |

## Tasks

| ID | Title | Week(s) | Status |
|---|---|---|---|
| ACT-01-001 | Define electrical and motor-control requirements | 1 | READY |
| ACT-01-002 | Select MCU/development board; bring up motor and FOC | 2–5 | PROPOSED |
| ACT-01-003 | Integrate encoder feedback and implement joint control | 5–7 | PROPOSED |
| ACT-01-004 | Diagnostics and fault handling | 8 | PROPOSED |
| ACT-01-005 | Custom controller PCB (A1) | 6–11 | PROPOSED |
| ACT-01-006 | CAN communication firmware (A1) | 9 | PROPOSED |
| ACT-01-007 | Firmware robustness, regression and release | 10–12 | PROPOSED |

The status column mirrors `planning/v1/TASKS.md`. If the two disagree, TASKS.md is authoritative.

## Folder convention

A **significant** task gets its own sub-folder `ACT-01/<TASK-ID>/` with five files:

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
2. Copy the five files from [`ACT-01-001/`](ACT-01-001/) and replace the task-specific content.
3. Link every deliverable by its repository path. **Never** copy design outputs into the task folder.
4. Open a branch `feature/<TASK-ID>-short-name` and reference the task ID in commits and PRs (see `CONTRIBUTING.md`).
5. When the work is complete, ask the reviewer named in `REVIEW.md` to review it. The Project Lead sets `DONE` only when the acceptance criteria are met with evidence.
