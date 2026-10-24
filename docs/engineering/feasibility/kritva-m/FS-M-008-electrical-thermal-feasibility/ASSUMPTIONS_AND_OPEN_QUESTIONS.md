---
study_id: FS-M-008
title: Electrical and Thermal Feasibility - Assumptions and Open Questions
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Embedded Intern
reviewer: Independent Reviewer TBD
upstream: [FS-M-001, FS-M-002, FS-M-003, FS-M-004, FS-M-007]
downstream: [FS-M-009, FS-M-010]
---

# FS-M-008 Assumptions and Open Questions

## 1. Purpose and ID rules

This file records the assumptions and open questions that affect electrical supply, motor-current demand, controller sizing, feedback, wiring, protection, and thermal feasibility.

Upstream assumptions ASM-001 through ASM-012 and open questions OQ-001 through OQ-014 remain owned by FS-M-001. Verify their exact source wording and status before applying them. Reference upstream IDs in calculations; do not redefine them as local decisions.

Use `FS8-ASM-nnn` for local assumptions and `FS8-OQ-nnn` for local questions. Input data collected or derived for this study uses `FS8-IN-nnn`.

An assumption is not an approved design decision. Any assumption used in a material result requires a rationale, an assessment of sensitivity where appropriate, an owner, and a resolution path. Safety-critical conclusions remain NOT_VERIFIED until the required evidence and independent review are complete.

## 2. Local assumptions register

| Local ID | Assumption / provisional method | Rationale and limitation | Required action |
|---|---|---|---|
| FS8-ASM-001 | Use IN-009's 24 V nominal value as a screening reference only | IN-009 is PRELIMINARY; it does not define the operating or withstand range | Resolve FS8-OQ-001 using SYS-REQ-041 |
| FS8-ASM-002 | Use IN-012's 85% gearbox efficiency only for initial screening | IN-012 is ASSUMED; efficiency may vary with load, speed, temperature, and candidate | Replace or bound using verified FS-M-004 evidence |
| FS8-ASM-003 | Use 15:1, 20:1, and 25:1 (IN-010) for comparative calculations | Ratio candidates are not a selected gearbox or motor decision | Verify FS-M-004 artifacts and recalculate using actual candidate data |
| FS8-ASM-004 | Treat 75-100 W (IN-013) as an initial motor search range only | Nameplate power does not establish continuous torque, peak current, or holding feasibility | Evaluate sourced torque-speed and thermal data |
| FS8-ASM-005 | Use a lumped thermal network for initial desk-study analysis | Useful for screening heat paths and sensitivities, but depends on parameter quality and model boundaries | Document nodes, equations, parameters, limitations, and uncertainty |
| FS8-ASM-006 | Calculate bus current from a clearly defined electrical input power and voltage | `I = P/V` requires consistent power and voltage reference points and a correct loss chain | Document power chain and avoid double-counting losses |
| FS8-ASM-007 | Do not calculate candidate motor current from torque until the torque constant and convention are sourced | Phase/line, peak/RMS, and commutation conventions can materially alter results | Obtain FS8-IN-002 and verify convention compatibility |
| FS8-ASM-008 | Treat continuous horizontal holding as a separate thermal operating point | A stationary motor can draw current and produce copper loss even when mechanical output power is zero | Calculate holding current and winding heating using verified motor data |
| FS8-ASM-009 | Treat peak thermal conclusions as conditional on duration, repetition, initial temperature, and cooling | IN-031 is UNKNOWN; a peak rating cannot be assumed to be continuous | Resolve FS8-OQ-008 before making an unconditional conclusion |
| FS8-ASM-010 | Use sensitivity bounds when ambient or thermal parameters are unknown | Avoids invented precision and identifies parameters dominating the conclusion | Record bounds, sources, and result sensitivity |
| FS8-ASM-011 | Treat output-encoder electrical properties as unspecified beyond IN-034 | The requirement alone does not establish resolution, protocol, bandwidth, or electrical levels | Define interface criteria with FS-M-007 and sourced candidate data |
| FS8-ASM-012 | Do not assume a brake, gravity compensation, active cooling, or a supply that absorbs regenerated energy | These features are not established by the supplied baseline | Resolve relevant architecture questions before feasibility claims |
| FS8-ASM-013 | Treat component ratings as conditional on the manufacturer's specified rating conditions | Ratings may depend on temperature, cooling, PCB copper, switching frequency, and duty | Capture conditions in `references/SOURCE_REGISTER.csv` |
| FS8-ASM-014 | Treat printed polymer thermal suitability as unproven until material and process are identified | Generic glass-transition or heat-deflection values alone do not establish long-term loaded suitability | Obtain material/process evidence and coordinate with FS-M-007 |
| FS8-ASM-015 | Treat MCU/A0 selection as capability criteria definition only | SYS-REQ-055 and SYS-REQ-005 are open items | Verify requirement content; do not select a part in this study |

