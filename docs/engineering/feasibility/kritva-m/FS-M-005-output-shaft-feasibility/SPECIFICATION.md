---
study_id: FS-M-005
title: Output Shaft Feasibility
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
downstream:
- FS-M-006
- FS-M-007
- FS-M-009
- FS-M-010
---

# FS-M-005 - Output Shaft Feasibility

## 1. Purpose

Evaluate the feasibility of a dedicated, independently supported output shaft for Kritva-M. Assess geometry, material, strength, fatigue, deflection, interfaces, manufacture and inspection against documented load cases. The preliminary 12 mm nominal diameter is a starting geometry, not an approved design.

## 2. Scope

In scope:

- Shaft geometry and preliminary diameter sizing.
- Material and heat-treatment comparison, including EN8, EN19/42CrMo4 Q&T and relevant stainless-steel alternatives.
- Combined torsion, bending and axial stress, stress concentrations, static margin and fatigue screening.
- Dynamic and hard-stop loading using verified FS-M-002 cases.
- Shaft deflection and slope at bearing locations and output encoder mounting.
- Dedicated bearing pair, bearing seats and the IN-016 diameter mismatch, coordinated with FS-M-006.
- Gearbox torque-transfer interface based on FS-M-004 `outputs/INTERFACE_COMPATIBILITY.csv`.
- Manufacturing, tolerances, surface finish, runout and inspection requirements.
- Hand calculations and traceable evidence; conditional FEA only where justified.

Out of scope:

- Final shaft release, production drawing approval or safety certification.
- Treating preliminary loads or handbook properties as verified material test data.
- Designing the gearbox, bearing pair or housing in isolation from their respective studies.
- Claiming fatigue life without a defined duty/load spectrum and supported material data.

## 3. Requirements Traceability

Link to canonical requirements; do not redefine their text:

- SYS-REQ-030: independent output shaft; nominal 12 mm initial CAD diameter; torsion, bending, combined stress, fatigue, stress concentrations and deflection validated before release.
- SYS-REQ-031: dedicated bearing pair.
- SYS-REQ-032: arm loads pass through shaft, bearings and housing, bypassing gearbox and motor bearings.
- SYS-REQ-033: gearbox output interface preferably at least 8 mm.
- SYS-REQ-034: encoder mounting and alignment remain within limits, including shaft deflection.
- SYS-REQ-035: hard stops.
- SYS-REQ-038: load-bearing material and process justified by calculation.
- SYS-REQ-014: shock-load specification.
- SYS-REQ-021: peak torque duration remains TBD.

## 4. Authoritative Inputs and Dependencies

Use the authoritative FS-M-001 input register at `kritva-m/FS-M-001-integrated-actuator-system/inputs/INPUTS.md`. Preserve upstream IDs, values and statuses. Required inputs include IN-007, IN-015, IN-016, IN-017, IN-018, IN-019, IN-023, IN-031, IN-036 and IN-037.

Use the FS-M-001 `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` by ID, particularly OQ-009 for shock loads and OQ-012 for the provenance of IN-019 and the preliminary EN8 safety-factor estimate. Do not redefine ASM-001..ASM-012 or OQ-001..OQ-014 in this study.

Use FS-M-002 outputs by their exact names, especially `outputs/LOAD_CASES.csv` and `outputs/DYNAMIC_TORQUE_RESULTS.csv`; verify their existence, revision and review status. Use FS-M-004 `outputs/INTERFACE_COMPATIBILITY.csv` and relevant gearbox candidate evidence. Coordinate bearing seats, bearing arrangement and housing interfaces with FS-M-006.

If upstream data are missing, inconsistent or unreviewed, mark dependent checks BLOCKED or PROVISIONAL. Do not invent replacement loads.

## 5. Baseline and Preliminary Screening

- IN-015: 12 mm nominal output shaft diameter, PRELIMINARY.
- IN-007: peak output torque 20 N·m minimum / 25 N·m stretch, PRELIMINARY.
- IN-018: mechanical-stop kinetic energy approximately 1.9 J, PRELIMINARY.
- IN-019: estimated full-speed impact torque approximately 47.5 N·m, PRELIMINARY; provenance unresolved.
- IN-023: target static strength factor 1.5, ASSUMED.
- IN-031: peak duration/repetition, UNKNOWN.
- IN-036: single-contact hard-stop load-sharing case governs, ASSUMED.
- IN-037: EN19/42CrMo4 Q&T is a candidate; the reported EN8 normalised safety factor of approximately 0.86 is preliminary and requires source/method verification.

For a solid circular shaft under pure torsion, nominal maximum shear stress is:

    tau_max = 16 T / (pi d^3)

For d = 12 mm, nominal torsional shear is approximately 29.5 MPa at 10 N·m, 58.9 MPa at 20 N·m and 73.7 MPa at 25 N·m. These values exclude bending, axial load, stress concentration, fatigue, material variability and impact dynamics. They are arithmetic screening values, not proof of adequacy.

