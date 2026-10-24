---
study_id: FS-M-009
title: Manufacturing and Cost Feasibility - Inputs
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Project Lead
priority: P3
upstream: [FS-M-003, FS-M-004, FS-M-005, FS-M-006, FS-M-007, FS-M-008]
downstream: [FS-M-010]
---

# FS-M-009 Inputs Register

## 1. Purpose and rules

This register records the verified upstream inputs, required study artifacts, and additional data needed for manufacturing and cost feasibility.

Upstream IDs and statuses remain authoritative. Reference FS-M-001 input IDs IN-001 through IN-039, assumptions ASM-001 through ASM-012, and questions OQ-001 through OQ-014 by ID without redefining them. Local inputs use `FS9-IN-nnn`; local assumptions use `FS9-ASM-nnn`; local questions use `FS9-OQ-nnn`.

The table below intentionally includes only the verified upstream inputs specified for this study. Do not infer unlisted values or upgrade preliminary/assumed data. Verify source paths and revisions before using the inputs in a decision.

## 2. Section A - Verified upstream inputs

Authoritative baseline path: `kritva-m/FS-M-001-integrated-actuator-system/`.

| Upstream ID | Input | Value/status | Manufacturing/cost use and limitation |
|---|---|---|---|
| IN-009 | Nominal DC supply | 24 V; PRELIMINARY | Sourcing context for electrical components only |
| IN-012 | Gearbox efficiency | 85%; ASSUMED | Performance/cost context; not a procurement acceptance criterion |
| IN-024 | Motor margin | 20%; ASSUMED | Verify definition and application before using |
| IN-025 | Gearbox margin | 20%; ASSUMED | Verify definition and application before using |
| IN-026 | Duty cycle and continuous holding duration | UNKNOWN | Blocks unsupported life, maintenance, and operating-cost assumptions |
| IN-028 | Ambient operating temperature | UNKNOWN | May affect component ratings, enclosure, materials, and test requirements |
| IN-029 | Supply current limit | UNKNOWN | May affect supply/controller sourcing and cost |
| IN-030 | Service life | UNKNOWN | Blocks unconditional life-related cost and maintenance assumptions |
| IN-031 | Peak duration/repetition | UNKNOWN | Blocks assumptions that peak-rated components are adequate |
| IN-034 | Output-side encoder required | PRELIMINARY | Include in interface/BOM review; electrical and mechanical specifications require verification |
| IN-037 | Shaft material | EN19/42CrMo4 Q&T candidate; EN8 normalised reported SF about 0.86; PRELIMINARY | Design context only; not an approved material or manufacturing-route selection |

Do not convert the EN8 reported factor into a manufacturing acceptance limit or infer that either shaft material is approved. Confirm the source and assumptions with FS-M-005 before any material/cost decision.

## 3. Budget and requirement inputs

| Requirement | Supplied content | Use |
|---|---|---|
| SYS-REQ-100 | A0 budget INR 10,000-15,000; A1 budget INR 20,000-30,000 | Budget authority for cost comparison; clarify included cost scope |
| SYS-REQ-091 | Gearbox/bearing life versus duty | Track life-related component and qualification dependencies |
| SYS-REQ-092 | Post-loaded-cycle integrity: no unacceptable permanent deformation, loosening, bearing damage, or encoder misalignment | Track manufacturing, assembly, inspection, and validation dependencies |
| SYS-REQ-014 | Conditional shock-load requirement (scope open, upstream OQ-009) | Track shock-related material/process and qualification dependencies |

SYS-REQ-092 is a post-loaded-cycle integrity requirement, not the shock-load requirement. Use SYS-REQ-014 for shock loads. Verify detailed requirement records before defining any test method or acceptance limit.

For SYS-REQ-100, record whether the approved budget includes tax, shipping, duties, assembly labour, inspection, testing, rework, and one-time tooling/NRE. Until scope is confirmed, show the inclusions/exclusions and do not claim budget compliance.

## 4. Required upstream artifacts

Verify each artifact's exact repository-relative path, revision or commit, units, review status, and limitations. Do not infer existence or approval from this expected list.

