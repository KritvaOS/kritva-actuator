# Kritva Actuator Feasibility Studies — Deliverables Standard

**Document ID:** KRITVA-ENG-FS-DEL-STD-001  
**Version:** 0.1  
**Status:** Proposed  
**Owner:** Kritva Actuator Engineering  
**Applies to:** Kritva-S, Kritva-M, Kritva-L and system-level actuator feasibility studies  
**Canonical location:** `docs/engineering/feasibility/common/DELIVERABLES_STANDARD.md`

---

## 1. Purpose

This standard defines the minimum deliverables, file formats, naming conventions, register schemas, reproducibility requirements and completion criteria for every Kritva actuator feasibility study.

It is intended to ensure that each study is:

- Traceable to applicable system requirements and engineering decisions.
- Supported by identifiable, reviewable evidence.
- Reproducible by another engineer.
- Consistent with the feasibility methodology and review process.
- Suitable for comparison across actuator variants and alternative designs.
- Auditable without relying on undocumented knowledge held by the study author.

This document establishes deliverable-control rules. It does not replace engineering requirements, detailed calculation methods, safety standards or study-specific acceptance criteria.

## 2. Related documents

| Document | Purpose |
|---|---|
| `../FEASIBILITY_STUDIES_STANDARD.md` | Governing feasibility-study structure and lifecycle |
| `FEASIBILITY_METHODOLOGY.md` | Engineering methodology, input classification, uncertainty and risk assessment |
| `STUDY_TEMPLATE.md` | Template for study-specific `SPECIFICATION.md` |
| `REVIEW_CHECKLIST.md` | Review and acceptance checks |
| `../registers/STUDY_REGISTER.csv` | Canonical study status and metadata |
| `../registers/DECISION_REGISTER.csv` | Canonical cross-study engineering decisions |
| `../../../..` — repository root | Resolve links to repository-level requirements and standards |

The canonical requirements source is `requirements/SYSTEM_REQUIREMENTS.md`. Requirements must be referenced by their existing `SYS-REQ-nnn` identifiers. Do not create duplicate requirement definitions in a feasibility study.

If a linked document does not yet exist, record it as a dependency or open item. Do not imply that a missing document has been approved or that its contents have been verified.

## 3. Deliverable classification

Every deliverable shall be classified as Mandatory (M), Conditional (C) or Optional (O).

| Classification | Meaning | Completion rule |
|---|---|---|
| M — Mandatory | Required for every study, regardless of its technical scope | Must be present and meet its minimum content requirements before study acceptance |
| C — Conditional | Required when triggered by study scope, engineering method, evidence needs or an explicit reviewer decision | Trigger and applicability must be recorded; if applicable, the deliverable is required |
| O — Optional | May be included when it adds useful evidence or improves engineering decisions | If included, it must follow the applicable format, traceability and review rules |

### 3.1 Rules for conditional deliverables

A conditional deliverable must not be silently omitted.

For each C deliverable, the study owner shall record one of the following:

- `APPLICABLE` — the deliverable is required and must be completed.
- `NOT_APPLICABLE` — the deliverable is not required for this study; provide a concise justification.
- `PENDING_DECISION` — applicability has not been resolved; the study cannot be accepted while a required applicability decision remains unresolved.

An explicit study-specific acceptance criterion or reviewer direction may make a normally conditional deliverable mandatory.

A deliverable marked not applicable does not override a requirement, safety obligation, contractual obligation or applicable engineering standard.

### 3.2 Minimum deliverable inventory

| Deliverable | Class | Minimum expectation |
|---|---|---|
| `SPECIFICATION.md` | M | Approved scope, requirements, inputs, tasks, deliverables and acceptance criteria |
| `WORK_PLAN.md` | M | Tasks, owners, dependencies, milestones and completion evidence |
| `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` | M | Traceable assumptions, unresolved questions and their dispositions |
| `REVIEW.md` | M | Review records, findings, actions and final review recommendation |
| Study `README.md` | M | Study purpose, navigation, status and instructions for reproducing results |
| `inputs/` | M | Directory exists; contains controlled input files or a README explaining input provenance and locations |
| `calculations/` | C | Applicable analytical calculations and supporting scripts |
| `component_research/` | C | Required when component alternatives, vendor specifications or component suitability are evaluated |
| `simulation/` | C | Required when simulation or numerical modelling contributes to a conclusion |
| `CAD/` | C | Required when geometry, packaging, interference or mechanical design is evaluated using CAD |
| `test_data/` | C | Required when physical, bench, prototype or other empirical tests contribute to a conclusion |
| `outputs/` | M | Study results, comparison tables, plots, reports and the final conclusion |
| `references/` | M | Source register and accessible copies or links to relied-upon evidence |
| `cost_estimate/` | C | Required when cost, BOM, manufacturing economics or cost trade-offs are evaluated |
| `CHANGELOG.md` | C | Required when a study has multiple controlled revisions or its history is needed to understand changed results |
| Additional evidence | O | Additional supporting material that improves traceability or technical understanding |

