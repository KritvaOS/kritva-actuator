---
study_id: FS-M-009
title: Manufacturing and Cost Feasibility - Work Plan
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Project Lead
priority: P3
upstream: [FS-M-003, FS-M-004, FS-M-005, FS-M-006, FS-M-007, FS-M-008]
downstream: [FS-M-010]
specification: SPECIFICATION.md
inputs: inputs/INPUTS.md
assumptions_and_open_questions: ASSUMPTIONS_AND_OPEN_QUESTIONS.md
---

# FS-M-009 Work Plan

## 1. Objective

Produce a traceable manufacturing, sourcing, and cost-feasibility assessment for Kritva-M. Compare process routes and build-versus-buy options, create an evidence-backed BOM roll-up for A0/A1, compare it with SYS-REQ-100, and identify unresolved costs, supply-chain risks, tolerance/inspection needs, and validation dependencies.

This plan is governed by `SPECIFICATION.md`. AC-001 through AC-016 below must match the specification in ID and intent.

## 2. Roles

- **Owner - Mechanical Intern:** verify upstream artifacts, assess process routes, collect supplier evidence, maintain the BOM/cost model, and record risks.
- **Reviewer - Project Lead:** review cost scope, budget comparison, manufacturing conclusions, and unresolved decisions.
- **Upstream study owners:** confirm candidate data, interfaces, analysis results, and artifact revisions.
- **Downstream owner:** consume the manufacturing/cost evidence and outstanding risks in FS-M-010.

The owner shall not invent missing prices, part numbers, lead times, tolerances, or supplier capabilities. Missing evidence must be recorded as TBD or BLOCKED.

## 3. Work breakdown

| Task | Activity | Evidence / output | Exit condition |
|---|---|---|---|
| WP-01 | Verify baseline inputs and requirements | Input traceability table | IDs, values, units, statuses, and requirement wording checked |
| WP-02 | Verify upstream study artifacts | Artifact manifest | Exact path, revision, units, and review status recorded |
| WP-03 | Build component and part inventory | Preliminary BOM structure | Every line tied to an upstream candidate or explicit TBD |
| WP-04 | Compare manufacturing routes | Process comparison matrix | Geometry, material, tolerance, quantity, finish, and inspection considered |
| WP-05 | Assess sourcing and lead time | Supplier/availability matrix | Sources dated; unknown lead times remain TBD |
| WP-06 | Build A0/A1 cost roll-up | BOM calculation and budget comparison | Cost basis, inclusions, exclusions, and TBD exposure explicit |
| WP-07 | Assess build-versus-buy and quantity | Trade-off and sensitivity tables | Quantity assumptions documented; no speculative committed discounts |
| WP-08 | Assess tolerances and inspection | Critical-characteristic and inspection matrix | Verified dimensions used; unresolved dimensions identified |
| WP-09 | Assess assembly and test cost drivers | Assembly/test driver list | Cost basis or TBD recorded |
| WP-10 | Consolidate risks and handoff | Risk register and FS-M-010 handoff | Owners/actions assigned; unsupported claims removed |
| WP-11 | Review and close | Project Lead review record | Findings and dispositions recorded against evidence revision |

## 4. Required directory structure

Mandatory:

- `calculations/` - reproducible cost roll-ups, quantity sensitivity, and other quantitative assessments.
- `outputs/` - process comparison, BOM summary, sourcing/lead-time matrix, tolerance/inspection risks, and budget status.
- `references/SOURCE_REGISTER.csv` - dated source register.

Conditional:

- `cost_estimate/` - detailed cost model or quote comparison when needed.
- `component_research/` - sourced supplier/component candidate research when performed.

Not applicable by default:

- `CAD/` - NOT_APPLICABLE unless a specific manufacturing question requires a new model; geometry ownership remains upstream.
- `test_data/` - NOT_APPLICABLE for this desk study. Testing is a separately planned activity.

Document the rationale for any change in applicability.

## 5. Work sequence and gates

### Gate A - Baseline and interfaces

Verify `kritva-m/FS-M-001-integrated-actuator-system/` and the relevant FS-M-003 through FS-M-008 artifacts. Preserve upstream IDs and statuses. Record exact artifact paths, revisions, units, and review status.

Confirm that the component inventory represents the current documented architecture. Missing or conflicting motor, gearbox, shaft, bearing, encoder, controller, housing, or thermal-interface data must be logged before costing dependent items.

### Gate B - Process and sourcing feasibility

For each significant part, compare appropriate routes against actual geometry, material, tolerance, finish, quantity, load, thermal environment, inspection, and supplier capability. Consider 3D printing, CNC machining, turning, sheet metal, and casting only where applicable.

Identify candidate suppliers and record dated evidence. Separate verified availability from a listing, and a published price from a formal quotation. Keep unknown prices, lead times, MOQ, taxes, and shipping explicitly TBD.

### Gate C - BOM and budget

Create separate A0 and A1 cost roll-ups. Include purchased and manufactured parts, finishing, fasteners, wiring, assembly, inspection, test, logistics, and one-time costs where known and in scope. Make the budget inclusions/exclusions explicit.

Compare with SYS-REQ-100 only after defining cost scope and quantity assumptions. Do not treat missing cost as zero or claim PASS with material unpriced lines. Show cost subtotal, TBD exposure, one-time cost, budget gap, and main cost drivers.

### Gate D - Manufacturing and quality risks

Document critical tolerances, fits, datums, inspection methods, assembly sequence, serviceability, and rework access. Reconcile shaft, bearing, housing, encoder, and thermal interface risks with upstream studies.

