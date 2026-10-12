# Kritva Actuator v1: Risks and Dependencies

| Field | Value |
|---|---|
| Document ID | KA-PLAN-RISKS |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead |
| Reviewer / Approver | Project Lead |
| Applies to | A0, A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** The risk scores and mitigations are a proposed initial assessment, pending approval. They are reviewed weekly. Binding decisions arising from this register are recorded in `planning/v1/DECISIONS.md`.

---

## 1. Purpose and boundaries

This document holds the **project-level** risk register (technical, schedule, procurement, cost, skills, safety-process, integration and documentation risks) and the **dependency register** for v1. It also gives the critical-path analysis.

Two related registers live elsewhere and are not duplicated here:

- **Mechanical failure modes** (shaft fracture, bearing overload and so on) are in `audit/mechanical/MECHANICAL_RISK_REGISTER.md`.
- **Safety hazards** (HAZ-NNN) and their controls are in `requirements/SAFETY_REQUIREMENTS.md`.

Where a project risk relates to either of these, it is cross-referenced.

## 2. Scoring

Likelihood (L) and Impact (I) are each scored 1–5. Score = L × I.

| Score | Rating | Action |
|---|---|---|
| 1–6 | Low | Monitor |
| 7–12 | Medium | Mitigation plan with an owner |
| 15–25 | High | Active mitigation; Project Lead reviews weekly; contingency prepared |

| Level | Likelihood | Impact (schedule / cost / technical) |
|---|---|---|
| 1 | Rare | < 2 days slip; < ₹500; negligible |
| 2 | Unlikely | ≤ 1 week; ≤ ₹2,000; minor rework |
| 3 | Possible | 1–2 weeks; ≤ ₹5,000; one deliverable reduced |
| 4 | Likely | 2–4 weeks; ≤ ₹10,000; a milestone exit at risk |
| 5 | Almost certain | > 4 weeks; > ₹10,000; a milestone objective lost |

## 3. Risk register

