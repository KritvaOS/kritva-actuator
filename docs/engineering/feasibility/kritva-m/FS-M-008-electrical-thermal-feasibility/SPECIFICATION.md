---
study_id: FS-M-008
title: Electrical and Thermal Feasibility
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Embedded Intern
reviewer: Independent Reviewer TBD
upstream:
- FS-M-001
- FS-M-002
- FS-M-003
- FS-M-004
- FS-M-007
downstream:
- FS-M-009
- FS-M-010
---

# FS-M-008 - Electrical and Thermal Feasibility

## 1. Purpose

Establish a traceable electrical and thermal feasibility assessment for the Kritva-M integrated actuator through a desk study. Evaluate the supply architecture, motor operating points, current demand, controller power-stage requirements, feedback interfaces, wiring, protection, thermal behaviour, continuous holding, peak operation, and mechanical thermal interfaces.

The study shall distinguish verified source data, upstream preliminary inputs, assumptions, calculated results, unresolved questions, and conclusions requiring independent review. It shall identify whether available evidence supports a conclusion or whether missing information blocks it.

This study does not authorize powered testing, select production components, or independently establish that the actuator is feasible or safe.

## 2. Scope

The study includes:

- Electrical power budget and DC bus analysis based on IN-009, including voltage-range and withstand requirements, inrush, brownout, reverse polarity, regeneration, and bus overvoltage handling.
- Motor torque, speed, current, and loss calculations for applicable load cases and the 15:1, 20:1, and 25:1 gearbox ratios.
- Controller power-stage and current-sensing sizing criteria derived from calculated motor-current requirements.
- FOC feedback feasibility, including motor feedback and the output-side encoder required by IN-034.
- Wiring, connectors, cable gauge, voltage drop, grounding, shielding, and EMI considerations.
- Motor copper and iron losses, controller losses, gearbox losses, thermal paths, steady-state temperature, transient response, and sensitivity to unknown parameters.
- Continuous output torque and horizontal-load holding thermal assessments.
- Conditional peak torque/current thermal assessment using explicit peak duration, repetition, initial temperature, and cooling conditions.
- Temperature sensing, thermal derating, printed-housing material constraints, and thermal-path coordination with FS-M-007.
- Protection and safe-state behaviour, including evidence required before controlled bench testing.
- MCU/A0 controller-board capability criteria without selecting a part.

The initial activity is a desk study. A bench thermal/electrical validation activity shall be planned separately.

## 3. Out of scope

The study shall not:

- Select or approve a motor, driver, MCU, development board, supply, or battery without adequate evidence and an authorized decision.
- Invent datasheet values, part numbers, thermal limits, prices, or measured results.
- Treat nominal supply voltage or motor power alone as proof of feasibility.
- Claim protection verification based on analysis or documentation alone.
- Treat a lumped thermal network as measured validation, FEA, or CFD.
- Change upstream input IDs, values, statuses, or decisions.
- Claim EMC compliance, production safety certification, or service life without appropriate evidence.

## 4. Authoritative baseline and traceability

The upstream baseline is `kritva-m/FS-M-001-integrated-actuator-system/`. Preserve all upstream input IDs, values, statuses, and ownership. Verify the authoritative `INPUTS.md` before relying on any upstream record.

Required upstream references include:

- IN-009 - 24 V DC nominal supply, PRELIMINARY.
- IN-012 - gearbox efficiency 85%, ASSUMED.
- IN-014 - motor operating data, including torque-speed, current, resistance, efficiency, and thermal limits, UNKNOWN.
- IN-026 - duty cycle and continuous holding duration, UNKNOWN.
- IN-028 - ambient operating temperature, UNKNOWN.
- IN-029 - supply current limit, UNKNOWN.
- IN-034 - output-side encoder required, PRELIMINARY.

Where present in the upstream `INPUTS.md`, also reference IN-006 (continuous output torque), IN-007 (peak output torque), IN-008 (output speed), IN-013 (motor power range), IN-024 (motor margin), and IN-031 (peak duration/repetition). Verify each ID, exact value, unit, and status before using it. Do not create a substitute upstream record if an expected ID is absent or differs.