The directories marked C shall be created when applicable. For a non-applicable directory, record the applicability decision in the study specification and README rather than creating empty placeholder files throughout the directory.

The study owner may use subdirectories when needed, provided the canonical study structure remains recognizable.

## 4. Standard study directory structure

The following is the recommended structure. Conditional directories are included only when applicable.

```text
FS-M-NNN-short-study-name/
  README.md
  SPECIFICATION.md
  WORK_PLAN.md
  ASSUMPTIONS_AND_OPEN_QUESTIONS.md
  REVIEW.md
  CHANGELOG.md
  inputs/
    README.md
  calculations/
    README.md
  component_research/
    README.md
  simulation/
    README.md
  CAD/
    README.md
  test_data/
    README.md
  outputs/
    README.md
    SOURCE_REGISTER.csv
    RISK_REGISTER.csv
    comparison_table.csv
    results.csv
  cost_estimate/
    README.md
    BOM_COST_ESTIMATE.csv
  references/
    README.md
```

This is an illustrative layout, not a requirement to create every conditional directory. Do not create empty CSV files containing only headers to suggest that analysis has been completed.

Each directory that contains evidence must have a README describing the contents, provenance, relationships and reproduction instructions. A directory that is not applicable need not have a README.

## 5. Minimum content for mandatory control files

### 5.1 `README.md`

The study README is the navigation entry point. It must contain:

1. Study ID and title.
2. Product or system scope.
3. Study owner and reviewer roles.
4. Current study lifecycle and verification status.
5. Purpose and engineering question.
6. Scope summary and applicable requirements.
7. Links to `SPECIFICATION.md`, `WORK_PLAN.md`, `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` and `REVIEW.md`.
8. Directory map with brief descriptions of applicable evidence folders.
9. Summary of major results and current feasibility conclusion, if available.
10. Links to the main result tables, calculation entry points, models and reports.
11. Instructions to reproduce the main results.
12. Open blockers, required reviews and next actions.
13. Revision or change history link, if applicable.

The README must distinguish planned work from completed work. Do not describe a result as verified, accepted or released unless the applicable evidence and approvals support that status.

### 5.2 `SPECIFICATION.md`

This file defines the authorized study scope and acceptance basis. It must contain:

1. Document control metadata, including study ID, version and status.
2. Purpose and engineering question.
3. Decisions the study is intended to support.
4. Background and design context.
5. In-scope activities and explicit exclusions.
6. Applicable requirements using canonical `SYS-REQ-nnn` identifiers and links.
7. Inputs, their units, source references and status classifications.
8. Assumptions and unresolved questions.
9. Technical approach and planned analysis tasks.
10. Required deliverables and applicability decisions.
11. Study-specific acceptance criteria.
12. Dependencies and interfaces with other studies.
13. Roles, responsibilities and required independent reviews.
14. Schedule, checkpoints and expected evidence.
15. Safety, reliability and manufacturing considerations relevant to scope.
16. Approval record for authorization to start, where required.

Changes to scope, requirements, input baselines or acceptance criteria after approval must be documented and reviewed.

### 5.3 `WORK_PLAN.md`

This file defines how the study will be executed. It must contain:

1. Study ID and reference to the governing specification.
2. Ordered work packages or tasks.
3. Unique task identifiers.
4. Task descriptions and expected outputs.
5. Task owners and reviewers, where assigned.
6. Dependencies and sequencing constraints.
7. Planned milestones and checkpoints.
8. Required tools, datasets, component samples or test equipment.
9. Entry criteria and exit criteria for major tasks.
10. Status and evidence links for completed tasks.
11. Blockers, schedule changes and corrective actions.
12. Final completion and handoff activities.

A task marked complete must point to evidence, a reviewed artefact or a documented reason why no artefact is needed. Completion must not be inferred from the presence of a file alone.

### 5.4 `ASSUMPTIONS_AND_OPEN_QUESTIONS.md`

This file tracks uncertainty that may affect the study conclusion. It must contain:

1. Study ID and revision.
2. Unique assumption or question ID.
3. Statement of the assumption or question.
4. Reason it is necessary.
5. Source or rationale.
6. Classification and status.
7. Affected calculations, requirements, components or conclusions.
8. Impact if incorrect or unresolved.
9. Planned method to resolve or validate it.
10. Owner and target checkpoint, where assigned.
11. Resolution evidence and disposition.
12. Date and reviewer of resolution, where applicable.

Use explicit classifications such as `APPROVED`, `PRELIMINARY`, `ASSUMED`, `UNKNOWN` and `MEASURED` for input confidence or provenance as appropriate. These labels are not substitutes for a separate workflow status.

An unresolved assumption that can materially change a safety-critical or feasibility conclusion must remain visible in the final conclusion and may prevent acceptance.

### 5.5 `REVIEW.md`

This file is the study review record. It must contain:

1. Study ID and reviewed revision or commit.
2. Review scope and applicable checklist.
3. Author and reviewer identities or roles.
4. Review date and review type.
5. Artefacts and evidence reviewed.
6. Requirement and acceptance-criteria coverage.
7. Technical findings, including calculation and unit checks.
8. Findings classified by severity or priority.
9. Action items, owners and closure evidence.
10. Independent review status for safety-critical work.
11. Final recommendation and rationale.
12. Approval or rejection record, including reviewer and date.
13. Remaining limitations, deviations and accepted residual risks, where authorized.

