---
study_id: FS-M-005
title: Output Shaft Feasibility - Assumptions and Open Questions
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
---

# FS-M-005 Assumptions and Open Questions

## 1. Purpose and Rules

Track uncertainties that affect output-shaft geometry, material, strength, fatigue, impact, deflection, interfaces and manufacture.

- Use `FS5-ASM-nnn` for study-local assumptions and `FS5-OQ-nnn` for open questions.
- Preserve upstream IDs, values and statuses.
- Reference FS-M-001 ASM-001..ASM-012 and OQ-001..OQ-014 by ID; do not redefine them.
- Use FS-M-002 and FS-M-004 output artifacts by their exact names and verify revision before use.
- An assumption is not evidence of compliance. An unresolved safety-critical item cannot be closed by the author's judgment alone.
- Link every disposition to calculations, outputs, source evidence, acceptance criteria and the review record.

## 2. Upstream References

### FS-M-001

Authoritative path: `kritva-m/FS-M-001-integrated-actuator-system/ASSUMPTIONS_AND_OPEN_QUESTIONS.md`.

Use the original ASM-001..ASM-012 and OQ-001..OQ-014 records. Particular attention:

- OQ-009: shock-load assumptions.
- OQ-012: provenance of the approximately 47.5 N·m impact torque and approximately 0.86 EN8 safety-factor estimate.

IN-007, IN-015, IN-016, IN-017, IN-018, IN-019, IN-023, IN-031, IN-036 and IN-037 remain governed by the authoritative input register. This study must not independently promote their status.

### FS-M-002

Use:

- `outputs/LOAD_CASES.csv`
- `outputs/DYNAMIC_TORQUE_RESULTS.csv`
- `outputs/REFLECTED_INERTIA.csv`
- `outputs/GRAVITY_TORQUE_SWEEP.csv`, if present in the current baseline.

Verify file existence, revision, units, calculation method and review status. A summary or old copy does not replace the approved calculation output.

### FS-M-004

Use `outputs/INTERFACE_COMPATIBILITY.csv` and the relevant candidate manufacturer's interface drawing. Verify the exact gearbox candidate and source revision before fixing shaft interface geometry.

### FS-M-006

Coordinate the bearing pair, seat dimensions, bearing spacing, housing and arm-load path. The shaft study must not independently assume a resolved bearing arrangement.

## 3. Study-Local Assumptions

These are provisional working assumptions, not verified design facts.

| ID | Assumption | Rationale / limitation | Closure evidence |
|---|---|---|---|
| FS5-ASM-001 | 12 mm is the initial shaft diameter to evaluate | IN-015 is PRELIMINARY; geometry may require revision | Reproducible sizing and independent review |
| FS5-ASM-002 | Shaft is independently supported by a dedicated bearing pair | SYS-REQ-030/031; support geometry is not yet proven | FS-M-006 bearing/housing design |
| FS5-ASM-003 | Arm loads bypass gearbox and motor bearings | SYS-REQ-032 | Verified load path and bearing reaction calculations |
| FS5-ASM-004 | Single-contact hard-stop case governs initial stop-load screening | IN-036 is ASSUMED | Validated contact/load-sharing analysis or approved disposition |
| FS5-ASM-005 | IN-019 may be used only as a preliminary impact screening value | Provenance unresolved under OQ-012 | Reconciled load derivation and independent review |
| FS5-ASM-006 | IN-023's 1.5 static strength factor is a screening target | Failure criterion and margin convention must be documented | Approved calculation method and requirement confirmation |
| FS5-ASM-007 | Material handbook properties may support early comparison only | Actual condition, heat treatment and certification may differ | Applicable material specification or certified evidence |
| FS5-ASM-008 | EN19/42CrMo4 Q&T is a candidate for comparison, not selected | IN-037 is PRELIMINARY | Strength, toughness, fatigue, process and sourcing review |
| FS5-ASM-009 | EN8 normalised is retained as a comparison case | Reported factor of approximately 0.86 needs source/method verification | Reproduced calculation using traceable properties |
| FS5-ASM-010 | A machined shaft is the baseline for the primary load path | Cyclic torsion, bending and impact require justified properties and geometry | Manufacturing/process review |
| FS5-ASM-011 | Stress-concentration effects must be included where relevant | Shoulders, keyways, grooves and set screws can govern local strength | Geometry-based factor or documented conservative method |
| FS5-ASM-012 | FEA is conditional, not a substitute for hand calculations | Use only for a specific question that hand calculations cannot resolve | Justified model, boundary conditions and validation |

