# Kritva Engineering Feasibility Studies — Methodology

**Document ID:** KRITVA-ENG-FS-METH-001  
**Version:** 0.1  
**Status:** Proposed  
**Canonical Path:** `docs/engineering/feasibility/common/FEASIBILITY_METHODOLOGY.md`

## 1. Purpose

This document defines the common engineering methodology for Kritva actuator feasibility studies.

It establishes consistent rules for:

- Selecting and evaluating technical evidence.
- Referencing canonical requirements and baseline inputs.
- Classifying input data and assumptions.
- Treating uncertainty and performing sensitivity analysis.
- Evaluating actuator torque, speed, motor, gearbox, shaft, bearing, thermal, and cost feasibility.
- Assessing and accepting engineering risks.
- Recording feasibility conclusions and verification limitations.

This methodology applies to Kritva-S, Kritva-M, Kritva-L, and other actuator-related feasibility studies.

The methodology establishes a common analysis approach. It does not replace applicable engineering standards, component manufacturers' instructions, safety reviews, or formal design approval.

## 2. Governing Requirements and Kritva-M Baseline

### 2.1 Canonical requirement source

Studies shall use the applicable requirements from the canonical file:

`requirements/SYSTEM_REQUIREMENTS.md`

Each applicable requirement shall be referenced by its assigned ID, following the `SYS-REQ-nnn` convention.

Study specifications, input records, calculation notes, and final reports shall link to the canonical requirement source. They shall not create independently maintained copies of system requirements.

Where a requirement is missing, ambiguous, conflicting, or insufficiently defined, record the issue in `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` and seek clarification through the applicable requirements process.

### 2.2 Kritva-M baseline values

For Kritva-M studies, the baseline shall be taken from the applicable entries in `requirements/SYSTEM_REQUIREMENTS.md` and identified by their actual `SYS-REQ-nnn` IDs.

The following values are examples of previously discussed preliminary design targets. They are not a substitute for checking the canonical requirements file and shall not be treated as approved baseline values unless confirmed there.

| Parameter | Previously discussed value | Treatment |
|---|---:|---|
| Continuous output torque | 10 Nm | Verify against the canonical requirement |
| Minimum peak output torque | 20 Nm | Verify against the canonical requirement and peak duration |
| Stretch peak output torque | 25 Nm | Verify against the canonical requirement and operating conditions |
| Target output speed | 45 RPM | Verify against the canonical requirement |
| DC supply | 24 V | Verify against the canonical requirement |
| Candidate gearbox ratios | 15:1, 20:1, 25:1 | Candidate values, not approved design decisions |
| Preliminary gearbox efficiency | 85% | Assumption unless supported by applicable data |
| Forearm and hand mass | 1.5 kg | Verify against the applicable baseline or identify as an assumption |
| Forearm and hand centre-of-mass distance | 180 mm | Verify against the applicable baseline or identify as an assumption |
| Payload mass | 1.0 kg | Verify against the applicable baseline or identify as an assumption |
| Payload centre-of-mass distance | 350 mm | Verify against the applicable baseline or identify as an assumption |
| Preliminary output shaft diameter | 12 mm | Verify against the applicable baseline or identify as a candidate dimension |
| Preliminary shaft free length | 30 mm | Verify against the applicable baseline or identify as a candidate dimension |
| Preliminary bearing span | 25 mm | Verify against the applicable baseline or identify as a candidate dimension |
| Preliminary shaft overhang | 20 mm | Verify against the applicable baseline or identify as a candidate dimension |
| Target operating life | 2,000 operating hours | Verify the applicable requirement and duty conditions |
| Mean output speed for life calculations | 10 RPM | Assumption unless supported by the intended duty profile |

If these values differ from the canonical requirements, the canonical requirements govern unless an authorized change has been approved.

If a value is absent from the requirements file, do not silently promote a previously discussed value to an approved requirement. Record it as `PRELIMINARY`, `ASSUMED`, or `UNKNOWN`, as appropriate, and obtain clarification where it materially affects the conclusion.

### 2.3 Baseline traceability

Each study shall identify:

- Applicable `SYS-REQ-nnn` IDs.
- The revision or commit of the requirements file used, where available.
- Relevant input values and their source.
- Any differences between the requirement and the analysis model.
- Any proposed changes and their justification.

