---
study_id: FS-M-004
title: Gearbox Selection and Ratio Optimization - Input Register
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
upstream_sources:
- FS-M-001 inputs/INPUTS.md
- FS-M-002 outputs/LOAD_CASES.csv
- FS-M-002 outputs/DYNAMIC_TORQUE_RESULTS.csv
- FS-M-002 outputs/REFLECTED_INERTIA.csv
- FS-M-003 candidate motor data
---

# FS-M-004 Input Register

## 1. Purpose and Rules

This file records the inputs needed for gearbox candidate research and ratio optimization. It is not a replacement for the authoritative FS-M-001 input register, FS-M-002 calculations or FS-M-003 motor data.

- Preserve upstream input IDs, values, units and statuses.
- Use `FS4-IN-nnn` for study-local inputs, `FS4-ASM-nnn` for assumptions and `FS4-OQ-nnn` for open questions.
- Do not assign new meanings to upstream IDs.
- Use `UNKNOWN` when data is absent; do not infer a pass from missing evidence.
- Every candidate-specific number must cite its source-register entry and exact model.
- Record the source revision/commit for upstream outputs and calculations.

## 2. Required Upstream FS-M-001 Inputs

Authoritative source: `kritva-m/FS-M-001-integrated-actuator-system/inputs/INPUTS.md`.

| Upstream ID | Value / meaning | Status | Use in FS-M-004 |
|---|---|---|---|
| IN-006 | Continuous output torque requirement, at least 10 N·m | PRELIMINARY | Continuous gearbox rating check |
| IN-007 | Peak output torque 20 N·m minimum / 25 N·m stretch | PRELIMINARY | Peak rating and joint motor/gearbox check |
| IN-008 | Output speed target 45 RPM | PRELIMINARY | Input speed and ratio calculation |
| IN-010 | Candidate ratios 15:1, 20:1, 25:1 | PRELIMINARY | Primary ratio comparison |
| IN-011 | 20:1 first candidate | PRELIMINARY | Initial candidate only; not frozen |
| IN-012 | Gearbox efficiency 85% | ASSUMED | Baseline calculation until candidate-specific data is available |
| IN-013 | Motor power range 75-100 W | PRELIMINARY | Joint motor/gearbox screening |
| IN-014 | Motor data not yet consolidated | UNKNOWN | Obtain actual FS-M-003 candidate data |
| IN-015 | Output shaft nominal diameter 12 mm | PRELIMINARY | Interface assessment; not a gearbox bore requirement |
| IN-016 | 6202 bearing on 15 mm seats; mismatch recorded | ASSUMED | Compatibility risk; do not treat as resolved |
| IN-019 | Full-speed impact torque estimate approx. 47.5 N·m | PRELIMINARY | Impact case only after provenance check; not a validated rating requirement |
| IN-025 | Gearbox continuous torque margin 20% | ASSUMED | Transparent screening margin; avoid double-counting |
| IN-026 | Duty cycle | UNKNOWN | Required for thermal and life suitability |
| IN-030 | Expected service life | UNKNOWN | Compare manufacturer life-rating basis; do not invent a target |
| IN-031 | Peak torque duration/repetition | UNKNOWN | Required to judge intermittent and emergency ratings |
| IN-035 | Reflected inertia/backdrivability | UNKNOWN | Use FS-M-002 data and candidate-specific evidence |
| IN-038 | Exact BOM part numbers | UNKNOWN | Populate only from verifiable manufacturer evidence |
| IN-039 | 20:1 may require a low-Kv pancake motor; approximately 37:1 for a typical BLDC | PRELIMINARY | Include 37:1 as comparison-only, not as a selected ratio |

The full authoritative input descriptions, status definitions and change history remain in FS-M-001. Do not copy upstream assumptions ASM-001..ASM-012 or open questions OQ-001..OQ-014 into this register as new FS-M-004 records; reference them by ID.

## 3. FS-M-002 Output Dependencies

Upstream study: `kritva-m/FS-M-002-load-torque-analysis/`.

| Required artifact | Use | If missing or unreviewed |
|---|---|---|
| `outputs/LOAD_CASES.csv` | Load-case definition and applicable output torque/load conditions | Mark dependent checks BLOCKED or provisional |
| `outputs/DYNAMIC_TORQUE_RESULTS.csv` | Dynamic, continuous/RMS and peak torque inputs | Do not fabricate dynamic results |
| `outputs/REFLECTED_INERTIA.csv` | Ratio-related inertia analysis and reference convention | Record convention/data gap; do not substitute guessed values |
| `outputs/GRAVITY_TORQUE_SWEEP.csv` | Gravity torque versus angle, if present in the current baseline | Verify path and revision before use |

Record each artifact's exact repository path, commit/revision, generation date, units, column definitions, status and reviewer disposition in the calculation notes. If multiple versions exist, use the approved version or escalate the ambiguity.

