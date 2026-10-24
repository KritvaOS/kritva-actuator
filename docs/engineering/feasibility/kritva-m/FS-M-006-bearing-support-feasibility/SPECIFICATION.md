---
study_id: FS-M-006
title: Bearing and Support Feasibility
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
downstream:
- FS-M-007
- FS-M-009
- FS-M-010
---

# FS-M-006 - Bearing and Support Feasibility

## 1. Purpose

Assess the feasibility of a dedicated output-shaft bearing pair and its joint-housing support for Kritva-M. Select candidate bearing types and arrangements from calculated loads, interface geometry, stiffness, life, environment and serviceability. The study must not assume that gearbox output bearings carry arm loads.

## 2. Scope

In scope:

- Bearing type and pair arrangement: deep-groove, angular-contact pair, tapered, crossed-roller and thin-section options as appropriate.
- Bearing spacing, locating/floating strategy, face-to-face/back-to-back arrangements, axial retention, preload/clearance and shaft/housing fits.
- Radial, axial and moment reactions from FS-M-005 `outputs/SHAFT_LOAD_CASES.csv`.
- Static rating C0, dynamic rating C, equivalent loads and L10 life with stated methods and limitations.
- Hard-stop/impact reaction screening against applicable static ratings.
- Bearing-seat and housing geometry, material/process, thermal expansion, sealing, lubrication and inspection.
- Coordination with shaft deflection and encoder alignment.
- Independent replacement, exact part numbers, mass, price and India sourcing when verifiable.

Out of scope:

- Final bearing or housing release, qualification testing or safety certification.
- Claiming life compliance while duty cycle or service-life requirements remain unknown.
- Assuming a catalogue rating applies without verifying bearing type, load direction, speed, lubrication, fits and operating conditions.

## 3. Requirements Traceability

Link to canonical requirements; do not redefine them:

- SYS-REQ-031: dedicated bearing pair in the joint housing, selected from load calculations with justified type, spacing, fits, preload/clearance and life.
- SYS-REQ-032: arm radial, axial and bending loads pass through shaft, bearings and housing, bypassing gearbox and motor bearings unless explicit manufacturer ratings permit otherwise.
- SYS-REQ-034: encoder alignment under rated load, including shaft deflection.
- SYS-REQ-035: hard stops.
- SYS-REQ-036: motor, gearbox, bearings and encoder independently replaceable where practical.
- SYS-REQ-038: load-bearing material and process justified by calculation.
- SYS-REQ-090: ambient conditions (range TBD).
- SYS-REQ-091: gearbox and bearing life checked against the intended duty cycle.
- SYS-REQ-092: after loaded-cycle testing, no unacceptable permanent deformation, loosening, bearing damage or encoder misalignment.
- SYS-REQ-014: shock-load specification when the arm must absorb impacts.

## 4. Upstream Inputs and Dependencies

Use authoritative inputs from `kritva-m/FS-M-001-integrated-actuator-system/inputs/INPUTS.md`, preserving the IDs, values and statuses for IN-007, IN-015, IN-016, IN-018, IN-019, IN-023, IN-026, IN-030, IN-031 and IN-036. Reference upstream ASM-001..ASM-012 and OQ-001..OQ-014 by ID; do not redefine them.

Use FS-M-002 outputs `outputs/LOAD_CASES.csv` and `outputs/DYNAMIC_TORQUE_RESULTS.csv` as applicable, after verifying file existence, revision, units and review status.

Use FS-M-004 `outputs/INTERFACE_COMPATIBILITY.csv` and relevant candidate evidence to understand the gearbox interface and permitted loads.

Use FS-M-005 outputs:

- `outputs/SHAFT_LOAD_CASES.csv`
- `outputs/SHAFT_STRENGTH_CHECK.csv`
- `outputs/IMPACT_CHECK.csv`
- `outputs/DEFLECTION_CHECK.csv`
- `outputs/INTERFACE_CHECK.csv`
- `outputs/MATERIAL_COMPARISON.csv`

