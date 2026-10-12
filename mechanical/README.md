# mechanical/

Mechanical implementation of the Kritva Actuator: CAD, drawings, calculations, BOM and assembly records. Owner: **Mechanical Intern**. Reviewer for safety-critical items: **Independent Mechanical Reviewer**.

The design intent and rationale are in [docs/mechanical/MECHANICAL_DESIGN_SPECIFICATION.md](../docs/mechanical/MECHANICAL_DESIGN_SPECIFICATION.md). Requirements are in [requirements/MECHANICAL_REQUIREMENTS.md](../requirements/MECHANICAL_REQUIREMENTS.md).

| Folder | Contents | Rules |
|---|---|---|
| `cad/assembly/` | Top-level actuator assembly; test-fixture assembly | Native CAD plus a STEP export per release (Git LFS) |
| `cad/housing/` | Joint housing, motor/gearbox plate, covers | |
| `cad/shafts/` | Output shaft, coupling interfaces | |
| `cad/brackets/` | Mounting brackets, fixture parts | |
| `cad/encoder_mount/` | Magnet holder, encoder PCB bracket | |
| `drawings/` | Released fabrication drawings (PDF) with revision letters | Drawn per [FABRICATION_GUIDELINES.md](../docs/mechanical/FABRICATION_GUIDELINES.md) |
| `calculations/` | Load cases, torque and speed, shaft strength, bearing selection, gearbox selection, plus `actuator_sizing.py` | Run `make calc`. The documents must match the script output |
| `bom/MECHANICAL_BOM.csv` | Mechanical bill of materials | Schema in [scripts/bom/README.md](../scripts/bom/README.md); `make check-bom` |
| `assembly/` | As-built records, photos, inspection sheets, tightening logs | Procedure in [ASSEMBLY_PROCEDURE.md](../docs/mechanical/ASSEMBLY_PROCEDURE.md) |

## Part numbering

`KA-MEC-NNNN` for actuator parts and `KA-FIX-NNNN` for fixture parts. Revisions use letters (A, B, ...). File names follow `<part-number>_<name>_rev<X>.<ext>`.

| Part number | Part |
|---|---|
| KA-MEC-0001 | Joint housing |
| KA-MEC-0002 | Motor and gearbox mounting plate |
| KA-MEC-0003 | Output shaft |
| KA-MEC-0004 | Output flange |
| KA-MEC-0005 | Hard-stop pin/lug set |
| KA-MEC-0006 | Encoder mount |
| KA-FIX-0001 | Test fixture |

## Workflow

1. Calculations (ACT-02-003) come before the CAD freeze. CAD and drawings (ACT-02-004) are reviewed at M2 and Gate A.
2. Nothing is fabricated before Gate A.
3. After fabrication, inspection records go in `assembly/`, and test evidence goes in `results/mechanical/`.

> The earlier first-pass files `docs/mechanical/A1-mechanical-design.md` and `tools/` are superseded (see CHANGELOG.md) and should be deleted.
