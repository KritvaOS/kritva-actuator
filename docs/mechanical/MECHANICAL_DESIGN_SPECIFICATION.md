# Kritva Actuator: Mechanical Design Specification

| Field | Value |
|---|---|
| Document ID | KA-DOC-MECH-DESIGN |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Mechanical Intern |
| Reviewer / Approver | Independent Mechanical Reviewer / Project Lead |
| Applies to | A0 (fixture), A1 (integrated actuator) |
| Classification | Proprietary and confidential |

> **Status note.** This specification describes the **proposed** mechanical design concept for the integrated elbow actuator. Component models (motor, gearbox, bearings, encoder) are not yet selected. Dimensions are placeholders until the CAD exists (ACT-02-004). Nothing here may be fabricated before Gate A. Values are binding only once approved in `planning/v1/DECISIONS.md`.

---

## 1. Purpose and scope

This document defines the **mechanical architecture, load paths, component arrangement, interfaces and design rules** of the Kritva Actuator for the humanoid elbow. It shows how the design meets `requirements/MECHANICAL_REQUIREMENTS.md`, and it links to the calculations in `mechanical/calculations/`.

**Superseded first-pass design.** An earlier draft (`docs/mechanical/A1-mechanical-design.md`) proposed a custom two-stage planetary gearbox sized for 8 N·m / 60 RPM / 15:1. That draft is **superseded** by ACT-DEC-003 (commercial planetary gearbox) and ACT-DEC-008 (10 N·m / 20–25 N·m / 45 RPM). Only its general ideas are reused here, namely the balanced hard stop, the stationary output-encoder board and the steel load path.

## 2. Design basis

| Item | Value | Source |
|---|---|---|
| Joint | Humanoid elbow, single rotary axis | ACT-DEC-007 |
| Load case | 1.5 kg forearm/hand at 180 mm (provisional) + 1.0 kg at 350 mm; T_g = 6.08 N·m | LOAD_CASES.md |
| Continuous / peak / speed | 10 N·m / 20 N·m minimum, 25 N·m stretch / 45 RPM | ACT-DEC-008 |
| Motor | Commercial BLDC/PMSM, 24 V, 75–100 W continuous class | SYS-REQ-042 |
| Gearbox | Commercial planetary, 20:1 first (15:1 and 25:1 alternatives) | ACT-DEC-003 |
| Output | Independent 12 mm shaft on a dedicated bearing pair | ACT-DEC-009 |
| Feedback | Output-side magnetic encoder; motor-side feedback for FOC | ACT-DEC-010 |
| Range | 0–120° to 0–135°, with hard stops | SYS-REQ-023 |
| Stop energy | 1.90 J at 45 RPM (point mass) | LOAD_CASES §8 |

## 3. Architecture

### 3.1 Axial stack (concept)

```
  rear                                                                          front (forearm side)
  +--------+   +-----------+   +--------------+   +-----------+   +-------------------------+   +--------+
  | PCB /  |   | BLDC/PMSM |   | commercial   |   | coupling  |   |  12 mm output shaft     |   | output |
  | ctrl   |-->| motor     |-->| planetary    |-->| (Oldham / |-->|  on bearing pair B1, B2 |-->| flange |--> forearm
  | (A1)   |   | (+ motor  |   | gearbox      |   |  jaw /    |   |  in the joint housing   |   |        |
  +--------+   | feedback) |   | (20:1 cand.) |   |  bellows) |   |  + encoder magnet       |   +--------+
               +-----------+   +--------------+   +-----------+   +-------------------------+
                     ^                ^                                   ^            ^
                     |                |                                   |            |
            motor/gearbox mounting plate (KA-MEC-0002)       joint housing (KA-MEC-0001) + balanced hard stops
                     \______________________ rigidly connected, one load-bearing frame _______/
```

### 3.2 Load paths

| Load | Path | Must not pass through |
|---|---|---|
| Joint torque | Motor → gearbox → coupling → shaft → flange → forearm. The reaction runs gearbox housing → mounting plate → joint housing → upper-arm/fixture mount | — |
| Forearm radial, axial and moment loads | Flange → shaft → bearings B1/B2 → joint housing → mount | **Gearbox output bearing, motor bearings** (ACT-DEC-009) |
| Hard-stop reaction | Stop pins on the flange → stop lugs on the housing → mount (balanced pair: a couple only) | Gearbox, bearings (with the balanced stop) |
| Gravity and handling loads of the actuator | Housing → mount | Encoder, PCB |

The coupling isolates the gearbox output from the bearing-pair misalignment and from shaft bending (LC-09).

## 4. Component design

### 4.1 Motor