Verify their revisions and review status before using them. FS-M-005 and FS-M-006 are peer studies and must iterate jointly. Missing or unreviewed load/interface data must result in a documented blocker or provisional assessment, not invented reactions.

## 5. Baseline and Known Interface Issue

- IN-007: output peak torque 20 N·m minimum / 25 N·m stretch, PRELIMINARY.
- IN-015: independent output shaft nominal diameter 12 mm, PRELIMINARY.
- IN-016: 6202 bearing associated with 15 mm seats, ASSUMED. A 6202 has a 15 mm bore and does not directly fit a nominal 12 mm shaft.
- Bearings with 12 mm bore, such as 6001 or 6201 series, may be investigated as candidates only; neither is selected by this specification.
- IN-018: hard-stop kinetic energy approximately 1.9 J, PRELIMINARY.
- IN-019: estimated full-speed impact torque approximately 47.5 N·m, PRELIMINARY; provenance unresolved under upstream OQ-012.
- IN-023: static strength factor target 1.5, ASSUMED.
- IN-026: duty cycle and continuous holding duration, UNKNOWN.
- IN-030: expected service life, UNKNOWN.
- IN-031: peak duration/repetition, UNKNOWN.
- IN-036: single-contact hard-stop load-sharing case governs, ASSUMED.

Do not silently change IN-015 or IN-016. Document bearing/shaft alternatives and submit the interface decision to the Project Lead, jointly with FS-M-005. Any candidate series or part number requires verification against manufacturer documentation.

## 6. Load Path and Reaction Analysis

The default load path is arm -> independent output shaft -> dedicated bearing pair -> load-bearing housing. Gearbox and motor bearings are bypassed unless the exact manufacturers explicitly permit the calculated radial, axial and moment loads for the actual operating conditions.

Use the shaft/bearing geometry and reactions in FS-M-005 `outputs/SHAFT_LOAD_CASES.csv`. If that file lacks bearing reactions or support coordinates, coordinate a revised analysis with FS-M-005; do not infer reaction forces from output torque alone.

For each load case, document radial and axial force, bending/moment effects, reaction distribution, load direction, operating speed, duration and repetition. Check whether the proposed pair and spacing provide adequate stiffness and support. Treat the bearing pair as a system with shaft, housing, fits and load path, not merely as a catalogue rating.

## 7. Bearing Type and Arrangement Selection

Compare suitable bearing architectures against the actual load spectrum, packaging, stiffness, alignment, speed, friction, replaceability and cost:

- Deep-groove ball bearings: assess combined-load capability and moment support limits for the chosen arrangement.
- Angular-contact pairs: assess contact angle, pair orientation, axial capacity, preload and stiffness.
- Tapered roller pairs: assess combined load capacity, preload adjustment, friction and package needs.
- Crossed-roller or thin-section bearings: assess moment capacity, stiffness, envelope, cost and manufacturer limits.

Select no type solely by generic family capability. Verify the exact candidate's permitted loads and arrangement. Evaluate bearing spacing, face-to-face/back-to-back pairing, locating/floating strategy, thermal expansion and axial retention. Do not impose preload without manufacturer guidance and a justified thermal/tolerance analysis.

## 8. Static and Dynamic Load Ratings

For each exact candidate, record manufacturer C0 (basic static load rating), C (basic dynamic load rating), limiting speed, permitted axial/radial load conditions, load factors and applicable definitions. Source each value to a specific catalogue, datasheet or manufacturer document.

Calculate equivalent static and dynamic bearing loads using the applicable manufacturer or recognized standard method, documenting factors and applicability. Compare the static equivalent load with the appropriate static rating using a stated safety criterion. Account for combined radial/axial loads and any moment effects that the selected bearing arrangement can actually support.

Do not treat C0 or C as a universal allowable force. Verify the rating basis and the candidate-specific conditions before concluding suitability.

## 9. Life Assessment

