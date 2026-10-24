---
study_id: FS-M-007
title: Housing and Mechanical Integration - Assumptions and Open Questions
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Project Lead; Independent Reviewer TBD for safety-critical structural and hard-stop checks
upstream:
- FS-M-001
- FS-M-003
- FS-M-004
- FS-M-005
- FS-M-006
---

# FS-M-007 Assumptions and Open Questions

## 1. Purpose and Rules

Track uncertainties affecting the Kritva-M housing, mechanical interfaces, load path, hard stops, encoder alignment, assembly, serviceability, manufacturing and CAD concept.

- Use `FS7-ASM-nnn` for local assumptions and `FS7-OQ-nnn` for open questions.
- Preserve upstream input IDs, values and statuses.
- Reference FS-M-001 ASM-001..ASM-012 and OQ-001..OQ-014 by ID; do not redefine them.
- Use exact upstream output filenames and verify revisions before use.
- Do not invent dimensions, mass limits, prices, part numbers or supplier availability.
- An unresolved safety-critical question cannot be closed by author judgment alone.
- Record each closure with evidence, affected CAD/calculations, reviewer and commit.

## 2. Upstream References

### FS-M-001

Authoritative path: `kritva-m/FS-M-001-integrated-actuator-system/ASSUMPTIONS_AND_OPEN_QUESTIONS.md`.

Reference the original ASM-001..ASM-012 and OQ-001..OQ-014. Relevant input IDs include IN-009, IN-014, IN-015, IN-016, IN-018, IN-019, IN-023, IN-028, IN-033, IN-034 and IN-036.

OQ-012 is relevant to the provenance of IN-019's preliminary impact torque. SYS-REQ-014 is the shock-load requirement. SYS-REQ-092 is the post-loaded-cycle-test integrity requirement, not a shock-load requirement.

Mass and envelope budgets remain unresolved under SYS-REQ-039 and the applicable upstream open-question mapping. Do not use IN-039 for mass or envelope; it concerns ratio/motor-speed estimation.

### FS-M-003

Use the actual motor candidate data and operating points. Verify mounting dimensions, mass, thermal constraints, connectors and exact candidate identity before using them to finalize CAD.

### FS-M-004

Verify:

- `outputs/GEARBOX_CANDIDATE_MATRIX.csv`
- `outputs/RATIO_OPTIMIZATION.csv`
- `outputs/LOAD_RATING_CHECK.csv`
- `outputs/INTERFACE_COMPATIBILITY.csv`
- `outputs/LIFE_RATING_ASSESSMENT.csv`

Use the exact candidate's drawings and source revisions.

### FS-M-005

Verify:

- `outputs/SHAFT_LOAD_CASES.csv`
- `outputs/SHAFT_STRENGTH_CHECK.csv`
- `outputs/IMPACT_CHECK.csv`
- `outputs/DEFLECTION_CHECK.csv`
- `outputs/INTERFACE_CHECK.csv`
- `outputs/MATERIAL_COMPARISON.csv`

Coordinate shaft geometry, deflection, encoder position and hard-stop constraints.

### FS-M-006

Verify:

- `outputs/BEARING_LOAD_CASES.csv`
- `outputs/BEARING_CANDIDATE_MATRIX.csv`
- `outputs/BEARING_RATING_CHECK.csv`
- `outputs/LIFE_ASSESSMENT.csv`
- `outputs/IMPACT_BEARING_CHECK.csv`
- `outputs/INTERFACE_DECISION.csv`
- `outputs/SUPPORT_FEASIBILITY.csv`

The FS-M-006 `outputs/INTERFACE_DECISION.csv` is the handoff for the IN-015/IN-016 mismatch. Do not silently change either upstream input.

## 3. Study-Local Assumptions

These assumptions are provisional and must not be treated as verified design facts.

| ID | Assumption | Rationale / limitation | Closure evidence |
|---|---|---|---|
| FS7-ASM-001 | CAD begins as concept geometry | Exact candidate interfaces and budgets may be incomplete | Verified drawings and reviewed interface model |
| FS7-ASM-002 | Arm loads follow the independent shaft -> bearing pair -> housing -> mounting interface path | SYS-REQ-032 | Verified load-path and reaction assessment |
| FS7-ASM-003 | Gearbox torque reaction is separate from the arm-load path | Prevents unintended loading of gearbox/motor bearings | Interface and structural review |
| FS7-ASM-004 | Dedicated bearings are located in the joint housing | SYS-REQ-031 | FS-M-006 support design and interface review |
| FS7-ASM-005 | Housing material/process selection remains open | Aluminium, steel, printed and hybrid options require evidence | Comparative process and structural assessment |
| FS7-ASM-006 | Load-bearing bearing seats and motor/gearbox mounts require justified material/process | SYS-REQ-038 | Hand calculations and process/material evidence |
| FS7-ASM-007 | Hard-stop travel is bounded by the preliminary IN-033 range | Final range and clearances require approval | Approved joint range and reviewed stop geometry |
| FS7-ASM-008 | Single-contact hard-stop load case is used for initial concept screening | IN-036 is ASSUMED | Validated load-sharing/contact assessment |
| FS7-ASM-009 | IN-019 is a preliminary impact input only | Provenance unresolved under OQ-012 | Reconciled impact analysis and review |
| FS7-ASM-010 | Housing stiffness is first screened using hand estimates | FEA only if justified by unresolved structural questions | Calculation review; conditional FEA if needed |
| FS7-ASM-011 | Motor, gearbox, bearings and encoder should be independently replaceable where practical | SYS-REQ-036 | CAD assembly/serviceability review |
| FS7-ASM-012 | Mass/envelope and cost compliance cannot be determined until budgets and sourced component data exist | SYS-REQ-039 and SYS-REQ-100 | Approved arm-layout budgets and traceable cost basis |

