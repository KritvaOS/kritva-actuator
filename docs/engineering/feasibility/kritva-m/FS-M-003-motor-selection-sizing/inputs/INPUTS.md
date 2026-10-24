---
study_id: FS-M-003
title: Motor Selection and Sizing - Input Register
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
upstream_sources:
- FS-M-001 inputs/INPUTS.md
- FS-M-002 outputs/LOAD_CASES.csv
- FS-M-002 outputs/DYNAMIC_TORQUE_RESULTS.csv
- FS-M-002 outputs/REFLECTED_INERTIA.csv
---

# FS-M-003 Input Register

## 1. Rules

- `IN-nnn` IDs belong to FS-M-001 and must not be redefined here.
- `FS3-IN-nnn` IDs are local to FS-M-003.
- Verify upstream file values and statuses against the actual repository files before using them in calculations.
- Do not invent candidate part numbers, datasheet values, prices, or availability.
- Each candidate-specific value must identify its source document and revision in `references/SOURCE_REGISTER.csv`.
- Keep UNKNOWN values explicit; do not replace missing data with assumed values without recording a study-local assumption.

## 2. Section A — Study-Local Inputs

Columns: `input_id, parameter, value, unit, status, source, owner, used_by_study, notes`

| input_id | parameter | value | unit | status | source | owner | used_by_study | notes |
|---|---|---|---|---|---|---|---|---|
| FS3-IN-001 | Motor/gearbox ratio convention | N = motor speed / output speed | ratio | PRELIMINARY | FS-M-003 SPECIFICATION; verify against FS-M-004 | Mechanical Intern | All ratio calculations | Use consistently in torque and speed transformations |
| FS3-IN-002 | Candidate motor identity | To be populated from verified manufacturer evidence | part number | UNKNOWN | Manufacturer datasheet/product page | Mechanical Intern | Candidate shortlist | Do not invent candidates or part numbers |
| FS3-IN-003 | Candidate torque-speed data | To be populated per candidate | N·m, RPM | UNKNOWN | Manufacturer torque-speed curve/datasheet | Mechanical Intern | Continuous and peak screening | Record continuous/peak conditions and curve source |
| FS3-IN-004 | Candidate motor constants | Kt, Kv, winding resistance and definitions per candidate | N·m/A, RPM/V, Ω | UNKNOWN | Manufacturer datasheet | Mechanical Intern; Embedded Intern input | Torque/current/voltage calculations | Record phase/line, RMS/peak, and unit conventions |
| FS3-IN-005 | Candidate current and thermal limits | Continuous/peak current, duration, temperature, cooling conditions | A, s, °C | UNKNOWN | Manufacturer datasheet or written manufacturer confirmation | Mechanical Intern; Embedded Intern input | Continuous, peak, and thermal screening | Do not infer duration from a peak-current value |
| FS3-IN-006 | Required motor operating points | Derived from accepted/provisional FS-M-002 load cases for each ratio | N·m, RPM, rad/s | UNKNOWN until load-case reconciliation | FS-M-002 `outputs/LOAD_CASES.csv` and `outputs/DYNAMIC_TORQUE_RESULTS.csv` | Mechanical Intern | Motor sizing | Preserve source load-case verification status |
| FS3-IN-007 | Candidate feedback/FOC data | Encoder/Hall type, resolution, interface, commutation data | type and units | UNKNOWN | Manufacturer datasheet/interface documentation | Embedded Intern with Mechanical Intern | FOC compatibility | Record only supported feedback modes |
| FS3-IN-008 | Candidate package and sourcing data | Mass, envelope, mounting, shaft, cooling, price, supplier, India availability | kg, mm, currency | UNKNOWN | Manufacturer drawings and dated supplier evidence | Mechanical Intern | Integration, cost, trade-off | Leave UNKNOWN until sourced |
| FS3-IN-009 | Supply and drive limits | Nominal 24 V; allowed voltage range, regeneration, modulation/current limits TBD | V, A | PRELIMINARY (nominal) / UNKNOWN (rest) | IN-009; SYS-REQ-041; Embedded Intern/system definition | Embedded Intern | Voltage headroom and power-stage handoff | Nominal voltage is not a complete electrical specification |
| FS3-IN-010 | Proposed motor screening margin | 20 | % | ASSUMED for screening; confirm convention | IN-024 and project sizing method | Mechanical Intern | Continuous torque screening | Apply once; do not double-count |
| FS3-IN-011 | Ambient/cooling conditions | TBD | °C and cooling | UNKNOWN | SYS-REQ-090 and integration definition | Project Lead; Embedded Intern input | Thermal screening | Thermal feasibility stays unverified until defined |
| FS3-IN-012 | Motor rotor inertia | Candidate-specific value TBD | kg·m² | UNKNOWN | Manufacturer datasheet or measured data | Mechanical Intern | Dynamic and ratio trade-off | Coordinate with FS-M-002 reflected-inertia assumptions |
| FS3-IN-013 | Candidate efficiency data | Candidate-specific efficiency map or operating-point data TBD | % | UNKNOWN | Manufacturer datasheet or test data | Mechanical Intern | Loss and thermal estimates | Do not treat gearbox efficiency as motor efficiency |
| FS3-IN-014 | Candidate voltage/back-EMF data | Required-speed operating point and back-EMF model TBD | V, RPM | UNKNOWN | Manufacturer constants and drive limits | Embedded Intern with Mechanical Intern | Voltage headroom | Evaluate at actual candidate operating point |
| FS3-IN-015 | Candidate demagnetisation limits | Current/temperature operating envelope TBD | A, °C | UNKNOWN | Manufacturer data or written confirmation | Mechanical Intern; Embedded Intern input | Peak screening | Escalate if manufacturer does not publish limits |