If a requirement changes during a study, assess the impact on dependent calculations and conclusions. Record whether the study requires recalculation, review, or reopening.

## 3. Evidence Hierarchy

### 3.1 Preferred evidence order

Use the following hierarchy when evaluating technical claims. The order is a guide to evidence quality, not a substitute for assessing relevance, applicability, or uncertainty.

1. **Approved project requirements and controlled engineering baselines** — Authoritative for the specified project requirement or design constraint.
2. **Applicable official standards and regulatory requirements** — Authoritative within their stated scope and applicability.
3. **Manufacturer datasheets and official technical documentation** — Preferred evidence for component ratings, operating conditions, dimensions, limits, and interfaces.
4. **Manufacturer application notes and validated engineering models** — Useful for interpretation, design guidance, and operating-condition details.
5. **Traceable measurements and controlled test results** — Evidence of observed performance under the documented test conditions.
6. **Peer-reviewed technical publications and established engineering references** — Useful for general methods, material properties, and analytical approaches.
7. **Supplier quotations, catalogues, and distributor information** — Useful for availability, pricing, and preliminary component information; verify critical technical ratings against authoritative sources.
8. **Engineering estimates and analytical assumptions** — Acceptable for preliminary exploration when explicitly identified and accompanied by limitations.
9. **Unverified informal claims or undocumented estimates** — Insufficient on their own to establish a critical engineering conclusion.

A lower-ranked source may still be useful if it is the only available evidence, but the study shall document the limitation and avoid claiming a level of certainty that the evidence does not support.

### 3.2 Evidence traceability

For each material technical claim, record as applicable:

- Source identifier.
- Manufacturer or author.
- Document title and revision.
- Component model or applicable configuration.
- URL or canonical repository path.
- Date accessed or measured.
- Relevant page, table, graph, or section.
- Parameter supported by the source.
- Applicable conditions and limitations.

Datasheet values shall not be copied into calculations without checking units, operating conditions, and applicability to the selected component configuration.

### 3.3 Manufacturer ratings: continuous versus peak

Manufacturer ratings shall be interpreted according to their stated definitions and operating conditions.

**Continuous ratings** must be checked against the specified steady-state or continuous operating conditions, including cooling, ambient temperature, mounting, supply voltage, duty cycle, and thermal limits where stated.

**Peak ratings** must be checked against the permitted duration, repetition rate, duty cycle, initial temperature, current limit, and recovery conditions where specified.

A peak rating shall not be treated as a continuous rating.

If a manufacturer publishes a maximum or stall torque without sufficient operating conditions, do not assume that the value is available throughout the operating range or can be sustained safely.

For a motor, verify at least:

- Torque-speed characteristics.
- Continuous torque and speed limits.
- Peak torque and permitted duration.
- Current and voltage limits.
- Thermal and cooling conditions.
- Efficiency and losses, where available.
- Mechanical speed limits.
- Required operating point and duty profile.

For a gearbox, verify at least:

- Continuous output torque rating.
- Peak or intermittent torque rating and its conditions.
- Input speed limits.
- Efficiency and the conditions under which it is specified.
- Backlash and torsional stiffness, where relevant.
- Permitted radial and axial loads.
- Service-life assumptions.
- Lubrication, mounting, and thermal constraints.

A component shall not be declared suitable solely because a single published maximum rating exceeds the nominal requirement.

### 3.4 Conflicting evidence

When sources disagree:

1. Confirm that the sources refer to the same component revision and operating conditions.
2. Prefer the authoritative source applicable to the intended configuration.
3. Investigate whether differences arise from temperature, duty cycle, cooling, mounting, or rating definitions.
4. Record the discrepancy and its effect on the conclusion.
5. Use a conservative assumption for preliminary analysis where justified, while seeking clarification for material unresolved discrepancies.

Do not average conflicting ratings without a technically justified method.

## 4. Input Status Labels

Every material input shall be assigned an appropriate status.

