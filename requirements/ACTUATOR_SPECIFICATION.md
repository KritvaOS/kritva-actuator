# Kritva Actuator: Actuator Specification (Humanoid Elbow)

| Field | Value |
|---|---|
| Document ID | KA-REQ-ACT |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead |
| Reviewer / Approver | Reviewers: Mechanical Intern, Electronics/Embedded Intern, Independent Mechanical Reviewer, Independent Electrical/Firmware Reviewer. Approver: Project Lead |
| Applies to | Milestone A1 (Humanoid Smart Actuator); A0 for motor-level items; A2 for interface items |
| Classification | Proprietary and confidential (see `LICENSE`) |

> **Status note.** Every value in this specification is a **proposed target pending approval**. Nothing here is a measured result or a released rating. A value becomes binding only when the Project Lead approves it and records the approval in `planning/v1/DECISIONS.md` (the elbow load case and the torque/speed targets are decision **ACT-DEC-008**, status PROPOSED). Approved values are then copied into section 12 of this document with the decision reference.

---

## 1. Purpose

This document is the **datasheet-level specification** of the Kritva Actuator in its humanoid-elbow configuration. It:

1. defines the **elbow load model** that is the design basis, with every assumption stated and the gravity-torque and inertia figures worked out;
2. defines precisely what **continuous torque**, **peak torque** and **rated speed** mean for this actuator, so that ratings are tested against agreed definitions;
3. states the actuator-level requirements (`ACT-REQ-NNN`) with a target value, a status, a verification method and an evidence location;
4. presents the **provisional datasheet** as it would appear on a product sheet, with every value flagged as proposed;
5. compares the candidate gearbox ratios and shows the resulting operating envelope;
6. links each item to acceptance Gates A, B and C.

It states **what** the actuator must deliver and **how well**. How each value is achieved belongs to the child documents and engineering directories (see section 3).

## 2. Scope

### 2.1 In scope

- The complete actuator module: commercial BLDC/PMSM motor, commercial planetary gearbox, independent output shaft on dedicated bearings, housing, output-side and motor-side position feedback, motor controller inside the module, firmware and communication interface.
- Performance at the actuator output flange, at 24 V DC nominal, at the reference ambient (TBD, ACT-REQ-089).
- The elbow design load case of SYS-REQ-010 to SYS-REQ-014.

### 2.2 Out of scope

