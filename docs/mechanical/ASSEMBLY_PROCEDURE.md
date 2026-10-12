# Kritva Actuator: Assembly Procedure

| Field | Value |
|---|---|
| Document ID | KA-DOC-MECH-ASSEMBLY |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Mechanical Intern |
| Reviewer / Approver | Independent Mechanical Reviewer / Project Lead |
| Applies to | A1 |
| Classification | Proprietary and confidential |

> **Status note.** This procedure follows the proposed concept in `MECHANICAL_DESIGN_SPECIFICATION.md`. Steps, part numbers and tightening torques are **provisional**. They are updated as-built after the first assembly (ACT-02-005), and the procedure is re-issued before the A1 release. Component manufacturers' instructions (motor, gearbox, coupling, bearings) take precedence where they differ.

---

## 1. Purpose

This document gives a repeatable, inspectable procedure to assemble, inspect and disassemble the Kritva Actuator. It supports SYS-REQ-036 (independent replaceability), SAF-REQ-046 (fastener control) and the M3 prototype-verification gate.

## 2. Safety

- The actuator is **unpowered** throughout assembly. No battery or PSU is connected.
- Wear safety glasses when pressing bearings or fitting circlips.
- Use an ESD mat and wrist strap when handling the encoder PCB or the controller PCB (SAF-REQ-072).
- **Rare-earth magnets** (the motor rotor, the encoder magnet) cause pinch hazards and attract tools. Keep steel tools away from them.

## 3. Tools and consumables

