---
study_id: FS-M-001
title: Integrated Actuator System Feasibility - Inputs
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Project Lead; Independent Reviewer TBD for safety-critical shaft, bearing and stop checks
---

# FS-M-001 Input Register

Maintains the input baseline, source traceability, status classification and limitations for the integrated actuator system feasibility study. Document: `inputs/INPUTS.md`.

## 1. Purpose and rules

This file is the input register for FS-M-001. It records the values used or considered by the study, with provenance and limitations.

The canonical requirements source is [`requirements/SYSTEM_REQUIREMENTS.md`](../../../../../../requirements/SYSTEM_REQUIREMENTS.md), revision 0.2 (KA-REQ-SYS). Refer to requirements by their `SYS-REQ-nnn` identifiers. Do not copy or redefine requirement text here.

All values in the repository requirements baseline are **PROPOSED**. In this register they are mapped to `PRELIMINARY`. This mapping does not approve the requirements.

Allowed status labels:

- `APPROVED` — formally approved through the applicable project process (Project Lead approval recorded in `planning/v1/DECISIONS.md`).
- `PRELIMINARY` — proposed or provisional value, not yet approved.
- `ASSUMED` — working assumption used pending confirmation.
- `UNKNOWN` — value or condition not yet established.
- `MEASURED` — obtained from a documented measurement with method and conditions recorded.

A value may be used in preliminary calculations without being approved. Every material conclusion must disclose the status and limitations of its inputs.

Study abbreviations used in `used_by_study`: FS-M-002 load and torque; FS-M-003 motor; FS-M-004 gearbox; FS-M-005 shaft; FS-M-006 bearings; FS-M-007 housing; FS-M-008 electrical and thermal; FS-M-009 manufacturing and cost; FS-M-010 integrated trade-off.

## 2. Input register

