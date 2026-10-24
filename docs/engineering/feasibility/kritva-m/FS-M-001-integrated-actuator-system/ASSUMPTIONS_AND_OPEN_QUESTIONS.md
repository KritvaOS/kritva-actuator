---
study_id: FS-M-001
title: Integrated Actuator System Feasibility - Assumptions and Open Questions
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Project Lead
independent_reviewer: TBD
canonical_requirements: requirements/SYSTEM_REQUIREMENTS.md
inputs_register: inputs/INPUTS.md
---

# Assumptions and Open Questions

**Study ID:** FS-M-001 — Integrated Actuator System Feasibility
**Product:** Kritva-M
**Owner:** Mechanical Intern
**Reviewer:** Project Lead
**Independent reviewer:** TBD (needed for safety-critical shaft, bearing and hard-stop checks)

## 1. Purpose

This file records assumptions used provisionally and questions that must be resolved during FS-M-001.

The registers support traceability between inputs, calculations, component selection, requirements and dependent studies. They do not approve requirements, give design sign-off, or replace the canonical requirements document.

Rules:

- The canonical requirement source is `requirements/SYSTEM_REQUIREMENTS.md` (rev 0.2). Open questions 1–10 below map to its section 12 open items.
- The input source is `inputs/INPUTS.md`. Linked input IDs must exist there.
- Assumptions must not be presented as measured or approved facts.
- Open questions stay `OPEN` until evidence supports closure and the appropriate reviewer accepts the resolution.
- Safety-critical items needing independent review remain `NOT_VERIFIED` until that review is done.
- Never change an assumption or question silently. Record the evidence, update the register and assess impact on calculations and dependent studies.

## 2. Assumptions register

