# Kritva Engineering Feasibility Studies — Folder and File Structure Standard

**Document ID:** KRITVA-ENG-FS-STD-001  
**Version:** 0.4  
**Status:** Proposed  
**Canonical Path:** `docs/engineering/feasibility/FEASIBILITY_STUDIES_STANDARD.md`  
**Parent Repository:** `KritvaOS/kritva-actuator`

---

## 1. Purpose

This standard defines the directory structure, file organization, naming conventions, evidence requirements, and review controls for engineering feasibility studies conducted within the Kritva actuator program.

It establishes a consistent framework for studies covering Kritva-S, Kritva-M, Kritva-L, and other actuator-related engineering topics.

Every study must make its objective, inputs, assumptions, analysis, results, limitations, and engineering conclusions traceable and reviewable.

This standard governs the organization and control of feasibility-study artefacts. It does not replace system requirements, engineering design standards, safety procedures, or formal design approval processes.

## 2. Scope

This standard applies to feasibility studies involving, but not limited to:

- System-level actuator feasibility.
- Load, torque, speed, and motion analysis.
- Motor and gearbox selection.
- Output shaft and bearing analysis.
- Mechanical packaging and structural feasibility.
- Electrical power and thermal feasibility.
- Embedded control and interface feasibility.
- Manufacturing, assembly, and cost feasibility.
- Materials and component trade-offs.
- Prototype readiness and integrated design trade-offs.

The requirements apply to studies performed by interns, engineers, or other authorized contributors.

The depth of analysis and required evidence must be proportional to the study objective, technical risk, and intended engineering decision.

## 3. Normative Principles

All feasibility studies shall follow these principles.

### 3.1 One canonical home per artefact

Every controlled engineering artefact shall have one canonical location.

If an artefact already exists elsewhere in the repository, link to its canonical location rather than copying and independently maintaining another version.

In particular:

- System requirements remain canonical in `requirements/SYSTEM_REQUIREMENTS.md`.
- Engineering standards remain canonical under `docs/standards/`.
- Planning artefacts remain in their established planning location.
- Audit records remain in their established audit location.
- Feasibility-study artefacts belong under `docs/engineering/feasibility/`, unless another existing repository convention establishes a more appropriate canonical location.

A feasibility study may quote a short requirement for explanatory purposes, but it must identify the requirement ID and link to the canonical source. Such explanatory text does not replace the source requirement.

### 3.2 Traceability

Every material conclusion shall be traceable to the applicable requirements, input data, assumptions, calculations, technical references, or test evidence.

### 3.3 Evidence-based conclusions

A feasibility conclusion shall distinguish between:

- Verified facts.
- Manufacturer specifications.
- Approved requirements.
- Preliminary requirements.
- Engineering calculations.
- Assumptions.
- Measurements.
- Engineering judgments.
- Unresolved questions.

Missing evidence shall not be treated as evidence of feasibility.

### 3.4 Independent review

The author shall not approve their own safety-critical work.

Safety-critical work requires independent review by an authorized, technically competent reviewer. If the required independent review has not been completed, the verification status shall remain `NOT_VERIFIED`.

For non-safety-critical work, independent review is required when specified by the study, applicable standards, risk assessment, or engineering lead.

### 3.5 No implicit design approval

A feasibility study may recommend a design, component, material, or requirement change. The recommendation does not itself authorize the change.

Changes to controlled requirements or design baselines shall follow the applicable repository approval process.

### 3.6 Proportional documentation

Mandatory control files shall be present for every study. Technical subdirectories and supporting files shall be created only when relevant.

Empty directories, duplicate artefacts, and unnecessary documentation shall be avoided.

## 4. Canonical Root Directory

The canonical root for feasibility-study artefacts is `docs/engineering/feasibility/`.

The following structure defines the intended organization:

```text
docs/
└── engineering/
    └── feasibility/
        ├── README.md
        ├── FEASIBILITY_STUDIES_STANDARD.md
        │
        ├── common/
        │   ├── FEASIBILITY_METHODOLOGY.md
        │   ├── STUDY_TEMPLATE.md
        │   ├── DELIVERABLES_STANDARD.md
        │   └── REVIEW_CHECKLIST.md
        │
        ├── registers/
        │   ├── STUDY_REGISTER.csv
        │   ├── DECISION_REGISTER.csv
        │   └── CROSS_STUDY_DEPENDENCIES.csv
        │
        ├── kritva-s/
        │   └── FS-S-001-<study-name>/
        │
        ├── kritva-m/
        │   └── FS-M-001-<study-name>/
        │
        └── kritva-l/
            └── FS-L-001-<study-name>/
```

This is the logical target structure. A file or directory shall be created only when it is required, approved for use, or needed to support an authorized study.

### 4.1 Root-level files

- `README.md` provides an entry point to the feasibility-study area, including links to this standard, common guidance, and the study register.
- `FEASIBILITY_STUDIES_STANDARD.md` defines the common folder structure, file requirements, naming conventions, evidence expectations, and study controls.

### 4.2 Common standards

| File | Responsibility |
|---|---|
| `common/FEASIBILITY_METHODOLOGY.md` | Defines the common engineering approach, evidence evaluation, uncertainty treatment, and feasibility assessment method. |
| `common/STUDY_TEMPLATE.md` | Provides the template for a study-specific `SPECIFICATION.md`. |
| `common/DELIVERABLES_STANDARD.md` | Defines mandatory, conditional, and optional deliverables and their expected formats. |
| `common/REVIEW_CHECKLIST.md` | Defines the common technical review and acceptance checklist. |

These files contain reusable rules. Study-specific requirements and conclusions shall remain in the relevant study directory.

### 4.3 Registers

| File | Responsibility |
|---|---|
| `registers/STUDY_REGISTER.csv` | Tracks study IDs, titles, owners, reviewers, status, dependencies, and acceptance decisions. |
| `registers/DECISION_REGISTER.csv` | Provides an index of important engineering decisions and links to their supporting evidence. |
| `registers/CROSS_STUDY_DEPENDENCIES.csv` | Records dependencies between studies, including shared inputs, prerequisite analyses, and decisions. |

Each register shall have one canonical location. Do not maintain competing manually updated copies of the same register.

## 5. Study Identification and Directory Naming

### 5.1 Study ID format

Use the format `FS-<PRODUCT>-<NUMBER>`, where:

- `FS` identifies a feasibility study.
- `<PRODUCT>` identifies the applicable actuator family or defined system scope.
- `<NUMBER>` is a unique, zero-padded sequential identifier.

Examples: `FS-S-001`, `FS-M-001`, `FS-M-002`, `FS-L-001`.

For cross-family studies, use a system identifier such as `FS-SYS-001` only after defining it in the study register.

Study IDs shall be unique and shall not be reused after a study is closed, cancelled, or superseded.

### 5.2 Directory naming

Use `<STUDY-ID>-<short-kebab-case-name>/`.

Examples: `FS-M-001-actuator-system-feasibility/`, `FS-M-002-load-torque-analysis/`, `FS-S-001-motor-sizing/`.

Study directory names shall remain stable. Status changes and document revisions shall not be represented by renaming the study directory.

### 5.3 File naming

Use descriptive, consistent filenames.

Standard control documents shall use the prescribed uppercase names: `SPECIFICATION.md`, `WORK_PLAN.md`, `ASSUMPTIONS_AND_OPEN_QUESTIONS.md`, `REVIEW.md`, `FINAL_REPORT.md`.

Supporting analysis files should use descriptive names, such as `motor_sizing.xlsx`, `shaft_stress_analysis.py`, `motor_candidate_comparison.csv`, `torque_speed_comparison.png`.

Use repository version control to preserve file history. Avoid ambiguous names such as `final_latest_v3_revised.xlsx`.

## 6. Standard Individual Study Structure

Every study shall have separate `inputs/` and `outputs/` directories.

```text
FS-M-001-actuator-system-feasibility/
├── SPECIFICATION.md
├── WORK_PLAN.md
├── ASSUMPTIONS_AND_OPEN_QUESTIONS.md
├── REVIEW.md
│
├── inputs/
│   └── README.md
│
├── calculations/
│   └── README.md
│
├── outputs/
│   └── README.md
│
├── component_research/
│   └── README.md
│
└── references/
    └── SOURCE_REGISTER.csv
```

