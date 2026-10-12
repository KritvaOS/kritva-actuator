# scripts/bom

BOM validation and cost summary for `mechanical/bom/MECHANICAL_BOM.csv` and `hardware/bom/ELECTRICAL_BOM.csv`. Standard library only.

| Script | Make target | Purpose |
|---|---|---|
| `check_bom.py` | `make check-bom` | Validates the schema, the allowed values and the arithmetic (extended cost = quantity × unit cost) |
| `bom_summary.py` | `make bom-summary` | Totals by milestone and category, and by cost status (estimate vs quoted vs purchased) |

## BOM CSV schema (both BOMs use exactly these columns)

```
item_id,milestone,category,description,manufacturer,manufacturer_part_number,supplier,supplier_part_number,quantity,unit,unit_cost_inr,extended_cost_inr,cost_status,lead_time_days,status,owner,notes
```

| Column | Rule |
|---|---|
| `item_id` | Unique within the file, `MB-NNN` (mechanical) or `EB-NNN` (electrical) |
| `milestone` | `A0`, `A1` or `A2` |
| `cost_status` | `ESTIMATE`, `QUOTED`, `PURCHASED` or `TBD` |
| `status` | `CANDIDATE`, `SELECTED`, `ORDERED`, `RECEIVED` or `REJECTED` |
| `unit_cost_inr` | May be blank when `cost_status` is `TBD` |
| `extended_cost_inr` | Equals `quantity × unit_cost_inr` when both are present |

**Cost rule (SYS-REQ-105).** An `ESTIMATE` is a planning allowance taken from the project budget targets. It is never a supplier price. Only `QUOTED` or `PURCHASED` rows carry real supplier prices.
