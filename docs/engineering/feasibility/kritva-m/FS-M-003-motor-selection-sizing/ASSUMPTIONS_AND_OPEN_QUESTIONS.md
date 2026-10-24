---
study_id: FS-M-003
title: Motor Selection and Sizing - Assumptions and Open Questions
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Project Lead; Independent Reviewer TBD for safety-critical motor peak and thermal checks
upstream_assumptions: ../FS-M-001-integrated-actuator-system/ASSUMPTIONS_AND_OPEN_QUESTIONS.md
upstream_load_source: ../FS-M-002-load-torque-analysis/outputs/LOAD_CASES.csv
---

# FS-M-003 Assumptions and Open Questions

## 1. Rules

This file records study-local assumptions and questions. Upstream FS-M-001 assumptions `ASM-001..ASM-012` and open questions `OQ-001..OQ-014` remain authoritative in FS-M-001 and are referenced by ID only. FS-M-002 outputs are referenced by filename; their load cases and statuses are not redefined here.

- Study-local assumptions use `FS3-ASM-nnn`; questions use `FS3-OQ-nnn`.
- Keep candidate-specific values tied to source evidence.
- Do not invent motor part numbers, ratings, prices, or sourcing claims.
- An assumption is not an approved requirement.
- If a missing input affects a claimed operating point, mark that result incomplete or `NOT_VERIFIED`.

## 2. Study-Local Assumptions Register

| assumption_id | statement | basis | status | impact_if_wrong | validation_action | owner | linked_input | linked_study |
|---|---|---|---|---|---|---|---|---|
| FS3-ASM-001 | The idealized gearbox efficiency for initial motor-side estimates is 85%, inherited from upstream IN-012. | Upstream value is ASSUMED. | ASSUMED | Motor torque and power estimates are wrong if actual efficiency differs by ratio, load or speed. | Obtain candidate gearbox data from FS-M-004 and update each operating point with a justified efficiency model. | Mechanical Intern | FS3-IN-001; FS3-IN-006; IN-012 | FS-M-003; FS-M-004; FS-M-010 |
| FS3-ASM-002 | The 20% motor margin from IN-024 is a proposed screening margin, applied once to the documented continuous sizing basis. | Upstream motor margin is ASSUMED. | ASSUMED | Margin may be insufficient, excessive or double-counted. | Confirm the convention with the Project Lead and document the exact application in calculations. | Mechanical Intern | FS3-IN-010; IN-024 | FS-M-003; FS-M-004; FS-M-010 |
| FS3-ASM-003 | The 75–100 W range is an initial screening range, not proof that a motor in that range meets the load requirements. | IN-013 and SYS-REQ-042. | PRELIMINARY | A candidate may meet nominal power but fail torque-speed, peak, current or thermal requirements. | Evaluate torque-speed curves and required continuous and peak operating points for every candidate. | Mechanical Intern | FS3-IN-003; FS3-IN-006; IN-013 | FS-M-003; FS-M-004; FS-M-008; FS-M-010 |
| FS3-ASM-004 | Motor and gearbox selection are iterated jointly across 15:1, 20:1 and 25:1. | IN-010, IN-011 and dependency on FS-M-004. | PRELIMINARY | A separately chosen motor may become unsuitable when ratio, speed, package or efficiency changes. | Maintain a common candidate/ratio matrix with FS-M-004 and record trade-offs. | Mechanical Intern | FS3-IN-001; FS3-IN-006 | FS-M-003; FS-M-004; FS-M-010 |
| FS3-ASM-005 | Where approved acceleration or duty data are unavailable, illustrative profiles are used for sensitivity only. | IN-026, IN-031 and IN-032 are UNKNOWN. | ASSUMED | Scenario results may be mistaken for requirement-based performance. | Label scenarios in calculations and obtain approved motion and duty definitions before final acceptance. | Mechanical Intern; Project Lead | FS3-IN-005; FS3-IN-006; IN-026; IN-031; IN-032 | FS-M-002; FS-M-003; FS-M-004; FS-M-008 |
| FS3-ASM-006 | Nominal 24 V is used for preliminary voltage screening until the permitted range and regeneration behaviour are defined. | IN-009; SYS-REQ-041 unresolved. | PRELIMINARY | Back-EMF headroom and drive compatibility may be misjudged at actual supply limits. | Obtain the system voltage envelope and drive modulation/regeneration constraints; repeat voltage checks. | Embedded Intern | FS3-IN-009; FS3-IN-014; IN-009 | FS-M-003; FS-M-008; FS-M-010 |
| FS3-ASM-007 | Candidate data are accepted only when supported by an identifiable manufacturer or supplier source; missing data remain UNKNOWN. | Source-control requirement and SYS-REQ-105. | PRELIMINARY | Unsupported specifications could lead to false feasibility or procurement decisions. | Populate the source register; verify exact part number, document revision and applicability. | Mechanical Intern | FS3-IN-002; FS3-IN-003; FS3-IN-004; FS3-IN-008; IN-038 | FS-M-003; FS-M-007; FS-M-009; FS-M-010 |
| FS3-ASM-008 | Candidate continuous ratings are interpreted only under the manufacturer's stated thermal, cooling, mounting and ambient conditions. | Continuous ratings depend on the specified conditions. | PRELIMINARY | Published continuous torque may not be achievable in the integrated actuator. | Record rating conditions and compare with SYS-REQ-090 and proposed thermal integration. | Mechanical Intern; Embedded Intern | FS3-IN-005; FS3-IN-011; IN-028 | FS-M-003; FS-M-007; FS-M-008; FS-M-010 |
| FS3-ASM-009 | Torque-constant and current calculations use the candidate manufacturer's stated electrical and mechanical conventions. | Data may distinguish phase/line, RMS/peak and SI/non-SI definitions. | PRELIMINARY | Current estimates may be wrong due to convention or unit mismatch. | Record the exact definition, conversion and source for each candidate calculation. | Embedded Intern with Mechanical Intern | FS3-IN-004 | FS-M-003; FS-M-008 |
| FS3-ASM-010 | Candidate peak torque is not treated as usable unless duration, repetition, recovery, and thermal and demagnetisation limits are compatible with the load case. | IN-031 and FS-M-002 peak-case dependencies. | PRELIMINARY | A motor may be damaged or unable to meet the required peak duty. | Compare the load case with explicit manufacturer peak limits; obtain missing ratings before acceptance. | Mechanical Intern; Embedded Intern | FS3-IN-005; FS3-IN-006; FS3-IN-015; IN-031 | FS-M-003; FS-M-004; FS-M-008 |
| FS3-ASM-011 | The 15:1, 20:1 and 25:1 motor speed and torque estimates are idealized screening values, not verified candidate operating points. | Ratio arithmetic and provisional IN-012 efficiency. | PRELIMINARY | Candidate sizing may be inaccurate if losses, motor data or load profile differ. | Recalculate using actual load cases, candidate curves and gearbox efficiency data. | Mechanical Intern | FS3-IN-001; FS3-IN-006 | FS-M-003; FS-M-004; FS-M-010 |
| FS3-ASM-012 | Cost and India availability are reported only when supported by dated, traceable supplier or manufacturer evidence. | SYS-REQ-105 and sourcing requirements. | PRELIMINARY | Unsupported price or availability claims may distort the BOM and trade-off. | Record supplier, date, currency, quantity, exclusions and exact part number in the source register and cost estimate. | Mechanical Intern | FS3-IN-008 | FS-M-003; FS-M-009; FS-M-010 |