The author may not approve their own safety-critical work. If the required independent review is missing, the affected verification status must be `NOT_VERIFIED`.

### 5.6 `CHANGELOG.md`

When required, this file must contain:

1. Study ID.
2. Revision or version.
3. Date.
4. Author.
5. Summary of changes.
6. Reason for the change.
7. Impact on results, requirements, assumptions and decisions.
8. Revalidation or review required.
9. Commit or other immutable change reference, when available.

Do not use the changelog as a replacement for version control, review records or the decision register.

## 6. Minimum content for every directory README

Each README in an evidence directory must explain what the directory contains and how the evidence is used.

| Directory | Required README content |
|---|---|
| `inputs/README.md` | Input inventory, source, revision, units, status classification, access method and input ownership |
| `calculations/README.md` | Calculation inventory, execution order, tools, dependencies, entry points and reproduction instructions |
| `component_research/README.md` | Component categories, selection criteria, vendor/source references, candidate identifiers and comparison approach |
| `simulation/README.md` | Model purpose, simulator/version, model assumptions, boundary conditions, configuration, run instructions and output locations |
| `CAD/README.md` | CAD tool/version, assembly structure, coordinate conventions, units, source files, model dependencies and export instructions |
| `test_data/README.md` | Test purpose, equipment, setup, calibration status, conditions, raw-data inventory, processing steps and limitations |
| `outputs/README.md` | Result inventory, units, comparison criteria, conclusion location, traceability to inputs and reproduction instructions |
| `cost_estimate/README.md` | Costing basis, currency, quantity assumptions, manufacturing volume, sourcing basis, date and treatment of taxes, shipping and non-recurring costs |
| `references/README.md` | Source-register location, reference organization, document revisions, access constraints and evidence provenance |

A README must not merely repeat the directory name. It must enable another engineer to locate the relevant evidence and understand its purpose.

If a directory contains only a single small file and no independent workflow, its README may be omitted only if the study specification records that exception and the main study README provides the required navigation and reproduction information.

## 7. Accepted file formats

### 7.1 Preferred formats

| Purpose | Preferred format | Additional acceptable formats |
|---|---|---|
| Engineering narrative and control files | Markdown `.md` | Plain text `.txt` for supplementary notes |
| Tabular data and registers | CSV `.csv`, UTF-8 | XLSX `.xlsx` for interactive analysis, provided a canonical machine-readable export is also maintained where required |
| Calculations and analysis scripts | Python `.py`, Jupyter notebook `.ipynb` | MATLAB/Octave source, spreadsheet formulas, other documented engineering tools |
| Plots and diagrams | SVG `.svg`, PNG `.png`, PDF `.pdf` | Other documented vector or raster formats |
| CAD source | Native CAD format | STEP `.step`/`.stp` and other suitable exchange formats |
| Simulation models and results | Native model and result formats | CSV, TXT and documented report formats |
| Test data | CSV `.csv`, UTF-8 | JSON, binary instrument output or native acquisition format with a documented decoder |
| BOM and cost estimate | CSV `.csv`, UTF-8 | XLSX as a working view, with a controlled CSV export |
| External evidence | Original source format | PDF or stable source URL, where permitted |
| Compressed datasets | ZIP `.zip` or another documented archive | Other formats only when tool constraints require them |

### 7.2 Format requirements

1. Use UTF-8 text encoding for Markdown, CSV and text files.
2. Prefer open, portable and machine-readable formats.
3. Preserve original vendor datasheets and original test outputs when permitted.
4. Never replace raw test data with only a processed plot or summary.
5. For proprietary formats, document the tool, version and any licensing or access constraints.
6. When a binary or proprietary file is required, include a human-readable summary and enough metadata to identify and reproduce its use.
7. Do not commit generated caches, temporary files, large disposable intermediate files or credentials.
8. Large datasets may be stored in an approved artifact store if the repository contains a stable identifier, revision or checksum, access instructions and reproduction metadata.
9. The absence of an external file from the repository must not make a conclusion impossible to audit.
10. If a required format cannot be generated with the available tools, document the limitation and propose an equivalent controlled artefact for reviewer approval.

## 8. Naming and versioning rules

### 8.1 Study and file names

- Study IDs shall use `FS-<PRODUCT>-<NUMBER>`, for example `FS-M-001`.
- Product identifiers shall be consistent with the governing feasibility standard.
- Study directory names shall use the study ID followed by a concise lowercase kebab-case description.
- Use the canonical control-file names defined in this standard.
- Use uppercase snake case for standard register names and prescribed CSV filenames.
- Use lowercase snake case for calculation scripts and machine-generated data files.
- Use descriptive names for reports, plots, simulation cases and CAD exports.
- Include units in a filename only when they materially distinguish the artefact and do not replace the units recorded inside it.
- Avoid names such as `final`, `final2`, `latest`, `new`, `test1` or `fixed` as the only revision identifier.

