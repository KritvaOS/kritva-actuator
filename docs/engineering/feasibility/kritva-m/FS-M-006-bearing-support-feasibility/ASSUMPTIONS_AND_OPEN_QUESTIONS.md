---
study_id: FS-M-006
title: Bearing and Support Feasibility - Assumptions and Open Questions
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Independent Reviewer TBD
upstream:
- FS-M-001
- FS-M-002
- FS-M-004
- FS-M-005
---

# FS-M-006 Assumptions and Open Questions

## 1. Purpose and Rules

Track unresolved decisions affecting bearing type, arrangement, ratings, life, interfaces, housing support and serviceability.

- Use `FS6-ASM-nnn` for study-local assumptions and `FS6-OQ-nnn` for open questions.
- Preserve upstream input IDs and statuses.
- Reference FS-M-001 ASM-001..ASM-012 and OQ-001..OQ-014 by ID; do not redefine them.
- Use exact FS-M-002, FS-M-004 and FS-M-005 output names and verify revisions before use.
- Unknown ratings or missing evidence must remain unknown; they cannot be treated as passes.
- Link closures to evidence, calculations, acceptance criteria, reviewer disposition and commit.

## 2. Upstream References

### FS-M-001

Authoritative path: `kritva-m/FS-M-001-integrated-actuator-system/ASSUMPTIONS_AND_OPEN_QUESTIONS.md`.

Preserve upstream assumptions ASM-001..ASM-012 and questions OQ-001..OQ-014. OQ-009 concerns shock-load assumptions; OQ-012 concerns provenance of the preliminary impact estimate. Use the original records rather than creating duplicate upstream questions.

Relevant inputs include IN-007, IN-015, IN-016, IN-018, IN-019, IN-023, IN-026, IN-030, IN-031 and IN-036.

### FS-M-002

Use `outputs/LOAD_CASES.csv` and `outputs/DYNAMIC_TORQUE_RESULTS.csv`, plus `outputs/REFLECTED_INERTIA.csv` where relevant. Verify file existence, revision, units, definitions and review status.

### FS-M-004

Use `outputs/INTERFACE_COMPATIBILITY.csv` and exact-candidate manufacturer documentation. Confirm the gearbox interface and any explicitly permitted output-bearing loads; do not assume the gearbox bearing carries the arm.

### FS-M-005

Use:

- `outputs/SHAFT_LOAD_CASES.csv`
- `outputs/SHAFT_STRENGTH_CHECK.csv`
- `outputs/IMPACT_CHECK.csv`
- `outputs/DEFLECTION_CHECK.csv`
- `outputs/INTERFACE_CHECK.csv`
- `outputs/MATERIAL_COMPARISON.csv`

FS-M-005 and FS-M-006 must iterate jointly on bearing locations, reactions, shaft-seat dimensions, deflection and encoder alignment. A shaft load case is not automatically a bearing reaction calculation unless its support assumptions and reactions are explicitly defined.

## 3. Study-Local Assumptions

These entries are provisional working assumptions, not verified design facts.

| ID | Assumption | Rationale / limitation | Closure evidence |
|---|---|---|---|
| FS6-ASM-001 | Arm loads use an independent shaft/bearing/housing path | SYS-REQ-032; gearbox and motor bearings bypassed by default | Verified load path and reaction calculations |
| FS6-ASM-002 | A dedicated bearing pair is the baseline | SYS-REQ-031; exact arrangement remains undecided | Load-based arrangement assessment |
| FS6-ASM-003 | 6202 is not directly compatible with the preliminary 12 mm shaft | 6202 has a 15 mm bore; IN-015/IN-016 mismatch | Project Lead decision with FS-M-005 |
| FS6-ASM-004 | 6001 and 6201 series may be investigated as 12 mm-bore candidates | Candidate series only; dimensions and ratings require verification | Exact manufacturer/model evidence |
| FS6-ASM-005 | Single-contact hard-stop load sharing is the initial governing assumption | IN-036 is ASSUMED | Validated load-sharing/contact assessment |
| FS6-ASM-006 | IN-019 is only a preliminary impact screening value | Provenance unresolved under OQ-012 | Reconciled load derivation and independent review |
| FS6-ASM-007 | Catalogue C and C0 values are meaningful only with their definitions and conditions | Rating applicability varies by load, speed and arrangement | Candidate-specific rating checks |
| FS6-ASM-008 | Bearing life cannot be signed off with duty and service-life inputs unknown | IN-026 and IN-030 UNKNOWN; IN-031 UNKNOWN | Resolved duty/life inputs and reviewed calculation |
| FS6-ASM-009 | Housing bearing seats are load-bearing structural features | Fit, stiffness, creep and wear affect support accuracy | Material/process justification |
| FS6-ASM-010 | Preload/clearance is not selected until fit and thermal effects are evaluated | Excessive preload or incorrect clearance can impair operation | Manufacturer guidance and tolerance/thermal analysis |
| FS6-ASM-011 | Encoder alignment must be checked using actual support and shaft compliance | SYS-REQ-034 | Verified limits and coordinated deflection results |
| FS6-ASM-012 | Candidate prices and India availability are unconfirmed until sourced | Prevents invented commercial claims | Dated supplier evidence |