## 3. Upstream assumptions and questions to preserve

The following upstream records remain authoritative and must be checked in FS-M-001 before use:

- ASM-001 through ASM-012 - upstream assumptions; retain their source wording and status.
- OQ-001 through OQ-014 - upstream open questions; retain their source wording and status.
- IN-012 - gearbox efficiency, ASSUMED.
- IN-014 - motor operating data, UNKNOWN.
- IN-026 - duty cycle and continuous holding duration, UNKNOWN.
- IN-028 - ambient operating temperature, UNKNOWN.
- IN-029 - supply current limit, UNKNOWN.
- IN-031 - peak duration and repetition, UNKNOWN.
- IN-034 - output-side encoder requirement, PRELIMINARY.

Do not copy upstream records into this local register as though FS-M-008 owns or has resolved them. When an analysis depends on an upstream item, cite the upstream ID and describe the effect of its current status.

## 4. Open questions register

| Local ID | Open question | Impact if unresolved | Owner / resolution evidence |
|---|---|---|---|
| FS8-OQ-001 | What are the approved minimum/maximum operating voltage, maximum withstand voltage, and reverse-polarity behaviour, including regeneration? | Supply compatibility and safe bus-voltage conclusions remain blocked | Project Lead; verified SYS-REQ-041 evidence |
| FS8-OQ-002 | What are the supply current limit, transient response, inrush capability, and ability to sink regenerated energy? | Final supply sizing and bus-protection assessment remain blocked | Embedded Intern; sourced supply/bus evidence; IN-029 remains UNKNOWN until resolved |
| FS8-OQ-003 | Which motor candidates and exact FS-M-003 files are authoritative, revision-controlled, and reviewed? | Candidate-specific torque/current/thermal conclusions remain blocked | FS-M-003 owner; repository artifact manifest |
| FS8-OQ-004 | What torque constant, winding resistance, resistance temperature coefficient, efficiency map, and thermal limits apply to each candidate? | Reliable current, copper-loss, derating, and thermal calculations remain blocked or conditional | Embedded Intern; manufacturer datasheets or traceable measurements |
| FS8-OQ-005 | Which phase/line and peak/RMS conventions apply to the torque constant, motor ratings, and controller measurements? | Current calculations and driver sizing may be invalid if conventions are mixed | Embedded Intern; motor/controller documentation |
| FS8-OQ-006 | Which FS-M-002 load cases, acceleration profiles, and operating points apply to each gearbox ratio? | Complete current and loss comparison remains blocked | FS-M-002/FS-M-003 owners; verified artifact revisions |
| FS8-OQ-007 | What continuous duty cycle and horizontal holding duration are required, and what cooling conditions apply? | Unconditional SYS-REQ-012 and SYS-REQ-020 thermal conclusions remain blocked | Project Lead; resolved IN-026 and approved operating profile |
| FS8-OQ-008 | What are peak duration, repetition interval, initial temperature, and recovery conditions? | Peak current and thermal conclusions remain conditional; IN-031 must not be assumed | Project Lead; approved peak operating profile |
| FS8-OQ-009 | What indoor laboratory ambient range applies, and where/how will ambient be measured for later tests? | Ambient-dependent thermal conclusions and test-record definition remain incomplete | Project Lead; SYS-REQ-090 clarification; resolve IN-028 |
| FS8-OQ-010 | What thermal resistances/capacitances connect the winding, motor housing, controller, gearbox, actuator housing, and ambient? | Lumped-model predictions remain conditional or sensitivity-only | Embedded Intern and Mechanical owner; sourced data and FS-M-007 evidence |
| FS8-OQ-011 | What printed housing materials, process parameters, orientation, loaded temperature limits, and creep constraints apply? | Thermal suitability claims for printed components remain blocked | Mechanical owner; FS-M-007 and material/process data |
| FS8-OQ-012 | What motor-feedback and output-encoder interfaces, resolution, bandwidth, supply, and fault behaviour are required? | FOC and encoder interface closure remain blocked | Embedded Intern and Mechanical owner; verified interface specification |
| FS8-OQ-013 | What wiring lengths, cable/connector ratings, allowable voltage drop, grounding, shielding, and EMC constraints apply? | Final interconnect sizing and EMC risk closure remain incomplete | Embedded Intern; approved routing information and sourced ratings |
| FS8-OQ-014 | What protection architecture and safe-state response are required for overcurrent, thermal faults, undervoltage/overvoltage, encoder failure, and emergency stop? | Safety-critical conclusions and powered-test readiness remain NOT_VERIFIED | Project Lead and independent reviewer; approved fault matrix and review record |
| FS8-OQ-015 | What controller power-stage ratings, current-sense range, switching conditions, thermal path, and control-loop timing are required? | Power-stage sizing and MCU/controller criteria remain incomplete | Embedded Intern; sourced design evidence and verified system requirements |
| FS8-OQ-016 | Can the chosen supply and bus architecture safely handle regenerative energy during relevant deceleration and fault conditions? | Bus-overvoltage and fault-response conclusions remain blocked | Embedded Intern; documented energy calculation and independent protection review |
| FS8-OQ-017 | What MCU/A0 board capabilities are mandatory under SYS-REQ-055 and SYS-REQ-005, and what is the status of those requirements? | Premature board selection and incomplete control criteria are risks | Project Lead; verified requirement records; no part selection in this study |
| FS8-OQ-018 | Which source revisions and review statuses apply to the FS-M-002/003/004/007 artifacts used? | Calculations may rely on stale or unapproved operating points/interfaces | Study owner; artifact manifest with commit/revision references |
| FS8-OQ-019 | Who is the independent reviewer for protection/safe-state and thermal-limit conclusions? | Safety-critical conclusions remain NOT_VERIFIED | Project Lead; named independent reviewer and revision-bound review record |
| FS8-OQ-020 | What separate bench procedure, instrumentation, voltage/current limits, thermal sensors, ambient recording, and acceptance criteria will validate the desk-study model? | No empirical thermal or protection verification can be claimed | Project Lead and test owner; separately approved test plan |