This is a structural template. Conditional directories shall be created only when required by the study.

**Scaffold versus evidence (v0.4).** Structure and evidence are distinct. At study creation the root control files (`SPECIFICATION.md`, `WORK_PLAN.md`, `ASSUMPTIONS_AND_OPEN_QUESTIONS.md`, `REVIEW.md`, `README.md`) and `inputs/` are required. `calculations/`, `outputs/` and `references/SOURCE_REGISTER.csv` are required when the study begins producing results and before any acceptance criterion may be marked `PASS`; their absence at the PROPOSED stage is not a defect. Empty directories shall not be created. The input register may be `inputs/INPUTS.md` in place of `inputs/README.md`.

The standard control files at the study root define and govern the work. The `inputs/`, `calculations/`, and `outputs/` directories separate incoming evidence, working analysis, and produced results.

## 7. Study Root Control Files

### 7.1 SPECIFICATION.md — Mandatory

The study specification shall define:

- Study ID, title, version, and status.
- Objective and engineering question.
- Background and motivation.
- Scope and exclusions.
- Applicable requirements and constraints.
- Technical tasks and investigation methods.
- Required inputs and dependencies.
- Expected deliverables.
- Study-specific acceptance criteria.
- Owner and reviewer roles.
- Schedule and review checkpoints.
- Safety and risk considerations, where applicable.

Requirements shall be referenced by their canonical IDs, such as `SYS-REQ-nnn`, with links to the canonical requirement source.

The study specification shall not create a competing copy of the system requirements baseline.

### 7.2 WORK_PLAN.md — Mandatory

The work plan shall identify: task ID, task description, responsible person or role, expected technical output, dependencies, target date or milestone, review checkpoint, and status.

The work plan shall emphasize engineering analysis and evidence generation rather than documentation activity alone.

### 7.3 ASSUMPTIONS_AND_OPEN_QUESTIONS.md — Mandatory

This file shall record material assumptions, unknowns, and unresolved questions.

For each item, record as applicable: identifier, description, reason for the assumption or question, current value or treatment, source or justification, effect on the analysis, sensitivity or potential consequence, owner, status, and resolution evidence.

An assumed value shall not be presented as a verified fact.

Where an unknown input could materially change the conclusion, the study shall explain the resulting limitation and whether further evidence is required.

### 7.4 REVIEW.md — Mandatory

The review record shall identify: study ID and reviewed revision, reviewer and review date, review scope, checklist results, technical findings and severity, required corrections, resolution evidence, final review decision, and authorized approver where applicable.

The author shall not approve their own safety-critical work. If independent approval is required and has not been obtained, the verification status shall remain `NOT_VERIFIED`.

## 8. Input Directory — `inputs/`

### 8.1 Purpose

The `inputs/` directory contains information consumed by the study. It shall not be used as a general-purpose archive of unrelated project documents.

Inputs may include requirements references, engineering parameters, approved interface information, manufacturer datasheets, measurements, and other source data necessary to conduct the analysis.

### 8.2 Recommended structure

```text
inputs/
├── README.md
├── requirements/
├── mechanical/
├── electrical/
├── component_datasheets/
└── reference_data/
```

Create only the subdirectories relevant to the study.

| Subdirectory | Intended content |
|---|---|
| `requirements/` | Requirement references, applicable acceptance targets, and links to canonical requirement sources. |
| `mechanical/` | Relevant dimensions, masses, centres of mass, load cases, interfaces, and mechanical constraints. |
| `electrical/` | Supply voltage, current limits, driver constraints, interfaces, and other applicable electrical inputs. |
| `component_datasheets/` | Datasheets and technical specifications for candidate or baseline components, where permitted. |
| `reference_data/` | Relevant measurements, approved reference calculations, and other baseline data. |

### 8.3 Input control

The `inputs/README.md` shall describe the input package and identify important source locations and limitations.

Each material input shall have a traceable source and a clear status, as applicable:

- `APPROVED` — Formally approved input.
- `PRELIMINARY` — Provisional target or requirement.
- `ASSUMED` — Unverified value adopted for analysis.
- `UNKNOWN` — Not yet established.
- `MEASURED` — Supported by measurement evidence.

A `MEASURED` value must be supported by traceable measurement evidence.

Approved baseline inputs shall not be silently modified. Proposed changes shall be documented and handled through the applicable approval process.

Where a requirement already exists in `requirements/SYSTEM_REQUIREMENTS.md`, reference its `SYS-REQ-nnn` ID and link to the canonical source instead of creating a duplicate requirement record.

Where a source file has an existing canonical location, link to it rather than maintaining an independently edited copy. A local copy of external technical data may be retained when necessary and permitted, provided its source, revision, and identity are recorded.

## 9. Calculations Directory — `calculations/`

### 9.1 Purpose

The `calculations/` directory contains working engineering analyses, reproducible calculations, models, and supporting calculation notes.

### 9.2 Recommended structure

```text
calculations/
├── README.md
├── load_torque/
├── motor_sizing/
├── gearbox_sizing/
├── shaft_analysis/
├── bearing_analysis/
└── power_thermal/
```

The example subdirectories are applicable to an integrated actuator study. A focused study shall create only the calculation areas relevant to its scope.

### 9.3 Accepted artefact types

- `.xlsx` — Engineering calculation spreadsheets.
- `.py` — Reproducible Python calculations.
- `.m` — MATLAB scripts, where applicable.
- `.md` — Derivations, methods, calculation notes, and interpretation.
- Native model or simulation files, where required.

### 9.4 Calculation evidence

Each significant calculation shall identify: calculation purpose, input parameters and their sources, units and conversion conventions, equations or analytical method, assumptions and boundary conditions, intermediate results where needed, final results, applicable limits and uncertainty, and validation or independent checks where applicable.

Scripts and models shall identify necessary dependencies or execution assumptions where those affect reproducibility.

The final result shall be traceable to the calculation and input revision used.

## 10. Component Research Directory — `component_research/`

### 10.1 Purpose

The `component_research/` directory is conditional. Use it when the study evaluates commercial components, materials, suppliers, or alternative technologies.

### 10.2 Recommended structure

```text
component_research/
├── README.md
├── motor_candidates/
├── gearbox_candidates/
├── bearings/
└── materials/
```

Create only the categories relevant to the study.

### 10.3 Expected evidence

Where component selection is in scope, record as applicable: manufacturer and exact model; source datasheet and revision; relevant ratings and operating conditions; mechanical and electrical interfaces; environmental and thermal limits; availability and cost evidence; limitations and missing information; candidate comparison and selection rationale.

Manufacturer ratings shall be interpreted according to their stated conditions. Advertised maximum values shall not be assumed to represent continuous operating capability.

Component research shall support the calculations and conclusions; it shall not substitute for them.

## 11. Outputs Directory — `outputs/`

### 11.1 Purpose

The `outputs/` directory contains the results and deliverables produced by the study.

It separates the final analysis outputs from incoming source information and working calculations.

### 11.2 Recommended structure

```text
outputs/
├── README.md
├── calculations_results/
├── comparison_tables/
├── plots/
├── risk_assessment/
├── cost_estimate/
├── FINAL_REPORT.md
└── FINAL_PRESENTATION.pdf
```

Create only the relevant subdirectories and files.

| Subdirectory or file | Intended content |
|---|---|
| `calculations_results/` | Final numerical results, calculation summaries, and result datasets. |
| `comparison_tables/` | Candidate comparisons, parameter tables, and trade-off matrices. |
| `plots/` | Torque-speed curves, stress plots, performance graphs, and other visual results. |
| `risk_assessment/` | Study-specific risks, mitigations, and unresolved technical concerns. |
| `cost_estimate/` | Preliminary BOM, component prices, manufacturing estimates, and cost assumptions. |
| `FINAL_REPORT.md` | Consolidated technical findings, limitations, feasibility conclusion, and recommendation. |
| `FINAL_PRESENTATION.pdf` | Formal presentation when required by the study specification. |

### 11.3 Output integrity

The `outputs/README.md` shall identify the principal outputs and their relationships to the inputs and calculations.