Examples:

```text
FS-M-001-integrated-actuator-system/
calculations/output_torque_budget.py
calculations/gear_ratio_sweep.py
outputs/torque_speed_comparison.csv
outputs/torque_speed_comparison.svg
simulation/README.md
CAD/assembly_envelope.step
test_data/no_load_speed_run_001.csv
```

### 8.2 Revisions

1. Use version control for source-controlled files.
2. Use a version field in the control-file metadata.
3. Use a commit hash or other immutable revision reference to identify the exact source state used to generate results.
4. Do not create a separate copy of every revision unless a controlled baseline or archival requirement makes it necessary.
5. When an analysis change could alter a conclusion, regenerate affected outputs and record the change.
6. Record the tool version and significant dependency versions for reproducible calculations.
7. External vendor documents must include the source revision or publication date when available.
8. File modification timestamps alone are not an acceptable revision-control mechanism.

## 9. Standard CSV schemas

All prescribed CSV files shall have one header row, consistent column order and one record per logical entity. Column names must match the schemas below unless an approved study-specific extension is recorded.

CSV conventions:

- Encoding: UTF-8.
- Delimiter: comma.
- First row: header.
- Quote fields containing commas, quotes or line breaks according to CSV conventions.
- Decimal separator: period.
- Units: explicit column or field; do not rely on implicit display formatting.
- Missing values: empty field plus a documented reason or status where meaningful; do not use `0` to mean unknown.
- Boolean values: `TRUE` or `FALSE`.
- Dates: ISO 8601, preferably `YYYY-MM-DD`; timestamps include timezone where relevant.
- Enumerated values: use controlled spellings documented in the relevant file.
- Identifiers: stable and unique within the applicable register.

### 9.1 `SOURCE_REGISTER.csv`

Purpose: trace every important external source, internal input, measurement or dataset used to support the study.

Required header:

```text
source_id,source_type,title,manufacturer_or_author,document_number,revision_or_version,publication_date,access_date,source_location,checksum,applicable_claim_or_parameter,units,source_quality,approval_status,study_usage,limitations,notes
```

Column guidance:

- `source_id`: stable source identifier, unique within the study.
- `source_type`: for example `DATASHEET`, `STANDARD`, `APPLICATION_NOTE`, `REQUIREMENT`, `MEASUREMENT`, `INTERNAL_DOCUMENT`, `SIMULATION_MODEL` or `WEB_SOURCE`.
- `title`: source title or dataset name.
- `manufacturer_or_author`: responsible organization or author.
- `document_number`: document identifier, if available.
- `revision_or_version`: source revision, publication version or dataset revision.
- `publication_date`: publication date, when known.
- `access_date`: date accessed or retrieved.
- `source_location`: repository-relative path, stable URL or controlled artifact location.
- `checksum`: checksum for a stored file when practical; state `NOT_RECORDED` only when the omission is justified.
- `applicable_claim_or_parameter`: parameter, requirement or claim supported.
- `units`: units associated with the supported parameter, if applicable.
- `source_quality`: evidence-quality classification based on the methodology.
- `approval_status`: whether the source or input has the necessary approval for the intended use.
- `study_usage`: where and how the source is used.
- `limitations`: restrictions, uncertainties, applicability conditions or missing information.
- `notes`: supplementary information.

A source's presence in this register does not mean the source is approved, authoritative or applicable. Those attributes must be evaluated for the intended claim.

### 9.2 `RISK_REGISTER.csv`

Purpose: track technical, safety, schedule, manufacturing, supply and evidence risks that can affect the study or its conclusion.

Required header:

```text
risk_id,risk_title,category,cause,event,consequence,likelihood_1_to_5,severity_1_to_5,risk_score,initial_risk_band,existing_controls,mitigation_action,action_owner,due_date,residual_likelihood_1_to_5,residual_severity_1_to_5,residual_risk_score,residual_risk_band,status,affected_requirements,affected_deliverables,evidence_link,reviewer,notes
```

Column guidance:

- `risk_id`: unique stable identifier.
- `risk_title`: concise description.
- `category`: risk domain.
- `cause`, `event`, `consequence`: distinguish the underlying cause, uncertain event and potential impact.
- `likelihood_1_to_5`: likelihood rating using the approved project risk scale.
- `severity_1_to_5`: severity rating using the approved project risk scale.
- `risk_score`: likelihood multiplied by severity, unless the approved risk policy specifies another calculation.
- `initial_risk_band`: risk band before additional mitigation.
- `existing_controls`: controls already implemented and evidenced.
- `mitigation_action`: planned or completed action.
- `action_owner`: accountable owner.
- `due_date`: target date where applicable.
- `residual_likelihood_1_to_5`, `residual_severity_1_to_5`, `residual_risk_score`, `residual_risk_band`: residual assessment after credited controls.
- `status`: controlled workflow status, defined in the study README or approved risk policy.
- `affected_requirements`: applicable canonical requirement IDs.
- `affected_deliverables`: impacted file or evidence identifiers.
- `evidence_link`: evidence of controls, mitigation or closure.
- `reviewer`: person or role responsible for risk review.
- `notes`: supplementary information.

