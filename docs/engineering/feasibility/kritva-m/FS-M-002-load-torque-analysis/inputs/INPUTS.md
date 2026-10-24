---
study_id: FS-M-002
title: Load and Torque Analysis - Study Input Register
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
upstream_input_source: ../../FS-M-001-integrated-actuator-system/inputs/INPUTS.md
canonical_requirements: requirements/SYSTEM_REQUIREMENTS.md
---

# FS-M-002 Study Input Register

## 1. Purpose and Rules

This file records study-local inputs and indexes the upstream FS-M-001 inputs used by FS-M-002.

- Upstream input IDs and their stated values/statuses are authoritative in FS-M-001 `inputs/INPUTS.md`.
- Do not reassign, redefine, or silently change upstream IN IDs.
- Study-local inputs use the `FS2-IN-nnn` namespace.
- Proposed or assumed values are not approved requirements.
- Every calculation must identify its input IDs, units, source, and assumptions.
- If an upstream value changes, update this study's impact assessment and recalculate affected outputs as necessary.

## 2. Section A — Study-Local Inputs

Columns: `input_id, parameter, value, unit, status, source, owner, used_by_study, notes`

| input_id | parameter | value | unit | status | source | owner | used_by_study | notes |
|---|---|---|---|---|---|---|---|---|
| FS2-IN-001 | Gravitational acceleration | 9.80665 | m/s² | ASSUMED | Study calculation convention; confirm against project convention if specified | Mechanical Intern | Static gravity torque; torque cross-check | Study-local assumption, not an upstream IN ID. FS-M-001 IN-005 used 9.81. |
| FS2-IN-002 | Forearm/hand CoM sensitivity | 160, 180, 200 | mm | ASSUMED | IN-002 nominal value with ±20 mm study sensitivity placeholder | Mechanical Intern | Gravity torque sensitivity | The ±20 mm range is not an approved tolerance; confirm using CAD or measurement |
| FS2-IN-003 | Payload-position sensitivity | Nominal 350 mm; exploratory lower/upper bounds TBD | mm | ASSUMED once bounds are selected | IN-004 and documented CAD/configuration rationale | Mechanical Intern | Payload gravity torque sensitivity | Bounds are recorded in FS2-IN-009. Select and document bounds before relying on the result; otherwise mark sensitivity incomplete |
| FS2-IN-004 | Gravity-torque angle sweep | 0 to 135 inclusive, initial increment 1 | degrees | ASSUMED | Study plan and canonical range reference SYS-REQ-023 / IN-033 | Mechanical Intern | Static torque sweep | Confirm angle convention first; refine sweep resolution if required |
| FS2-IN-005 | Illustrative acceleration profiles | TBD; explicit scenarios only if approved profile unavailable | rad/s², rad/s, s | UNKNOWN | IN-032 and OQ-002 | Mechanical Intern; Project Lead for requirement resolution | Dynamic torque, peak and RMS scenarios | Must state speed, acceleration, duration, and motion boundaries; illustrative only |
| FS2-IN-006 | Joint-angle and torque sign convention | 0° = fully extended elbow; positive rotation and torque sign to be explicitly defined against canonical requirement and CAD | degrees; N·m | PRELIMINARY pending reconciliation | `requirements/SYSTEM_REQUIREMENTS.md` section 6, CAD, and OQ-001 / FS2-OQ-001 | Mechanical Intern | All torque calculations | Convention is documented in `docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md` section 3: q = 0 at full extension, positive in flexion; at the horizontal forearm pose with the upper arm vertical (q = 90°) gravity torque is negative and the actuator supplies about +6.08 N·m. Horizontal pose gives maximum gravity torque only for that upper-arm orientation; see FS2-IN-010. Verify the CAD axis before accepting results |
| FS2-IN-007 | Inertia reference and included bodies | TBD; verify whether IN-017 includes forearm, hand, payload, and other moving bodies and identify its axis | kg·m² | UNKNOWN | FS-M-001 IN-017 source calculation/CAD | Mechanical Intern | Dynamic torque; reflected inertia | Source calculation: `mechanical/calculations/LOAD_CASES.md` section 4 (point masses, elbow axis; 0.1711 kg·m², rod model 0.1873). Verify against CAD mass properties and do not use 0.171 kg·m² as fully verified until then |
| FS2-IN-008 | Friction and drivetrain-loss model | TBD; identify included losses and whether model is output-side or motor-side | N·m or model parameters | UNKNOWN | Component datasheets, measurements, or explicitly documented engineering model | Mechanical Intern | Dynamic torque; motor-side demand | Do not silently set losses to zero in final acceptance cases |
| FS2-IN-009 | Payload-position sensitivity bounds | TBD; select and justify around the 350 mm nominal location | mm | UNKNOWN until bounds are justified | IN-004, CAD/configuration constraints | Mechanical Intern | Payload sensitivity | Separates the selected range from the nominal upstream value; record rationale and review |
| FS2-IN-010 | Upper-arm orientation for the gravity sweep | TBD; state the upper-arm angle from vertical used with q = 0..135° | degrees | UNKNOWN | `docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md` section 3; Project Lead for the operating poses | Mechanical Intern; Project Lead | Gravity torque sweep | The documented horizontal pose (q = 90°) assumes a vertical upper arm. Sweep the vertical-upper-arm case first and record it as a stated assumption; other upper-arm orientations are sensitivity cases |
| FS2-IN-011 | Repository reference calculations | `mechanical/common-sizing/actuator_sizing.py` and `expected_results.json`; documents `mechanical/calculations/LOAD_CASES.md` and `TORQUE_AND_SPEED.md` (rev 0.3 / 0.2, draft, pending approval) | n/a | PRELIMINARY | Repository | Mechanical Intern | Cross-check | Reference values only. Recalculate independently first, then compare with the script and record any difference. Repository uses g = 9.81 m/s² (FS2-IN-001 uses 9.80665; about 0.03 % difference). Do not edit the script or expected results from this study |

