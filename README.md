# Kritva Actuator

> Kritva Actuator Development Platform: an in-house smart rotary actuator for the elbow of the Kritva humanoid. It covers the motor-control electronics, FOC firmware, mechanical integration, CAN communication and KritvaOS integration. This is a private repository.

| Property | Value |
|---|---|
| Project | KritvaOS |
| Repository | `KritvaOS/kritva-actuator` |
| Repository Type | Hardware interface (parent repository of the actuator family) |
| Visibility Class | PRIVATE (future private; ACT-DEC-023, D-037, D-039) |
| GitHub Setting | PUBLIC (verified 2026-10-18; temporary, ACT-DEC-023 amendments and D-028: owner action returns it to private) |
| Lifecycle Status | ACTIVE (mechanical HOLD lifted by ACT-DEC-029; Gate A still required) |
| Repository Owner | Project Lead / Integration Owner ([role table](#15-ownership-and-escalation)) |
| Security Owner | Security Owner role ([SECURITY.md](SECURITY.md), program decision D-032) |
| Architecture | [docs/architecture/SYSTEM_ARCHITECTURE.md](docs/architecture/SYSTEM_ARCHITECTURE.md) and [docs/architecture/ACTUATOR_ARCHITECTURE.md](docs/architecture/ACTUATOR_ARCHITECTURE.md) |
| Milestones | [planning/v1/MILESTONE.md](planning/v1/MILESTONE.md) and [planning/v1/ROADMAP.md](planning/v1/ROADMAP.md) |
| Tasks | [planning/v1/TASKS.md](planning/v1/TASKS.md) and [status/tasks.csv](status/tasks.csv) |
| Acceptance Criteria | [requirements/SYSTEM_REQUIREMENTS.md](requirements/SYSTEM_REQUIREMENTS.md) and [docs/validation/](docs/validation/) |
| Status Reporting | [status/status.json](status/status.json) (generated, planning only) and [docs/standards/PROGRAM_ALIGNMENT.md](docs/standards/PROGRAM_ALIGNMENT.md) |
| License | [LICENSE](LICENSE) (proprietary, all rights reserved) |

> Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved. See [LICENSE](LICENSE).

This README follows the Kritva README standard (`v2/planning/standards/README_STANDARD.md` in [kritva-program](https://github.com/KritvaOS/kritva-program)). It is the entry point; the documents it links own the detail. Every value in sections 3 and 8 is a proposed planning value with the status stated there, not an approved requirement.

## 1. Purpose and Scope

The project follows **Option C**: an *educational motor-control platform* that evolves into a *smart actuator*, and then into a *humanoid joint actuator* (decision ACT-DEC-001). Its principle is **build once, evolve through iterations**. The first prototype is low cost, but its interfaces, firmware, mounting and tests are designed to be reused.

| Milestone | Name | Goal | Lead |
|---|---|---|---|
| **A0** | Educational Motor Control | FOC, current sensing, encoder feedback and basic closed-loop control on a motor-control development board | Electronics/Embedded Intern |
| **A1** | Humanoid Smart Actuator | Motor + commercial planetary gearbox + independent output shaft and bearings + output encoder + custom controller PCB + CAN; elbow load case (to be validated; see section 13) | Mechanical Intern + Electronics/Embedded Intern |
| **A2** | KritvaOS Integration | Actuator interface, KritvaOS driver, Kritva Edge integration, diagnostics, system tests | Project Lead / Integration Owner |

**Scope.** This parent repository owns the actuator's system requirements, planning, decisions, architecture, interface control (ICD, CAN protocol, units), the shared sizing engine, system-level integration software and tests, and the independent audits. Mechanical design of the S, M and L variants and the firmware and controller hardware live in the four child repositories (section 7). It is an experimental device and not a human-safe joint (section 13).

## 2. Position in the KritvaOS Ecosystem

The actuator drives a joint of the Kritva humanoid. The real-time side connects to KritvaOS EDGE and planning to KritvaOS NEXUS over CAN (A1) or USB/UART (A0). In the program's repository plan it follows kritva-core and kritva-motion and is the dependency of the four child repositories; the roster, order and required checks are owned by `v2/planning/repo-pipeline.json` in [kritva-program](https://github.com/KritvaOS/kritva-program), not by this README. Its status report is planning only and earns no program credit (section 10).

## 3. Architecture

```
  KritvaOS NEXUS (planning)  ->  KritvaOS EDGE (real-time joints)
                                        |
                                 CAN (A1) / USB-UART (A0)
                                        v
  +---------------------------- KRITVA ACTUATOR ----------------------------+
  | MCU: FOC, current sensing, encoder processing, joint control, faults    |
  |  -> gate driver -> 3-phase inverter -> BLDC/PMSM -> planetary gearbox    |
  |  -> 12 mm output shaft on dedicated bearings -> output encoder (feedback)|
  +-------------------------------------------------------------------------+
                                        |
                             forearm + hand + payload
```

The detailed architecture is in [docs/architecture/](docs/architecture/): [SYSTEM_ARCHITECTURE](docs/architecture/SYSTEM_ARCHITECTURE.md), [ACTUATOR_ARCHITECTURE](docs/architecture/ACTUATOR_ARCHITECTURE.md), [REPOSITORY_ARCHITECTURE](docs/architecture/REPOSITORY_ARCHITECTURE.md), [ACTUATOR_FAMILY_SPEC](docs/architecture/ACTUATOR_FAMILY_SPEC.md), [SOFTWARE_HARDWARE_BOUNDARY](docs/architecture/SOFTWARE_HARDWARE_BOUNDARY.md). Several of these are proposed decisions (ACT-DEC-024, 025, 026); read each document's own status.

### 3.1 Proposed design baseline (NOT approved, NOT frozen)

> **Status:** every value below is a **proposed target, pending approval**. ACT-DEC-008 (load and performance) and ACT-DEC-009 (output shaft) are still `PROPOSED`, and gate M0 is open. Nothing here may be used to buy components or release drawings until the decisions are `ACCEPTED` in [planning/v1/DECISIONS.md](planning/v1/DECISIONS.md) and Gate A has passed.

| Parameter | Proposed target |
|---|---|
| Application | Humanoid elbow, single rotary axis |
| Design load | Forearm + hand 1.5 kg (centre of mass 180 mm, provisional) + payload 1.0 kg at 350 mm, so T_g ≈ 6.1 N·m |
| Continuous output torque | 10 N·m |
| Peak output torque | 20 N·m minimum, 25 N·m stretch (duration not yet defined) |
| Output speed | up to 45 RPM |
| Supply | 24 V DC nominal |
| Motor | Commercial BLDC/PMSM, 75–100 W continuous mechanical (candidate range) |
| Reduction | Commercial planetary; 20:1 first candidate, 15:1 and 25:1 alternatives |
| Output | Independent 12 mm shaft (initial CAD, not frozen) on a dedicated bearing pair (baseline 6202 on 15 mm seats until the balanced stop is proven) |
| Feedback | Output-side encoder plus motor-side feedback for FOC |
| Control | FOC with current sensing; position, velocity and torque control |
| Communication | USB/UART (A0); CAN (A1) |
| MCU | STM32G4-class proposed (TI C2000 alternative), not frozen |
| Budget (provisional) | A0 ₹10,000–₹15,000; A1 ₹20,000–₹30,000 cumulative |

## 4. Documents to Read First

| # | Document | Label, status | What it answers |
|---|---|---|---|
| 1 | [requirements/SYSTEM_REQUIREMENTS.md](requirements/SYSTEM_REQUIREMENTS.md) | AUTHORITATIVE for the system requirements; PROPOSED (draft baseline pending approval) | What the actuator must do; the parent of everything else. Until approval is recorded, work follows it as a proposed baseline and the owner's recorded decisions |
| 2 | [requirements/ACTUATOR_SPECIFICATION.md](requirements/ACTUATOR_SPECIFICATION.md) | AUTHORITATIVE for the datasheet-level targets; PROPOSED | Datasheet-level targets and the elbow load model |
| 3 | [planning/v1/ROADMAP.md](planning/v1/ROADMAP.md), [MILESTONE.md](planning/v1/MILESTONE.md), [TASKS.md](planning/v1/TASKS.md) | AUTHORITATIVE for the plan, gates and task owners; status per document (planning information, not approved commitments) | The plan, the gates and who does what |
| 4 | [docs/architecture/SYSTEM_ARCHITECTURE.md](docs/architecture/SYSTEM_ARCHITECTURE.md) | REFERENCE | How it fits together |
| 5 | [planning/v1/tasks/](planning/v1/tasks/) | INPUT | Your workstream folder |
| 6 | [REPOSITORY_ARCHITECTURE](docs/architecture/REPOSITORY_ARCHITECTURE.md), [ACTUATOR_FAMILY_SPEC](docs/architecture/ACTUATOR_FAMILY_SPEC.md), [planning/v2/](planning/v2/README.md) | AUTHORITATIVE for the repository layout and the family classes; PROPOSED (ACT-DEC-024, ACT-DEC-025) | The parent plus four submodules; migration stages 1 to 4 are done, stage 5 adds the submodules |
| 7 | [AGENTS.md](AGENTS.md), [CONTRIBUTING.md](CONTRIBUTING.md) | AUTHORITATIVE for contributor and agent rules; in force | Rules for agents and contributors |

A label names a role, not an approval. Where this README states a document's status it is shown; otherwise read the document's own header.

## 5. Repository Structure and File Responsibilities

The tree below is a conceptual ownership map, not a listing of what exists. Implementation state: `mechanical/common-sizing/`, `mechanical/calculations/`, `docs/`, `requirements/`, `planning/`, `audit/` and the validation scripts hold real files (IMPLEMENTED as documents and checks, and PROPOSED where a document says so); `software/`, `results/`, `communication/can/` and the system-level `tests/` are scaffolding with no implementation (NOT YET IMPLEMENTED); the child repositories are described in the next paragraph. A folder or document existing is not evidence that the design or integration it names is built or accepted.

**Submodule states.** Four conditions are different and are not interchangeable: the submodule is configured in `.gitmodules`; the parent commit records a pointer; a clone has initialised the checkout (`git submodule update --init`); and the child implementation is verified. This README claims only the first two (checked by `make check-submodules`). Whether a child is checked out or verified depends on your clone and on that child's own records.

This is the parent (program and integration) repository. Four child repositories are Git submodules (ACT-DEC-024). Clone with `git clone --recurse-submodules`.

```
kritva-actuator/                              parent
├── README.md, LICENSE, CONTRIBUTING.md, CODE_OF_CONDUCT.md, CHANGELOG.md, Makefile, .gitignore, .gitattributes, .gitmodules
├── requirements/        What the actuator must do (canonical): SYSTEM, ACTUATOR_SPECIFICATION, MECHANICAL,
│                        ELECTRICAL, FIRMWARE, INTERFACE, SAFETY requirements
├── planning/v1/         Roadmap, milestones, task register, decisions, risks; tasks/ACT-01..03 task records
├── planning/v2/         Four-submodule plan: migration plan and manifest, task ID mapping, workstreams, 24-week roadmap, reforecast (P1-P58)
├── docs/
│   ├── architecture/    System, actuator, repository and family architecture, sourcing and cost
│   ├── interfaces/      Interface control document, actuator interface (API), CAN protocol, unit conventions
│   ├── mechanical/      Common mechanical specification, materials, assembly, fabrication
│   ├── standards/       CAD naming, BOM, design review, release, submodule workflow
│   └── validation/      Validation plan, test equipment, performance characterisation
├── mechanical/
│   ├── common-sizing/   Shared sizing engine and reference results
│   ├── calculations/    A0 reference baseline calculations (elbow case)
│   ├── actuator-s/      submodule: KritvaOS/kritva-actuator-s  (Kritva-S)
│   ├── actuator-m/      submodule: KritvaOS/kritva-actuator-m  (Kritva-M, A0 reference)
│   └── actuator-l/      submodule: KritvaOS/kritva-actuator-l  (Kritva-L)
├── embedded/
│   └── kritva-actuator-embedded/   submodule: firmware, controller hardware, electronics and firmware docs, electrical BOM
├── communication/can/   CAN protocol definitions (protocol/, tools/)
├── software/            actuator_interface, kritva_driver, host_tools, simulation
├── tests/               integration, performance, safety (system-level test procedures)
├── audit/               Independent reviews: traceability, mechanical/electronics/firmware audits, release audit
├── results/             System-level evidence: integration, thermal
├── scripts/             validation (doc, link, traceability, calculation, manifest checks), bom, integration (submodule and migration tools)
└── .github/             Issue and PR templates, CI workflows
```

| Path | Responsibility | Label | Edit by hand? |
|---|---|---|---|
| [requirements/](requirements/) | What the actuator must do (canonical) | AUTHORITATIVE | yes, with review |
| [planning/v1/](planning/v1/) | Roadmap, milestones, task register, decisions, risks | MIXED: AUTHORITATIVE per document | per document |
| [planning/v2/](planning/v2/) | Four-submodule plan, task ID mapping, roadmaps | MIXED: AUTHORITATIVE and INPUT per file | per file; IDs only by owner decision |
| [docs/](docs/) | Architecture, interfaces, procedures, standards, validation approach | MIXED: AUTHORITATIVE and REFERENCE per document | per document |
| [mechanical/common-sizing/](mechanical/common-sizing/), [mechanical/calculations/](mechanical/calculations/) | Shared sizing engine and reference results | INPUT and EVIDENCE | with the regression check |
| `mechanical/actuator-s`, `-m`, `-l`, `embedded/kritva-actuator-embedded` | Child repositories (submodules) | SNAPSHOT pointers | one reviewed pointer bump at a time |
| [communication/can/](communication/can/), [software/](software/) | CAN protocol definitions and integration software | INPUT; NOT YET IMPLEMENTED (scaffold only) | yes, with tests |
| [tests/](tests/), [results/](results/) | System-level test procedures; measured evidence | EVIDENCE; NOT YET IMPLEMENTED (almost empty; no measured result exists) | append only for results |
| [audit/](audit/) | Independent reviews and gate decisions | EVIDENCE | append only |
| [status/status.json](status/status.json) | Program status report | GENERATED from `status/tasks.csv` | no: regenerate |
| [scripts/](scripts/) | Validation, BOM, integration, status and security tools | INPUT | yes, with checks |

### Ownership rules (ACT-DEC-011)

- `requirements/` is the canonical source of **what** the actuator must do.
- `planning/v1/` holds **planned work, owners and approvals**.
- `docs/` explains architecture, procedures, interfaces and the validation approach.
- The implementation directories hold the artefacts.
- `tests/` holds test code and procedures. `results/` holds measured evidence.
- `audit/` holds independent reviews and gate decisions. It never duplicates design documents.
- **One canonical home per artefact.** Link to records; don't copy them.
- Folders are populated incrementally. A `.gitkeep` marks an agreed, still-empty folder.

## 6. Toolchain and Development Workflow

Python 3.8 or later is needed; the scripts use the standard library only. Tool-flow documents: [docs/standards/TOOLFLOW_MECHANICAL.md](docs/standards/TOOLFLOW_MECHANICAL.md), [docs/standards/TOOLFLOW_ELECTRONICS_EMBEDDED.md](docs/standards/TOOLFLOW_ELECTRONICS_EMBEDDED.md), [docs/standards/OPEN_SOURCE_TOOLFLOW.md](docs/standards/OPEN_SOURCE_TOOLFLOW.md). Submodule handling: [docs/standards/SUBMODULE_WORKFLOW.md](docs/standards/SUBMODULE_WORKFLOW.md).

```bash
make help          # list targets
make check         # run all documentation, traceability and BOM checks
make check-docs    # document headers and revision history
make check-links   # relative links
make check-trace   # traceability CSV versus requirement IDs
make check-bom     # mechanical and electrical BOM schema
make check-calcs   # calculation regression + document consistency
make bom-summary   # BOM cost totals by milestone and category
make calc          # run the mechanical sizing calculations (prints; writes no file)
make clean         # MODIFIES local files: deletes __pycache__ and *.pyc
```

The `check*` targets are read-only checks, and `make calc` and `make bom-summary` print to the terminal and write no repository file. `make clean` is different: it modifies local files (it deletes `__pycache__` folders and `*.pyc` files and nothing else). No target modifies remote state. This statement covers the targets listed above and in section 11; run `make help` for the complete list.

## 7. Dependencies and Interfaces

| Dependency | Direction | Kind | Contract | State |
|---|---|---|---|---|
| [kritva-actuator-m](https://github.com/KritvaOS/kritva-actuator-m), [-s](https://github.com/KritvaOS/kritva-actuator-s), [-l](https://github.com/KritvaOS/kritva-actuator-l) | downstream (submodules) | mechanical design | ICD and common mechanical spec in this repository | child repositories exist; layout is a PROPOSED decision (ACT-DEC-024) |
| [kritva-actuator-embedded](https://github.com/KritvaOS/kritva-actuator-embedded) | downstream (submodule) | firmware and controller hardware | CAN protocol and interface documents in this repository | exists; layout PROPOSED (ACT-DEC-024) |
| KritvaOS EDGE and NEXUS | upstream consumer | runtime integration over CAN or USB/UART | [docs/interfaces/](docs/interfaces/) | PLANNED (stage A2) |
| kritva-core, kritva-motion | upstream | not yet specified here | none in this repository | PROPOSED: ordered before the actuator in the program's repository plan |
| kritva-program | upstream | governance | status schema 2.0 ([docs/standards/PROGRAM_ALIGNMENT.md](docs/standards/PROGRAM_ALIGNMENT.md)) | ESTABLISHED for the schema; the report is planning only |

Interface, CAN protocol, units and shared requirements are owned here; a child repository does not redefine them. That is an ownership rule recorded in `AGENTS.md`; no automated test checks that a child conforms to the interface yet, and the interface documents are PROPOSED until approved. Five kinds of relationship are kept apart: program ordering (the repository plan), Git submodule (configured and pinned, section 5), source or build dependency, runtime integration, and governance or status reporting. A PROPOSED or PLANNED dependency is not an integration that exists, and placing kritva-core or kritva-motion before the actuator in the program plan is ordering only.

## 8. Milestones and Implementation Plan

**Status: provisional planning information. Not approved requirements.** Stage scope is held in `planning/v1/ROADMAP.md` and `planning/v1/MILESTONE.md`; class ranges in `docs/architecture/ACTUATOR_FAMILY_SPEC.md` (ACT-DEC-025, PROPOSED). Budgets are provisional. Nothing here authorises purchase, fabrication or design freeze.

### Stage comparison: A0 and A1

| Item | A0: Educational Motor Control | A1: Humanoid Smart Actuator |
|---|---|---|
| Primary objective | Learn and validate motor control; build the reusable electronics and firmware base | Working actuator module: motor, gearbox, output shaft and bearings, output encoder, controller, CAN |
| Motor | Low-cost commercial BLDC/PMSM | Commercial BLDC/PMSM selected from the sizing results (ACT-DEC-003, 008 pending) |
| Controller | Motor-control development board (about ₹3,000-₹5,000) | Custom controller PCB (repository baseline) |
| Position control | FOC with current sensing; basic closed-loop position and speed | Position, velocity and torque control on the actuator |
| Encoder | Motor-side feedback | Motor-side feedback plus output-side encoder |
| Communication | USB/UART | CAN (firmware and protocol per the parent ICD) |
| Diagnostics | Basic status, faults, logging | Fault handling, thermal and current limits, CAN diagnostics |
| Mechanical design | Mounting and bench fixture only | Commercial planetary gearbox, independent output shaft and bearings, housing (HOLD lifted by ACT-DEC-029; Gate A still required) |
| Validation | Bench tests on a restrained fixture | Elbow load case; Gates A/B/C with independent review (ACT-DEC-014, 015) |
| Budget (provisional) | ₹10,000-₹15,000 | ₹20,000-₹30,000, cumulative including A0 |
| Deliverable | Working motor-control platform with firmware, tests and documents | Target: an actuator ready for validation, with CAD, BOM, firmware and test reports. "Validated" is a future outcome that depends on the physical tests and Gates A, B and C; it does not describe the current state |

Dates, phase numbers and checkpoints are proposed planning targets, not approved delivery commitments. The current reforecast, including the A0 exit, Gate A and the M prototype checkpoint, is in `planning/v2/ROADMAP_48_WEEKS.md` and the decisions it cites (ACT-DEC-032, ACT-DEC-033); read that record for any date. The custom controller PCB and CAN firmware stay the A1 baseline; a development-board substitute is a reviewed deviation. Stage names above are the official names.

### Variant classes (provisional)

| Class | Repository baseline (ACT-DEC-025, PROPOSED) | Wider planning range (under review, not approved) | Typical joints |
|---|---|---|---|
| Kritva-S | 2-5 N·m continuous, 5-10 N·m peak, about 60 RPM | 2-5 / 5-10 N·m | Wrist, neck |
| Kritva-M | 10 N·m continuous, 20-25 N·m peak, 45 RPM (elbow baseline and A0 reference, ACT-DEC-008) | 5-20 / 20-40 N·m | Elbow, shoulder (shoulder not yet in the spec) |
| Kritva-L | 25-40 N·m continuous, 50-80 N·m peak, about 20-40 RPM | 20-80 / 80-150 N·m | Hip, knee, ankle (ankle not yet in the spec) |

Use the repository baseline column for sizing and reviews. The wider range is a discussion input; it becomes a requirement only after the owner records it in `planning/v1/DECISIONS.md`. For L the two columns differ materially, so confirm the intended load cases first.

| Plan | Status and meaning of dates |
|---|---|
| [planning/v1/ROADMAP.md](planning/v1/ROADMAP.md), [MILESTONE.md](planning/v1/MILESTONE.md) | Stage scope and gates; read each document's own status |
| [planning/v2/ROADMAP_48_WEEKS.md](planning/v2/ROADMAP_48_WEEKS.md), [ROADMAP_24_WEEKS.md](planning/v2/ROADMAP_24_WEEKS.md), [ROADMAP_12_MONTHS.md](planning/v2/ROADMAP_12_MONTHS.md) | Proposed reforecasts; dates are proposed targets awaiting Project Lead confirmation, not delivery commitments |

## 9. Tasks and Acceptance Criteria

- **Where tasks live.** [planning/v1/TASKS.md](planning/v1/TASKS.md) and the task records in [planning/v1/tasks/](planning/v1/tasks/). Task facts for status reporting are in [status/tasks.csv](status/tasks.csv). [planning/v2/TASK_ID_MAPPING.csv](planning/v2/TASK_ID_MAPPING.csv) maps these IDs to the program inventory; IDs and rows change only by owner decision.
- **Acceptance.** Requirements carry their own acceptance in [requirements/](requirements/); verification is planned in [docs/validation/](docs/validation/); gates A, B and C and the mechanical, electronics and firmware gates are in [planning/v1/MILESTONE.md](planning/v1/MILESTONE.md) and recorded in [audit/](audit/). Work is not accepted because code, a CAD file, a commit, a merged pull request or a bench result exists.

- **Requirement IDs:** `SYS-REQ-NNN` (system), `ACT-REQ`, `MECH-REQ`, `ELEC-REQ`, `FW-REQ` / `CTRL-REQ`, `IF-REQ`, `SAF-REQ`.
- **Verification status:** `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `PASS_WITH_ACTIONS`, `FAIL`, `NOT_VERIFIED`.
- **Gates:** A (design release), B (bench validation), C (safety and release); mechanical M0–M4, electronics E0–E4, firmware F0–F4.
- **Units:** SI. Documents use N·m, RPM, ° and °C; firmware and protocol use rad, rad/s, N·m, A, V and °C. q = 0 at full extension, positive in flexion.
- **Every document** carries the KA- header table and a revision history.
- **Every test record** states the hardware revision, firmware version, supply voltage, load, ambient temperature, instruments and results.

## 10. Status Reporting and Program Integration

`status/status.json` (schema 2.0) is generated by `scripts/status/gen_status.py` from `status/tasks.csv` and checked by `make check-status`. It is planning only: it reports task facts (execution, git sync, readiness; evidence stays empty until recorded centrally), marks no task accepted, and creates no program credit. How the five actuator repositories report is in [docs/standards/PROGRAM_ALIGNMENT.md](docs/standards/PROGRAM_ALIGNMENT.md) (PROPOSED, ACT-DEC-027).

| Dimension | Source record | Authority |
|---|---|---|
| Execution | `status/tasks.csv`, reported in `status/status.json` | The task owner records it; the Project Lead approves |
| Evidence | A record in [results/](results/) or [audit/](audit/) naming the commit, hardware revision, firmware version, test conditions and result, with its scope | The author records it; a reviewer other than the author checks it |
| Acceptance | The gate and audit records in [audit/](audit/) | The independent reviewer and the Project Lead, never a status report |
| Release readiness | The result of Gates A, B and C | Project Lead with a qualified safety reviewer |

Evidence has types that are not interchangeable: a software test, a calculation, a simulation, a bench measurement and an independently accepted physical test support different claims. Today `status/status.json` carries no evidence (the field stays empty until recorded centrally), so it reports planning state only. The generated report is a snapshot that can lag its inputs, cannot approve its own work, and does not establish physical safety or program credit.

| Item | Status (planning information; read the linked record for the current state) |
|---|---|
| Documentation baseline (requirements, planning, docs, calculations, audit framework) | Draft 0.1, proposed, pending approval; external audit 2026-10-12: M0 FAIL, not ready (see [audit/external/](audit/external/)) |
| A0, A1, A2 | Not started |

Repository visibility is not a status item: see the metadata table and ACT-DEC-023 in [planning/v1/DECISIONS.md](planning/v1/DECISIONS.md).

## 11. Build, Test, Regression and Validation

| Check | Command | Effect | Runs in CI? |
|---|---|---|---|
| Document headers and revision history | `make check-docs` | check | yes (`docs-checks`) |
| Relative links | `make check-links` | check | yes |
| Traceability CSV against requirement IDs | `make check-trace` | check | yes |
| BOM schema | `make check-bom` | check | yes |
| Calculation regression and document consistency | `make check-calcs` | check | yes |
| Migration manifest against the tree | `make check-manifest` | check | yes |
| Submodule layout | `make check-submodules` | check | yes |
| Status report against `status/tasks.csv` | `make check-status` | check | yes |
| All of the above | `make check` | check | yes |
| README standard | `make check-readme` | check | yes (`readme-check`; not a required check yet, D-067) |
| Remove Python caches (`__pycache__`, `*.pyc`) | `make clean` | modify (deletes local cache files only) | no |
| Firmware build | see the `firmware-build` workflow | build | yes (workflow) |

These are software and document checks. A passing run does not show physical safety, design acceptance or a closed gate (section 13). Hardware tests are not run in CI and need a restrained, instrumented fixture (section 13). A test that is not run is recorded as `NOT_VERIFIED`, never as passing. System-level test procedures are in [tests/](tests/); evidence is in [results/](results/).

## 12. Git Workflow and Review

This repository's approved convention is [CONTRIBUTING.md](CONTRIBUTING.md): branch from `main`, prefix the commit message with the task ID (`ACT-02-003: add combined-stress check for 12 mm shaft`), imperative mood, a summary of 72 characters or fewer, one logical change per commit, and a pull request that links the task and requirement IDs and passes `make check`. This is the one controlling commit rule here. What CI enforces is only that a commit carries no AI session trailer or link (the `commit-message-check` workflow); the task-ID prefix is a convention. The Kritva commit standard (Conventional Commits with a `Task:` or `Tasks:` footer, kritva-program D-053) has **not** been adopted by this repository (PD-019 in kritva-program); it is advisory reference only, not a second mandatory format. Its checker is present in `scripts/security/check_commit_format.py` and is not enforced. `AGENTS.md` and `CONTRIBUTING.md` describe the same convention; a commit that implements no task has no task ID to prefix, and the repository does not yet define a separate form for it.

A safety-relevant change needs an independent review (ACT-DEC-014): if no qualified reviewer is available the review is recorded `NOT_VERIFIED` and the gate stays blocked. Required checks and approvals for pull requests are listed in the program's repository plan.

## 13. Safety and Security

The actuator is an **experimental device and not a human-safe joint**.

- Loaded, peak and fault tests happen **only on a restrained, guarded, instrumented fixture**.
- Never resist the actuator by hand or attach it to a person.
- Bring-up uses a current-limited PSU and a hardware e-stop.

See [requirements/SAFETY_REQUIREMENTS.md](requirements/SAFETY_REQUIREMENTS.md).

**Limits of software evidence.** Software checks, analytical calculations and simulation validate only the stated model, inputs and software properties. They do not establish physical safety, component suitability, design acceptance or readiness for human use. Physical test evidence, independent domain review and the applicable gate approvals are required separately. `make check` and `make check-calcs` are software and document checks of this kind.

**Open gates.** The lifecycle status ACTIVE describes the repository and its workstream; it says nothing about hardware readiness. Lifting the mechanical HOLD (ACT-DEC-029) does not approve a design, waive a gate or authorise physical operation. The gate records and their status are in [audit/release/](audit/release/) and `planning/v1/MILESTONE.md` (sections 6.4 and 8.4); this table summarises what each gate controls and does not state its current status.

| Gate | Controls | Required closed inputs | Decision maker | Prohibited while open |
|---|---|---|---|---|
| A, design release | Release of the design for fabrication | M0, M1, M2; E1; E2 schematic stage for housing and connector interfaces; independent calculation review (SAF-REQ-044) | Project Lead | Fabrication, and the first loaded test |
| B, bench validation | Claims that the bench performance targets are met | M3, E3, F3 (bench scope) | Project Lead | Treating any performance target as demonstrated |
| C, safety and release | Safety sign-off and release | M4, E4, F3; verification of every SAF-REQ item (SAF-REQ-080) | Project Lead with a qualified safety reviewer | Release, and any use outside the restrained, guarded, instrumented fixture |


- **Independent review.** No author approves their own safety-critical design. Gates A, B and C and the mechanical (M0 to M4), electronics (E0 to E4) and firmware (F0 to F4) gates stay open until independently reviewed and recorded in [audit/](audit/); software checks and calculations do not close a physical safety gate.
- **Vulnerabilities.** Report as described in [SECURITY.md](SECURITY.md); its private reporting route is not yet verified, and it says so. Never put details of an unfixed vulnerability in a public issue, pull request or commit message. Never commit secrets; the `secret-scan` workflow runs on every push and pull request.

## 14. Release and Versioning

Releases are tagged per milestone, for example `A0-v0.1.0` ([CHANGELOG.md](CHANGELOG.md)). The release criteria are in [docs/standards/RELEASE_CHECKLIST.md](docs/standards/RELEASE_CHECKLIST.md) and the design review in [docs/standards/DESIGN_REVIEW_CHECKLIST.md](docs/standards/DESIGN_REVIEW_CHECKLIST.md). A tag is evidence, not acceptance: a release needs Gate C. This README records no release state.

## 15. Ownership and Escalation

| Role | Owns |
|---|---|
| Project Lead | System requirements, planning, decisions, integration, release approval |
| Mechanical Intern | Mechanical design, calculations, CAD, fabrication, mechanical tests |
| Electronics/Embedded Intern | Electronics, motor-control firmware, encoder sensing, electrical tests |
| Independent Mechanical Reviewer | Mechanical audits (M0–M4) |
| Independent Electrical/Firmware Reviewer | Electronics and firmware audits (E0–E4, F0–F4) |

No author approves their own safety-critical design. If no qualified reviewer is available, the review is recorded as `NOT_VERIFIED` and the gate stays blocked (ACT-DEC-014).

## 16. Related Repositories and References

| Repository | Relationship |
|---|---|
| [kritva-program](https://github.com/KritvaOS/kritva-program) | Program plan, baseline, decisions, status consolidation, README standard |
| [kritva-actuator-embedded](https://github.com/KritvaOS/kritva-actuator-embedded), [kritva-actuator-s](https://github.com/KritvaOS/kritva-actuator-s), [kritva-actuator-m](https://github.com/KritvaOS/kritva-actuator-m), [kritva-actuator-l](https://github.com/KritvaOS/kritva-actuator-l) | Child repositories (submodules) |
| [kritva-core](https://github.com/KritvaOS/kritva-core), [kritva-motion](https://github.com/KritvaOS/kritva-motion) | Upstream in the program's repository plan (PROPOSED) |

## 17. License

Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved. See [LICENSE](LICENSE).
