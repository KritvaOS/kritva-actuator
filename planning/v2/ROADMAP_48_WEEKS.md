# Kritva Actuator: Reforecast (P1 to P58)

| Field | Value |
|---|---|
| Document ID | KA-PLAN-ROADMAP48 |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.2 |
| Date | 2026-10-18 |
| Document owner | Project Lead |
| Reviewer / Approver | Project Lead |
| Applies to | A0, A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** Dated reforecast overlay under `ACT-DEC-030` (48 weeks, rev 0.1), re-sequenced under `ACT-DEC-032` (A0 exit extended to P12) and `ACT-DEC-033` (Gate A to fabrication gap of two weeks). The file name is kept from rev 0.1 for traceability; the horizon is now **58 weeks, ending 28 Nov 2027**, a forecast consequence that the Project Lead should confirm (ACT-DEC-033 item 4). It does not replace the official program clock (`ACT-DEC-029`: week 1 = Mon 14 Sep 2026), does not rewrite `ACT-DEC-028`, and does not change any gate, task ID or status file. Dates are planning targets, not supplier commitments. Gates A/B/C, independent review (ACT-DEC-014) and restrained-fixture testing (ACT-DEC-015) apply unchanged and are never waived to protect a date.

---

## 1. Why the horizon grew

Rev 0.1 (48 weeks, ending 19 Sep 2027) assumed A0 exit at P6 and M fabrication overlapping Gate A. Two Project Lead instructions changed that: A0 exit moves 4 to 8 weeks later (P12 chosen), and M fabrication starts 2 to 4 weeks after Gate A passes (two weeks chosen). Re-sequencing gives 58 weeks with the PCB respin window, qualification and reserve kept. The reserve and the respin were not squeezed to hold 48 weeks. The re-plan came from an external planning discussion (ChatGPT, 2026-10-18); lead times, team capacity and supplier schedules are unverified.

## 2. Two clocks

| Clock | Meaning | Status |
|---|---|---|
| Official program week | Week 1 = Mon 14 Sep 2026 (`ACT-DEC-029`) | ACCEPTED, unchanged |
| Reforecast week P1 to P58 | P1 = Mon 19 Oct 2026; P58 ends Sun 28 Nov 2027 | Overlay (ACT-DEC-030, 032, 033) |

P(n) = official week (n + 5). The original dates and decisions stay in the record; changes are recorded as amendments.

## 3. Phase plan

| Phase | P-weeks | Official weeks | Dates | Exit / dependency |
|---|---|---|---|---|
| A0 Educational Motor Control (electronics exit) | 1-12 | 6-17 | 19 Oct-10 Jan 2027 | Reviewed evidence package accepted (section 4). Extended by 6 weeks from P6 (ACT-DEC-032) |
| M design closure and A1 Gate A | 11-14 | 16-19 | 28 Dec-24 Jan 2027 | Pending motor, gearbox, encoder, bearing, peak-torque and safe-state decisions recorded; independent design review; Gate A passed by P14 |
| Fabrication release and procurement gap | 15-16 | 20-21 | 25 Jan-7 Feb 2027 | Release package, purchase orders, supplier lead times confirmed. Two weeks after Gate A (ACT-DEC-033); no fabrication before this |
| M fabrication and assembly | 17-22 | 22-27 | 8 Feb-21 Mar 2027 | Mechanical prototype assembled; starts only after Gate A and the gap |
| M prototype checkpoint | 23 | 28 | 22 Mar-28 Mar 2027 | Bench test with embedded control on a restrained fixture; not an A1 release |
| Custom controller PCB, first spin | 24-28 | 29-33 | 29 Mar-2 May 2027 | Assembly, power-on, controller and CAN bring-up; needs A0 exit and Gate A |
| A1 Gate B: first-spin validation | 29-33 | 34-38 | 3 May-6 Jun 2027 | Restrained-fixture validation and independent evidence review |
| Contingency PCB respin | 34-38 | 39-43 | 7 Jun-11 Jul 2027 | Only for first-spin defects or validation findings; use needs evidence and Project Lead approval |
| Gate B regression and closure | 39-40 | 44-45 | 12 Jul-25 Jul 2027 | Re-test affected requirements, close evidence gaps |
| A1 Gate C: safety and release review | 41 | 46 | 26 Jul-1 Aug 2027 | Independent safety and release review; no waivers |
| S and L design and variant review (reuse M after Gate A) | 15-32 | 20-37 | 25 Jan-30 May 2027 | S/L load cases and variant evidence; update if the M checkpoint shows an architecture issue |
| A2-SW: software and interface integration | 24-41 | 29-46 | 29 Mar-1 Aug 2027 | Drivers, CAN interface, diagnostics, staged tests; once interfaces are stable |
| A2-HW: hardware integration | 42-46 | 47-51 | 2 Aug-5 Sep 2027 | Integrate hardware that passed its applicable gates |
| Qualification | 47-52 | 52-57 | 6 Sep-17 Oct 2027 | Duty-cycle, thermal, reliability and safety evidence |
| Release | 53-54 | 58-59 | 18 Oct-31 Oct 2027 | Release only variants meeting acceptance criteria |
| Schedule reserve | 55-58 | 60-63 | 1 Nov-28 Nov 2027 | Recovery only (defects, supplier delay, review findings). Not for feature growth |