| Status | Definition | Treatment |
|---|---|---|
| `APPROVED` | Formally approved requirement, constraint, or baseline input | Use within its approved scope and conditions. |
| `PRELIMINARY` | Provisional engineering target or input awaiting confirmation | Analyze provisionally and identify its approval status. |
| `ASSUMED` | Unverified value adopted to enable analysis | State the rationale, evaluate sensitivity, and identify its effect on the conclusion. |
| `UNKNOWN` | Value or condition has not been established | Do not invent a value; bound, parameterize, or request clarification. |
| `MEASURED` | Value supported by traceable measurement evidence | Record measurement method, conditions, instrumentation, uncertainty, and provenance as appropriate. |

These labels describe input provenance and status. They are not verification results.

A measured value is not automatically an approved design input. An approved requirement is not automatically evidence of measured performance.

Where an input is derived from another calculation, identify the derivation and the status of its underlying inputs.

## 5. Uncertainty and Sensitivity Analysis

### 5.1 General method

A study shall identify uncertainties that could materially affect the engineering decision.

For each significant uncertainty:

1. Identify the unknown or uncertain parameter.
2. Explain why it is uncertain.
3. Establish a justified range, bound, or set of scenarios where possible.
4. Calculate the effect on the relevant result.
5. Identify whether the conclusion changes across the range.
6. Record the additional evidence needed to reduce uncertainty.

Do not assign arbitrary precision to uncertain inputs. Use engineering units and precision appropriate to the evidence.

### 5.2 Unknown duty cycle

Duty cycle is a critical input for motor, gearbox, electrical, and thermal feasibility.

If the actuator duty cycle is unknown, do not assume that peak torque can be sustained continuously or that a low average torque guarantees acceptable temperature.

Where sufficient information exists, evaluate distinct operating scenarios, such as:

- Light or intermittent operation.
- Representative expected operation.
- High-load operation.
- Repeated peak-torque operation.
- Sustained high-load operation.

The actual scenarios and numerical ranges must be justified by the intended use case or explicitly identified as exploratory assumptions.

Record the required peak duration, repetition frequency, rest periods, ambient temperature, cooling conditions, and representative motion profile where relevant.

If the duty cycle cannot be bounded credibly, identify continuous thermal feasibility and repeated-peak capability as unresolved. The study may conclude that feasibility has not been established.

### 5.3 Centre-of-mass uncertainty

Centre-of-mass distance can materially affect gravity torque and joint loading.

For example, the previously discussed Kritva-M forearm and hand centre-of-mass distance was 180 mm. A study shall verify whether this value is present in the canonical requirements or another authoritative source.

If it is not confirmed, mark it `ASSUMED` or `PRELIMINARY`, as appropriate.

Evaluate the effect of plausible centre-of-mass variation using documented scenarios or a justified range. Consider changes in:

- Gravity torque.
- Output shaft bending load.
- Bearing reactions.
- Required motor torque.
- Gearbox loading.
- Structural stiffness and deflection.

Do not treat the 180 mm value as measured or approved solely because it has been used in a previous calculation.

### 5.4 Sensitivity methods

Use methods appropriate to the study, including:

- One-variable-at-a-time sensitivity analysis.
- Low, nominal, and high scenarios.
- Parameter sweeps.
- Analytical bounds.
- Monte Carlo analysis where justified by sufficient input distributions.
- Comparison of alternative operating assumptions.

For a sensitivity study, record the baseline case, changed parameter, evaluated range, resulting metric, and effect on the engineering decision.

Where multiple uncertainties interact, analyze combinations that could produce a materially worse operating condition.

A nominal result alone is insufficient when the conclusion depends strongly on an uncertain parameter.

### 5.5 Uncertainty disposition

Classify important uncertainty as one of the following:

- Acceptable for the current feasibility decision.
- Requires a conservative design assumption.
- Requires additional measurement or supplier evidence.
- Requires a focused follow-up study.
- Prevents the conclusion from being established.

Document the rationale and required action.

## 6. Standard Actuator Engineering Checks

The following checks are the default engineering scope for an integrated actuator feasibility study. Individual studies shall select the checks applicable to their scope and document exclusions.

### 6.1 Load cases and output torque

Identify applicable operating conditions, including:

- Static gravity loading.
- Required motion and acceleration.
- Deceleration and reversal.
- External forces and payload variation.
- Start-up and stopping conditions.
- Repeated peak loading.
- Shock or collision conditions where relevant.
- Stall or blocked-output conditions where credible.

