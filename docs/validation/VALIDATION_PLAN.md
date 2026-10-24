# Kritva Actuator: Validation Plan

| Field | Value |
|---|---|
| Document ID | KA-DOC-VAL-PLAN |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead (coordination); interns execute their domain tests |
| Reviewer / Approver | Independent Mechanical Reviewer; Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A0, A1, A2 |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** This plan is proposed and pending approval. Numerical pass limits that are not yet set (backlash, position error, repeatability, thermal stability) **must be approved and recorded before the related test is run**. They are never chosen after seeing the results.

---

## 1. Purpose

This plan defines **how every requirement is verified**, in what order, on what setup and with what evidence. It also defines how verification feeds Gates A, B and C and the milestone exits. Test procedures live in `tests/`, measured evidence in `results/`, and status in `audit/requirements_traceability/REQUIREMENTS_TRACEABILITY.csv`.

## 2. Verification principles

1. **Evidence, not documents.** A requirement is `PASS` only with the specified evidence (SYS-REQ-102).
2. **Pre-approved criteria.** Each test has its pass criterion approved in the task `ACCEPTANCE_CRITERIA.md` before execution.
3. **Restrained fixture.** All loaded, peak, impact and fault tests happen on the guarded fixture (ACT-DEC-015). Nobody resists the actuator by hand.
4. **Staged load.** No load → 25 % → 50 % → 100 % of continuous → peak (SAF-REQ-063).
5. **Complete records.** Hardware revision, firmware version, supply voltage, load, ambient temperature, instruments, operator, observer and results (SYS-REQ-103).
6. **Independent review** of safety-critical evidence. Without it, the item is `NOT_VERIFIED` and the gate is blocked.

## 3. Verification methods

| Method | Code | Typical evidence |
|---|---|---|
| Test | T | Test record in `results/`, data files, plots |
| Analysis | A | Calculation in `mechanical/calculations/` or `docs/`, independently recalculated |
| Inspection | I | Inspection sheet, review record, photographs |
| Demonstration | D | Demonstration record (video optional), with the observer named |

## 4. Test campaigns

| Campaign | ID prefix | Milestone | Setup | Owner | Main requirements |
|---|---|---|---|---|---|
| Bring-up | BU-00…BU-15 | A0 (repeated A1) | Development board / PCB, motor clamped | Electronics/Embedded Intern | SYS-REQ-040–055, 080, 084 |
| Motor characterisation | MC-01…MC-08 | A0 | Motor on the fixture, optional dynamometer or brake | Electronics/Embedded Intern | SYS-REQ-042, 043 |
| Gearbox arrival checks | GB-01…GB-05 | A1 | Bench (GEARBOX_SELECTION §6) | Mechanical Intern | SYS-REQ-003, 004, 025, 027 |
| Mechanical inspection | MI-01…MI-10 | A1 | Assembly (ASSEMBLY_PROCEDURE §7) | Mechanical Intern | SYS-REQ-030–038 |
| Performance characterisation | PC-01…PC-14 | A1 | Integrated actuator on the fixture | Both | SYS-REQ-012, 020–028 |
| Fault injection | FI-01…FI-24 | A0/A1 | Per SAFETY_REQUIREMENTS §8 | Electronics/Embedded Intern (with Mechanical for FI-23/24) | SYS-REQ-063, 080–085 |
| Communication and interface conformance | CT-01…CT-08, CAN-01…CAN-10 | A1/A2 | Host, USB-CAN, analyser | Project Lead | SYS-REQ-060–067 |
| Integration | INT-01…INT-08 | A2 | Edge / host, SimulatedActuator then hardware | Project Lead | SYS-REQ-064, 065 |
| Durability | DU-01…DU-03 | A1 | Cycling on the fixture | Mechanical Intern | SYS-REQ-091, 092 |

Performance tests are defined in `PERFORMANCE_CHARACTERIZATION.md`. Equipment is listed in `TEST_EQUIPMENT.md`.

## 5. Test sequence and gate mapping

```
A0:  BU-00..BU-06 (protections first) -> BU-07..BU-12 -> MC-01..MC-08 -> BU-13..BU-15 -> FI (A0 subset) -> A0 exit
A1:  Gate A (design release: analyses + reviews) -> fabrication -> MI-01..MI-10 -> GB-01..GB-05
     -> BU on the PCB (if fitted) -> FI-01..FI-17 (no load) -> staged load PC-01..PC-14 -> FI-18..FI-24
     -> DU-01..DU-03 -> post-test inspection -> Gate B -> safety evidence review -> Gate C -> A1 exit
A2:  CT-01..CT-08 on SimulatedActuator -> on hardware -> CAN-01..CAN-10 -> INT-01..INT-08 -> A2 exit
```

