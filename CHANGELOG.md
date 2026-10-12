# Changelog

This file records notable changes to the Kritva Actuator repository.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Releases are tagged per milestone, for example `A0-v0.1.0`. Document revisions are tracked in each document's revision history; this file summarises them at repository level.

## [Unreleased]

### Added (2026-10-11 documentation baseline)

**Requirements** (proposed, pending approval):

- `SYSTEM_REQUIREMENTS.md` (rev 0.2, aligned with the agreed project direction)
- `ACTUATOR_SPECIFICATION.md`
- `MECHANICAL_REQUIREMENTS.md`
- `ELECTRICAL_REQUIREMENTS.md`
- `FIRMWARE_REQUIREMENTS.md`
- `INTERFACE_REQUIREMENTS.md`
- `SAFETY_REQUIREMENTS.md`

**Planning (`planning/v1/`):**

- ROADMAP, MILESTONE, TASKS, DECISIONS (ACT-DEC-001 to 015) and RISKS_AND_DEPENDENCIES.
- Workstream guides for ACT-01, ACT-02 and ACT-03.
- Full task records for ACT-01-001, ACT-02-001 and ACT-03-001.

**Documentation:**

- `docs/architecture`
- `docs/mechanical`
- `docs/electronics`
- `docs/firmware`
- `docs/interfaces` (actuator interface, CAN protocol, unit conventions)
- `docs/validation`

**Mechanical calculations and BOMs:**

- Calculation documents for load cases, torque and speed, shaft strength, bearing selection and gearbox selection.
- `mechanical/calculations/actuator_sizing.py`.
- `mechanical/bom/MECHANICAL_BOM.csv` and `hardware/bom/ELECTRICAL_BOM.csv` (candidate items, estimates only).

**Audit framework:**

- Traceability CSV.
- Mechanical design and acceptance audits, risk register and release checklist.
- Electronics and firmware audits.
- Release audit.

**Tooling:**

- `Makefile`.
- Scripts in `scripts/validation` (document, link and traceability checks) and `scripts/bom` (BOM check and summary).
- `.gitignore` and `.gitattributes` (Git LFS).
- `.github` issue and PR templates and CI workflows.

**Repository basics:**

- `README.md`, `LICENSE` (proprietary), `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`.
- Folder skeleton with `.gitkeep` placeholders.

### Superseded

- `docs/mechanical/A1-mechanical-design.md` and `tools/sizing.py` / `tools/sizing_report.txt` from the first pass are superseded. They assumed a custom two-stage gearbox and 8 N·m / 60 RPM / 15:1. They are replaced by `docs/mechanical/MECHANICAL_DESIGN_SPECIFICATION.md` and `mechanical/calculations/`, which follow ACT-DEC-003 (commercial planetary gearbox) and ACT-DEC-008 (10 N·m / 20–25 N·m / 45 RPM). The old files should be deleted from the working copy.
- The early targets (1–2 N·m continuous, 10 mm shaft, 5:1–15:1) and the interim targets (6–8 N·m, 15–20 N·m, 30–60 RPM, 10:1–20:1) are superseded by ACT-DEC-008.