| Item | Specification |
|---|---|
| Torque screwdriver or wrench | 0.5–6 N·m range, calibrated (record the ID) |
| Hex keys / bits | 1.5–5 mm |
| Bearing press tool or arbor press | Applies force to the **pressed ring only** |
| Circlip pliers | Internal and external |
| Dial indicator with a magnetic base | 0.01 mm resolution |
| Feeler gauges | 0.02–0.5 mm |
| Thread-locker | Medium strength (blue, removable) |
| Retaining compound | Bearing-retainer grade, only if specified (TBC) |
| Anti-seize | For steel into aluminium threads that are removed often |
| Isopropyl alcohol, lint-free wipes | Cleaning |
| Epoxy | For bonding the encoder magnet (grade TBC; follow the IC vendor's guidance) |
| Paint marker | Witness marks |

## 4. Tightening torques (provisional)

| Fastener | Into | Grade | Torque (N·m) | Thread-locker |
|---|---|---|---|---|
| M3 SHCS | Aluminium (≥ 2 × d engagement) | 8.8 / A2-70 | 1.0 | Medium |
| M3 SHCS | Steel | 12.9 | 1.8 | Medium |
| M4 SHCS | Aluminium (≥ 2 × d engagement) | 8.8 / A2-70 | 2.2 | Medium |
| M4 SHCS | Steel | 12.9 | 4.0 | Medium |
| Motor mounting screws | Per motor datasheet | Per datasheet | Per datasheet | Medium |
| Gearbox mounting screws | Per gearbox datasheet | Per datasheet | Per datasheet | Medium |
| Coupling clamp screws | Per coupling datasheet | — | Per datasheet | None (unless the vendor specifies one) |

These values are typical starting points for dry or lightly oiled threads. **Confirm them** against the fastener supplier's data and the thread engagement in the CAD before release.

## 5. Assembly sequence

The parts referenced (`mechanical/README.md`) are: KA-MEC-0001 housing, -0002 plate, -0003 shaft, -0004 flange, -0005 stops, -0006 encoder mount, plus the bought-in motor, gearbox, coupling and bearings.

### Step 0: Kitting and inspection

1. Check every part against the BOM (`mechanical/bom/MECHANICAL_BOM.csv`) and the drawing revisions.
2. Inspect and record the critical dimensions:
   - bearing bores (two-point measurement, both bores);
   - shaft bearing seats;
   - coupling bores;
   - housing-to-plate pilot.
3. Clean all parts and remove burrs. Check that the thread holes are clean.
4. Record the serial numbers of the motor, gearbox and encoder PCB.

### Step 1: Output shaft sub-assembly

1. Fit the **located bearing** (B_near) onto the shaft against its shoulder. Press on the **inner ring only**.
2. Fit the external circlip and check that it is fully seated.
3. Bond the **encoder magnet** to its seat on the shaft (alignment, adhesive and cure time per the encoder IC guidance). Mark its orientation and let it cure fully before the next handling step.
4. Fit the far bearing (B_far), floating.

### Step 2: Install the shaft in the housing

1. Press the shaft sub-assembly into the housing, pressing on the **outer ring** of the located bearing.
2. Fit the internal circlip or retaining ring for the located bearing.
3. Fit the wave spring (if used) behind the floating bearing's outer ring.
4. **Inspection.**
   - Rotate the shaft by hand. It must turn smoothly, with no catching.
   - Measure the radial runout at the flange seat with the dial indicator (target ≤ 0.02 mm, TBC).
   - Measure the axial play (target ≤ 0.05 mm, or zero with preload; TBC).

### Step 3: Output flange and hard stops

1. Mount the flange onto the shaft (bolt circle or keyed hub, per the drawing). Tighten to the specified torque with thread-locker.
2. Fit the two **stop pins** into the flange (press fit or bonded, per the drawing).
3. Fit the stop lugs and **bumpers** on the housing. Do not fully tighten the slotted lugs yet.
4. Rotate the flange to each end of travel and check that **both pins contact at the same time** (balanced stop). Adjust the slots, tighten, and witness-mark.
5. Record the stop angles with a protractor or the encoder later (target about −5° and about 140°, TBC).

### Step 4: Motor and gearbox sub-assembly

1. Mount the gearbox onto the plate (pilot engaged). Tighten to the datasheet torque with thread-locker.
2. Fit the motor to the gearbox input according to the gearbox manufacturer's instructions (clamp collar or keyed bore, shaft engagement length). **Never** hammer the motor shaft.
3. Mount the motor to the plate if the arrangement requires it (motor flange or support). Avoid over-constraining the motor, gearbox and plate. Use one rigid mount and one compliant support where the datasheets require it.
4. Apply thermal paste between the motor stator mount and the plate (if specified).

### Step 5: Coupling and joining

1. Fit the coupling hub onto the gearbox output (clamp screw torque per the coupling datasheet).
2. Fit the other hub onto the 12 mm shaft end (D-flat or spline engagement).
3. Join the plate to the housing: dowels first, then screws to torque.
4. **Alignment check.**
   - Measure the coupling offset and angular misalignment with feeler gauges or a dial indicator. They must be within the coupling datasheet limits.
   - Rotate by hand through the full range. The motion must be smooth, with no binding.

### Step 6: Encoder and electronics

1. Mount the encoder PCB on its stationary bracket. Set the **air gap** with feeler gauges to the IC datasheet value.
2. Route the cables on the non-rotating side only, with strain relief (SAF-REQ-048).
3. Mount the controller PCB (A1) or route the cables to the development board (A0).
4. Fit the covers.

### Step 7: Final inspection (record in `mechanical/assembly/`)

| # | Check | Criterion | Result |
|---|---|---|---|
| 1 | All fasteners torqued and witness-marked | 100 % | |
| 2 | Hand rotation through the range | Smooth; no interference | |
| 3 | Both stops contact simultaneously | Yes | |
| 4 | Flange runout | ≤ 0.02 mm (TBC) | |
| 5 | Axial play | ≤ 0.05 mm (TBC) | |
| 6 | Encoder air gap | Per the IC datasheet | |
| 7 | Cable routing; no cable crossing the output | Yes | |
| 8 | Pinch points guarded or marked | Yes | |
| 9 | Mass of the assembled actuator | Recorded | |
| 10 | Serial numbers recorded | Yes | |

After the first powered run (performed per `docs/electronics/HARDWARE_BRINGUP.md`), do the **direction and zero calibration** per `docs/firmware/CALIBRATION_PROCEDURE.md`.

## 6. Post-test inspection (after each loaded campaign, SAF-REQ-046/047)

1. Check the witness marks on every fastener. If any has moved, record a non-conformance.
2. Check the backlash and play against the values recorded after assembly.
3. Rotate by hand and listen for bearing roughness.
4. Inspect the bumpers for cracking or permanent set, and replace them if needed.
5. Check that the encoder magnet is still bonded and aligned.
6. Record the impact count since the last inspection.

## 7. Disassembly (for replacing a component)

| To replace | Steps (reverse order) | Notes |
|---|---|---|
| Motor | Covers → controller connection → motor-to-gearbox interface → motor | Gearbox and shaft are undisturbed |
| Gearbox | Covers → plate-to-housing screws → coupling hub → gearbox from plate | Re-check the alignment on reassembly |
| Bearings | Plate off → flange off → circlips → press the shaft out | Bearings are replaced as a pair; never re-use pressed-out bearings |
| Encoder PCB | Covers → PCB bracket | Recalibrate the output zero afterwards |
| Bumpers | Stop lugs | Re-check the balanced contact |

## 8. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | As-built update after the first assembly | Mechanical Intern | M3 |
| 2 | Confirm the torques with the actual fasteners and engagement | Mechanical Intern | M2 |
| 3 | Runout and play limits approved | Project Lead + reviewer | M2 |
| 4 | Magnet bonding method from the encoder vendor | Electronics/Embedded Intern | ACT-01-003 |

## 9. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