- The forearm/hand structure itself (only its mass properties, as a load, are in scope).
- Robot-level power distribution, emergency-stop circuit and motion planning (only the actuator's interfaces to them are in scope).
- Human-interactive operation. The actuator is an experimental device (SYS-REQ-083, SYS-REQ-085).
- Shock and impact ratings beyond the hard-stop case, unless a shock-load specification is produced (SYS-REQ-014, ACT-REQ-015).

### 2.3 Relationship to other documents

This document refines the system requirements allocated to it in `requirements/SYSTEM_REQUIREMENTS.md` section 11 (SYS-REQ-001, 010–014, 020–028, 039, 040, 042, 090). For items that belong to another domain it gives the actuator-level target and links to the canonical home:

| Topic | Canonical home |
|---|---|
| Shaft, bearing, housing, hard-stop and fixture requirements | `requirements/MECHANICAL_REQUIREMENTS.md` |
| Supply range, power stage, current sensing, protection hardware | `requirements/ELECTRICAL_REQUIREMENTS.md` |
| FOC, control loops, limits, fault handling | `requirements/FIRMWARE_REQUIREMENTS.md` |
| CAN, USB/UART, actuator software interface | `requirements/INTERFACE_REQUIREMENTS.md` |
| Hazards, safe state, guarding, test restrictions | `requirements/SAFETY_REQUIREMENTS.md` |
| Detailed load, torque/speed and gearbox calculations | `mechanical/calculations/LOAD_CASES.md`, `TORQUE_AND_SPEED.md`, `GEARBOX_SELECTION.md` |
| Test procedures and gate content | `docs/validation/VALIDATION_PLAN.md` |

## 3. References

| Ref | Document | Relationship |
|---|---|---|
| [R1] | `requirements/SYSTEM_REQUIREMENTS.md` | Parent (SYS-REQ IDs) |
| [R2] | `requirements/MECHANICAL_REQUIREMENTS.md` | Sibling; mechanical flow-down of this specification |
| [R3] | `requirements/ELECTRICAL_REQUIREMENTS.md` | Sibling |
| [R4] | `requirements/FIRMWARE_REQUIREMENTS.md` | Sibling |
| [R5] | `requirements/INTERFACE_REQUIREMENTS.md` | Sibling |
| [R6] | `requirements/SAFETY_REQUIREMENTS.md` | Sibling |
| [R7] | `planning/v1/DECISIONS.md` | ACT-DEC-003, 006, 007, 008, 009, 010, 013, 015 |
| [R8] | `mechanical/calculations/LOAD_CASES.md`, `TORQUE_AND_SPEED.md`, `GEARBOX_SELECTION.md` | Calculations (canonical) |
| [R9] | `docs/validation/VALIDATION_PLAN.md` | Verification approach and gates |
| [R10] | `docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md` | Joint-angle sign convention and units |
| [R11] | `audit/requirements_traceability/REQUIREMENTS_TRACEABILITY.csv` | Traceability and verification status |

## 4. Definitions and conventions

| Term | Definition |
|---|---|
| Output | The output shaft and forearm flange of the actuator. All torque, speed and position values in this document are at the output unless marked "motor side". |
| Joint angle q | Output angle relative to the housing. **q = 0° at full elbow extension, positive in the flexion direction** (detailed convention in [R10]). |
| Horizontal load case | Forearm horizontal with payload. Gives the maximum static gravity torque T_g,max. |
| T_g | Static gravity torque about the elbow axis. |
| J_arm | Moment of inertia of forearm, hand and payload about the elbow axis (excludes motor rotor and gearbox). |
| Reference ambient | The ambient temperature at which ratings are stated (TBD, ACT-REQ-089). |
| N | Gearbox reduction ratio (motor speed / output speed). |
| η | Gearbox efficiency. **0.85 is used for preliminary sizing only** (SYS-REQ-028). |
| Status PROPOSED | A value is proposed and pending Project Lead approval. |
| Status TBC | A value exists as a placeholder and must be confirmed by data (datasheet, CAD or test) before it is approved. |
| Status TBD | No value exists yet. A value must be defined before the stated milestone or gate. |

Verification methods, priorities and verification status values are as defined in [R1] section 6: **T** Test, **A** Analysis, **I** Inspection/review, **D** Demonstration; Priority **M**/**H**/**L**; status `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `PASS_WITH_ACTIONS`, `FAIL`, `NOT_VERIFIED`.

## 5. Elbow load model (design basis)

The detailed and canonical calculation is kept in `mechanical/calculations/LOAD_CASES.md`. This section records the inputs and the headline results that the ratings in section 7 depend on.

### 5.1 Assumptions

| # | Assumption | Value | Status | Basis / how it will be replaced |
|---|---|---|---|---|
| LA-01 | Forearm + hand mass, m_a | 1.5 kg | PROPOSED (ACT-DEC-008) | Approved elbow load selection (SYS-REQ-010). Confirm by weighing the actual link or from CAD. |
| LA-02 | Forearm + hand centre of mass from elbow axis, r_a | 180 mm | **TBC: provisional assumption** | Replace with CAD mass properties or physical measurement before Gate A (SYS-REQ-011). |
| LA-03 | Payload mass, m_p | 1.0 kg | PROPOSED | SYS-REQ-010 |
| LA-04 | Payload centre from elbow axis, r_p | 350 mm | PROPOSED | SYS-REQ-010 |
| LA-05 | Gravitational acceleration, g | 9.81 m/s² | Fixed | Standard value |
| LA-06 | Worst static orientation | Forearm horizontal | Fixed | Gravity torque ∝ cosine of the forearm angle from horizontal |
| LA-07 | Masses treated as point masses at their centres | — | TBC | Distributed link inertia added from CAD (SYS-REQ-011) |
| LA-08 | Angular acceleration requirement | — | **TBD** | SYS-REQ-013; open item 2 |
| LA-09 | Duty cycle and continuous horizontal holding duration | — | **TBD** | SYS-REQ-013; open item 2 |
| LA-10 | Impacts, catching or aggressive motion | Not in scope unless a shock spec is produced | TBD | SYS-REQ-014 |

### 5.2 Static gravity torque (worked)

For the forearm horizontal:

```
T_g = m_a · g · r_a  +  m_p · g · r_p
    = 1.5 kg · 9.81 m/s² · 0.180 m  +  1.0 kg · 9.81 m/s² · 0.350 m
    = 2.649 N·m                     +  3.434 N·m
    = 6.082 N·m   ≈ 6.1 N·m
```

The payload contributes 56 % of T_g and the forearm/hand 44 %. A 1 mm error in r_a changes T_g by 0.015 N·m; a 10 mm error changes it by 0.147 N·m (2.4 %).

Margins of the proposed ratings over T_g:

| Rating | Value | Ratio to T_g = 6.08 N·m | Torque left for acceleration and friction |
|---|---|---|---|
| Continuous | 10 N·m | 1.64× | 3.92 N·m |
| Peak, minimum target | 20 N·m | 3.29× | 13.92 N·m |
| Peak, stretch target | 25 N·m | 4.11× | 18.92 N·m |

**Gravity torque against joint angle (informative).** With the upper arm vertical and q = 0° at full extension (forearm hanging), the gravity torque is T_g(q) = T_g,max · sin q:

| q | 0° | 30° | 45° | 60° | 90° | 120° | 135° |
|---|---|---|---|---|---|---|---|
| T_g(q) [N·m] | 0.00 | 3.04 | 4.30 | 5.27 | **6.08** | 5.27 | 4.30 |

The posture on the test fixture may differ. Every fixture test record shall state the actuator mounting orientation so that the gravity torque at each angle can be recomputed.

### 5.3 Arm inertia estimate

Point-mass estimate about the elbow axis:

```
J_arm = m_a · r_a²  +  m_p · r_p²
      = 1.5 · 0.180²  +  1.0 · 0.350²
      = 0.0486        +  0.1225
      = 0.171 kg·m²
```

This **excludes the distributed inertia of the link itself, the flange, and the reflected motor-rotor inertia** (J_rotor · N², with J_rotor TBD from the motor datasheet). It is **TBC from CAD**. It is used here for preliminary acceleration estimates and for the hard-stop energy.

Derived informative values at 45 RPM (ω = 4.712 rad/s):

| Quantity | Value | Use |
|---|---|---|
| Arm kinetic energy, ½·J_arm·ω² | **1.90 J** | Hard-stop design input (MECHANICAL_REQUIREMENTS, hard stops) |
| Centripetal force, (m_a·r_a + m_p·r_p)·ω² | 13.8 N | Radial load contribution (small compared with the weight) |
| Total link weight, (m_a + m_p)·g | 24.5 N | Radial load on the output bearings |

**Illustrative acceleration capability** (horizontal arm, rotor inertia and friction neglected; not a requirement because the acceleration requirement is TBD):

| Output torque | Net torque after T_g | α = (T − T_g)/J_arm | Time from 0 to 45 RPM |
|---|---|---|---|
| 10 N·m | 3.92 N·m | 22.9 rad/s² | 0.21 s |
| 20 N·m | 13.92 N·m | 81.3 rad/s² | 0.058 s |
| 25 N·m | 18.92 N·m | 110.6 rad/s² | 0.043 s |

### 5.4 Sensitivity of the load model

T_g [N·m] for forearm/hand mass 1.5 kg, payload at 350 mm, horizontal arm. The baseline cell is bold. The second figure is the ratio of the 10 N·m continuous target to T_g.

| r_a \ payload m_p | 0.5 kg | 1.0 kg | 2.0 kg |
|---|---|---|---|
| 150 mm | 3.92 (2.55×) | 5.64 (1.77×) | 9.07 (1.10×) |
| **180 mm** | 4.37 (2.29×) | **6.08 (1.64×)** | 9.52 (1.05×) |
| 210 mm | 4.81 (2.08×) | 6.52 (1.53×) | 9.96 (1.00×) |

J_arm [kg·m²] and hard-stop kinetic energy at 45 RPM [J] for the same cases:

| r_a \ payload m_p | 0.5 kg | 1.0 kg | 2.0 kg |
|---|---|---|---|
| 150 mm | 0.095 / 1.05 J | 0.156 / 1.73 J | 0.279 / 3.10 J |
| **180 mm** | 0.110 / 1.22 J | **0.171 / 1.90 J** | 0.294 / 3.26 J |
| 210 mm | 0.127 / 1.41 J | 0.189 / 2.09 J | 0.311 / 3.45 J |

**Findings.**

1. Within ±30 mm of the assumed centre of mass, at 1.0 kg payload, T_g stays between 5.64 and 6.52 N·m. The 10 N·m continuous target still gives at least 1.53× margin.
2. **A 2.0 kg payload is not covered by the continuous rating.** T_g reaches 9.07–9.96 N·m, leaving 0.0–0.9 N·m for friction and acceleration. Any payload above 1.0 kg requires a new approved load case and a re-check of the continuous rating, the gearbox and the motor.
3. The hard-stop energy is dominated by the payload term. Doubling the payload raises it by about 72 %.

## 6. Rating definitions

These definitions refine [R1] section 6. A rating is not valid unless it is stated with the conditions below.

### 6.1 Continuous output torque

The output torque that the actuator delivers **indefinitely** at the reference ambient (TBD), at 24 V nominal, mounted on the reference test fixture, without any component exceeding its temperature limit (motor winding, gearbox lubricant/housing, controller power stage, bearings).

- It is demonstrated by a **loaded thermal test**, run until a **thermal-stability criterion** is met. Proposed candidate criterion for approval: every monitored temperature changes by no more than 1 °C over 10 minutes (TBC; final criterion approved before testing and recorded in the task `ACCEPTANCE_CRITERIA.md`).
- It is stated at a stated speed. The continuous rating applies over **0 to 45 RPM**, including **0 RPM holding** (stall), which concentrates current in fewer phases and is thermally harder for the motor and power stage.
- Temperature limits are taken from the component datasheets with a margin approved by the Project Lead (TBD, ACT-REQ-087).

### 6.2 Peak output torque

The output torque deliverable for a **defined duration**, at a **defined repetition rate**, followed by a **defined recovery period**, starting from a **defined initial thermal state**, without exceeding any temperature, current or mechanical rating.

| Element | Proposed value | Status |
|---|---|---|
| Peak torque level | 20 N·m minimum target; 25 N·m stretch target | PROPOSED; level to be adopted (open item 3) |
| Duration per event | ≤ 2 s | **TBC: planning placeholder only** |
| Repetition (duty) | ≤ 10 % duty (for example 2 s on, 18 s off) | **TBC: planning placeholder only** |
| Recovery | Return to the continuous-rating thermal state before the next peak sequence; recovery time TBD | TBD |
| Initial thermal state | Thermally stable at continuous rating (worst case) | PROPOSED |
| Speed at peak | TBD (see section 10); proposed: peak torque required up to a speed to be defined, not necessarily 45 RPM | TBD |

A peak rating that does not state duration, repetition and recovery is incomplete and shall not appear on a datasheet or in a test report. The gearbox manufacturer's own peak definition (for example "emergency stop torque" or "max. acceleration torque" with a number of cycles) shall be read and mapped onto this definition before the gearbox is accepted.

### 6.3 Rated speed and no-load speed

- **Rated speed**: 45 RPM (4.71 rad/s) output, reached at the continuous torque of 10 N·m at 24 V nominal (TBC, SYS-REQ-022).
- **No-load speed**: the maximum output speed with no external load at 24 V nominal. It shall be measured and recorded; it must exceed 45 RPM with enough margin to cover the voltage drop and back-EMF at 10 N·m.
- **Firmware speed limit**: a configurable limit at or below the rated speed. Firmware limits are defined in [R4].

### 6.4 Holding

**Holding** is maintaining the commanded position against gravity at 0 RPM with the motor energised. The design holding case is the horizontal load case (6.08 N·m). Its required duration is TBD (SYS-REQ-013). The actuator has no brake in v1, so the arm is not held when power is removed. That consequence is handled in [R6].

## 7. Requirements

Column key: **Status** = PROPOSED / TBC / TBD as defined in section 4. **Verif.** = T/A/I/D. **Evidence location** = where the evidence that closes the requirement is stored. **Parent** = SYS-REQ IDs from [R1].

### 7.1 Application and configuration

| ID | Requirement | Target value | Status | Verif. | Evidence location | Parent SYS-REQ | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| ACT-REQ-001 | The actuator shall provide one rotary degree of freedom for a humanoid elbow (flexion/extension). | 1 rotary DOF | PROPOSED | I | `mechanical/cad/assembly/`; Gate A review in `audit/mechanical/` | 001 | A1 | M |
| ACT-REQ-002 | The actuator shall use a commercially available BLDC/PMSM motor, selected jointly by both interns and approved by the Project Lead. | Commercial BLDC/PMSM | PROPOSED | I | `planning/v1/DECISIONS.md`; `hardware/bom/ELECTRICAL_BOM.csv` | 002 | A0 | M |
| ACT-REQ-003 | The actuator shall use a commercially available planetary gearbox (ACT-DEC-003). | Commercial planetary | PROPOSED | I | `mechanical/calculations/GEARBOX_SELECTION.md`; `mechanical/bom/MECHANICAL_BOM.csv` | 003 | A1 | M |
| ACT-REQ-004 | The motor-control MCU and power stage shall be located inside the actuator module in A1. | Integrated controller | PROPOSED | I | `mechanical/cad/assembly/` | 007 | A1 | H |
| ACT-REQ-005 | The module shall keep motor-specific parameters (pole pairs, Kt, limits, encoder offsets) in configuration, separate from generic control code. | Configuration-separated | PROPOSED | I, D | `firmware/`; review in `audit/firmware/` | 006 | A1 | H |

### 7.2 Load case

| ID | Requirement | Target value | Status | Verif. | Evidence location | Parent SYS-REQ | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| ACT-REQ-010 | The design load case shall be forearm + hand 1.5 kg at 180 mm and payload 1.0 kg at 350 mm, horizontal. | See section 5.1 | PROPOSED (ACT-DEC-008) | I | `mechanical/calculations/LOAD_CASES.md` | 010 | A1 | M |
| ACT-REQ-011 | The 180 mm centre of mass shall be replaced by a CAD or measured value, and T_g, J_arm and the hard-stop energy shall be recalculated before Gate A. | Measured r_a | TBC | A, I | `mechanical/calculations/LOAD_CASES.md`; `results/mechanical/` | 011 | A1 | M |
| ACT-REQ-012 | The actuator shall hold the horizontal load case (T_g ≈ 6.1 N·m) continuously without exceeding any thermal limit. | 6.08 N·m at 0 RPM, holding duration TBD | PROPOSED; duration TBD | A, T | `results/thermal/`; `tests/performance/` | 012 | A1 | M |
| ACT-REQ-013 | The arm inertia shall be recalculated from CAD, including the distributed link inertia and the reflected rotor inertia J_rotor·N² of the selected motor and ratio. | 0.171 kg·m² (point-mass estimate) | TBC | A | `mechanical/calculations/LOAD_CASES.md` | 011, 013 | A1 | H |
| ACT-REQ-014 | The required angular acceleration, motion duty cycle and continuous horizontal holding duration shall be defined and approved before the motor and gearbox are frozen. | — | TBD | I | `planning/v1/DECISIONS.md` | 013 | A1 | M |
| ACT-REQ-015 | If impacts, catching or aggressive motion are in scope, a dynamic model and a shock-load specification shall be added to this document before Gate A. | — | TBD | A | This document; `mechanical/calculations/LOAD_CASES.md` | 014 | A1 | H |
| ACT-REQ-016 | Any payload above 1.0 kg, or any change of the payload radius, shall require a new approved load case (section 5.4 finding 2). | ≤ 1.0 kg at 350 mm | PROPOSED | I | `planning/v1/DECISIONS.md` | 010, 020 | A1 | H |

### 7.3 Torque

| ID | Requirement | Target value | Status | Verif. | Evidence location | Parent SYS-REQ | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| ACT-REQ-020 | Continuous output torque shall be at least the target value over 0–45 RPM, demonstrated by a loaded thermal test to the stability criterion of section 6.1. | ≥ 10 N·m | PROPOSED | T | `results/thermal/`; `tests/performance/` | 020 | A1 | M |
| ACT-REQ-021 | Peak output torque shall be at least the minimum target, with the stretch target adopted or rejected by recorded decision. | ≥ 20 N·m min; 25 N·m stretch | PROPOSED; level TBD | T | `results/thermal/`; `results/mechanical/` | 021 | A1 | M |
| ACT-REQ-022 | The peak duration, repetition rate, recovery period and initial thermal state shall be defined and approved before the motor and gearbox are frozen. | Placeholder ≤ 2 s, ≤ 10 % duty | TBC | I | `planning/v1/DECISIONS.md` | 021 | A1 | M |
| ACT-REQ-023 | The actuator shall hold the design gravity torque at 0 RPM at any angle in the joint range (stall holding). | 6.08 N·m at 0 RPM | PROPOSED | T | `results/thermal/` | 012 | A1 | M |
| ACT-REQ-024 | The relationship between commanded current/torque and measured output torque shall be characterised across 0 to peak torque, in both directions. An accuracy limit shall be approved before the test. | Accuracy limit TBD | TBD | T | `results/motor_control/`; `results/mechanical/` | 026 | A1 | H |
| ACT-REQ-025 | No-load backdrive torque and friction torque at the output shall be measured for the selected ratio and recorded. | Record only | PROPOSED | T | `results/mechanical/` | 027 | A1 | H |

### 7.4 Speed

| ID | Requirement | Target value | Status | Verif. | Evidence location | Parent SYS-REQ | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| ACT-REQ-030 | The output shall reach the rated speed at continuous torque at 24 V nominal. | 45 RPM (4.71 rad/s) at 10 N·m | PROPOSED; load at speed TBC | T | `results/mechanical/`; `tests/performance/` | 022 | A1 | M |
| ACT-REQ-031 | Speed shall be measured across the load range (at least 0, T_g, 10 N·m) and the no-load speed recorded. | Record; no-load > 45 RPM | PROPOSED | T | `results/mechanical/` | 022 | A1 | M |
| ACT-REQ-032 | Output speed and acceleration shall be limited by configurable firmware limits. | ≤ 45 RPM default; accel limit TBD | PROPOSED; accel TBD | T | `results/motor_control/` | 051 | A0/A1 | M |
| ACT-REQ-033 | The firmware shall reduce the speed limit near both ends of travel so that the hard-stop impact energy stays within the hard-stop design value (see MECHANICAL_REQUIREMENTS hard stops). | Approach speed TBD | TBD | T | `results/mechanical/`; `tests/safety/` | 035, 082 | A1 | H |

### 7.5 Range of motion

| ID | Requirement | Target value | Status | Verif. | Evidence location | Parent SYS-REQ | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| ACT-REQ-035 | The joint range shall be bounded by mechanical hard stops at both ends. | Approx. 0–120° to 0–135° | PROPOSED; final range TBD from arm geometry | I, T | `mechanical/drawings/`; `results/mechanical/` | 023, 035 | A1 | M |
| ACT-REQ-036 | Firmware soft limits shall lie inside the hard stops with a margin approved before test. | Margin TBD | TBD | T | `results/motor_control/` | 023, 051 | A1 | M |
| ACT-REQ-037 | The joint angle sign convention shall be q = 0° at full extension, positive in flexion, and identical in firmware, protocol and host software. | As [R10] | PROPOSED | I, D | `docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md` | 023, 064 | A1 | M |

### 7.6 Gearbox

| ID | Requirement | Target value | Status | Verif. | Evidence location | Parent SYS-REQ | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| ACT-REQ-040 | The ratios 15:1, 20:1 and 25:1 shall be evaluated against the motor torque-speed curve, efficiency, backlash, backdrivability and rated input speed. 20:1 is the first candidate and shall not be frozen until those data are available. | 20:1 first; 15:1, 25:1 alternatives | PROPOSED | A, T | `mechanical/calculations/GEARBOX_SELECTION.md` | 004 | A1 | M |
| ACT-REQ-041 | The gearbox continuous output rating shall be ≥ 10 N·m, and the peak rating ≥ 25 N·m if the 25 N·m target is adopted (≥ 20 N·m otherwise), using the manufacturer's definitions mapped to section 6.2. | ≥ 10 N·m cont.; ≥ 20/25 N·m peak | PROPOSED | I | Manufacturer datasheet referenced in `GEARBOX_SELECTION.md` | 003, 021 | A1 | M |
| ACT-REQ-042 | Gearbox efficiency shall be documented across the operating range; 0.85 is used for preliminary sizing. | η = 0.85 (sizing) | TBC | A, T | `results/mechanical/` | 028 | A1 | H |
| ACT-REQ-043 | The gearbox rated input speed shall be at least the motor speed at 45 RPM output for the selected ratio, with margin. | ≥ 675 / 900 / 1125 RPM for 15/20/25:1 | PROPOSED | I | `GEARBOX_SELECTION.md` | 003, 004 | A1 | M |
| ACT-REQ-044 | Reflected inertia, backdrivability and the effect of gearbox friction on compliant/force control shall be evaluated and recorded for each candidate ratio. | N² = 225 / 400 / 625 | PROPOSED | A, T | `GEARBOX_SELECTION.md`; `results/mechanical/` | 027 | A1 | H |

### 7.7 Motor

| ID | Requirement | Target value | Status | Verif. | Evidence location | Parent SYS-REQ | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| ACT-REQ-045 | The motor shall provide continuous mechanical output in the candidate range, with enough continuous torque at the motor speed of the selected ratio and enough peak torque/current for the joint peak. | 75–100 W continuous; ≥ 55 W at the 10 N·m / 45 RPM point | PROPOSED | A | `GEARBOX_SELECTION.md`; motor datasheet | 042 | A0 | M |
| ACT-REQ-046 | The motor shall have a published torque constant (or data to derive it), thermal data (winding limit, thermal resistance or time constant) and 24 V compatibility. | Datasheet data | PROPOSED | I | `hardware/bom/ELECTRICAL_BOM.csv`; `results/motor_control/` | 043 | A0 | M |
| ACT-REQ-047 | The motor shall have feedback suitable for FOC (Hall sensors and/or a motor-shaft magnetic encoder). | Hall and/or encoder | PROPOSED | I | `docs/electronics/` | 043, 052 | A0 | M |
| ACT-REQ-048 | The motor shaft shall be used as supplied (typically 5–6 mm) without modification. | As supplied | PROPOSED | I | `mechanical/drawings/` | 033 | A0 | H |

### 7.8 Supply

| ID | Requirement | Target value | Status | Verif. | Evidence location | Parent SYS-REQ | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| ACT-REQ-050 | The actuator shall operate from a 24 V DC nominal supply (ACT-DEC-013). | 24 V DC | PROPOSED | T | `results/motor_control/` | 040 | A0 | M |
| ACT-REQ-051 | The operating voltage range shall be specified in [R3]. | 20–28 V | TBC | T | `results/motor_control/`; [R3] | 041 | A1 | M |
| ACT-REQ-052 | The withstand voltage, including regeneration during braking, shall be specified in [R3]. | ≥ 32 V | TBC | T | [R3]; `results/motor_control/` | 041 | A1 | M |
| ACT-REQ-053 | Reverse-polarity behaviour shall be specified and verified. | Protected, no damage | TBC | T | [R3]; `tests/hardware/` | 041 | A1 | M |
| ACT-REQ-054 | Supply current shall be specified from the motor current and power, not from the supply voltage. Indicative supply power at 10 N·m / 45 RPM: ≈ 55 W motor mechanical plus motor and controller losses (TBD). | TBD from selected motor | TBD | A | [R3] | 044 | A1 | M |

### 7.9 Output shaft, bearings and interfaces

Detailed requirements are in [R2].

| ID | Requirement | Target value | Status | Verif. | Evidence location | Parent SYS-REQ | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| ACT-REQ-055 | The output shall be an independent shaft, 12 mm nominal initial CAD diameter, validated for torsion, bending, combined stress, fatigue, stress concentration and deflection (ACT-DEC-009). | 12 mm nominal | PROPOSED | A, I | `mechanical/calculations/SHAFT_STRENGTH.md` | 030 | A1 | M |
| ACT-REQ-056 | The output shaft shall run in a dedicated bearing pair in the housing; external arm loads shall bypass the gearbox and motor bearings. | Dedicated pair; type TBD | PROPOSED; type TBD | A, I | `mechanical/calculations/BEARING_SELECTION.md` | 031, 032 | A1 | M |
| ACT-REQ-057 | The output flange and the housing mounting interface shall be defined once and reused by later revisions and other joints. | Interface dimensions TBD | TBD | I | `mechanical/drawings/`; [R2] interface summary | 037 | A1 | H |
| ACT-REQ-058 | The motor, gearbox, bearings and encoder should be replaceable independently. | Independent replacement | PROPOSED | I, D | `mechanical/assembly/` | 036 | A1 | H |

### 7.10 Position feedback

| ID | Requirement | Target value | Status | Verif. | Evidence location | Parent SYS-REQ | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| ACT-REQ-060 | Joint position shall be measured by an encoder on the output side of the gearbox (ACT-DEC-010). Proposed: magnetic absolute encoder (candidate ICs AS5047P / AS5048A / MT6835: verify against datasheet). | Output-side encoder | PROPOSED | I, T | `docs/electronics/`; `results/motor_control/` | 024 | A1 | M |
| ACT-REQ-061 | The output position should be absolute at power-up, without a homing move. | Absolute at power-up | TBC | D | `results/motor_control/` | 024, 053 | A1 | H |
| ACT-REQ-062 | Motor-side feedback suitable for FOC commutation shall be provided (motor Hall sensors and/or a motor-shaft magnetic encoder). | Hall and/or encoder | PROPOSED | I, T | `docs/electronics/` | 052 | A0 | M |
| ACT-REQ-063 | The output encoder resolution shall be chosen so that its quantisation step is no more than one tenth of the approved position-error limit (ACT-REQ-066). | Rule; limit TBD | PROPOSED rule | A | `docs/electronics/` | 024, 025 | A1 | H |

### 7.11 Backlash, accuracy and stiffness

No numerical limits are set in this revision. Each limit shall be approved by the Project Lead **before** the corresponding test and recorded in the task `ACCEPTANCE_CRITERIA.md` (`planning/v1/tasks/ACT-02/ACT-02-006/ACCEPTANCE_CRITERIA.md`). A limit chosen after the result is seen is not acceptable (SYS-REQ-025).

| ID | Requirement | Target value | Status | Verif. | Evidence location | Parent SYS-REQ | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| ACT-REQ-065 | Output backlash shall be measured at the output encoder by a defined torque-reversal procedure and shall not exceed the approved limit. | Limit TBD | TBD | T | `results/mechanical/` | 025 | A1 | M |
| ACT-REQ-066 | Static output position error (commanded vs measured, under the defined load) shall not exceed the approved limit. | Limit TBD | TBD | T | `results/mechanical/`; `results/motor_control/` | 025 | A1 | M |
| ACT-REQ-067 | Position repeatability (same target approached repeatedly from the same direction) shall not exceed the approved limit. | Limit TBD | TBD | T | `results/mechanical/` | 025 | A1 | M |
| ACT-REQ-068 | Torsional stiffness at the output shall be measured and recorded. | Record; target TBD | TBD | T | `results/mechanical/` | 027 | A1 | H |

### 7.12 Control

Detailed requirements are in [R4].

| ID | Requirement | Target value | Status | Verif. | Evidence location | Parent SYS-REQ | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| ACT-REQ-070 | The motor shall be driven by FOC with phase-current sensing. | FOC | PROPOSED | I, T | `results/motor_control/` | 050 | A0 | M |
| ACT-REQ-071 | The actuator shall provide current/torque, velocity and position control modes; the joint loop shall close on the output encoder. | 3 modes | PROPOSED | T | `results/motor_control/` | 026, 051, 052 | A0/A1 | M |
| ACT-REQ-072 | Impedance control, or position control with feed-forward torque, should be provided as a later goal. | — | PROPOSED goal | D | `results/integration/` | 026, 027 | A2 | L |
| ACT-REQ-073 | Torque, speed and acceleration limits shall be enforced in firmware. | Configurable | PROPOSED | T | `results/motor_control/` | 051 | A0/A1 | M |
| ACT-REQ-074 | Loss of commands for longer than the timeout shall put the actuator in the safe state. | 50 ms default | TBC | T | `tests/safety/`; `results/integration/` | 063 | A1 | M |
| ACT-REQ-075 | Control loop rates shall meet the proposed values in [R4]. | PWM 20 kHz; current loop 20 kHz (10 kHz min); velocity 2 kHz; position 1 kHz | TBC | T | `results/motor_control/` | 050, 051 | A0/A1 | H |

### 7.13 Communication

Detailed requirements are in [R5].

| ID | Requirement | Target value | Status | Verif. | Evidence location | Parent SYS-REQ | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| ACT-REQ-078 | USB/UART shall be available for commands, configuration, telemetry and debug in all phases. | Telemetry ≥ 100 Hz | TBC | D | `results/motor_control/` | 060 | A0 | M |
| ACT-REQ-079 | CAN shall be provided for real-time commands, feedback and diagnostics (ACT-DEC-006). | CAN 2.0B, 1 Mbit/s; FD-capable hardware preferred (TBC); 120 Ω termination | PROPOSED | D, T | `results/integration/` | 061 | A1 | M |
| ACT-REQ-080 | The actuator shall report position, velocity, current, temperature and fault status at the CAN feedback rate. | 500 Hz target, 1 kHz goal | TBC | T | `results/integration/` | 061, 062 | A1 | M |
| ACT-REQ-081 | The actuator shall report hardware, firmware and protocol versions. | Versioned | PROPOSED | D | `results/integration/` | 067 | A1 | H |

### 7.14 Protection and safe state

Detailed requirements are in [R6].

| ID | Requirement | Target value | Status | Verif. | Evidence location | Parent SYS-REQ | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| ACT-REQ-083 | The actuator shall detect overcurrent, overtemperature (motor and controller), bus over/under-voltage, encoder fault, communication loss and emergency stop, and enter the safe state. Each response shall be verified by fault injection. | All listed faults | PROPOSED; thresholds TBD | T | `tests/safety/`; `results/motor_control/` | 080 | A0/A1 | M |
| ACT-REQ-084 | Motor power shall be removable by a hardware means independent of firmware. | Hardware disable | PROPOSED | T | `tests/safety/` | 081 | A1 | M |
| ACT-REQ-085 | The default safe state shall be PWM disabled (coast), with optional configurable active damping (phase short). | Coast default | TBC | T | `tests/safety/` | 080 | A1 | M |
| ACT-REQ-086 | Loaded and peak tests shall be run only on a restrained, guarded, instrumented fixture (ACT-DEC-015). | Fixture only | PROPOSED | I | `tests/mechanical/`; `audit/` | 083 | A0–A2 | M |

### 7.15 Thermal

| ID | Requirement | Target value | Status | Verif. | Evidence location | Parent SYS-REQ | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| ACT-REQ-087 | Temperature limits for the motor winding, gearbox, bearings and controller power stage shall be derived from component datasheets with an approved margin. | Limits TBD | TBD | I | `results/thermal/`; datasheets | 020, 080 | A1 | M |
| ACT-REQ-088 | Motor and controller temperatures shall be measured during operation and reported in telemetry. | Reported | PROPOSED | T, D | `results/thermal/` | 062, 080 | A1 | M |

### 7.16 Environment

| ID | Requirement | Target value | Status | Verif. | Evidence location | Parent SYS-REQ | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| ACT-REQ-089 | The actuator shall operate in an indoor laboratory. The reference ambient and operating ambient range shall be defined before Gate B and recorded in every test record. | Range TBD | TBD | T, I | Every test record in `results/` | 090, 103 | A1 | H |
| ACT-REQ-090 | Dust and liquid ingress protection is not required for v1; any ingress rating shall be defined by decision. | Not required (v1) | PROPOSED | I | `planning/v1/DECISIONS.md` | 090 | A1 | L |

### 7.17 Mass, envelope and life

| ID | Requirement | Target value | Status | Verif. | Evidence location | Parent SYS-REQ | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| ACT-REQ-091 | The actuator mass budget (including controller and connectors) shall be defined from the humanoid arm layout. | TBD | TBD | I, T | This document section 12; `results/mechanical/` | 039 | A1 | H |
| ACT-REQ-092 | The actuator envelope (maximum diameter, axial length, connector exit) shall be defined from the arm layout. | TBD | TBD | I | `mechanical/drawings/` | 039 | A1 | H |
| ACT-REQ-093 | Gearbox and bearing life shall be checked against the approved duty cycle. | Life target TBD | TBD | A | `BEARING_SELECTION.md`; `GEARBOX_SELECTION.md` | 091 | A1 | H |

### 7.18 Budget

| ID | Requirement | Target value | Status | Verif. | Evidence location | Parent SYS-REQ | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| ACT-REQ-095 | The A0 cost shall be tracked against the indicative budget (provisional, not supplier-verified). | ₹10,000–₹15,000 | PROPOSED | I | `hardware/bom/ELECTRICAL_BOM.csv`; `mechanical/bom/MECHANICAL_BOM.csv` | 100 | A0 | H |
| ACT-REQ-096 | The A1 cumulative cost shall be tracked against the indicative budget, with real vendor quotations. Laboratory equipment is excluded. | ₹20,000–₹30,000 cumulative | PROPOSED | I | Both BOMs | 100, 105 | A1 | H |

## 8. Datasheet summary (provisional)

This table shows the specification as it would appear on a datasheet. **Every value is proposed or undetermined. None is a measured or released rating.** Do not quote it externally.

| Parameter | Value | Unit | Condition | Status |
|---|---|---|---|---|
| Application | Humanoid elbow, 1 rotary DOF | — | — | PROPOSED |
| Supply voltage, nominal | 24 | V DC | — | PROPOSED (ACT-DEC-013) |
| Supply voltage, operating range | 20–28 | V DC | — | TBC |
| Withstand voltage incl. regeneration | ≥ 32 | V DC | — | TBC |
| Reverse-polarity protection | Yes | — | — | TBC |
| Continuous output torque | 10 | N·m | 0–45 RPM, reference ambient, thermally stable | PROPOSED |
| Peak output torque | 20 (min) / 25 (stretch) | N·m | ≤ 2 s, ≤ 10 % duty, recovery TBD | PROPOSED; conditions TBC |
| Design gravity load | 6.1 | N·m | 1.5 kg @ 180 mm + 1.0 kg @ 350 mm, horizontal | PROPOSED; r_a TBC |
| Rated output speed | 45 | RPM | At 10 N·m, 24 V | PROPOSED |
| No-load output speed | Record | RPM | 24 V | TBD |
| Output power at rated point | 47.1 | W | 10 N·m × 4.71 rad/s | Derived |
| Joint range | 0–120 to 0–135 | ° | Mechanical hard stops | PROPOSED |
| Reduction | Planetary, 20:1 first candidate (15:1, 25:1) | — | — | PROPOSED |
| Gearbox efficiency (sizing) | 85 | % | — | TBC |
| Motor | Commercial BLDC/PMSM, 75–100 W continuous | W | 24 V | PROPOSED |
| Output shaft | Independent, 12 mm nominal, dedicated bearing pair | mm | — | PROPOSED (ACT-DEC-009) |
| Output position sensor | Output-side magnetic absolute encoder | — | — | PROPOSED |
| Motor position sensor | Hall and/or motor-shaft encoder | — | — | PROPOSED |
| Backlash | TBD | ° | Defined reversal torque | TBD |
| Position error / repeatability | TBD / TBD | ° | Defined load | TBD |
| Torsional stiffness | Record | N·m/° | — | TBD |
| Control modes | Torque, velocity, position (impedance later) | — | — | PROPOSED |
| Communication | USB/UART; CAN 2.0B 1 Mbit/s | — | — | PROPOSED |
| Feedback rate | 500 (1000 goal) | Hz | CAN | TBC |
| Command timeout | 50 | ms | → safe state | TBC |
| Protections | Overcurrent, overtemperature, over/under-voltage, encoder fault, comms loss, E-stop | — | — | PROPOSED |
| Safe state | PWM disabled (coast); optional active damping | — | — | TBC |
| Brake | None (v1) | — | — | PROPOSED |
| Mass | TBD | g | Complete module | TBD |
| Envelope | TBD | mm | — | TBD |
| Ambient (operating) | TBD | °C | Indoor laboratory | TBD |
| Ingress protection | Not specified (v1) | — | — | PROPOSED |

## 9. Gearbox ratio comparison

The canonical trade study, including motor class against ratio, is in `mechanical/calculations/GEARBOX_SELECTION.md`. The figures below are a consistency check computed from: 45 RPM output, η = 0.85, T_motor = T_out / (N·η), P_motor = T_motor · ω_motor.

| Quantity | 15:1 | **20:1 (first candidate)** | 25:1 |
|---|---|---|---|
| Motor speed at 45 RPM output | 675 RPM (70.7 rad/s) | **900 RPM (94.2 rad/s)** | 1 125 RPM (117.8 rad/s) |
| Motor torque for T_g = 6.08 N·m | 0.477 N·m | **0.358 N·m** | 0.286 N·m |
| Motor torque for 10 N·m output | 0.784 N·m | **0.588 N·m** | 0.471 N·m |
| Motor torque for 20 N·m output | 1.569 N·m | **1.176 N·m** | 0.941 N·m |
| Motor torque for 25 N·m output | 1.961 N·m | **1.471 N·m** | 1.176 N·m |
| Motor mechanical power, 10 N·m at 45 RPM | 55.4 W | **55.4 W** | 55.4 W |
| Motor mechanical power, 20 N·m at 45 RPM | 110.9 W | **110.9 W** | 110.9 W |
| Motor mechanical power, 25 N·m at 45 RPM | 138.6 W | **138.6 W** | 138.6 W |
| Minimum Kv at 24 V, no margin (n_motor / 24 V) | 28 RPM/V | **38 RPM/V** | 47 RPM/V |
| Estimated Kv at 24 V with margin (n_motor / (24 V × 0.9 × 0.7)) | ≈ 45 RPM/V | **≈ 60 RPM/V** | ≈ 74 RPM/V |
| Reflected rotor inertia factor N² | 225 | **400** | 625 |

**Kv estimate assumptions (TBC).** The 0.9 factor allows for usable modulation and drops in the power stage. The 0.7 factor allows for the loaded speed being below the no-load speed at continuous torque. Both are planning factors to be replaced by the selected motor's torque-speed curve. A motor with a Kv below the "minimum" row cannot reach 45 RPM output at 24 V with that ratio.

**Current implication (indicative, owned by [R3]).** With the approximation Kt ≈ 9.55 / Kv (N·m/A, Kv in RPM/V; the Kt convention, RMS or amplitude, must be confirmed from the motor datasheet), a motor exactly at the "with margin" Kv draws about 3.7 A at 10 N·m and 9.2 A at 25 N·m, for all three ratios. Motors with a higher Kv draw proportionally more. At 20:1, a Kv of about 97–162 RPM/V gives the planning range of 6–10 A continuous and 15–25 A peak. Phase currents are TBC until the motor is selected.

**Motor class against ratio.** A typical industrial 24 V BLDC is rated near 3000 RPM with a low torque. To reach 45 RPM output it would need about 67:1, which is outside the 15–25:1 candidates and would raise reflected inertia and friction. The 15–25:1 candidates therefore point towards a high-torque, low-Kv motor (outrunner or pancake class). This is a trade study item, not a decision (see `GEARBOX_SELECTION.md`).

**Peak power note.** Delivering the full peak torque at the full 45 RPM would need 111–139 W of motor mechanical power, above the 75–100 W continuous candidate range. This is acceptable for a short peak only if the selected motor and power stage support it. Otherwise the peak torque is specified at a reduced speed (section 10, corner P2).

## 10. Operating envelope

Proposed torque-speed envelope at the output, 24 V nominal, reference ambient. Corners marked TBD are set when the motor and ratio are selected.

| Corner | Torque | Speed | Output power | Region | Status |
|---|---|---|---|---|---|
| C0 | 0 N·m | No-load speed (> 45 RPM) | 0 W | Continuous | TBD (measure) |
| C1 | 10 N·m | 0 RPM (holding) | 0 W | Continuous | PROPOSED |
| C2 | 10 N·m | 45 RPM | 47.1 W | Continuous (rated point) | PROPOSED |
| C3 | 6.08 N·m | 0 RPM, any angle | 0 W | Continuous holding (design gravity load) | PROPOSED |
| P1 | 20 N·m (25 stretch) | 0 RPM | 0 W | Peak, ≤ 2 s / ≤ 10 % duty | PROPOSED; conditions TBC |
| P2 | 20 N·m (25 stretch) | Speed at which peak is required | ≤ 94.2 W (117.8 W at 25 N·m) if at 45 RPM | Peak | TBD |
| L1 | Firmware torque limit | — | — | Limit | PROPOSED; value ≤ approved peak |
| L2 | — | Firmware speed limit ≤ 45 RPM | — | Limit | PROPOSED |

```
 Torque (N·m)
   25 |- - - - - - - +  P (stretch)                        - - - peak region (≤ 2 s, ≤ 10 %; TBC)
   20 |=============+  P1 ......... P2 (speed TBD)
      |             :
   10 |#############################+ C2 (45 RPM)           ### continuous region
 6.08 |# C3 holding                 #
      |#                            #
    0 +-----------------------------+------> C0 no-load (TBD)
      0                            45            Speed (RPM)
```

The envelope is verified at least at C1, C2, C3 and P1 (and P2 once defined) during Gate B (section 11).

## 11. Acceptance-criteria summary

Gate content is defined in [R1] section 9 and detailed in [R9]. Numerical acceptance limits are defined and approved in each task's `ACCEPTANCE_CRITERIA.md` before the test.

| Gate | Gate item ([R1] §9) | ACT-REQ IDs | Evidence |
|---|---|---|---|
| A | A1: CAD assembly with motor, gearbox, shaft, bearings, housing, encoder, arm/link | 001, 003, 055, 056, 060 | `mechanical/cad/assembly/` |
| A | A2: centre of mass measured or from CAD; T_g recalculated | 011, 013 | `LOAD_CASES.md` |
| A | A3/A4: shaft, bearing and housing calculations reviewed | 055, 056, 093 | `SHAFT_STRENGTH.md`, `BEARING_SELECTION.md` |
| A | A5: gearbox ratings confirmed from manufacturer data | 040–044 | `GEARBOX_SELECTION.md` |
| A | A6: BOM with exact part numbers and quotations | 095, 096 | Both BOMs |
| A | Prerequisite decisions recorded | 014, 022, 015, 091, 092 | `planning/v1/DECISIONS.md` |
| B | B1/B2: holds 1.5 kg + 1 kg horizontal; 6.1 N·m verified with final mass properties | 012, 023 | `results/mechanical/`, `results/thermal/` |
| B | B3: 10 N·m continuous to thermal stability | 020, 087, 088 | `results/thermal/` |
| B | B4: peak at approved duration and duty | 021, 022 | `results/thermal/`, `results/mechanical/` |
| B | B5: speed across load range including 45 RPM | 030, 031 | `results/mechanical/` |
| B | B6: position error, repeatability, backlash against pre-approved limits | 065–068 | `results/mechanical/` |
| B | B7: no deformation, loosening, bearing damage, encoder misalignment | 055, 056, 060 (via [R2]) | `results/mechanical/` |
| B | B8: complete test records | 089 | All `results/` records |
| C | C1: current limit, overtemperature, encoder fault, E-stop tested | 083, 084, 085, 074 | `tests/safety/`, `results/` |
| C | C2: hard stops and pinch-point guarding reviewed | 033, 035 | `audit/mechanical/` |
| C | C3: peak-torque and failure behaviour documented | 021, 085 | `results/`, [R6] |
| C | C4/C5: dispositions traceable; qualified safety approval before human-interactive testing | 086 | `audit/release/`, [R11] |

## 12. Recorded approvals

To be filled in by the Project Lead when each value is approved. An entry is valid only with a decision reference in `planning/v1/DECISIONS.md`. Until an entry exists, the value in this document remains PROPOSED/TBC/TBD.

| # | Item | ACT-REQ IDs | Approved value | Decision ref | Approved by | Date | Evidence |
|---|---|---|---|---|---|---|---|
| 1 | Elbow load case and measured centre of mass | 010, 011 | | | | | |
| 2 | Continuous torque | 020 | | | | | |
| 3 | Peak torque level, duration, repetition, recovery | 021, 022 | | | | | |
| 4 | Rated speed and speed at peak | 030, P2 corner | | | | | |
| 5 | Angular acceleration, duty cycle, holding duration | 014 | | | | | |
| 6 | Gearbox ratio and part | 040, 041 | | | | | |
| 7 | Motor part | 045–047 | | | | | |
| 8 | Supply range, withstand, reverse polarity | 051–053 | | | | | |
| 9 | Backlash, position-error, repeatability limits | 065–067 | | | | | |
| 10 | Temperature limits and thermal-stability criterion | 087 | | | | | |
| 11 | Reference ambient and operating range | 089 | | | | | |
| 12 | Mass and envelope budget | 091, 092 | | | | | |
| 13 | Joint range and soft-limit margin | 035, 036 | | | | | |

## 13. Open items

| # | Item | ACT-REQ | Owner | Needed by |
|---|---|---|---|---|
| 1 | Measured or CAD forearm/hand centre of mass; recompute T_g, J_arm and hard-stop energy | 011, 013 | Mechanical Intern | Gate A |
| 2 | Angular acceleration, duty cycle and continuous horizontal holding duration | 014 | Project Lead | Before motor/gearbox freeze |
| 3 | Peak torque level (20 or 25 N·m), duration, repetition and recovery; speed at which peak is required (corner P2) | 021, 022 | Project Lead | Before motor/gearbox freeze |
| 4 | Final gearbox ratio and part, with manufacturer peak definition mapped to section 6.2 | 040, 041 | Mechanical + Electronics Interns; PL approves | After datasheet comparison |
| 5 | Motor selection: Kv, Kt (and its convention), thermal data, rotor inertia | 045–047, 013 | Electronics Intern leads; Mechanical evaluates fit | Week 2 (M1/E1) |
| 6 | Backlash, position-error and repeatability limits | 065–067 | Project Lead | Before Gate B testing |
| 7 | Temperature limits and thermal-stability criterion (1 °C / 10 min proposed) | 087 | Project Lead with Electronics Intern | Before thermal testing |
| 8 | Supply range, withstand voltage, regeneration handling | 051–053 | Electronics Intern | A1 PCB start |
| 9 | Mass and envelope budget | 091, 092 | Project Lead + Mechanical Intern | Gate A |
| 10 | Shock-load specification, if impacts are in scope | 015 | Project Lead | Gate A |
| 11 | Reference ambient and operating range | 089 | Project Lead | Gate B |
| 12 | Approach-speed limit near the hard stops | 033 | Electronics + Mechanical Interns | Gate A |
| 13 | Torque accuracy limit (commanded vs measured) | 024 | Project Lead | Before Gate B testing |

## 14. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