FS-M-004 must explicitly identify the stop-impact cases from FS-M-002 and use their defined assumptions. Independent review is required for impact/peak conclusions. Do not treat IN-019's estimated impact torque as a validated gearbox rating requirement without checking its provenance and the relevant FS-M-002 assessment.

## 4. FS-M-003 Motor Dependencies

Upstream study: `kritva-m/FS-M-003-motor-selection-sizing/`.

Required motor-side data, per exact candidate and source:

- Continuous and peak torque-speed curves.
- Rated and maximum speed; operating points at the target gearbox input speeds.
- Torque constant, speed constant and winding/electrical limits when published.
- Continuous and peak current, thermal limits and peak duration constraints.
- Rotor inertia, mass, envelope, shaft and mounting interface.
- Feedback arrangement and integration constraints.
- Motor efficiency and operating-point assumptions, where available.

The gearbox study and motor study are peers and must iterate jointly. Do not assume that a motor is compatible merely because its rated power is within IN-013. Document the motor/gearbox pair and ratio for every joint feasibility claim.

## 5. Section A - Study-Local Inputs

These local inputs establish the research and calculation fields. They do not imply that candidate evidence already exists.

| ID | Input | Units / format | Initial status | Required evidence / handling |
|---|---|---|---|---|
| FS4-IN-001 | Candidate manufacturer and exact model | Text | UNKNOWN | Manufacturer datasheet/manual or written confirmation |
| FS4-IN-002 | Gearbox topology and stage count | Single/two stage; text | UNKNOWN | Exact model documentation |
| FS4-IN-003 | Nominal reduction ratio and tolerance, if stated | Ratio | UNKNOWN | Manufacturer specification |
| FS4-IN-004 | Rated continuous output torque and conditions | N·m, speed, temperature, duty | UNKNOWN | Datasheet with operating conditions |
| FS4-IN-005 | Intermittent/peak output torque and permitted duration | N·m, s, duty/recovery | UNKNOWN | Exact rating definition; no extrapolation |
| FS4-IN-006 | Emergency-stop/shock/impact torque capacity | N·m and conditions | UNKNOWN | Explicit manufacturer rating or written confirmation |
| FS4-IN-007 | Maximum and rated input speed | RPM | UNKNOWN | Manufacturer specification |
| FS4-IN-008 | Efficiency versus load/speed/ratio | %, operating points | UNKNOWN | Manufacturer curves or documented test data |
| FS4-IN-009 | Backlash and measurement conditions | arcmin or degrees | UNKNOWN | Manufacturer tolerance and test conditions |
| FS4-IN-010 | Permissible radial load | N and reference distance | UNKNOWN | Manufacturer load chart |
| FS4-IN-011 | Permissible axial load | N and direction | UNKNOWN | Manufacturer load chart |
| FS4-IN-012 | Permissible tilting moment | N·m and conditions | UNKNOWN | Manufacturer specification |
| FS4-IN-013 | Output interface | Drawing, bore/shaft/flange dimensions | UNKNOWN | Dimensioned drawing and tolerance details |
| FS4-IN-014 | Input interface and motor mounting | Drawing/dimensions | UNKNOWN | Manufacturer drawing and compatibility review |
| FS4-IN-015 | Gearbox output-bearing configuration and load role | Text, ratings | UNKNOWN | Manufacturer documentation; arm loads bypass by default |
| FS4-IN-016 | Life rating and rating basis | Hours/cycles/revolutions, conditions | UNKNOWN | Manufacturer calculation method and duty assumptions |
| FS4-IN-017 | Lubrication and maintenance | Type, interval, orientation | UNKNOWN | Manufacturer manual |
| FS4-IN-018 | Ambient and operating temperature limits | °C | UNKNOWN | Manufacturer specification |
| FS4-IN-019 | Mass and package envelope | kg, mm | UNKNOWN | Exact model datasheet/drawing |
| FS4-IN-020 | Noise/vibration information | dB or stated limits | UNKNOWN | Manufacturer evidence, if published |
| FS4-IN-021 | Backdrivability/drag or friction data | Units and conditions | UNKNOWN | Manufacturer data or clearly labelled measurement |
| FS4-IN-022 | Input/output inertia and convention | kg·m² | UNKNOWN | Manufacturer data; identify reference axis |
| FS4-IN-023 | Replacement/serviceability | Text | UNKNOWN | Mounting, availability and disassembly evidence |
| FS4-IN-024 | Price and quote conditions | Currency, amount, date | UNKNOWN | Dated quote or clearly identified listing |
| FS4-IN-025 | India sourcing and lead time | Supplier, location, lead time | UNKNOWN | Supplier evidence; distinguish stock from request-to-quote |
| FS4-IN-026 | Source provenance and revision | URL/path, date, page/table | UNKNOWN | Required for every candidate claim |

Add rows with new `FS4-IN-nnn` IDs when necessary. Do not reuse an ID for a different input. Record candidate data per candidate, not collapsed into a single assumed value.