## 4. Open Questions

| ID | Question | Why it matters | Closure evidence / owner |
|---|---|---|---|
| FS6-OQ-001 | Which FS-M-005 load-case revision and support geometry are approved? | Bearing reactions depend on loads and support coordinates | Verified artifact paths, revision and review status; Mechanical Intern |
| FS6-OQ-002 | What radial, axial and moment reactions act at each bearing? | Torque alone does not establish bearing loads | Reaction calculation using shaft geometry and applicable load cases; Mechanical Intern |
| FS6-OQ-003 | How will the IN-015 12 mm shaft and IN-016 6202/15 mm seat mismatch be resolved? | Direct interface is dimensionally incompatible | Coordinated alternatives and recorded Project Lead decision; FS-M-005 owner |
| FS6-OQ-004 | Which exact bearing type and pair arrangement suits the load spectrum? | Arrangement affects axial capacity, stiffness and moment support | Candidate comparison and load-based justification; Mechanical Intern |
| FS6-OQ-005 | What bearing spacing and locating/floating strategy are required? | Controls reactions, moment support and thermal expansion | Coordinated shaft/housing concept and thermal assessment; Mechanical Intern |
| FS6-OQ-006 | Which fits and tolerances are required for shaft and housing seats? | Affects ring creep, stiffness, alignment and assembly | Manufacturer guidance and tolerance analysis; Mechanical Intern |
| FS6-OQ-007 | Is preload required, or is a clearance class appropriate? | Impacts friction, stiffness, temperature and life | Candidate-specific guidance and tolerance/thermal analysis; Mechanical Intern |
| FS6-OQ-008 | What exact C0, C, speed and permitted-load ratings apply? | Prevents unsupported catalogue-rating assumptions | Exact model documentation and normalized candidate matrix; Mechanical Intern |
| FS6-OQ-009 | What is the applicable static equivalent load and safety criterion? | Needed for static suitability and shock-related screening | Documented load method and candidate-specific calculation; Mechanical Intern |
| FS6-OQ-010 | What dynamic equivalent load and L10 method apply? | Life calculations depend on bearing type and loading | Applicable standard/manufacturer method with traceable inputs; Mechanical Intern |
| FS6-OQ-011 | What duty cycle and continuous holding duration apply? | IN-026 is UNKNOWN | Approved duty profile; Project Lead |
| FS6-OQ-012 | What expected service life must be demonstrated? | IN-030 is UNKNOWN | Approved life target and operating assumptions; Project Lead |
| FS6-OQ-013 | What peak duration, repetition and recovery conditions apply? | IN-031 is UNKNOWN | Resolved upstream question and duty profile; Project Lead |
| FS6-OQ-014 | What are the validated stop-impact reactions and their uncertainty? | IN-018/IN-019 are preliminary and the impact estimate's provenance is unresolved | Reconciled FS-M-002/005 cases and independent review; Independent Reviewer TBD |
| FS6-OQ-015 | Does the bearing arrangement withstand the governing stop-impact case? | A static catalogue rating alone does not establish transient survival | Documented impact reaction comparison and independent review; Independent Reviewer TBD |
| FS6-OQ-016 | Can the housing seat material/process sustain loads without unacceptable deformation or creep? | Printed and machined seats may behave differently | Structural/process justification and relevant material evidence; Mechanical Intern |
| FS6-OQ-017 | What encoder alignment limits apply at the bearing-supported shaft? | SYS-REQ-034 requires alignment under rated load | Canonical limits, encoder data and FS-M-005 deflection results; Mechanical Intern |
| FS6-OQ-018 | What lubrication, sealing and maintenance arrangement is appropriate? | Affects life, contamination sensitivity and serviceability | Exact bearing documentation and environment assessment; Mechanical Intern |
| FS6-OQ-019 | What ambient and operating temperature range applies? | Affects clearance, preload, lubrication and life | SYS-REQ-090 conditions and thermal assessment; Project Lead |
| FS6-OQ-020 | Can the bearing pair be replaced independently in the intended housing? | Required serviceability consideration under SYS-REQ-036 | Assembly/serviceability review and documented access strategy; Mechanical Intern |
| FS6-OQ-021 | Which exact candidate models, prices and Indian sourcing options are verifiable? | Procurement feasibility depends on traceable evidence | Dated manufacturer/distributor documentation or quotations; Mechanical Intern |
| FS6-OQ-022 | What bearing constraints must be handed to FS-M-007, FS-M-009 and FS-M-010? | Support geometry affects integration and packaging | Interface/constraint handoff with revisions and acknowledgements; Mechanical Intern |

