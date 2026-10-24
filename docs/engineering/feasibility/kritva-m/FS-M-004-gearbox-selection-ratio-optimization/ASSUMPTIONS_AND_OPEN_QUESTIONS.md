---
study_id: FS-M-004
title: Gearbox Selection and Ratio Optimization - Assumptions and Open Questions
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Independent Reviewer TBD
upstream:
- FS-M-001
- FS-M-002
- FS-M-003
---

# FS-M-004 Assumptions and Open Questions

## 1. Purpose and Control Rules

Track study-local assumptions and open questions that affect commercial planetary gearbox selection, ratio optimization, load capacity, interfaces and service life.

- Use `FS4-ASM-nnn` for assumptions and `FS4-OQ-nnn` for open questions.
- Reference FS-M-001 ASM-001..ASM-012 and OQ-001..OQ-014 by their existing IDs. Do not redefine them here.
- Reference FS-M-002 and FS-M-003 inputs and outputs by their exact IDs and artifact names.
- An assumption is not a verified engineering fact. A question remains open until its evidence and disposition are recorded.
- Never mark an item resolved merely because a candidate datasheet omits the relevant parameter.
- Link changed assumptions to affected calculations, output rows, acceptance criteria and downstream studies.

## 2. Upstream Assumption and Question References

### FS-M-001

Use `kritva-m/FS-M-001-integrated-actuator-system/ASSUMPTIONS_AND_OPEN_QUESTIONS.md` as the authoritative record for ASM-001..ASM-012 and OQ-001..OQ-014.

Particular attention is required for:

- OQ-002: duty, acceleration and holding requirements (SYS-REQ-013).
- OQ-003: peak duration, repetition and recovery (SYS-REQ-021).
- OQ-009: shock-load assumptions (SYS-REQ-014).
- OQ-012: provenance of the 47.5 N·m impact estimate and approximately 0.86 shaft safety factor.

Also check upstream questions concerning mass properties and center of mass where they affect the FS-M-002 load cases. These are not new FS-M-004 questions; reference the original IDs and use the latest approved evidence.

### FS-M-002

Use the authoritative FS-M-002 `ASSUMPTIONS_AND_OPEN_QUESTIONS.md`, `outputs/LOAD_CASES.csv`, `outputs/DYNAMIC_TORQUE_RESULTS.csv` and `outputs/REFLECTED_INERTIA.csv`. Verify their existence, revisions and review status. The FS-M-004 stop-impact assessment must use the actual load-case definitions, not a copied or assumed torque value.

### FS-M-003

Use the authoritative FS-M-003 motor candidate data and its local assumption/question register. Gearbox input speed, motor torque, current, thermal capability and rotor inertia must be evaluated as a joint motor/gearbox combination. Do not create a separate assumed motor operating envelope if the upstream study has not supplied one.

## 3. Study-Local Assumptions

All entries below are provisional screening assumptions. Change status only when the supporting evidence and disposition are recorded.

| ID | Assumption | Rationale and limitations | Status / closure evidence |
|---|---|---|---|
| FS4-ASM-001 | 20:1 is the initial comparison candidate, not the selected design | Follows upstream IN-011; all primary ratios must be compared | OPEN; joint FS-M-003 comparison |
| FS4-ASM-002 | Compare 15:1, 20:1 and 25:1 on a common set of operating points | Preserves upstream IN-010 comparison basis | OPEN; completed ratio matrix |
| FS4-ASM-003 | Include approximately 37:1 as comparison-only | Motivated by IN-039; not a preferred or approved ratio | OPEN; clearly labelled results |
| FS4-ASM-004 | Use 85% gearbox efficiency for initial sizing where no candidate-specific value is available | Upstream IN-012; actual efficiency depends on model, ratio, speed and load | OPEN; manufacturer evidence or explicit residual limitation |
| FS4-ASM-005 | Apply the 20% gearbox margin as a screening margin | Upstream IN-025; avoid double-counting any existing margin | OPEN; documented margin calculation |
| FS4-ASM-006 | Arm loads bypass gearbox and motor bearings by default | Consistent with SYS-REQ-032 unless explicit ratings support an alternative | OPEN; load-path and support-bearing review |
| FS4-ASM-007 | The output interface should preferably be at least 8 mm | SYS-REQ-033; actual geometry and shaft/bore compatibility must be checked | OPEN; interface drawing review |
| FS4-ASM-008 | A commercial planetary gearbox is the baseline architecture | Consistent with SYS-REQ-003 and the study scope | OPEN; candidate research |
| FS4-ASM-009 | Catalogue ratings are not interchangeable unless rating definitions and conditions match | Prevents invalid comparison of continuous, peak and emergency ratings | OPEN; rating normalization review |
| FS4-ASM-010 | A published maximum torque is not assumed to qualify as emergency-stop capacity | Duration, repetition, speed and shock definition may differ | OPEN; explicit manufacturer evidence and independent review |
| FS4-ASM-011 | Candidate prices and India availability are unconfirmed until sourced | Avoids invented commercial claims | OPEN; dated supplier evidence |
| FS4-ASM-012 | Life suitability cannot be established without the applicable duty and rating basis | IN-026 and IN-030 are UNKNOWN; IN-031 is UNKNOWN | OPEN; duty and life assessment |

