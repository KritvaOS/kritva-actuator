# Kritva Actuator: CAD Naming and Revision Standard

| Field | Value |
|---|---|
| Document ID | KA-STD-CAD-NAMING |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 |
| Date | 2026-10-15 |
| Document owner | Project Lead |
| Reviewer / Approver | Project Lead; Independent Mechanical Reviewer |
| Applies to | A0, A1 |
| Classification | Proprietary and confidential |

> **Status note.** Proposed standard (ACT-DEC-024). It applies to all four repositories once approved.

---

## 1. Part and assembly numbers

`KA-<VAR>-<SYS>-<NNN>` where `<VAR>` is `S`, `M`, `L` or `C` (common), `<SYS>` is a two to four letter system code, and `<NNN>` is a three-digit serial.

| `<SYS>` | System |
|---|---|
| `HSG` | Housing |
| `SHF` | Shaft and output |
| `BRG` | Bearing seats and retainers |
| `GBX` | Gearbox interface |
| `MTR` | Motor interface |
| `ENC` | Encoder mount |
| `PCB` | Controller PCB mount |
| `FIX` | Test fixture |
| `ASY` | Assembly |

Example: `KA-M-HSG-001`.

## 2. File names

`<part number>_<short-name>_rev<X>.<ext>`, for example `KA-M-HSG-001_housing_revB.step`. Native CAD files and neutral formats (STEP) are both stored for released parts. Drawings are PDF plus native.

## 3. Revision letters

| State | Revision | Rule |
|---|---|---|
| Draft | `X0.1`, `X0.2` ... | Working |
| Released for review | `A`, `B` ... | Tagged in Git `cad-<part>-rev<X>` |
| Released for fabrication | Same letter plus review record | Only after the Design review checklist |

A released revision is never overwritten; a new letter is issued.

## 4. Units and tolerances

Millimetres, degrees. General tolerances as stated in `docs/mechanical/FABRICATION_GUIDELINES.md`. Critical fits are listed on the drawing.

## 5. Large files

Binary CAD files are tracked with Git LFS in each mechanical repository. Do not commit exports that can be regenerated.

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-15 | Kritvaos Actuator Team | Initial draft |
