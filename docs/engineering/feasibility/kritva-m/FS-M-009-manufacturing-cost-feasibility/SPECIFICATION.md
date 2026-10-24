---
study_id: FS-M-009
title: Manufacturing and Cost Feasibility
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

# FS-M-009 Manufacturing and Cost Feasibility

## 1. Purpose

Assess manufacturing feasibility, sourcing, supplier lead times, assembly, inspection, and estimated build cost for the Kritva-M actuator. Produce an evidence-backed comparison of manufacturing routes and a traceable BOM cost roll-up against SYS-REQ-100 budget targets.

This is a feasibility study, not a production release, supplier commitment, purchase authorization, or declaration that a design is manufacturable or within budget.

## 2. Scope

Evaluate manufacturing and sourcing options for the current documented actuator architecture, including:

- Manufacturing process options for housing, shaft, bearing support, brackets, flanges, and other relevant mechanical parts.
- Commercial motor, gearbox, bearings, encoder, controller, and interconnect candidates from FS-M-003 through FS-M-008.
- Supplier availability, geographic sourcing, lead time, minimum order quantity, quotation validity, shipping, taxes, and import considerations where evidence is available.
- BOM cost roll-up for A0 and A1 against SYS-REQ-100.
- Build-versus-buy choices and quantity sensitivity.
- Machining, 3D-printing, turning, sheet-metal, and casting routes as applicable; casting is a reference option unless volume, tooling, and design maturity justify it.
- Tolerances, fits, datum strategy, inspection, finishing, assembly, rework, and test cost drivers.
- Procurement risks, long-lead items, alternative sourcing, supplier qualification, and manufacturing-readiness gaps.
- Handoff of cost, sourcing, manufacturing, and unresolved design constraints to FS-M-010.

All costs must be traceable to a dated source or explicitly marked TBD. Engineering estimates must be identified as estimates and must not be presented as supplier quotations.

## 3. Out of scope

This study does not authorize:

- Production release, tooling orders, purchases, or supplier commitments.
- A claim of manufacturability without sufficient geometry, material, tolerance, and process evidence.
- Substitution of unverified motor, gearbox, shaft, bearing, encoder, or controller parts.
- Changing upstream design inputs, assumptions, or decisions.
- Claiming life, shock, thermal, structural, or safety compliance from manufacturing analysis alone.
- Treating a reference process or supplier listing as proof of production capability.
- Inventing prices, supplier lead times, part numbers, MOQ, or test costs.

## 4. Authoritative inputs and traceability

The upstream baseline is `kritva-m/FS-M-001-integrated-actuator-system/`. Preserve upstream IDs and statuses. Reference ASM-001 through ASM-012 and OQ-001 through OQ-014 by their original IDs; do not redefine or silently close them.

Required upstream studies:

- FS-M-003 - motor candidate data and operating points.
- FS-M-004 - gearbox candidates, ratio optimization, ratings, interfaces, and life assessment.
- FS-M-005 - output shaft geometry, strength, impact, deflection, material comparison, and interface checks.
- FS-M-006 - bearing candidates, rating, life, impact, interface, and support feasibility.
- FS-M-007 - mechanical interfaces, mass/envelope status, structural checks, housing, and integration.
- FS-M-008 - electrical and thermal feasibility, candidate data, interconnect constraints, and protection/thermal limitations.

Verify the exact repository paths, revisions, units, review status, and evidence of consumed outputs before relying on them. A listed filename does not establish that the artifact exists or is approved.

### Verified upstream inputs for this study

| Upstream ID | Input | Value/status | Manufacturing and cost relevance |
|---|---|---|---|
| IN-009 | Nominal DC supply | 24 V; PRELIMINARY | Supply and controller sourcing context only |
| IN-012 | Gearbox efficiency | 85%; ASSUMED | Performance/cost trade-off context; not a procurement specification |
| IN-024 | Motor margin | 20%; ASSUMED | Verify definition before using in candidate acceptance |
| IN-025 | Gearbox margin | 20%; ASSUMED | Verify definition before using in candidate acceptance |
| IN-026 | Duty cycle and continuous holding duration | UNKNOWN | Blocks life/cost assumptions dependent on operating duty |
| IN-028 | Ambient operating temperature | UNKNOWN | May affect component ratings, enclosure, and test needs |
| IN-029 | Supply current limit | UNKNOWN | Affects supply/controller sizing and sourcing |
| IN-030 | Service life | UNKNOWN | Blocks unconditional life-related cost and maintenance assumptions |
| IN-031 | Peak duration/repetition | UNKNOWN | Blocks assumptions about peak-rated component suitability |
| IN-034 | Output-side encoder required | PRELIMINARY | Include in interface/BOM review; specifications remain to be verified |
| IN-037 | Shaft material | EN19/42CrMo4 Q&T candidate; EN8 normalised reported SF about 0.86; PRELIMINARY | Design constraint/reference only; not an approved material selection |