For a force applied at a lever arm, calculate torque using the appropriate force vector and moment arm.

For a point mass under gravity, the magnitude of gravity torque about the joint is:

$$T_g = m\,g\,r_\perp$$

where:

- $m$ is the mass.
- $g$ is gravitational acceleration.
- $r_\perp$ is the perpendicular distance from the joint axis to the gravity-force line of action.

For a simplified horizontal arm, the gravity torque contribution from multiple masses is:

$$T_g = \sum_i m_i\,g\,r_{\perp,i}$$

Document the geometry and operating orientation. Include dynamic contributions where applicable, and do not treat static gravity torque as a complete motion requirement.

Avoid double-counting loads. Explain how gravity, acceleration, external forces, friction, and other terms are combined.

### 6.2 Static and dynamic torque

Determine the required output torque for each applicable load case.

Distinguish:

- Continuous or sustained torque.
- Intermittent torque.
- Peak torque and its duration.
- Dynamic torque during acceleration and deceleration.
- Exceptional loads such as shock or collision, where relevant.

Compare calculated demands against the appropriate continuous and peak ratings of the motor, gearbox, shaft, bearings, and other torque-path components.

A design shall not be considered feasible merely because the nominal static torque is below the peak rating.

### 6.3 Motor torque-speed and power

For a gearbox with reduction ratio $G$, define:

- $n_o$: output speed.
- $n_m$: motor speed.
- $T_o$: required output torque.
- $T_m$: motor shaft torque.
- $\eta_g$: gearbox efficiency under the applicable operating conditions.

For a simplified reduction model:

$$n_m = G\,n_o$$

$$T_m \approx \frac{T_o}{G\,\eta_g}$$

These equations are preliminary relationships. The actual system model must account for the gearbox configuration, operating conditions, losses, and any relevant dynamic effects.

Mechanical power is:

$$P = T\,\omega$$

$$\omega = \frac{2\pi n}{60}$$

Use consistent units and evaluate torque and speed together. Confirm that the candidate motor can deliver the required operating point rather than comparing torque and speed ratings independently.

### 6.4 Motor thermal and electrical margin

Evaluate:

- Continuous torque and current.
- Peak current and permitted duration.
- Torque-speed operating envelope.
- Motor winding and case temperature limits.
- Cooling and mounting assumptions.
- Driver current and voltage limits.
- Electrical and mechanical losses.
- Duty cycle and repetition of peak loads.
- Thermal margin under the relevant operating scenarios.

Where manufacturer thermal models or test data are unavailable, state the limitation and avoid unsupported temperature predictions.

A current or power calculation alone does not establish thermal feasibility.

### 6.5 Gearbox feasibility

Evaluate:

- Continuous and peak output torque.
- Input speed.
- Efficiency at relevant load and speed.
- Backlash and torsional stiffness where relevant.
- Radial and axial load capacity.
- Gearbox life and service conditions.
- Lubrication and thermal limits.
- Mechanical interfaces, size, and mass.
- Availability and cost.

Check combined operating conditions rather than relying on an isolated maximum torque rating.

### 6.6 Output shaft combined stress and fatigue

Identify torsion, bending, axial loading, and relevant load combinations.

For a solid circular shaft under pure torsion, the nominal maximum torsional shear stress is:

$$\tau_{\max} = \frac{16\,T}{\pi d^3}$$

This equation does not by itself establish shaft adequacy.

Where applicable, assess:

- Bending stress.
- Combined stress using an appropriate failure criterion.
- Stress concentrations at shoulders, keyways, splines, holes, and interfaces.
- Material strength and condition.
- Fatigue under repeated or reversing loads.
- Deflection and torsional stiffness.
- Manufacturing tolerances and surface condition.
- Relevant safety factors.

Document the material properties and the basis for the selected failure and fatigue criteria. If the loading spectrum or material data is insufficient, identify the limitation.

### 6.7 Bearing feasibility and life

Evaluate bearing loads, including radial and axial components, moments, preload, mounting, and load distribution where relevant.

Use the applicable manufacturer method and bearing type.

For basic rating life under the assumptions applicable to the bearing, the nominal relationship is:

$$L_{10} = \left(\frac{C}{P}\right)^{p}$$

where:

- $L_{10}$ is the basic rating life in millions of revolutions.
- $C$ is the basic dynamic load rating.
- $P$ is the equivalent dynamic bearing load.
- $p$ is the life exponent specified for the bearing type.

For ball bearings, $p$ is commonly 3; for roller bearings, it is commonly $10/3$. Verify the applicable manufacturer method and bearing type.

Convert life in revolutions to operating hours using the actual or justified representative speed profile. A mean-speed assumption shall be identified and justified.

The basic rating-life equation does not account automatically for every effect, including lubrication, contamination, misalignment, reliability adjustments, or static overload. Evaluate additional factors where relevant.

### 6.8 Thermal feasibility

Consider losses and thermal limits in the complete relevant system, including:

- Motor winding and other motor losses.
- Gearbox losses.
- Driver losses.
- Bearing and friction losses where material.
- Cooling path and mounting.
- Ambient temperature.
- Duty cycle and peak repetition.
- Thermal limits of materials, lubricants, sensors, and electronics.

Use a validated thermal model, manufacturer data, or appropriately controlled measurements where available.

If the available evidence is insufficient to calculate or verify operating temperature, record thermal feasibility as unresolved rather than inferring a pass.

### 6.9 Manufacturing and cost feasibility

Identify the proposed manufacturing and assembly approach.

Include relevant cost elements such as:

- Motor and gearbox.
- Shaft and bearings.
- Housing and structural components.
- Sensors and encoders.
- Driver and controller.
- Wiring and connectors.
- Fasteners and purchased components.
- Manufacturing and finishing.
- Assembly, calibration, and testing.
- Expected scrap, rework, and supplier constraints where material.

Record the basis of each cost estimate, including source, date, quantity assumptions, currency, and whether taxes, shipping, tooling, or assembly are included.

Distinguish supplier quotations from catalogue prices and engineering estimates.

A cost conclusion shall identify major cost drivers, missing quotations, and uncertainty. An incomplete BOM shall not be represented as a verified total production cost.

## 7. Proposed Safety-Factor and Margin Conventions

**Status: Proposed. These conventions are preliminary guidance and are not approved design requirements.**

The study shall identify the basis of every safety factor and margin used. Do not apply an arbitrary universal factor without considering the failure mode, material, loading, uncertainty, applicable standard, and consequences of failure.

### 7.1 General conventions

- Use applicable approved standards and design requirements where they define factors or acceptance limits.
- Distinguish a safety factor from an operating margin.
- Identify whether the comparison uses nominal, worst-case, or statistical values.
- Avoid applying the same uncertainty allowance multiple times without justification.
- Evaluate continuous and peak operating conditions separately.
- Record all deviations from the proposed guidance and justify them.

### 7.2 Proposed preliminary guidance

| Analysis area | Proposed preliminary convention | Important limitation |
|---|---|---|
| Static structural strength | Investigate a preliminary factor of 1.5 or greater against the applicable failure limit where appropriate | Not a universal acceptance criterion; material, load uncertainty, failure mode, and applicable standards govern. |
| Shaft combined loading | Use a documented combined-stress and material-strength criterion with an explicitly stated factor | Fatigue, stress concentrations, and stiffness require separate assessment. |
| Fatigue | Use an applicable fatigue method with documented loading spectrum, material data, and design factor | A static strength factor does not establish fatigue life. |
| Motor continuous capability | Investigate a preliminary capability margin of at least 20% against the required continuous operating point where appropriate | Must be checked against torque-speed and thermal limits; a percentage margin alone is insufficient. |
| Gearbox continuous torque | Investigate a preliminary capability margin of at least 20% against required continuous output torque where appropriate | Manufacturer service factors, duty, speed, shock, and life requirements take precedence. |
| Bearing life | Compare calculated life against the approved operating-life requirement, including relevant life adjustments | No universal additional life factor is prescribed by this methodology. |
| Thermal limits | Establish a positive margin to applicable temperature limits under the required duty and ambient conditions | The margin must account for model uncertainty, sensor accuracy, and transient behaviour where relevant. |
| Electrical current and voltage | Maintain documented margin to motor, driver, connector, and supply limits under applicable conditions | Peak and continuous limits must be assessed separately. |

