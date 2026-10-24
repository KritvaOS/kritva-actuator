# Kritva Actuator v1: M0 Blocker Decision Sheet

| Field | Value |
|---|---|
| Document ID | KA-PLAN-M0-DECISIONS |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.3 (Draft: proposed, pending approval) |
| Date | 2026-10-13 |
| Document owner | Project Lead |
| Reviewer / Approver | Project Lead; independent reviewer for B6 (ACT-DEC-014) |
| Applies to | A0, A1 |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** This sheet turns the M0 blockers B1 to B7 of `audit/external/EXTERNAL_REPO_AUDIT_2026-10-12.md` §3 into decisions the Project Lead can take. The columns "External reviewer recommendation" come from the ChatGPT reviewer session (2026-10-13). The column "Author suggestion for discussion" is **not** from the reviewer and was **not adopted**: on 2026-10-13 the Project Lead decided to follow the external reviewer's recommendations. The suggestions are kept only as discussion notes. **Nothing here is approved.** M0 stays `FAIL / NOT READY TO CLOSE` until every row is closed with evidence (ACT-DEC-014).

---

## 1. How to use this sheet

1. For each blocker, read the recommendation and the suggestion.
2. Write the decision (or "CAD/measurement pending") in the **Decision** column and the approver and date.
3. Copy accepted values into `ACTUATOR_SPECIFICATION.md`, `LOAD_CASES.md` and `DECISIONS.md` (ACT-DEC-008), then re-run `make check`.
4. Ask the independent reviewer to verify the evidence column before M0 is marked PASS.

## 2. Decision table

| # | Blocker | External reviewer recommendation | Author suggestion for discussion | Closure evidence | Approver | Decision (to fill) |
|---|---|---|---|---|---|---|
| B1 | Forearm and hand mass properties, centre of mass | **CAD or measurement required.** Keep 1.5 kg at 180 mm plus 1.0 kg at 350 mm (T_g ≈ 6.08 N·m) as provisional only. Record configuration and uncertainty | None: do not guess. Re-run `make calc` with the measured values; `check_calcs.py` will flag every document that changes | CAD mass-properties report; weighing and balance (CoM) check on the prototype | Mechanical Intern; independent reviewer | **Adopted ChatGPT recommendation (2026-10-13):** provisional 1.5 kg at 180 mm until CAD/measurement; **OPEN, data pending** |
| B2 | Angular acceleration, duty cycle, horizontal holding duration | Define separate continuous, cyclic-motion and static-hold profiles. Do not assume zero acceleration or unlimited holding. Freeze the numbers only after the use case is documented | Design acceleration α = 10 rad/s² (the script's middle example): T = T_g + J·α ≈ 7.8 N·m (5 rad/s²: 6.9; 20 rad/s²: 9.5). Hold duration and duty cycle: Project Lead to state the use case | Approved motion-profile table; RMS and peak torque and thermal calculation; instrumented worst-case test | Project Lead; Safety reviewer | **Adopted ChatGPT recommendation:** separate continuous, cyclic and static-hold profiles; numeric α, duty and hold time not yet frozen; **OPEN, use case pending** |
| B3 | Peak torque (20 or 25 N·m) with duration, repetition and recovery | 20 N·m minimum peak capability. Keep 25 N·m as a stretch target, not an approved operating point. Define duration, repetitions, recovery and permitted temperature before selecting hardware | Adopt 20 N·m as the approved peak and 25 N·m as stretch; Project Lead sets duration (s), events per minute and recovery time | Approved torque-time-duty envelope; current limits; gearbox and motor ratings; repeated-stop test | Project Lead; Electrical/Controls; Safety reviewer | **Adopted ChatGPT recommendation:** 20 N·m minimum peak, 25 N·m stretch only; duration, repetition and recovery to be set before hardware selection (ACT-DEC-021); **OPEN, duty pending** |
| B4 | Final joint range, mass and envelope budget | Freeze an application-derived range, stop angles, maximum actuator mass and 3D envelope before component release. Do not invent numbers without the robot-level packaging requirements | Range: 0 to 135° (upper end of ACT-REQ-035 range). Mass and envelope: Project Lead plus robot architect to state | CAD assembly, swept-volume and collision analysis; mass roll-up; physical inspection of stops | Project Lead; Mechanical Intern | **Adopted ChatGPT recommendation:** freeze range, stops, mass and envelope from robot-level requirements; no invented values; **OPEN, data pending** |
| B5 | Numeric limits: position error, repeatability, backlash, thermal stability | Set numeric limits in an approved performance specification **before** testing, each with load, speed, direction, temperature, measurement method and pass/fail calculation. Values stay TBD pending robot-level requirements | Use these only as discussion starting points: backlash at output ≤ 0.5° (commercial planetary stages are typically a few tenths of a degree), position error and repeatability set from the robot's task accuracy, thermal stability = temperature rise < 1 K per 10 min | Approved test procedures and numeric table; calibrated encoder measurements; thermal-soak test | Project Lead; Validation lead | **Adopted ChatGPT recommendation:** numeric limits in an approved performance spec before testing; values TBD; **OPEN, data pending** |
| B6 | ACT-DEC-008 accepted, or blockers recorded | Keep PROPOSED until it records the accepted M0 operating envelope, peak-duty definition, numeric limits, required evidence and remaining blockers. A documentation update is not approval | Accept only after B1 to B5 have values; until then record the open blockers inside ACT-DEC-008 | Updated `DECISIONS.md` linking requirements, calculations, procedures and evidence; approver and date | Project Lead; independent reviewer | **Adopted ChatGPT recommendation:** ACT-DEC-008 stays PROPOSED until B1 to B5 have values; **OPEN** |
| B7 | Repository visibility (ACT-DEC-023) | Keep the repository **private** until an IP/confidentiality review approves a public release. If public is chosen, complete the licence, secrets, IP and tracked-artifact review first | Make the repository private now. Also run `git rm -r "Claude outputs"` (EXT-AUD-018) | ACT-DEC-023 recorded with rationale; GitHub visibility checked; history and secrets scan | Project Lead; IP/legal reviewer | **CLOSED 2026-10-13 (Project Lead):** repository moved to private; ACT-DEC-023 ACCEPTED (external reviewer recommendation adopted). History and secrets scan still recommended. **Superseded 2026-10-24 by ACT-DEC-034 (repositories stay public).** |

## 3. Closure rule

- B1 to B5 need approved inputs and objective evidence.
- B6 needs a recorded decision, reviewed independently.
- B7 needs an explicit visibility decision.
- M0 is PASS only when all seven are closed and the evidence is reviewed. A suggestion in this sheet is never evidence.

## 4. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-13 | Kritvaos Actuator Team | Initial decision sheet for blockers B1 to B7 |
| 0.2 | 2026-10-13 | Kritvaos Actuator Team | B7: interim decision recorded (stay public until the specification is filled in) |
| 0.3 | 2026-10-13 | Kritvaos Actuator Team | Decisions recorded: reviewer recommendations adopted for B1-B6 (values still pending); B7 closed (repository private) |