Budget requirement:

- **SYS-REQ-100:** A0 budget INR 10,000-15,000; A1 budget INR 20,000-30,000.

Use the exact requirement record as the budget authority. Confirm whether budget scope includes taxes, shipping, labour, test equipment, rework, and non-recurring costs before making a budget-compliance statement.

Requirement references:

- **SYS-REQ-091:** gearbox/bearing life versus duty.
- **SYS-REQ-092:** post-loaded-cycle integrity: no unacceptable permanent deformation, loosening, bearing damage, or encoder misalignment.
- **SYS-REQ-014:** conditional shock-load requirement (applies only if impacts are in scope; scope open, upstream OQ-009).

SYS-REQ-092 is not the shock-load requirement. Do not conflate post-loaded-cycle integrity with shock-load qualification.

## 5. Manufacturing-process assessment

Assess process options against actual part geometry, material, required tolerances, load path, thermal environment, quantity, finish, inspection, and supplier capability.

Potential routes include:

- 3D printing: prototype housings, fixtures, and non-critical geometry where material/process properties and temperature limits are appropriate.
- CNC machining: housings, bearing supports, precision interfaces, and prototypes requiring controlled geometry.
- Turning: shafts, spacers, cylindrical interfaces, and bearing-seat features.
- Sheet metal: covers, brackets, guards, and other suitable low-load components.
- Casting: reference option for later volume production only when geometry, tooling economics, material, finishing, and qualification justify it.

These are candidate process routes, not approved selections. Do not assign a process solely from nominal cost or assume printed parts meet structural, thermal, tolerance, or life requirements.

For each significant part, record geometry maturity, material, process, critical dimensions, tolerances, datum scheme, finish, inspection method, supplier capability evidence, quantity, and outstanding design decisions.

## 6. Sourcing and supplier assessment

For each candidate component or process, capture:

- Manufacturer/supplier and exact part number where verified.
- Source URL or document, access/quotation date, revision, and validity period.
- Unit price, currency, quantity break, MOQ, tooling/NRE, and quotation conditions.
- Lead time, stock status, order constraints, shipping, duties, taxes, and delivery location where documented.
- Datasheet/rating evidence and interface compatibility.
- Alternative sources, obsolescence risks, and supplier qualification status.
- Evidence status: sourced quotation, published price, historical estimate, engineering estimate, or TBD.

Do not treat an online listing as an enforceable quotation or confirmed stock. Do not infer an Indian supplier's delivery time, tax treatment, or local availability without evidence.

## 7. BOM cost roll-up and budget assessment

Build separate A0 and A1 BOM views based on the actual candidate architecture and evidence from FS-M-003 through FS-M-008.

For each BOM line, record quantity per actuator, source, unit cost, currency, cost date, quote/listing status, shipping/tax treatment, lead time, and confidence. Separate:

- Purchased components.
- Custom manufactured parts.
- Finishing and secondary operations.
- Fasteners, inserts, wiring, connectors, and consumables.
- Assembly labour and inspection.
- Functional and acceptance testing.
- Expected scrap/rework allowance, only where a justified basis exists.
- Tooling/NRE and one-time setup, shown separately from recurring unit cost.
- Shipping, duties, and taxes where applicable.

Report known subtotal, TBD cost exposure, one-time costs, and the basis of any quantity assumptions. Never treat missing costs as zero.

Compare the resulting estimate with SYS-REQ-100 only after budget scope and cost inclusions are explicit. A result is not PASS if significant BOM lines remain unpriced or excluded without approval. Show the gap to each target and identify the largest cost drivers.