Reference SYS-REQ-091 for gearbox/bearing life versus duty; SYS-REQ-092 for post-loaded-cycle integrity; and SYS-REQ-014 for shock loads. Do not interchange these requirement meanings.

### Gate E - Review and handoff

Complete mandatory outputs and source registration. Assign owners or resolution actions to material sourcing, cost, process, and qualification gaps. Submit the evidence revision and risk summary to the Project Lead and FS-M-010.

## 6. Acceptance criteria

Initial status is `NOT_STARTED` for every criterion. Allowed status values are `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `FAIL`, and `BLOCKED`. Update status only when evidence supports the transition.

| AC | Acceptance criterion | Evidence required | Initial status |
|---|---|---|---|
| AC-001 | All used upstream inputs and artifacts are traceable by ID, exact path, revision, units, and review status; upstream IDs and statuses are not redefined. | Input traceability table and artifact manifest | NOT_STARTED |
| AC-002 | Relevant FS-M-003 through FS-M-008 candidate data and interface constraints are verified or recorded as missing/unreviewed blockers. | Upstream artifact verification record | NOT_STARTED |
| AC-003 | Manufacturing-process options are compared against actual part function, geometry maturity, material, tolerances, quantity, finish, and inspection needs. | Process comparison matrix | NOT_STARTED |
| AC-004 | Significant custom parts have a documented provisional process/material route or an explicit unresolved decision, with supporting evidence and limitations. | Part/process matrix | NOT_STARTED |
| AC-005 | Sourcing candidates have traceable manufacturer/supplier, part identification where verified, source date, lead-time status, and availability limitations. | Supplier and lead-time matrix | NOT_STARTED |
| AC-006 | Every quoted, published, or estimated cost has a dated source or is explicitly TBD; no invented prices or zero-cost placeholders are used. | BOM source mapping and source register | NOT_STARTED |
| AC-007 | A BOM roll-up separates purchased components, custom parts, assembly, inspection, testing, logistics/taxes where known, and one-time costs. | A0/A1 cost roll-up | NOT_STARTED |
| AC-008 | A0 and A1 cost estimates are compared with SYS-REQ-100 using explicit scope, quantity, inclusions, exclusions, and TBD exposure. | Budget comparison and cost-gap summary | NOT_STARTED |
| AC-009 | Build-versus-buy options and quantity sensitivity are documented where evidence supports them; speculative volume discounts are not presented as committed costs. | Trade-off and quantity-sensitivity analysis | NOT_STARTED |
| AC-010 | Critical tolerances, fits, datums, inspection methods, and unresolved dimensional dependencies are documented or explicitly TBD. | Critical-characteristic/inspection matrix | NOT_STARTED |
| AC-011 | Assembly, rework, serviceability, and functional/acceptance test cost drivers are identified with a stated basis or TBD status. | Assembly/test cost-driver assessment | NOT_STARTED |
| AC-012 | SYS-REQ-091 life-versus-duty and SYS-REQ-092 post-loaded-cycle integrity are referenced correctly; SYS-REQ-014 remains the shock-load requirement. | Requirement traceability and risk register | NOT_STARTED |
| AC-013 | Material and manufacturing-route implications for shaft, bearings, housing, encoder alignment, and thermal interfaces are reconciled with upstream evidence without unsupported compliance claims. | Interface and manufacturing risk assessment | NOT_STARTED |
| AC-014 | Mandatory calculations, outputs, and `references/SOURCE_REGISTER.csv` are complete and reproducible; conditional directories and NOT_APPLICABLE deliverables are handled as specified. | Deliverable audit and reproducibility check | NOT_STARTED |
| AC-015 | Supplier, cost, lead-time, quality, and manufacturing risks are documented with owners or resolution actions and handed off to FS-M-010. | Risk register and handoff record | NOT_STARTED |
| AC-016 | Project Lead review is recorded against the evidence revision, budget limitations, manufacturing risks, and unresolved decisions; unsupported feasibility claims remain NOT_VERIFIED or BLOCKED. | Project Lead review record | NOT_STARTED |

## 7. Cost model controls

For each cost line, preserve quantity, unit, currency, source date, quote/listing/estimate classification, source reference, and included/excluded charges. Separate recurring unit cost from tooling/NRE and other one-time costs. If currency conversion is needed, record the dated exchange-rate source and calculation.

A subtotal containing TBD lines is not a complete cost estimate. Show the known subtotal and unpriced exposure separately. State whether labour, tax, shipping, duties, testing, rework, and tooling are included. Do not infer budget compliance from a component-only subtotal.

## 8. Review and change control

Record Project Lead findings, reviewer/date, source revision, and disposition. When a candidate, design interface, material, process, supplier quotation, or quantity assumption changes, identify affected BOM lines, calculations, risks, and downstream decisions.

Do not overwrite source evidence. Retain prior quotation dates and revisions so that a later reader can distinguish a current price from an expired or historical observation.

## 9. Completion checklist

- [ ] Upstream inputs and artifacts verified.
- [ ] Manufacturing process and material options documented.
- [ ] Supplier and lead-time evidence recorded.
- [ ] Every cost is dated and sourced or marked TBD.
- [ ] A0/A1 BOM roll-ups and SYS-REQ-100 comparison reproducible.
- [ ] Quantity and build-versus-buy assumptions explicit.
- [ ] Tolerances, inspection, assembly, and test cost drivers documented.
- [ ] SYS-REQ-091, SYS-REQ-092, and SYS-REQ-014 distinguished correctly.
- [ ] Mandatory deliverables and source register complete.
- [ ] Risks and open decisions handed off to FS-M-010.
- [ ] Project Lead review recorded; unsupported feasibility claims remain unresolved.
