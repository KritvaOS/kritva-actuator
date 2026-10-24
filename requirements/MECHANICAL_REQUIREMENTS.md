# Kritva Actuator: Mechanical Requirements

| Field | Value |
|---|---|
| Document ID | KA-REQ-MECH |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Mechanical Intern |
| Reviewer / Approver | Reviewer: Independent Mechanical Reviewer. Contributor (control implications, PCB/connector constraints): Electronics/Embedded Intern. Approver: Project Lead |
| Applies to | Milestone A1 (Humanoid Smart Actuator); A0 for motor mounting and bench fixture items |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** Every numerical value in this document is a **proposed target pending approval**. Values marked TBC or TBD are not design values. Nothing here is a measured result. A requirement or limit becomes binding only when the Project Lead approves it and records the approval in `planning/v1/DECISIONS.md` (for example ACT-DEC-008 load case, ACT-DEC-009 output shaft). The author of a mechanical design may not be the sole approver of its safety-critical aspects (ACT-DEC-014). If no qualified independent reviewer is available, the review is recorded as `NOT_VERIFIED` and the gate stays blocked.

---

## 1. Purpose

This document states the **mechanical requirements** of the Kritva Actuator in its humanoid-elbow configuration. It flows down the system requirements allocated to the mechanical domain in `requirements/SYSTEM_REQUIREMENTS.md` section 11 (SYS-REQ-003, 004, 027, 030–039, 082, 091, 092), together with the load-case requirements SYS-REQ-010 to 014 and the fixture rule SYS-REQ-083.

It is the Mechanical Intern's working document for workstream ACT-02. Each requirement has a rationale, a verification method, an **auditable acceptance criterion**, an evidence location and its parent system requirements, so that the Independent Mechanical Reviewer can close it at the mechanical audit gates M0–M4 (section 10).

It states **what** the mechanical design must achieve. The design itself (calculations, CAD, drawings, BOM) lives in `mechanical/`, and is linked, not copied.

## 2. Scope

### 2.1 In scope

- Mechanical integration of the commercial motor and commercial planetary gearbox.
- The in-house output shaft, dedicated output bearing pair, housing, hard stops, encoder mounting, forearm flange and mounting interface to the upper arm or test fixture.
- Fasteners, materials and fabrication processes for A0/A1.
- Mechanical documentation deliverables and the mechanical test fixture.

### 2.2 Out of scope

- Design of the motor or of the gearbox internals (commercial parts, ACT-DEC-002, ACT-DEC-003). Custom harmonic and cycloidal drives are deferred.
- The forearm and upper-arm structures beyond their interfaces to the actuator.
- Controller PCB design (see `requirements/ELECTRICAL_REQUIREMENTS.md`). This document covers only its mechanical mounting, thermal path and cable exits.

## 3. References

| Ref | Document | Relationship |
|---|---|---|
| [R1] | `requirements/SYSTEM_REQUIREMENTS.md` | Parent (SYS-REQ IDs) |
| [R2] | `requirements/ACTUATOR_SPECIFICATION.md` | Load model, rating definitions, ACT-REQ targets |
| [R3] | `requirements/SAFETY_REQUIREMENTS.md` | Hazards, guarding, test restrictions |
| [R4] | `requirements/ELECTRICAL_REQUIREMENTS.md` | PCB, connector and thermal constraints |
| [R5] | `requirements/INTERFACE_REQUIREMENTS.md` | Interface requirements, including the mechanical interface references |
| [R6] | `mechanical/calculations/LOAD_CASES.md` | Canonical load-case calculation |
| [R7] | `mechanical/calculations/TORQUE_AND_SPEED.md` | Torque/speed derivation |
| [R8] | `mechanical/calculations/SHAFT_STRENGTH.md` | Shaft calculation |
| [R9] | `mechanical/calculations/BEARING_SELECTION.md` | Bearing calculation and selection |
| [R10] | `mechanical/calculations/GEARBOX_SELECTION.md` | Gearbox and motor-class trade study |
| [R11] | `mechanical/bom/MECHANICAL_BOM.csv` | Mechanical BOM |
| [R12] | `planning/v1/tasks/ACT-02/` | Mechanical task folders (TASKS, ACCEPTANCE_CRITERIA, DESIGN_NOTES, TEST_PLAN, REVIEW) |
| [R13] | `docs/validation/VALIDATION_PLAN.md` | Gate content and test approach |
| [R14] | `audit/requirements_traceability/REQUIREMENTS_TRACEABILITY.csv` | Traceability and verification status |
| [R15] | `docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md` | Joint-angle sign convention |

## 4. Definitions and conventions

### 4.1 Terms

| Term | Definition |
|---|---|
| Output shaft | The independent in-house shaft (12 mm nominal initial CAD diameter) that carries the forearm flange and runs in the dedicated bearing pair. |
| Gearbox output | The output member of the commercial planetary gearbox (preferably ≥ 8 mm). It delivers torque to the output shaft through the gearbox-to-shaft coupling. |
| Load path | The route by which a force or moment travels from the forearm to ground. "Bypasses the gearbox" means the arm's radial, axial and bending loads go forearm → flange → output shaft → dedicated bearings → housing → mounting interface, and only torque passes through the coupling into the gearbox. |
| Safety factor (SF) | Material allowable divided by calculated stress for the stated load case, with stress concentrations included. |
| Joint angle q | q = 0° at full extension, positive in flexion ([R15]). |
| Load case LC-nn | A defined combination of loads in section 6. |

### 4.2 Verification methods, priorities, status