| Study | Required evidence | Verification need |
|---|---|---|
| FS-M-003 | Candidate motor data and operating points | Discover exact filenames in repository; confirm candidate identity, ratings, and source provenance |
| FS-M-004 | `outputs/GEARBOX_CANDIDATE_MATRIX.csv` | Candidate identity, price/source if present, ratings, and interface constraints |
| FS-M-004 | `outputs/RATIO_OPTIMIZATION.csv` | Ratio decision context and underlying assumptions |
| FS-M-004 | `outputs/LOAD_RATING_CHECK.csv` | Rating constraints and unresolved conditions |
| FS-M-004 | `outputs/LIFE_RATING_ASSESSMENT.csv` | Life assumptions and limitations |
| FS-M-004 | `outputs/INTERFACE_COMPATIBILITY.csv` | Verified interfaces and unresolved compatibility |
| FS-M-005 | `outputs/SHAFT_LOAD_CASES.csv` | Loads and units relevant to shaft manufacturing |
| FS-M-005 | `outputs/SHAFT_STRENGTH_CHECK.csv` | Strength assessment and material dependencies |
| FS-M-005 | `outputs/IMPACT_CHECK.csv` | Impact assessment and unresolved shock dependencies |
| FS-M-005 | `outputs/DEFLECTION_CHECK.csv` | Deflection/alignment constraints |
| FS-M-005 | `outputs/INTERFACE_CHECK.csv` | Shaft, bearing-seat, and gearbox interfaces |
| FS-M-005 | `outputs/MATERIAL_COMPARISON.csv` | Material alternatives and evidence basis |
| FS-M-006 | `outputs/BEARING_CANDIDATE_MATRIX.csv` | Candidate identity, sourcing, and interface context |
| FS-M-006 | `outputs/BEARING_RATING_CHECK.csv` | Bearing rating constraints |
| FS-M-006 | `outputs/LIFE_ASSESSMENT.csv` | Life assumptions and limitations |
| FS-M-006 | `outputs/INTERFACE_DECISION.csv` | Shaft/bearing interface disposition |
| FS-M-006 | `outputs/SUPPORT_FEASIBILITY.csv` | Support arrangement and manufacturing implications |
| FS-M-007 | `outputs/INTERFACE_REGISTER.csv` | Housing, mounting, and mechanical interfaces |
| FS-M-007 | `outputs/MASS_ENVELOPE_STATUS.csv` | Mass/envelope constraints and unresolved values |
| FS-M-007 | `outputs/STRUCTURAL_CHECK.csv` | Housing/support strength and limitations |
| FS-M-008 | Electrical/thermal outputs and source register | Exact filenames must be verified; capture sourcing, thermal, current, wiring, and protection constraints |

If any artifact is missing, stale, incomplete, or unreviewed, record it as an evidence gap. Do not guess the missing content or substitute a similarly named file without documenting the decision.

## 5. Section B - Study-local inputs

These local records describe information to collect, verify, or derive for this study. Their initial status is UNKNOWN unless evidence is recorded.

| Local ID | Required input | Status | Source/action |
|---|---|---|---|
| FS9-IN-001 | Current component inventory and approved architecture baseline | UNKNOWN | Reconcile FS-M-003 through FS-M-008 |
| FS9-IN-002 | Exact part numbers, quantities, and interface details for candidate purchased components | UNKNOWN | Verify upstream candidate records and manufacturer datasheets |
| FS9-IN-003 | Supplier identity and dated unit-price evidence for each purchased BOM line | UNKNOWN | Supplier quotation or dated published listing; otherwise TBD |
| FS9-IN-004 | Supplier stock/availability and lead time | UNKNOWN | Dated supplier evidence; distinguish stock from estimated lead time |
| FS9-IN-005 | MOQ, quantity breaks, quote validity, and order constraints | UNKNOWN | Supplier quotation or explicit TBD |
| FS9-IN-006 | Shipping, duties, taxes, and delivery assumptions | UNKNOWN | Dated source and declared delivery location; do not assume inclusion |
| FS9-IN-007 | Housing and support geometry maturity, material, and critical interfaces | UNKNOWN | FS-M-007 artifacts and design-owner confirmation |
| FS9-IN-008 | Shaft geometry, material condition, machining/heat-treatment requirements | UNKNOWN | FS-M-005 and controlled material/process evidence |
| FS9-IN-009 | Bearing and shaft-seat fit, tolerance, coaxiality, and finish requirements | UNKNOWN | FS-M-005/006 approved interface evidence |
| FS9-IN-010 | Encoder mounting, alignment, and cable-interface constraints | UNKNOWN | FS-M-005/007/008 verified evidence |
| FS9-IN-011 | Process capability, tolerances, finishing, and inspection evidence for each custom part | UNKNOWN | Supplier capability documents or qualified process evidence |
| FS9-IN-012 | Assembly labour, inspection effort, rework, and test cost basis | UNKNOWN | Documented estimate method or supplier quotation |
| FS9-IN-013 | A0/A1 quantities and included/excluded cost categories | UNKNOWN | SYS-REQ-100 clarification and Project Lead decision |
| FS9-IN-014 | Tooling, fixture, setup, and non-recurring engineering cost | UNKNOWN | Supplier quotation or explicitly TBD |
| FS9-IN-015 | Scrap/yield/rework allowance and its basis | UNKNOWN | Verified historical/process evidence or TBD |
| FS9-IN-016 | Planned quantity scenarios and build-versus-buy constraints | UNKNOWN | Project Lead-approved planning scenarios |
| FS9-IN-017 | Material certificate, heat treatment, finish, and inspection requirements for shaft and other load-bearing parts | UNKNOWN | FS-M-005/006 and engineering-approved requirements |
| FS9-IN-018 | Thermal/process limits for printed or polymer parts near heat sources | UNKNOWN | FS-M-007/008 and sourced material/process data |
| FS9-IN-019 | Qualification and test activities required before acceptance | UNKNOWN | Relevant system requirements and approved test planning |
| FS9-IN-020 | Supplier qualification, traceability, and obsolescence constraints | UNKNOWN | Project Lead/sourcing decision and supplier evidence |