These assumptions must not override canonical requirements or upstream input statuses.

## 4. Open Questions

| ID | Question | Why it matters | Closure evidence / owner |
|---|---|---|---|
| FS4-OQ-001 | Which FS-M-002 load-case and dynamic torque output revisions are approved for selection work? | Ratio ranking depends on the authoritative load envelope | Verified artifact paths, revisions and review status; Mechanical Intern |
| FS4-OQ-002 | What continuous/RMS torque and peak operating points must each gearbox support? | Required to distinguish continuous and intermittent ratings | FS-M-002 results reconciled with SYS-REQ-003; Mechanical Intern |
| FS4-OQ-003 | What is the validated stop-impact torque, speed, duration and repetition profile? | A catalogue peak rating may not cover impact loading | FS-M-002 evidence and independent review; Independent Reviewer TBD |
| FS4-OQ-004 | Do shortlisted manufacturers publish an explicit emergency-stop, shock or transient torque rating? | A generic maximum torque does not prove impact survival | Manufacturer documentation or written confirmation; Mechanical Intern |
| FS4-OQ-005 | Which candidate ratios satisfy motor torque-speed and input-speed limits at the required output speed? | Ratio and motor must be selected jointly | FS-M-003 candidate operating-point comparison; Mechanical Intern and motor-study owner |
| FS4-OQ-006 | What are the efficiency curves at the actual speed/load points for each candidate? | The 85% value is an assumption, not verified candidate performance | Model-specific manufacturer curves or documented limitation; Mechanical Intern |
| FS4-OQ-007 | What backlash and measurement conditions apply, and what is the approved SYS-REQ-025 limit? | Position-error acceptability cannot be concluded while the limit is TBD | Canonical requirement disposition and manufacturer data; Project Lead |
| FS4-OQ-008 | What reflected-inertia values and reference convention apply to the gearbox and motor candidates? | Ratio ranking and dynamic response depend on compatible inertia data | FS-M-002 `REFLECTED_INERTIA.csv` plus candidate data; Mechanical Intern |
| FS4-OQ-009 | What backdrivability or friction data are available for the candidates? | Impacts compliance, controllability and power-off behavior | Manufacturer data or a separately authorized measurement plan; Mechanical Intern |
| FS4-OQ-010 | Can the gearbox output bearings carry the calculated radial, axial and tilting loads? | Unsupported arm loads can cause premature failure | Manufacturer load charts checked against calculated loads; Mechanical Intern |
| FS4-OQ-011 | What independent output-bearing arrangement is required to bypass arm loads? | Establishes the mechanical load path and package implications | Interface/load-path review; Mechanical Intern |
| FS4-OQ-012 | How will the gearbox interface reconcile the preferred ≥8 mm interface, IN-015's 12 mm shaft and IN-016's 6202/15 mm seat mismatch? | A nominal diameter alone does not establish mechanical compatibility | Dimensioned drawings, tolerance review and adapter/support decision; Mechanical Intern |
| FS4-OQ-013 | Which candidates meet the life requirement under the eventual duty cycle and load spectrum? | IN-026 and IN-030 remain UNKNOWN | Duty profile, manufacturer life basis and documented calculation; Mechanical Intern |
| FS4-OQ-014 | What peak duration, repetition and recovery interval must the gearbox tolerate? | Determines whether intermittent torque ratings apply | Resolution of IN-031 and applicable FS-M-001 OQ-003; Project Lead |
| FS4-OQ-015 | Which lubrication, mounting orientation and temperature constraints apply? | Affects life, efficiency, maintenance and integration | Candidate manuals compared with SYS-REQ-090; Mechanical Intern |
| FS4-OQ-016 | Are exact models, current prices, lead times and Indian supply channels verifiable? | Supports procurement feasibility without inventing commercial facts | Dated manufacturer/distributor evidence; Mechanical Intern |
| FS4-OQ-017 | Can each candidate be independently replaced without redesigning the motor or actuator housing? | Required by SYS-REQ-036 | Interface drawings, mounting assessment and serviceability review; Mechanical Intern |
| FS4-OQ-018 | Are noise, vibration and torsional compliance adequately characterized for shortlisted gearboxes? | May affect control, perception, durability and product integration | Manufacturer data or a recorded unresolved limitation; Mechanical Intern |
| FS4-OQ-019 | Does the preferred ratio change when efficiency, backlash, inertia, life and interface constraints are considered together? | Avoids selecting by torque multiplication alone | Weighted or gated decision matrix with traceable rationale; Project Lead |
| FS4-OQ-020 | Are the gearbox's continuous, peak and input-speed ratings valid under the actual ambient and mounting conditions? | Catalogue ratings may depend on temperature, lubrication and installation | Model-specific derating guidance and resolved SYS-REQ-090 conditions; Mechanical Intern |
| FS4-OQ-021 | Are gearbox ratings sufficient with the IN-025 margin without double-counting upstream margins? | Prevents misleading overload claims | Auditable load-rating calculations and review; Independent Reviewer TBD |
| FS4-OQ-022 | Which remaining evidence gaps block recommendation versus final design freeze? | Separates feasibility ranking from engineering approval | Explicit blocker list, AC dispositions and review record; Project Lead |

