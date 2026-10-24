---
study_id: FS-M-008
title: Electrical and Thermal Feasibility - Inputs
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Embedded Intern
reviewer: Independent Reviewer TBD
upstream: [FS-M-001, FS-M-002, FS-M-003, FS-M-004, FS-M-007]
downstream: [FS-M-009, FS-M-010]
---

# FS-M-008 Inputs Register

## 1. Purpose and rules

This register identifies upstream baseline inputs, required study artifacts, and additional electrical/thermal data needed for the feasibility assessment.

Upstream IDs, values, and statuses remain authoritative in their source study. Local inputs use `FS8-IN-nnn`, assumptions use `FS8-ASM-nnn`, and open questions use `FS8-OQ-nnn`. Do not reassign an upstream ID or change its status in this study.

Before using any value, verify the exact upstream record, units, source revision, and applicability. An expected filename is not proof that an artifact exists or is approved. Missing or unreviewed evidence must be recorded as a blocker.

## 2. Section A - Upstream baseline inputs

Authoritative path: `kritva-m/FS-M-001-integrated-actuator-system/`. IDs, values and statuses below were checked against FS-M-001 `inputs/INPUTS.md`.

| Upstream ID | Input | Baseline value/status | Use and limitation |
|---|---|---|---|
| IN-006 | Continuous output torque target | >= 10 N·m; PRELIMINARY | Operating conditions and duty cycle remain open |
| IN-007 | Peak output torque target | 20 N·m minimum / 25 N·m stretch; PRELIMINARY | Peak operating point; duration/repetition unresolved (IN-031) |
| IN-008 | Output speed target | 45 RPM; PRELIMINARY | Confirm whether required simultaneously with continuous torque |
| IN-009 | DC supply voltage (nominal) | 24 V DC; PRELIMINARY | Nominal reference only; range, ripple, regeneration limits open (SYS-REQ-041) |
| IN-012 | Gearbox efficiency | 85 %; ASSUMED | Screening only; actual efficiency varies with load, speed, temperature, candidate |
| IN-013 | Motor continuous mechanical output power | 75-100 W; PRELIMINARY | Starting search range, not proof of motor suitability |
| IN-014 | Motor operating data (torque-speed, current, resistance, efficiency, thermal limits) | not yet consolidated; UNKNOWN | Critical blocker for unconditional current, loss, and thermal conclusions |
| IN-024 | Motor continuous capability margin | 20 %; ASSUMED | Does not replace thermal or duty-cycle verification |
| IN-026 | Duty cycle and continuous holding duration | not defined; UNKNOWN | Blocks unconditional continuous/holding thermal conclusion |
| IN-028 | Ambient operating temperature | not defined; UNKNOWN | Blocks unconditional ambient-dependent thermal conclusion |
| IN-029 | Supply current limit | not defined; UNKNOWN | Blocks final supply and current-limit assessment |
| IN-031 | Peak torque duration and repetition | not defined; UNKNOWN | Peak thermal conclusions remain conditional |
| IN-034 | Output-side encoder | required; PRELIMINARY | Resolution, interface and alignment tolerance not specified |

If an upstream value or status later changes in FS-M-001, report it to the Project Lead; do not create a replacement upstream record.

## 3. Screening calculations

These figures are arithmetic screening references, not component ratings, approved operating points, or proof of feasibility. They use the stated nominal targets and 85% assumed gearbox efficiency.

| Screening case | Approximate value | Limitation |
|---|---:|---|
| Output power at 10 N·m and 45 RPM | 47 W | Mechanical output calculation only |
| Motor mechanical power at 85% gearbox efficiency | 55 W | Excludes other losses and design margins |
| Motor speed at 15:1 and 45 RPM output | 675 RPM | Assumes the stated ratio and output speed |
| Motor speed at 20:1 and 45 RPM output | 900 RPM | Assumes the stated ratio and output speed |
| Motor speed at 25:1 and 45 RPM output | 1125 RPM | Assumes the stated ratio and output speed |
| Motor torque for 10 N·m output at 15:1 | 0.78 N·m | Approximate ratio/efficiency calculation |
| Motor torque for 10 N·m output at 20:1 | 0.59 N·m | Approximate ratio/efficiency calculation |
| Motor torque for 10 N·m output at 25:1 | 0.47 N·m | Approximate ratio/efficiency calculation |
| Motor torque for 25 N·m output at 15:1 | 1.96 N·m | Approximate ratio/efficiency calculation |
| Motor torque for 25 N·m output at 20:1 | 1.47 N·m | Approximate ratio/efficiency calculation |
| Motor torque for 25 N·m output at 25:1 | 1.18 N·m | Approximate ratio/efficiency calculation |

Use verified FS-M-002 load cases and FS-M-003 candidate motor data for the actual analysis. The screening values do not capture all losses, transient effects, thermal constraints, or candidate-specific limitations.

## 4. Required upstream artifacts

For each artifact, record exact repository-relative path, revision/commit, units, review status, and provenance in the artifact manifest or related study output.

