# Kritva Actuator: Firmware Acceptance Audit (F3–F4)

| Field | Value |
|---|---|
| Document ID | KA-AUD-FW-ACCEPT |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Independent Electrical/Firmware Reviewer |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A0, A1 |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** This is the acceptance framework. No results have been recorded.

---

## 1. Purpose

This document records the verification of the firmware on real hardware:

- **F3:** HIL, timing and fault injection;
- **F4:** release of the firmware package (FW-REQ-075).

## 2. F3: HIL and fault-injection verification

| # | Criterion | Req. | Evidence | Observed result | Status | Comment |
|---|---|---|---|---|---|---|
| F3-01 | Current-loop rate and jitter measured (≤ 1 µs, TBC); CPU load ≤ 70 % at maximum rates | FW-REQ-061 | `results/motor_control/` timing capture | — | NOT VERIFIED | |
| F3-02 | Current-loop step response meets CTRL-REQ-011 | CTRL-REQ-011 | BU-09 | — | NOT VERIFIED | |
| F3-03 | Position and velocity loops stable with the arm; performance recorded | CTRL-REQ-020–025 | PC-10 | — | NOT VERIFIED | |
| F3-04 | Limits enforced from every command source | CTRL-REQ-030 | `tests/firmware/` | — | NOT VERIFIED | |
| F3-05 | Soft-limit approach at maximum speed stops before the hard stop | CTRL-REQ-031/032 | FI-18 | — | NOT VERIFIED | |
| F3-06 | Fault-injection matrix FI-01 to FI-22 passes (reaction, code, class, timing) | CTRL-REQ-001–006 | `tests/safety/` | — | NOT VERIFIED | |
| F3-07 | Command timeout gives the safe state within timeout + 5 ms | SAF-REQ-020 | FI-11 | — | NOT VERIFIED | |
| F3-08 | State/call matrix conformance (CT-01) | FW-REQ-030 | `tests/firmware/` | — | NOT VERIFIED | |
| F3-09 | Configuration atomicity and NVM power-fail safety | FW-REQ-060 | `tests/firmware/` | — | NOT VERIFIED | |
| F3-10 | Calibration procedure C0–C11 executed; values repeatable | FW-REQ-020–024 | CAL records | — | NOT VERIFIED | |
| F3-11 | Malformed and fuzzed input causes no crash and no motion | FW-REQ-053 | FI-20 | — | NOT VERIFIED | |
| F3-12 | CAN conformance CAN-01 to CAN-10 | FW-REQ-051 | `results/integration/` | — | NOT VERIFIED | |
| F3-13 | Host unit-test coverage target met | FW-REQ-072 | CI report | — | NOT VERIFIED | |

## 3. F4: Firmware release

| # | Criterion | Evidence | Status |
|---|---|---|---|
| F4-01 | Release tag; binary plus hash; release notes; configuration defaults | Release artefacts | NOT VERIFIED |
| F4-02 | Release build contains no test-build fault hooks | Build flags review | NOT VERIFIED |
| F4-03 | All FW-REQ and CTRL-REQ rows PASS / PASS_WITH_ACTIONS (no safety actions) | Traceability CSV | NOT VERIFIED |
| F4-04 | Third-party register complete and approved | `firmware/README.md` | NOT VERIFIED |
| F4-05 | All F-gate findings closed and verified | FIRMWARE_REVIEW §3 | NOT VERIFIED |
| F4-06 | Version reporting verified over USB/UART and CAN | Test record | NOT VERIFIED |

## 4. Summary

| Gate | Criteria | PASS | PASS WITH ACTIONS | FAIL | NOT VERIFIED |
|---|---|---|---|---|---|
| F3 | 13 | 0 | 0 | 0 | 13 |
| F4 | 6 | 0 | 0 | 0 | 6 |

## 5. Sign-off

| Gate | Reviewer | Result | Date | Project Lead |
|---|---|---|---|---|
| F3 | | | | |
| F4 | | | | |

## 6. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft (framework) |