- Commercial BLDC/PMSM chosen jointly with the gearbox (`TORQUE_AND_SPEED.md` §5).
- **Preference:** a low-Kv outrunner or pancake class, so that 20:1 is feasible.
- The motor flange is bolted to the mounting plate with the manufacturer's pattern and a pilot. The motor shaft is used as supplied (5–6 mm typical; SYS-REQ-033).
- Thermal path: the motor stator is clamped to the aluminium plate, with thermal paste where the manufacturer allows it. The plate conducts heat to the housing.
- Motor-side feedback: the motor's Hall sensors and/or an on-axis magnet on the motor's rear shaft, read by the controller PCB.

### 4.2 Gearbox

- Commercial planetary, mounted to the plate with its own flange and pilot.
- Selected per `mechanical/calculations/GEARBOX_SELECTION.md`.
- Required: ≥ 10 N·m continuous and ≥ 25 N·m peak (if adopted), an input speed rating of at least 900 RPM at 20:1, and published backlash and efficiency.
- The motor input connection follows the gearbox manufacturer's method (clamp collar or keyed bore).

### 4.3 Coupling

- A misalignment-tolerant coupling between the gearbox output (≥ 8 mm preferred) and the 12 mm shaft:
  - **Oldham**: tolerates offset, low cost, very small backlash, but the disc wears;
  - **jaw (spider)**: some damping, but the spider adds compliance and backlash;
  - **bellows**: torsionally stiff with no backlash, at higher cost.
- **Proposed for A1:** Oldham or bellows, chosen for torsional stiffness at 25 N·m. Its rated torque must be ≥ the peak plus margin.

### 4.4 Output shaft (KA-MEC-0003)

- 12 mm nominal, **EN19 / 42CrMo4 Q&T** (SHAFT_STRENGTH §7). EN8 normalised does not meet SF 2.0 under the single-sided stop case.
- Detail features:
  - a D-flat or spline at the coupling end, with no keyway at the maximum-moment section;
  - shoulders for bearing location, fillet r ≥ 0.5 mm (TBC);
  - a circlip groove placed away from peak-stress sections;
  - a bolted flange interface at the front;
  - a magnet seat for the output encoder (an axial magnet on the shaft end, or a ring magnet, depending on the encoder choice).
- Verified at Gate A: combined stress with the actual Kt, fatigue and deflection.

### 4.5 Bearings (B1, B2)

- **Proposed:** a pair of deep-groove 2RS bearings, **6001 (12×28×8) or 6201 (12×32×10)**, with a span of ≥ 25 mm and a minimal overhang. This is adequate **with the balanced hard stop** (BEARING_SELECTION §5).
- One bearing is located (shoulder plus circlip); the other floats, with optional wave-spring preload.
- Fits are proposed in BEARING_SELECTION §7. Both bores are machined in one set-up for coaxiality.

### 4.6 Joint housing (KA-MEC-0001) and mounting plate (KA-MEC-0002)

- **Al 6061-T6, CNC machined.** The bearing bores are machined directly in the housing, or in a pressed steel carrier if wear is a concern.
- The housing carries the bearing pair, the stop lugs, the encoder board mount, the mounting interface to the upper arm or fixture, and cable exits on the non-rotating side only (SAF-REQ-048).
- The mounting plate carries the motor and gearbox and is doweled and bolted to the housing, so that the gearbox stays concentric with the output shaft (target ≤ 0.05 mm, TBC).
- Covers, cable guides and the PCB cover may be 3D-printed (PETG or PA-CF), because they are outside the load path (SAF-REQ-043).
- The housing stiffness and deflection limit are TBD. They are checked by hand calculation or FEA at M2.

### 4.7 Output flange (KA-MEC-0004)

- Bolted to the shaft, by a flange-to-shaft bolt circle or a keyed hub with a clamping screw (detail at M2).
- Carries the forearm interface pattern: a bolt circle plus two dowels. The pattern is the **reusable interface** for later revisions (SYS-REQ-037).
- Carries the two hard-stop pins at 180°.

### 4.8 Hard stops (KA-MEC-0005) and bumpers

- **Balanced, two-sided** stops: two hardened pins on the flange strike two lugs on the housing simultaneously at each end of the range. Polyurethane bumpers (Shore 80–90A) are replaceable.
- Stop angles: about −5° and about 140° (outside the 0–135° range). Slotted, adjustable lugs allow 120° or 135° (TBC).
- **Energy management (LOAD_CASES §8):** the 1.9 J at 45 RPM cannot be absorbed within the peak rating by a compact bumper. The design therefore relies on **firmware approach-speed limiting** (≤ 29 RPM at the stop for a 2 mm / 25 mm bumper to stay ≤ 20 N·m; proposed ≤ 50 % v_max within the last 10°), plus the bumper, plus a balanced reaction into the housing.
- Impact tests are staged (FI-24).