Use the risk bands and scoring method approved for the project. If only the proposed bands in `FEASIBILITY_METHODOLOGY.md` are available, identify them as provisional and obtain the necessary approval before using them as a project-wide acceptance policy.

Safety-critical risks must not be closed solely because a numerical risk score is low. Required safety review and acceptance remain independent obligations.

### 9.3 Standard comparison tables

Purpose: compare design candidates using consistent criteria, source-backed data and explicit uncertainty.

Required header:

```text
comparison_id,candidate_id,candidate_name,criterion_id,criterion_name,requirement_id,value,units,acceptance_limit,margin,source_id,input_status,method,uncertainty_or_range,confidence,decision_relevance,notes
```

Column guidance:

- `comparison_id`: identifier for the comparison set.
- `candidate_id`: unique candidate identifier.
- `candidate_name`: readable candidate name.
- `criterion_id`: stable criterion identifier.
- `criterion_name`: criterion being evaluated.
- `requirement_id`: applicable `SYS-REQ-nnn` or an explicit study-specific criterion identifier.
- `value`: evaluated value or result.
- `units`: engineering units.
- `acceptance_limit`: applicable limit, target or range.
- `margin`: calculated margin using a stated convention.
- `source_id`: link to the source register.
- `input_status`: `APPROVED`, `PRELIMINARY`, `ASSUMED`, `UNKNOWN` or `MEASURED`, as appropriate.
- `method`: calculation, measurement, simulation or evaluation method.
- `uncertainty_or_range`: uncertainty, tolerance or evaluated range.
- `confidence`: evidence-confidence classification, if used.
- `decision_relevance`: explanation of how the criterion affects selection.
- `notes`: additional conditions and limitations.

The comparison table may contain multiple rows per candidate, one per criterion. Define margin direction and units explicitly; a positive margin must not be assumed to mean acceptable without understanding the criterion.

For readability, a derived human-readable matrix may be produced from this canonical table. The derived matrix must identify the source data and must not silently change values or acceptance logic.

### 9.4 Calculation results CSV

Purpose: provide machine-readable outputs from calculations, simulations or parameter sweeps.

Required header:

```text
run_id,study_id,calculation_id,calculation_version,case_id,parameter_name,parameter_value,parameter_units,result_name,result_value,result_units,acceptance_limit,margin,pass_fail_status,input_status,source_ids,tool_name,tool_version,run_timestamp,code_revision,notes
```

Column guidance:

- `run_id`: unique execution identifier.
- `study_id`: study identifier.
- `calculation_id`: stable calculation or model identifier.
- `calculation_version`: version of the calculation method.
- `case_id`: unique scenario, sweep point or test case.
- `parameter_name`, `parameter_value`, `parameter_units`: evaluated input parameter.
- `result_name`, `result_value`, `result_units`: result name, numeric value and units.
- `acceptance_limit`: applicable limit or target, if defined.
- `margin`: result margin using the documented convention.
- `pass_fail_status`: controlled result status, including `NOT_EVALUATED` where no valid limit exists.
- `input_status`: confidence/provenance classification for the evaluated input set, with mixed-input cases explained in notes or a linked input manifest.
- `source_ids`: identifiers from `SOURCE_REGISTER.csv`, using a documented delimiter when multiple sources are referenced.
- `tool_name`, `tool_version`: execution tool and version.
- `run_timestamp`: timestamp of the run with timezone where available.
- `code_revision`: immutable revision of the calculation source.
- `notes`: limitations, warnings and special conditions.

For a calculation producing multiple parameters and results, use one row per parameter-result combination or publish a normalized results file with a documented schema. Do not mix quantities with incompatible units in a single value column without an accompanying units field.

### 9.5 BOM and cost estimate CSV

Purpose: record component-level cost estimates and the basis for comparing cost across candidate designs.

Required header:

```text
bom_item_id,candidate_id,reference_designator,component_name,manufacturer,manufacturer_part_number,description,quantity_per_unit,unit_of_measure,unit_cost,currency,extended_cost,cost_basis,quantity_basis,annual_volume,source_id,quote_date,lead_time,moq,availability_status,make_or_buy,recurring_or_nonrecurring,manufacturing_process,excluded_costs,confidence,notes
```

Column guidance:

- `bom_item_id`: unique line identifier.
- `candidate_id`: candidate design to which the line belongs.
- `reference_designator`: designator or assembly location, if assigned.
- `component_name`: component or assembly name.
- `manufacturer`: manufacturer, if known.
- `manufacturer_part_number`: exact part number, where applicable.
- `description`: specification or short description.
- `quantity_per_unit`: quantity required per finished actuator or defined assembly.
- `unit_of_measure`: `EA`, `SET`, `M`, `KG` or another defined unit.
- `unit_cost`: cost per stated unit.
- `currency`: ISO 4217 currency code, for example `INR` or `USD`.
- `extended_cost`: quantity multiplied by unit cost, with currency and rounding conventions documented.
- `cost_basis`: supplier quote, distributor price, estimate, historical cost or other basis.
- `quantity_basis`: manufacturing or purchase volume corresponding to the estimate.
- `annual_volume`: estimated annual volume, where relevant.
- `source_id`: source-register identifier.
- `quote_date`: quote or price-observation date.
- `lead_time`: supplier lead time and units or a defined textual representation.
- `moq`: minimum order quantity, if known.
- `availability_status`: known sourcing or availability status.
- `make_or_buy`: planned manufacturing or sourcing approach.
- `recurring_or_nonrecurring`: identifies recurring component cost versus non-recurring expense.
- `manufacturing_process`: relevant process or finishing route.
- `excluded_costs`: costs not included in the line or estimate.
- `confidence`: confidence classification.
- `notes`: qualifications and additional detail.

Cost-estimate rules:

1. Do not combine currencies without an explicit conversion basis, exchange rate and date.
2. Distinguish component costs from machining, assembly, testing, tooling, development, shipping, duties, taxes and overhead.
3. Avoid double-counting purchased assemblies and their constituent parts.
4. Separate recurring unit cost from non-recurring engineering and tooling costs.
5. Record volume assumptions and supplier quote dates.
6. Identify estimated values separately from confirmed quotes.
7. Include all material components in the defined BOM scope, including fasteners, connectors, wiring and ancillary parts where relevant.
8. The cost-estimate README must define whether the estimate is ex-works, landed, tax-inclusive or otherwise bounded.
9. Do not report a complete actuator cost if significant cost categories are excluded or unknown. Report the scope and limitations instead.

## 10. Calculation-file header block

Every calculation source file must begin with a header containing the following fields. Use equivalent metadata for tools that do not support source-code comments, and link the metadata to the calculation artefact.

```text
Calculation ID: CALC-<STUDY-ID>-<NNN>
Study ID: FS-<PRODUCT>-<NNN>
Title: <Calculation title>
Version: <Semantic or project-defined version>
Status: <PROPOSED | IN_PROGRESS | REVIEWED | APPROVED>
Author: <Name or role>
Reviewer: <Name or role, if assigned>
Purpose: <Engineering question this calculation answers>
Inputs: <Input names and source identifiers>
Units: <Units and unit convention>
Method: <Equations, algorithm or method reference>
Assumptions: <Assumptions and applicability limits>
Dependencies: <Tool and library dependencies>
Expected outputs: <Output artefacts and result names>
Reproduction: <Command, workbook procedure or execution steps>
Acceptance criteria: <Relevant limits or study-specific criteria>
Change reference: <Commit or controlled revision>
```

The header may include additional fields required by a tool, analysis method or applicable engineering discipline.

### 10.1 Calculation implementation rules

1. Use descriptive variable names and explicit units.
2. Avoid ambiguous bare constants when they represent physical quantities; annotate units or convert into a documented internal unit system.
3. Document equation sources and applicability limits.
4. Include input validation and sanity checks where practical.
5. Handle invalid, missing or out-of-range inputs explicitly.
6. Separate raw inputs, intermediate calculations and reported results.
7. Do not silently replace unknown values with defaults.
8. Record numerical precision, rounding and significant-figure conventions where they affect decisions.
9. Include warnings and limitations in generated outputs.
10. Provide a minimal test or independent hand-check for calculations that materially affect design decisions.
11. Where feasible, validate analytical results against an independent method or trusted reference case.
12. A reviewed calculation is not automatically approved for every product or operating condition; applicability must be established.

## 11. Reproducibility requirements

A study must provide enough information for another qualified engineer to reproduce its material conclusions without relying on undocumented conversations with the original author.

### 11.1 Required reproducibility information

For each material calculation, simulation, CAD evaluation or test-data analysis, record:

- Exact input files, revisions and source identifiers.
- Input values, units, confidence classifications and assumptions.
- Equations, algorithms, boundary conditions and model simplifications.
- Tool and software versions.
- Relevant library, package and solver versions.
- Execution commands, configuration files or procedural steps.
- Random seeds for stochastic methods, where supported and material.
- Mesh settings, solver tolerances, convergence criteria or equivalent model settings, where applicable.
- CAD coordinate system, units, material definitions and configuration identifiers, where applicable.
- Test equipment, calibration status, environmental conditions and acquisition settings, where applicable.
- Raw data, data-processing steps and filtering rules.
- Output files, run identifiers and timestamps.
- Source revision or commit hash.
- Known sources of non-determinism and acceptable reproducibility tolerances.

### 11.2 Reproduction levels

The study owner shall identify the reproduction level appropriate to each evidence type.

- `LEVEL_1_REVIEWABLE`: inputs, equations or methods, units and outputs are documented well enough for an independent technical review.
- `LEVEL_2_REPRODUCIBLE`: another engineer can rerun the analysis using available inputs and documented tools.
- `LEVEL_3_INDEPENDENTLY_CHECKED`: material results have been reproduced or cross-checked by an independent engineer or a genuinely independent method.

The required level depends on the engineering risk and study acceptance criteria. Level 1 alone is not sufficient where a study explicitly requires rerunning a model or independent verification.