These values are proposed starting points for preliminary feasibility analysis only. They shall not be used as automatic sign-off criteria for safety-critical components.

Where an applicable standard, approved requirement, manufacturer constraint, or safety analysis requires a more stringent approach, that requirement governs.

### 7.3 Margin reporting

For a capacity $C$ and demand $D$, report the relationship explicitly.

Where both quantities are positive and comparable, a capacity-to-demand ratio may be reported as:

$$R = \frac{C}{D}$$

A ratio above 1 indicates that the stated capacity exceeds the stated demand under the assumptions used. It does not, by itself, prove adequate design margin or compliance.

For percentage margin, state the definition used. For example:

$$M = \frac{C-D}{D}\times 100\%$$

Do not compare quantities with different definitions, operating conditions, units, or rating bases.

## 8. Shared Risk Assessment Method

### 8.1 Purpose

All feasibility studies shall use a common 1-to-5 likelihood scale and 1-to-5 severity scale when a structured risk assessment is appropriate.

The scales provide consistent prioritization. They do not replace detailed safety analysis or a formally approved project risk policy.

### 8.2 Likelihood scale

| Score | Label | Guidance |
|---:|---|---|
| 1 | Rare | Unlikely under the defined conditions; credible occurrence is remote. |
| 2 | Unlikely | Could occur, but is not expected during normal intended operation. |
| 3 | Possible | Could occur under foreseeable conditions. |
| 4 | Likely | Expected to occur repeatedly or under common operating conditions. |
| 5 | Almost Certain | Expected to occur frequently or is already being observed. |

Use available evidence, operating history, test data, and documented engineering judgment to assign likelihood.

If evidence is inadequate, state that limitation. Do not imply statistical precision where no supporting data exists.

### 8.3 Severity scale

| Score | Label | Guidance |
|---:|---|---|
| 1 | Negligible | Minimal impact; no meaningful loss of function or injury potential. |
| 2 | Minor | Limited impact, readily recoverable, with minor repair or schedule effect. |
| 3 | Moderate | Significant degradation, repair, or schedule impact; potentially substantial equipment damage. |
| 4 | Major | Major functional failure, substantial damage, serious project impact, or credible serious injury potential. |
| 5 | Critical | Catastrophic equipment or system consequences, fatality potential, or other intolerable safety consequences. |

For safety-related hazards, severity shall be evaluated against the applicable safety process. The qualitative guidance above is not a substitute for formal hazard classification.

### 8.4 Risk score

Calculate the preliminary risk score as:

$$R_{\text{risk}} = L \times S$$

where $L$ is likelihood and $S$ is severity, each scored from 1 to 5.

Use the following proposed bands:

| Score | Proposed category | Expected response |
|---:|---|---|
| 1–4 | Low | Record and manage through routine engineering controls. |
| 5–9 | Moderate | Define mitigation or document why existing controls are adequate. |
| 10–16 | High | Require explicit mitigation, owner, and engineering review before proceeding with affected work. |
| 17–25 | Extreme | Do not proceed with the affected activity until the risk is addressed and the authorized decision-maker approves the disposition. |

These bands are proposed and require approval before being treated as a project-wide risk policy.

### 8.5 Risk acceptance rule

A risk shall not be accepted solely because its numerical score falls below a threshold.

- All risks shall have a documented description and rationale.
- Moderate and higher risks shall have a documented disposition.
- High and extreme risks require explicit engineering review and mitigation or an authorized disposition before proceeding with the affected activity.
- A credible safety-critical hazard shall be escalated through the applicable safety review process regardless of its numerical score.
- Unknown or unverified controls shall not be assumed effective.
- Residual risk shall be recorded after mitigation, with supporting evidence where available.
- Risk acceptance authority shall be identified and shall be appropriate to the risk and applicable project controls.

A feasibility study may identify an unacceptable or unresolved risk. It shall not silently accept that risk to make the design appear feasible.

## 9. Feasibility Conclusion Categories

Each final report shall use one of the following conclusion categories and explain the supporting evidence.

### 9.1 `PROMISING`

Available evidence supports continued investigation or development of the proposed approach within the study's defined scope.