| assumption_id | statement | basis | status | impact_if_wrong | validation_action | owner | linked_input | linked_study |
|---|---|---|---|---|---|---|---|---|
| ASM-001 | Gearbox efficiency is 85% for preliminary calculations. | Initial engineering estimate (SYS-REQ-028); real efficiency depends on design, ratio, speed, load, temperature and lubrication. | ASSUMED | Motor torque, input power, current and thermal loading may be misestimated. | Obtain manufacturer efficiency data at representative operating points; otherwise use measurement or sensitivity analysis. | Mechanical Intern | IN-012 | FS-M-001; FS-M-003; FS-M-004; FS-M-008 |
| ASM-002 | Forearm and hand centre of mass is provisionally 180 mm from the elbow axis. | Preliminary estimate; flagged provisional by SYS-REQ-011. | PRELIMINARY | Gravity torque, joint loading, motor sizing and stop loads change. | Take from CAD mass properties or measurement; verify mass distribution and reference. | Mechanical Intern | IN-002, IN-027 | FS-M-001; FS-M-002; FS-M-003 |
| ASM-003 | A 6202 bearing on 15 mm seats is considered while the independent output shaft is 12 mm. | Preliminary architecture; nominal bore and shaft diameters are inconsistent. | ASSUMED | Bearing may not fit as proposed; needs stepped shaft, sleeve, other bearing or new architecture. | Verify exact bearing part number and dimensions; produce a dimensioned shaft and bearing interface drawing. Do not release the interface before resolving the mismatch. | Mechanical Intern | IN-015, IN-016 | FS-M-001; FS-M-005; FS-M-006 |
| ASM-004 | A single-contact hard-stop case governs until balanced or multi-contact load sharing is demonstrated. | Conservative treatment of uncertain contact and load sharing. | ASSUMED | Stop reaction, local stress, shaft bending, bearing loads and housing strength may be underestimated. | Define stop geometry, contact sequence, tolerances, stiffness and load path; calculate governing cases; obtain independent review. | Mechanical Intern | IN-036 | FS-M-001; FS-M-005; FS-M-006; FS-M-007 |
| ASM-005 | A static strength factor of 1.5 is the preliminary screening target. | Proposed feasibility methodology; suitability depends on material, loading, failure mode and uncertainty. | ASSUMED | Strength margin may be inadequate for the actual load cases. | Document load cases, material properties, failure modes and design basis; obtain reviewer agreement for safety-critical results. | Project Lead | IN-023 | FS-M-001; FS-M-005; FS-M-006; FS-M-007 |
| ASM-006 | A 20% preliminary margin is applied to motor continuous capability. | Proposed sizing allowance; not a manufacturer requirement or validated margin. | ASSUMED | Continuous torque, thermal performance and life may be inadequate. | Compare rated continuous capability against duty cycle, ambient, efficiency and thermal limits; document margin rationale. | Project Lead | IN-024 | FS-M-001; FS-M-003; FS-M-008 |
| ASM-007 | A 20% preliminary margin is applied to gearbox continuous torque rating. | Proposed sizing allowance; rating basis differs by manufacturer. | ASSUMED | Gearbox may be undersized or margin double-counted with other factors. | Confirm the rating basis and service factor; apply margins consistently in calculation sheets and selection tables. | Project Lead | IN-025 | FS-M-001; FS-M-004 |
| ASM-008 | EN19 / 42CrMo4 Q&T is a candidate shaft material because an earlier EN8 normalised calculation gave a safety factor of about 0.86. | Earlier shaft-strength assessment; source calculation and condition not yet verified. | PRELIMINARY | Material selection and shaft size may be wrong if the result or heat-treatment assumptions are wrong. | Retrieve the original calculation, verify loads and units, confirm material properties, recalculate strength and fatigue, obtain independent review. | Mechanical Intern | IN-037 | FS-M-001; FS-M-005 |
| ASM-009 | The nominal supply is 24 V DC. | System-level electrical target (SYS-REQ-040). | PRELIMINARY | Winding selection, drive topology, current, wiring and thermal performance may need revision. | Confirm allowable voltage range, transient limits and available current. | Embedded Intern | IN-009, IN-029 | FS-M-001; FS-M-003; FS-M-008 |
| ASM-010 | The A0 BOM is about ₹22,000 against a proposed A0 budget of ₹10,000–₹15,000. | Earlier component and cost estimate; quotations and scope not confirmed. | PRELIMINARY | Concept may exceed budget or need architecture, sourcing or scope changes. | Produce a line-item BOM with exact part numbers, quantities, quotes, taxes, shipping, machining and explicit exclusions; compare like for like. | Mechanical Intern | IN-020, IN-021 | FS-M-001; FS-M-009; FS-M-010 |
| ASM-011 | A 20:1 ratio needs a low-Kv pancake motor; about 37:1 would suit a typical BLDC motor. | Earlier speed and torque matching assessment; motor data not verified. | PRELIMINARY | Motor may not meet speed and torque together; ratio, form factor, cost and packaging may change. | Calculate motor speed and torque per ratio; screen real torque-speed curves, constants, voltage, current and gearbox limits. Treat 37:1 as a comparison estimate, not a requirement. | Mechanical Intern | IN-039 | FS-M-001; FS-M-003; FS-M-004; FS-M-010 |
| ASM-012 | Requirements marked PROPOSED in the canonical document are treated as PRELIMINARY study inputs until approved. | Configuration-control rule. | PRELIMINARY | Unapproved targets could be mistaken for released constraints. | Check canonical status and revision before use; record approval evidence. Never upgrade a value without an authoritative record. | Project Lead | All applicable IN-nnn | All affected studies |

### 2.1 Assumption status rules

- `ASSUMED`: adopted provisionally for analysis, not yet sufficiently verified.
- `PRELIMINARY`: a provisional estimate, target or result that needs confirmation or formal approval.

These describe the assumption, not the success of a verification. Evidence that contradicts an assumption triggers an impact assessment and updates to inputs, calculations, risks and studies.

## 3. Open questions register

`needed_by` names a stage, not a calendar date. Questions OQ-001 to OQ-010 map one-to-one to SYSTEM_REQUIREMENTS section 12 items 1–10.