Upstream assumptions ASM-001 through ASM-012 and open questions OQ-001 through OQ-014 remain owned by FS-M-001. Reference their exact IDs and verify their wording before application. Local assumptions and questions shall use `FS8-ASM-nnn` and `FS8-OQ-nnn`; local input records shall use `FS8-IN-nnn`.

### Required upstream artifacts

**FS-M-002**

- `outputs/LOAD_CASES.csv`
- `outputs/DYNAMIC_TORQUE_RESULTS.csv`

**FS-M-003**

- Candidate motor data.
- Motor operating points.

The exact filenames for the FS-M-003 artifacts must be verified in the repository. Do not assume filenames or treat a summary as an approved artifact.

**FS-M-004**

- `outputs/GEARBOX_CANDIDATE_MATRIX.csv`
- `outputs/RATIO_OPTIMIZATION.csv`
- `outputs/LOAD_RATING_CHECK.csv`
- `outputs/LIFE_RATING_ASSESSMENT.csv`

**FS-M-007**

- `outputs/INTERFACE_REGISTER.csv`
- `outputs/MASS_ENVELOPE_STATUS.csv`
- `outputs/STRUCTURAL_CHECK.csv`

For each consumed artifact, record the exact repository-relative path, revision or commit, units, review status, provenance, and limitations. If an artifact is absent, stale, incomplete, or unreviewed, record the gap and identify which calculations it blocks.

## 5. Requirements

Record the applicability and evidence status of the following requirements. The descriptions below are the supplied scope statements; do not expand them into invented requirements.

- SYS-REQ-040 - 24 V DC nominal supply.
- SYS-REQ-041 - operating-voltage range, maximum withstand voltage including regeneration, and reverse-polarity behaviour specified in [R3]; TBD.
- SYS-REQ-042 - motor 75-100 W continuous mechanical-output starting range, sufficient continuous torque at calculated motor speed, and peak torque/current for the 20-25 N·m joint peak.
- SYS-REQ-043 - published torque constant or data to derive it, thermal data, 24 V compatibility, and feedback suitable for FOC.
- SYS-REQ-044 - controller power stage and current sensing sized from motor-current requirements, not from 24 V alone.
- SYS-REQ-045 - bench testing on a current-limited DC supply until protection is verified.
- SYS-REQ-020 - continuous output torque ≥10 N·m demonstrated thermally.
- SYS-REQ-012 - hold horizontal load case continuously without exceeding any thermal limit.
- SYS-REQ-084 - initial testing at low voltage with current limiting.
- SYS-REQ-090 - indoor lab ambient, range TBD, recorded in every test record.

Use SYS-REQ-084 and the section 8.7 safety group generically for safety cross-references unless the content of another safety requirement has been verified. Do not infer additional requirement details.

## 6. Analysis method

### 6.1 Supply and power budget

Define the electrical power chain from DC bus through controller and motor to gearbox output. Show the efficiency assumptions at each stage and avoid double-counting losses.

Calculate bus current from the applicable electrical input power and bus voltage using `I = P/V` only when the power quantity, voltage point, and conversion losses are explicitly defined. Account for controller losses, motor losses, transient demand, inrush, and wiring voltage drop where evidence permits.

Evaluate:

- Minimum and maximum operating bus voltage.
- Maximum withstand voltage.
- Reverse-polarity behaviour.
- Inrush and startup transients.
- Brownout and undervoltage behaviour.
- Regenerative energy during deceleration and fault conditions.
- Bus overvoltage clamping, braking, or dissipation strategy.
- Whether the supply can absorb regenerated energy.
- Current limiting and supply transient response.

Voltage limits and clamp thresholds remain TBD until supported by [R3] or other verified, applicable evidence. A 24 V nominal label does not establish supply adequacy.

### 6.2 Motor operating points and current

Use verified FS-M-002 load cases and FS-M-003 motor candidate data. Calculate motor speed, torque, and current for the applicable continuous, peak, acceleration, deceleration, and holding cases for each candidate ratio.