Use a recognized bearing life method applicable to the selected bearing type, manufacturer and load conditions. State the equivalent dynamic load, speed, exponent/method, reliability or modification factors, lubrication, contamination, alignment and load spectrum assumptions. Compare calculated L10 life with the approved service-life target and duty requirements.

IN-026, IN-030 and IN-031 are UNKNOWN. Until duty, holding duration, required service life and peak repetition are resolved, report only conditional calculations or comparative screening. Do not claim service-life compliance from a catalogue life figure alone.

## 10. Hard-Stop and Impact Assessment

Evaluate bearing reactions for the relevant FS-M-005 and FS-M-002 stop/impact cases. Reconcile IN-018 and IN-019 with upstream OQ-012 and document uncertainty in torque, force, duration, contact assumptions and load sharing.

Compare impact-related equivalent static load against the applicable C0 rating and the selected arrangement's permitted load envelope. Do not assume the basic static rating alone proves survival of a transient impact. Consider shaft/housing compliance, contact dynamics, fit movement and local seat stress where material.

Independent review is mandatory for peak-load and stop-impact bearing checks. The study author cannot approve their own safety-critical analysis. If independent review has not occurred, mark the result `NOT_VERIFIED`.

## 11. Shaft, Housing and Bearing Seats

Coordinate with FS-M-005 on shaft diameter, shoulder locations, fits, deflection and slope. Resolve the 12 mm shaft versus 6202's 15 mm bore mismatch as an explicit project decision. Investigate 12 mm-bore series only as sourced candidates; verify actual bore, outside diameter, width, ratings, speed and load capabilities.

Define shaft and housing seat dimensions, tolerances, roundness/cylindricity where required, surface finish, shoulder squareness, coaxiality, retention and assembly access. Evaluate the intended fit against load direction, ring creep risk, thermal expansion and manufacturer recommendations.

Load-bearing bearing seats in the housing require a justified material and manufacturing process. A 3D-printed housing seat must not be accepted merely because the nominal geometry fits; evaluate stiffness, creep, anisotropy, temperature, wear, tolerances and retention. Use a machined or otherwise validated load-bearing interface unless analysis and evidence justify another process.

## 12. Encoder Alignment and Deflection

Use FS-M-005 `outputs/DEFLECTION_CHECK.csv` and the actual bearing-support geometry to assess shaft deflection and slope at bearing and encoder locations. Check SYS-REQ-034 against the canonical alignment limits and encoder manufacturer's allowable misalignment.

Record radial and angular displacement, support compliance, fit effects and tolerance stack-up as relevant. If encoder limits or support geometry are unavailable, mark the alignment conclusion BLOCKED or PROVISIONAL. Feed any bearing spacing or stiffness changes back to FS-M-005.

## 13. Lubrication, Sealing and Environment

Compare candidate lubrication type, replenishment requirements, seals/shields, contamination sensitivity, mounting orientation, allowable operating temperature and speed limits. Consider thermal expansion and preload/clearance changes across the intended ambient and operating range under SYS-REQ-090.

Document maintenance access and whether the bearing pair can be replaced independently without destructive disassembly. Do not infer lifetime lubrication, sealing performance or temperature suitability unless the exact candidate documentation supports it.

## 14. Deliverables and Repository Structure

Mandatory:

- `calculations/`: reaction, equivalent load, static rating, life, fit/tolerance, thermal and stiffness calculations.
- `outputs/`: machine-readable candidate matrix, load checks, life assessment, interface decision and support comparison.
- `component_research/`: manufacturer catalogues, candidate documentation, drawings and written confirmations.
- `references/SOURCE_REGISTER.csv`: traceable source register for all candidate ratings, dimensions, methods and commercial claims.

Conditional:

- `simulation/`: when analysis justifies a specific unresolved question, such as housing-seat deformation or complex load sharing. Record model, boundary conditions, mesh/convergence, validation and limitations.
- `CAD/`: when support geometry is sufficiently mature for a meaningful assembly/clearance model.
- `cost_estimate/`: only when prices and integration costs have sufficient evidence for a defensible comparison.

