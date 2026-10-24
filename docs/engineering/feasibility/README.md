# Kritva Engineering Feasibility Studies

**Document ID:** KRITVA-ENG-FS-README-001  
**Version:** 0.1  
**Status:** Proposed  
**Canonical Path:** `docs/engineering/feasibility/README.md`

## 1. Purpose

This directory is the entry point for engineering feasibility studies in the Kritva actuator program.

It provides a consistent framework for investigating engineering questions, evaluating design alternatives, documenting technical evidence, and making evidence-based feasibility recommendations for Kritva-S, Kritva-M, Kritva-L, and related actuator systems.

The feasibility-study framework separates inputs, working calculations, and outputs; maintains traceability to canonical requirements and technical sources; and establishes consistent review and verification controls.

This README provides navigation and workflow guidance. The detailed folder and file requirements are defined in the feasibility-study standard.

## 2. Current Status

| Item | Status |
|---|---|
| Feasibility-study standard | Version 0.4 — Proposed |
| Standard document | [FEASIBILITY_STUDIES_STANDARD.md](FEASIBILITY_STUDIES_STANDARD.md) |
| Common methodology and templates | Created (Proposed): methodology, study template, deliverables standard, review checklist |
| Study and decision registers | Created (Proposed): study register, decision register, cross-study dependencies |
| Kritva-M studies | FS-M-001 to FS-M-010 drafted (control documents only; no calculations yet) |
| Study execution | Pending reviewer assignment, specification approval and authorization; all studies PROPOSED, results NOT_VERIFIED |

The standard is proposed and is not yet an approved engineering baseline. Study IDs and study descriptions listed as planned are proposals until authorized and recorded in the study register.

## 3. Navigation

### 3.1 Standard

- [Feasibility Studies Standard](FEASIBILITY_STUDIES_STANDARD.md) — Canonical definition of the folder structure, naming conventions, evidence requirements, review controls, and study lifecycle.

### 3.2 Common Guidance

The following common files provide reusable methods and templates.

- [Common methodology](common/FEASIBILITY_METHODOLOGY.md) — Engineering analysis methods, evidence expectations, uncertainty treatment, and feasibility assessment.
- [Study template](common/STUDY_TEMPLATE.md) — Template for creating a study-specific specification.
- [Deliverables standard](common/DELIVERABLES_STANDARD.md) — Mandatory, conditional, and optional deliverables.
- [Review checklist](common/REVIEW_CHECKLIST.md) — Common technical review and acceptance checklist.

These files exist but are Proposed. They are not approved procedures until approval is recorded.

### 3.3 Registers

The registers provide the authoritative overview of study status, decisions, and dependencies.

- [Study register](registers/STUDY_REGISTER.csv) — Authoritative index of study IDs, ownership, status, dependencies, and acceptance decisions.
- [Decision register](registers/DECISION_REGISTER.csv) — Index of engineering decisions and links to supporting evidence.
- [Cross-study dependencies](registers/CROSS_STUDY_DEPENDENCIES.csv) — Dependencies between studies and shared engineering inputs.

The study register is the authoritative source for the current list and status of feasibility studies. The planned-study table in this README is for navigation and planning only; it must not be used as a competing status record.

### 3.4 Actuator Family Studies

- Kritva-S feasibility studies — `kritva-s/` (not yet created)
- [Kritva-M feasibility studies](kritva-m/)
- Kritva-L feasibility studies — `kritva-l/` (not yet created)

Only `kritva-m/` currently exists. Directories marked "not yet created" are intended locations and shall not be assumed to exist.

## 4. Planned Kritva-M Studies

The following studies are candidates for the Kritva-M feasibility program. They are proposed work packages, not automatically authorized assignments.

The authoritative IDs, lifecycle statuses, ownership, dependencies, and acceptance decisions must be maintained in [STUDY_REGISTER.csv](registers/STUDY_REGISTER.csv).

| Study ID | Planned study | Primary engineering question |
|---|---|---|
| FS-M-001 | Integrated actuator system feasibility | Can the proposed Kritva-M actuator architecture plausibly meet its preliminary system requirements? |
| FS-M-002 | Load and torque analysis | What output torque, speed, and load cases must the actuator support? |
| FS-M-003 | Motor selection and sizing | Which candidate motor can satisfy the required operating points and constraints? |
| FS-M-004 | Gearbox selection and ratio optimization | Which gearbox and ratio provide a suitable balance of torque, speed, efficiency, backlash, size, and cost? |
| FS-M-005 | Output shaft feasibility | Can the output shaft withstand the applicable torsional and bending loads? |
| FS-M-006 | Bearing and support feasibility | Can the bearing arrangement support the loads and meet the intended life target? |
| FS-M-007 | Housing and mechanical integration | Can the components be packaged into a practical, structurally adequate assembly? |
| FS-M-008 | Electrical and thermal feasibility | Can the electrical and thermal design support the required operating conditions? |
| FS-M-009 | Manufacturing and cost feasibility | Can the actuator be manufactured, assembled, and tested at a realistic cost? |
| FS-M-010 | Integrated design trade-off | Which candidate architecture should proceed to the next engineering stage? |