Use a sourced motor torque constant and document its convention. Confirm whether the constant and current ratings refer to phase or line quantities, peak or RMS values, and the relevant commutation/control method. Do not combine incompatible conventions.

Screening references only, based on 85% assumed gearbox efficiency:

| Quantity | Screening value |
|---|---:|
| Output mechanical power at 10 N·m and 45 RPM | Approximately 47 W |
| Idealized motor mechanical power at 85% gearbox efficiency | Approximately 55 W |
| Motor speed at 15:1, 45 RPM output | 675 RPM |
| Motor speed at 20:1, 45 RPM output | 900 RPM |
| Motor speed at 25:1, 45 RPM output | 1125 RPM |
| Motor torque for 10 N·m output at 15:1 | Approximately 0.78 N·m |
| Motor torque for 10 N·m output at 20:1 | Approximately 0.59 N·m |
| Motor torque for 10 N·m output at 25:1 | Approximately 0.47 N·m |
| Motor torque for 25 N·m output at 15:1 | Approximately 1.96 N·m |
| Motor torque for 25 N·m output at 20:1 | Approximately 1.47 N·m |
| Motor torque for 25 N·m output at 25:1 | Approximately 1.18 N·m |

These values are approximate screening calculations, not approved operating points, component ratings, or proof of feasibility. Recalculate with actual ratio, operating speed, losses, motor curves, and the verified load cases. IN-012 remains ASSUMED unless changed through upstream control.

### 6.3 Motor and controller losses

Estimate motor copper loss using a defined current convention and winding resistance. Record the resistance reference temperature and apply a sourced winding-resistance temperature coefficient or explicitly documented approximation. Include iron and other losses where relevant data exists. Missing loss terms must be identified rather than silently treated as zero.

Estimate controller losses using sourced or explicitly parameterized values for MOSFET conduction, switching, current-sense shunt, gate drive, dead time, and relevant bus-capacitor losses. Document PWM frequency, modulation, current ripple, sampling strategy, and thermal interface where known.

Evaluate controller ratings under the expected current, switching conditions, ambient, PCB/thermal configuration, and duty. Do not select a driver from bus voltage or nominal motor wattage alone.

### 6.4 Continuous, holding, and peak operation

Use FS-M-002 to establish applicable load cases and sign conventions. Verify the horizontal-load case and use the approximately 6.1 N·m gravity-torque value only as a screening reference after checking its upstream provenance and applicability.

Assess horizontal holding as a distinct thermal condition. A stationary motor can have zero mechanical output power while still drawing substantial current and generating winding copper loss. Calculate holding current and winding temperature using actual motor data. Do not assume a brake, gravity compensation, active cooling, or a favourable duty cycle unless supported by a recorded decision.

IN-026 and IN-031 are UNKNOWN. Continuous holding conclusions require a defined holding duration, duty cycle, ambient, and cooling condition. Peak thermal conclusions require peak duration, repetition, starting temperature, and recovery conditions. If these are unavailable, present conditional calculations and clearly state the unresolved dependency.

### 6.5 Lumped thermal network

Construct a reproducible thermal-resistance/capacitance model with explicit heat sources and thermal nodes, as applicable:

- Motor winding.
- Motor housing.
- Motor-to-actuator housing interface.
- Controller power devices and PCB.
- Gearbox and gearbox housing.
- Actuator housing and mounting path.
- Ambient.

Use sourced thermal resistance, thermal capacitance, heat generation, and temperature limits wherever available. Record equations, boundary conditions, initial temperatures, ambient assumptions, contact interfaces, and the applicable time constants.

Where parameters are unknown, use sensitivity analysis or explicitly bounded conditional scenarios. Do not invent thermal resistance or capacitance values to force a result. Assess steady-state and transient behaviour separately. Include temperature-dependent winding resistance, thermal derating, sensor placement, sensor response time, and the difference between measured housing temperature and winding hot-spot temperature.

A lumped network is a calculation. FEA or CFD is conditional and requires justification, suitable geometry, material data, and boundary conditions.

### 6.6 Housing and material temperature limits

