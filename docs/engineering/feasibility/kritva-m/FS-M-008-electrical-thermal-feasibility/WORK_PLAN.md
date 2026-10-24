---
study_id: FS-M-008
title: Electrical and Thermal Feasibility - Work Plan
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Embedded Intern
reviewer: Independent Reviewer TBD
priority: P2
upstream: [FS-M-001, FS-M-002, FS-M-003, FS-M-004, FS-M-007]
downstream: [FS-M-009, FS-M-010]
specification: SPECIFICATION.md
inputs: inputs/INPUTS.md
assumptions_and_open_questions: ASSUMPTIONS_AND_OPEN_QUESTIONS.md
---

# FS-M-008 Work Plan

## 1. Objective

Deliver a traceable electrical and thermal desk study covering the supply, motor-current demand, controller sizing criteria, feedback, wiring, protection, and thermal feasibility of Kritva-M. Produce reproducible calculations and decision-oriented outputs, document evidence gaps, and obtain independent review of protection/safe-state behaviour and thermal-limit conclusions.

This plan is governed by `SPECIFICATION.md`. AC-001 through AC-016 below shall match the specification in ID and intent. A document's existence alone is not evidence that its criterion has passed.

## 2. Roles and responsibilities

- **Owner - Embedded Intern:** verify input records and source data, perform calculations, maintain local registers, prepare outputs, record limitations, and coordinate the handoff.
- **Reviewer - Independent Reviewer TBD:** independently review protection/safe-state behaviour and thermal-limit conclusions.
- **Project Lead:** resolve system-level decisions, assign an independent reviewer, and coordinate downstream acceptance.
- **Mechanical owner:** supply verified FS-M-007 interfaces, mounting information, housing material/process information, and thermal paths.
- **Upstream study owners:** confirm source artifact revisions, units, statuses, and interpretation.

The study author cannot approve their own safety-critical work. If independent review is incomplete, applicable conclusions remain NOT_VERIFIED.

## 3. Work breakdown

| Task | Activity | Required evidence | Exit condition |
|---|---|---|---|
| WP-01 | Verify authoritative baseline | Input traceability table; requirement applicability | IDs, values, units, statuses, and source revisions checked |
| WP-02 | Verify upstream artifacts | Artifact manifest with exact path, revision, units, and review status | Missing, stale, or unreviewed inputs logged |
| WP-03 | Define supply envelope | Bus-voltage and current-budget analysis | Unknown limits explicit; no invented voltage/current ratings |
| WP-04 | Calculate motor operating points | Ratio/load-case speed, torque, and current tables | Candidate data and current conventions sourced or results conditional |
| WP-05 | Estimate losses | Motor, gearbox, and controller loss budget | Parameters traceable; omissions and sensitivities documented |
| WP-06 | Assess power stage and feedback | Controller sizing criteria; FOC and encoder interface matrix | Criteria based on actual current needs; no unsupported part selection |
| WP-07 | Assess protection and safe state | Fault matrix, response descriptions, review package | Independent review completed or status remains NOT_VERIFIED |
| WP-08 | Build thermal model | Lumped network, equations, source data, transient/steady results | Parameters and limitations documented; missing data blocks unconditional conclusions |
| WP-09 | Assess holding, peak, and material constraints | Thermal assessment and FS-M-007 handoff | IN-026, IN-028, IN-031, and material unknowns explicitly handled |
| WP-10 | Assess wiring and EMI | Interconnect, voltage-drop, and EMI risk assessment | Ratings sourced or marked TBD |
| WP-11 | Consolidate study outputs | Calculations, outputs, source register, status matrix | Mandatory deliverables complete and referenced |
| WP-12 | Review and hand off | Independent review record, findings, downstream updates | No author self-approval; unresolved issues remain visible |

## 4. Required directory structure

Mandatory:

- `calculations/` - reproducible power, current, torque-speed, loss, lumped thermal, voltage-drop, and sensitivity calculations.
- `outputs/` - result tables, decision records, status summaries, and evidence gaps.
- `references/SOURCE_REGISTER.csv` - traceable external source register.