### 4.9 Output encoder mounting (KA-MEC-0006)

- The encoder IC sits on a **stationary** small PCB fixed to the housing, so that no cable crosses the rotating output.
- The magnet is on the output shaft: an axial diametric magnet on the shaft end (on-axis) if the shaft end is accessible, otherwise a ring magnet (off-axis encoder).
- The air gap and runout tolerance follow the selected encoder IC datasheet. The design checks shaft deflection (≈ 0.013 mm at LC-05 at the flange) plus the bearing clearance against that tolerance.
- The magnet is bonded and keyed, so that it cannot slip (RISK-006, HAZ-010).

## 5. Interfaces

| ID | Interface | Definition | Owner |
|---|---|---|---|
| IF-01 | Housing → upper arm / fixture | Pilot plus a bolt pattern of at least 4 × M4 (TBC); dowels for repeatability | Mechanical Intern |
| IF-02 | Flange → forearm | Bolt circle plus 2 dowels (TBC); reused across revisions | Mechanical Intern |
| Internal | Motor → plate | Manufacturer's pattern plus pilot | Mechanical Intern |
| Internal | Gearbox → plate | Manufacturer's pattern plus pilot | Mechanical Intern |
| Internal | Gearbox output → coupling → shaft | Bore and flat per gearbox; 12 mm shaft end | Mechanical Intern |
| Internal | PCB → housing rear | Envelope and mounting holes from the Electronics Intern (DEP-009) | Both |

The interface requirements themselves are in `requirements/INTERFACE_REQUIREMENTS.md` (IF-01, IF-02, IF-16 and IF-17).

## 6. Mass and envelope (to be completed)

| Item | Estimate | Basis |
|---|---|---|
| Motor | TBD | Datasheet |
| Gearbox | TBD | Datasheet |
| Shaft, flange, stops | ≈ 0.08–0.12 kg | Steel, rough volume |
| Housing and plate | ≈ 0.15–0.25 kg | Al, rough volume |
| Bearings, coupling, fasteners | ≈ 0.05–0.08 kg | — |
| Controller PCB and cover | ≈ 0.05 kg | — |
| **Total** | TBD against the budget (SYS-REQ-039) | — |

## 7. Design rules

1. **Steel or aluminium in the load path.** No 3D-printed load-bearing parts without analysis and test (SAF-REQ-043).
2. **No cable across the rotating output** (SAF-REQ-048).
3. **Every fastener** has a defined size, grade, tightening torque and thread-locking (ASSEMBLY_PROCEDURE).
4. **Serviceability.** The motor, gearbox, bearings and encoder can each be replaced without destroying other parts (SYS-REQ-036).
5. **Tolerances.** Datum features are the bearing bores and the mounting pilot. Critical tolerances are bore coaxiality, gearbox-to-shaft concentricity and the encoder gap (FABRICATION_GUIDELINES).
6. **Pinch points** are identified on the drawings and guarded (SAF-REQ-040).
7. **One set-up** for both bearing bores.

## 8. Verification summary

| Requirement area | Verification | Gate |
|---|---|---|
| Load cases and torques | LOAD_CASES and TORQUE_AND_SPEED, independently recalculated | M0 / M1 |
| Gearbox and motor ratings | GEARBOX_SELECTION with datasheets | M1 |
| Shaft and bearings | SHAFT_STRENGTH and BEARING_SELECTION with CAD values | M2 / Gate A |
| CAD assembly, interference, range of motion | CAD review, motion study | M2 |
| Fabrication | Inspection against drawings | M3 |
| Holding, continuous and peak torque; backlash; repeatability | Bench tests (`docs/validation/`) | Gate B |
| Post-test integrity | Inspection (fasteners, bearings, encoder) | Gate B |

## 9. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | Motor and gearbox selection (ACT-DEC-016/017) | Both interns | M1 |
| 2 | Encoder IC and magnet configuration (ACT-DEC-018) | Electronics/Embedded Intern + Mechanical Intern | M2 |
| 3 | Bearing arrangement final (ACT-DEC-019) | Mechanical Intern | M2 |
| 4 | Coupling type | Mechanical Intern | M2 |
| 5 | Housing stiffness limit and check | Mechanical Intern | M2 |
| 6 | Mass and envelope budget | Project Lead | Gate A |
| 7 | Forearm interface pattern agreed with the arm design | Project Lead | M2 |

## 10. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft. Supersedes the first-pass docs/mechanical/A1-mechanical-design.md |