Not applicable to this initial desk-based study:

- `test_data/`: no physical bearing test is required for the initial feasibility comparison. If testing is later authorized, create a scoped test plan and separate evidence record.

## 15. Acceptance Criteria

| AC | Criterion |
|---|---|
| AC-001 | Upstream input IDs, values and statuses are preserved and traceable. |
| AC-002 | FS-M-002 load artifacts and FS-M-005 shaft outputs are verified by path, revision, units and review status; missing dependencies are blocked explicitly. |
| AC-003 | FS-M-004 gearbox interface and permitted-load evidence is reconciled with the independent bearing load path. |
| AC-004 | Bearing candidates have verified manufacturer identities, exact model/part numbers or are clearly marked unverified leads. |
| AC-005 | Bearing type, pair arrangement, spacing, locating/floating strategy, axial retention and preload/clearance rationale are documented. |
| AC-006 | Radial, axial and moment reactions are derived from the documented shaft/load cases and support geometry. |
| AC-007 | Candidate C0, C, speed and permitted-load ratings are sourced and checked against applicable conditions. |
| AC-008 | Equivalent static/dynamic load and life calculations use a stated, applicable method with traceable inputs. |
| AC-009 | Life claims are withheld while duty, required service life or peak duration/repetition remains unresolved. |
| AC-010 | Hard-stop and impact bearing checks use the applicable upstream cases; IN-019 uncertainty and OQ-012 are addressed. |
| AC-011 | The 6202/15 mm bore versus 12 mm shaft mismatch is explicitly assessed and escalated for project decision without silently changing IN-015 or IN-016. |
| AC-012 | Shaft/housing fits, seats, retention, material/process and thermal expansion are assessed or explicitly left open. |
| AC-013 | Shaft deflection, bearing support stiffness and encoder alignment are coordinated with FS-M-005 and checked against SYS-REQ-034 limits or marked blocked. |
| AC-014 | Lubrication, sealing, ambient conditions, replaceability, exact part numbers, pricing and India sourcing are documented with evidence or marked UNKNOWN. |
| AC-015 | Mandatory deliverables and `references/SOURCE_REGISTER.csv` are complete and reproducible; conditional and not-applicable deliverables are handled as specified. |
| AC-016 | Independent review of peak-load and stop-impact bearing checks is recorded, with residual risks and the provisional disposition explicit. |

## 16. Review and Approval

The Mechanical Intern prepares the comparison and calculations. FS-M-005 provides shaft loads, geometry and deflection inputs; FS-M-004 provides gearbox interface evidence. Project Lead resolves the IN-015/IN-016 interface decision.

Independent Reviewer TBD must review peak-load and stop-impact bearing checks. The author cannot self-approve safety-critical results. Record findings, reviewer, date, evidence revision, corrective actions and commit in `REVIEW.md` or the approved project review record. Without independent review, affected results remain `NOT_VERIFIED`.

## 17. Must-Not-Conclude and Completion Definition

This study must NOT conclude that:

- A bearing is adequate based on bore size or catalogue C0/C values alone.
- Required life is met while duty cycle, service-life target or peak repetition is unknown.
- A 6202 bearing is compatible with the 12 mm shaft.
- A 3D-printed bearing seat is acceptable without justified material, process and load-bearing validation.
- The gearbox output bearing can carry arm loads by default.
- A nominal static-rating check proves survival of stop-impact loads.
- Encoder alignment is acceptable without support geometry and actual limits.
- A candidate part number, price or India availability is verified without traceable evidence.
- The feasibility result constitutes released hardware or safety approval.

FS-M-006 is complete when AC-001..AC-016 are dispositioned with evidence, mandatory deliverables are committed, the bearing/shaft interface decision is escalated and recorded, and independent review of critical peak/impact checks is documented. The result is a feasibility assessment, not a released bearing or housing design.