## 3. Upstream Records to Reference

Do not copy or redefine these records:

- FS-M-001 assumptions: `ASM-001..ASM-012`.
- FS-M-001 open questions: `OQ-001..OQ-014`.
- FS-M-002 outputs: `outputs/LOAD_CASES.csv`, `outputs/DYNAMIC_TORQUE_RESULTS.csv`, `outputs/REFLECTED_INERTIA.csv`.

Relevant dependencies: IN-014 motor data, IN-026 duty cycle, IN-028 ambient, IN-029 current limit, IN-031 peak duration/repetition, IN-032 acceleration profile, IN-035 reflected inertia/backdrivability, IN-038 part numbers, IN-039 motor/ratio estimate. Confirm the actual upstream status before relying on any value. Upstream OQ-002, OQ-003, OQ-007 and OQ-010 are particularly relevant.

## 4. Study-Local Open Questions Register

| question_id | question | why_it_matters | blocking | affected_studies | owner | needed_by | status |
|---|---|---|---|---|---|---|---|
| FS3-OQ-001 | Which FS-M-002 load cases are accepted for continuous/RMS, peak and dynamic motor sizing, and which remain provisional or unverified? | Motor sizing must not use unverified load cases as approved limits. | YES | FS-M-003; FS-M-004; FS-M-008; FS-M-010 | Mechanical Intern; Project Lead for disposition | Before candidate sizing results are accepted | OPEN |
| FS3-OQ-002 | What exact torque-speed curves and continuous ratings are available for shortlisted commercial candidates? | Nameplate power alone cannot show torque at the required speed. | YES | FS-M-003; FS-M-004; FS-M-008; FS-M-010 | Mechanical Intern | Before continuous candidate acceptance | OPEN |
| FS3-OQ-003 | What are each candidate's Kt, Kv, winding resistance, phase/line definitions and RMS/peak conventions? | Current, back-EMF and loss calculations need consistent motor data. | YES | FS-M-003; FS-M-008; FS-M-010 | Mechanical Intern; Embedded Intern | Before candidate current and voltage calculations are accepted | OPEN |
| FS3-OQ-004 | What are the required supply minimum and maximum, transient limits, regeneration behaviour and drive voltage headroom (SYS-REQ-041, upstream OQ-007)? | Nominal 24 V is insufficient to prove voltage compatibility. | YES | FS-M-003; FS-M-008; FS-M-010 | Project Lead; Embedded Intern | Before voltage-compatibility acceptance | OPEN |
| FS3-OQ-005 | What continuous and peak current, peak duration, repetition, recovery and demagnetisation limits apply to each candidate? | Peak and continuous feasibility depend on manufacturer limits and conditions. | YES | FS-M-003; FS-M-004; FS-M-008; FS-M-010 | Mechanical Intern; Embedded Intern | Before peak candidate acceptance | OPEN |
| FS3-OQ-006 | What ambient temperature and cooling path must the integrated motor support (SYS-REQ-090, upstream OQ-010)? | Continuous rating depends on actual installation conditions. | YES | FS-M-003; FS-M-007; FS-M-008; FS-M-010 | Project Lead; Embedded Intern; Mechanical Intern | Before thermal feasibility is accepted | OPEN |
| FS3-OQ-007 | Which feedback device and interface are required for FOC, and what resolution and commutation data are needed? | Motor compatibility depends on feedback and the controller architecture (upstream OQ-008). | PARTIAL | FS-M-003; FS-M-008; FS-M-010 | Embedded Intern | Before motor/drive interface is frozen | OPEN |
| FS3-OQ-008 | Which gearbox ratio and candidate motor/gearbox combination satisfies load, speed, current, package and efficiency constraints together? | Motor selection cannot be finalized independently of FS-M-004. | YES | FS-M-003; FS-M-004; FS-M-007; FS-M-008; FS-M-010 | Mechanical Intern and FS-M-004 owner | Before final candidate recommendation | OPEN |
| FS3-OQ-009 | What exact manufacturer part numbers, dimensions, mass, mounting interfaces and shaft details apply to the leading candidates? | Integration and traceability need exact identities and drawings. | PARTIAL | FS-M-003; FS-M-007; FS-M-009; FS-M-010 | Mechanical Intern | Before packaging and sourcing handoff | OPEN |
| FS3-OQ-010 | What traceable supplier quotations, India availability, lead times and price conditions exist for candidate motors? | Cost comparison cannot rely on guessed or undated prices. | PARTIAL | FS-M-003; FS-M-009; FS-M-010 | Mechanical Intern | Before cost comparison is accepted | OPEN |
| FS3-OQ-011 | What motor rotor inertia and relevant drivetrain inertia data exist for each candidate? | Ratio trade-offs and dynamic response depend on reflected inertia. | PARTIAL | FS-M-003; FS-M-004; FS-M-010 | Mechanical Intern | Before final ratio/candidate trade-off | OPEN |
| FS3-OQ-012 | What power-stage continuous and peak current limits, sensing needs and protection constraints apply? | A motor may be feasible alone but incompatible with the planned drive. | YES | FS-M-003; FS-M-008; FS-M-010 | Embedded Intern | Before drive compatibility is accepted | OPEN |

