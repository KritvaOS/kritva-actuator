---
study_id: FS-M-009
title: Manufacturing and Cost Feasibility - Assumptions and Open Questions
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

# FS-M-009 Assumptions and Open Questions

## 1. Purpose and ID rules

This file records local assumptions and unresolved questions for manufacturing process selection, sourcing, supplier lead time, BOM costing, assembly, inspection, and budget feasibility.

Upstream FS-M-001 input IDs IN-001 through IN-039, assumptions ASM-001 through ASM-012, and questions OQ-001 through OQ-014 remain owned by FS-M-001. Reference them by ID and verify their exact wording/status before use. Do not redefine or silently close upstream records.

Use local IDs `FS9-ASM-nnn`, `FS9-OQ-nnn`, and `FS9-IN-nnn`. An assumption is not an approved design decision. Unknown cost is not zero; an unverified supplier listing is not a quotation; a proposed manufacturing route is not proof of manufacturability.

## 2. Local assumptions register

| Local ID | Provisional assumption or method | Limitation | Resolution action |
|---|---|---|---|
| FS9-ASM-001 | Use the current verified upstream candidate set as the starting BOM basis | Candidate completeness and revision status must be checked | Verify FS-M-003 through FS-M-008 artifact paths and revisions |
| FS9-ASM-002 | Treat 3D printing as a possible prototype route for suitable parts | Material/process limits, creep, tolerance, and load capacity are part-specific | Compare against geometry and sourced material/process data |
| FS9-ASM-003 | Treat CNC machining and turning as candidate routes for precision interfaces | Cost and achievable tolerances depend on geometry, material, setup, quantity, and supplier capability | Obtain sourced process capability and cost evidence |
| FS9-ASM-004 | Treat sheet metal as a reference route for suitable covers/brackets | May be unsuitable for the actual load path or envelope | Verify part function and geometry before retaining the route |
| FS9-ASM-005 | Treat casting as a reference option rather than the default prototype route | Tooling, design maturity, quantity, and finishing may dominate economics | Evaluate only with a stated volume and supplier/tooling basis |
| FS9-ASM-006 | Separate recurring unit cost from tooling/NRE and setup cost | Combining them can obscure the cost per unit and budget scope | Report one-time and recurring costs separately |
| FS9-ASM-007 | Treat published online prices as indicative, not firm quotations | Stock, taxes, shipping, validity, and supplier terms may be unknown | Record source date and conditions; seek a quotation when required |
| FS9-ASM-008 | Treat all missing prices, lead times, MOQ, and logistics charges as TBD | A blank or TBD item cannot be treated as zero in a total | Show known subtotal and unpriced exposure |
| FS9-ASM-009 | Compare A0/A1 costs against SYS-REQ-100 only after defining cost inclusions | Budget scope may exclude labour, test, shipping, tax, or tooling | Obtain Project Lead clarification and document scope |
| FS9-ASM-010 | Use only quantity scenarios with a stated planning basis | Unverified volumes and volume discounts can create misleading cost projections | Record scenario source and sensitivity assumptions |
| FS9-ASM-011 | Treat manufacturing tolerances and inspection limits as TBD until supported by engineering evidence | Invented tolerances can conflict with shaft/bearing/encoder interfaces | Verify FS-M-005/006/007 and approved interface records |
| FS9-ASM-012 | Treat supplier lead time as unknown unless a dated source supports it | A listing or past order does not establish current availability | Capture date, quantity, supplier, and validity |
| FS9-ASM-013 | Treat assembly/test labour as a cost driver, not an automatic zero-cost activity | Time, equipment, qualification, and rework basis may be missing | Obtain a documented estimate or quote |
| FS9-ASM-014 | Treat shaft material/process alternatives as unapproved until FS-M-005 evidence is reviewed | IN-037 is PRELIMINARY and does not approve EN19/42CrMo4 or EN8 | Reconcile strength, heat treatment, machining, certification, and cost |
| FS9-ASM-015 | Treat SYS-REQ-091, SYS-REQ-092, and SYS-REQ-014 as distinct requirements | Life, post-loaded-cycle integrity, and shock loads are not interchangeable | Trace each to its proper evidence and validation plan |

## 3. Upstream assumptions and questions