## 4. Open Questions

| ID | Question | Why it matters | Closure evidence / owner |
|---|---|---|---|
| FS7-OQ-001 | Which motor candidate and mounting drawing are approved for concept integration? | Motor geometry, mass, heat and access affect the housing | FS-M-003 candidate evidence; Mechanical Intern |
| FS7-OQ-002 | Which gearbox candidate, ratio and interface are being used for the current CAD revision? | Determines pilots, fasteners, shaft interface and torque reaction | FS-M-004 candidate/ratio/interface outputs; Mechanical Intern |
| FS7-OQ-003 | Which FS-M-005 shaft geometry and FS-M-006 bearing arrangement are authoritative? | Housing support locations and alignment depend on both | Verified output revisions and coordinated interface model |
| FS7-OQ-004 | What is the recorded Project Lead disposition for the IN-015/IN-016 mismatch? | Shaft and bearing-seat dimensions must be consistent | FS-M-006 `outputs/INTERFACE_DECISION.csv`; Project Lead |
| FS7-OQ-005 | What approved arm/joint mounting datum and interface dimensions apply? | Required for mounting compatibility and reusable interface design | Arm layout/drawing and SYS-REQ-037 interpretation |
| FS7-OQ-006 | What are the approved actuator mass and envelope budgets? | SYS-REQ-039 remains TBD; no compliance claim is possible without limits | Approved humanoid arm layout and mass allocation; Project Lead |
| FS7-OQ-007 | Which housing material and manufacturing process are appropriate? | Stiffness, strength, creep, tolerance and cost depend on process | Material/process comparison and calculations; Mechanical Intern |
| FS7-OQ-008 | Can the bearing seats and mounting features retain alignment under rated loads? | Housing deformation affects bearing life and encoder alignment | Hand stiffness/deformation estimates and upstream load cases |
| FS7-OQ-009 | Are any load-bearing printed features justified? | Printed parts may have anisotropy, creep, insert pull-out and tolerance limits | Feature-specific material/process evidence and calculation |
| FS7-OQ-010 | What hard-stop geometry, contact location and final travel limits are required? | IN-033 is PRELIMINARY; clearance and stop loading depend on geometry | Approved range, stop model and load-path review |
| FS7-OQ-011 | What are the validated hard-stop/impact loads and uncertainty? | IN-018/IN-019 are preliminary; IN-019 provenance is unresolved | FS-M-005/006 impact evidence and Project Lead review |
| FS7-OQ-012 | Does the housing and mounting interface withstand the governing peak/stop loads? | Structural adequacy cannot be inferred from CAD fit | Traceable hand calculations and independent safety-critical review |
| FS7-OQ-013 | What encoder alignment limits and mounting tolerances apply? | SYS-REQ-034 includes rated-load alignment and shaft deflection | Canonical limits, encoder documentation and FS-M-005 deflection output |
| FS7-OQ-014 | How will motor/encoder cables be routed and protected? | Moving parts, hard stops and service access can create interference or pinch risks | Cable/connector data and CAD routing review; FS-M-008 coordination |
| FS7-OQ-015 | Can motor, gearbox, bearings and encoder be independently removed? | SYS-REQ-036 requires replaceability where practical | CAD access checks and documented assembly/disassembly sequence |
| FS7-OQ-016 | What tolerance stack is needed for bearing coaxiality, motor/gearbox concentricity and encoder alignment? | Alignment errors may accumulate across interfaces | Datum/tolerance analysis and component drawings |
| FS7-OQ-017 | What fasteners, threads or inserts are required in the selected housing process? | Joint strength, repeat assembly and serviceability depend on them | Fastener/insert evidence and load calculation |
| FS7-OQ-018 | What is the motor heat flow into the housing and what thermal limits apply? | Affects housing temperature, fit and cable/component integration | FS-M-003/008 thermal data and material properties |
| FS7-OQ-019 | What ambient range applies under SYS-REQ-090? | Affects thermal expansion, lubrication and material choices | Approved indoor-lab ambient range; Project Lead |
| FS7-OQ-020 | What post-loaded-cycle integrity criteria and evidence plan apply under SYS-REQ-092? | Required to define post-test inspection/evaluation without inventing thresholds | Canonical requirement and approved test plan; Project Lead |
| FS7-OQ-021 | Are A0/A1 budget targets achievable with sourced components and manufacturing processes? | SYS-REQ-100 gives budget limits, but current quotes/BOM may be incomplete | Dated cost evidence and defined BOM scope; Mechanical Intern |
| FS7-OQ-022 | Which manufacturing options and India sourcing routes are practical? | Affects lead time, repeatability, inspection and downstream planning | Supplier/process evidence; FS-M-009 coordination |
| FS7-OQ-023 | What integration constraints must be handed to FS-M-008, FS-M-009 and FS-M-010? | Mechanical choices affect electrical, manufacturing and system integration | Versioned interface/constraint handoff and acknowledgement |

