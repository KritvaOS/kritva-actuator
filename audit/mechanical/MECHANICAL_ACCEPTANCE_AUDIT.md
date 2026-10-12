# Kritva Actuator: Mechanical Acceptance Audit (M3–M4)

| Field | Value |
|---|---|
| Document ID | KA-AUD-MECH-ACCEPT |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Independent Mechanical Reviewer |
| Reviewer / Approver | Independent Mechanical Reviewer / Project Lead |
| Applies to | A1 |
| Classification | Proprietary and confidential |

> **Status note.** This is the acceptance-audit framework. No results have been recorded. Acceptance limits marked TBD must be approved **before** testing. Physical inspection by a qualified person is required; a remote review alone does not satisfy M3 or M4.

---

## 1. Purpose

This document records, criterion by criterion, whether the fabricated and tested mechanical assembly meets its approved requirements. It covers gate **M3 Prototype verification** (weeks 7–10) and gate **M4 Final acceptance audit** (weeks 11–12). It feeds Gates B and C in `audit/release/RELEASE_AUDIT.md`.

## 2. Record format

Every row records:

- the acceptance criterion and its requirement ID;
- the verification method;
- the required evidence;
- the observed result;
- PASS / PASS WITH ACTIONS / FAIL / NOT VERIFIED;
- reviewer comments;
- closure evidence for criteria that failed.

## 3. M3: Prototype verification

| # | Criterion | Req. | Method | Required evidence | Observed result | Status | Reviewer comment | Closure evidence |
|---|---|---|---|---|---|---|---|---|
| M3-01 | Parts conform to the released drawings (critical features) | MECH fabrication | I | Inspection sheets (`mechanical/assembly/`) | — | NOT VERIFIED | | |
| M3-02 | Shaft and pin material certificates match the specification (EN19 Q&T or approved) | MECH materials | I | Mill certificate | — | NOT VERIFIED | | |
| M3-03 | Assembly per ASSEMBLY_PROCEDURE; torque log complete; witness marks applied | SAF-REQ-046 | I | Assembly record | — | NOT VERIFIED | | |
| M3-04 | No unintended interference through the operating range | SYS-REQ-023 | I, T | Range test record (PC-06) | — | NOT VERIFIED | | |
| M3-05 | Flange runout and axial play within the approved limits | MECH bearings | T | Dial-indicator record | — | NOT VERIFIED | | |
| M3-06 | Balanced hard-stop contact; stop angles recorded; margins to the soft limits | SYS-REQ-035 | I, T | MI-08, C8 records | — | NOT VERIFIED | | |
| M3-07 | Encoder installed, air gap set, calibrated; resolution and repeatability measured against the approved specification | SYS-REQ-024 | T | C5/C6 records; PC-07/08 | — | NOT VERIFIED | | |
| M3-08 | Gearbox arrival checks (ratio, backlash, backdrive, noise) | SYS-REQ-003/025 | T | GB-01–05 | — | NOT VERIFIED | | |
| M3-09 | Backlash at the output measured by the documented method, within the approved limit | SYS-REQ-025 | T | PC-09 | — | NOT VERIFIED | | |
| M3-10 | Holding of the 1.5 kg arm + 1 kg payload horizontal; T_g verified with the final mass properties | SYS-REQ-012 | T | PC-01/02 | — | NOT VERIFIED | | |
| M3-11 | Continuous 10 N·m thermal test completed; housing and surface temperatures within the limits | SYS-REQ-020; SAF-REQ-035 | T | PC-03 | — | NOT VERIFIED | | |
| M3-12 | Peak test at the approved duration and duty; no permanent deformation | SYS-REQ-021 | T | PC-04 + post-test inspection | — | NOT VERIFIED | | |
| M3-13 | Hard-stop impact tests (staged) without damage; encoder calibration unchanged | SAF-REQ-041 | T | FI-24, DU-03 | — | NOT VERIFIED | | |
| M3-14 | Housing deformation under load within the approved limit (if measured) | MECH housing | T/A | Record | — | NOT VERIFIED | | |
| M3-15 | Post-test inspection: no loosening, bearing damage or encoder misalignment | SYS-REQ-092 | I | Post-test inspection sheet | — | NOT VERIFIED | | |
| M3-16 | Fixture performed as designed (no movement or yielding) | SAF-REQ-065 | I | Fixture inspection | — | NOT VERIFIED | | |

## 4. M4: Final acceptance audit

| # | Criterion | Req. | Method | Required evidence | Observed result | Status | Reviewer comment | Closure evidence |
|---|---|---|---|---|---|---|---|---|
| M4-01 | All MECH-REQ verification rows in the traceability CSV are PASS or PASS_WITH_ACTIONS (with no safety-related actions) | SYS-REQ-102 | I | Traceability CSV | — | NOT VERIFIED | | |
| M4-02 | Native CAD, STEP exports, drawings, BOM and revision information submitted and consistent | SYS-REQ-104/105 | I | Repository | — | NOT VERIFIED | | |
| M4-03 | BOM reconciled against quotations and purchases; within the approved budget, or with a variance approved | SYS-REQ-100/105 | I | `make bom-summary`; quotations | — | NOT VERIFIED | | |
| M4-04 | Assembly procedure updated as-built and followed once by someone other than the author | SYS-REQ-036 | D | Record | — | NOT VERIFIED | | |
| M4-05 | Mechanical risk register reviewed; residual risks accepted by the Project Lead | — | I | MECHANICAL_RISK_REGISTER | — | NOT VERIFIED | | |
| M4-06 | Release checklist complete | — | I | MECHANICAL_RELEASE_CHECKLIST | — | NOT VERIFIED | | |
| M4-07 | All findings closed with verified evidence; no open CRITICAL or HIGH findings | SYS-REQ-106 | I | Findings registers | — | NOT VERIFIED | | |
| M4-08 | Limitations and improvement opportunities documented for the next iteration | — | I | Mechanical test report | — | NOT VERIFIED | | |

## 5. Summary

| Gate | Total criteria | PASS | PASS WITH ACTIONS | FAIL | NOT VERIFIED |
|---|---|---|---|---|---|
| M3 | 16 | 0 | 0 | 0 | 16 |
| M4 | 8 | 0 | 0 | 0 | 8 |

## 6. Sign-off

| Gate | Independent Mechanical Reviewer | Result | Date | Project Lead |
|---|---|---|---|---|
| M3 | | | | |
| M4 | | | | |

## 7. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft (framework) |