| question_id | question | why_it_matters | blocking | affected_studies | owner | needed_by | status |
|---|---|---|---|---|---|---|---|
| OQ-001 | **SYS-REQ-011:** What is the measured or CAD-derived forearm and hand centre of mass (replacing the 180 mm assumption), with reference axis and uncertainty? | Gravity torque and the elbow load case depend on mass distribution. | PARTIAL | FS-M-001; FS-M-002; FS-M-003 | Mechanical Intern | Gate A | OPEN |
| OQ-002 | **SYS-REQ-013:** What are the required angular acceleration, motion duty cycle and continuous horizontal holding duration? | Sets RMS torque, peak demand, thermal sizing, motor selection and gearbox life. | YES | FS-M-001; FS-M-002; FS-M-003; FS-M-004; FS-M-008 | Project Lead | Before motor and gearbox freeze | OPEN |
| OQ-003 | **SYS-REQ-021:** What are the peak-torque duration, repetition rate and recovery period, which of 20 or 25 N·m is adopted, and how will compliance be demonstrated? | A peak value alone does not establish motor, gearbox, shaft or thermal capability. | YES | FS-M-001; FS-M-002; FS-M-003; FS-M-004; FS-M-005; FS-M-006; FS-M-008 | Project Lead | Before motor and gearbox freeze | OPEN |
| OQ-004 | **SYS-REQ-004:** What is the final gearbox ratio (20:1 versus 15:1 or 25:1) and the selection criteria? | Constrains motor speed, torque, efficiency, packaging and cost. | PARTIAL | FS-M-001; FS-M-003; FS-M-004; FS-M-010 | Mechanical Intern with Embedded Intern | After datasheet comparison | OPEN |
| OQ-005 | **SYS-REQ-025:** What are the numerical limits for position error, repeatability and backlash? | Acceptance must use pre-agreed limits; backlash also affects ratio and gearbox choice. | PARTIAL | FS-M-001; FS-M-004; FS-M-010 | Project Lead | Before Gate B testing | OPEN |
| OQ-006 | **SYS-REQ-039:** What are the actuator mass and envelope budgets, and which interfaces are fixed? | Motor, gearbox, bearing, housing and connector choices depend on volume and mass. | PARTIAL | FS-M-001; FS-M-003; FS-M-004; FS-M-005; FS-M-006; FS-M-007; FS-M-009 | Project Lead with Mechanical Intern | Gate A | OPEN |
| OQ-007 | **SYS-REQ-041:** What are the operating voltage range, maximum withstand voltage (including regeneration) and reverse-polarity behaviour? | Affects motor winding choice, drive design, protection and thermal results. | PARTIAL | FS-M-001; FS-M-003; FS-M-008 | Embedded Intern | A1 PCB start | OPEN |
| OQ-008 | **SYS-REQ-055 / SYS-REQ-005:** Which MCU family and A0 development board are selected? | Determines control architecture, sensing interfaces and PWM and current-control capability. | PARTIAL | FS-M-001; FS-M-003; FS-M-008; FS-M-010 | Embedded Intern | A0 start | OPEN |
| OQ-009 | **SYS-REQ-014:** Is a shock-load specification needed, and if so what impact cases (magnitude, direction, duration, repetition) apply? | Impact loading can govern shaft, bearing, stop, housing and gearbox survivability. | YES | FS-M-001; FS-M-002; FS-M-005; FS-M-006; FS-M-007 | Project Lead with Mechanical Intern | Gate A | OPEN |
| OQ-010 | **SYS-REQ-090:** What is the reference ambient temperature range? | Motor, gearbox, bearing, lubricant, encoder and electronics ratings depend on it. | PARTIAL | FS-M-001; FS-M-003; FS-M-004; FS-M-006; FS-M-008 | Project Lead | Gate B | OPEN |
| OQ-011 | How will a 6202 bearing with a nominal 15 mm bore interface with the 12 mm shaft baseline? | A compatible shaft and bearing interface and load path must be established. | YES | FS-M-001; FS-M-005; FS-M-006; FS-M-007 | Mechanical Intern | Before shaft and bearing architecture is frozen | OPEN |
| OQ-012 | What are the source files, equations, units, load cases, material properties and boundary conditions behind the approximately 47.5 N·m impact torque and the EN8 safety factor of about 0.86? Progress: sources located in `mechanical/calculations/LOAD_CASES.md` section 8 (impact) and `mechanical/calculations/SHAFT_STRENGTH.md` (EN8 factor). Remaining: independent reproduction and review. | These results drive stop, shaft and material decisions but cannot be accepted without reproducible derivations. | YES | FS-M-001; FS-M-002; FS-M-005; FS-M-006; FS-M-007 | Mechanical Intern; Independent Reviewer for safety-critical results | Before either value is used for acceptance | OPEN |
| OQ-013 | What exact manufacturer part numbers and revisions apply to the motor, gearbox, bearings, encoder, controller and other costed items? | Without part numbers, dimensions, ratings, cost and availability cannot be confirmed (SYS-REQ-105). | PARTIAL | FS-M-001; FS-M-003; FS-M-004; FS-M-006; FS-M-008; FS-M-009; FS-M-010 | Mechanical Intern; Embedded Intern for electronics | Before component shortlist and BOM are accepted | OPEN |
| OQ-014 | Who is the named independent reviewer for the safety-critical shaft, bearing and hard-stop calculations? | Independent review cannot be shown without an identified reviewer and recorded evidence (SYS-REQ-106). | YES | FS-M-001; FS-M-005; FS-M-006; FS-M-007 | Project Lead | Before safety-critical results are submitted | OPEN |