## 4. Open Questions

| ID | Question | Why it matters | Closure evidence / owner |
|---|---|---|---|
| FS5-OQ-001 | Which FS-M-002 load-case revision is authoritative for shaft design? | Determines the applicable force and torque envelope | Verified output path, revision and review status; Mechanical Intern |
| FS5-OQ-002 | What are the actual transverse forces, axial loads and lever arms at the shaft? | Torque alone cannot establish bending or combined stress | Approved load geometry and FS-M-002 data; Mechanical Intern |
| FS5-OQ-003 | What is the derivation and applicability of IN-019's approximately 47.5 N·m impact torque? | The estimate is preliminary and could dominate shaft strength | Reconciled calculation and independent review against OQ-012 |
| FS5-OQ-004 | What are the stop speed, contact duration, repetition and load-sharing conditions? | Impact response depends on dynamic and contact assumptions | FS-M-002 case definition and SYS-REQ-014/035 interpretation |
| FS5-OQ-005 | What peak duration and repetition must the shaft survive? | IN-031 is UNKNOWN; fatigue and transient limits depend on it | Resolved duty profile and upstream OQ-003 |
| FS5-OQ-006 | Which material grade, heat treatment and section condition are intended? | Material properties vary with condition and process | Approved material specification and traceable property evidence |
| FS5-OQ-007 | Is the reported EN8 safety factor of approximately 0.86 reproducible? | It cannot be relied upon without the original method and inputs | Calculation provenance, property source and independent check |
| FS5-OQ-008 | Which fatigue data are applicable to the selected material and surface condition? | Fatigue life cannot be inferred from yield strength alone | Traceable S-N or equivalent data, condition and method |
| FS5-OQ-009 | What shaft geometry and bearing spacing will FS-M-006 use? | Governs bending moments, reactions, deflection and critical sections | Coordinated dimensioned concept and revision |
| FS5-OQ-010 | How will the 12 mm shaft reconcile with the 6202/15 mm seat mismatch in IN-016? | Bearing-seat dimensions and shaft interface are currently inconsistent | FS-M-006 interface decision and verified bearing geometry |
| FS5-OQ-011 | Which gearbox output interface and torque-transfer method are available? | Keyway, clamp, coupling or D-shaft changes local stress and packaging | FS-M-004 `outputs/INTERFACE_COMPATIBILITY.csv` and candidate drawing |
| FS5-OQ-012 | What are the allowable encoder misalignment, shaft slope and runout limits? | SYS-REQ-034 requires alignment to remain within limits | Canonical limits and encoder manufacturer documentation |
| FS5-OQ-013 | What torsional twist is acceptable for positioning and control? | Shaft compliance can contribute to joint error | Canonical tolerance/control allocation and calculation |
| FS5-OQ-014 | What corrosion, temperature and environmental conditions apply? | Affects material, finish, corrosion protection and fatigue | SYS-REQ-090 and approved environment definition |
| FS5-OQ-015 | Which shoulder radii, grooves, keyways and retention features are required? | Geometry can introduce critical local stress | Interface and manufacturing concept with dimensions |
| FS5-OQ-016 | What tolerances, surface finish, runout and inspection datums are required? | Bearing and encoder alignment depend on manufacturability | Drawing requirements and manufacturing review |
| FS5-OQ-017 | Does the shaft require a critical-speed check beyond a screening estimate? | May matter if operating speed or excitation overlaps a bending mode | Speed range, support stiffness and documented screening |
| FS5-OQ-018 | Are material certificates and supplier traceability available for the intended build? | Final strength validation requires known material condition | Supplier documentation and procurement decision |
| FS5-OQ-019 | Are hand calculations sufficient for all critical sections and impact cases? | Complex geometry/contact may require additional analysis | Independent review of method limits; justified FEA if needed |
| FS5-OQ-020 | Who will independently review the strength and stop-impact conclusions? | Author must not self-approve safety-critical work | Named reviewer, review date, findings and recorded disposition |
| FS5-OQ-021 | What residual constraints must be handed to FS-M-006, FS-M-007, FS-M-009 and FS-M-010? | Shaft choices affect bearings, packaging, assembly and system integration | Traceable interface/constraint handoff and acknowledgement |