## 6. Load Cases and Analysis Method

Build a traceable load-case table from FS-M-002, including relevant gravity, dynamic, holding, peak, stop-impact and hard-stop cases. For each case document torque, transverse forces, axial force, lever arms, direction, duration, repetition and source revision. Where a quantity is unknown, state the missing input and its consequence.

Calculate shaft reactions and bending moments using the proposed bearing locations and arm-load geometry. Evaluate critical sections: maximum bending, torque-transfer feature, shoulders, fillets, keyways, retaining-ring grooves, set-screw contacts, bearing seats and encoder interface. Include combined stress and local stress concentration effects. Use a stated method and explain assumptions; do not compare a local peak stress directly with an unrelated nominal material strength.

## 7. Strength and Material Assessment

Compare candidate materials using traceable property sources and the actual proposed condition, including heat treatment and section size where relevant. Distinguish minimum specified properties, handbook estimates, supplier claims and certified material data. Do not invent test results or assume that a grade name alone establishes yield strength, fatigue strength or toughness.

Assess:

- Torsional, bending and axial normal stress, including combined loading.
- Local stresses and concentration factors at geometric discontinuities.
- Static yield/failure criteria and the IN-023 target factor, with the chosen method stated.
- Impact and hard-stop cases, including uncertainty in IN-019.
- Fatigue under fully reversed and pulsating load cases using Goodman or an explicitly justified equivalent method.
- Sensitivity to surface finish, size, heat treatment, residual stress, corrosion and manufacturing variation.

EN8 must not be accepted or rejected solely on the inherited approximate safety factor. Reproduce the method and input properties before relying on it.

## 8. Fatigue and Life

Use the available duty/load spectrum, including torque direction, cycles, dwell, peak repetition and stop events. IN-031 remains UNKNOWN until resolved. If the spectrum or material fatigue data are insufficient, provide a conditional screening result and explicitly withhold a fatigue-life claim.

Document mean and alternating stress, selected fatigue criterion, stress concentration and notch sensitivity treatment, surface/size factors if used, reliability assumptions and data source. State whether the result is a comparative screening calculation or a substantiated life assessment. Do not invent a cycle count or safety factor to force closure.

## 9. Deflection, Slope and Encoder Alignment

Calculate shaft deflection and angular slope at both bearing locations and the output encoder mounting point for relevant combined loads. Use the actual proposed shaft geometry, support conditions, bearing spacing and material modulus. Check the result against the canonical encoder alignment limits in SYS-REQ-034; if the limits are unavailable, report the result as not signoff-ready.

Include torsional twist where relevant to positioning/control. Assess bearing-seat alignment, runout and local compliance. If the support geometry is not yet defined by FS-M-006, record the assumed boundary conditions and treat the result as provisional.

## 10. Interfaces and Load Path

The independent shaft carries arm loads through the dedicated bearing pair and housing, bypassing gearbox and motor bearings as required by SYS-REQ-032. Verify this load path with the FS-M-006 bearing/housing concept.

Use FS-M-004 `outputs/INTERFACE_COMPATIBILITY.csv` to assess gearbox output torque transfer: key/keyway, clamp, D-shaft, coupling or other documented interface. Check dimensions, fit, retention, contact pressure, stress concentration and serviceability as applicable. SYS-REQ-033's preferred gearbox output interface of at least 8 mm does not prove compatibility with the preliminary 12 mm independent shaft.

IN-016 records a 6202 bearing associated with 15 mm seats, creating a mismatch with IN-015's 12 mm nominal shaft. Do not silently modify either dimension. Document alternatives and hand off the bearing-seat decision to FS-M-006.

## 11. Hard Stops and Impact

Evaluate hard-stop and stop-impact cases from FS-M-002 and canonical SYS-REQ-014/SYS-REQ-035. Confirm the governing contact assumption, torque path, speed, energy, contact geometry, duration and repetition. IN-018 and IN-019 are preliminary; the origin and derivation of IN-019 must be reconciled with upstream OQ-012.

A shaft-only stress calculation may not capture contact compliance, rebound, housing deformation or load sharing. Explain model limitations and request a more detailed analysis where hand calculations cannot establish a defensible bound. Independent review is mandatory for peak-load and stop-impact conclusions. The author cannot self-approve safety-critical strength work.

## 12. Manufacturing and Inspection

Compare feasible machined manufacturing routes and material/heat-treatment conditions. Specify the critical drawing features needed for a later design: bearing-seat diameters and tolerances, shoulder/fillet radii, surface finish, runout, coaxiality, perpendicularity, keyway or clamp features, retention, encoder interface and inspection datums.

A 3D-printed polymer or metal part must not be assumed suitable for this primary shaft load path. Explain why a shaft carrying cyclic torque, bending and impact loads requires a justified load-bearing material and manufacturing process. If additive manufacturing is considered for a non-load-bearing prototype, separate it from the proposed production shaft.

## 13. Deliverables and Repository Structure

