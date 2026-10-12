# Kritva Actuator: Gearbox Selection

| Field | Value |
|---|---|
| Document ID | KA-CALC-GEARBOX |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Mechanical Intern (lead); Electronics/Embedded Intern (control implications) |
| Reviewer / Approver | Independent Mechanical Reviewer / Project Lead |
| Applies to | A0, A1 |
| Classification | Proprietary and confidential |

> **Status note.** ACT-DEC-003 sets the baseline: a commercial planetary gearbox, with 20:1 evaluated first and 15:1 and 25:1 as alternatives. **No gearbox model is selected yet.** This document defines the selection method, the required ratings, the comparison template and the release gate. Candidate rows are filled in during ACT-02-002 from real datasheets and quotations. They are never filled with invented data.

---

## 1. Purpose

This document provides a repeatable, auditable selection of the planetary gearbox. The selection is made **jointly** with the motor (joint selection rule), because the ratio, motor class, backlash, efficiency and backdrivability are coupled (`TORQUE_AND_SPEED.md` §5).

**Release gate (ACT-DEC-003).** The selected gearbox must satisfy the documented requirements and pass the mechanical design audit and the acceptance audit before the actuator design is approved for release.

## 2. Required gearbox ratings (from the load cases)

| Requirement | Value | Source | Notes |
|---|---|---|---|
| Ratio candidates | 20:1 first; 15:1, 25:1 alternatives (wider only by decision) | ACT-DEC-003 | Coupled to the motor class |
| Continuous output torque rating | ≥ **10 N·m** at the operating speed, temperature and life | ACT-DEC-008 | Check the manufacturer's definition (nominal or rated) |
| Peak / maximum output torque rating | ≥ **25 N·m** if the 25 N·m target is adopted (≥ 20 N·m minimum) | ACT-DEC-008 | Check the definition: acceleration torque, emergency-stop torque or repeated peak |
| Emergency / impact torque | ≥ the stop torque allowed by the design (≤ 20–25 N·m with speed limiting; see LOAD_CASES §8) | LC-04/LC-05 | If it is not published, ask the vendor |
| Rated input speed | ≥ 900 RPM continuous at 20:1 (675 / 1 125 RPM for 15 / 25:1) | TORQUE_AND_SPEED | Must not be the limiting factor |
| Efficiency | ≥ 85 % (sizing assumption); publish or measure | SYS-REQ-028 | A two-stage gearbox is typically lower than a single stage |
| Backlash | Datasheet value **required**; acceptance limit approved before test (TBD) | SYS-REQ-025 | Arc-minutes; standard and precision grades differ widely |
| Permitted output radial/axial load | Documented. The design keeps external loads **off** the gearbox output (ACT-DEC-009) | SYS-REQ-032 | Needed for the coupling misalignment check |
| Input interface | Compatible with the selected motor shaft (5–6 mm typical) and mounting pattern | SYS-REQ-033 | Clamp collar or keyed input |
| Output interface | ≥ 8 mm preferred, keyed or D-shaft | SYS-REQ-033 | Couples to the independent 12 mm shaft |
| Life | Rated hours at the continuous torque ≥ the life target (TBD; proposed 2 000 h) | SYS-REQ-091 | |
| Lubrication / orientation | Sealed, any orientation | — | The elbow rotates through 135° |
| Mass and size | Within the actuator mass and envelope budget (TBD) | SYS-REQ-039 | |
| Price and availability | Within the BOM allowance (planetary gearbox ₹2,000–₹4,000 target, provisional); stock or lead time ≤ 2 weeks preferred | SYS-REQ-100, RISK-010 | A quotation is required before ordering |

## 3. Motor and gearbox combinations to evaluate

From `TORQUE_AND_SPEED.md` §5 (illustrative motor classes):

| Combination | Motor class | Ratio | Comment |
|---|---|---|---|
| C-20 | 80–90 mm low-Kv pancake | 20:1 single-stage (or 15:1) | Best backdrivability; check the motor diameter against the envelope and cost |
| B-25 | 60–70 mm low-Kv outrunner | 25:1 (two-stage, typically) | Middle option |
| A-40 | 57 mm high-speed inrunner | ≈ 37–40:1 (two-stage) | Outside the current ratio set; needs a decision (RISK-001). Higher friction and less backdrivable |

