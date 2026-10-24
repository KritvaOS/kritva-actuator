# Kritva Actuator: BOM Standard

| Field | Value |
|---|---|
| Document ID | KA-STD-BOM |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 |
| Date | 2026-10-15 |
| Document owner | Project Lead |
| Reviewer / Approver | Project Lead |
| Applies to | A0, A1 |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** Proposed standard (ACT-DEC-024). It applies to all four repositories once approved.

---

## 1. Files

| Repository | File | Item prefix |
|---|---|---|
| `kritva-actuator-s` | `bom/MECHANICAL_BOM.csv` | `MB-S-NNN` |
| `kritva-actuator-m` | `bom/MECHANICAL_BOM.csv` | `MB-NNN` (existing) |
| `kritva-actuator-l` | `bom/MECHANICAL_BOM.csv` | `MB-L-NNN` |
| `kritva-actuator-embedded` | `hardware/bom/ELECTRICAL_BOM.csv` | `EB-NNN` |

The parent does not hold a BOM. It summarises the children when they are checked out (`make bom-summary`).

## 2. Schema

Every BOM uses the 17 columns defined in `scripts/bom/README.md`: item_id, milestone, category, description, manufacturer, manufacturer_part_number, supplier, supplier_part_number, quantity, unit, unit_cost_inr, extended_cost_inr, cost_status, lead_time_days, status, owner, notes.

## 3. Rules

1. `cost_status` is one of ESTIMATE, QUOTED, PURCHASED, TBD. A quoted or listed price needs a source and a date in `notes`. `status` is one of CANDIDATE, SELECTED, ORDERED, RECEIVED, REJECTED.
2. `extended_cost_inr` equals quantity times unit cost.
3. A part with status CANDIDATE is not ordered.
4. Each child vendors `scripts/bom/check_bom.py` and runs it in its own CI. Prefix handling is passed on the command line.

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-15 | Kritvaos Actuator Team | Initial draft |