The following upstream records must remain under their original ownership:

- ASM-001 through ASM-012 - upstream assumptions in FS-M-001.
- OQ-001 through OQ-014 - upstream open questions in FS-M-001.
- IN-012 - gearbox efficiency 85%, ASSUMED.
- IN-024 - motor margin 20%, ASSUMED.
- IN-025 - gearbox margin 20%, ASSUMED.
- IN-026 - duty cycle and continuous holding duration UNKNOWN.
- IN-028 - ambient operating temperature UNKNOWN.
- IN-029 - supply current limit UNKNOWN.
- IN-030 - service life UNKNOWN.
- IN-031 - peak duration/repetition UNKNOWN.
- IN-034 - output-side encoder required, PRELIMINARY.
- IN-037 - shaft material candidates and reported EN8 strength-factor context, PRELIMINARY.

These records may influence supplier selection, cost, process, qualification, and maintenance analysis. They do not by themselves establish a price, a manufacturing route, an approved component, or a production acceptance limit.

## 4. Open questions register

| Local ID | Question | Impact if unresolved | Owner / evidence to close |
|---|---|---|---|
| FS9-OQ-001 | Which FS-M-003 motor candidate records and exact filenames are authoritative and reviewed? | Motor BOM line, supplier price, and lead time remain unverified | FS-M-003 owner; repository artifact manifest |
| FS9-OQ-002 | Which gearbox candidate and ratio are current, and what supplier/source evidence supports the candidate? | Gearbox price, availability, interfaces, and cost comparison remain provisional | FS-M-004 owner; verified candidate matrix and dated supplier source |
| FS9-OQ-003 | What shaft geometry, material condition, heat treatment, and inspection requirements are supported by FS-M-005? | Shaft process route, quote scope, and acceptance requirements remain open | FS-M-005 owner; reviewed calculations and interface/material outputs |
| FS9-OQ-004 | What bearing candidate and shaft/bearing interface decision are approved by FS-M-006? | Bearing purchase and support-machining decisions remain blocked | FS-M-006 owner; `outputs/INTERFACE_DECISION.csv` and relevant reviewed outputs |
| FS9-OQ-005 | Which housing geometry, material, interfaces, and thermal paths from FS-M-007 are mature enough to quote? | Housing process, cost, and supplier feasibility remain uncertain | FS-M-007 owner; verified interface and structural outputs |
| FS9-OQ-006 | Which electrical/thermal candidates and constraints from FS-M-008 affect the BOM and supplier choice? | Controller, wiring, thermal interface, and protection-related BOM lines may be incomplete | FS-M-008 owner; verified output paths and source register |
| FS9-OQ-007 | What is included in the SYS-REQ-100 A0/A1 budget: components only, or also labour, inspection, test, tax, shipping, duties, and tooling? | Budget-compliance result cannot be stated consistently | Project Lead; explicit budget-scope decision |
| FS9-OQ-008 | What are the planned A0/A1 build quantities and intended quantity scenarios? | Quantity breaks, setup allocation, and unit-cost comparison remain speculative | Project Lead; approved planning assumptions |
| FS9-OQ-009 | Which supplier quotations are required, and what quote validity/quantity/terms apply? | Published prices may not support a purchase-ready estimate | Mechanical Intern; dated supplier quotations |
| FS9-OQ-010 | What are current availability, MOQ, lead time, shipping, and tax/duty conditions for each key component? | Delivery schedule and landed cost remain unverified | Mechanical Intern/sourcing owner; dated supplier evidence |
| FS9-OQ-011 | Which custom parts need CNC, turning, printing, sheet metal, or another process, based on verified geometry and load/thermal constraints? | Process comparison cannot progress beyond preliminary options | Mechanical Intern with upstream owners; part/process matrix |
| FS9-OQ-012 | What critical tolerances, fits, datums, surface finish, and inspection methods are required at shaft, bearing, gearbox, housing, and encoder interfaces? | Supplier quotes may be incomparable; assembly and alignment risk remains | FS-M-005/006/007 owners; reviewed interface evidence |
| FS9-OQ-013 | What material certificates, heat-treatment records, surface finishing, and inspection reports are required for load-bearing components? | Quality, traceability, and process cost remain incomplete | Project Lead and mechanical owner; controlled engineering requirements |
| FS9-OQ-014 | What assembly labour, inspection, functional test, thermal test, and rework costs must be included in A0/A1? | BOM totals may understate the actual build cost | Project Lead; defined estimate scope and sourced/estimated time basis |
| FS9-OQ-015 | What supplier qualification and incoming-inspection controls are required for purchased motor, gearbox, bearing, and encoder parts? | Supplier acceptance and quality risk remain unresolved | Project Lead; supplier-quality decision and applicable requirements |
| FS9-OQ-016 | Which manufacturing-route decisions depend on service life and duty-cycle requirements? | Process/material selection and maintenance cost may be premature | Project Lead; resolve IN-026/IN-030 and SYS-REQ-091 dependencies |
| FS9-OQ-017 | What qualification evidence will demonstrate SYS-REQ-092 post-loaded-cycle integrity? | Inspection and validation cost cannot be finalized; compliance cannot be claimed | Project Lead and test owner; separately approved test plan |
| FS9-OQ-018 | What shock-load evidence is required under SYS-REQ-014, and which manufacturing/material choices depend on it? | Shock-related material/process decisions remain open | Relevant engineering owner; reviewed shock-load analysis and validation plan |
| FS9-OQ-019 | Which material/process constraints apply near motor/controller heat sources? | Printed-part and housing routes may be thermally unsuitable | FS-M-007/008 owners; sourced material and thermal evidence |
| FS9-OQ-020 | What are the largest budget risks and what cost ceilings or trade-offs can the Project Lead authorize? | Cost optimization priorities and escalation thresholds remain undefined | Project Lead; recorded trade-off and approval decision |

