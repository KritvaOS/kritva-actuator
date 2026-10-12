# Kritva Actuator: Release Audit (Gates A, B, C and Milestone Exits)

| Field | Value |
|---|---|
| Document ID | KA-AUD-RELEASE |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead |
| Reviewer / Approver | Independent Mechanical Reviewer; Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A0, A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** This is the release-gate framework. No gate has been passed. A gate is passed only when every item is supported by evidence and every required specialist has signed. If any required review is `NOT_VERIFIED`, the gate stays blocked (ACT-DEC-014).

---

## 1. Purpose

This document is the **single place where release gates are decided**:

- Gate A, design release;
- Gate B, bench validation;
- Gate C, safety and release;
- the milestone exits A0, A1 and A2.

It summarises, and links to, the domain audits. It does not repeat them.

## 2. Gate A: design release (before fabrication)

| # | Item | Evidence | Result |
|---|---|---|---|
| A-1 | CAD assembly includes the motor, gearbox, shaft, bearings, housing, encoder and a representative arm/link | M2 record | NOT VERIFIED |
| A-2 | Forearm/hand centre of mass measured or taken from CAD; gravity torque recalculated | LOAD_CASES rev; M2 | NOT VERIFIED |
| A-3 | Shaft combined bending/torsion, fatigue and deflection calculations reviewed | SHAFT_STRENGTH; M2 | NOT VERIFIED |
| A-4 | Bearing loads, life, fits, alignment and housing stiffness checked | BEARING_SELECTION; M2 | NOT VERIFIED |
| A-5 | Gearbox continuous/peak torque, efficiency, backlash, life, input speed and output-load ratings confirmed from manufacturer data | GEARBOX_SELECTION; M1 | NOT VERIFIED |
| A-6 | Mechanical BOM with exact part numbers, suppliers and current quotations | MECHANICAL_BOM.csv | NOT VERIFIED |
| A-7 | Independent design audit with no unresolved CRITICAL or HIGH findings | MECHANICAL_DESIGN_AUDIT | NOT VERIFIED |
| A-8 | Mechanical release checklist, Release 1, complete | MECHANICAL_RELEASE_CHECKLIST | NOT VERIFIED |
| A-9 | Electronics E1 (and E2 if the PCB is in scope) passed for the housing and connector interfaces | ELECTRONICS_DESIGN_AUDIT | NOT VERIFIED |

| Sign-off | Name | Decision | Date |
|---|---|---|---|
| Independent Mechanical Reviewer | | | |
| Project Lead | | | |

## 3. Gate B: bench validation

| # | Item | Evidence | Result |
|---|---|---|---|
| B-1 | Holds the representative 1.5 kg arm + 1 kg payload horizontally | PC-01 | NOT VERIFIED |
| B-2 | The ≈ 6.1 N·m gravity load is independently verified with the final mass properties | PC-02 | NOT VERIFIED |
| B-3 | 10 N·m continuous test on an instrumented fixture until the thermal-stability criterion is met | PC-03 | NOT VERIFIED |
| B-4 | Peak rating tested at its approved duration and duty cycle | PC-04 | NOT VERIFIED |
| B-5 | Speed measured across the load range, including 45 RPM | PC-05 | NOT VERIFIED |
| B-6 | Position error, repeatability and backlash measured against the pre-approved limits | PC-07–PC-09 | NOT VERIFIED |
| B-7 | No unacceptable deformation, loosening, bearing damage or encoder misalignment after testing | M3-15 | NOT VERIFIED |
| B-8 | Test records complete (HW rev, FW version, load, supply, ambient, instruments, results) | `results/` | NOT VERIFIED |
| B-9 | M3, E3 and F3 passed for the bench scope | Domain audits | NOT VERIFIED |

| Sign-off | Name | Decision | Date |
|---|---|---|---|
| Independent Mechanical Reviewer | | | |
| Independent Electrical/Firmware Reviewer | | | |
| Project Lead | | | |

## 4. Gate C: safety and release

| # | Item | Evidence | Result |
|---|---|---|---|
| C-1 | Current limit, overtemperature, encoder fault and e-stop behaviour tested | FI-01–FI-24 | NOT VERIFIED |
| C-2 | Mechanical hard stops and pinch-point guarding reviewed | M2/M3; SAF-REQ-040–042 | NOT VERIFIED |
| C-3 | Peak-torque and failure behaviour documented | PC-04; FI-24; report | NOT VERIFIED |
| C-4 | All test failures and deviations have traceable dispositions | Issues and non-conformance records | NOT VERIFIED |
| C-5 | Every SAF-REQ verified with evidence (none NOT_VERIFIED) | Traceability CSV (SAF rows) | NOT VERIFIED |
| C-6 | A qualified human reviewer approved the mechanical and electrical safety evidence | Signatures below | NOT VERIFIED |
| C-7 | Scope statement: approval covers **bench operation on a restrained fixture only** | This record | NOT VERIFIED |

| Sign-off | Name | Decision | Date |
|---|---|---|---|
| Independent Mechanical Reviewer | | | |
| Independent Electrical/Firmware Reviewer | | | |
| Project Lead | | | |

## 5. Milestone exits

| Milestone | Exit criteria (summary; detail in `planning/v1/MILESTONE.md`) | Required gates | Result | Date | Project Lead |
|---|---|---|---|---|---|
| **A0** Educational Motor Control | Motor controlled repeatably on the bench (current, velocity, position); operating limits documented; bring-up BU-00–BU-15 and motor characterisation MC-01–MC-08 recorded | E0, E1, E3 (development board), F0, F1, F2 (A0 scope) | NOT VERIFIED | | |
| **A1** Humanoid Smart Actuator | The integrated actuator meets the approved A1 requirements | Gates A, B, C; M4, E4, F4 | NOT VERIFIED | | |
| **A2** KritvaOS Integration | A host commands the actuator through the interface, observes its state and handles faults (CT, CAN, INT tests) | F3/F4 for A2 scope; INT-01–INT-08 | NOT VERIFIED | | |

**Deployment note.** Installing the actuator on the humanoid robot, or any human-interactive use, requires a **separate system-level safety review** (SAF-REQ-082). Passing A2 does not establish human-interactive safety.

## 6. Release log

| Release | Tag | Date | Scope | Gates passed | Approved by |
|---|---|---|---|---|---|
| — | | | | | |

## 7. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft (framework) |
