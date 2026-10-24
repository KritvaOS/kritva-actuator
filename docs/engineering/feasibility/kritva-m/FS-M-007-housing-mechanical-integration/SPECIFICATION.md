---
study_id: FS-M-007
title: Housing and Mechanical Integration
product: Kritva-M
version: 0.1
status: PROPOSED
lifecycle: PROPOSED
owner: Mechanical Intern
reviewer: Project Lead; Independent Reviewer TBD for safety-critical structural and hard-stop checks
upstream:
- FS-M-001
- FS-M-003
- FS-M-004
- FS-M-005
- FS-M-006
downstream:
- FS-M-008
- FS-M-009
- FS-M-010
---

# FS-M-007 - Housing and Mechanical Integration

## 1. Purpose

Develop and assess the Kritva-M actuator housing and mechanical integration concept. Establish a traceable structural load path, assembly architecture, interfaces, hard stops, encoder mounting, serviceability and CAD envelope/interference model. CAD geometry is mandatory but must be clearly labelled concept geometry until its dimensions and interfaces are validated.

## 2. Scope

In scope:

- Housing/frame architecture and load path from output shaft through dedicated bearings and housing to the arm/joint mounting interface.
- Motor and gearbox mounting, concentricity, pilots, fasteners, torque reaction and output-flange/arm interface.
- Housing material/process comparison, seat and mount stiffness, hand estimates of deformation and alignment.
- Hard-stop geometry, angular range, contact path and load transfer into the housing.
- Output encoder mounting and cable routing.
- Assembly/disassembly sequence and independent replacement of motor, gearbox, bearings and encoder where practical.
- Tolerance stack-up, threads/inserts, fasteners, inspection and service access.
- Mandatory CAD assembly/envelope/interference model, with explicit concept status.
- Mass/envelope tracking against the humanoid arm layout when approved budgets become available.

Out of scope:

- Production-released drawings, safety certification or verified structural qualification.
- Inventing dimensions, loads, mass budgets, prices, part numbers or supplier availability.
- Treating a CAD fit check as proof of strength, serviceability or post-test integrity.

## 3. Requirements Traceability

Link to canonical requirements; do not redefine their text:

- SYS-REQ-031: dedicated bearing pair in joint housing.
- SYS-REQ-032: arm loads bypass gearbox and motor bearings through shaft, bearings and housing.
- SYS-REQ-034: output encoder mounting within alignment limits under rated load, including shaft deflection.
- SYS-REQ-035: mechanical hard stops at joint-range ends.
- SYS-REQ-036: independent replacement of motor, gearbox, bearings and encoder where practical.
- SYS-REQ-037: consistent mounting interface and output-shaft/flange interface for reuse.
- SYS-REQ-038: A0/A1 process options and justified material/process for load-bearing parts.
- SYS-REQ-039: actuator mass and envelope budgets from humanoid arm layout; TBD.
- SYS-REQ-023: approximate 0-120° to 0-135° range bounded by hard stops.
- SYS-REQ-090: indoor laboratory ambient range TBD.
- SYS-REQ-092: post-test integrity (no unacceptable permanent deformation, loosening, bearing damage or encoder misalignment).
- SYS-REQ-100: A0 budget INR 10-15k; A1 budget INR 20-30k cumulative.

## 4. Upstream Inputs and Dependencies

Use the authoritative input register at `kritva-m/FS-M-001-integrated-actuator-system/inputs/INPUTS.md`. Preserve upstream IDs, values and statuses for IN-009, IN-014, IN-015, IN-016, IN-018, IN-019, IN-023, IN-028, IN-033, IN-034 and IN-036. Reference upstream ASM-001..ASM-012 and OQ-001..OQ-014 by ID; do not redefine them.

FS-M-003: use the actual motor candidate data and operating points. Motor identity, mounting geometry, heat rejection and interface remain unconfirmed where candidate data are unavailable.

FS-M-004 outputs:

- `outputs/GEARBOX_CANDIDATE_MATRIX.csv`
- `outputs/RATIO_OPTIMIZATION.csv`
- `outputs/LOAD_RATING_CHECK.csv`
- `outputs/INTERFACE_COMPATIBILITY.csv`
- `outputs/LIFE_RATING_ASSESSMENT.csv`

