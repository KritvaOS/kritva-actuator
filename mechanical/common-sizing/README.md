# mechanical/common-sizing/

Shared sizing engine for all actuator variants (ACT-DEC-026, proposed). Owner: Integration Owner.

| File | Purpose |
|---|---|
| `actuator_sizing.py` | Deterministic sizing calculations (load cases, torque and speed, shaft, bearing, stops, gearbox requirements). Standard library only |
| `expected_results.json` | Approved reference results for the A0 baseline (`INPUTS`) and the document patterns that must match. Change only in a reviewed pull request together with the documents |

```text
python3 mechanical/common-sizing/actuator_sizing.py --section torque
python3 mechanical/common-sizing/actuator_sizing.py --inputs mechanical/actuator-s/sizing/inputs.json
make check-calcs
```

Each variant keeps its own inputs in `sizing/inputs.json` in its repository and stores results there together with the parent commit used. The A0 baseline documents in `mechanical/calculations/` use the built-in `INPUTS`, which equal the Kritva-M inputs.

The files arrive here at migration Stage 4 (M) through `scripts/integration/stage4_parent_moves.sh`; until then they are in `mechanical/calculations/`.