Coordinate motor/controller mounting, thermal interfaces, and heat paths with FS-M-007. Identify printed polymer components near the motor, controller, and gearbox. Obtain sourced limits for the actual material and process, including applicable glass-transition, heat-deflection, continuous-use, and creep considerations.

Do not treat a generic polymer datasheet value as proof that a printed, loaded part is suitable for sustained service. If material, print process, orientation, enclosure, or operating limit is unknown, keep the conclusion unresolved. Record the required FS-M-007 follow-up.

### 6.7 Feedback, wiring, and EMI

Document FOC feedback criteria, including feedback type, interface, resolution, bandwidth, signal integrity, power requirements, and fault detection. Reconcile the output-side encoder requirement IN-034 with the FS-M-007 mechanical interface. Do not invent encoder resolution, protocol, or electrical levels.

Develop a wiring and interconnect assessment covering:

- DC bus and motor phase currents.
- Cable lengths and conductor resistance.
- Permissible voltage drop.
- Cable gauge, insulation, and temperature rating.
- Connector and terminal current/temperature ratings.
- Strain relief and mechanical routing.
- Grounding, shielding, and return-current paths.
- Switching-noise coupling into feedback signals.
- Relevant EMI risks and unresolved verification needs.

Values must be sourced or clearly marked TBD. A desk assessment does not establish EMC compliance.

### 6.8 Protection and safe-state behaviour

Document the protection architecture and evidence required for overcurrent, overtemperature, undervoltage, overvoltage, reverse polarity, encoder faults, controller faults, and emergency-stop behaviour where applicable. For each fault, describe detection, response, recovery or latching, output behaviour, and unresolved assumptions.

SYS-REQ-045 requires use of a current-limited DC supply until protection is verified. SYS-REQ-084 requires initial testing at low voltage with current limiting. A design review or written fault matrix does not demonstrate that hardware or firmware protection has been implemented or verified.

Independent review is mandatory for protection/safe-state behaviour. The study author must not approve their own safety-critical conclusions.

### 6.9 MCU and A0 board criteria

SYS-REQ-055 and SYS-REQ-005 are open items. Do not select a specific MCU, controller board, or A0 board in this study. Define criteria for evaluation, including PWM/timer capability, ADC and current-sense sampling, FOC loop timing, encoder interfaces, communications, fault handling, memory, debug support, software support, thermal environment, and safe-state implementation.

Verify the exact requirements before treating any criterion as mandatory. Record missing requirement definitions as open questions.

## 7. Evidence and source registration

Every external numerical value must be registered in `references/SOURCE_REGISTER.csv` with supplier/manufacturer, document title, document number or URL, revision/date, relevant page/table/figure, units, access date where applicable, and the exact parameter used.

For every material result, retain the equation, input IDs, unit conversions, efficiency chain, assumptions, source references, and limitations. Distinguish:

- Upstream input.
- Sourced component or material value.
- Calculated value.
- Assumption.
- Estimate or screening result.
- Unknown or unresolved value.

A supplier headline rating without applicable conditions is insufficient for a signoff-critical limit. Preserve conflicting sources and escalate the discrepancy rather than silently selecting the favourable value.

## 8. Deliverables

### 8.1 Mandatory

- `calculations/` - reproducible power, current, torque-speed, loss, thermal-network, voltage-drop, and sensitivity calculations.
- `outputs/` - decision-oriented tables, results, interface assessments, and unresolved-item summaries.
- `references/SOURCE_REGISTER.csv` - traceable source register.

### 8.2 Conditional

- `component_research/` - required only when actual sourced component or material candidate research is performed.
- `simulation/` - required only when justified FEA, CFD, or another simulation beyond a hand-calculated lumped thermal network is performed.
- `cost_estimate/` - conditional; create only if a cost estimate is requested and supported by sourced information.

The lumped RC thermal network is a calculation and belongs in `calculations/`; it does not by itself justify `simulation/`.

### 8.3 Not applicable to this desk study

- `CAD/` - NOT_APPLICABLE. Mechanical geometry ownership remains with FS-M-007.
- `test_data/` - NOT_APPLICABLE for the initial desk study. Bench electrical/thermal validation is a later, separately planned activity with its own reviewed procedure, instrumentation, limits, and acceptance criteria.