### Study execution strategy

FS-M-001 is the baseline study. Real calculations should start with FS-M-002 (load and torque analysis), because FS-M-003, 004, 005, 006 and 008 consume its load cases. No study is complete or approved until evidence and the required review are recorded.

The integrated study should perform enough analysis of loads, motor and gearbox candidates, shaft and bearings, electrical and thermal constraints, packaging, and cost to identify the principal feasibility risks.

Authorize additional focused studies only when the integrated study identifies unresolved questions that require deeper analysis. This avoids duplicated calculations and inconsistent assumptions.

The planned list may be revised as evidence becomes available. Changes to the authoritative study register shall take precedence over this planning table.

## 5. How to Start a Study

Follow these steps when proposing and initiating a new feasibility study.

### Step 1 — Identify the engineering question

State the decision the study must support. Define the scope and exclusions clearly enough to prevent unrelated work from being included.

### Step 2 — Allocate a study ID

Obtain a unique ID following the convention defined in the feasibility-study standard:

    FS-<PRODUCT>-<NUMBER>

Examples include FS-M-001 and FS-S-001. Record the allocated ID in the study register. Do not reuse IDs.

### Step 3 — Create the study directory

Use the naming convention:

    <STUDY-ID>-<short-kebab-case-name>/

For example:

    kritva-m/
    └── FS-M-001-actuator-system-feasibility/
        ├── SPECIFICATION.md
        ├── WORK_PLAN.md
        ├── ASSUMPTIONS_AND_OPEN_QUESTIONS.md
        ├── REVIEW.md
        ├── inputs/
        ├── calculations/
        └── outputs/

Create additional directories such as component research, references, simulation, CAD, or test data only when required.

### Step 4 — Define the specification and acceptance criteria

Use the common study template when available. Identify the applicable requirements by their canonical IDs, such as SYS-REQ-nnn, and link to their authoritative source rather than copying requirement records.

Define the expected technical evidence, deliverables, review responsibilities, dependencies, and acceptance criteria before work begins.

### Step 5 — Establish the input baseline

Populate the study's inputs directory with the relevant, traceable information.

Distinguish approved inputs from preliminary targets, assumptions, unknowns, and measured data. Record material assumptions and unresolved questions in `ASSUMPTIONS_AND_OPEN_QUESTIONS.md`.

Do not silently modify approved requirements or baseline data.

### Step 6 — Perform and record the analysis

Store working calculations and analytical models under `calculations/`. Preserve the inputs, methods, units, assumptions, and limitations needed to reproduce or independently verify significant results.

Use `outputs/` for results, comparisons, plots, risk assessments, cost estimates, and final deliverables.

### Step 7 — Submit for technical review

Complete the final report and record the review in `REVIEW.md`. Resolve review findings or document their authorized disposition.

The author shall not approve their own safety-critical work. If required independent review is incomplete, the verification status remains `NOT_VERIFIED`.

### Step 8 — Update the authoritative register

Update `STUDY_REGISTER.csv` with the study's current lifecycle status, owner, reviewer, dependencies, and acceptance decision.

Do not mark a study accepted merely because its files exist. Acceptance requires the applicable technical criteria and review controls to be satisfied.

## 6. Canonical Requirements and Repository Artefacts

Feasibility studies shall follow the repository's one-canonical-home principle.

- System requirements remain canonical in `requirements/SYSTEM_REQUIREMENTS.md`.
- Engineering standards remain canonical under `docs/standards/`.
- Planning artefacts remain in their established planning location.
- Audit records remain in their established audit location.
- Feasibility analysis and study-specific conclusions belong under `docs/engineering/feasibility/`, unless an existing canonical location applies.

Use requirement IDs and links to establish traceability. Do not create independently maintained copies of existing requirements, standards, or controlled project records.

## 7. Status Conventions

The study register shall distinguish study lifecycle status from verification status.

Study lifecycle values are defined by the feasibility-study standard. Verification records shall use only the following values:

- `NOT_STARTED`
- `IN_PROGRESS`
- `PASS`
- `PASS_WITH_ACTIONS`
- `FAIL`
- `NOT_VERIFIED`

A feasibility conclusion and a verification status are different. A study may conclude that an architecture is promising while its verification status remains `NOT_VERIFIED` because required evidence or independent review is outstanding.

## 8. Ownership and Maintenance

The engineering lead or designated authority is responsible for approving study specifications, allocating study IDs, assigning reviewers, and accepting or rejecting study deliverables.

Study owners are responsible for conducting the technical analysis, maintaining traceable evidence, documenting assumptions and limitations, and addressing review findings.

This README shall remain a navigation and workflow document. The feasibility-study standard and authoritative registers govern detailed requirements and current study status.

**End of Document**