| Gate | Required evidence |
|---|---|
| **Gate A: design release** | LOAD_CASES, TORQUE_AND_SPEED, SHAFT_STRENGTH, BEARING_SELECTION and GEARBOX_SELECTION reviewed; CAD assembly review (M2); BOM with quotations; independent design audit with no open CRITICAL or HIGH findings; centre of mass from CAD or measurement |
| **Gate B: bench validation** | PC-01 (hold 1.5 kg + 1 kg horizontal), PC-02 (T_g verification), PC-03 (10 N·m continuous thermal), PC-04 (peak), PC-05 (speed incl. 45 RPM), PC-07–PC-09 (position error, repeatability, backlash), MI post-test inspection, complete records |
| **Gate C: safety and release** | FI-01–FI-24 results; hard-stop and pinch-point review; peak and failure behaviour documented; all failures dispositioned; qualified reviewer approval |

## 6. Requirement-to-test matrix (system level)

The full matrix, including child requirements, is in the traceability CSV.

| SYS-REQ | Verification | Test / analysis |
|---|---|---|
| 010–012 | A, T | LOAD_CASES; PC-01, PC-02 |
| 013, 014 | I, A | Decision records; LOAD_CASES §5 |
| 020 | T | PC-03 |
| 021 | T | PC-04 |
| 022 | T | PC-05 |
| 023 | I, T | MI-07, PC-06 |
| 024, 052 | I, T | Calibration C5/C6; PC-07 |
| 025 | T | PC-07, PC-08, PC-09 |
| 026, 051 | T | BU-09–BU-11; PC-10 |
| 027 | A, T | TORQUE_AND_SPEED §7; PC-11 (backdrive), PC-12 (reflected inertia) |
| 028 | A, T | PC-13 (efficiency) |
| 030–034 | A, I | SHAFT_STRENGTH, BEARING_SELECTION; MI-01–MI-06 |
| 035, 082 | I, T | MI-08; FI-18, FI-24 |
| 040–045 | T, A, I | BU-02, BU-04, BU-13–BU-15; MOTOR_CONTROLLER_SPECIFICATION |
| 050, 053 | I, T, D | BU-08, BU-09; CALIBRATION_PROCEDURE |
| 060–067 | D, T | CT-01–CT-08; CAN-01–CAN-10 |
| 080–085 | T, I | FI-01–FI-24; Gate C review |
| 091, 092 | A, I, T | DU-01–DU-03; post-test inspection |
| 100–107 | I | Release audit |

## 7. Communication and interface tests (A1/A2)

| ID | Test | Pass criterion |
|---|---|---|
| CAN-01 | Bit timing and error-free operation at 1 Mbit/s for 30 min (TBC) | Error counters 0 |
| CAN-02 | 500 Hz setpoint/feedback sustained | No missed feedback frames; latency ≤ 1 ms (TBC) |
| CAN-03 | 1 kHz (goal) | Recorded |
| CAN-04 | Heartbeat in all states at 10 Hz | Present; counter increments |
| CAN-05 | Fault event latency | ≤ one feedback period |
| CAN-06 | Alive-counter stale-frame rejection | Rejected; counted |
| CAN-07 | Broadcast setpoint ignored; STOP_ALL works | As specified |
| CAN-08 | Bus-off → safe state | Within the timeout |
| CAN-09 | Parameter read/write during 500 Hz operation | Latency limits kept |
| CAN-10 | Version mismatch handling | `E_VERSION_MISMATCH` |

## 8. Durability tests (A1)

| ID | Test | Pass criterion |
|---|---|---|
| DU-01 | 1 000 cycles 0 → 90 → 0° with the arm and payload at 30 RPM (TBC) | No fault except the expected thermal warnings; no change in backlash beyond the limit (TBD) |
| DU-02 | Thermal soak: 10 N·m continuous until stable, repeated 3 times | Repeatable temperatures |
| DU-03 | Impact series (FI-24 staged) of 20 impacts at the approved approach speed | No damage; encoder calibration unchanged |

## 9. Non-conformance handling

1. Stop the test if it is safety-related. Record the result as `FAIL` with the data.
2. Open a `test_failure` Issue with the containment action.
3. Root cause analysis, then a disposition: rework, retest, or a requirement change through a DCR. A requirement change is **never** made just to make the test pass.
4. The reviewer verifies the closure. Safety-critical failures cannot be accepted as-is.

## 10. Roles

| Role | Responsibility |
|---|---|
| Project Lead | Approves the test plans and pass criteria, coordinates campaigns, signs the gates |
| Mechanical Intern | Mechanical tests, fixture, inspections |
| Electronics/Embedded Intern | Electrical, firmware and fault-injection tests |
| Independent reviewers | Review the evidence; record `NOT_VERIFIED` if they cannot verify it |
| Observer | Second person for loaded tests (SAF-REQ-064) |

## 11. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | Approve the numerical limits for backlash, position error, repeatability and thermal stability | Project Lead | Before Gate B tests |
| 2 | Durability cycle counts and speeds | Project Lead | Before DU tests |
| 3 | Availability of the test equipment (TEST_EQUIPMENT gaps) | Project Lead | Week 4 |

## 12. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