## 5. Blocking Classification

- `YES`: the affected result or conclusion cannot be accepted until resolved.
- `PARTIAL`: screening may continue with labelled assumptions, but final acceptance stays qualified.
- `NO`: does not block the current stage but still needs ownership and closure evidence.

A blocker applies to the affected conclusion, not necessarily all research or calculations.

## 6. How to Close an Item

### 6.1 Close an assumption

1. Identify the assumption and linked study-local input.
2. Obtain authoritative evidence: datasheet, manufacturer response, requirement decision, verified calculation or integration constraint.
3. Update `inputs/INPUTS.md` and the source register as applicable.
4. Recalculate affected candidates and record downstream impacts.
5. Update the assumption with the evidence and resolution.
6. Obtain the appropriate technical review and record the disposition.

### 6.2 Close an open question

1. Confirm the question, owner and blocking status.
2. Obtain the required data or project decision.
3. Record the answer in the authoritative source and update input and status references.
4. Recalculate affected operating points and compare candidates again.
5. Record evidence in the study calculation, source register or `REVIEW.md`.
6. Change `OPEN` only after the responsible reviewer accepts the resolution.
7. If unresolved, retain the question and document the limitation and next action.

## 7. Maintenance

Review this file when FS-M-002 load cases change, a candidate is added or removed, a manufacturer provides new data, the gearbox ratio changes, or voltage, current or thermal requirements are clarified.

The Mechanical Intern maintains candidate evidence and calculations. The Embedded Intern owns electrical and FOC interface input. The Project Lead resolves system-level questions and reviews the disposition. Communicate changes to FS-M-004, FS-M-007, FS-M-008, FS-M-009 and FS-M-010.