### 11.3 Raw and derived evidence

1. Preserve original test data separately from processed results.
2. Never overwrite raw data during cleaning or transformation.
3. Record each transformation, filter, exclusion or correction.
4. Maintain a traceable relationship between raw data, processing scripts and reported results.
5. Use stable input manifests or checksums for large or externally stored datasets.
6. Record missing, corrupted, clipped or otherwise suspect observations.
7. State whether plots are generated from raw or processed data.
8. Do not manually edit a generated result without recording the change and its rationale.
9. For spreadsheet calculations, identify formula cells, input cells, external links and any manual overrides.
10. For simulation results, record convergence status and warnings; a run that did not converge must not be presented as a valid quantitative result without explicit justification.

### 11.4 Reproducibility failure

If a material result cannot be reproduced:

- Record the failure in `REVIEW.md` and the relevant assumptions or risk records.
- Identify the missing input, tool, source revision or procedural step.
- Mark the affected result as not verified.
- Assess whether the conclusion remains supported by independent evidence.
- Rework the evidence or obtain an explicitly justified, reviewed disposition.

Do not mark a study accepted solely because the original author can reproduce the result on their own workstation.

## 12. Deliverable-by-study-type matrix

This matrix defines the default applicability for the proposed Kritva-M study sequence. The study specification and reviewer may add deliverables when required by actual scope or evidence.

Legend:

- `M` — mandatory for the study type.
- `C` — conditional; applicability must be decided and justified.
- `O` — optional.
- `—` — not expected by default; create only if scope or evidence requires it.

| Study | Calculations | Component research | Simulation | CAD | Test data | Cost estimate |
|---|---|---|---|---|---|---|
| FS-M-001 Integrated actuator system feasibility | M | M | C | M | C | C |
| FS-M-002 Load and torque analysis | M | — | C | C | C | — |
| FS-M-003 Motor selection and sizing | M | M | C | C | C | C |
| FS-M-004 Gearbox selection and ratio optimization | M | M | C | C | C | C |
| FS-M-005 Output shaft feasibility | M | C | C | M | C | C |
| FS-M-006 Bearing and support feasibility | M | M | C | M | C | C |
| FS-M-007 Housing and mechanical integration | M | C | C | M | C | C |
| FS-M-008 Electrical and thermal feasibility | M | M | C | C | C | C |
| FS-M-009 Manufacturing and cost feasibility | C | M | C | C | C | M |
| FS-M-010 Integrated design trade-off | M | C | C | C | C | M |

### 12.1 Matrix interpretation

- `FS-M-001`: Establish the integrated actuator feasibility baseline. Include system calculations, component evidence and CAD-based packaging evidence. Simulation, testing and costing are conditional on the scope and evidence needed for the initial decision.
- `FS-M-002`: Establish load cases, torque and speed demands, duty-cycle assumptions and uncertainty. Simulation, CAD and test data are conditional on whether analytical methods alone are sufficient.
- `FS-M-003`: Compare motor candidates against torque-speed, power, current, thermal and operating constraints. Component research is mandatory; costing is conditional unless the specification requires a cost-based selection.
- `FS-M-004`: Evaluate candidate gearbox technologies and ratios against output torque, speed, efficiency, backlash, life, envelope and interface requirements. Vendor or component research is mandatory.
- `FS-M-005`: Assess shaft geometry, material, combined loading, deflection, stress concentration and fatigue. CAD is mandatory to establish geometry and interfaces. More advanced simulation and test evidence depend on risk and model validity.
- `FS-M-006`: Assess bearing selection, load distribution, life, stiffness, mounting and support arrangement. Component research and CAD are mandatory for the baseline evaluation.
- `FS-M-007`: Assess housing geometry, interfaces, stiffness, clearances, assembly access, mass and manufacturability. CAD is mandatory.
- `FS-M-008`: Assess electrical supply, current, power loss, motor drive, wiring and thermal limits. Component research is mandatory; simulation and test data depend on available thermal and electrical evidence.
- `FS-M-009`: Assess manufacturing routes, sourcing, assembly, yield assumptions and cost. BOM and cost-estimate evidence are mandatory; calculations, CAD and simulation are conditional on the manufacturing questions being evaluated.
- `FS-M-010`: Compare integrated candidate architectures against requirements, performance, risk, manufacturing and cost. A consistent calculation and comparison baseline is mandatory. A final CAD, simulation or test-data package is conditional on its contribution to the decision.

### 12.2 Applicability override

The matrix is a planning baseline, not permission to omit necessary evidence.

A study owner shall record the applicability of every conditional deliverable in `SPECIFICATION.md`. If the engineering question cannot be answered credibly without a deliverable marked conditional or not expected by default, the deliverable becomes required for that study.

If a required deliverable is unavailable, the study may remain in progress, blocked or submitted for review with explicit limitations. It must not be accepted by simply relabeling the missing evidence as not applicable.

## 13. Definition of Done

A study is ready for acceptance only when the applicable checks below are satisfied.

### 13.1 Scope and requirements