FS-M-005 outputs:

- `outputs/SHAFT_LOAD_CASES.csv`
- `outputs/SHAFT_STRENGTH_CHECK.csv`
- `outputs/IMPACT_CHECK.csv`
- `outputs/DEFLECTION_CHECK.csv`
- `outputs/INTERFACE_CHECK.csv`
- `outputs/MATERIAL_COMPARISON.csv`

FS-M-006 outputs:

- `outputs/BEARING_LOAD_CASES.csv`
- `outputs/BEARING_CANDIDATE_MATRIX.csv`
- `outputs/BEARING_RATING_CHECK.csv`
- `outputs/LIFE_ASSESSMENT.csv`
- `outputs/IMPACT_BEARING_CHECK.csv`
- `outputs/INTERFACE_DECISION.csv`
- `outputs/SUPPORT_FEASIBILITY.csv`

Verify file existence, revision, units and review status before relying on any artifact. The FS-M-006 interface decision is the authoritative handoff for resolving the IN-015/IN-016 mismatch; use its recorded disposition rather than silently changing either input. Missing or unreviewed data make dependent conclusions provisional or blocked.

## 5. Baseline and Open Budgets

- IN-009: 24 V nominal supply, PRELIMINARY; electrical integration context only.
- IN-014: motor data, UNKNOWN.
- IN-015: 12 mm nominal output shaft, PRELIMINARY.
- IN-016: 6202 bearing associated with 15 mm seats, ASSUMED; refer to FS-M-006 `outputs/INTERFACE_DECISION.csv` for the project decision.
- IN-018: hard-stop kinetic energy approximately 1.9 J, PRELIMINARY.
- IN-019: estimated impact torque approximately 47.5 N·m, PRELIMINARY; provenance unresolved under OQ-012.
- IN-023: static strength factor target 1.5, ASSUMED.
- IN-028: ambient conditions, UNKNOWN.
- IN-033: range of motion 0° to 120-135°, PRELIMINARY.
- IN-034: output-side encoder required, PRELIMINARY.
- IN-036: single-contact hard-stop load case governs, ASSUMED.

Mass and envelope budgets remain UNKNOWN under SYS-REQ-039 and the applicable upstream open-question mapping. Do not use IN-039 for mass or envelope: it concerns ratio/motor-speed estimation. Do not claim mass, envelope or budget compliance until the arm layout and component data are approved.

## 6. Architecture and Structural Load Path

Define the assembly architecture and interfaces for the independent output shaft, dedicated bearing pair, housing, gearbox, motor, encoder and arm mounting interface. The primary arm-load path must be explicit: output shaft -> bearing pair -> load-bearing housing -> joint/arm mounting interface.

Do not route arm radial, axial or bending loads through gearbox or motor bearings unless the exact manufacturer ratings explicitly permit the calculated loads. Identify the gearbox torque-reaction path separately from the arm-load path. Document load directions, interfaces, fasteners, locating features and critical joints.

Use FS-M-005 shaft-load/strength/interface outputs and FS-M-006 bearing/support outputs to define the concept. If upstream geometry or loads are incomplete, mark the affected interface or strength assessment provisional.

## 7. Housing Material and Manufacturing Process

Compare plausible options without assuming one is selected:

- Machined aluminium.
- Machined steel where justified by strength, stiffness or interface needs.
- 3D-printed polymer or metal for concept parts or justified features.
- Hybrid constructions with distinct load-bearing and non-load-bearing elements.

A0/A1 may use 3D printing and simple machining, but load-bearing shaft supports, bearing seats, gearbox mounts and motor mounts require material and process justification by calculation. A printed part is not automatically acceptable because it is inexpensive or geometrically convenient. Evaluate stiffness, creep, anisotropy, temperature, wear, fastener pull-out, insert retention, surface finish and dimensional stability as applicable.

Record material properties and process limitations with source-register entries. Do not invent strength data or assume a printed seat meets alignment tolerances without evidence.

## 8. Housing Stiffness and Deformation

Use hand calculations to estimate deformation and alignment at bearing seats, motor/gearbox pilots and encoder mounts under relevant rated loads. Identify load paths, support conditions, contact interfaces and fastener assumptions. Coordinate the deflection limits and shaft slope with FS-M-005 `outputs/DEFLECTION_CHECK.csv`.