This conclusion does not mean that the design is fully validated or ready for production.

### 9.2 `PROMISING_WITH_CONDITIONS`

The approach appears feasible subject to explicit conditions, unresolved questions, design changes, or additional verification.

The report shall identify the conditions, required actions, responsible roles, and evidence needed to close them.

### 9.3 `FEASIBILITY_NOT_ESTABLISHED`

Available evidence is insufficient to establish feasibility.

Examples include missing duty-cycle data, unknown component limits, incomplete loading information, or an unresolved critical calculation.

This category is appropriate when the study cannot justify either a positive feasibility conclusion or a finding that the approach is infeasible.

### 9.4 `POTENTIALLY_INFEASIBLE`

Available evidence indicates that the proposed approach may not satisfy one or more important constraints without significant changes.

The report shall identify the violated or threatened constraints, supporting evidence, and plausible alternatives or corrective actions where known.

### 9.5 Conclusion versus verification status

The feasibility conclusion shall be reported separately from the verification status.

The permitted verification status values are:

- `NOT_STARTED`
- `IN_PROGRESS`
- `PASS`
- `PASS_WITH_ACTIONS`
- `FAIL`
- `NOT_VERIFIED`

A study may be `PROMISING` while its verification status is `NOT_VERIFIED` because independent review, critical input data, or required evidence is outstanding.

The author shall not claim a verification pass where the defined criteria have not been demonstrated. The author of safety-critical work shall not approve their own work.

## 10. Study Execution Workflow

Use the following workflow for a typical feasibility study.

1. **Define the engineering question.** Establish the objective, scope, constraints, and decision the study must support.
2. **Identify canonical requirements.** Reference applicable `SYS-REQ-nnn` IDs and the relevant requirement revision.
3. **Establish inputs.** Record source, unit, status, and limitations for material inputs.
4. **Record assumptions and unknowns.** Identify uncertainties that could affect the engineering conclusion.
5. **Define load cases and operating conditions.** Include continuous, peak, transient, and exceptional conditions where relevant.
6. **Perform engineering analysis.** Use applicable analytical methods, component data, and models.
7. **Evaluate margins and sensitivity.** Determine whether the conclusion changes under plausible variation in material inputs.
8. **Assess risks and cost.** Identify critical risks, mitigations, cost drivers, and missing evidence.
9. **Prepare the final report.** Summarize results, limitations, conclusion, and recommendations.
10. **Complete technical review.** Address review findings and obtain the required independent review.
11. **Record the decision and status.** Update the study record and any applicable canonical decision register.

The workflow may be adapted to a focused study, provided the required technical checks, traceability, and review controls are maintained.

## 11. Minimum Reporting Expectations

Each study shall report, as applicable:

- Applicable requirement IDs.
- Input values and source status.
- Key assumptions and unknowns.
- Load cases and operating conditions.
- Analysis methods and calculations.
- Component ratings and applicable conditions.
- Results and relevant design margins.
- Sensitivity to uncertain inputs.
- Risks and required mitigations.
- Cost basis and uncertainty where relevant.
- Feasibility conclusion.
- Verification status.
- Outstanding actions and evidence required.
- Required reviewer and approval status.

The report shall explicitly state which checks were completed, which were not applicable, and which remain incomplete.

An incomplete check shall not be represented as passed.

## 12. Methodology Limitations and Change Control

This methodology provides a common preliminary engineering framework. It does not define every design-specific acceptance criterion or replace the need for competent engineering judgment.

Where a relevant standard, approved requirement, manufacturer specification, or safety process imposes stricter criteria, the applicable controlled requirement shall govern.

Proposed safety factors, risk bands, and general analysis conventions in this document shall not be treated as approved design requirements until formally reviewed and approved.

Changes to this methodology shall be version-controlled and reviewed through the applicable repository document-control process.

## 13. Final Principle

A feasibility conclusion must follow from traceable evidence, explicit assumptions, technically appropriate calculations, and an honest treatment of uncertainty.

Where material inputs are unknown, required ratings are unverified, analysis is incomplete, or required independent review has not occurred, the study shall state the limitation and retain the appropriate verification status rather than asserting an unsupported pass.

**End of Document**
