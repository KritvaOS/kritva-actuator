# Kritva Actuator: Mechanical Release Checklist

| Field | Value |
|---|---|
| Document ID | KA-AUD-MECH-RELEASE |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Independent Mechanical Reviewer |
| Reviewer / Approver | Independent Mechanical Reviewer / Project Lead |
| Applies to | A1 |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** This checklist is used twice:
>
> - **Release 1:** release for fabrication, at Gate A;
> - **Release 2:** release for integration with the motor controller and the rest of the actuator, after M3.
>
> Every item needs evidence. An item without evidence is `NOT VERIFIED` and blocks the release.

---

## Release 1: design release for fabrication (Gate A)

| # | Check | Evidence | Result | Reviewer initials |
|---|---|---|---|---|
| R1-01 | Load cases complete; centre of mass from CAD or measurement; T_g recalculated | LOAD_CASES.md rev | NOT VERIFIED | |
| R1-02 | Motor and gearbox selected (ACT-DEC-016/017) with datasheets and quotations; M1 passed | DECISIONS.md; M1 record | NOT VERIFIED | |
| R1-03 | Shaft: combined stress, fatigue and deflection reviewed with the CAD geometry; SF ≥ the approved target | SHAFT_STRENGTH rev; M2 record | NOT VERIFIED | |
| R1-04 | Bearings: s0, life, fits, preload and coaxiality checked (ACT-DEC-019) | BEARING_SELECTION rev | NOT VERIFIED | |
| R1-05 | Hard stops: energy and stop torque within the ratings at the approved approach speed; reaction path into the housing | LOAD_CASES §8; M2 | NOT VERIFIED | |
| R1-06 | Housing stiffness check | M2 | NOT VERIFIED | |
| R1-07 | Encoder mount tolerance stack within the IC limits | M2 | NOT VERIFIED | |
| R1-08 | Drawings: material and condition, tolerances, finishes, critical features, title block, revision | `mechanical/drawings/` | NOT VERIFIED | |
| R1-09 | No printed parts in the load path (SAF-REQ-043) | Drawing review | NOT VERIFIED | |
| R1-10 | Fastener table (size, grade, torque, thread-locker) complete | ASSEMBLY_PROCEDURE §4 | NOT VERIFIED | |
| R1-11 | Pinch points identified; cable routing on the non-rotating side | CAD review | NOT VERIFIED | |
| R1-12 | Mechanical BOM: part numbers, suppliers, quotations | MECHANICAL_BOM.csv; `make check-bom` | NOT VERIFIED | |
| R1-13 | Fixture design reviewed (≥ 2 × peak; rest/catch; guard) | M2 | NOT VERIFIED | |
| R1-14 | Mechanical risk register: every RPN ≥ 40 item mitigated | MECHANICAL_RISK_REGISTER | NOT VERIFIED | |
| R1-15 | Independent design audit: no open CRITICAL or HIGH findings | MECHANICAL_DESIGN_AUDIT | NOT VERIFIED | |

**Release 1 decision**

| Reviewer | Decision | Date | Project Lead |
|---|---|---|---|
| | | | |

## Release 2: release for integration (after M3)

| # | Check | Evidence | Result | Reviewer initials |
|---|---|---|---|---|
| R2-01 | Parts inspected and conforming (or non-conformances dispositioned) | Inspection sheets | NOT VERIFIED | |
| R2-02 | Material certificates on file | `mechanical/assembly/` | NOT VERIFIED | |
| R2-03 | Assembly complete per procedure; torque log; witness marks | Assembly record | NOT VERIFIED | |
| R2-04 | Hand rotation smooth through the range; balanced stop contact | MI records | NOT VERIFIED | |
| R2-05 | Runout and axial play within limits | MI records | NOT VERIFIED | |
| R2-06 | Encoder air gap set; magnet bonded and cured | MI records | NOT VERIFIED | |
| R2-07 | Gearbox arrival checks passed | GB-01–05 | NOT VERIFIED | |
| R2-08 | Cable routing and strain relief inspected | Inspection | NOT VERIFIED | |
| R2-09 | Mass recorded against the budget | MI-09 | NOT VERIFIED | |
| R2-10 | Fixture inspected; e-stop functional | Pre-test checklist | NOT VERIFIED | |

**Release 2 decision**

| Reviewer | Decision | Date | Project Lead |
|---|---|---|---|
| | | | |

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