Every significant output shall identify or link to the source calculation, model, or evidence that produced it.

Where practical, generated outputs should be reproducible from version-controlled analysis files and identified input revisions.

The final report shall distinguish calculated results, manufacturer specifications, measured results, assumptions, and engineering judgments.

A report or presentation shall not claim that an analysis has been independently verified unless the required verification has actually been completed.

## 12. References and Source Register

The `references/` directory is conditional but shall be used whenever external technical sources need a structured register.

```text
references/
└── SOURCE_REGISTER.csv
```

Recommended source-register columns:

```text
source_id,source_type,manufacturer_or_author,title,model_or_document_id,revision,url_or_path,date_accessed,parameters_supported,notes
```

Source references shall be sufficiently specific to identify the information used.

Prefer authoritative manufacturer documentation for component ratings and applicable official documentation for standards or requirements.

Where external source files are retained locally, respect licensing, confidentiality, and redistribution restrictions.

References shall support claims and calculations. A URL alone does not establish that a particular rating, operating condition, or conclusion has been correctly interpreted.

## 13. Additional Conditional Directories

The following directories may be created when the study requires them:

| Directory | Use |
|---|---|
| `simulation/` | Simulation models, setup, boundary conditions, solver configuration, outputs, and validation evidence. |
| `CAD/` | CAD models, assemblies, drawings, exports, and mechanical packaging evidence. |
| `test_data/` | Test procedures, raw measurements, instrumentation details, and test-analysis artefacts. |

These directories shall follow the same traceability and canonical-home rules.

If a CAD model, test record, or other artefact already has an authoritative home elsewhere in the repository, link to it instead of creating an independent duplicate.

## 14. Final Report Requirements

Every study shall produce `outputs/FINAL_REPORT.md`.

The report shall contain, as applicable: executive summary; study objective and engineering question; applicable requirements and constraints; method and analysis approach; inputs and assumptions; results and supporting evidence; candidate comparison, where relevant; risks, limitations, and uncertainty; feasibility assessment; recommendation and rationale; outstanding questions and follow-up actions; links to calculations, source evidence, and relevant canonical artefacts.

The report shall state what has and has not been established.

A feasibility recommendation shall use one of the following categories, as appropriate:

- `PROMISING` — Available evidence supports continued investigation or development.
- `PROMISING_WITH_CONDITIONS` — Progress is plausible, subject to identified conditions.
- `FEASIBILITY_NOT_ESTABLISHED` — Available evidence is insufficient to establish feasibility.
- `POTENTIALLY_INFEASIBLE` — Evidence indicates that the proposed approach may not meet important constraints.

These categories describe engineering conclusions, not verification status. The report shall explain the evidence and rationale behind the selected category.

## 15. Verification Status and Review Controls

Use only the following verification status values: `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `PASS_WITH_ACTIONS`, `FAIL`, `NOT_VERIFIED`.

These values shall be used consistently in study-specific verification records and review artefacts.

### 15.1 Status interpretation

| Status | Meaning |
|---|---|
| `NOT_STARTED` | Verification has not begun. |
| `IN_PROGRESS` | Verification activities are underway. |
| `PASS` | Defined verification criteria have been satisfied with adequate evidence and required review. |
| `PASS_WITH_ACTIONS` | Verification criteria are satisfied subject to explicitly documented, authorized follow-up actions that do not invalidate the acceptance decision. |
| `FAIL` | Verification evidence demonstrates that one or more applicable criteria are not satisfied. |
| `NOT_VERIFIED` | Verification cannot be established, including where evidence or required independent review is missing. |

A status shall not be promoted based solely on document completion.

### 15.4 Status vocabularies (v0.4)

Three different status types shall not be mixed:

| Type | Where used | Allowed values |
|---|---|---|
| Document status (`status:` in front matter) | Every control document | `PROPOSED`, `APPROVED` (upper case) |
| Study lifecycle (`lifecycle:`) | Study register and front matter | As defined in the study template (for example `PROPOSED`, `IN_PROGRESS`, `BLOCKED`, `ACCEPTED`) |
| Verification / acceptance-criterion status | Work-plan AC tables, `REVIEW.md`, coverage matrices | `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `PASS_WITH_ACTIONS`, `FAIL`, `BLOCKED`, `NOT_VERIFIED`, `NOT_APPLICABLE` |