## 6. Ratio Calculation Conventions

For output speed n_o and reduction ratio i (motor speed / output speed, consistent with FS3-IN-001):

    n_in = i * n_o

For an idealized efficiency calculation:

    T_o ~= T_in * i * eta

This approximation is for screening only. It does not replace a manufacturer's torque rating or the motor's torque-speed curve. Record the efficiency used, its source and the operating point. If a manufacturer's published data uses a different convention, document it.

Primary ratios: 15:1, 20:1 and 25:1. Include 37:1 only as an IN-039 comparison. At 45 RPM output, arithmetic input-speed comparisons are 675, 900, 1125 and 1665 RPM respectively; candidate input-speed limits and motor feasibility remain to be verified.

For reflected inertia, use the convention documented by FS-M-002 and the candidate source. Do not mix motor-side and output-side inertia. If a theoretical transformation is calculated, state the assumptions and distinguish it from manufacturer-published data.

## 7. Interface and Load-Path Inputs

Check every candidate against:

- SYS-REQ-033 preferred gearbox output interface of at least 8 mm.
- IN-015 preliminary independent 12 mm shaft.
- IN-016 assumed 6202 bearing / 15 mm seat mismatch.
- SYS-REQ-032 arm-load bypass requirement.
- SYS-REQ-036 independent replacement requirement.

An 8 mm preferred interface does not mean an 8 mm shaft is mandatory, and a 12 mm independent shaft does not prove that a gearbox accepts a 12 mm bore or shaft. Record actual interface geometry, fits, retention, axial support, radial-load path and adapter needs. If a custom adapter or bearing support is required, record the associated design dependency.

## 8. Input Change Control

Any changed upstream value must be changed in its authoritative source first, reviewed and linked to the new revision. Update dependent calculations and record the impact on ratio ranking and candidate feasibility. Never silently upgrade PRELIMINARY, ASSUMED or UNKNOWN inputs to confirmed values.

## 9. Input Completeness Gate

Before making a definitive recommendation, verify that:

- FS-M-002 load, dynamic torque and reflected-inertia outputs are available and versioned.
- FS-M-003 candidate motor operating points are available for the compared ratios.
- Candidate ratings cover the relevant continuous, peak and emergency/impact cases, or the gaps are explicitly blocking.
- Duty cycle, life, peak duration/repetition, backlash target and ambient limits are resolved or identified as decision blockers.
- Output-bearing load path and shaft/bearing interface compatibility are documented.
- Every material numerical claim has traceable evidence.

If these conditions are not met, the study may still produce a provisional shortlist, but it must not claim confirmed suitability or release readiness.

## 10. Repository starting evidence (as of 2026-10-24)

The repository already holds draft calculation and design documents that overlap this study. They are **starting points, not verified evidence**: each is a draft pending approval, none has been independently reviewed, and several figures were gathered by an AI reviewer session and not re-checked against vendor pages. Read them first, then reproduce or re-source what you rely on and register it in `references/SOURCE_REGISTER.csv`. They do not change the status of any upstream input.

| Source | What it gives | Limits |
|---|---|---|
| `mechanical/calculations/MOTOR_GEARBOX_SHORTLIST.md` (rev 0.2) section 2.3 and 3.2 | Seed gearboxes: Neugart PLE 040, PLE 060, PLPE 050 (series-level ranges for continuous, maximum and emergency-stop torque, backlash, efficiency, mass) and WITTENSTEIN alpha DP+ as a benchmark | Series ranges, not part-number ratings; reported by an AI reviewer session and not re-checked. No gearbox price exists online, so every cost is unknown |
| `mechanical/calculations/GEARBOX_SELECTION.md` sections 2 to 6 | Required ratings from the load cases, the joint selection rule, a comparison template and a scoring method | Comparison rows are empty by design |
| `mechanical/calculations/TORQUE_AND_SPEED.md` section 3 | Motor-side torque by ratio | Illustrative |

Points to resolve, not assume:

- Efficiency: the repository uses 0.85 (IN-012, ASSUMED); the AI session used 0.92; the quoted datasheet range is 92 to 98 %. Do not change IN-012 here. Run both as sensitivity cases.
- The shortlist reports that only PLE 060 clears the 47.5 N·m screening stop torque (emergency-stop rating). That stop torque is an idealised estimate that depends on bumper and approach speed; do not eliminate candidates on it alone.
- Motor and gearbox are selected jointly (`TORQUE_AND_SPEED.md` section 5): this study depends on the FS-M-003 candidate operating points.
Child requirement documents also exist and are not yet reconciled with this study: `requirements/MECHANICAL_REQUIREMENTS.md` (MECH-REQ-nnn) and `requirements/ELECTRICAL_REQUIREMENTS.md` (ELEC-REQ-nnn). Check which IDs apply and cite them by ID.