| ID | Category | Risk | Cause | Effect | L | I | Score | Mitigation | Contingency | Owner | Trigger | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RISK-001 | Technical | No affordable commercial motor matches 0.59 N·m continuous at 900 RPM (20:1) at 24 V | Typical 24 V BLDCs are rated about 3000 RPM with low torque | Motor and ratio mismatch; underperformance or overheating | 4 | 4 | 16 High | Treat motor class and ratio as a joint trade study (GEARBOX_SELECTION.md); widen the ratio set to 25:1 or higher if needed; consider low-Kv outrunner/pancake motors | Lower the continuous target with a recorded decision; use a two-stage gearbox | Mechanical Intern | No candidate meets the operating point by week 2 | Open |
| RISK-002 | Technical | Commercial planetary gearbox backlash is too large for the position-accuracy goal | Low-cost gearboxes often have backlash of several arc-minutes or more | Position error; limit cycling | 3 | 3 | 9 Medium | Request backlash data; measure on arrival; use the output encoder in the loop | Choose a higher-grade gearbox for A1; accept a higher limit for A0 | Mechanical Intern | Datasheet backlash unknown or measured above the approved limit | Open |
| RISK-003 | Technical | Gearbox output bearing cannot take the arm loads | Gearbox not rated for overhung loads | Gearbox failure | 3 | 4 | 12 Medium | Independent shaft on a dedicated bearing pair (ACT-DEC-009); flexible or Oldham coupling to isolate loads | Redesign the coupling | Mechanical Intern | Load calculation exceeds the gearbox rating | Open (mitigated by design) |
| RISK-004 | Technical | FOC bring-up takes longer than planned | Sensor noise, alignment and tuning issues; intern learning curve | A0 slips | 4 | 3 | 12 Medium | Start from a proven board and reference library (SimpleFOC/vendor SDK); incremental bring-up procedure (HARDWARE_BRINGUP.md) | Use the vendor motor-control SDK for A0; develop in-house FOC in parallel | Electronics/Embedded Intern | No stable current loop by week 5 | Open |
| RISK-005 | Technical | Development-board current rating is insufficient for the motor peak current | Small ESC boards have limited continuous current | Board damage; cannot test peak torque | 3 | 3 | 9 Medium | Compute phase currents from Kt before selecting the board (ELECTRICAL_REQUIREMENTS §5) | Test peak torque only on the A1 PCB; use a higher-rated power board | Electronics/Embedded Intern | Peak phase current above the board rating | Open |
| RISK-006 | Technical | Output encoder misalignment or magnet slip | Poor mount design; shaft deflection | Position error; ENCODER_MISMATCH faults | 3 | 3 | 9 Medium | Mount design reviewed at M2; alignment tolerance analysis; magnet bonded and keyed | Re-machine the mount | Mechanical Intern | Mismatch faults in testing | Open |
| RISK-007 | Technical | Thermal limit prevents 10 N·m continuous | Motor copper losses; poor heat path | Continuous rating not met | 3 | 4 | 12 Medium | Thermal estimate at selection; heat path to the housing; measure in A0 | Reduce the continuous rating via a decision; add a heat sink | Electronics/Embedded Intern | A0 thermal test exceeds the limits | Open |
| RISK-008 | Technical | Regenerated energy trips the bench PSU or damages hardware | Backdriving or deceleration with a PSU that cannot sink current | Damage; unreliable tests | 3 | 3 | 9 Medium | Bus-voltage limiting; clamp or brake resistor; PSU choice (HAZ-012) | Series diode plus clamp module | Electronics/Embedded Intern | Bus spikes > 30 V | Open |
| RISK-009 | Technical | 3D-printed parts deform under load or heat | Material creep; temperature | Misalignment; failure | 3 | 3 | 9 Medium | Metal for the load path (SAF-REQ-043); prints only for non-structural parts | Machine the affected parts | Mechanical Intern | Deformation at inspection | Open |
| RISK-010 | Schedule | Motor and gearbox lead time from suppliers in India or imports | Stock and customs | Weeks 3–6 slip | 4 | 4 | 16 High | Order candidates in week 2; shortlist with stock confirmation; consider two candidates | Start A0 on any available 24 V BLDC for FOC learning | Mechanical Intern | No delivery date by the end of week 2 | Open |
| RISK-011 | Schedule | Custom PCB fabrication and assembly delay | Fab and assembly lead times; design iterations | A1 PCB late | 4 | 3 | 12 Medium | Development-board prototype is the primary milestone; PCB is not a prerequisite for A0 | Move the PCB to the second iteration (decision) | Electronics/Embedded Intern | PCB not ordered by week 8 | Open |
| RISK-012 | Schedule | Reviewer availability for gates | No qualified independent reviewer at the gate date | Gates blocked (NOT_VERIFIED) | 3 | 4 | 12 Medium | Name reviewers in week 1; book gate dates; remote review with ChatGPT for preparation (not sole authority) | Hold the gate; continue non-dependent work | Project Lead | Reviewer not named by week 1 | Open |
| RISK-013 | Schedule | Machining capacity and turnaround for the housing and shaft | Local workshop availability | Weeks 6–7 slip | 3 | 3 | 9 Medium | Identify two workshops in week 3; simple-to-machine design | Prints for the A0 fixture; metal only for the shaft and bearing seats | Mechanical Intern | No quote by week 4 | Open |
| RISK-014 | Cost | A1 exceeds ₹20,000–₹30,000 cumulative | Gearbox quality, PCB, machining | Budget overrun | 3 | 3 | 9 Medium | BOM with real quotations (SYS-REQ-105); weekly budget review | Re-scope A1 (reuse the A0 board) | Project Lead | Forecast > ₹30,000 | Open |
| RISK-015 | Cost | Low-cost gearbox is unsuitable and has to be bought twice | Insufficient datasheet ratings | Extra cost; delay | 3 | 3 | 9 Medium | Demand ratings before purchase; M1 review | Budget reserve ₹3,000 (TBC) | Mechanical Intern | Missing ratings | Open |
| RISK-016 | Cost | Lab equipment not available (oscilloscope, current probe, torque fixture) | Not in the prototype budget | Cannot verify key requirements | 3 | 4 | 12 Medium | TEST_EQUIPMENT.md lists needs; borrow or rent; low-cost alternatives (load arm with weights) | Defer specific tests; record as NOT_VERIFIED | Project Lead | Equipment missing at week 5 | Open |
| RISK-017 | Skills | Interns are new to FOC, power electronics or bearing design | Educational programme | Slower progress; design errors | 4 | 3 | 12 Medium | Structured learning in week 1; references; reviews at each gate; pairing | Project Lead support; simplify scope | Project Lead | Gate findings show fundamental gaps | Open |
| RISK-018 | Skills | Intern unavailability (illness, exams) | Internship constraints | Workstream stall | 2 | 4 | 8 Medium | Documentation discipline; the other intern can resume from records | Re-plan the milestones | Project Lead | Absence > 1 week | Open |
| RISK-019 | Safety process | Testing performed outside the fixture or without guarding | Schedule pressure | Injury; damage (HAZ-006, HAZ-009) | 2 | 5 | 10 Medium | ACT-DEC-015; briefing; two-person rule for loaded tests; test-record checklist | Stop testing; incident review | Project Lead | Any observed violation | Open |
| RISK-020 | Safety process | Safety-critical defect waived to meet a deadline | Schedule pressure | Unsafe release | 2 | 5 | 10 Medium | SAF-REQ-083; gate rules; independent reviewer | Gate held | Project Lead | Pressure to waive a finding | Open |
| RISK-021 | Integration | Motor, gearbox and encoder interfaces chosen independently by the two interns | Poor coordination | Incompatible parts; rework | 3 | 4 | 12 Medium | Joint selection rule; mid-week sync; interface control in INTERFACE_REQUIREMENTS | Rework the mounts | Project Lead | Selections made without a joint review | Open |
| RISK-022 | Integration | KritvaOS Edge not ready for A2 | Separate team or schedule | A2 demonstration limited to a host PC | 3 | 3 | 9 Medium | Host-PC driver and SimulatedActuator first; agree the Edge interface early | Demonstrate from Linux host tools | Project Lead | Edge interface not agreed by week 6 | Open |
| RISK-023 | Integration | CAN protocol changes break host tools | Protocol not frozen | Rework; incompatibility | 3 | 2 | 6 Low | Protocol versioning; conformance tests | Version negotiation | Project Lead | Late protocol changes | Open |
| RISK-024 | Documentation | Documents diverge from implementation | Duplicated content; no update discipline | Wrong decisions; failed audits | 3 | 3 | 9 Medium | One canonical home; CI checks (`make check`); traceability CSV updates are part of the definition of done | Documentation sprint in week 11 | Project Lead | check-trace or check-links failures | Open |
| RISK-025 | Documentation | Large CAD and binary files bloat the repository | Committing exports and builds | Slow repository; lost history | 3 | 2 | 6 Low | `.gitignore`, `.gitattributes` (LFS); CONTRIBUTING policy | Move to LFS; history clean-up | Mechanical Intern | Repository > 500 MB | Open |
| RISK-026 | Legal / IP | Open-source code reused without a licence review | Copying from references | IP contamination of the proprietary code | 2 | 4 | 8 Medium | FW-REQ-074 third-party register; PR checklist | Rewrite affected modules | Electronics/Embedded Intern | Third-party code found in review | Open |
| RISK-027 | Requirements | Load-model assumptions (180 mm centre of mass, payload) prove wrong | Arm CAD not available | Torque targets wrong | 3 | 4 | 12 Medium | Replace with CAD or measurement (SYS-REQ-011); sensitivity table in ACTUATOR_SPECIFICATION | Re-run the sizing; choose a different ratio | Mechanical Intern | CAD centre of mass differs by > 10 % | Open |
| RISK-028 | Requirements | Missing dynamic requirements (acceleration, duty cycle) | Not yet defined | Motor undersized for dynamics | 4 | 3 | 12 Medium | Define them before the motor/gearbox freeze (SYS-REQ-013) | Margin in the peak torque | Project Lead | Not defined by week 2 | Open |