| input_id | parameter | value | unit | status | source | owner | used_by_study | notes |
|---|---|---|---|---|---|---|---|---|
| IN-001 | Forearm and hand mass | 1.5 | kg | PRELIMINARY | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-010 | Mechanical Intern | FS-M-002, FS-M-010 | Confirm mass scope and whether cables, covers and attachments are included. |
| IN-002 | Forearm centre-of-mass distance | 180 | mm | PRELIMINARY | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-010, SYS-REQ-011 | Mechanical Intern | FS-M-002 | Explicitly provisional (SYS-REQ-011). Uncertainty range is UNKNOWN (see IN-027). |
| IN-003 | Payload mass | 1.0 | kg | PRELIMINARY | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-010 | Mechanical Intern | FS-M-002 | Confirm payload definition and whether end-effector mass is included. |
| IN-004 | Payload centre distance | 350 | mm | PRELIMINARY | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-010 | Mechanical Intern | FS-M-002 | Confirm measurement reference and load orientation. |
| IN-005 | Static gravity holding torque (horizontal case) | approx. 6.1 | N·m | PRELIMINARY | Derived from IN-001 to IN-004; SYS-REQ-012 | Mechanical Intern | FS-M-002, FS-M-003 | T_g = 1.5·9.81·0.18 + 1.0·9.81·0.35 ≈ 6.1 N·m. Recalculate and verify. Excludes dynamic, friction and impact contributions. |
| IN-006 | Continuous output torque target | >= 10 | N·m | PRELIMINARY | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-020 | Mechanical Intern | FS-M-003, FS-M-004, FS-M-010 | Proposed target; operating conditions and duty cycle not yet defined. |
| IN-007 | Peak output torque target | 20 minimum; 25 stretch | N·m | PRELIMINARY | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-021 | Mechanical Intern | FS-M-003, FS-M-004, FS-M-005, FS-M-006 | Treat 25 N·m as stretch, not approved. Duration, repetition and recovery are UNKNOWN (see IN-031). |
| IN-008 | Output speed target | 45 | RPM | PRELIMINARY | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-022 | Mechanical Intern | FS-M-003, FS-M-004 | 4.71 rad/s. Confirm whether required simultaneously with continuous torque (marked TBC in SYS-REQ-022). |
| IN-009 | DC supply voltage (nominal) | 24 | V DC | PRELIMINARY | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-040 | Embedded Intern | FS-M-003, FS-M-008 | Allowable range, ripple and regeneration limits are open (SYS-REQ-041). |
| IN-010 | Gearbox ratio candidate set | 15:1, 20:1, 25:1 | ratio | PRELIMINARY | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-004 | Mechanical Intern | FS-M-003, FS-M-004 | Evaluate all three with consistent load cases. |
| IN-011 | First gearbox ratio candidate | 20:1 | ratio | PRELIMINARY | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-004 | Mechanical Intern | FS-M-004 | First evaluation candidate, not a selection. Not frozen until datasheet data are available. |
| IN-012 | Gearbox efficiency | 85 | % | ASSUMED | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-028 | Mechanical Intern | FS-M-003, FS-M-004, FS-M-008 | Preliminary sizing value only. Replace with candidate-specific data; run sensitivity. |
| IN-013 | Motor continuous mechanical output power | 75–100 | W | PRELIMINARY | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-042 | Mechanical Intern | FS-M-003 | Starting candidate range. Power alone does not establish feasibility; check torque-speed point and peak current. |
| IN-014 | Motor operating data (torque-speed, current, resistance, efficiency, thermal limits) | not yet consolidated | n/a | UNKNOWN | SYS-REQ-043; manufacturer datasheets to be collected | Embedded Intern | FS-M-003, FS-M-008 | Collect into FS-M-003 component_research. |
| IN-015 | Output shaft nominal diameter | 12 | mm | PRELIMINARY | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-030 | Mechanical Intern | FS-M-005 | Starting CAD geometry, not a strength guarantee. |
| IN-016 | Bearing arrangement | 6202 on 15 mm seats | designation / mm | ASSUMED | Earlier mechanical concept; SYS-REQ-031, SYS-REQ-032 | Mechanical Intern | FS-M-005, FS-M-006, FS-M-007 | **Interface mismatch flagged:** 6202 has a 15 mm bore; shaft baseline is 12 mm. Define stepped shaft or alternative, fits, shoulders and load path. |
| IN-017 | Arm inertia about elbow axis | 0.171 | kg·m² | PRELIMINARY | Earlier mechanical calculation (point-mass estimate; SYSTEM_REQUIREMENTS section 10) | Mechanical Intern | FS-M-002, FS-M-005 | Verify with CAD mass properties. Derivation located: `mechanical/calculations/LOAD_CASES.md` section 4 (point masses m_a·r_a² + m_p·r_p² = 0.1711 kg·m² about the elbow axis; rod model 0.1873). Includes forearm/hand and payload as point masses; omits centroidal inertia and rotor. Still PRELIMINARY until independently reproduced. |
| IN-018 | Mechanical-stop kinetic energy | approx. 1.9 | J | PRELIMINARY | Earlier estimate; SYSTEM_REQUIREMENTS section 10 | Mechanical Intern | FS-M-002, FS-M-005, FS-M-006 | At 45 RPM. Energy alone does not set stop torque. Derivation located: `mechanical/calculations/LOAD_CASES.md` sections 4 and 8.1 (E = ½·J·ω²; point mass 1.90 J, rod 2.08 J, 2.1–2.8 J with reflected rotor). The 1.90 J point-mass value is illustrative only. |
| IN-019 | Full-speed impact torque estimate | approx. 47.5 | N·m | PRELIMINARY | Earlier impact-load estimate; derivation to be retrieved | Mechanical Intern | FS-M-002, FS-M-005, FS-M-006 | Verify stopping time or distance, compliance and load path. Not an approved design load. Derivation located: `mechanical/calculations/LOAD_CASES.md` section 8 (T = 2E/θ_stop; E = 1.90 J; 2 mm bumper at r_s = 25 mm gives θ = 0.08 rad and 47.5 N·m). Idealised linear-spring screening estimate (section 8.1), not a validated load. Reproduce independently. |
| IN-020 | A0 BOM upper-bound allowance | approx. 22,000 | INR | PRELIMINARY | Earlier preliminary BOM estimate; detail to be linked | Mechanical Intern | FS-M-009 | Exceeds the proposed A0 budget (IN-021). Scope and exclusions need review. |
| IN-021 | A0 budget range | 10,000–15,000 | INR | PRELIMINARY | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-100 | Project Lead | FS-M-009, FS-M-010 | Provisional, not supplier-verified. Confirm inclusions. |
| IN-022 | A1 cumulative budget range | 20,000–30,000 | INR | PRELIMINARY | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-100 | Project Lead | FS-M-009, FS-M-010 | Cumulative per SYS-REQ-100. Confirm treatment of non-recurring costs. |
| IN-023 | Static strength factor target | 1.5 | dimensionless | ASSUMED | Feasibility methodology (proposed) | Project Lead | FS-M-005, FS-M-006, FS-M-007 | Screening target only; not an approved design rule. |
| IN-024 | Motor continuous capability margin | 20 | % | ASSUMED | Feasibility methodology (proposed) | Project Lead | FS-M-003 | Does not replace thermal or duty-cycle verification. |
| IN-025 | Gearbox continuous torque margin | 20 | % | ASSUMED | Feasibility methodology (proposed) | Project Lead | FS-M-004 | Verify rating basis and service conditions. |
| IN-026 | Duty cycle and continuous holding duration | not defined | n/a | UNKNOWN | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-013 | Project Lead | FS-M-002, FS-M-003, FS-M-004, FS-M-006, FS-M-008 | Required before a defensible thermal and life conclusion. |
| IN-027 | Forearm centre-of-mass uncertainty | not defined | mm or range | UNKNOWN | SYS-REQ-011; CAD or measurement required | Mechanical Intern | FS-M-002 | Establish a range for sensitivity analysis. |
| IN-028 | Ambient operating temperature | not defined | °C | UNKNOWN | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-090 | Project Lead | FS-M-003, FS-M-008 | Define minimum, nominal and maximum. |
| IN-029 | Supply current limit | not defined | A | UNKNOWN | Power supply and power stage pending; SYS-REQ-044 | Embedded Intern | FS-M-003, FS-M-008 | Continuous and peak limits, protection and transients. |
| IN-030 | Expected service life | not defined | h | UNKNOWN | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-091 | Project Lead | FS-M-004, FS-M-006 | Required life and operating profile. |
| IN-031 | Peak torque duration and repetition | not defined | s; events per interval | UNKNOWN | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-021 | Project Lead | FS-M-003, FS-M-004, FS-M-005, FS-M-006 | Needed to evaluate peak ratings and thermal recovery. |
| IN-032 | Acceleration profile | not defined | rad/s² | UNKNOWN | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-013 | Project Lead | FS-M-002, FS-M-003 | Needed for dynamic torque. |
| IN-033 | Range of motion | 0 to 120–135 | degrees | PRELIMINARY | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-023 | Mechanical Intern | FS-M-007 | Final range set by arm geometry; define reference position. Joint-angle and torque sign convention: `docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md` section 3 (q = 0 at full extension, positive in flexion). |
| IN-034 | Output-side encoder | required | n/a | PRELIMINARY | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-024, SYS-REQ-034 | Embedded Intern | FS-M-007, FS-M-008 | Resolution, interface and alignment tolerance to be set. |
| IN-035 | Reflected inertia and backdrivability | not quantified | n/a | UNKNOWN | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-027 | Mechanical Intern | FS-M-003, FS-M-004 | Define criteria and compare ratios (reflected inertia scales with N²). |
| IN-036 | Hard-stop load sharing | single-contact case governs provisionally | n/a | ASSUMED | Earlier stop assessment; SYS-REQ-035 | Mechanical Intern | FS-M-005, FS-M-006, FS-M-007 | Do not assume balanced contact until demonstrated. |
| IN-037 | Load-bearing shaft material | EN19 / 42CrMo4 Q&T candidate; EN8 normalised SF approx. 0.86 | grade | PRELIMINARY | Earlier shaft-strength assessment; SYS-REQ-038 | Mechanical Intern | FS-M-005, FS-M-009 | Calculation located: `mechanical/calculations/SHAFT_STRENGTH.md` (12 mm shaft, governing case LC-05: EN8 normalised SF 0.86; EN19/42CrMo4 Q&T SF 2.00). Conditional on assumed geometry, Kt and indicative material data; shaft not frozen. Reproduce independently and review before deciding. |
| IN-038 | Exact BOM part numbers | not established for all components | n/a | UNKNOWN | SYSTEM_REQUIREMENTS rev 0.2, SYS-REQ-105 | Mechanical Intern | FS-M-009 | Do not present generic estimates as a completed BOM. |
| IN-039 | Ratio and motor-type constraint | 20:1 needs a low-Kv pancake motor; about 37:1 suits a typical BLDC | n/a | PRELIMINARY | Earlier mechanical assessment | Mechanical Intern | FS-M-003, FS-M-004 | Carry into the motor and gearbox comparison; verify against datasheets. |

