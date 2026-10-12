# ACT-01-001: Design Notes

| Field | Value |
|---|---|
| Document ID | KA-TASK-ACT-01-001-DN |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Electronics/Embedded Intern |
| Reviewer / Approver | Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A0, A1 |
| Classification | Proprietary and confidential |

> **Status note.** These are working notes. The canonical content is in the requirement documents and `docs/electronics/`.

## 1. Sizing chain

The current requirement follows from the output torque, the ratio, the efficiency and the motor's Kt:

```
T_out (10 N·m cont, 25 N·m peak)
  -> motor torque  T_m = T_out / (N · η)        (η = 0.85 for sizing)
  -> phase current I_q = T_m / Kt
  -> power-stage rating ≥ 1.5 × I_q,peak (margin TBC); shunt and ADC range from I_q,peak
  -> bus current   I_bus ≈ P_in / V_bus
```

Example: at 20:1, T_m is 0.59 N·m continuous and 1.47 N·m peak.

- With Kt = 0.08 N·m/A (illustrative), Iq ≈ 7.4 A continuous and 18.4 A peak.
- With Kt = 0.05 N·m/A, Iq ≈ 11.8 A continuous and 29.4 A peak. This exceeds the rating of many small development boards.

**Conclusion:** the motor selection (ACT-02-002) and the board selection must be made together.

## 2. Board-selection notes

| Candidate | Points to check |
|---|---|
| B-G431B-ESC1 | Continuous current rating with and without a heat sink; three-shunt sensing; whether the CAN pins are reachable; SWD access |
| NUCLEO-G474RE + IHM08M1-class | Voltage and current headroom; cabling between the boards; the extra space it takes on the bench |
| ODrive-class | Used as a reference platform. Firmware licence and reuse need checking (FW-REQ-074) |

## 3. Open questions

1. Will A0 use the motor's Hall sensors, or add a motor-side magnetic encoder from the start?
2. Is CAN isolation needed? Proposed: not for A1 (single robot ground), TBC.
3. What regeneration strategy will the bench use, given the PSU's capability?

## 4. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