| Study | Expected artifact | Verification needed |
|---|---|---|
| FS-M-002 | `outputs/LOAD_CASES.csv` | Verify load cases, sign convention, units, and revision |
| FS-M-002 | `outputs/DYNAMIC_TORQUE_RESULTS.csv` | Verify calculation assumptions, applicable cases, and review status |
| FS-M-003 | Candidate motor data | Discover exact filename in repository; do not guess |
| FS-M-003 | Motor operating points | Discover exact filename in repository; do not guess |
| FS-M-004 | `outputs/GEARBOX_CANDIDATE_MATRIX.csv` | Verify candidate data and sourced ratings |
| FS-M-004 | `outputs/RATIO_OPTIMIZATION.csv` | Verify ratio definitions and optimization assumptions |
| FS-M-004 | `outputs/LOAD_RATING_CHECK.csv` | Verify load cases and rating basis |
| FS-M-004 | `outputs/LIFE_RATING_ASSESSMENT.csv` | Verify assumptions, source data, and review status |
| FS-M-007 | `outputs/INTERFACE_REGISTER.csv` | Verify mounting and motor/controller/encoder interface evidence |
| FS-M-007 | `outputs/MASS_ENVELOPE_STATUS.csv` | Mechanical context only; does not establish electrical feasibility |
| FS-M-007 | `outputs/STRUCTURAL_CHECK.csv` | Verify mounting/load-path context and stated limitations |

If an artifact is absent, stale, incomplete, or unreviewed, record the gap and identify which calculations it blocks. Do not substitute a guessed filename or infer approval from a summary.

## 5. Section B - Study-local inputs

These study-local IDs describe required data to collect, verify, or derive. They do not replace upstream inputs.

| Local ID | Required data | Status | Source or action |
|---|---|---|---|
| FS8-IN-001 | Approved operating and withstand voltage limits, including regeneration and reverse-polarity behaviour | UNKNOWN | Verify document/revision and SYS-REQ-041 |
| FS8-IN-002 | Motor torque constant and phase/line, peak/RMS, and commutation conventions | UNKNOWN | Manufacturer datasheet or traceable measurement |
| FS8-IN-003 | Motor torque-speed curves and continuous/peak operating limits | UNKNOWN | Verify FS-M-003 candidate files and rating conditions |
| FS8-IN-004 | Winding resistance, measurement temperature, and temperature coefficient | UNKNOWN | Manufacturer data or traceable measurement |
| FS8-IN-005 | Motor efficiency, iron-loss data, thermal resistance/capacitance, and winding/housing limits | UNKNOWN | Manufacturer data or traceable test evidence |
| FS8-IN-006 | Controller device ratings, MOSFET parameters, switching conditions, current-sense limits, and thermal path | UNKNOWN | Sourced candidate evidence; no part selection implied |
| FS8-IN-007 | PWM frequency, modulation, dead time, current-sampling method, and control-loop timing | UNKNOWN | Architecture definition and verified controller/MCU criteria |
| FS8-IN-008 | Supply transient response, current limit, inrush capability, and ability to sink regenerated energy | UNKNOWN | Supply specification and bus-architecture evidence |
| FS8-IN-009 | Bus capacitance, clamp/braking strategy, and permitted bus overvoltage | UNKNOWN | Sourced design constraints and SYS-REQ-041 evidence |
| FS8-IN-010 | Motor feedback type and electrical characteristics suitable for FOC | UNKNOWN | FS-M-003 candidate data |
| FS8-IN-011 | Output encoder electrical interface, resolution, bandwidth, supply, and fault behaviour | UNKNOWN beyond IN-034 requirement | Verified interface evidence; do not assume resolution |
| FS8-IN-012 | Wiring lengths, routing, connector ratings, allowable voltage drop, and environmental exposure | UNKNOWN | FS-M-007 interface data and documented routing |
| FS8-IN-013 | Thermal interfaces from motor, controller, and gearbox to housing | UNKNOWN | FS-M-007 mounting/thermal-path evidence |
| FS8-IN-014 | Printed housing material, process, orientation, and temperature/creep limits near heat sources | UNKNOWN | FS-M-007 and sourced material data |
| FS8-IN-015 | Peak duration, repetition interval, initial temperature, and cooling conditions | UNKNOWN | Resolve IN-031 and operating-profile requirements |
| FS8-IN-016 | Continuous holding duration, duty cycle, and horizontal-load profile | UNKNOWN | Resolve IN-026 and verify FS-M-002 load case |
| FS8-IN-017 | Indoor laboratory ambient range and temperature measurement method for later tests | UNKNOWN | SYS-REQ-090; range TBD |
| FS8-IN-018 | Temperature sensor type, placement, accuracy, and response time | UNKNOWN | Thermal design criteria and sourced sensor data |
| FS8-IN-019 | Cable/connector current and temperature ratings, shielding, grounding, and EMC constraints | UNKNOWN | Sourced component data and system interface definition |
| FS8-IN-020 | MCU/A0 board capability criteria and verified applicable requirements | UNKNOWN | SYS-REQ-055 and SYS-REQ-005 remain open; criteria only, no part selection |

## 6. Source and input acceptance

For every local input used in a calculation, record:

- Value and unit.
- Source document, manufacturer, revision/date, and exact page/table/figure where applicable.
- Operating condition, temperature, speed, duty, and rating convention.
- Classification as sourced, calculated, assumed, estimated, or unknown.
- Evidence path and dependent calculations.
- Review disposition when used in a safety-critical conclusion.

Supplier headline ratings without applicable conditions are insufficient for critical limits. If sources conflict, retain both references and raise an open question instead of silently choosing one.

## 7. Change control

When an upstream input, motor candidate, gearbox ratio, current convention, supply limit, thermal path, or housing material changes, identify affected calculations and outputs. Preserve the original upstream IDs and revisions. New local input records shall receive the next available `FS8-IN-nnn` ID and shall not reuse an existing ID.

## 8. Initial readiness

The initial baseline contains critical unknown electrical and thermal inputs. Screening calculations and sensitivity analyses may proceed, but unconditional feasibility conclusions are blocked wherever required motor data, operating limits, current limits, duty cycle, ambient conditions, thermal parameters, or independent review evidence is missing.