## 8. Quantity sensitivity and build-versus-buy

Evaluate practical quantity scenarios only when there is a stated planning basis. Separate prototype quantities from repeatable low-volume builds and potential future production volumes.

Compare build-versus-buy options for components and subassemblies using evidence for purchase cost, in-house process capability, equipment, labour, inspection, yield, lead time, tooling, repeatability, and supplier risk.

For CNC versus printing, turning versus bought shaft, custom versus commercial bearing support, and purchased versus custom actuator subassemblies, document trade-offs without declaring a winner where geometry, volume, or evidence is missing.

Do not present speculative volume discounts or amortized tooling as a committed cost. Clearly state the quantity and amortization assumptions.

## 9. Tolerance, inspection, assembly, and test cost

Identify manufacturing and assembly cost drivers, including:

- Bearing-seat diameter, fit, coaxiality, alignment, and surface finish.
- Shaft material, heat treatment, runout, critical dimensions, and inspection.
- Gearbox/motor mounting, flange interfaces, fastener access, and alignment.
- Encoder mounting and alignment with the output shaft.
- Housing interfaces, printed inserts, threads, fastener retention, and finishing.
- Cable routing, connector access, strain relief, and assembly sequence.
- Inspection tools, gauges, metrology, and supplier inspection reports.
- Assembly time, rework access, serviceability, and replaceable subassemblies.
- Functional test, current-limited electrical test, thermal test, and loaded-cycle test cost drivers.

Use verified dimensions and tolerances from the upstream studies. Where the design is preliminary or a dimension is absent, mark it TBD and identify the design owner. Do not create unsupported tolerances or inspection acceptance limits.

## 10. Life, safety, and qualification considerations

Use SYS-REQ-091 to track gearbox/bearing life versus duty. IN-026 and IN-030 remain UNKNOWN and must not be replaced with an assumed service life or duty profile.

Use SYS-REQ-092 for post-loaded-cycle integrity: no unacceptable permanent deformation, loosening, bearing damage, or encoder misalignment. Use SYS-REQ-014 for shock-load requirements. Manufacturing process, material, fits, fasteners, and inspection plans may influence these outcomes, but this study alone does not prove them.

Coordinate FS-M-005 shaft and FS-M-006 bearing findings. Do not claim a shaft, bearing, housing, or fastener is safe or life-qualified unless the relevant analysis and required review support the claim.

## 11. Evidence and source register

Mandatory file: `references/SOURCE_REGISTER.csv`.

Register every external price, supplier capability, lead time, material property, process tolerance, and other numerical claim. Capture source, date, currency/units, revision, relevant page/table, quantity, quote validity, and limitations.

Use TBD when no reliable value is available. Distinguish quotation, published list price, historical observation, estimate, and unknown. Keep a traceable link between each BOM line and its source record.

## 12. Deliverables and directory structure

### Mandatory

- `calculations/` - reproducible cost roll-ups, quantity sensitivity, and other quantitative assessments.
- `outputs/` - BOM summary, manufacturing process comparison, sourcing/lead-time matrix, tolerance/inspection risks, and budget status.
- `references/SOURCE_REGISTER.csv` - dated, traceable source register.

### Conditional

- `cost_estimate/` - detailed cost model, quote comparison, or quantity-sensitive model when needed.
- `component_research/` - sourced supplier/component candidate research when performed.

### Not applicable by default

- `CAD/` - NOT_APPLICABLE unless a specific manufacturing feasibility question requires a new model; authoritative geometry remains with the relevant upstream study.
- `test_data/` - NOT_APPLICABLE for this initial desk study. Manufacturing validation and loaded-cycle/electrical/thermal tests require separately planned and approved activities.

Record a rationale if any conditional directory is created or if applicability changes.

## 13. Acceptance criteria

Every criterion must have a traceable evidence pointer and one status: PASS, FAIL, BLOCKED, NOT_VERIFIED, or NOT_APPLICABLE. Do not mark a criterion PASS because a template exists or because missing cost is treated as zero.