## 3. Input-use rules

1. Record new inputs in this file before relying on them for a material conclusion.
2. If an input changes, update its source, status, value, units and affected calculations.
3. Keep source requirements, assumptions, derived values and measurements distinct.
4. Use explicit units. Do not mix RPM and rad/s, mm and m, or N·mm and N·m without documented conversion.
5. Keep equations in `calculations/`. This file indexes inputs; it does not replace calculation evidence.
6. Link manufacturer evidence through the study's source register when established.
7. If a value cannot be confirmed, keep `UNKNOWN` or `PRELIMINARY` and state the impact. Do not invent values to complete a table.
8. Any input whose uncertainty can change the conclusion needs sensitivity analysis or a documented alternative.

## 4. How to update inputs

1. Confirm the canonical source document and its revision.
2. Add or update the row using the columns `input_id`, `parameter`, `value`, `unit`, `status`, `source`, `owner`, `used_by_study`, `notes`.
3. Keep input IDs stable. Never reuse an ID for a different parameter.
4. Map proposed repository values to `PRELIMINARY`. Use `APPROVED` only with recorded approval evidence.
5. Use `MEASURED` only when method, conditions and evidence are recorded.
6. Update affected calculations and result tables and rerun the relevant checks.
7. Record material changes in the study changelog and update `ASSUMPTIONS_AND_OPEN_QUESTIONS.md` when uncertainty changes.
8. If a changed input affects a safety-critical conclusion, request independent review before marking it verified.