Mandatory:

- `calculations/`: reproducible load, reaction, bending, torsion, combined stress, static margin, fatigue, deflection/slope and sensitivity calculations.
- `outputs/`: machine-readable load cases, section checks, material comparison and shaft feasibility results.
- `references/SOURCE_REGISTER.csv`: traceable source register for all material properties, standards, geometry, equations and external claims.

Conditional:

- `simulation/`: FEA only if hand calculations identify a specific question that requires it. Record boundary conditions, mesh/convergence checks, material model, load mapping, validation and limitations.
- `CAD/`: conditional on geometry being sufficiently mature to model; label concept geometry and identify assumptions. CAD does not substitute for strength validation.

Not applicable to this initial desk-based study:

- `cost_estimate/`: no cost estimate is required for the shaft feasibility calculation.
- `test_data/`: no physical test data are required to complete the initial analytical study. If testing is later authorized, create a separately scoped test plan and evidence record.

## 14. Source and Calculation Evidence

Prefer applicable standards, recognized engineering handbooks, material standards, certified supplier material data and manufacturer drawings. Register the source title, publisher, edition/revision, date, URL or repository path, access date, relevant section/table and the exact claim supported.

Every calculated result must record input IDs, source revision, units, equations/method, assumptions and calculation revision. Handbook values without verified material condition must be labelled ASSUMED or PRELIMINARY, not certified properties. Record calculation scripts or spreadsheets in a reproducible form.

## 15. Acceptance Criteria

| AC | Criterion |
|---|---|
| AC-001 | Authoritative upstream input IDs, values and statuses are preserved and traceable. |
| AC-002 | FS-M-002 load-case and dynamic torque outputs are verified by path, revision and review status; missing dependencies are explicitly blocked. |
| AC-003 | FS-M-004 gearbox interface evidence is reconciled with the independent shaft and the selected candidate remains provisional until reviewed. |
| AC-004 | Shaft geometry, support locations and critical sections are documented with units and traceable assumptions. |
| AC-005 | Torsional, bending and axial stresses are calculated for the relevant load cases. |
| AC-006 | Combined stress and stress concentrations at critical geometric features are evaluated using a stated method. |
| AC-007 | Static strength and the IN-023 target factor are assessed with traceable material properties and clearly stated limitations. |
| AC-008 | Fatigue is evaluated using a stated method and supported load/material data; unresolved duty or fatigue evidence is recorded as a blocker. |
| AC-009 | Hard-stop and impact cases use documented FS-M-002 inputs; IN-019 uncertainty and upstream OQ-012 are addressed. |
| AC-010 | Deflection, slope and relevant torsional twist are assessed at bearing and encoder locations against SYS-REQ-034, or marked blocked where limits/geometry are missing. |
| AC-011 | Dedicated bearing pair and arm-load bypass path are documented and coordinated with FS-M-006. |
| AC-012 | Gearbox torque-transfer interface and the IN-015/IN-016 dimensional mismatch are assessed and handed off to FS-M-006 as needed. |
| AC-013 | Material, heat treatment, manufacture, tolerances, surface finish and inspection needs are justified or explicitly left open. |
| AC-014 | Calculation, output and material-source evidence is reproducible; all external numerical claims are registered in `references/SOURCE_REGISTER.csv`. |
| AC-015 | Mandatory deliverables exist; conditional FEA/CAD use is justified and `cost_estimate/` and `test_data/` remain not applicable to this initial study. |
| AC-016 | Independent review of peak-load, stop-impact and shaft-strength conclusions is recorded; residual risks and the provisional disposition are explicit. |

## 16. Review and Approval

The Mechanical Intern prepares the calculations and evidence. FS-M-002 and FS-M-004 owners supply load and interface data; FS-M-006 owner reviews bearing-seat and load-path dependencies. Independent Reviewer TBD must review the critical strength, peak and stop-impact cases.

The author must not approve their own safety-critical analysis. If independent review has not occurred, mark the relevant result `NOT_VERIFIED`, not `PASS`. Record findings, disposition, reviewer, date, evidence revision and commit in `REVIEW.md` or the project-approved review record.

## 17. Must-Not-Conclude and Completion Definition

This study must NOT conclude that:

- 12 mm is adequate merely because nominal torsional stress appears modest.
- EN8 is acceptable based on the inherited approximate safety factor.
- A shaft survives impact because nominal static stress is below a handbook yield value.
- Fatigue life is met without an adequate load spectrum and supported material data.
- Encoder alignment is acceptable without deflection/slope limits and support geometry.
- The 6202/15 mm bearing-seat arrangement is compatible with the 12 mm shaft.
- A shaft, bearing arrangement or hard stop is approved for production or human-interaction safety.

FS-M-005 is complete only when AC-001..AC-016 have evidence-backed dispositions, mandatory deliverables are committed, unresolved questions are explicit, and independent review of critical strength and impact conclusions is recorded. The outcome is a feasibility assessment, not a released shaft design.