## 5. Decision Rules

1. **Candidate identity:** If the exact model cannot be verified, classify it as an unverified lead, not a qualified candidate.
2. **Continuous torque:** Compare continuous ratings at applicable speed, temperature and duty conditions. Do not use peak ratings as substitutes.
3. **Peak torque:** Record permitted duration, repetition and recovery conditions. If absent, mark applicability UNKNOWN.
4. **Emergency-stop loads:** Require an independently reviewed comparison against FS-M-002 impact cases. Do not infer impact survival from a generic peak torque value.
5. **Input speed:** Verify the required input speed against the candidate's permitted operating range and the selected motor's torque-speed curve.
6. **Efficiency:** Use 85% only as the current sizing assumption. Do not present it as measured or manufacturer-confirmed candidate efficiency.
7. **Backlash:** Record the published value, measurement conditions and unresolved SYS-REQ-025 limit. Do not claim position accuracy is satisfied while the limit remains unresolved.
8. **Reflected inertia:** Preserve the source's reference convention and the FS-M-002 transformation basis.
9. **Bearing loads:** Assume arm loads bypass gearbox and motor bearings unless the manufacturer explicitly rates the relevant bearing configuration for the calculated loads.
10. **Interface:** A shaft diameter, bore or flange dimension alone is insufficient; confirm fits, retention, axial support, load path and replaceability.
11. **Life:** Do not compare life figures without the underlying duty, load, speed, lubrication and rating basis.
12. **Cost and sourcing:** Record dated evidence and currency. Distinguish quotation, published listing and estimate.
13. **Recommendation:** A missing safety-critical rating is a blocker, not a favorable assumption. A provisional shortlist may be produced with explicit limitations.

## 6. Impact and Peak-Load Review Record

Complete these fields when review occurs:

- Reviewer: `Independent Reviewer TBD`
- Review date: `TBD`
- FS-M-002 source revision/commit: `TBD`
- Applicable impact/peak load cases: `TBD`
- Gearbox candidate model and rating source: `TBD`
- Torque, speed, duration and repetition comparison: `TBD`
- Rating applicability and margin disposition: `TBD`
- Findings and required corrective actions: `TBD`
- Review outcome: `PENDING`
- Evidence path / commit: `TBD`

Do not change the outcome to `PASS` or `APPROVED` until the reviewer has examined the evidence and the decision is recorded. Until then the impact/peak conclusions are NOT_VERIFIED.

## 7. Closure and Change Control

For every assumption or question closed, record:

- Evidence file or source-register ID.
- Candidate model and document revision where applicable.
- Affected calculation/output and relevant acceptance criterion.
- Decision, reviewer and date.
- Repository commit containing the change.

If new evidence changes the ratio ranking, load capacity, interface, life assessment or motor compatibility, regenerate the affected outputs and notify the owners of FS-M-005 through FS-M-010 as relevant. Preserve the prior decision history rather than silently overwriting it.

## 8. Must-Not-Conclude Register

Until the evidence and required reviews exist, this study must not conclude that:

- 20:1 is the final or optimal ratio.
- A 37:1 gearbox is preferred merely because a typical high-speed BLDC may need more reduction.
- A candidate's advertised peak torque proves emergency-stop or impact survival.
- The 85% efficiency assumption is verified for a selected gearbox.
- Backlash satisfies SYS-REQ-025 while its limit remains TBD.
- Gearbox or motor bearings can carry arm loads without explicit load ratings.
- The IN-015 shaft and IN-016 bearing-seat arrangement is compatible.
- Required life, duty, thermal behavior, backdrivability or safety has been validated without evidence.
- A part number, price, stock position or supplier lead time is confirmed without a traceable source.
- A feasibility shortlist constitutes design release, production qualification or human-interaction safety approval.