## 5. Decision and escalation rules

1. Do not change upstream input values or statuses within FS-M-008. Raise a controlled issue with the owning study or Project Lead.
2. Do not select a motor, driver, MCU, supply, or battery from the screening calculations alone.
3. Register each external numerical value in `references/SOURCE_REGISTER.csv` with its source revision, units, conditions, and exact location.
4. Do not compare current or torque ratings until conventions and operating conditions are reconciled.
5. If duty cycle, ambient, thermal resistance, or peak duration is unknown, state which conclusions are conditional and which are blocked.
6. A lumped thermal model is not proof of measured winding temperature and does not replace a later bench thermal test.
7. SYS-REQ-045 and SYS-REQ-084 apply to later test planning; documentation does not prove protection has been implemented or verified.
8. Independent review is required for protection/safe-state behaviour and thermal-limit conclusions. The study author cannot approve their own safety-critical conclusions.
9. If FS-M-007 geometry, thermal paths, mounting, or material assumptions change, identify affected calculations and repeat them as needed.
10. Carry unresolved questions, evidence gaps, and resulting limitations into the FS-M-009 and FS-M-010 handoffs.

## 6. Must-not-conclude list

Until adequate evidence and required review are complete, this study must not conclude that:

- A 24 V supply or bus architecture is adequate or safe over the full operating range.
- Thermal limits are met.
- Continuous 10 N·m output torque is achievable or thermally sustainable.
- The horizontal holding load can be maintained without overheating.
- A 20-25 N·m peak can be sustained for an unspecified duration.
- Motor nameplate power alone proves torque/current feasibility.
- The controller power stage or current sensing is adequately sized.
- Protection, reverse-polarity handling, regenerative-energy management, or safe-state behaviour has been implemented or verified.
- FOC feedback and output-encoder interfaces are fully specified or validated.
- A printed housing material is thermally or mechanically suitable.
- A specific motor, driver, MCU, development board, supply, or battery is approved.
- Bench testing, EMC compliance, production safety, or life has been demonstrated.

## 7. Review and closure

For every question, record the answer or unresolved disposition, supporting evidence, owner, date, and affected calculations. A verbal statement alone does not close a question. Safety-critical answers require independent review where applicable.

The study author shall not approve their own safety-critical work. Until critical inputs and required review are resolved, the study remains PROPOSED and affected results remain BLOCKED or NOT_VERIFIED.