`BLOCKED` means a required input, dependency or decision is missing. `NOT_APPLICABLE` requires a recorded rationale. `PASS_WITH_ACTIONS` follows section 15.1. The lifecycle value `PROPOSED` is not a technical result. A work plan may use a subset of the verification values but shall not introduce others.

### 15.5 Conditional requirements (v0.4)

A requirement that applies only under a condition (for example SYS-REQ-014, which applies only if the arm must absorb impacts) shall be recorded as conditional, with the condition and its decision owner. Studies shall not describe it as unconditionally in scope until the condition is decided, and shall not treat it as satisfied by a different requirement (for example SYS-REQ-092 post-loaded-cycle integrity).

### 15.6 Reviewer assignment (v0.4)

Where safety-critical conclusions are produced, the study header shall name the Independent Reviewer role in addition to any other reviewer (for example `Project Lead; Independent Reviewer TBD for safety-critical checks`). An unassigned independent reviewer keeps those conclusions `NOT_VERIFIED`.

### 15.2 Independent-review rule

The author of safety-critical work shall not approve that work.

Where independent review is required but has not been completed, the relevant verification status shall remain `NOT_VERIFIED`.

A reviewer's approval shall be explicit and traceable to the reviewed revision and supporting evidence.

Any actions associated with `PASS_WITH_ACTIONS` shall have documented owners, due dates or milestones, and closure criteria. This status shall not be used to bypass unresolved safety-critical issues or missing mandatory evidence.

### 15.3 Verification versus feasibility conclusion

The feasibility conclusion and verification status are separate.

For example, a study may conclude that an approach is promising while remaining `NOT_VERIFIED` because an important input or independent review is outstanding.

Both the engineering conclusion and the verification status shall be reported accurately.

## 16. Risk and Decision Management

### 16.1 Risk records

Where structured risk tracking is warranted, use a study-specific risk register, such as `outputs/risk_assessment/RISK_REGISTER.csv`.

Recommended columns:

```text
risk_id,description,category,likelihood,severity,evidence,mitigation,owner,status
```

Likelihood, severity, and risk-acceptance rules shall follow the applicable project methodology. Do not introduce incompatible scales independently within individual studies.

For a small study, a concise risk section in `FINAL_REPORT.md` may be sufficient.

### 16.2 Engineering decisions

Significant decisions shall be summarized in the canonical decision register, `registers/DECISION_REGISTER.csv`.

Recommended columns:

```text
decision_id,study_id,decision_date,decision_question,options_considered,decision,rationale,evidence,approver,status
```

The detailed analysis supporting a decision shall remain in its authoritative study artefact. The register shall summarize the decision and link to the supporting evidence.

A recommendation in a feasibility report shall not be treated as approval to modify a controlled design baseline.

## 17. Study Register and Dependencies

The authoritative study register shall be maintained at `registers/STUDY_REGISTER.csv`.

Recommended columns:

```text
study_id,study_name,product,priority,owner,reviewer,status,specification_path,dependencies,acceptance_decision,approval_date,next_action
```

The register shall identify each study, its owner, reviewer, current status, dependencies, and acceptance decision.

Use the canonical verification status values defined in Section 15 for verification fields. Study lifecycle status shall be separately defined and shall not be confused with verification status.

Dependencies shall be recorded where one study relies on another study's input, result, or decision.

If a shared input changes, assess whether dependent studies require recalculation, review, or reopening. Record the impact assessment where appropriate.

## 18. Study Lifecycle

Use the following lifecycle values for the study register: `PROPOSED`, `APPROVED_TO_START`, `IN_PROGRESS`, `BLOCKED`, `SUBMITTED_FOR_REVIEW`, `REWORK_REQUIRED`, `ACCEPTED`, `CLOSED`, `CANCELLED`.

These are lifecycle states, not verification statuses.

A study shall not be marked `ACCEPTED` merely because all expected files exist. Acceptance requires the applicable technical criteria and review requirements to be satisfied.

