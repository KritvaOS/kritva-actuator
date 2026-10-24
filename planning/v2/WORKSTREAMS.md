# Kritva Actuator: Workstreams and Ownership (v2)

| Field | Value |
|---|---|
| Document ID | KA-PLAN-WORKSTREAMS |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.2 |
| Date | 2026-10-15 |
| Document owner | Project Lead |
| Reviewer / Approver | Project Lead |
| Applies to | A0, A1 |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** Proposed (ACT-DEC-024). Replaces the two-intern split in `planning/v1/TASKS.md` for new work. Legacy IDs remain valid; see `TASK_ID_MAPPING.csv`.

---

Program crosswalk: the workstreams ACT-S/M/L/EMB/INT are mapped to kritva-program workstreams in `PROGRAM_CROSSWALK.csv` (proposal; central approval pending). Task facts are published in each repository's `status/status.json`.

## 1. Workstreams

| Workstream | Repository | Owner | Scope | Task ID prefix |
|---|---|---|---|---|
| ACT-S | `kritva-actuator-s` | Mechanical Intern 1 | Kritva-S variant: CAD, drawings, BOM, sizing, mechanical tests | `ACT-S-` |
| ACT-M | `kritva-actuator-m` | Mechanical Intern 2 | Kritva-M variant (elbow baseline, A0 reference) | `ACT-M-` |
| ACT-L | `kritva-actuator-l` | Mechanical Intern 3 | Kritva-L variant | `ACT-L-` |
| ACT-EMB | `kritva-actuator-embedded` | Embedded Intern | Firmware, controller, electronics, CAN firmware, bring-up | `ACT-EMB-` |
| ACT-INT | parent | Project Lead / Integration Owner | Contracts, common sizing, driver, integration, validation, audits | `ACT-INT-` |

## 2. Rules

1. M is the reference. S and L reuse M's structure and review checklists. They do not start detailed design until M's sizing and Design review checklist are passed.
2. Mechanical interns do not edit the interface or protocol. They raise a design change request in the parent.
3. The embedded intern supports all three variants through one parameterised firmware (motor and gear ratio in a variant configuration), not three forks.
4. Hand-offs between workstreams are recorded in the parent as dependencies with the child commit SHA.
5. Only the Project Lead merges submodule pointer updates in the parent.

## 3. Cross-workstream dependencies

| From | To | Hand-off |
|---|---|---|
| ACT-M, ACT-S, ACT-L | ACT-EMB | Motor choice, Kt, pole pairs, gear ratio, encoder mount envelope, PCB envelope |
| ACT-EMB | ACT-M, ACT-S, ACT-L | Controller footprint, connector pinout, thermal limits |
| ACT-INT | all | Interface Control Document, units, CAN protocol, test procedure |
| all | ACT-INT | Evidence (results, BOM, CAD release) for gates and audits |

## 4. Legacy task mapping

`ACT-01-xxx` becomes `ACT-EMB-xxx`. `ACT-02-xxx` becomes `ACT-M-xxx` (inherits status), with `ACT-S-xxx` and `ACT-L-xxx` created as NOT_STARTED. `ACT-03-xxx` becomes `ACT-INT-xxx`. The full list is `TASK_ID_MAPPING.csv`.

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-15 | Kritvaos Actuator Team | Initial draft |
| 0.2 | 2026-10-16 | Kritvaos Actuator Team | Program crosswalk and status reporting reference (ACT-DEC-027) |