- [ ] Study ID, product scope, owner and reviewer are defined.
- [ ] The specification is approved to the level required by the study lifecycle.
- [ ] Applicable canonical requirements are identified using `SYS-REQ-nnn`.
- [ ] Requirements have not been duplicated or silently redefined.
- [ ] Study-specific acceptance criteria are explicit and testable.
- [ ] Scope changes and deviations are documented.

### 13.2 Inputs and assumptions

- [ ] Material inputs have identifiable sources and units.
- [ ] Input status classifications are recorded.
- [ ] Preliminary values and assumptions are not presented as approved requirements.
- [ ] Open questions have owners or explicit dispositions.
- [ ] Uncertainty and sensitivity are assessed where they could change the conclusion.
- [ ] Missing information that affects safety or feasibility is visible in the conclusion.

### 13.3 Technical evidence

- [ ] Mandatory calculations, research, models, CAD, tests and costing deliverables are complete as applicable.
- [ ] Calculations have documented equations, inputs, units, methods and assumptions.
- [ ] Material results have sanity checks or independent checks appropriate to risk.
- [ ] Simulation and test limitations are recorded.
- [ ] Raw and derived data are distinguishable.
- [ ] Comparison criteria and margin conventions are consistent across candidates.
- [ ] Results are traceable to sources, requirements and input revisions.
- [ ] Cost estimates identify currency, volume assumptions, exclusions and confidence.
- [ ] Required CSV files follow the prescribed schemas.
- [ ] The final conclusion follows from the presented evidence and states remaining limitations.

### 13.4 Reproducibility and file quality

- [ ] All mandatory control files exist and meet their minimum content requirements.
- [ ] Every applicable evidence directory has a useful README.
- [ ] Filenames and study IDs follow the standard.
- [ ] Required input and tool versions are recorded.
- [ ] Material results can be reproduced or have an approved, documented alternative verification basis.
- [ ] The source revision used for results is identifiable.
- [ ] No required input, script, model configuration or evidence file is missing.
- [ ] No credentials, secrets or unapproved sensitive information are committed.
- [ ] Links and references resolve or explicitly describe access restrictions.
- [ ] Generated outputs are consistent with the reviewed source revision.

### 13.5 Risk and review

- [ ] Material risks are recorded and assessed.
- [ ] Mitigation actions have owners and closure evidence where required.
- [ ] Safety-critical issues have received the required independent review.
- [ ] The author has not approved their own safety-critical work.
- [ ] Review findings are dispositioned or explicitly remain open with an authorized decision.
- [ ] Required reviewers have recorded their decisions.
- [ ] Residual risks and limitations are visible and appropriately authorized.
- [ ] Verification statuses use the controlled values defined by the feasibility standard.

### 13.6 Final acceptance and handoff

- [ ] `README.md` provides a reliable entry point and reproducing instructions.
- [ ] `WORK_PLAN.md` reflects actual completion and links to evidence.
- [ ] `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` has current dispositions.
- [ ] `REVIEW.md` records the final review outcome and unresolved actions.
- [ ] Conditional deliverables have explicit applicability decisions.
- [ ] The study register has been updated through the established process.
- [ ] Relevant engineering decisions are recorded in the canonical decision register when required.
- [ ] Follow-on studies, design actions and requirement changes are identified.
- [ ] The study conclusion and lifecycle status are consistent with its evidence and approvals.

### 13.7 Completion is not equivalent to feasibility

A study may satisfy the Definition of Done and conclude that feasibility has not been established or that a candidate is potentially infeasible. This is a valid engineering outcome if the question has been adequately investigated and the evidence supports the conclusion.

Likewise, a complete set of files does not prove that a design is safe, feasible, verified or approved for release.

Use the verification status values defined by the governing feasibility standard:

- `NOT_STARTED`
- `IN_PROGRESS`
- `PASS`
- `PASS_WITH_ACTIONS`
- `FAIL`
- `NOT_VERIFIED`

Use the study lifecycle values separately. Do not substitute a lifecycle state for a verification status.

## 14. Exceptions and change control

Any exception to this standard must be documented in the study specification or review record with:

1. The rule being waived or modified.
2. The reason for the exception.
3. The affected deliverables and conclusions.
4. The technical or auditability impact.
5. Compensating controls, if required.
6. The approving reviewer or authority.
7. The date and evidence of approval.

An exception cannot waive an applicable legal, contractual, safety or approved system requirement.

Changes to this standard shall be reviewed for compatibility with existing studies, registers and automated tooling. Where a schema change affects machine-readable files, document the migration or compatibility strategy before applying it to active studies.

## 15. Approval status

This document is **Proposed**.

Until approved, it is a working baseline for establishing consistent feasibility-study deliverables. Study owners shall identify any mandatory project policy that remains provisional and shall not represent proposed rules as formally approved requirements.

Approval should confirm, at minimum:

- The M/C/O deliverable classification.
- The mandatory control-file content.
- The CSV schemas and naming rules.
- The reproducibility requirements.
- The FS-M-001 through FS-M-010 applicability matrix.
- The Definition of Done and independent-review obligations.
