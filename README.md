# Kritva Actuator

**Kritva Actuator Development Platform**: an in-house smart rotary actuator for the elbow of the Kritva humanoid. It covers the motor-control electronics, FOC firmware, mechanical integration, CAN communication and KritvaOS integration.

> Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved. See [LICENSE](LICENSE).

---

## 1. What this project is

The project follows **Option C**: an *educational motor-control platform* that evolves into a *smart actuator*, and then into a *humanoid joint actuator* (decision ACT-DEC-001). Its principle is **build once, evolve through iterations**. The first prototype is low cost, but its interfaces, firmware, mounting and tests are designed to be reused.

| Milestone | Name | Goal | Lead |
|---|---|---|---|
| **A0** | Educational Motor Control | FOC, current sensing, encoder feedback and basic closed-loop control on a motor-control development board | Electronics/Embedded Intern |
| **A1** | Humanoid Smart Actuator | Motor + commercial planetary gearbox + independent output shaft and bearings + output encoder + custom controller PCB + CAN; elbow load case validated | Mechanical Intern + Electronics/Embedded Intern |
| **A2** | KritvaOS Integration | Actuator interface, KritvaOS driver, Kritva Edge integration, diagnostics, system tests | Project Lead / Integration Owner |

### 1.1 Proposed design baseline (NOT approved, NOT frozen)

> **Status:** every value below is a **proposed target, pending approval**. ACT-DEC-008 (load and performance) and ACT-DEC-009 (output shaft) are still `PROPOSED`, and gate M0 is open. Nothing here may be used to buy components or release drawings until the decisions are `ACCEPTED` in [planning/v1/DECISIONS.md](planning/v1/DECISIONS.md) and Gate A has passed.

| Parameter | Proposed target |
|---|---|
| Application | Humanoid elbow, single rotary axis |
| Design load | Forearm + hand 1.5 kg (centre of mass 180 mm, provisional) + payload 1.0 kg at 350 mm, so T_g ≈ 6.1 N·m |
| Continuous output torque | 10 N·m |
| Peak output torque | 20 N·m minimum, 25 N·m stretch (duration TBD) |
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

### 1.2 Architecture

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

## 2. Where to start

1. **[requirements/SYSTEM_REQUIREMENTS.md](requirements/SYSTEM_REQUIREMENTS.md)**: what the actuator must do. This is the parent of everything else.
2. **[requirements/ACTUATOR_SPECIFICATION.md](requirements/ACTUATOR_SPECIFICATION.md)**: datasheet-level targets and the elbow load model.
3. **[planning/v1/ROADMAP.md](planning/v1/ROADMAP.md)**, **[MILESTONE.md](planning/v1/MILESTONE.md)** and **[TASKS.md](planning/v1/TASKS.md)**: the plan, the gates and who does what.
4. **[docs/architecture/SYSTEM_ARCHITECTURE.md](docs/architecture/SYSTEM_ARCHITECTURE.md)**: how it fits together.
5. Your workstream folder in [planning/v1/tasks/](planning/v1/tasks/).

## 3. Repository structure

```
kritva-actuator/
├── README.md, LICENSE, CONTRIBUTING.md, CODE_OF_CONDUCT.md, CHANGELOG.md, Makefile, .gitignore, .gitattributes
├── requirements/        What the actuator must do (canonical): SYSTEM, ACTUATOR_SPECIFICATION, MECHANICAL,
│                        ELECTRICAL, FIRMWARE, INTERFACE, SAFETY requirements
├── planning/v1/         Roadmap, milestones, task register, decisions, risks; tasks/ACT-01..03 task records
├── docs/
│   ├── architecture/    System and actuator architecture, software/hardware boundary
│   ├── mechanical/      Mechanical design specification, materials, assembly, fabrication
│   ├── electronics/     Electronics architecture, motor-controller specification, hardware bring-up
│   ├── firmware/        Firmware architecture, motor control, calibration
│   ├── interfaces/      Actuator interface (API, parameters), CAN protocol, unit conventions
│   └── validation/      Validation plan, test equipment, performance characterisation
├── mechanical/          CAD (assembly, housing, shafts, brackets, encoder_mount), drawings,
│                        calculations (load cases, torque/speed, shaft, bearings, gearbox), BOM, assembly
├── hardware/            Motor controller (development board, custom PCB), power stage, sensing, connectors, BOM
├── firmware/            platform, foc, motor_control, encoder, joint_control, diagnostics, communication
├── communication/can/   CAN protocol definitions, shared firmware and tools
├── software/            actuator_interface, kritva_driver, host_tools, simulation
├── tests/               unit, firmware, hardware, mechanical, integration, performance, safety (test code and procedures)
├── audit/               Independent reviews: traceability, mechanical/electronics/firmware audits, release audit
├── results/             Measured evidence: mechanical, motor_control, thermal, integration
├── scripts/             validation (doc, link and traceability checks), bom (BOM checks and summaries)
└── .github/             Issue and PR templates, CI workflows
```