## 5. Cost and sourcing decision rules

1. Every cost must have a dated source or be marked TBD. Do not invent prices, supplier names, part numbers, lead times, MOQ, or discounts.
2. Distinguish quoted, published, estimated, historical, and TBD costs. Record currency, quantity, source date, quote validity, and conditions.
3. Keep recurring unit cost separate from tooling/NRE, setup, and other one-time costs.
4. Do not treat an unpriced BOM line as zero. Report known subtotal and unpriced exposure separately.
5. Do not compare A0/A1 to SYS-REQ-100 until budget scope and quantity assumptions are explicit.
6. Do not use a supplier listing as proof of stock or a formal quotation.
7. Do not approve a manufacturing process from cost alone; verify geometry, material, load, tolerance, finish, thermal constraints, and inspection needs.
8. Do not approve a shaft or bearing interface by silently changing upstream dimensions or material decisions.
9. Reference SYS-REQ-091 for gearbox/bearing life versus duty, SYS-REQ-092 for post-loaded-cycle integrity, and SYS-REQ-014 for shock loads.
10. Preserve source revisions and dated prices so historical values cannot be mistaken for current quotations.

## 6. Must-not-conclude list

Until sufficient evidence and Project Lead review are available, this study must not conclude that:

- The actuator is manufacturable without unresolved geometry, material, tolerance, and process constraints.
- A0 or A1 is within budget when material BOM lines or cost categories remain unpriced or excluded without approval.
- A supplier has stock, a guaranteed lead time, or an enforceable price without appropriate evidence.
- A manufacturing process is selected or qualified merely because it is a common or low-cost option.
- The shaft material, bearing, gearbox, housing, encoder, or other component is approved for production.
- SYS-REQ-091 gearbox/bearing life has been demonstrated.
- SYS-REQ-092 post-loaded-cycle integrity has been demonstrated.
- SYS-REQ-014 shock-load compliance has been demonstrated.
- Assembly, inspection, thermal validation, loaded-cycle validation, or production qualification costs are zero when they have not been estimated.
- A preliminary cost model is a firm quotation, production cost commitment, or purchasing authorization.

## 7. Review and closure

For every open question, record the answer or unresolved disposition, evidence source, owner, date, and affected BOM lines/process decisions. Close questions only when the required evidence or an explicit authorized decision exists.

Project Lead review shall record the evidence revision, cost scope, budget comparison limitations, manufacturing risks, and unresolved decisions. Carry open items and their impact into FS-M-010. The study remains PROPOSED until its status is changed through the project's controlled review process.
