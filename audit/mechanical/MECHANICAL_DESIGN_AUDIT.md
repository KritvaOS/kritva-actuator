# Kritva Actuator: Mechanical Design Audit (M0–M2)

| Field | Value |
|---|---|
| Document ID | KA-AUD-MECH-DESIGN |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.2 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Independent Mechanical Reviewer |
| Reviewer / Approver | Independent Mechanical Reviewer / Project Lead |
| Applies to | A1 |
| Classification | Proprietary and confidential |

> **Status note.** This is the audit framework, ready for gates M0, M1 and M2. **No gate has been reviewed yet.** Section 4 lists *preliminary observations* raised while the documentation baseline was written. They are **not** independent findings, and the reviewer must confirm, reword or reject each one.

---

## 1. Purpose and scope

This document is the independent design audit of the Kritva Actuator mechanical design. It checks that the design is technically sound, measurable, testable, cost-effective and integrable with the electronics and firmware. It also checks that the design is treated as an **educational prototype**, not as a production-ready humanoid actuator.

| Audit area | What is verified |
|---|---|
| 1 Mechanical requirements | Torque, speed, angular range, dimensions, weight and operating conditions are explicitly specified |
| 2 Motor and gearbox selection | The ratings support the intended joint application |
| 3 Mechanical design | Shafts, bearings, mounting interfaces, housing, fasteners and load paths are appropriately designed |
| 4 Encoder integration | Output encoder placement, alignment, mounting and measurement resolution are adequate |
| 5 Material and fabrication | Materials, manufacturing methods, tolerances and assembly requirements are documented |
| 6 Engineering calculations | Torque, bending, bearing loads, shaft strength, thermal constraints and safety margins are evaluated |
| 7 Acceptance criteria | Requirements have measurable pass/fail criteria and reproducible test procedures |
| 8 Cost and manufacturability | The design meets its budget and can be assembled and maintained practically |

## 2. Audit method

1. The Mechanical Intern submits the evidence package listed for each gate.
2. The reviewer **independently recalculates** the key results. As a minimum: T_g, the motor torque and speed per ratio (T_out = T_motor·N·η), the shaft stresses for the governing case, and the bearing reactions and s0.
3. The reviewer distinguishes **continuous from peak** ratings. A gearbox that tolerates a short peak may not be suitable for sustained load.
4. Where evidence is missing, the item is **flagged**, not assumed to be satisfactory.
5. Each finding is recorded with its severity, required action, owner, due date and closure evidence.

**Weak versus auditable criteria (the reviewer rejects weak ones):**

| Item | Weak | Auditable |
|---|---|---|
| Assembly | "Should work correctly" | Assembled per the released drawings, with no interference over the operating range |
| Gearbox | "Should be suitable" | Manufacturer ratings and the documented load calculation support the torque, speed and duty cycle |
| Encoder | "Should measure position" | Installed and calibrated; resolution and repeatability measured against the approved specification |
| Backlash | "Should be low" | Measured by the documented method and compared with the approved numerical limit |
| Shaft | "Should be strong" | Calculated for the defined loads, with the approved material properties and margin |
| Housing | "Should be rigid" | Deflection evaluated under the specified load, against an approved limit |
| Cost | "Should be inexpensive" | BOM reconciled with quotations and the approved budget |
| Documentation | "CAD should be submitted" | Native CAD, neutral exports, drawings, BOM and revision information submitted and reviewed |

## 3. Gate records

### 3.1 M0: Requirements review (week 1)

| Item | Value |
|---|---|
| Evidence package | `requirements/SYSTEM_REQUIREMENTS.md`, `ACTUATOR_SPECIFICATION.md`, `MECHANICAL_REQUIREMENTS.md`; `mechanical/calculations/LOAD_CASES.md`; `planning/v1/tasks/ACT-02/ACT-02-001/` |
| Reviewer | TBD |
| Date | — |
| Result | NOT VERIFIED. External remote review 2026-10-12: **FAIL / not ready** (input only; not a qualified sign-off) |

| # | Check | Result | Comment |
|---|---|---|---|
| M0-01 | The load model and its assumptions are explicit (masses, centre-of-mass distances, orientation) | NOT VERIFIED | |
| M0-02 | T_g independently recalculated (6.08 N·m) | NOT VERIFIED | |
| M0-03 | Continuous, peak (with duration, repetition and recovery) and speed targets are defined, or tracked as TBD | NOT VERIFIED | |
| M0-04 | Dynamic requirements (α, duty cycle) are defined, or tracked as blocking for the motor freeze | NOT VERIFIED | |
| M0-05 | Range of motion and hard-stop philosophy defined | NOT VERIFIED | |
| M0-06 | External output load cases (radial, axial, moment) defined, with geometry | NOT VERIFIED | |
| M0-07 | Mass and envelope budget defined, or tracked | NOT VERIFIED | |
| M0-08 | Every MECH-REQ has a measurable criterion, a method and an evidence location | NOT VERIFIED | |
| M0-09 | Requirements consistent across SYS, ACT and MECH | NOT VERIFIED | |
| M0-10 | Traceability rows present | NOT VERIFIED | |