If hand estimates identify a significant uncertainty that affects structural or alignment conclusions, housing-stiffness FEA may be proposed. Simulation is conditional and must not replace validated loads, geometry or boundary conditions. Record model assumptions, mesh/convergence, material model, load mapping, validation and limitations if FEA is performed.

## 9. Motor, Gearbox and Output Interfaces

Use the FS-M-003 motor candidate data and FS-M-004 gearbox candidate/interface outputs. Define mounting pilots, concentricity, shaft coupling, torque reaction, fasteners, axial retention and replacement clearances only to the level supported by source drawings.

Maintain consistent reusable mounting and output-shaft/flange interfaces in accordance with SYS-REQ-037. Check fastener access, assembly direction, tolerance stack-up and the effect of adapters or shims. Do not invent interface dimensions where exact candidate data are unavailable.

## 10. Bearings, Shaft and Encoder Integration

Integrate the FS-M-005 shaft concept with the FS-M-006 bearing pair and support housing. Use the approved FS-M-006 interface decision for the IN-015/IN-016 mismatch.

Verify bearing seat locations, coaxiality, shaft shoulders, axial retention, lubrication access and bearing replacement. Assess encoder mount stiffness, alignment, cable routing, coupling and access using IN-034 and SYS-REQ-034. Alignment conclusions must include shaft deflection and housing/support deformation under rated load; CAD coincidence alone is insufficient.

## 11. Hard Stops and Range of Motion

Design concept hard stops at the ends of the permitted joint range, using IN-033 and SYS-REQ-023. Show contact geometry, clearance, travel limits and the load path from stop contact through the housing and mounting structure. Consider the single-contact case in IN-036 as an assumption pending validation.

Use FS-M-005 `outputs/IMPACT_CHECK.csv` and FS-M-006 `outputs/IMPACT_BEARING_CHECK.csv`, plus applicable upstream load cases, to evaluate stop loads. IN-018 and IN-019 are preliminary; reconcile the impact estimate with OQ-012. Do not infer stop survival from a CAD model or nominal static stress alone.

Project Lead review is required for housing strength and hard-stop load-path conclusions under peak and stop-impact cases. The author cannot self-approve safety-critical work; without the required review, results remain `NOT_VERIFIED`.

## 12. Assembly, Serviceability and Fasteners

Document the assembly and disassembly sequence. Assess whether the motor, gearbox, bearing pair and encoder can be removed independently where practical without damaging unrelated components or losing alignment.

Record fastener types only when supported by design needs and evidence. For printed parts, evaluate insert retention, thread engagement, local bearing stress and repeated service cycles. Include tool access, cable disconnection, lubrication access, inspection and replacement constraints. A proposed sequence is not proof of serviceability; verify it in CAD and review the relevant interfaces.

## 13. Tolerance Stack-Up, Cable Routing and Safety

Identify critical tolerance chains for bearing coaxiality, shaft alignment, motor/gearbox concentricity, encoder alignment, hard-stop position and arm interface. Record datum strategy, fits, runout and inspection requirements. Where tolerances are not yet specified, mark them TBD and identify the requirement owner.

Route motor, encoder and sensor cables with adequate clearance from moving parts, hard stops and pinch points. Identify guarding and pinch-point risks for later safety/integration review. Hand off electrical/thermal cable and connector constraints to FS-M-008. Do not claim safety compliance based solely on the concept model.

## 14. CAD and Required Deliverables

Mandatory:

- `CAD/`: assembly/envelope/interference model is core to this study. Clearly label all concept geometry, assumptions, non-final dimensions and unresolved interfaces.
- `calculations/`: load-path, hand stiffness/deformation, fastener/seat checks, tolerance stack-up and mass calculations when component data exist.
- `outputs/`: machine-readable interface, interference, assembly/serviceability, hard-stop and mass/envelope status outputs.
- `references/SOURCE_REGISTER.csv`: all external geometry, material properties, ratings and engineering claims.

Conditional:

- `simulation/`: housing stiffness FEA only if hand estimates justify it.
- `cost_estimate/`: when component pricing and manufacturing costs have traceable evidence.
- `component_research/`: when manufacturer drawings, material/process options or supplier evidence are gathered.