**Planetary stage notes.**

- Single-stage planetaries typically cover about 3:1 to 10:1.
- Ratios of about 15–25:1 are usually **two-stage**, which brings lower efficiency (often around 80–90 %) and more backlash.
- Confirm the stage count and the efficiency on each datasheet.

## 4. Comparison template (filled in during ACT-02-002)

Fill one row per candidate from the **datasheet and the quotation**. Leave a field blank (and flag it) rather than guess.

| # | Manufacturer / model | Ratio | Stages | Rated output torque | Peak torque (definition) | Max input speed | Efficiency | Backlash | Permitted output radial / axial load | Input interface | Output interface | Mass | Price (₹, quote ref.) | Lead time | Datasheet link | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| G1 | | 20:1 | | | | | | | | | | | | | | |
| G2 | | 15:1 | | | | | | | | | | | | | | |
| G3 | | 25:1 | | | | | | | | | | | | | | |
| G4 | | | | | | | | | | | | | | | | |

## 5. Scoring method

A candidate is scored only if it passes **every mandatory screen**. Missing data counts as a fail until the data is supplied.

**Mandatory screens:**

1. Continuous rating ≥ 10 N·m.
2. Peak rating ≥ the adopted peak.
3. Input speed rating ≥ the motor speed at 45 RPM output.
4. A datasheet with ratings is available.
5. The interface is compatible with a shortlisted motor.

**Weighted score (for candidates that pass):**

| Criterion | Weight | Scoring guide (1–5) |
|---|---|---|
| Torque margin (rating / requirement) | 20 % | 1 = 1.0×; 5 = ≥ 2.0× |
| Backlash | 15 % | 5 = lowest among the candidates |
| Efficiency | 15 % | 5 = ≥ 90 % |
| Backdrivability (measured backdrive torque, or estimated from the ratio and stages) | 15 % | 5 = lowest |
| Cost (quoted) | 15 % | 5 = lowest within the budget |
| Availability / lead time | 10 % | 5 = in stock in India |
| Mass and size | 10 % | 5 = smallest that meets the ratings |

## 6. Acceptance checks on arrival (before integration)

| Check | Method | Criterion |
|---|---|---|
| Ratio | Count input revolutions per output revolution, or read the encoders | Matches the nominal ratio (exact) |
| Backlash | Lock the input, apply ±1 N·m (TBC) at the output, and measure with a dial indicator on an arm or with the output encoder | ≤ the approved limit |
| No-load backdrive torque | Spring scale on a lever at the output, motor disconnected | Recorded; compared across candidates |
| No-load running torque at the input | Measured at 900 RPM, on the motor current or a torque sensor | Recorded |
| Visual and noise | Inspection, listening at speed | No grinding or abnormal noise |

The results are recorded in `results/mechanical/` with the conditions required by SYS-REQ-103.

## 7. Integration rules

1. The **gearbox output drives the 12 mm shaft through a coupling** that tolerates the expected misalignment, such as an Oldham, jaw or bellows coupling. Alternatively, it uses a rigid connection only if the gearbox output bearing is rated for the induced loads (LC-09).
2. The gearbox housing is mounted to the actuator housing using its own flange pattern and a pilot for concentricity.
3. The motor-to-gearbox input connection follows the gearbox manufacturer's instructions (clamp torque, shaft engagement length).
4. External arm loads never pass through the gearbox (ACT-DEC-009).

## 8. Decision record

The final selection is recorded as **ACT-DEC-016** (gearbox model and ratio), with the comparison table, the scores and the M1 review reference. Until then, the ACT-DEC-003 baseline applies.

## 9. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | Shortlist of ≥ 3 commercial planetary gearboxes with datasheets and quotations | Mechanical Intern | Week 2 (M1) |
| 2 | Joint motor shortlist (see TORQUE_AND_SPEED §5) | Both interns | Week 2 |
| 3 | Backlash acceptance limit | Project Lead | Before the arrival checks |
| 4 | Decision if only ratios above 25:1 are feasible with the available motors | Project Lead | M1 |

## 10. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
