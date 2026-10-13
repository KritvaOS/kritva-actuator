# audit/

Independent reviews, acceptance audits, risk registers and release-gate decisions for the Kritva Actuator.

**Ownership rule (ACT-DEC-014).** Audit findings are owned by the **reviewer**. The author supplies evidence and corrections, and the reviewer verifies closure. No author approves their own safety-critical design. If a qualified independent reviewer is not available, the item is recorded as `NOT_VERIFIED` and the related gate stays **blocked**.

**This folder never duplicates design documentation.** Audit records link to the requirements, calculations, CAD, test records and results by path.

| Path | Contents | Owner |
|---|---|---|
| `requirements_traceability/REQUIREMENTS_TRACEABILITY.csv` | Every requirement ID mapped to parents, owner, phase, verification method, procedure, evidence, verification status and audit status | Project Lead (maintains); reviewers (audit status) |
| `mechanical/MECHANICAL_DESIGN_AUDIT.md` | Gates M0 (requirements), M1 (component selection), M2 (CAD design and calculations) | Independent Mechanical Reviewer |
| `mechanical/MECHANICAL_ACCEPTANCE_AUDIT.md` | Gates M3 (prototype verification) and M4 (final acceptance): criterion-by-criterion results | Independent Mechanical Reviewer |
| `mechanical/MECHANICAL_RISK_REGISTER.md` | Mechanical failure modes, controls, mitigation, verification, residual risk | Independent Mechanical Reviewer, with input from the Mechanical Intern |
| `mechanical/MECHANICAL_RELEASE_CHECKLIST.md` | Checks before the mechanical design is released for integration and fabrication | Independent Mechanical Reviewer + Project Lead |
| `electronics/ELECTRONICS_DESIGN_AUDIT.md` | Gates E0–E2 (requirements, board and component selection, schematic and PCB) | Independent Electrical/Firmware Reviewer |
| `electronics/ELECTRONICS_ACCEPTANCE_AUDIT.md` | Gates E3–E4 (bring-up verification, final acceptance) | Independent Electrical/Firmware Reviewer |
| `firmware/FIRMWARE_REVIEW.md` | Gates F0–F2 (requirements, architecture, code review) | Independent Electrical/Firmware Reviewer |
| `firmware/FIRMWARE_ACCEPTANCE_AUDIT.md` | Gates F3–F4 (HIL / fault injection, release) | Independent Electrical/Firmware Reviewer |
| `external/EXTERNAL_REPO_AUDIT_<date>.md` | External (remote) repository and design audits, with findings, dispositions and M0 blockers. Input to gates, never a sign-off | External reviewer (findings); Project Lead (record) |
| `release/RELEASE_AUDIT.md` | Gates A, B and C; milestone exits A0, A1 and A2; release sign-off | Project Lead, with specialist sign-offs |

## Finding classification

| Result | Meaning |
|---|---|
| **PASS** | The requirement is supported by adequate evidence |
| **PASS WITH ACTIONS** | Acceptable for this stage, with documented **non-blocking** actions |
| **FAIL** | The requirement is not met, or the evidence is insufficient |
| **NOT VERIFIED** | The test or calculation has not been completed, or no qualified reviewer is available |

Severity levels are CRITICAL, HIGH, MEDIUM, LOW and OBSERVATION. A **safety-critical defect is never treated as non-blocking** to meet a deadline (SAF-REQ-083).

## Remote review limitation

A remote review (including AI-assisted review) can check the submitted data, recalculate results and challenge assumptions. It is **not** equivalent to physically inspecting the assembly or testing it in the lab. Safety-critical approval needs qualified human review and physical evidence.

## Checks

`make check-trace` validates the traceability CSV against the requirement documents.