### 3.2 M1: Component selection review (week 2)

| Item | Value |
|---|---|
| Evidence package | `mechanical/calculations/TORQUE_AND_SPEED.md`, `GEARBOX_SELECTION.md` (comparison table filled from datasheets and quotations); motor and gearbox datasheets; `mechanical/bom/MECHANICAL_BOM.csv`; ACT-DEC-016/017 drafts |
| Reviewer | TBD |
| Date | — |
| Result | NOT VERIFIED |

| # | Check | Result | Comment |
|---|---|---|---|
| M1-01 | Motor/ratio pairing justified with real torque-speed data (continuous torque at the operating speed, peak torque, Kv) | NOT VERIFIED | |
| M1-02 | Gearbox rated output torque ≥ 10 N·m continuous at the operating conditions | NOT VERIFIED | |
| M1-03 | Gearbox peak rating ≥ the adopted peak, with the manufacturer's definition understood | NOT VERIFIED | |
| M1-04 | Gearbox input speed rating ≥ the motor speed | NOT VERIFIED | |
| M1-05 | Backlash and efficiency are published, or a measurement plan exists | NOT VERIFIED | |
| M1-06 | The gearbox output-load rating is known; the design keeps the arm loads off it | NOT VERIFIED | |
| M1-07 | The motor/gearbox interface is compatible (shaft, pilot, pattern) | NOT VERIFIED | |
| M1-08 | Holding (stall) thermal case checked for the motor | NOT VERIFIED | |
| M1-09 | The encoder choice is compatible with the mounting (air gap, runout tolerance) | NOT VERIFIED | |
| M1-10 | Cost and lead time within the budget and schedule; quotations attached | NOT VERIFIED | |

### 3.3 M2: CAD design review (weeks 4–5)

| Item | Value |
|---|---|
| Evidence package | `mechanical/cad/` (native + STEP); `mechanical/drawings/` (PDF); `SHAFT_STRENGTH.md`, `BEARING_SELECTION.md` with CAD geometry; `docs/mechanical/MECHANICAL_DESIGN_SPECIFICATION.md`, `MATERIAL_SELECTION.md`, `FABRICATION_GUIDELINES.md`, `ASSEMBLY_PROCEDURE.md`; fixture design (ACT-02-007) |
| Reviewer | TBD |
| Date | — |
| Result | NOT VERIFIED |

| # | Check | Result | Comment |
|---|---|---|---|
| M2-01 | The CAD assembly includes the motor, gearbox, coupling, shaft, bearings, housing, encoder, stops and a representative arm | NOT VERIFIED | |
| M2-02 | The load path bypasses the gearbox and motor bearings (ACT-DEC-009) | NOT VERIFIED | |
| M2-03 | Shaft combined stress, fatigue and deflection recalculated with the CAD geometry and actual Kt; SF meets the approved target | NOT VERIFIED | |
| M2-04 | Bearing static (s0) and life checks with the CAD geometry; fits, preload and coaxiality specified | NOT VERIFIED | |
| M2-05 | Hard-stop design: energy at the approved approach speed; stop torque ≤ the peak rating; reaction path into the housing (balanced, or justified) | NOT VERIFIED | |
| M2-06 | Housing stiffness and deflection evaluated against an approved limit | NOT VERIFIED | |
| M2-07 | Encoder mount: air gap and runout stack-up within the IC tolerance | NOT VERIFIED | |
| M2-08 | Materials and conditions specified on the drawings; no printed parts in the load path | NOT VERIFIED | |
| M2-09 | Tolerances, fits and finishes on the drawings; inspection characteristics identified | NOT VERIFIED | |
| M2-10 | Fasteners: sizes, grades, torques and thread-locking defined | NOT VERIFIED | |
| M2-11 | Range of motion free of interference (motion study) | NOT VERIFIED | |
| M2-12 | Pinch points identified; cables do not cross the output | NOT VERIFIED | |
| M2-13 | Serviceability: motor, gearbox, bearings and encoder replaceable independently | NOT VERIFIED | |
| M2-14 | Fixture rated ≥ 2 × the peak test torque; arm rest/catch; guard | NOT VERIFIED | |
| M2-15 | BOM complete with part numbers, suppliers and quotations | NOT VERIFIED | |

## 4. Preliminary observations (raised during documentation; not independent findings)