### 3.1 Blocking definitions

- `YES`: prevents the affected conclusion or design decision from being accepted. Unrelated work may continue; the blocked conclusion stays open or `NOT_VERIFIED`.
- `PARTIAL`: preliminary work may proceed on a recorded assumption or bounded scenario. The affected conclusion keeps its limitations until resolved.
- `NO`: does not block the current stage but still needs an owner, resolution path and closure evidence.

A blocking classification applies to the affected conclusion, not to every task in every linked study.

## 4. How to close an item

### 4.1 Closing an assumption

1. Identify the assumption and its linked input IDs.
2. Obtain evidence: approved requirement, datasheet, quotation, calculation, CAD mass-properties report, measurement or test.
3. Update `inputs/INPUTS.md` with the verified value, source, status and revision.
4. Recalculate affected results and assess impact on dependent studies, risks and decisions.
5. Update this register with the validation action and evidence reference. If the assumption is no longer needed, record it as retired and why.
6. Obtain the appropriate review. Safety-critical calculations need independent review.
7. Make sure the study conclusion reflects the evidence and remaining limitations.

A completed calculation does not make a value `APPROVED`. Requirement approval is recorded in the canonical requirements process.

### 4.2 Closing an open question

1. Confirm the requirement mapping and current owner.
2. Gather the decision, measurement, calculation, supplier evidence or approved requirement update.
3. Record the answer and evidence in the authoritative location and update the canonical requirement or input register if applicable.
4. Assess impact on every affected study and repeat verification where needed.
5. Link the resolution evidence on the question row. Keep the question visible in history.
6. Change status from `OPEN` only after the responsible reviewer accepts the resolution, and record the decision in `registers/DECISION_REGISTER.csv`.
7. If it cannot be resolved, document the limitation, decision-maker, mitigation and whether the conclusion stays blocked.

### 4.3 Evidence and traceability

Use repository-relative paths and stable IDs. Typical locations: `inputs/INPUTS.md`, `calculations/`, `component_research/`, `CAD/`, `cost_estimate/`, `REVIEW.md` and `registers/DECISION_REGISTER.csv`. Use only evidence files that exist. Never invent a review record, approval, measurement, supplier confirmation or closure date.

## 5. Review and maintenance

Review this file whenever a canonical requirement changes, an input changes or gains stronger evidence, a calculation or selection exposes a new uncertainty, a dependent study finds an interface conflict, a safety-critical result is revised, or the study is submitted for review.

The Project Lead ensures ownership and cross-study impacts are addressed. The technical owner maintains evidence and technical updates. Independent safety review stays separate from authorship and must be recorded before safety-critical work is accepted.
