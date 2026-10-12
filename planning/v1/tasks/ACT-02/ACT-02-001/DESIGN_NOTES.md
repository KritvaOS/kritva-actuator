# ACT-02-001: Design Notes

| Field | Value |
|---|---|
| Document ID | KA-TASK-ACT-02-001-DN |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Mechanical Intern |
| Reviewer / Approver | Independent Mechanical Reviewer / Project Lead |
| Applies to | A1 |
| Classification | Proprietary and confidential |

> **Status note.** These are working notes for the assignee. The canonical calculations are in `mechanical/calculations/LOAD_CASES.md`. This file records the reasoning, assumptions and alternatives, and links to that document instead of copying it.

## 1. Approach

1. Model the forearm, hand and payload as point masses about the elbow axis for the first pass. Replace this with CAD mass properties when they are available.
2. Use the horizontal arm as the worst static case: the gravity moment is greatest when the arm is perpendicular to gravity.
3. Treat the dynamic torque as T_dyn = J_arm · α plus friction. Leave α undefined until the Project Lead approves a value. Example values (5, 10 and 20 rad/s²) can be tabulated for context only, and clearly labelled as such.
4. Derive the output-bearing loads from the vector sum of the gravity and inertial forces acting at the forearm centre of mass, plus the payload, applied at the stated overhang from the bearing reference.

## 2. Assumptions register

| # | Assumption | Value | Source | Status | Replacement plan |
|---|---|---|---|---|---|
| A1 | Forearm and hand mass | 1.5 kg | Approved elbow load selection | PROPOSED | Arm CAD |
| A2 | Forearm/hand centre of mass from the elbow | 180 mm | Explicit assumption | PROVISIONAL | CAD or a measurement (balance or suspension method) |
| A3 | Payload | 1.0 kg | Approved | PROPOSED | — |
| A4 | Payload centre from the elbow | 350 mm | Approved | PROPOSED | — |
| A5 | g | 9.81 m/s² | Standard | Fixed | — |
| A6 | Forearm inertia | Point mass (ignores its own distributed inertia) | First-pass simplification | PROVISIONAL | CAD inertia |
| A7 | Angular acceleration | TBD | Not yet specified | OPEN | Project Lead decision |

## 3. Alternatives considered

| Topic | Option | Note |
|---|---|---|
| Inertia model | Point masses vs a uniform rod plus point mass | A rod model (m·L²/3) gives a different J. The point-mass value is used until CAD is available. Record both. |
| Worst-case load | Static horizontal vs dynamic lift from hanging | The dynamic lift from the hanging position includes the acceleration torque at the start of motion. Assess it once α is known. |

## 4. Open questions for the Project Lead

1. Required angular acceleration (rad/s²), or the time to move from 0° to 90°.
2. Must the arm hold the horizontal pose continuously, and for how long?
3. Is any impact, catching or fall load in scope (SYS-REQ-014)?

## 5. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
