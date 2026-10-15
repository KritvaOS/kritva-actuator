# Changelog

This file records notable changes to the Kritva Actuator repository.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Releases are tagged per milestone, for example `A0-v0.1.0`. Document revisions are tracked in each document's revision history; this file summarises them at repository level.

## [Unreleased]

### Added (2026-10-15, restructure Stages 1-3; ACT-DEC-024 to 026 PROPOSED)

- Four-submodule plan (three mechanical variants S, M, L plus embedded): `docs/architecture/REPOSITORY_ARCHITECTURE.md`, `ACTUATOR_FAMILY_SPEC.md`, `docs/interfaces/INTERFACE_CONTROL_DOCUMENT.md`.
- `planning/v2/`: migration plan with runbook, migration manifest (every file with owner and destination), legacy-to-new task ID mapping, workstreams, 24-week roadmap.
- `docs/standards/`: CAD naming, BOM, design review checklist, release checklist, submodule workflow.
- `scripts/validation/check_manifest.py` and `scripts/integration/check_submodules.py`; Makefile targets `check-manifest` and `check-submodules`; CI steps added.
- Child-repository scaffolds delivered separately (`child-repos/`). **No existing file has been moved or deleted.** File moves are Stage 4.

### Added (2026-10-14)

- `docs/architecture/COMPONENTS_SOURCING_AND_COST.md` (new): component breakdown, candidate sources, draft pricing structure (listing, estimate, TBD) and phased localisation, based on the stated in/out of scope.

### Added (2026-10-13, ACT-02-002)

- `mechanical/calculations/MOTOR_GEARBOX_SHORTLIST.md` (new): motor and gearbox screening shortlist (CubeMars RI50/60/70/80; Neugart PLE 040/060, PLPE 050; WITTENSTEIN benchmark) with fit calculations. Candidate data are from the ChatGPT session and not yet re-checked against vendor pages; screening only. Rev 0.2 adds an online price check (CubeMars store, Robokits India); no gearbox prices exist online.

### Changed (2026-10-13, external re-verification of 894860e)

- `check_calcs.py` / `expected_results.json`: regression coverage of the effective-inertia range (rod inertia, low/mid/high rotor cases, rotor share); 24 results checked (EXT-AUD-019).
- `LOAD_CASES.md`: point-mass 1.90 J marked illustrative only; rotor share corrected to about 2 %–25 %.
- `BEARING_SELECTION.md` §9: 6202 stated as a candidate, not a released part (EXT-AUD-021).
- External audit record updated with the re-verification result and EXT-AUD-018..021.
- ACT-DEC-023 ACCEPTED: repository moved to private (EXT-AUD-001, blocker B7 closed). M0 decision sheet: reviewer recommendations adopted for B1-B6, values still pending.
- `planning/v1/M0_DECISION_SHEET.md` (new): decision sheet for M0 blockers B1-B7 with the external reviewer's recommendations.

### Changed (2026-10-12, external audit follow-up; see audit/external/EXTERNAL_REPO_AUDIT_2026-10-12.md)

- `LOAD_CASES.md` §8.1/§8.2: hard-stop model limitations; effective inertia with the reflected rotor (2.1–2.8 J); single-contact design rule (EXT-AUD-003/004).
- `BEARING_SELECTION.md`: baseline changed to **6202 on 15 mm seats**; 6001/6201 only after the balanced stop is proven (EXT-AUD-006). BOM MB-004 updated.
- `SHAFT_STRENGTH.md`: LC-05 remains the design case; the result is conditional and not frozen; stop fatigue case added (EXT-AUD-005).
- `TORQUE_AND_SPEED.md` §2.1: motor-constant conventions (EXT-AUD-008).
- README: baseline labelled "NOT approved, NOT frozen"; repository-visibility decision flagged (EXT-AUD-001/013).

### Added (2026-10-12)

- `scripts/validation/check_calcs.py` and `mechanical/calculations/expected_results.json`; `make check-calcs`, also in CI (EXT-AUD-011).
- Traceability gate rule: PASS/FAIL claims need concrete evidence and a specific procedure (EXT-AUD-010).
- `.github/CODEOWNERS` (EXT-AUD-015); warning and summary when the firmware CI job is skipped (EXT-AUD-014).
- `audit/external/` external audit record.

### Removed

- `Claude outputs/` (delivery archive) is ignored from now on; the committed copy must be removed with `git rm` (EXT-AUD-016).

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