## 3. Section B — Index of Upstream FS-M-001 Inputs Used

Values and statuses below are references only; the upstream register remains the source of record. All upstream inputs are owned as assigned in FS-M-001.

| input_id | parameter | value | unit | status | used_by_study | notes |
|---|---|---|---|---|---|---|
| IN-001 | Forearm and hand mass | 1.5 | kg | PRELIMINARY | Gravity torque | Upstream ID retained |
| IN-002 | Forearm/hand CoM | 180 | mm | PRELIMINARY | Gravity torque; CoM sensitivity | Sensitivity range is study-local |
| IN-003 | Payload mass | 1.0 | kg | PRELIMINARY | Gravity torque | Upstream ID retained |
| IN-004 | Payload centre distance | 350 | mm | PRELIMINARY | Gravity torque; payload sensitivity | Sensitivity bounds are study-local |
| IN-005 | Gravity torque estimate | about 6.1 | N·m | PRELIMINARY | Static torque cross-check | Recalculate independently |
| IN-006 | Continuous torque target | at least 10 | N·m | PRELIMINARY | Continuous comparison | Not proof of capability |
| IN-007 | Peak torque targets | 20 minimum / 25 stretch | N·m | PRELIMINARY | Peak cases | Peak duration/repetition unresolved |
| IN-008 | Output speed target | 45 | RPM | PRELIMINARY | Motion-profile context | Does not define acceleration |
| IN-010 | Gearbox ratios | 15:1, 20:1, 25:1 | ratio | PRELIMINARY | Reflected inertia | Evaluate all three |
| IN-011 | First gearbox candidate | 20:1 | ratio | PRELIMINARY | Ratio comparison | Candidate only |
| IN-012 | Gearbox efficiency | 85 | % | ASSUMED | Motor-side demand context | Not needed to calculate physical external-load torque |
| IN-014 | Motor data | not yet consolidated | n/a | UNKNOWN | Drivetrain inertia/context | Do not invent motor inertia |
| IN-017 | Arm inertia | 0.171 | kg·m² | PRELIMINARY | Dynamic torque and inertia analysis | Included bodies and reference axis must be confirmed |
| IN-018 | Stop energy | about 1.9 | J | PRELIMINARY | Impact assessment | Derivation in `LOAD_CASES.md` sections 4 and 8.1; reproduce independently. Point-mass value is illustrative; screening range 2.1–2.8 J with reflected rotor |
| IN-019 | Impact torque | about 47.5 | N·m | PRELIMINARY | Impact assessment | Derivation in `LOAD_CASES.md` section 8 (2E/θ_stop, 2 mm bumper at r_s = 25 mm); idealised screening estimate. Unverified until reproduced and independently reviewed |
| IN-026 | Duty cycle | not defined | n/a | UNKNOWN | RMS/continuous analysis | Blocking for duty-based conclusion |
| IN-027 | CoM uncertainty | not defined | mm | UNKNOWN | CoM sensitivity | FS2-IN-002 is a placeholder only |
| IN-031 | Peak duration/repetition | not defined | s | UNKNOWN | Peak analysis | Resolve before final peak conclusion |
| IN-032 | Acceleration profile | not defined | rad/s² | UNKNOWN | Dynamic torque | FS2-IN-005 scenarios are illustrative only |
| IN-033 | Range of motion | 0 to 120–135 | degrees | PRELIMINARY | Gravity sweep | This study sweeps 0–135; confirm final upper limit |
| IN-035 | Reflected inertia/backdrivability | not quantified | n/a | UNKNOWN | Reflected inertia | Verify relevant inertia data and assumptions |
| IN-036 | Hard-stop load sharing | single-contact case governs | n/a | ASSUMED | Stop-impact assessment | Independent review required |
| IN-039 | Ratio/motor-speed estimate | 20:1 needs low-Kv pancake motor; about 37:1 for typical BLDC | n/a | PRELIMINARY | Ratio context | Validate against actual motor data |

Other upstream inputs may be consulted if needed, such as IN-009 (supply context), IN-013 (motor power), IN-023..IN-025 (margins) and IN-029/IN-030 (current and life). Their presence upstream does not make them torque-calculation inputs by default.

## 4. How to Update This Register

1. Add new study-specific assumptions only under `FS2-IN-nnn`; never reuse an upstream IN ID.
2. Assign a unique ID, parameter, value, unit, status, source, owner, and intended use.
3. Use `UNKNOWN` when a value is unavailable. Do not substitute an unsupported numeric value.
4. Use `ASSUMED` for an explicit calculation assumption and `PRELIMINARY` for an estimate or provisional target. Use stronger labels only when supported by evidence.
5. When an upstream value changes, update the index and assess affected calculations and downstream studies.
6. Record changes in the study history/review record and identify output files that need regeneration.
7. Keep input values and units consistent between calculation sheets and CSV outputs.
8. Do not mark a calculation verified solely because the input table has been completed.