Conditional:

- `component_research/` - only when sourced component/material candidate research is performed.
- `simulation/` - only for justified FEA/CFD or another simulation beyond a hand-calculated lumped thermal network.
- `cost_estimate/` - only if a cost estimate is requested and supported by sources.

Not applicable to this initial desk study:

- `CAD/` - NOT_APPLICABLE; mechanical geometry remains under FS-M-007.
- `test_data/` - NOT_APPLICABLE; bench electrical/thermal validation is a later, separately planned activity.

A lumped RC thermal model is a calculation and belongs in `calculations/`; it does not alone require `simulation/`.

## 5. Work sequence and gates

### Gate A - Input and artifact integrity

Verify `kritva-m/FS-M-001-integrated-actuator-system/` and the required FS-M-002, FS-M-003, FS-M-004, and FS-M-007 artifacts. Record exact paths and revisions. Discover the actual FS-M-003 candidate motor and operating-point filenames in the repository; do not guess. Confirm that the consumed outputs have appropriate units and review status.

Reference upstream ASM-001 through ASM-012 and OQ-001 through OQ-014 by ID after checking their exact source wording. Do not redefine or silently resolve them.

### Gate B - Supply and motor operating points

Define the bus-voltage envelope and current budget. Calculate speed, torque, and current for relevant ratios and load cases. Confirm torque-constant and current conventions before comparing results with candidate ratings.

Keep calculations conditional if motor data, voltage limits, supply current limits, or load cases are missing. Treat the 75-100 W range and approximate ratio calculations as screening references, not evidence of feasibility.

### Gate C - Losses and controller criteria

Calculate motor copper loss, other motor losses where data permits, gearbox losses, and controller losses. Derive power-stage, current-sensing, bus-capacitance, and thermal criteria from the calculated electrical operating points. Do not select a specific driver or MCU.

### Gate D - Thermal model

Construct a lumped thermal network with defined nodes, heat sources, thermal paths, initial conditions, and ambient assumptions. Assess continuous operation, horizontal holding, and transient peak cases separately. Run sensitivity analyses for material unknowns and record when missing parameters prevent an unconditional conclusion.

Coordinate mounting, heat transfer, printed material, and temperature constraints with FS-M-007. Do not use a generic polymer temperature rating as proof of suitability for a particular printed component.

### Gate E - Protection and safe-state review

Prepare the fault matrix and document overcurrent, overtemperature, voltage faults, encoder faults, and emergency-stop behaviour where applicable. Record detection, response, recovery/latching, output behaviour, and unresolved decisions.

Respect SYS-REQ-045 and SYS-REQ-084 for later test planning. Documentation is not proof of implemented protection. Obtain independent review of safety-critical conclusions.

### Gate F - Final evidence and handoff

Complete mandatory deliverables, register sources, and cross-link each acceptance criterion to evidence. Record the disposition of missing inputs and open questions. Provide FS-M-009 and FS-M-010 with the current findings, risks, limitations, and review status.

## 6. Acceptance criteria

The following table matches `SPECIFICATION.md`. The initial status for every criterion is NOT_VERIFIED until its evidence and review conditions are satisfied.