- **AC-001:** All used upstream inputs and artifacts are traceable by ID, exact path, revision, units, and review status; upstream IDs and statuses are not redefined.
- **AC-002:** Relevant FS-M-003 through FS-M-008 candidate data and interface constraints are verified or recorded as missing/unreviewed blockers.
- **AC-003:** Manufacturing-process options are compared against actual part function, geometry maturity, material, tolerances, quantity, finish, and inspection needs.
- **AC-004:** Significant custom parts have a documented provisional process/material route or an explicit unresolved decision, with supporting evidence and limitations.
- **AC-005:** Sourcing candidates have traceable manufacturer/supplier, part identification where verified, source date, lead-time status, and availability limitations.
- **AC-006:** Every quoted, published, or estimated cost has a dated source or is explicitly TBD; no invented prices or zero-cost placeholders are used.
- **AC-007:** A BOM roll-up separates purchased components, custom parts, assembly, inspection, testing, logistics/taxes where known, and one-time costs.
- **AC-008:** A0 and A1 cost estimates are compared with SYS-REQ-100 using explicit scope, quantity, inclusions, exclusions, and TBD exposure.
- **AC-009:** Build-versus-buy options and quantity sensitivity are documented where evidence supports them; speculative volume discounts are not presented as committed costs.
- **AC-010:** Critical tolerances, fits, datums, inspection methods, and unresolved dimensional dependencies are documented or explicitly TBD.
- **AC-011:** Assembly, rework, serviceability, and functional/acceptance test cost drivers are identified with a stated basis or TBD status.
- **AC-012:** SYS-REQ-091 life-versus-duty and SYS-REQ-092 post-loaded-cycle integrity are referenced correctly; SYS-REQ-014 remains the shock-load requirement.
- **AC-013:** Material and manufacturing-route implications for shaft, bearings, housing, encoder alignment, and thermal interfaces are reconciled with upstream evidence without unsupported compliance claims.
- **AC-014:** Mandatory calculations, outputs, and `references/SOURCE_REGISTER.csv` are complete and reproducible; conditional directories and NOT_APPLICABLE deliverables are handled as specified.
- **AC-015:** Supplier, cost, lead-time, quality, and manufacturing risks are documented with owners or resolution actions and handed off to FS-M-010.
- **AC-016:** Project Lead review is recorded against the evidence revision, budget limitations, manufacturing risks, and unresolved decisions; unsupported feasibility claims remain NOT_VERIFIED or BLOCKED.

## 14. Review and approval

The Mechanical Intern prepares the study. The Project Lead reviews the evidence, cost basis, manufacturing decisions, and unresolved risks.

Record reviewer, date, artifact revision, findings, and disposition. Review does not substitute for supplier qualification, engineering signoff, or required validation testing. Any unresolved high-impact cost or manufacturing assumption must remain visible in the final status.

## 15. Risks and limitations

Key risks include incomplete candidate data, changing mechanical interfaces, missing quotes, unverified availability, uncertain duty and life, unresolved shaft/bearing interfaces, preliminary housing geometry, unknown material/process properties, and unpriced assembly/test activities.

A preliminary estimate can support trade-offs but must not be represented as a firm quotation or production cost.

## 16. Safety and test boundary

This is a manufacturing and cost desk study; it does not authorize fabrication, assembly, or powered testing. Any later test activity must have an approved procedure, acceptance criteria, suitable instrumentation, current/voltage limits where relevant, and required safety controls.

Do not treat manufacturing feasibility as proof of SYS-REQ-014 shock-load compliance, SYS-REQ-091 life compliance, or SYS-REQ-092 post-loaded-cycle integrity. These require the applicable engineering evidence and validation.

## 17. Completion checklist

- [ ] Upstream artifacts and input statuses verified.
- [ ] Process/material options documented against actual design constraints.
- [ ] Sourcing and lead-time evidence recorded.
- [ ] All prices dated and sourced or marked TBD.
- [ ] A0/A1 BOM roll-ups and SYS-REQ-100 comparisons reproducible.
- [ ] Quantity and build-versus-buy assumptions explicit.
- [ ] Tolerances, inspection, assembly, and test cost drivers documented.
- [ ] SYS-REQ-091, SYS-REQ-092, and SYS-REQ-014 distinguished correctly.
- [ ] Mandatory deliverables and source register complete.
- [ ] Risks and unresolved decisions handed off to FS-M-010.
- [ ] Project Lead review recorded; no unsupported feasibility claim remains.