Not applicable to this initial concept study:

- `test_data/`: no physical test data are required for the initial concept/integration assessment. Later testing must have its own approved plan and evidence record.

## 15. Acceptance Criteria

| AC | Criterion |
|---|---|
| AC-001 | Upstream input IDs, values and statuses are preserved and traceable. |
| AC-002 | Required FS-M-003, FS-M-004, FS-M-005 and FS-M-006 artifacts are verified by path, revision, units and review status; missing dependencies are blocked explicitly. |
| AC-003 | Structural load path is documented from output shaft through bearing pair and housing to the mounting interface, with gearbox/motor bearing bypass explicit. |
| AC-004 | Mandatory CAD assembly, envelope and interference model exists and clearly identifies concept geometry and unresolved dimensions. |
| AC-005 | Motor, gearbox, bearing, shaft, encoder and arm mounting interfaces are reconciled against available candidate evidence. |
| AC-006 | Housing material/process options and load-bearing seat/mount justification are documented; unsupported printed load-bearing features are not accepted. |
| AC-007 | Housing stiffness and deformation at critical bearing, motor/gearbox and encoder interfaces are assessed by hand estimates or a justified conditional analysis. |
| AC-008 | Hard-stop geometry, range, contact/load path and peak/impact cases are assessed with traceable upstream inputs. |
| AC-009 | Encoder mounting, cable routing and alignment under rated load are coordinated with SYS-REQ-034 and FS-M-005 deflection results. |
| AC-010 | Assembly/disassembly sequence and independent component replacement are assessed and supported by the concept model. |
| AC-011 | Critical tolerance stacks, fits, fasteners, inserts, retention and inspection requirements are documented or marked TBD. |
| AC-012 | Mass/envelope status is compared with approved arm-layout budgets when available; unknown budgets are not claimed as met. |
| AC-013 | Manufacturing/process and India sourcing considerations are recorded without inventing dimensions, prices or part numbers. |
| AC-014 | Mandatory calculations, outputs and `references/SOURCE_REGISTER.csv` are reproducible and traceable. |
| AC-015 | Conditional simulation/cost/component research and not-applicable test data are handled according to the specification. |
| AC-016 | Project Lead review of housing strength and hard-stop load-path conclusions is recorded; residual risks and provisional status are explicit. |

## 16. Review and Approval

The Mechanical Intern prepares the concept and calculations. FS-M-003 through FS-M-006 owners provide the motor, gearbox, shaft and bearing evidence. FS-M-008 receives electrical/thermal integration constraints; FS-M-009 receives manufacturing and sourcing constraints.

The Project Lead reviews structural load path, housing strength and hard-stop peak/impact conclusions. Safety-critical structural and hard-stop conclusions also require an Independent Reviewer (as in FS-M-001); the Project Lead shall assign one, and the author cannot self-approve safety-critical work. Record reviewer findings, date, evidence revisions, corrective actions and commit in `REVIEW.md` or the approved project review record. If review has not occurred, affected conclusions remain `NOT_VERIFIED`.

## 17. Must-Not-Conclude and Completion Definition

This study must NOT conclude that:

- The housing is structurally adequate without documented loads, material/process properties and calculations.
- A printed housing or bearing seat is acceptable for the load path without justified material/process and structural evidence.
- Mass or envelope budgets are met while SYS-REQ-039 and arm-layout budgets remain unresolved.
- Hard stops survive peak/impact loads without validated cases and required review.
- Motor, gearbox, bearings and encoder are independently serviceable without an evidence-backed assembly/access assessment.
- Encoder alignment is acceptable from CAD geometry alone.
- The IN-015/IN-016 interface is resolved without the recorded FS-M-006 Project Lead decision.
- A concept CAD model is production-ready or proves post-test integrity under SYS-REQ-092.
- The assembly is approved for production or human interaction.

FS-M-007 is complete when AC-001..AC-016 have evidence-backed dispositions, mandatory CAD and source/calculation deliverables are committed, downstream constraints are handed off, and Project Lead review of critical strength/stop-load conclusions is recorded. The result is a concept integration assessment, not a released mechanical design.