### 3.1 Top-5 risks (week 0)

| Rank | ID | Score | Summary | Immediate action |
|---|---|---|---|---|
| 1 | RISK-001 | 16 | Motor/ratio match at 24 V | Run the motor-class versus ratio trade study in ACT-02-002 (week 2) |
| 2 | RISK-010 | 16 | Motor and gearbox lead time | Shortlist with stock confirmation; order in week 2 |
| 3 | RISK-004 | 12 | FOC bring-up duration | Choose a board with a proven SDK/reference |
| 4 | RISK-012 | 12 | Reviewer availability | Name reviewers in week 1 |
| 5 | RISK-028 | 12 | Dynamic requirements undefined | Define acceleration and duty cycle in ACT-02-001 |

## 4. Dependency register

| ID | Type | Dependency | From → To | Needed by (week) | Owner | Status |
|---|---|---|---|---|---|---|
| DEP-001 | Internal | Load cases complete before gearbox comparison | ACT-02-001 → ACT-02-002 | 1 → 2 | Mechanical Intern | Open |
| DEP-002 | Internal | Motor selection (joint) before board selection is finalised | ACT-02-002 ↔ ACT-01-002a | 2 | Both interns | Open |
| DEP-003 | Internal | Motor delivered before characterisation | Procurement → ACT-01-002b | 3 | Mechanical Intern | Open |
| DEP-004 | Internal | Shaft and bearing calculations before CAD freeze | ACT-02-003 → ACT-02-004 | 4 → 5 | Mechanical Intern | Open |
| DEP-005 | Internal | Gate A passed before fabrication | ACT-02-004 → ACT-02-005 | 5 → 6 | Project Lead | Open |
| DEP-006 | Internal | Encoder mount fabricated before joint-control tuning on the output encoder | ACT-02-005 → ACT-01-003 | 6 → 7 | Mechanical Intern | Open |
| DEP-007 | Internal | Software interface defined before the CAN protocol | ACT-03-001 → ACT-03-002 | 3 | Project Lead | Open |
| DEP-008 | Internal | CAN protocol before CAN firmware | ACT-03-002 → ACT-01-006 | 8 → 9 | Project Lead | Open |
| DEP-009 | Internal | PCB envelope from CAD before PCB layout | ACT-02-004 → ACT-01-005 | 5 → 6 | Mechanical Intern | Open |
| DEP-010 | Internal | Fixture ready before loaded tests | ACT-02-007 → ACT-02-006 / Gate B | 6 → 8 | Mechanical Intern | Open |
| DEP-011 | External | Motor and gearbox suppliers (datasheets with ratings; stock) | Supplier → ACT-02-002 | 2 | Mechanical Intern | Open |
| DEP-012 | External | Development board availability in India | Supplier → ACT-01-002a | 2 | Electronics/Embedded Intern | Open |
| DEP-013 | External | Machining workshop | Workshop → ACT-02-005 | 6 | Mechanical Intern | Open |
| DEP-014 | External | PCB fabrication and assembly house | Vendor → ACT-01-005 | 9 | Electronics/Embedded Intern | Open |
| DEP-015 | External | Laboratory equipment (oscilloscope, current probe, torque measurement, thermocouples) | Lab → validation | 4 | Project Lead | Open |
| DEP-016 | External | Independent reviewers (mechanical, electrical/firmware) | Reviewers → all gates | 1 | Project Lead | Open |
| DEP-017 | External | KritvaOS Edge interface and readiness | KritvaOS team → ACT-03-003/005 | 6 / 10 | Project Lead | Open |
| DEP-018 | External | Humanoid arm CAD (centre of mass, mass properties, mounting envelope) | Arm design → ACT-02-001 (SYS-REQ-011) | 4 (Gate A) | Project Lead | Open |