## 5. Decision Rules

1. **Concept CAD:** Keep the model labelled concept until exact interfaces, critical dimensions and calculations have been reviewed.
2. **Load path:** Show the arm-load path through shaft, dedicated bearings and housing. Keep gearbox torque reaction distinct; do not route arm loads through gearbox/motor bearings by default.
3. **Housing material:** Compare materials and processes using traceable properties and actual load-bearing functions. Do not infer printed-part adequacy from nominal geometry.
4. **Bearing-seat stiffness:** Assess seat deformation and alignment using the approved load cases and support arrangement. Use FEA only where justified.
5. **Interfaces:** Use exact candidate drawings. If dimensions are unavailable, mark the interface provisional rather than inventing a fit.
6. **IN-015/IN-016:** Follow the documented FS-M-006 interface decision. Do not independently substitute a shaft or bearing dimension.
7. **Hard stops:** Use IN-033 and applicable FS-M-005/006 load cases. Treat IN-018/IN-019 as preliminary until their assumptions are verified.
8. **Review:** Project Lead must review housing strength and the hard-stop load path under peak/impact conditions. The author cannot self-approve safety-critical conclusions.
9. **Encoder alignment:** Include shaft and housing/bearing support deformation. CAD coincidence alone does not prove alignment.
10. **Serviceability:** Verify removal path, tools, fasteners, cable disconnection and reassembly access in CAD; do not assume independent replacement.
11. **Mass/envelope:** Use approved arm-layout limits and source-backed component masses. Do not derive budgets from IN-039.
12. **Post-test integrity:** SYS-REQ-092 concerns integrity after loaded-cycle testing. Keep the requirement linked to its canonical definition and approved test plan; do not reinterpret it as a shock-load requirement.
13. **Cost/sourcing:** Use dated sources and a defined BOM scope. Do not claim budget compliance from incomplete or invented prices.

## 6. Project Lead Review Record

Complete this record when review occurs:

- Reviewer: `Project Lead; Independent Reviewer TBD for safety-critical structural and hard-stop checks`
- Review date: `TBD`
- CAD revision/commit: `TBD`
- FS-M-003/004/005/006 evidence revisions: `TBD`
- Structural load path and mounting interface findings: `TBD`
- Housing material/process and stiffness findings: `TBD`
- Hard-stop/impact load-path findings: `TBD`
- Encoder alignment and serviceability findings: `TBD`
- IN-015/IN-016 decision reference: `TBD`
- Mass/envelope/budget limitations: `TBD`
- Corrective actions and residual risks: `TBD`
- Review outcome: `PENDING`
- Evidence path / commit: `TBD`

Until the Project Lead has reviewed the evidence and recorded the disposition, critical housing-strength and hard-stop conclusions remain `NOT_VERIFIED`.

## 7. Change Control and Closure

For each closed assumption/question, record:

- Source path, exact artifact and revision.
- CAD and calculation revisions affected.
- Requirement and acceptance criterion affected.
- Decision, reviewer, date and commit.
- Downstream study notified.

Changes to motor, gearbox, shaft, bearing, encoder, hard-stop or mounting geometry require a review of affected CAD clearances, tolerance stacks, load paths and serviceability. Preserve previous decisions and revisions.

## 8. Must-Not-Conclude Register

Until required evidence and review exist, this study must not conclude that:

- The housing is adequate without documented load cases, material/process evidence and calculations.
- A printed housing, bearing seat or mount is acceptable for the load path without justified structural/process evidence.
- Mass or envelope budgets are met while SYS-REQ-039 and approved arm-layout limits remain unresolved.
- Hard stops survive peak/impact loads without a defensible load model and required review.
- Motor, gearbox, bearings and encoder are independently serviceable without evidence-backed assembly/access checks.
- Encoder alignment is acceptable based on CAD alone.
- The IN-015/IN-016 mismatch is resolved without the recorded FS-M-006 decision.
- Post-test integrity under SYS-REQ-092 is established without the approved test criteria and relevant evidence.
- A concept assembly constitutes a production release or human-interaction safety approval.

Closure requires evidence-backed dispositions for AC-001..AC-016, committed mandatory CAD/calculation/source deliverables, explicit downstream handoffs and Project Lead review of critical housing-strength and hard-stop load-path conclusions. The result is a concept integration assessment, not a released mechanical design.