## 3. Section B — Index of Upstream FS-M-001 Inputs Used

Values and statuses follow the authoritative FS-M-001 input register. They are references, not new definitions. Confirm against the repository copy before formal acceptance. All are owned as assigned in FS-M-001.

| input_id | parameter | value | unit | status | used_by_study | notes |
|---|---|---|---|---|---|---|
| IN-006 | Continuous output torque target | >= 10 | N·m | PRELIMINARY | Continuous sizing | Use FS-M-002 load cases for the actual profile |
| IN-007 | Peak output torque targets | 20 minimum / 25 stretch | N·m | PRELIMINARY | Peak sizing | Duration/repetition unresolved |
| IN-008 | Output speed | 45 | RPM | PRELIMINARY | Ratio operating points | Does not define acceleration |
| IN-009 | Nominal supply voltage | 24 | V DC | PRELIMINARY | Voltage/headroom assessment | Range and regeneration need definition |
| IN-010 | Gearbox ratios | 15:1, 20:1, 25:1 | ratio | PRELIMINARY | Motor/gearbox iteration | Evaluate all three |
| IN-011 | First gearbox candidate | 20:1 | ratio | PRELIMINARY | Candidate comparison | Candidate, not a locked decision |
| IN-012 | Gearbox efficiency | 85 | % | ASSUMED | Motor-side torque/power estimates | Not motor efficiency |
| IN-013 | Motor power starting range | 75–100 | W | PRELIMINARY | Candidate screening | Does not override torque-speed/thermal requirements |
| IN-014 | Motor data | not yet consolidated | n/a | UNKNOWN | Candidate data collection | Populate from candidate sources |
| IN-024 | Motor margin | 20 | % | ASSUMED | Continuous screening | Proposed screening margin; apply once |
| IN-026 | Duty cycle | not defined | n/a | UNKNOWN | Continuous/RMS assessment | Blocking for duty-based conclusions |
| IN-028 | Ambient conditions | not defined | °C | UNKNOWN | Thermal assessment | Requires system definition |
| IN-029 | Supply current limit | not defined | A | UNKNOWN | Drive compatibility | Requires electrical/system definition |
| IN-031 | Peak duration/repetition | not defined | s | UNKNOWN | Peak-current/torque assessment | Do not infer from peak torque value |
| IN-032 | Acceleration profile | not defined | rad/s² | UNKNOWN | Dynamic sizing | Scenarios only when explicitly labelled |
| IN-035 | Reflected inertia/backdrivability | not quantified | n/a | UNKNOWN | Motor/ratio trade-off | Use FS-M-002 inertia results and candidate data |
| IN-038 | Exact part numbers | not established | n/a | UNKNOWN | Candidate/BOM traceability | Do not invent |
| IN-039 | Ratio/motor-speed estimate | 20:1 needs low-Kv pancake motor; about 37:1 for typical BLDC | n/a | PRELIMINARY | Ratio comparison | Validate with actual motor data |

## 4. Upstream FS-M-002 Outputs

Reference the actual output files; do not duplicate their load-case definitions here.

| Source | Intended use | Required check |
|---|---|---|
| `FS-M-002/outputs/LOAD_CASES.csv` | Static, peak, and output load cases | Confirm revision, units, load-case IDs, and verification status |
| `FS-M-002/outputs/DYNAMIC_TORQUE_RESULTS.csv` | Dynamic/RMS operating points | Confirm profile definitions, duty assumptions, and limitations |
| `FS-M-002/outputs/REFLECTED_INERTIA.csv` | Ratio-dependent inertia | Confirm reference axes and included inertias |

If a file is absent or its results remain unverified, record the dependency as open rather than substituting invented load cases.

## 5. How to Update

1. Assign each new study-local input the next unused `FS3-IN-nnn` ID.
2. Record value, unit, status, source, owner, use, and limitations.
3. For candidate-specific data, add a source-register entry with manufacturer, exact part number, document title/revision, URL or repository path, access date, and fields supported.
4. Use UNKNOWN when evidence is unavailable.
5. Record calculated values separately from manufacturer-published values.
6. When an upstream input or FS-M-002 output changes, identify affected calculations, candidates, and downstream handoffs.
7. Do not promote an assumption to verified without evidence and the applicable review.