A study may be closed after its acceptance decision and required follow-up disposition have been recorded. A cancelled or superseded study shall retain its historical evidence and disposition.

## 19. Acceptance Criteria

A study may be accepted only when all applicable criteria below are satisfied:

1. The study objective and scope have been addressed.
2. Applicable requirements and their canonical sources are identified.
3. Material inputs and assumptions are traceable.
4. Important calculations are reproducible or independently verifiable.
5. Technical sources support conclusions that depend on external specifications.
6. Results, limitations, and uncertainties are documented.
7. Significant risks and open questions are identified.
8. The recommendation follows from the evidence.
9. Study-specific acceptance criteria are satisfied or formally dispositioned through the applicable process.
10. Required review findings are resolved or explicitly dispositioned by an authorized authority.
11. Required independent review has been completed.
12. The final review decision is recorded against the reviewed revision.

Acceptance of a feasibility study does not by itself establish production readiness, safety certification, or complete product validation.

## 20. Application Across Kritva-S, Kritva-M, and Kritva-L

The same directory structure and control principles shall apply to Kritva-S, Kritva-M, and Kritva-L.

Each study shall maintain its own specification and work plan; input inventory and assumptions; calculations and technical evidence; results and conclusions; and review and verification records.

Shared methods and templates shall remain in the common directory.

Shared requirements shall remain at their canonical source. Shared component data or engineering assumptions shall be linked to their authoritative location where one exists.

Studies shall not independently redefine a shared requirement or assumption without documenting the proposed change and following the applicable approval process.

## 21. Implementation Plan

Implementation shall proceed in the following order.

**Phase 1 — Establish common controls.** Create and review `README.md`, `common/FEASIBILITY_METHODOLOGY.md`, `common/STUDY_TEMPLATE.md`, `common/DELIVERABLES_STANDARD.md`, `common/REVIEW_CHECKLIST.md`, `registers/STUDY_REGISTER.csv`, `registers/DECISION_REGISTER.csv` and `registers/CROSS_STUDY_DEPENDENCIES.csv`. This standard remains the canonical definition of the directory and file structure.

**Phase 2 — Define the first study.** Define the specification for the integrated Kritva-M actuator feasibility study. Establish the objective, inputs, tasks, expected evidence, schedule, dependencies, and acceptance criteria before assigning the work.

**Phase 3 — Execute and review.** Perform the technical investigation, preserve the calculations and evidence, and produce the final report. Complete the required review before accepting the study.

**Phase 4 — Authorize follow-up studies.** Use the results of the integrated study to determine whether focused motor, gearbox, shaft, bearing, thermal, electrical, manufacturing, or other feasibility studies are necessary. Do not create or authorize every possible study by default.

**Phase 5 — Extend to other actuator families.** Apply the same common framework to Kritva-S and Kritva-L, defining their product-specific inputs and study IDs independently.

## 22. Standard Ownership and Change Control

The engineering lead or designated authority shall be responsible for:

- Approving this standard and subsequent revisions.
- Allocating unique study IDs.
- Approving study specifications and acceptance criteria.
- Assigning reviewers.
- Ensuring required independent reviews are completed.
- Accepting or rejecting study deliverables.
- Approving changes to controlled requirements and design baselines through the applicable process.

Study owners shall be responsible for:

- Performing the assigned engineering analysis.
- Maintaining traceable inputs, assumptions, and evidence.
- Producing the required outputs.
- Recording limitations and unresolved questions.
- Addressing review findings.
- Ensuring that the reported verification status reflects the actual evidence and review state.

Changes to this standard shall be version-controlled and reviewed according to the repository's applicable document-control conventions.

## 23. Final Standard

This document establishes the common folder and file structure for Kritva engineering feasibility studies.

The core study working areas are:

- `inputs/` — Information consumed by the study.
- `calculations/` — Working engineering analysis.
- `outputs/` — Results and final deliverables.

The study root contains the control documents. Additional directories shall be used only when relevant. Canonical requirements and other controlled artefacts shall be referenced rather than duplicated.

All feasibility conclusions shall be evidence-based, traceable, and subject to the applicable review and approval requirements.

*End of Document*