### 3.1 Ownership rules (ACT-DEC-011)

- `requirements/` is the canonical source of **what** the actuator must do.
- `planning/v1/` holds **planned work, owners and approvals**.
- `docs/` explains architecture, procedures, interfaces and the validation approach.
- The implementation directories hold the artefacts.
- `tests/` holds test code and procedures. `results/` holds measured evidence.
- `audit/` holds independent reviews and gate decisions. It never duplicates design documents.
- **One canonical home per artefact.** Link to records; don't copy them.
- Folders are populated incrementally. A `.gitkeep` marks an agreed, still-empty folder.

## 4. Roles

| Role | Owns |
|---|---|
| Project Lead | System requirements, planning, decisions, integration, release approval |
| Mechanical Intern | Mechanical design, calculations, CAD, fabrication, mechanical tests |
| Electronics/Embedded Intern | Electronics, motor-control firmware, encoder sensing, electrical tests |
| Independent Mechanical Reviewer | Mechanical audits (M0–M4) |
| Independent Electrical/Firmware Reviewer | Electronics and firmware audits (E0–E4, F0–F4) |

No author approves their own safety-critical design. If no qualified reviewer is available, the review is recorded as `NOT_VERIFIED` and the gate stays blocked (ACT-DEC-014).

## 5. Conventions

- **Requirement IDs:** `SYS-REQ-NNN` (system), `ACT-REQ`, `MECH-REQ`, `ELEC-REQ`, `FW-REQ` / `CTRL-REQ`, `IF-REQ`, `SAF-REQ`.
- **Verification status:** `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `PASS_WITH_ACTIONS`, `FAIL`, `NOT_VERIFIED`.
- **Gates:** A (design release), B (bench validation), C (safety and release); mechanical M0–M4, electronics E0–E4, firmware F0–F4.
- **Units:** SI. Documents use N·m, RPM, ° and °C; firmware and protocol use rad, rad/s, N·m, A, V and °C. q = 0 at full extension, positive in flexion.
- **Every document** carries the KA- header table and a revision history.
- **Every test record** states the hardware revision, firmware version, supply voltage, load, ambient temperature, instruments and results.

## 6. Quick start

```bash
make help          # list targets
make check         # run all documentation, traceability and BOM checks
make check-docs    # document headers and revision history
make check-links   # relative links
make check-trace   # traceability CSV versus requirement IDs
make check-bom     # mechanical and electrical BOM schema
make check-calcs   # calculation regression + document consistency
make bom-summary   # BOM cost totals by milestone and category
make calc          # run the mechanical sizing calculations
```

Python 3.8 or later is needed; the scripts use the standard library only.

## 7. Safety

The actuator is an **experimental device and not a human-safe joint**.

- Loaded, peak and fault tests happen **only on a restrained, guarded, instrumented fixture**.
- Never resist the actuator by hand or attach it to a person.
- Bring-up uses a current-limited PSU and a hardware e-stop.

See [requirements/SAFETY_REQUIREMENTS.md](requirements/SAFETY_REQUIREMENTS.md).

## 8. Status

| Item | Status |
|---|---|
| Documentation baseline (requirements, planning, docs, calculations, audit framework) | Draft 0.1, proposed, pending approval; external audit 2026-10-12: M0 FAIL / not ready (see audit/external/) |
| Repository visibility | **Decision needed:** the repository is public, but the content is marked proprietary and confidential (EXT-AUD-001) |
| A0 | Not started |
| A1 | Not started |
| A2 | Not started |