## 5. Decision Rules

1. **Bearing selection:** Compare candidate types and exact models using the calculated load spectrum, arrangement, speed, stiffness, interface and environment. Do not select by bore size alone.
2. **6202 mismatch:** Do not silently alter IN-015 or IN-016. Investigate options and obtain an explicit Project Lead decision with FS-M-005 coordination.
3. **Candidate series:** 6001/6201 are research candidates only. Verify exact dimensions, C, C0, speed and permitted load conditions before ranking.
4. **Load path:** Arm radial, axial and bending loads pass through the independent shaft, bearing pair and housing. Gearbox/motor bearing loads are prohibited by default unless exact manufacturer ratings explicitly allow them.
5. **Static rating:** Use an applicable equivalent static load method and documented criterion. A catalogue C0 value is not an allowable load for every configuration.
6. **Dynamic rating/life:** State the method, speed, load spectrum, lubrication and modification assumptions. Withhold life compliance while IN-026, IN-030 or IN-031 remains unresolved.
7. **Impact:** Use the relevant FS-M-002/FS-M-005 case and document duration, repetition, reaction distribution and limitations. Require independent review.
8. **Fit and clearance:** Select shaft/housing fits and preload/clearance from manufacturer guidance, load direction, assembly tolerance and thermal expansion, not generic assumptions.
9. **Housing:** Justify load-bearing seat material and process. Do not accept a 3D-printed bearing seat merely because it has the correct nominal diameter.
10. **Encoder:** Check deflection/slope and alignment against actual limits. Missing limits or geometry mean no signoff conclusion.
11. **Sourcing:** Keep part number, rating, price and availability claims tied to exact, dated sources.
12. **Review:** The author cannot self-approve safety-critical peak-load or stop-impact checks. Until independent review is recorded, mark the results `NOT_VERIFIED`.

## 6. Independent Review Record

Complete this record when the review occurs:

- Reviewer: `Independent Reviewer TBD`
- Review date: `TBD`
- FS-M-002 source revision/commit: `TBD`
- FS-M-005 source revision/commit: `TBD`
- Bearing candidate model and rating source: `TBD`
- Governing load case and bearing reactions: `TBD`
- Static-rating method and result: `TBD`
- Impact/stop-load method and result: `TBD`
- Rating applicability and unresolved uncertainties: `TBD`
- Corrective actions and residual risks: `TBD`
- Review outcome: `PENDING`
- Evidence path / commit: `TBD`

Do not change the outcome to `PASS` or `APPROVED` until the independent reviewer has examined the evidence and the disposition is recorded.

## 7. Interface Decision Record

The IN-015/IN-016 mismatch requires an explicit decision. Complete when the options have been assessed:

- IN-015 status/value: `PRELIMINARY - 12 mm nominal shaft`
- IN-016 status/value: `ASSUMED - 6202 with 15 mm bore/seat`
- Candidate alternatives: `TBD; investigate 12 mm-bore series only with verified documentation`
- Shaft and bearing interface alternatives: `TBD`
- Effects on strength, stiffness, envelope, life and replacement: `TBD`
- FS-M-005 coordination/evidence: `TBD`
- Project Lead decision: `OPEN`
- Decision date and commit: `TBD`

Do not record an alternative as selected until the Project Lead decision and required engineering review are captured.

## 8. Change Control and Closure

For each resolved question or assumption, record:

- Evidence path and source-register ID.
- Exact bearing model and document revision.
- Load-case and support-geometry revisions.
- Affected calculation/output and acceptance criterion.
- Decision, reviewer, date and repository commit.
- Downstream studies notified where applicable.

If a change affects bearing type, spacing, shaft seat, housing seat, preload/clearance, impact capacity or encoder alignment, rerun the affected calculations and notify FS-M-005 and relevant downstream owners. Preserve prior decisions and their provenance.

## 9. Must-Not-Conclude Register

Until the required evidence and reviews exist, this study must not conclude that:

- A bearing is adequate based on bore size or catalogue ratings alone.
- Bearing life is met while duty cycle, service-life target or peak repetition remains unknown.
- A 6202 bearing is compatible with the preliminary 12 mm shaft.
- A 6001/6201 series candidate is suitable solely because it has a 12 mm bore.
- The gearbox output bearing may carry arm loads by default.
- A catalogue static rating proves survival of stop-impact loads.
- A 3D-printed housing seat is acceptable without justified material, process and load-bearing validation.
- Encoder alignment is acceptable without actual support geometry and limits.
- A candidate part number, rating, price or India availability is confirmed without traceable evidence.
- A feasibility assessment constitutes released hardware, validated life or safety approval.

Closure requires evidence-backed dispositions for AC-001..AC-016, committed mandatory deliverables, an explicit Project Lead decision on the IN-015/IN-016 mismatch and independent review of critical peak/impact checks. The outcome is a feasibility assessment, not a released bearing or housing design.