## 5. Critical-path analysis

```
Week:  1        2          3        4        5        6        7        8        9       10       11       12
ACT-02-001 -> ACT-02-002 -> [procurement lead time: motor + gearbox] -------+
                  |                                                          v
                  +-> ACT-02-003 -> ACT-02-004 -> Gate A -> ACT-02-005 -> integration -> ACT-02-006 -> Gate B
ACT-01-001 -> ACT-01-002a -> ACT-01-002b/c (needs motor) -> ACT-01-003 -> ACT-01-004 -------------^
ACT-03-001 -> ACT-03-002 -------------------------------------> ACT-01-006 -> ACT-03-003 -> ACT-03-005 -> Gate C
```

- **Critical path:** load cases → joint motor/gearbox selection → procurement → bring-up and fabrication → integration → Gate B → Gate C.
- **Float:** the custom PCB (ACT-01-005) and the simulation model (ACT-03-004) have float. They can slip to the second iteration without blocking A0 or the A1 development-board integration.
- **Schedule protection:** order the motor and gearbox no later than week 2. Begin FOC learning on any available motor if the selected motor is late (RISK-010 contingency).

## 6. Review cadence

- The Project Lead reviews this register **weekly** (Monday planning) and updates scores, statuses and the top-5.
- New risks are added by anyone through a pull request or an Issue. Closing a risk needs a short closure note.
- Gate reviews (M, E, F, A, B, C) confirm that no High risk affecting that gate is unmitigated.

## 7. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | Confirm the budget reserve value | Project Lead | Week 2 |
| 2 | Name the reviewers (DEP-016) | Project Lead | Week 1 |
| 3 | Confirm the arm CAD availability date (DEP-018) | Project Lead | Week 2 |

## 8. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