Suggested outputs include an artifact manifest, power/current budget, ratio/load-case operating-point table, motor/controller loss budget, thermal-network results, holding/peak thermal assessment, feedback/interface matrix, protection matrix, wiring/voltage-drop assessment, sensitivity analysis, and evidence-gap register. Establish filenames in the study documentation and keep referenced names stable.

## 9. Acceptance criteria

Each criterion requires an evidence pointer and explicit status: PASS, FAIL, BLOCKED, NOT_VERIFIED, or NOT_APPLICABLE. Missing inputs or incomplete review shall not be reported as PASS.

| AC | Criterion |
|---|---|
| AC-001 | All used upstream input IDs, values, units, and statuses are traceable to FS-M-001; local IDs use the FS8 prefix. |
| AC-002 | Required FS-M-002, FS-M-003, FS-M-004, and FS-M-007 artifacts are checked by exact path, revision, units, and review status; missing or unreviewed inputs are identified. |
| AC-003 | The 24 V supply and bus-voltage analysis covers operating range, withstand limits, inrush, brownout, reverse polarity, regeneration, and overvoltage handling; unresolved limits remain explicitly TBD. |
| AC-004 | Power and bus-current budgets show the efficiency chain, load cases, continuous/peak distinction, assumptions, and sensitivity to unknown inputs. |
| AC-005 | Motor torque/current/speed calculations cover applicable ratios and FS-M-002 load cases using sourced motor data or clearly conditional parameters. |
| AC-006 | Copper, motor, gearbox, and controller loss estimates are traceable; missing parameters and current/torque conventions are explicit. |
| AC-007 | Controller power-stage and current-sensing criteria are derived from calculated motor-current needs and documented loss/thermal conditions; no unsupported driver selection is made. |
| AC-008 | FOC feedback and output-encoder interface criteria are documented and reconciled with IN-034 and the relevant mechanical interfaces. |
| AC-009 | Protection and safe-state behaviour are documented with requirements, fault response, evidence gaps, and an independent-review disposition. |
| AC-010 | Wiring, connector, cable-gauge, voltage-drop, grounding, and EMI considerations are documented with sourced or explicitly TBD limits. |
| AC-011 | A reproducible lumped thermal network identifies nodes, heat sources, thermal paths, initial/ambient conditions, parameters, and limitations. |
| AC-012 | Continuous torque and horizontal holding thermal feasibility are evaluated; any unresolved thermal limit, duty cycle, ambient, or motor data blocks an unconditional conclusion. |
| AC-013 | Peak torque/current thermal feasibility is conditional on duration/repetition and starting conditions; IN-031 is not silently assumed. |
| AC-014 | Thermal derating, sensing placement, printed-material temperature/creep risks, and FS-M-007 thermal handoff are addressed. |
| AC-015 | Mandatory deliverables and source registration are complete; conditional simulation/component research and N/A CAD/test-data directories are handled according to this specification. |
| AC-016 | Independent review of protection/safe-state behaviour and thermal-limit conclusions is recorded; author self-approval is prohibited, and unresolved critical items remain NOT_VERIFIED or BLOCKED. |

## 10. Review and approval

The owner prepares the study and assembles the evidence. The reviewer is Independent Reviewer TBD. The Project Lead shall arrange an independent reviewer for protection/safe-state and thermal-limit conclusions.

Record reviewer identity, date, evidence revision, findings, disposition, and any limitations. The author cannot approve their own safety-critical work. Until the required independent review is recorded, affected conclusions remain NOT_VERIFIED.

## 11. Risks and limitations

Key risks include:

- Motor torque constant, winding resistance, efficiency, operating curves, and thermal limits are not yet consolidated.
- Supply operating limits, withstand voltage, transient response, current limit, and regenerative-energy handling remain unresolved.
- Continuous holding duty and peak duration/repetition are unknown.
- Ambient range and thermal interfaces are not established.
- Printed-housing material and process-specific temperature/creep limits may be unavailable.
- Controller ratings depend on actual current, switching conditions, PCB/thermal configuration, and operating temperature.
- Motor feedback and output-encoder interface details may be incomplete.
- Desk-study results cannot replace bench validation.