## 5. Decision Rules

1. **Diameter:** A nominal 12 mm diameter is a starting point. Decide adequacy only after the critical geometry and applicable load cases are evaluated.
2. **Material:** Do not select EN8, EN19/42CrMo4 Q&T or stainless steel based on grade name alone. Compare properties for the intended condition and process.
3. **Combined loading:** Check torsion, bending and axial loads at critical sections using a stated failure criterion and justified geometry.
4. **Stress concentration:** Assess shoulders, fillets, keyways, grooves and set-screw contacts where present. Do not treat nominal shaft stress as local peak stress.
5. **Static margin:** State the material property, failure criterion and margin convention used for IN-023. Avoid applying overlapping factors twice.
6. **Fatigue:** Require a supported duty spectrum and applicable material fatigue data. If either is missing, withhold a life claim.
7. **Impact:** Treat IN-018 and IN-019 as preliminary. Reconcile their assumptions with FS-M-002 and OQ-012; obtain independent review.
8. **Deflection:** Use the proposed support geometry and check encoder/bearing locations against actual limits. Missing limits mean no signoff conclusion.
9. **Bearing support:** Maintain the independent shaft/bearing/housing load path required by SYS-REQ-032. Do not route arm loads into gearbox or motor bearings by default.
10. **Interface:** Resolve the IN-015/IN-016 mismatch jointly with FS-M-004 and FS-M-006; do not silently change the shaft or bearing dimensions.
11. **Manufacturing:** Justify material, heat treatment, machining and inspection from load, fatigue and alignment requirements.
12. **FEA:** Use only when justified by a specific unresolved question; document model assumptions, mesh/convergence, boundary conditions and validation.
13. **Review:** Peak-load, impact and critical shaft-strength results remain `NOT_VERIFIED` until independently reviewed.

## 6. Required Independent Review Record

Complete when review takes place:

- Reviewer: `Independent Reviewer TBD`
- Review date: `TBD`
- FS-M-002 source revision/commit: `TBD`
- FS-M-004 interface revision/commit: `TBD`
- Shaft geometry revision: `TBD`
- Material condition and property sources: `TBD`
- Critical sections and governing load cases: `TBD`
- Static/combined strength findings: `TBD`
- Fatigue assumptions and findings: `TBD`
- Stop-impact assessment and IN-019 disposition: `TBD`
- Deflection/encoder alignment findings: `TBD`
- Corrective actions and residual risks: `TBD`
- Review outcome: `PENDING`
- Evidence path / commit: `TBD`

Do not mark the review `PASS` or `APPROVED` before the reviewer has examined the supporting evidence and the outcome is recorded.

## 7. Change Control and Closure

For each resolved assumption or question, record:

- Evidence path and source-register ID.
- Input/load-case and geometry revisions.
- Affected calculation/output and acceptance criterion.
- Decision, reviewer, date and repository commit.
- Downstream studies notified where relevant.

If a change affects the shaft diameter, material, bearing seats, interface, impact strength or deflection, rerun the affected calculations and update the integration handoff. Retain the previous decision history.

## 8. Must-Not-Conclude Register

Until evidence and required reviews exist, this study must not conclude that:

- A 12 mm shaft is adequate merely because nominal torsional stress appears modest.
- EN8 is acceptable based on the inherited approximate safety factor.
- The shaft survives the approximately 47.5 N·m impact case without validated load assumptions and independent review.
- Fatigue life is met without a supported duty spectrum and material fatigue data.
- Encoder alignment is acceptable without the required limits and support geometry.
- The 6202 bearing / 15 mm seat arrangement is compatible with the preliminary 12 mm shaft.
- The gearbox or motor bearings can carry arm loads without explicit manufacturer ratings.
- FEA, if performed, independently proves safety without validated loads, boundary conditions and suitable material data.
- A feasibility calculation constitutes a released design, production qualification or human-interaction safety approval.

Closure requires evidence-backed dispositions for all acceptance criteria, committed mandatory deliverables, explicit residual risks and independent review of critical strength and impact cases. The result is a feasibility assessment, not a released shaft design.