The M prototype checkpoint (P23) is a prototype checkpoint, not proof that A1 Gates B and C have passed. The v1 targets for A1 (weeks 11-12) and A2 (week 12) and the v2 "A0 checkpoint (M)" at week 12 are superseded planning targets only through these decisions; their text stays in `MILESTONE.md` and the earlier roadmaps. Phase ranges overlap on purpose where work is independent. S/L design and A2-SW do not bypass M's gates or release unqualified variants.

### 3.1 Dependencies

| Item | Depends on |
|---|---|
| M fabrication | Gate A passed, then the P15-P16 release and procurement gap; never fabricate against an unapproved design |
| Custom PCB first spin | A0 exit and Gate A; planned after the M prototype checkpoint to reduce integration risk |
| S/L design | Gate A (M architecture); can start before M fabrication completes; S/L load cases explicit |
| A2-SW | Stable control interfaces and requirements |
| A2-HW | Gate C and the relevant variant readiness |
| Gate A | Pending decisions ACT-DEC-016 to 021 recorded (gearbox, motor, encoder, bearing, safe state, peak torque), independent review |

## 4. A0 exit evidence (P12)

A0 exit needs a reviewed evidence package, not only a demonstration: (1) repeatable dev-board bring-up with FOC, current sensing and encoder feedback working together; (2) closed-loop speed and position behaviour with recorded test conditions and results; (3) calibrated current limits and documented safe-state behaviour on disable, fault and power interruption; (4) overcurrent and fault-response tests and a documented safe bench procedure including a means to remove power; (5) source and configuration commit, test logs, waveforms or traces, known limitations and a reviewer sign-off. A0 exit shows the educational electronics baseline works. It does not show loaded M torque capability, PCB readiness or A1 Gate B/C acceptance. Do not declare A0 passed from the calendar; record actual evidence and review status.

## 5. Milestone meaning

A0 remains Educational Motor Control and exits at P12. The M prototype checkpoint (P23) feeds A1. A1 (Humanoid Smart Actuator) completes only through Gates A/B/C. The custom controller PCB and CAN firmware remain the A1 baseline; a development-board substitute is a documented, reviewed deviation with explicit release-gate implications. M stays the reference; S and L reuse its approved architecture after Gate A. Torque classes stay as in `ACTUATOR_FAMILY_SPEC.md` (ACT-DEC-025, PROPOSED); no wider range becomes a requirement without an approved load case.

## 6. Resourcing (`ACT-DEC-031`)

Three mechanical interns and one embedded intern from Mon 2 Nov 2026 (P3). The A0 extension gives the embedded intern about ten weeks (P3 to P12) instead of four. Assignment of the mechanical interns to M, S and L is not decided here. Interns do not add independent reviewers, so schedule reviews early.

## 7. Decisions

| Decision | Record |
|---|---|
| 48-week overlay, official week 1 unchanged, respin window, S/L and A2-SW parallel after Gate A, reserve only | ACT-DEC-030 (ACCEPTED) |
| A0 exit at P12 (+6 weeks), evidence criteria in section 4 | ACT-DEC-032 (ACCEPTED) |
| Gate A to fabrication gap two weeks; re-sequenced phases | ACT-DEC-033 (ACCEPTED, items 1-3) |
| 58-week horizon ending 28 Nov 2027 | ACT-DEC-033 item 4 (PROPOSED, confirmation pending) |

## 8. Open items

1. Project Lead to confirm the 58-week horizon (ACT-DEC-033 item 4).
2. Assignment of the three mechanical interns to M, S and L, and the owner of each.
3. The pending Gate A decisions (ACT-DEC-016 to 021) have owners and "needed by" dates in `DECISIONS.md` section 5, set against the old plan; re-date them to P11-P14.
4. Record the HOLD lift and this reforecast in kritva-program (not possible from this repository). `ACT-DEC-027` remains PROPOSED. Tasks from P13 onward do not exist in `status/tasks.csv`.
5. Not run: `make check`, including the manifest check; the new files may need rows in `MIGRATION_MANIFEST.csv`.

## 9. Risks

| Risk | Handling |
|---|---|
| Scope growth consumes the reserve | P55-P58 reserve only; additions need a separate decision |
| Lead times exceed the two-week gap | Confirm supplier dates in P15-P16; slip the fabrication start, do not release early |
| One respin is not enough | A material architecture change reopens the plan; record impact, no waivers |
| S/L rework after an M change | Update S/L evidence after the P23 checkpoint; changes to M need a design change request |
| Review capacity | Interns add no reviewers; book independent reviews for Gate A (P14), Gate B and Gate C early |
| A0 slips beyond P12 | Reforecast from evidence; do not shorten Gate A or compress review |

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-18 | Kritvaos Actuator Team | 48-week reforecast overlay (ACT-DEC-030); A0 exit P6, forecast end 19 Sep 2027 |
| 0.2 | 2026-10-18 | Kritvaos Actuator Team | A0 exit P12 (ACT-DEC-032); Gate A to fabrication gap, re-sequenced to 58 weeks, end 28 Nov 2027 (ACT-DEC-033) |
