# ACT-02-001: Test and Verification Plan

| Field | Value |
|---|---|
| Document ID | KA-TASK-ACT-02-001-TP |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Mechanical Intern |
| Reviewer / Approver | Project Lead (scope approval) |
| Applies to | A1 |
| Classification | Proprietary and confidential |

> **Status note.** This plan is proposed, pending Project Lead approval of its scope. This task is mostly analysis. The physical verification of the load model happens later, at Gate B.

## 1. Verification activities

| # | Activity | Method | Instruments / tools | Expected result | Records |
|---|---|---|---|---|---|
| V1 | Independent recalculation of T_g | Analysis by the reviewer | Python or spreadsheet | 6.08 N·m ± 0.01 for the baseline inputs | REVIEW.md |
| V2 | Check of the unit and sign conventions | Inspection | `docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md` | Consistent N·m, m, kg, rad | REVIEW.md |
| V3 | Centre-of-mass measurement of the physical forearm (when it exists) | Test: balance method (support the link on a knife edge, or measure the reaction with two scales) | Two digital scales (±1 g), ruler | Centre-of-mass distance recorded ±2 mm | `results/mechanical/` |
| V4 | Mass of the forearm, hand and payload | Test | Scale ±1 g | Recorded | `results/mechanical/` |
| V5 | Gravity torque at the horizontal pose on the finished actuator (Gate B) | Test: hold the horizontal pose; read the estimated torque from the current; cross-check with a load arm and spring scale or torque sensor | Calibrated weight, load arm, torque sensor (TEST_EQUIPMENT.md) | Within the approved tolerance of the calculated T_g (tolerance TBD before the test) | `results/mechanical/` |

## 2. Test conditions to record (SYS-REQ-103)

For physical tests, record:

- hardware revision;
- firmware version (if powered);
- supply voltage;
- load;
- ambient temperature;
- instruments with their calibration status;
- operator and observer;
- measured results.

## 3. Safety

Physical tests V3–V5 use the restrained fixture (ACT-DEC-015). V5 is a loaded powered test and follows `requirements/SAFETY_REQUIREMENTS.md` SAF-REQ-060 to 066.

## 4. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