| ID | Observation | Suggested severity | Reference | Suggested action |
|---|---|---|---|---|
| PO-01 | A **single-sided hard stop** at a 25 N·m stall puts about 1 000 N on the flange. It governs both the shaft (σ_vM with Kt ≈ 325 MPa at 12 mm) and the bearings (s0 < 2 for 6001/6201) | HIGH | SHAFT_STRENGTH §4; BEARING_SELECTION §4 | Adopt a balanced two-sided stop, or move to 15 mm seats with 6202 |
| PO-02 | **EN8 normalised** is not adequate for the 12 mm shaft under the governing case (SF 0.86) | HIGH | SHAFT_STRENGTH §4.1 | Specify EN19/42CrMo4 Q&T, with a certificate |
| PO-03 | A **full-speed (45 RPM) impact** into a compact stop gives ≈ 47.5 N·m, about 2.4 × the peak rating | HIGH | LOAD_CASES §8 | Firmware approach-speed limit (≤ 29 RPM at the stop for a 2 mm / 25 mm bumper) plus a compliant bumper; staged impact test |
| PO-04 | The **20:1 ratio only works with a low-Kv pancake-class motor**. A typical 24 V high-speed BLDC needs about 37:1 | MEDIUM | TORQUE_AND_SPEED §5 | Joint motor/ratio trade study at M1; record a decision if the ratio range is extended |
| PO-05 | The **angular acceleration and duty cycle are undefined**, so the dynamic and thermal sizing are incomplete | MEDIUM | LOAD_CASES §5; SYS-REQ-013 | Define them before the motor/gearbox freeze |
| PO-06 | The **forearm centre of mass (180 mm) is provisional**; ±30 mm changes T_g by ±7 % | MEDIUM | LOAD_CASES §3.1 | Replace it with a CAD or measured value before Gate A |
| PO-07 | Holding at the horizontal pose is a **zero-speed, full-current** case, and may be the thermal limit rather than the 45 RPM point | MEDIUM | TORQUE_AND_SPEED §6 | Include MC-08 / PC-01 thermal evidence |
| PO-08 | The A0 BOM allowances total **₹22,000 at the upper estimates**, above the ₹10–15k A0 budget | LOW | `make bom-summary` | Obtain quotations; review the budget with the Project Lead |

## 5. Findings register

| ID | Gate | Severity | Finding | Required action | Owner | Due | Closure evidence | Reviewer verified | Status |
|---|---|---|---|---|---|---|---|---|---|
| EXT-AUD-002 | M0 | HIGH | Key design inputs open (CoM, α, duty, holding, peak definition, limits); ACT-DEC-008 PROPOSED | Close the M0 blockers B1–B6 (audit/external/EXTERNAL_REPO_AUDIT_2026-10-12.md §3) | Project Lead / Mechanical Intern | M0 | — | — | OPEN |
| EXT-AUD-003 | M2 | HIGH | Hard-stop load model idealised (linear bumper, point-mass J) | CAD inertia + J_rotor·N²; characterised bumper curve; approach-speed limit; FI-24/DU-03 (LOAD_CASES §8.1) | Mechanical Intern | Gate A | — | — | OPEN |
| EXT-AUD-004 | M2 | HIGH | Balanced-stop engagement and load path unproven | Single-contact design rule; tolerance analysis + bench proof; pin, lug, housing, fastener and gearbox checks (LOAD_CASES §8.2) | Mechanical Intern | Gate A | — | — | OPEN |
| EXT-AUD-005 | M2 | HIGH | Shaft SF conditional on assumed geometry, Kt and material | Recompute with CAD, actual Kt and certified material; stop fatigue case | Mechanical Intern | Gate A | — | — | OPEN |
| EXT-AUD-006 | M2 | HIGH | Bearing selection screening only | Baseline 6202 on 15 mm seats; vendor data; combined loads, fits, preload | Mechanical Intern | M2 | — | — | OPEN |
| EXT-AUD-007 | M1 | HIGH | Motor/gearbox operating point not verified | Joint selection with real datasheets (ACT-02-002) | Both interns | M1 | — | — | OPEN |
| EXT-AUD-012 | M2 | MED | Stop geometry changes the governing load path | Freeze the stop configuration in CAD before closing the shaft and bearing calculations | Mechanical Intern | M2 | — | — | OPEN |

## 6. Sign-off

| Gate | Reviewer | Result | Date | Project Lead acknowledgement |
|---|---|---|---|---|
| M0 | | | | |
| M1 | | | | |
| M2 | | | | |

## 7. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft (framework and preliminary observations) |
| 0.2 | 2026-10-12 | Kritvaos Actuator Team | External audit findings EXT-AUD-002..007/012 entered in the findings register; M0 external result recorded |