| AC | Acceptance criterion | Evidence required | Initial status |
|---|---|---|---|
| AC-001 | All used upstream input IDs, values, units, and statuses are traceable to FS-M-001; local IDs use the FS8 prefix. | Traceability table and local input register | NOT_VERIFIED |
| AC-002 | Required FS-M-002, FS-M-003, FS-M-004, and FS-M-007 artifacts are checked by exact path, revision, units, and review status; missing or unreviewed inputs are identified. | Upstream artifact manifest | NOT_VERIFIED |
| AC-003 | The 24 V supply and bus-voltage analysis covers operating range, withstand limits, inrush, brownout, reverse polarity, regeneration, and overvoltage handling; unresolved limits remain explicitly TBD. | Voltage envelope and bus analysis | NOT_VERIFIED |
| AC-004 | Power and bus-current budgets show the efficiency chain, load cases, continuous/peak distinction, assumptions, and sensitivity to unknown inputs. | Reproducible power/current budget | NOT_VERIFIED |
| AC-005 | Motor torque/current/speed calculations cover applicable ratios and FS-M-002 load cases using sourced motor data or clearly conditional parameters. | Ratio/load-case calculations | NOT_VERIFIED |
| AC-006 | Copper, motor, gearbox, and controller loss estimates are traceable; missing parameters and current/torque conventions are explicit. | Loss model and source links | NOT_VERIFIED |
| AC-007 | Controller power-stage and current-sensing criteria are derived from calculated motor-current needs and documented loss/thermal conditions; no unsupported driver selection is made. | Power-stage and sensing assessment | NOT_VERIFIED |
| AC-008 | FOC feedback and output-encoder interface criteria are documented and reconciled with IN-034 and the relevant mechanical interfaces. | Feedback/interface matrix | NOT_VERIFIED |
| AC-009 | Protection and safe-state behaviour are documented with requirements, fault response, evidence gaps, and an independent-review disposition. | Protection matrix and independent review record | NOT_VERIFIED |
| AC-010 | Wiring, connector, cable-gauge, voltage-drop, grounding, and EMI considerations are documented with sourced or explicitly TBD limits. | Wiring and voltage-drop assessment | NOT_VERIFIED |
| AC-011 | A reproducible lumped thermal network identifies nodes, heat sources, thermal paths, initial/ambient conditions, parameters, and limitations. | Thermal model and calculation record | NOT_VERIFIED |
| AC-012 | Continuous torque and horizontal holding thermal feasibility are evaluated; any unresolved thermal limit, duty cycle, ambient, or motor data blocks an unconditional conclusion. | Holding/continuous thermal results and blockers | NOT_VERIFIED |
| AC-013 | Peak torque/current thermal feasibility is conditional on duration/repetition and starting conditions; IN-031 is not silently assumed. | Peak transient assessment and explicit conditions | NOT_VERIFIED |
| AC-014 | Thermal derating, sensing placement, printed-material temperature/creep risks, and FS-M-007 thermal handoff are addressed. | Thermal-management and mechanical handoff record | NOT_VERIFIED |
| AC-015 | Mandatory deliverables and source registration are complete; conditional simulation/component research and N/A CAD/test-data directories are handled according to this specification. | Directory audit and source register | NOT_VERIFIED |
| AC-016 | Independent review of protection/safe-state behaviour and thermal-limit conclusions is recorded; author self-approval is prohibited, and unresolved critical items remain NOT_VERIFIED or BLOCKED. | Revision-bound independent review record | NOT_VERIFIED |

## 7. Reporting and change control

Every output shall identify the calculation revision, input revision, units, operating conditions, assumptions, and limitations. Distinguish source data from calculated values and assumptions. When an input or candidate changes, identify and rerun affected calculations. Do not overwrite upstream decisions.

Record findings as PASS, FAIL, BLOCKED, NOT_VERIFIED, or NOT_APPLICABLE, with an evidence pointer and rationale. A missing input is a blocker where it prevents a valid conclusion, not a reason to choose a favourable default.

## 8. Completion checklist

- [ ] Upstream artifact paths, revisions, units, and review statuses checked.
- [ ] All used upstream inputs and local IDs traceable.
- [ ] Electrical, current, loss, feedback, wiring, and thermal calculations reproducible.
- [ ] Every external numerical value registered in `references/SOURCE_REGISTER.csv`.
- [ ] Continuous holding and peak cases assessed with explicit limits and conditions.
- [ ] Protection/safe-state and thermal-limit conclusions independently reviewed.
- [ ] Mandatory, conditional, and NOT_APPLICABLE deliverables handled correctly.
- [ ] FS-M-007 thermal/interface handoff recorded.
- [ ] FS-M-009 and FS-M-010 handoffs updated.
- [ ] No unsupported component selection or feasibility claim remains.