As in [R1] section 6: **T** Test, **A** Analysis/calculation, **I** Inspection/review, **D** Demonstration. Priority **M** mandatory, **H** high (a deviation needs a recorded decision), **L** goal. Verification status in [R14]: `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `PASS_WITH_ACTIONS`, `FAIL`, `NOT_VERIFIED`. Audit finding classes: PASS, PASS WITH ACTIONS, FAIL, NOT VERIFIED; finding severity CRITICAL, HIGH, MEDIUM, LOW, OBSERVATION.

### 4.3 Weak versus auditable acceptance criteria

Every acceptance criterion in this document must let an independent reviewer decide PASS or FAIL **from the evidence alone**, without asking the author what was meant. The criterion names the quantity, the load case or test condition, the limit and the evidence.

| Weak (not acceptable) | Auditable (required form) |
|---|---|
| "The shaft is strong enough." | "Calculated static SF on yield ≥ approved minimum (proposed 2.0) at LC-03 and LC-05, including Kt at every shoulder and keyway, in `SHAFT_STRENGTH.md`; reviewed at M2." |
| "Backlash is low." | "Output backlash measured by the ACT-02-006 reversal procedure ≤ limit to be approved before test, recorded in ACCEPTANCE_CRITERIA.md." |
| "No damage after testing." | "After the LC-02 thermal run and the LC-04 stop test: no visible cracking or yielding under 10× magnification; fastener torque stripes unbroken; bearing rotation free of roughness by hand check; output-encoder zero offset change ≤ limit to be approved before test, recorded in ACCEPTANCE_CRITERIA.md." |
| "Bearings are adequate." | "Calculated static safety s0 ≥ approved minimum (proposed 2.0) at the worst of LC-01 to LC-06, and basic rating life L10h ≥ approved duty-based life target, in `BEARING_SELECTION.md`." |

Where a number has not yet been set, the criterion reads **"limit to be approved before test, recorded in ACCEPTANCE_CRITERIA.md"**. That means the Project Lead must approve the numerical limit and write it in the relevant `planning/v1/tasks/ACT-02/ACT-02-00Y/ACCEPTANCE_CRITERIA.md` **before** the test or review is run. A limit chosen after seeing the result is not acceptable (SYS-REQ-025). Proposed safety-factor values in this document are candidates for that approval, not approved values.

## 5. Design basis (summary)

The canonical values are in [R2]. Summary for convenience:

| Quantity | Value | Status |
|---|---|---|
| Forearm + hand | 1.5 kg at 180 mm | PROPOSED; 180 mm **TBC (provisional)** |
| Payload | 1.0 kg at 350 mm | PROPOSED |
| Static gravity torque, horizontal | T_g = 6.08 N·m | Derived |
| Total link weight | 24.5 N | Derived |
| Arm inertia (point mass) | 0.171 kg·m² | TBC from CAD |
| Continuous / peak output torque | 10 N·m / 20 N·m min, 25 N·m stretch | PROPOSED |
| Peak duration, duty | ≤ 2 s, ≤ 10 % (planning placeholder) | TBC |
| Output speed | 45 RPM (4.71 rad/s) | PROPOSED |
| Arm kinetic energy at 45 RPM | 1.90 J | Derived; TBC with CAD |
| Joint range | ≈ 0–120° to 0–135°, hard stops | PROPOSED |
| Gearbox | Commercial planetary, 20:1 first (15:1, 25:1), η = 0.85 for sizing | PROPOSED |
| Output shaft | Independent, 12 mm nominal, dedicated bearing pair | PROPOSED (ACT-DEC-009) |

## 6. Load cases

The canonical calculation is in [R6]. The geometry-dependent values below are **illustrative**, computed with assumed dimensions that must be replaced by CAD values. They show the order of magnitude and which case governs each component.

| LC | Name | Definition | Output torque | Radial / axial / moment on output bearings | Governs |
|---|---|---|---|---|---|
| LC-01 | Static horizontal hold | Arm horizontal, 1.5 kg + 1.0 kg, 0 RPM | 6.08 N·m | Radial = link weight 24.5 N acting at the flange offset; axial TBD from mounting orientation | Holding, bearing static check, encoder alignment |
| LC-02 | Continuous | 10 N·m, 0–45 RPM, until thermally stable | 10 N·m | As LC-01, plus centripetal 13.8 N at 45 RPM | Fatigue, thermal, life |
| LC-03 | Peak | 20 N·m (25 N·m stretch), ≤ 2 s, ≤ 10 % duty (TBC) | 20 / 25 N·m | As LC-02 | Shaft static strength, gearbox peak, coupling |
| LC-04 | Hard-stop impact | Arm at speed hits a stop; 1.90 J at 45 RPM (point-mass J, TBC) | Stop torque = 2E / θ_stop (see §8.3) | Stop reaction force F = T_stop / r_stop, radial if the stop is single-sided | Stops, shaft section between stop and flange, bearings, housing |
| LC-05 | Stall into stop | Firmware fault drives the arm into a stop at the peak torque limit, indefinitely | 20 / 25 N·m held | F = 800–1250 N for a stop radius of 20–30 mm (single-sided) | Stops, housing lugs, bearings (static), fasteners |
| LC-06 | Handling and assembly | Lifting the actuator by the output flange, bench drops, fixture clamping | — | TBD | Housing, flange, encoder protection |
| LC-07 | Shock / impact on link | Only if impacts are in scope (SYS-REQ-014) | TBD | TBD | TBD (shock specification) |
| LC-08 | Fixture test loads | Loaded lever and weights on the test fixture | As tested | Per fixture design | Fixture, mounting interface |
| LC-09 | Misalignment-induced loads | Concentricity/angular error between gearbox output and output shaft | — | Radial and axial loads into the gearbox output from the coupling stiffness | Coupling, gearbox output bearing |

Notes:

1. The motor rotor's reflected inertia (J_rotor · N², with N² = 225 / 400 / 625) adds to the LC-04 energy and decelerates **through the gearbox**. It shall be added once the motor is selected.
2. LC-04 and LC-05 usually dominate the bearing and stop loads by more than an order of magnitude over LC-01. They must not be omitted.

## 7. Requirements

Abbreviation used in the acceptance-criterion column: **"Limit before test (AC-0Y)"** means *limit to be approved before test, recorded in ACCEPTANCE_CRITERIA.md* of task ACT-02-00Y.

### 7.1 Primary requirements

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| MECH-REQ-001 | The actuator structure shall support the **1.5 kg forearm/hand (CoM 180 mm, TBC) plus 1.0 kg payload at 350 mm** in the horizontal orientation, in all load cases LC-01 to LC-05, without yield, loosening or loss of function. | Defines the elbow load the mechanics must carry. | A, T | (a) `LOAD_CASES.md` recomputed with the CAD or measured CoM and reviewed at M2. (b) Fixture test: the arm and payload held horizontal under closed-loop control for the approved holding duration; post-test inspection per MECH-REQ-012 passes. | `mechanical/calculations/LOAD_CASES.md`; `results/mechanical/` | 010, 011, 012, 092 | A1 | M |
| MECH-REQ-002 | The output shaft shall meet **strength and deflection limits**: static, combined and fatigue stresses within the approved safety factors, and slope/deflection within limits set by the bearings and encoder, for LC-01 to LC-05. | The 12 mm diameter is a starting geometry, not a strength guarantee. | A | `SHAFT_STRENGTH.md` shows, for each critical section: static SF on yield ≥ approved minimum (proposed 2.0) at LC-03/LC-04/LC-05; fatigue SF ≥ approved minimum (proposed 1.5) at LC-02; slope at each bearing ≤ the bearing manufacturer's permitted misalignment; deflection at the encoder magnet ≤ the encoder IC's permitted offset. Reviewed at M2. | `mechanical/calculations/SHAFT_STRENGTH.md` | 030, 034 | A1 | M |
| MECH-REQ-003 | The **bearing loads** (radial, axial and moment) on the dedicated output bearing pair shall be calculated for LC-01 to LC-06, and the bearings shall be selected for static capacity, life, fits, preload/clearance and alignment from those loads. | Arm and stop loads must be carried by the dedicated bearings, not the gearbox. | A | `BEARING_SELECTION.md` contains a free-body diagram with CAD dimensions, reactions per bearing per load case, s0 ≥ approved minimum (proposed 2.0) at the worst case and L10h ≥ approved duty-based life target. Reviewed at M2. | `mechanical/calculations/BEARING_SELECTION.md` | 031, 032, 091 | A1 | M |

### 7.2 Load cases and load path

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| MECH-REQ-010 | The load cases LC-01 to LC-09 shall be defined in `LOAD_CASES.md` with magnitudes, directions, points of application and CAD-derived dimensions. | Every downstream calculation starts here. | A, I | All nine cases present with numerical values or an explicit TBD and owner; reviewed at M0 (definitions) and M2 (values). | `LOAD_CASES.md` | 010, 013, 014 | A1 | M |
| MECH-REQ-011 | The forearm/hand CoM, mass and inertia shall be taken from CAD mass properties or measurement, replacing the 180 mm assumption, before Gate A. | SYS-REQ-011. | A, I | `LOAD_CASES.md` records the source (CAD file revision or measurement record) and the recalculated T_g, J_arm and LC-04 energy. | `LOAD_CASES.md`; `results/mechanical/` | 011 | A1 | M |
| MECH-REQ-012 | After loaded testing there shall be no unacceptable permanent deformation, loosening, bearing damage or encoder misalignment. | SYS-REQ-092. | I, T | Post-test inspection checklist completed: no cracks or yielding visible under 10× magnification; torque stripes unbroken; bearings rotate freely without roughness; axial and radial play at the flange ≤ limit before test (AC-06); output-encoder zero offset change ≤ limit before test (AC-06). | `results/mechanical/` | 092 | A1 | M |
| MECH-REQ-013 | External radial, axial and bending loads from the arm shall pass through the output shaft, dedicated bearings and housing to the mounting interface, bypassing the gearbox and motor bearings, unless the manufacturer's rated loads explicitly allow otherwise. | SYS-REQ-032; commercial parts are not rated for arm loads. | A, I | Load-path diagram in `LOAD_CASES.md`; MECH-REQ-064 calculation shows the residual load on the gearbox output ≤ manufacturer permitted values; CAD review at M2 confirms no second load path. | `LOAD_CASES.md`; `mechanical/cad/assembly/` | 032 | A1 | M |
| MECH-REQ-014 | The angular acceleration, duty cycle and horizontal holding duration used in the mechanical calculations shall be the values approved under ACT-REQ-014. Until approved, calculations shall state the placeholder used. | Avoids hidden assumptions. | I | Each calculation file lists its input values with their status (PROPOSED/TBC/TBD). | `mechanical/calculations/` | 013 | A1 | H |
| MECH-REQ-015 | If impacts, catching or aggressive motion are in scope, LC-07 shall be defined from a shock-load specification and all components re-checked. | SYS-REQ-014. | A | Decision recorded either "impacts out of scope for A1" or a shock specification with LC-07 values. | `planning/v1/DECISIONS.md`; `LOAD_CASES.md` | 014 | A1 | H |
| MECH-REQ-016 | The design shall state the actuator mounting orientation(s) for which it is rated (horizontal axis on the fixture; arm orientation). | Gravity and axial loads depend on orientation. | I | Orientation shown on the assembly drawing and in every test record. | `mechanical/drawings/`; `results/mechanical/` | 012, 103 | A1 | H |

### 7.3 Output shaft

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| MECH-REQ-020 | The output shaft shall be an independent in-house shaft with a 12 mm nominal initial CAD diameter at the bearing seats (ACT-DEC-009). The diameter may change only by recorded decision driven by calculation. | Starting geometry. | I | Drawing shows the shaft as a separate part; any diameter change has a DECISIONS.md entry. | `mechanical/drawings/`; `mechanical/cad/shafts/` | 030 | A1 | M |
| MECH-REQ-021 | Torsional shear shall be calculated at every section carrying torque, for 10, 20, 25 N·m and for the LC-04/LC-05 stop torque. | Nominal 12 mm solid: 29.5 / 58.9 / 73.7 MPa at 10 / 20 / 25 N·m. | A | Values per section tabulated in `SHAFT_STRENGTH.md` using the actual minimum section (keyway, flat or groove root). | `SHAFT_STRENGTH.md` | 030 | A1 | M |
| MECH-REQ-022 | Bending stress shall be calculated from the CAD overhang of the forearm flange relative to the bearings, for the link weight, centripetal force and stop reaction force. | Stop reactions can exceed the link weight by over 30× (§8.3). | A | Bending moment diagram per load case in `SHAFT_STRENGTH.md`. | `SHAFT_STRENGTH.md` | 030 | A1 | M |
| MECH-REQ-023 | Combined stress (von Mises) shall be calculated at each critical section, with stress-concentration factors for shoulders, fillets, retaining-ring grooves, keyways, flats and cross holes. | Stress concentrations dominate small shafts. | A | Kt source cited (chart, handbook or FEA); static SF ≥ approved minimum (proposed 2.0) at LC-03, LC-04 and LC-05. | `SHAFT_STRENGTH.md` | 030 | A1 | M |
| MECH-REQ-024 | Fatigue shall be assessed for the LC-02 duty and the approved number of peak cycles, using a stated method (for example modified Goodman with surface, size and reliability factors). | Torque reversals and rotating bending. | A | Fatigue SF ≥ approved minimum (proposed 1.5); method and factors stated. | `SHAFT_STRENGTH.md` | 030, 091 | A1 | M |
| MECH-REQ-025 | Torsional twist between the forearm flange and the output-encoder magnet, and slope at the bearings, shall be calculated. | Twist adds to position error; slope limits bearing life. | A | Twist at 10 N·m and at peak reported (nominal 12 mm solid, 30 mm length: 0.106° at 10 N·m, 0.264° at 25 N·m); slope at each bearing ≤ manufacturer limit. | `SHAFT_STRENGTH.md` | 030, 034 | A1 | H |
| MECH-REQ-026 | The shaft material shall be a justified steel. Proposed: EN8 (C45) or EN19 (42CrMo4) in the stated heat-treatment condition. Aluminium and printed materials are not permitted for the output shaft. | Load-bearing part (SYS-REQ-038). | A, I | Material, condition and the yield/fatigue values used are cited from the standard or supplier certificate; the drawing states material and condition. | `SHAFT_STRENGTH.md`; `mechanical/drawings/` | 030, 038 | A1 | M |
| MECH-REQ-027 | Torque transfer to the forearm flange shall use a feature whose stress concentration is included in MECH-REQ-023 (for example a bolted flange with dowels, a key, or a spline). The method is TBD and is chosen by calculation. | Keyways in a 12 mm shaft carry high Kt. | A, I | Chosen method justified in `SHAFT_STRENGTH.md` and approved at M2. | `SHAFT_STRENGTH.md` | 030, 037 | A1 | H |
| MECH-REQ-028 | Shaft tolerances, surface finish and geometric tolerances at the bearing seats and encoder magnet seat shall be specified on the drawing to suit the selected bearing fits and the encoder runout limit. | Fits and runout depend on them. | I | Drawing shows the seat tolerance class, roughness, concentricity/runout to the bearing axis. | `mechanical/drawings/` | 030, 031, 034 | A1 | M |
| MECH-REQ-029 | The shaft shall be axially located so that axial loads in both directions are carried by the bearing pair and not by the gearbox output. | Axial loads bypass the gearbox. | A, I | Axial location scheme shown in drawing; axial load path stated in `BEARING_SELECTION.md`. | `BEARING_SELECTION.md` | 031, 032 | A1 | M |
| MECH-REQ-030 | The as-made shaft shall be inspected against the drawing. | Prototype parts vary. | I | Inspection record with measured bearing-seat diameters and runout, all within drawing tolerance. | `results/mechanical/` | 030 | A1 | M |

### 7.4 Bearings

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| MECH-REQ-040 | The output shaft shall be supported by a dedicated bearing pair in the joint housing. The type (deep-groove pair, angular-contact pair or crossed-roller) shall be selected after the load calculation and not pre-committed. | SYS-REQ-031. | A, I | `BEARING_SELECTION.md` compares at least two types against MECH-REQ-003 loads and moment stiffness, and records the choice. | `BEARING_SELECTION.md` | 031 | A1 | M |
| MECH-REQ-041 | Bearing static safety s0 = C0 / P0 shall be at least the approved minimum at the worst of LC-01 to LC-06. | Stop and stall loads are the critical static cases. | A | s0 ≥ approved minimum (proposed 2.0); C0 cited from the manufacturer catalogue (candidate part numbers verified against the datasheet). | `BEARING_SELECTION.md` | 031 | A1 | M |
| MECH-REQ-042 | Bearing basic rating life L10h = (C/P)^p · 10⁶ / (60 · n) (p = 3 for ball, 10/3 for roller bearings) shall meet the approved duty-based life target at LC-02. | SYS-REQ-091. | A | L10h ≥ life target approved under MECH-REQ-166; equivalent load and speed spectrum stated. | `BEARING_SELECTION.md` | 091 | A1 | H |
| MECH-REQ-043 | Bearing spacing shall be chosen to give the moment capacity and tilt stiffness needed by the forearm overhang and the encoder alignment. | Short spacing raises reactions and tilt. | A | Reactions computed with the CAD spacing; tilt at the encoder within the IC offset limit. | `BEARING_SELECTION.md` | 031, 034 | A1 | M |
| MECH-REQ-044 | Shaft and housing fits shall be specified from the manufacturer's recommendations for the load direction (rotating inner ring) and the housing material. | Wrong fits cause creep or preload loss. | A, I | Fit classes on the drawing, with the catalogue reference; thermal expansion of an aluminium housing against a steel bearing considered. | `mechanical/drawings/`; `BEARING_SELECTION.md` | 031 | A1 | M |
| MECH-REQ-045 | Preload or internal clearance shall be defined (method: spacer, wave spring or shim; value TBD). | Determines play, stiffness and friction. | A, T | Preload value and method stated; measured axial/radial play at the flange ≤ limit before test (AC-06). | `BEARING_SELECTION.md`; `results/mechanical/` | 031 | A1 | M |
| MECH-REQ-046 | Bearing seats shall be machined in metal, coaxial within the tolerance needed by the bearing misalignment limit. Bearing seats in printed polymer are not permitted for A1 loaded tests. | Alignment and creep resistance. | I | Drawing coaxiality tolerance; inspection record of the as-made housing. | `mechanical/drawings/`; `results/mechanical/` | 031, 038 | A1 | M |
| MECH-REQ-047 | Bearing lubrication and sealing (shielded or sealed bearings, or a separate seal) shall be specified. | Life in a lab environment with debris from fabrication. | I | Bearing suffix or seal part number stated in the BOM. | `MECHANICAL_BOM.csv` | 031, 091 | A1 | H |
| MECH-REQ-048 | Bearing friction torque shall be estimated and included in the output friction budget. | Affects backdrivability and torque accuracy. | A | Estimate in `BEARING_SELECTION.md` and compared with the measured friction under ACT-REQ-025. | `BEARING_SELECTION.md`; `results/mechanical/` | 027 | A1 | L |

### 7.5 Gearbox

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| MECH-REQ-060 | The reduction shall be a commercial planetary gearbox (ACT-DEC-003). The Mechanical Intern leads the selection; the Electronics/Embedded Intern evaluates the control implications; the Project Lead approves. | Joint selection rule. | I | Selection recorded in DECISIONS.md with both interns named. | `GEARBOX_SELECTION.md`; `planning/v1/DECISIONS.md` | 003 | A1 | M |
| MECH-REQ-061 | Ratios 15:1, 20:1 and 25:1 shall be compared against the motor torque-speed curve, efficiency, backlash, backdrivability, reflected inertia and rated input speed; 20:1 is evaluated first and not frozen until the motor data are available. | SYS-REQ-004. | A | Comparison table with datasheet values for each ratio; ratio choice recorded. | `GEARBOX_SELECTION.md` | 004, 027 | A1 | M |
| MECH-REQ-062 | The following manufacturer ratings shall be obtained from the datasheet and verified against requirements: continuous output torque ≥ 10 N·m; peak output torque ≥ 25 N·m if 25 N·m is adopted (≥ 20 N·m otherwise), with the manufacturer's peak definition mapped to the ACT spec §6.2; efficiency; backlash; life; rated and maximum input speed; permitted radial and axial output loads; input shaft/bore compatibility. | Gate A item 5. | I | Each rating listed with the datasheet reference and revision; any rating missing from the datasheet is recorded as NOT_VERIFIED and blocks M1. | `GEARBOX_SELECTION.md` | 003 | A1 | M |
| MECH-REQ-063 | The gearbox shall be mounted on its specified pilot and bolt pattern to a metal mounting plate or housing face, with the bolt grade and tightening torque specified. | Alignment and torque reaction. | I | Drawing shows pilot fit, bolt pattern and torque; inspection at assembly. | `mechanical/drawings/`; `mechanical/assembly/` | 003, 038 | A1 | M |
| MECH-REQ-064 | The gearbox output shall be isolated from arm loads: the gearbox-to-shaft coupling shall transmit torque and limit radial and axial loads on the gearbox output to values within the manufacturer's permitted loads. | SYS-REQ-032. | A | Calculation of the residual radial/axial load from coupling stiffness and the worst-case misalignment (LC-09) ≤ manufacturer permitted values with the approved margin. | `GEARBOX_SELECTION.md`; `SHAFT_STRENGTH.md` | 032 | A1 | M |
| MECH-REQ-065 | Gearbox backlash shall be taken from the datasheet for selection and measured at the output after assembly. | SYS-REQ-025. | I, T | Datasheet value recorded; measured output backlash ≤ limit before test (AC-06). | `GEARBOX_SELECTION.md`; `results/mechanical/` | 025 | A1 | M |
| MECH-REQ-066 | Gearbox efficiency shall be documented across the operating range; 0.85 is used for sizing until data are available. | SYS-REQ-028. | A, T | Datasheet efficiency curve or the measured efficiency at 3 or more load points recorded. | `results/mechanical/` | 028 | A1 | H |
| MECH-REQ-067 | The gearbox rated input speed shall be at least the motor speed at 45 RPM output (675 / 900 / 1125 RPM for 15:1 / 20:1 / 25:1), and the maximum input speed at least the motor no-load speed at 24 V or the firmware speed limit. | Over-speed wear and lubricant limits. | I | Values compared in `GEARBOX_SELECTION.md`. | `GEARBOX_SELECTION.md` | 003 | A1 | M |
| MECH-REQ-068 | The torque the gearbox experiences during LC-04 (rotor reflected-inertia deceleration plus motor torque) shall be estimated and shown to be within the gearbox peak/emergency rating. | Stops on the output protect the arm side, but the rotor still decelerates through the gearbox. | A | Calculation in `GEARBOX_SELECTION.md` using the selected motor's rotor inertia. | `GEARBOX_SELECTION.md` | 035, 082 | A1 | M |
| MECH-REQ-069 | Backdrive torque at the output shall be measured for the selected ratio. | Compliant-control evaluation (SYS-REQ-027). | T | Measured backdrive torque recorded with method and conditions. | `results/mechanical/` | 027 | A1 | H |

### 7.6 Motor mounting

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| MECH-REQ-080 | The motor shaft shall be used as supplied (typically 5–6 mm) without machining. | SYS-REQ-033. | I | Drawings and assembly procedure contain no motor-shaft modification. | `mechanical/drawings/`; `mechanical/assembly/` | 033 | A0 | H |
| MECH-REQ-081 | The motor-to-gearbox interface (input bore/clamp, adapter plate, pilot, shaft length) shall be compatible with the gearbox manufacturer's input specification, or an adapter shall be designed and justified. | Motor and gearbox are bought separately. | I | Interface check table (IF-M1, §9) completed with both datasheets. | `GEARBOX_SELECTION.md`; `mechanical/drawings/` | 033 | A0 | M |
| MECH-REQ-082 | Motor-to-gearbox concentricity and perpendicularity shall be within the gearbox manufacturer's tolerance. | Misalignment causes wear and noise. | I | Tolerances stated on the adapter drawing; inspection record. | `mechanical/drawings/`; `results/mechanical/` | 033 | A1 | M |
| MECH-REQ-083 | The gearbox output interface should be ≥ 8 mm. | Avoids an undersized coupling. | I | Datasheet value recorded; a smaller output needs a recorded decision. | `GEARBOX_SELECTION.md` | 033 | A1 | H |
| MECH-REQ-084 | The motor mount shall react the motor torque (up to the peak motor torque of 0.94–1.96 N·m depending on ratio) without slip, using the motor's specified fasteners. | Torque reaction. | A, I | Fastener check in `GEARBOX_SELECTION.md` or `DESIGN_NOTES.md`. | `planning/v1/tasks/ACT-02/ACT-02-002/DESIGN_NOTES.md` | 033, 038 | A1 | M |
| MECH-REQ-085 | The motor mount shall provide a conduction path from the motor to the housing (metal-to-metal contact or thermal interface material). | Continuous rating is thermal (ACT-REQ-020). | I, T | Drawing shows the contact face; motor temperature in the LC-02 test within the limit approved under ACT-REQ-087. | `results/thermal/` | 020 | A1 | H |
| MECH-REQ-086 | The motor-side feedback (Hall sensors and/or motor-shaft magnetic encoder) mounting shall follow the sensor datasheet for air gap and alignment. | FOC commutation. | I | Gap and offset recorded at assembly. | `mechanical/assembly/` | 052 | A0/A1 | M |

### 7.7 Housing

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| MECH-REQ-090 | The housing shall carry the bearing reactions, stop reactions (LC-04, LC-05) and gearbox/motor reaction torque to the mounting interface. | Load path. | A | Housing load path shown; stress at lugs and bearing bosses within the approved SF. | `LOAD_CASES.md`; `DESIGN_NOTES.md` | 031, 032 | A1 | M |
| MECH-REQ-091 | Housing stiffness shall keep the bearing-seat misalignment and the encoder read-head offset within limits under LC-01 to LC-05. A housing deflection limit shall be set. | Encoder accuracy and bearing life (SYS-REQ-034). | A | Deflection at the bearing seats and encoder ≤ limit to be approved before review, recorded in ACCEPTANCE_CRITERIA.md (AC-03). | `DESIGN_NOTES.md` (ACT-02-003) | 031, 034 | A1 | M |
| MECH-REQ-092 | Load-bearing housing parts shall be metal. Proposed: aluminium 6061-T6. | SYS-REQ-038. | I | Drawings state material and temper. | `mechanical/drawings/` | 038 | A1 | M |
| MECH-REQ-093 | Sealing and ingress protection are not required for A1 unless decided otherwise (TBD). Openings shall prevent fingers or tools reaching gears or rotating parts during operation. | Indoor lab use; pinch hazard. | I | Decision recorded; inspection for exposed rotating parts. | `planning/v1/DECISIONS.md`; `audit/mechanical/` | 090, 082 | A1 | H |
| MECH-REQ-094 | Cable routing shall provide defined channels for motor phases, sensor, encoder, CAN/UART and power cables, with strain relief, minimum bend radius and no cable in the swept path of the forearm. | Wiring damage and pinch points. | I | Cable routing shown in CAD; inspection at assembly; no cable within the swept volume. | `mechanical/cad/assembly/` | 037, 082 | A1 | M |
| MECH-REQ-095 | The housing shall provide a thermal path for the motor and the controller power stage (coordinated with the Electronics/Embedded Intern). | Continuous rating is thermal. | A, T | Thermal path shown; LC-02 temperatures within approved limits. | `results/thermal/` | 020 | A1 | H |
| MECH-REQ-096 | The housing shall provide the controller PCB mounting, connector cut-outs and any keep-outs given by [R4]. | MCU inside the module (SYS-REQ-007). | I | PCB mounting checked against the PCB outline revision at M2. | `mechanical/cad/housing/` | 007 | A1 | H |
| MECH-REQ-097 | Housing temperature sensor positions (for test thermocouples) shall be defined. | Thermal evidence. | I | Positions marked on the assembly drawing. | `mechanical/drawings/` | 020, 103 | A1 | H |

### 7.8 Encoder mounting and alignment

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| MECH-REQ-105 | The output encoder shall measure the output shaft (after the gearbox) (ACT-DEC-010). The Electronics/Embedded Intern leads the electrical side; the Mechanical Intern leads the mounting. | True joint position. | I | CAD shows the magnet on the output shaft or flange and the read-head on the housing. | `mechanical/cad/encoder_mount/` | 024 | A1 | M |
| MECH-REQ-106 | Magnet-to-sensor air gap and lateral offset shall be within the encoder IC datasheet limits (candidate ICs AS5047P / AS5048A / MT6835: verify) at assembly and under LC-01 to LC-05, including shaft deflection and bearing play. | SYS-REQ-034. | A, T | Tolerance stack in `DESIGN_NOTES.md`; measured gap at assembly; encoder field-strength diagnostic in range during loaded tests. | `DESIGN_NOTES.md`; `results/mechanical/` | 034 | A1 | M |
| MECH-REQ-107 | The magnet holder shall respect the IC manufacturer's guidance on surrounding ferromagnetic material (the steel shaft can distort the field); a non-magnetic holder or spacer shall be used if needed. | Steel shafts affect magnetic encoders. | A, I | Guidance cited; design checked at M2. | `DESIGN_NOTES.md` | 034 | A1 | H |
| MECH-REQ-108 | The magnet shall be retained positively (bonded and/or mechanically captured) and indexed so that the encoder zero is repeatable after reassembly. | Calibration retention. | I, T | Zero-offset change after a disassemble/reassemble cycle ≤ limit before test (AC-06). | `results/mechanical/` | 034, 053 | A1 | H |
| MECH-REQ-109 | The encoder read-head and its cable shall be protected from contact with moving parts and from handling damage. | Reliability. | I | Inspection at M3. | `audit/mechanical/` | 034 | A1 | H |

### 7.9 Hard stops and pinch-point guarding

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| MECH-REQ-115 | Mechanical hard stops shall bound the joint range at both ends (≈ 0–120° to 0–135°), outside the firmware soft limits. | SYS-REQ-023, 035. | I, T | Stop angles measured on the assembled actuator; both outside the soft limits by the approved margin. | `results/mechanical/` | 023, 035 | A1 | M |
| MECH-REQ-116 | The stops shall absorb the LC-04 impact energy (≈ 1.9 J at 45 RPM with J = 0.171 kg·m², plus the reflected rotor inertia, TBC) **without damage to the gearbox**, shaft, bearings or housing. | Last line of over-travel protection. | A, T | Calculation of stop torque from the compliant angle (§8.3); impact test sequence at stepped speeds (for example 10, 20, 30 RPM, and 45 RPM only if approved) on the fixture; post-test inspection per MECH-REQ-012 passes; output backlash unchanged within limit before test (AC-06). | `LOAD_CASES.md`; `results/mechanical/` | 035, 082 | A1 | M |
| MECH-REQ-117 | The stop shall act between the output member (shaft or flange) and the housing, so that the arm's impact torque goes to the housing and not through the gearbox or coupling. | Protects the commercial gearbox. | I | CAD review at M2 confirms the stop position in the load path. | `mechanical/cad/assembly/` | 032, 035 | A1 | M |
| MECH-REQ-118 | The stops shall withstand LC-05 (stall into the stop at the firmware peak torque limit, indefinitely) without yield. | Firmware fault case. | A | Static SF ≥ approved minimum (proposed 2.0) at 25 N·m for the stop, lugs, shaft section and fasteners. | `LOAD_CASES.md` | 035, 082 | A1 | M |
| MECH-REQ-119 | The stop shall include a replaceable compliant element (bumper) whose compliance limits the stop torque to the value approved under MECH-REQ-116. | A rigid stop at full speed gives very high torque (§8.3). | A, I | Bumper material, stroke and replacement interval stated. | `DESIGN_NOTES.md`; `MECHANICAL_BOM.csv` | 035 | A1 | H |
| MECH-REQ-120 | If the stop reaction is single-sided, the resulting radial force shall be included in the shaft and bearing calculations; otherwise a balanced (paired) stop shall be used. | A single stop at 25 mm radius gives 800 N at 20 N·m. | A | Stop reaction included in MECH-REQ-003 and MECH-REQ-022. | `BEARING_SELECTION.md`; `SHAFT_STRENGTH.md` | 031, 035 | A1 | M |
| MECH-REQ-121 | The stop positions should be adjustable or replaceable to give the 120° and 135° ranges. | Range TBD from arm geometry. | I | Both ranges achievable by documented part change or adjustment. | `mechanical/drawings/` | 023 | A1 | L |
| MECH-REQ-122 | The approach speed near the stops shall be limited by firmware so that the impact energy stays within the hard-stop design value (coordinated with ACT-REQ-033). | Reduces stop energy (E ∝ ω²). | A, T | Approach-speed limit stated; test shows the limit is active. | `results/motor_control/` | 035, 051 | A1 | H |
| MECH-REQ-123 | Pinch and crush points between the forearm link, flange, stops and housing shall be identified, and guarding or minimum gaps provided for the test fixture configuration (candidate reference: ISO 13854 minimum gaps, verify applicability). | SYS-REQ-082. | I | Pinch-point list with disposition for each item, reviewed at M2 and M4 by the Independent Mechanical Reviewer. | `audit/mechanical/`; [R3] | 082 | A1 | M |
| MECH-REQ-124 | Peak-torque and mechanical failure behaviour (which part fails first, and how) shall be documented. | SYS-REQ-082. | A | Failure-mode section in `LOAD_CASES.md` naming the weakest element and its failure load. | `LOAD_CASES.md` | 082 | A1 | M |

### 7.10 Mounting interfaces

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| MECH-REQ-130 | The housing shall have one defined mounting interface (bolt pattern, location dowels or pilot, datum faces) used both for the test fixture and for the upper-arm structure. | SYS-REQ-037. | I | Interface drawing IF-M4 (§9); fixture and arm adapter both built to it. | `mechanical/drawings/` | 037 | A1 | H |
| MECH-REQ-131 | The output shall have one defined forearm flange interface (bolt circle, dowels, pilot) reusable by later revisions and other joints. | SYS-REQ-037. | I | Interface drawing IF-M3 (§9). | `mechanical/drawings/` | 037 | A1 | H |
| MECH-REQ-132 | The interfaces shall be sized for LC-03, LC-04 and LC-05 with the approved SF, including bolt shear/friction and bearing pressure. | Interfaces are part of the load path. | A | Interface check in `DESIGN_NOTES.md`. | `DESIGN_NOTES.md` (ACT-02-003) | 037, 038 | A1 | M |
| MECH-REQ-133 | Interface dimensions shall be placed under revision control; changes need a recorded decision and an updated interface drawing. | Reuse depends on stable interfaces. | I | Interface drawing revision and DECISIONS.md entry for any change. | `mechanical/drawings/`; `planning/v1/DECISIONS.md` | 037 | A1 | H |
| MECH-REQ-134 | The interfaces shall define the angular datum (q = 0°) and the direction of positive rotation relative to the housing. | Sign convention ([R15]). | I | Marked on the interface drawing and on the housing. | `mechanical/drawings/` | 023, 053 | A1 | H |

### 7.11 Fasteners, thread locking and tightening torques

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| MECH-REQ-138 | Every fastener in the load path shall have its size, property class (proposed 8.8 steel or A2-70 stainless, TBC) and length specified in the BOM. | Reproducibility. | I | BOM complete for all load-path fasteners. | `MECHANICAL_BOM.csv` | 105 | A1 | M |
| MECH-REQ-139 | Tightening torques shall be specified on the drawings or the assembly procedure, and applied with a torque tool. | Preload and loosening. | I | Torque values in `mechanical/assembly/`; assembly record lists the tool. | `mechanical/assembly/` | 092 | A1 | M |
| MECH-REQ-140 | Fasteners subject to vibration or reversing torque shall use a removable thread-locking method (for example medium-strength anaerobic threadlocker) or a mechanical locking element. | Reversing torque loosens joints. | I | Locking method stated per joint. | `mechanical/assembly/` | 092 | A1 | M |
| MECH-REQ-141 | Torque stripes (witness marks) shall be applied to load-path fasteners after tightening. | Gives auditable loosening evidence (MECH-REQ-012). | I | Visible on the assembled unit. | `results/mechanical/` | 092 | A1 | H |
| MECH-REQ-142 | Load-path threads shall not be cut directly into printed polymer. Threads in aluminium that are assembled repeatedly should use thread inserts. | Thread strip-out. | I | Drawing review at M2. | `mechanical/drawings/` | 038 | A1 | H |
| MECH-REQ-143 | Bolted joints transmitting torque (flange, gearbox mount, stops) shall be checked for slip or bolt shear at LC-03 and LC-05. | Joint integrity. | A | Joint check in `DESIGN_NOTES.md`. | `DESIGN_NOTES.md` | 037, 038 | A1 | M |

### 7.12 Fabrication and materials

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| MECH-REQ-145 | A0/A1 parts may use 3D printing and simple machining. The process for each part shall be stated in the BOM. | Low cost (SYS-REQ-038). | I | BOM process column complete. | `MECHANICAL_BOM.csv` | 038 | A0/A1 | H |
| MECH-REQ-146 | These parts **shall be metal** with a justified material: output shaft, bearing seats/bosses, gearbox and motor mounting plates, hard-stop features and lugs, forearm flange, mounting interface, test fixture structure. | Load-bearing parts. | A, I | Each listed part has a material, condition and calculation reference. | `mechanical/drawings/`; `mechanical/calculations/` | 038 | A1 | M |
| MECH-REQ-147 | These parts may be printed (PETG or PA-CF proposed): covers, cable guides, encoder cover (non-magnetic), connector bezels, non-heat-sinking PCB brackets and fit-check mock-ups. A printed part shall not be in the arm load path. | Cost and speed. | I | Drawing review at M2. | `mechanical/drawings/` | 038 | A0/A1 | H |
| MECH-REQ-148 | Proposed materials: shaft EN8/C45 or EN19/42CrMo4; housing aluminium 6061-T6. Values used in calculations shall be cited from the standard or material certificate. | Justified metal. | I | Citations present. | `mechanical/calculations/` | 038 | A1 | M |
| MECH-REQ-149 | Fabricated parts shall be inspected against their drawings before assembly (critical dimensions at least: bearing seats, pilots, shaft seats, stop angles). | Prototype variation. | I | Inspection record per part. | `results/mechanical/` | 038, 092 | A1 | M |

### 7.13 Serviceability

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| MECH-REQ-155 | The motor, gearbox, output bearings and output encoder should be replaceable independently, without destroying other parts. | SYS-REQ-036. | D | Documented disassembly/reassembly of each item demonstrated once. | `mechanical/assembly/`; `results/mechanical/` | 036 | A1 | H |
| MECH-REQ-156 | An assembly and disassembly procedure shall be written, including tools, torques, locking compound and the encoder re-calibration step. | Repeatable assembly. | I, D | Procedure followed by someone other than the author once without unresolved queries. | `mechanical/assembly/` | 036, 053 | A1 | H |
| MECH-REQ-157 | Bonded joints that prevent replacement (for example the gearbox bonded into the housing) shall not be used without a recorded decision. | Serviceability. | I | Drawing review at M2. | `mechanical/drawings/` | 036 | A1 | H |

### 7.14 Mass and envelope

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| MECH-REQ-160 | The actuator mass shall not exceed the mass budget approved under ACT-REQ-091 (TBD). | Elbow mass loads the shoulder. | A, T | CAD mass and weighed mass ≤ approved budget (TBD). | `results/mechanical/` | 039 | A1 | H |
| MECH-REQ-161 | The actuator envelope (maximum diameter, length, connector exit) shall fit the envelope approved under ACT-REQ-092 (TBD). | Arm layout. | I | Envelope drawing within the approved envelope. | `mechanical/drawings/` | 039 | A1 | H |
| MECH-REQ-162 | The CAD mass and mass-property report shall be updated at each design review. | Load model input. | I | Report present at M2 and M4. | `mechanical/cad/assembly/` | 011, 039 | A1 | H |

### 7.15 Lifetime

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| MECH-REQ-165 | Gearbox life shall be checked against the approved duty cycle using the manufacturer's life rating method. | SYS-REQ-091. | A | Life at the duty ≥ approved life target (MECH-REQ-166). | `GEARBOX_SELECTION.md` | 091 | A1 | H |
| MECH-REQ-166 | An A1 life target (operating hours or cycles) shall be defined from the test programme and educational use (TBD). | No target exists yet. | I | Target recorded in ACCEPTANCE_CRITERIA.md (AC-03). | `planning/v1/tasks/ACT-02/ACT-02-003/ACCEPTANCE_CRITERIA.md` | 091 | A1 | H |
| MECH-REQ-167 | Bumper and wear-part replacement intervals shall be defined. | Stop performance degrades. | I | Intervals in the assembly/maintenance procedure. | `mechanical/assembly/` | 035, 091 | A1 | L |

### 7.16 Documentation deliverables

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| MECH-REQ-170 | Native CAD files and neutral STEP exports of every part and the assembly shall be stored following the agreed versioned approach. | Review and reuse (SYS-REQ-107). | I | Native and STEP present for every released part. | `mechanical/cad/` | 107 | A1 | M |
| MECH-REQ-171 | The CAD assembly shall include the motor, gearbox, shaft, bearings, housing, encoder and a representative arm/link. | Gate A item 1. | I | Assembly reviewed at M2. | `mechanical/cad/assembly/` | 030–037 | A1 | M |
| MECH-REQ-172 | Fabrication drawings (PDF) shall be produced for every fabricated part with material, process, tolerances, fits, finish and revision block. | Fabrication and inspection. | I | Drawing set complete at M2. | `mechanical/drawings/` | 038 | A1 | M |
| MECH-REQ-173 | The mechanical BOM shall list exact part numbers, suppliers, quantities, processes and current quotations, with sourcing in India where practical. | SYS-REQ-105, Gate A item 6. | I | Every row complete; no price without a quotation reference. | `MECHANICAL_BOM.csv` | 105 | A1 | M |
| MECH-REQ-174 | Each CAD file, drawing and BOM shall carry revision information consistent with the release (revision letter/number, date, author, change). | Configuration control. | I | Revisions consistent across CAD, drawings and BOM at M2 and M4. | `mechanical/` | 107 | A1 | M |
| MECH-REQ-175 | The calculation files LOAD_CASES, TORQUE_AND_SPEED, SHAFT_STRENGTH, BEARING_SELECTION and GEARBOX_SELECTION shall state inputs with status, method, results and limitations. | Auditable calculations. | I | Reviewed at M2 by the Independent Mechanical Reviewer. | `mechanical/calculations/` | 102 | A1 | M |
| MECH-REQ-176 | Generated or large binary files that are not source or review exports shall not be committed. | SYS-REQ-107. | I | Repository review at M4. | Repository | 107 | A1 | H |

### 7.17 Test fixture

| ID | Requirement | Rationale | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| MECH-REQ-180 | All loaded, peak and stop tests shall be run on a **restrained, guarded, instrumented fixture**. Manually resisting the actuator or attaching it to a person is prohibited (ACT-DEC-015). | SYS-REQ-083. | I | Fixture review record before the first loaded test; every test record names the fixture revision. | `tests/mechanical/`; `audit/mechanical/` | 083 | A0–A2 | M |
| MECH-REQ-181 | The fixture shall be rigidly clamped or bolted to the bench and sized for LC-03, LC-04 and LC-05 with the approved SF. | Fixture failure is a hazard. | A, I | Fixture calculation and inspection. | `tests/mechanical/` | 083 | A1 | M |
| MECH-REQ-182 | The fixture shall use the actuator mounting interface (MECH-REQ-130) and allow the horizontal load case. | Representative loading. | I | Fixture drawing. | `tests/mechanical/` | 012, 037 | A1 | M |
| MECH-REQ-183 | The fixture shall include a guard enclosing the swept volume of the arm and weights, and an emergency stop within reach of the operator outside the guard. | Pinch and impact hazard. | I | Guard and E-stop checked before each test session (checklist). | `tests/mechanical/`; `tests/safety/` | 082, 083 | A1 | M |
| MECH-REQ-184 | Payload weights shall be positively retained (no free-hanging loose weights). | Dropped-load hazard. | I | Inspection before the test. | `tests/mechanical/` | 083 | A1 | M |
| MECH-REQ-185 | The fixture shall provide instrumentation for: output angle (independent reference where needed), output torque (calibrated lever and weights or torque sensor), temperatures (motor, gearbox, bearings, controller), supply voltage and current. | Gate B evidence. | I | Instrument list with calibration status in each test record. | `results/` | 103 | A1 | M |
| MECH-REQ-186 | Every test record shall identify hardware revision, firmware version, load, supply voltage, ambient temperature, mounting orientation, instruments and measured results. | SYS-REQ-103. | I | Records missing any field are not accepted as evidence. | `results/mechanical/`; `results/thermal/` | 103 | A1 | M |

## 8. Reference figures (informative)

These figures are computed with nominal or assumed dimensions and are for consistency checking only. The canonical calculations are in `mechanical/calculations/`.

### 8.1 Output shaft, 12 mm solid (nominal)

τ = 16·T / (π·d³); polar moment J_p = π·d⁴/32 = 2 036 mm⁴; section modulus in bending Z = π·d³/32 = 170 mm³; G = 80 GPa for steel (assumed).

| Torque | Case | Nominal τ | Twist over 30 mm |
|---|---|---|---|
| 6.08 N·m | LC-01 | 17.9 MPa | 0.064° |
| 10 N·m | LC-02 | 29.5 MPa | 0.106° |
| 20 N·m | LC-03 min | 58.9 MPa | 0.211° |
| 25 N·m | LC-03 stretch / LC-05 | 73.7 MPa | 0.264° |
| 47.5 N·m | LC-04 with a 2 mm bumper at 25 mm radius (example, §8.3) | 140.0 MPa | — |

Illustrative combined stress at 25 N·m with a bending moment from twice the link weight at a 30 mm overhang (M = 1 472 N·mm, σ_b = 8.7 MPa): von Mises 127.9 MPa without stress concentration, **≈ 256 MPa with Kt = 2**. Bending from the link weight is small; torsion and stress concentration dominate. A peak equivalent stress of this order is close to the minimum yield of normalised medium-carbon steel grades (verify against the standard and the material certificate). This is why MECH-REQ-023 requires stated Kt values and MECH-REQ-026 requires the heat-treatment condition. A quenched-and-tempered alloy steel gives more margin.

### 8.2 Bearing reactions (illustrative)

For a radial load F at the flange, an overhang a beyond the near bearing and a bearing spacing L (simple supports):

```
R_near = F · (1 + a / L)        R_far = F · a / L
```

| F | a | L | R_near | R_far |
|---|---|---|---|---|
| 24.5 N (link weight) | 20 mm | 20 mm | 49.1 N | 24.5 N |
| 24.5 N | 20 mm | 30 mm | 40.9 N | 16.4 N |
| 24.5 N | 30 mm | 20 mm | 61.3 N | 36.8 N |
| 800 N (single stop, 20 N·m at 25 mm) | at the stop position | CAD | Governs | Governs |

The link weight gives reactions of tens of newtons. A single-sided stop reaction gives hundreds of newtons. The bearing static check is therefore governed by LC-04/LC-05 unless the stop is balanced (MECH-REQ-120).

### 8.3 Hard-stop energy and stop torque

E = ½·J·ω², with J = 0.171 kg·m² (point mass, rotor not included). For a stop with linear compliance, the peak stop torque is T_peak = 2E / θ_stop, where θ_stop is the angular compression of the bumper (θ_stop = linear stroke / stop radius).

| Approach speed | Energy E | θ_stop needed for T_peak = 10 N·m | 20 N·m | 25 N·m |
|---|---|---|---|---|
| 45 RPM | 1.900 J | 21.8° | 10.9° | 8.7° |
| 30 RPM | 0.844 J | 9.7° | 4.8° | 3.9° |
| 20 RPM | 0.375 J | 4.3° | 2.2° | 1.7° |
| 15 RPM | 0.211 J | 2.4° | 1.2° | 1.0° |
| 10 RPM | 0.094 J | 1.1° | 0.5° | 0.4° |

Example: a 2 mm bumper stroke at a 25 mm radius (θ_stop = 4.6°) at 45 RPM gives a peak force of 1 900 N and a stop torque of 47.5 N·m, about twice the peak rating. **Full-speed impact into a compact stop is not compatible with the 20–25 N·m peak rating.** The design therefore needs a combination of firmware approach-speed limiting near the ends of travel (MECH-REQ-122, ACT-REQ-033), a compliant bumper (MECH-REQ-119) and a stop that reacts into the housing, not the gearbox (MECH-REQ-117). The approved approach speed and stop torque are recorded under MECH-REQ-116.

Stall into stop (LC-05), single-sided stop force F = T / r:

| Stop radius | 20 N·m | 25 N·m |
|---|---|---|
| 20 mm | 1 000 N | 1 250 N |
| 25 mm | 800 N | 1 000 N |
| 30 mm | 667 N | 833 N |

## 9. Mechanical interface control summary

This section is the summary of the mechanical interfaces. Dimensions are recorded in the interface drawings in `mechanical/drawings/` and are TBD until M2. Interface requirements towards software and electronics are in [R5].

| IF | Interface | Side A | Side B | Transmits | Controlled characteristics | Owner | Status |
|---|---|---|---|---|---|---|---|
| IF-M1 | Motor ↔ gearbox | Motor shaft as supplied (5–6 mm typical), motor flange/bolt pattern | Gearbox input bore or clamp, adapter plate, input pilot | Motor torque (0.29–1.96 N·m depending on ratio and load) | Shaft diameter and length, clamp/key type, pilot diameter and fit, concentricity and perpendicularity per gearbox datasheet, bolt pattern, fastener grade and torque | Mechanical Intern (fit); Electronics Intern (motor data) | TBD (after M1 selection) |
| IF-M2 | Gearbox output ↔ output shaft coupling | Gearbox output (≥ 8 mm preferred): shaft, key, flat or flange | Output shaft coupling feature | **Torque only** (up to peak 20/25 N·m) | Torsionally stiff; radial/axial compliance or float so that arm loads and misalignment loads stay within the gearbox permitted output loads (MECH-REQ-064); backlash contribution of the coupling; Kt at the shaft feature | Mechanical Intern | TBD |
| IF-M3 | Output shaft/flange ↔ forearm | Output flange: bolt circle, dowels, pilot | Forearm link adapter | Torque, radial, axial and moment loads | Bolt circle diameter, number/size of bolts, dowel positions, pilot fit, q = 0° datum mark, positive rotation direction, hard-stop features if on the flange | Mechanical Intern; PL approves (reused across revisions) | TBD |
| IF-M4 | Housing ↔ fixture / upper arm | Housing mounting face, bolt pattern, dowels/pilot | Test fixture plate and upper-arm adapter (same interface) | All reactions (torque, forces, moments, stop reactions) | Bolt pattern, dowels, datum faces, flatness, joint axis position relative to datums, cable exit position | Mechanical Intern; PL approves | TBD |
| IF-M5 | Output shaft ↔ output encoder | Magnet and holder on the shaft | Read-head PCB on the housing | Position (magnetic field) | Air gap, lateral offset, runout, ferromagnetic keep-out, magnet indexing for repeatable zero | Mechanical Intern (mounting); Electronics Intern (IC) | TBD |
| IF-M6 | Housing ↔ controller PCB and connectors | PCB mounting bosses, thermal pad face, connector cut-outs | Controller PCB (A1) or development board (A0) | Heat, mechanical support | Hole pattern, standoff height, thermal contact face, keep-outs, cable strain relief | Electronics Intern (PCB); Mechanical Intern (housing) | TBD |

Rules:

1. Any change to IF-M3 or IF-M4 is a change to a reused interface and requires a decision entry (MECH-REQ-133).
2. Each interface drawing shows both sides, the controlled dimensions with tolerances, and the revision of each side's part.
3. At M1, IF-M1 and IF-M2 are checked against the selected motor and gearbox datasheets. Any characteristic not available from the datasheet is recorded as NOT_VERIFIED.

## 10. Mechanical audit gates

Gate schedule from the baseline plan. Finding classes are PASS, PASS WITH ACTIONS, FAIL, NOT VERIFIED. **A safety-critical defect can never be treated as non-blocking to meet a deadline.** The reviewer is the Independent Mechanical Reviewer; the author does not approve their own safety-critical design. Review records are kept in `audit/mechanical/` and the task `REVIEW.md` files.

| Gate | Week | Purpose | MECH-REQ items reviewed | Required evidence | Exit criteria |
|---|---|---|---|---|---|
| M0 Requirements Review | 1 | Requirements complete, measurable, traced | All IDs (wording and acceptance criteria); 010 and 014 definitions | This document; traceability rows in [R14] | No requirement without a verification method and an auditable acceptance criterion; open items have owners and dates |
| M1 Component Selection Review | 2 | Motor, gearbox, bearing and encoder candidates checked | 040, 060–067, 080–083, 105, IF-M1, IF-M2 | `GEARBOX_SELECTION.md`, `BEARING_SELECTION.md` (type comparison), datasheets, joint selection record | All MECH-REQ-062 ratings verified from datasheets or recorded NOT_VERIFIED; PL approval of the selection recorded |
| M2 CAD Design Review | 4–5 | Design ready for fabrication (supports Gate A) | 001–003, 010–029, 040–047, 064, 068, 090–097, 105–109, 115–124, 130–134, 138–143, 145–148, 155–157, 160–162, 170–175 | CAD assembly, drawings, BOM, calculations, interface drawings, pinch-point list | No unresolved CRITICAL or HIGH finding; Gate A mechanical items satisfied |
| M3 Prototype Verification | 7–10 | Built parts and assembly verified | 012, 030, 045, 046, 065, 066, 069, 085, 106, 108, 109, 115, 116, 122, 149, 155, 156, 180–186 | Inspection records, assembly records, `results/mechanical/`, `results/thermal/` | Measured values meet the limits approved before test; post-test inspection passes |
| M4 Final Acceptance Audit | 11–12 | Release of the A1 mechanical design | All; with focus on 001, 012, 116, 118, 123, 124, 160, 161, 170–176 | Complete evidence set, final CAD/drawing/BOM release, traceability status | Every requirement PASS, PASS WITH ACTIONS (non-safety actions only) or a recorded disposition; supports Gates B and C |

**Task allocation (ACT-02).**

| Task | Main MECH-REQ items |
|---|---|
| ACT-02-001 Define elbow load cases and mechanical requirements | 001, 010–016, this document |
| ACT-02-002 Motor/gearbox interface constraints and gearbox comparison | 060–069, 080–086, IF-M1, IF-M2 |
| ACT-02-003 Shaft, bearing and housing calculations | 002, 003, 020–029, 040–048, 090–097, 118, 120, 124, 132, 143, 165, 166 |
| ACT-02-004 CAD assembly and fabrication drawings | 105–109, 115, 117, 119, 121, 130, 131, 133, 134, 138–142, 145–148, 157, 160–162, 170–176 |
| ACT-02-005 Fabrication and assembly | 030, 139–141, 149, 155, 156, 180–184 |
| ACT-02-006 Mechanical characterisation | 012, 045, 065, 066, 069, 108, 116, 122, 185, 186 |

## 11. Open items

| # | Item | MECH-REQ | Owner | Needed by |
|---|---|---|---|---|
| 1 | Measured or CAD forearm/hand CoM, mass and inertia | 011 | Mechanical Intern | M2 / Gate A |
| 2 | Approved safety factors (static, fatigue, bearing s0); proposed 2.0 / 1.5 / 2.0 | 002, 003, 023, 024, 041, 118 | Project Lead | M0 |
| 3 | Housing deflection limit | 091 | Project Lead with Mechanical Intern | M2 |
| 4 | Bearing type, spacing, fits and preload | 040–045 | Mechanical Intern | M2 |
| 5 | Gearbox part and ratio; manufacturer peak definition and permitted output loads | 061, 062, 064 | Mechanical Intern leads; Electronics Intern evaluates; PL approves | M1 |
| 6 | Gearbox-to-shaft coupling type (IF-M2) | 064 | Mechanical Intern | M2 |
| 7 | Torque transfer method to the forearm flange | 027 | Mechanical Intern | M2 |
| 8 | Hard-stop approach-speed limit, bumper design and approved stop torque | 116, 119, 122 | Mechanical + Electronics Interns; PL approves | M2 |
| 9 | Pinch-point list and guarding for the fixture | 123, 183 | Mechanical Intern; Independent Mechanical Reviewer | M2 |
| 10 | Backlash, play and encoder zero-shift limits | 012, 065, 108 | Project Lead | Before M3 tests |
| 11 | A1 life target | 166 | Project Lead | M2 |
| 12 | Mass and envelope budget | 160, 161 | Project Lead + Mechanical Intern | Gate A |
| 13 | Shock-load specification or decision that impacts are out of scope | 015 | Project Lead | Gate A |
| 14 | Sealing/ingress decision | 093 | Project Lead | M2 |
| 15 | Fastener property class (8.8 steel or A2-70) | 138 | Mechanical Intern | M2 |

## 12. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
