# Kritva Actuator: Firmware Review (F0–F2)

| Field | Value |
|---|---|
| Document ID | KA-AUD-FW-REVIEW |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Independent Electrical/Firmware Reviewer |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A0, A1 |
| Classification | Proprietary and confidential |

> **Status note.** This is the review framework. No review has been carried out. Safety-relevant firmware must be reviewed by someone other than its author (FW-REQ-076).

---

## 1. Purpose

This document is the independent review of:

- the firmware requirements (F0);
- the firmware architecture (F1);
- the firmware code (F2, rolling, per pull request or per module).

## 2. Gate records

### 2.1 F0: Firmware requirements

| Item | Value |
|---|---|
| Evidence | `requirements/FIRMWARE_REQUIREMENTS.md`; `planning/v1/tasks/ACT-01/ACT-01-001/` |
| Reviewer / date / result | TBD / — / NOT VERIFIED |

| # | Check | Result | Comment |
|---|---|---|---|
| F0-01 | Every FW-REQ and CTRL-REQ is measurable, with a method and evidence location | NOT VERIFIED | |
| F0-02 | State machine identical to INTERFACE_REQUIREMENTS §8.8.1 | NOT VERIFIED | |
| F0-03 | The fault table covers the minimum fault set (IF §8.13) with thresholds and reactions consistent with SAFETY | NOT VERIFIED | |
| F0-04 | Loop rates and the CPU budget are plausible for the proposed MCU | NOT VERIFIED | |
| F0-05 | Licence rule for reused code is present (FW-REQ-074) | NOT VERIFIED | |

### 2.2 F1: Architecture review

| Item | Value |
|---|---|
| Evidence | `docs/firmware/FIRMWARE_ARCHITECTURE.md`, `MOTOR_CONTROL.md`, `CALIBRATION_PROCEDURE.md`; `docs/interfaces/ACTUATOR_INTERFACE.md`, `CAN_PROTOCOL.md` |
| Reviewer / date / result | TBD / — / NOT VERIFIED |

| # | Check | Result | Comment |
|---|---|---|---|
| F1-01 | Module boundaries; HAL isolation | NOT VERIFIED | |
| F1-02 | Interrupt priorities and execution model; communication cannot block the current loop | NOT VERIFIED | |
| F1-03 | Single PWM-enable path guarded by the state | NOT VERIFIED | |
| F1-04 | Watchdog supervision design (both contexts must report alive) | NOT VERIFIED | |
| F1-05 | Shared-data design (single writer; double-buffered) | NOT VERIFIED | |
| F1-06 | NVM design: two copies, CRC, power-fail safe, no writes while ENABLED | NOT VERIFIED | |
| F1-07 | CAN function-code allocation and priorities; broadcast restrictions; alive counter | NOT VERIFIED | |
| F1-08 | Calibration safety: current-limited sub-state; validity flag | NOT VERIFIED | |
| F1-09 | Test strategy covers unit, HIL and fault injection | NOT VERIFIED | |
| F1-10 | Test-build fault hooks cannot be present in release builds | NOT VERIFIED | |

### 2.3 F2: Code review (rolling)

**Per-PR checklist**, applied to every safety-relevant module:

| # | Check |
|---|---|
| C-01 | Compiler warnings = 0; static analysis clean (or justified suppressions) |
| C-02 | No dynamic allocation after init; no blocking calls in ISRs or control loops |
| C-03 | Fixed-width types; no undefined behaviour; bounded loops in ISRs |
| C-04 | Limits enforced independently of the command source |
| C-05 | Faults raised through the fault manager with the correct code and class |
| C-06 | Units and sign conventions per SIGNAL_AND_UNIT_CONVENTIONS; output and motor side named explicitly |
| C-07 | Unit tests added or updated; coverage target met for host-testable modules |
| C-08 | No vendor code outside `platform/` |
| C-09 | Third-party code registered (FW-REQ-074) |
| C-10 | Timing impact measured if the code runs in an ISR |

**Code review log:**

| PR / commit | Module | Reviewer | Result | Findings |
|---|---|---|---|---|
| — | | | | |

## 3. Findings register

| ID | Gate | Severity | Finding | Required action | Owner | Due | Closure evidence | Reviewer verified | Status |
|---|---|---|---|---|---|---|---|---|---|
| — | | | | | | | | | |

## 4. Sign-off

| Gate | Reviewer | Result | Date | Project Lead |
|---|---|---|---|---|
| F0 | | | | |
| F1 | | | | |
| F2 (summary) | | | | |

## 5. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft (framework) |
