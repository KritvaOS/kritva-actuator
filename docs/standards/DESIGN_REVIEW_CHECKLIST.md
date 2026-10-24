# Kritva Actuator: Design Review Checklist (Gate A)

| Field | Value |
|---|---|
| Document ID | KA-STD-DESIGN-REVIEW |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 |
| Date | 2026-10-15 |
| Document owner | Project Lead |
| Reviewer / Approver | Independent Mechanical Reviewer; Independent Electrical/Firmware Reviewer |
| Applies to | A0, A1 |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** Proposed standard (ACT-DEC-024). It applies to all four repositories once approved. The checklist is a template; each variant copies it into its own `docs/` and records the result there.

---

## 1. Use

Each variant passes this checklist before drawings are released for fabrication. A passed checklist moves the variant from Concept to Designed. It does not mean Validated.

## 2. Checklist

| # | Item | Evidence | Result |
|---|---|---|---|
| 1 | Sizing inputs complete and reviewed (`sizing/inputs.json`) | Sizing results, `make check-calcs` clean | |
| 2 | Motor and gearbox chosen with datasheets and a quote | BOM rows, datasheets | |
| 3 | Gearbox rated torque and stop-torque margin checked | Calculation | |
| 4 | Output bearing and shaft checked for the load cases | Calculation | |
| 5 | Housing stress and stiffness checked | Calculation or FEA with assumptions | |
| 6 | Thermal path and limits stated | Calculation, test plan | |
| 7 | Encoder mount, magnet and air gap defined | Drawing | |
| 8 | Controller envelope and connector positions agreed with embedded | Hand-off record | |
| 9 | Common interface rows (ICD section 2) unchanged | ICD diff | |
| 10 | Fabrication method and tolerance checked against guidelines | Drawing review | |
| 11 | Test fixture is restrained and guarded; no human-interactive tests | Fixture design | |
| 12 | BOM complete, prices dated | `make check-bom` clean | |
| 13 | Reviewer independent of the author | Review record | |

## 3. Result

Pass, pass with actions, or fail. Actions are tracked as issues in the variant repository.

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-15 | Kritvaos Actuator Team | Initial draft |