## 6. Cost evidence classification

Every cost value must be classified as one of:

- **QUOTED:** supplier quotation with date, validity, quantity, and scope.
- **PUBLISHED:** dated published price with source and stated conditions.
- **ESTIMATED:** calculation or estimate with method, assumptions, and source basis.
- **HISTORICAL:** past price retained for context, not treated as current.
- **TBD:** no adequate value available.

Each BOM line must record quantity, unit, currency, source date, price classification, source reference, logistics/tax treatment, and lead-time status. Do not treat TBD as zero. Separate recurring costs from tooling/NRE.

## 7. Change control and input acceptance

Changes to component candidates, interfaces, material, process, supplier quotation, quantity, or budget scope must identify affected BOM lines, calculations, risk entries, and downstream decisions.

New local inputs use the next available `FS9-IN-nnn` ID. Do not reuse an ID or change an upstream record from this study. Preserve source revisions and dated prices so that historical and current evidence remain distinguishable.

## 8. Initial readiness

The baseline includes budget targets but does not establish a complete priced BOM or supplier availability. Process selection, cost totals, lead times, and manufacturing readiness remain unverified until actual component data, geometry, quotations, and process evidence have been reviewed.

## 9. Repository starting evidence (as of 2026-10-24)

The repository already holds draft calculation and design documents that overlap this study. They are **starting points, not verified evidence**: each is a draft pending approval, none has been independently reviewed, and several figures were gathered by an AI reviewer session and not re-checked against vendor pages. Read them first, then reproduce or re-source what you rely on and register it in `references/SOURCE_REGISTER.csv`. They do not change the status of any upstream input.

| Source | What it gives | Limits |
|---|---|---|
| `docs/architecture/COMPONENTS_SOURCING_AND_COST.md` (draft) sections 2 and 3 | Component breakdown by phase; the A0 total of 22,000 INR line by line (the source of IN-020); scenarios S1 to S4 replacing the motor and gearbox lines with listed prices (26,245 to 32,885 INR for S1 to S3, 22,328 INR for S4) | Lines are mostly estimates; listings are dated 2026-10-13 and are not quotations; no gearbox price is known; no shipping, duty, GST or lead time |
| `mechanical/calculations/MOTOR_GEARBOX_SHORTLIST.md` section 2.2 | Dated motor listing prices (CubeMars store in USD, Robokits India in INR) | Not quotations; delivered cost unknown |

The BOM files cited by those documents, `mechanical/bom/MECHANICAL_BOM.csv` and `hardware/bom/ELECTRICAL_BOM.csv`, are not in the repository (both folders contain only placeholder files). Until they are restored or located, the tables in `COMPONENTS_SOURCING_AND_COST.md` are the only record of the estimate. Record that in the source register and do not treat the 22,000 INR total as a priced BOM. Cost classification remains as in section 6 of this register.
Child requirement documents also exist and are not yet reconciled with this study: `requirements/MECHANICAL_REQUIREMENTS.md` (MECH-REQ-nnn) and `requirements/ELECTRICAL_REQUIREMENTS.md` (ELEC-REQ-nnn). Check which IDs apply and cite them by ID.