Numerical precision does not remove uncertainty in the input data.

## 12. Dependencies and handoffs

- **FS-M-001:** authoritative inputs, statuses, and system requirements.
- **FS-M-002:** load cases and dynamic torque results.
- **FS-M-003:** candidate motor data and operating points.
- **FS-M-004:** gearbox candidates, ratios, load ratings, and life assessments.
- **FS-M-007:** mechanical interfaces, mass/envelope status, structural checks, mounting, housing materials, and physical thermal paths.
- **FS-M-009:** manufacturing implications, sourcing constraints, and implementation handoff.
- **FS-M-010:** integrated evidence, risk, and readiness disposition.

Iterate with upstream owners when motor, ratio, mounting, thermal interface, or operating-profile assumptions change. Preserve revision traceability and do not silently overwrite upstream decisions.

## 13. Change control

Changes to motor candidates, gearbox ratios, current conventions, bus limits, controller architecture, thermal parameters, housing material, or duty-cycle assumptions must identify affected calculations, outputs, requirements, and downstream studies.

Retain prior evidence revisions and document why a result changed. New local inputs, assumptions, and questions must use the next available local ID. Upstream values and IDs remain under upstream ownership.

## 14. Status semantics

- **PASS:** evidence demonstrates the criterion under stated conditions using appropriate inputs and required review.
- **FAIL:** evidence demonstrates that the criterion is not met.
- **BLOCKED:** a required input, dependency, or decision is missing.
- **NOT_VERIFIED:** evidence is insufficient or review is incomplete.
- **NOT_APPLICABLE:** the criterion or deliverable does not apply, with a recorded rationale.

PROPOSED is the study lifecycle state and is not an approval or feasibility result.

## 15. Must-not-conclude list

Unless adequate evidence and the required review are available, this study must not conclude that:

- The 24 V supply is adequate or safe over the full operating-voltage range.
- Thermal limits are met.
- Continuous 10 N·m output torque is achievable or thermally sustainable.
- The horizontal holding load can be maintained without overheating.
- Peak torque/current can be sustained for an unspecified duration.
- Motor power rating alone proves torque/current feasibility.
- The controller power stage or current sensing is adequately sized.
- Protection, reverse-polarity handling, regenerative-energy management, or safe-state behaviour is implemented or verified.
- A specific motor, driver, MCU, development board, supply, or battery is approved.
- FOC feedback and output-encoder interfaces are fully specified or validated.
- A printed housing material is thermally or mechanically suitable.
- EMC compliance, production safety, or service life has been demonstrated.

## 16. Safety and test boundary

This is an initial desk study and does not authorize energized testing. Any subsequent bench activity must be planned separately with a reviewed procedure, defined voltage/current limits, suitable instrumentation, emergency-stop arrangements, thermal monitoring, and acceptance criteria.

Apply SYS-REQ-084 for initial low-voltage testing with current limiting. Apply SYS-REQ-045 for current-limited DC supply use until protection is verified. Record indoor lab ambient in each test record in accordance with SYS-REQ-090 once the test activity is planned and the applicable ambient range is established.

## 17. Completion checklist

- [ ] Authoritative upstream inputs and artifact revisions verified.
- [ ] Local input, assumption, and open-question IDs traceable.
- [ ] Power, torque/current, loss, feedback, wiring, and thermal calculations reproducible.
- [ ] Every external numerical value has a source-register entry.
- [ ] Continuous holding and peak cases assessed with explicit limits and conditions.
- [ ] Protection and safe-state behaviour documented and independently reviewed.
- [ ] Thermal-limit conclusions independently reviewed.
- [ ] Mandatory, conditional, and NOT_APPLICABLE deliverables handled as specified.
- [ ] FS-M-007 thermal/interface handoff recorded.
- [ ] FS-M-009 and FS-M-010 handoffs updated.
- [ ] No unsupported component selection, verification, or feasibility claim remains.
