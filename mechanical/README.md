# mechanical/

Mechanical work of the Kritva Actuator family, after the restructure to a parent plus four submodules (ACT-DEC-024, see [docs/architecture/REPOSITORY_ARCHITECTURE.md](../docs/architecture/REPOSITORY_ARCHITECTURE.md) and [planning/v2/MIGRATION_PLAN.md](../planning/v2/MIGRATION_PLAN.md)).

| Path | Owner | Content |
|---|---|---|
| `common-sizing/` | Integration Owner (parent) | Shared sizing engine `actuator_sizing.py` and its approved reference `expected_results.json` (ACT-DEC-026). Run `make calc` or `make check-calcs`. Per-variant run: `python3 mechanical/common-sizing/actuator_sizing.py --inputs mechanical/actuator-m/sizing/inputs.json` |
| `calculations/` | Integration Owner (parent) | A0 reference baseline calculations (elbow case): load cases, torque and speed, shaft, bearing, gearbox selection, motor/gearbox shortlist. They stay in the parent because requirements, decisions and traceability cite them, and `check_calcs.py` keeps them consistent with the engine |
| `actuator-s/` | Mechanical Intern 1 | Submodule `KritvaOS/kritva-actuator-s` (added at migration Stage 5) |
| `actuator-m/` | Mechanical Intern 2 | Submodule `KritvaOS/kritva-actuator-m`: the M variant and A0 reference. Holds `bom/MECHANICAL_BOM.csv` |
| `actuator-l/` | Mechanical Intern 3 | Submodule `KritvaOS/kritva-actuator-l` (added at migration Stage 5) |

CAD, drawings, assembly records, the mechanical BOM and mechanical test evidence live in each variant repository, not here. Design intent and common requirements remain in [docs/mechanical/MECHANICAL_DESIGN_SPECIFICATION.md](../docs/mechanical/MECHANICAL_DESIGN_SPECIFICATION.md) and [requirements/MECHANICAL_REQUIREMENTS.md](../requirements/MECHANICAL_REQUIREMENTS.md).

Part numbers for new parts follow [docs/standards/CAD_NAMING_STANDARD.md](../docs/standards/CAD_NAMING_STANDARD.md) (`KA-<VAR>-<SYS>-<NNN>`). The earlier `KA-MEC-NNNN` and `KA-FIX-NNNN` numbers in the A0 baseline documents are legacy and are mapped when the M drawings are made.

Nothing is fabricated before Gate A, and loaded tests are done only on a restrained, guarded, instrumented fixture.
