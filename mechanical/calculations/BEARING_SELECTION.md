# Kritva Actuator: Output Bearing Selection

| Field | Value |
|---|---|
| Document ID | KA-CALC-BEARING |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.3 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Mechanical Intern |
| Reviewer / Approver | Independent Mechanical Reviewer / Project Lead |
| Applies to | A1 |
| Classification | Proprietary and confidential |

> **Status note.** Bearing type and size are **not yet selected**. ACT-DEC-009 says to select them after the load calculation. This document performs that calculation with assumed geometry. Catalogue ratings are **typical published values** for the generic size and must be verified against the chosen manufacturer's catalogue. The results are proposed and pending approval.

---

## 1. Purpose

This document sizes the **dedicated output bearing pair** that carries the forearm's radial, axial and moment loads independently of the gearbox and motor bearings (SYS-REQ-031/032, MECH-REQ-003). It covers static capacity, life, arrangement, fits and preload.

Numbers are reproduced by `python3 mechanical/common-sizing/actuator_sizing.py --section bearing`.

## 2. Arrangement and assumptions

```
          B_far                 B_near        flange (load line)
   |======[  ]==================[  ]==========|
          <---------- L --------->  <--- a --->
               25 mm (assumed)       20 mm (assumed)
```

- The two bearings are treated as simple supports. The radial load F acts at the flange.
- R_near = F·(1 + a/L), R_far = F·a/L.
- **Axial load:** from forearm orientation and handling. TBD from CAD; it is small for a horizontal elbow axis. One bearing locates the shaft axially and the other floats, or the pair is preloaded with a wave spring.
- Static safety factor target **s0 ≥ 2.0 (TBC)**. This is common practice for shock-loaded, low-speed robotic joints.
- Life target **L10h ≥ 2 000 h (TBC)** at an equivalent mean speed of 10 RPM (TBC: the duty cycle is not yet defined).

## 3. Bearing reactions

| Load case | F at flange | R_near | R_far |
|---|---|---|---|
| LC-01 link weight | 24.5 N | 44.1 N | 19.6 N |
| LC-02 weight + centripetal | 38.3 N | 68.9 N | 30.6 N |
| LC-03 2 × weight (dynamic allowance) | 49.1 N | 88.3 N | 39.2 N |
| **LC-05 single-sided stop at 25 N·m, r_s = 25 mm** | **1 000 N** | **1 800 N** | **800 N** |

**Span sensitivity for LC-05:**

| L | R_near | R_far |
|---|---|---|
| 15 mm | 2 333 N | 1 333 N |
| 20 mm | 2 000 N | 1 000 N |
| 25 mm | 1 800 N | 800 N |
| 30 mm | 1 667 N | 667 N |
| 40 mm | 1 500 N | 500 N |

A wider span and a shorter overhang both reduce R_near. However, the dominant lever is the **stop configuration** (section 5).

## 4. Candidate deep-groove bearings (single-sided stop, governing LC-05)

Ratings are typical catalogue values; verify them with the vendor.

| Bearing | d × D × B (mm) | C (kN) | C0 (kN) | s0 at LC-05 | s0 ≥ 2.0? | L10h at LC-02 and 10 RPM |
|---|---|---|---|---|---|---|
| 6001 | 12 × 28 × 8 | 5.40 | 2.36 | 1.31 | No | ≫ 10⁶ h |
| 6201 | 12 × 32 × 10 | 7.28 | 3.10 | 1.72 | No | ≫ 10⁶ h |
| 6002 | 15 × 32 × 9 | 5.85 | 2.85 | 1.58 | No | ≫ 10⁶ h |
| 6202 | 15 × 35 × 11 | 8.06 | 3.75 | 2.08 | Yes | ≫ 10⁶ h |

**Observations.**

1. **Life is not the issue.** At these low speeds and normal loads, L10 life far exceeds any requirement. The selection is governed by **static capacity under the stop/stall case**, plus stiffness and size.
2. With a **single-sided** stop and 12 mm bearings, s0 < 2 at LC-05. Only a 15 mm bore (6202) meets s0 ≥ 2. That would mean stepping the shaft up to 15 mm at the bearing seats.

## 5. Balanced (two-sided) stop: preferred, but credit only after proof

If the hard stop uses **two stop features 180° apart**, the stop torque reacts as a **couple**. The net radial force on the shaft is ideally zero; in practice it is limited to the share mismatch from tolerances, say ≤ 20 % (TBC). With that arrangement:

| Case | Governing R_near | 6001 s0 | 6201 s0 |
|---|---|---|---|
| Balanced stop, 20 % mismatch (200 N at the flange) | 360 N | 6.6 | 8.6 |
| No stop load (LC-03) | 88 N | 26.7 | 35.1 |

With a **proven** balanced stop, **a 6001 or 6201 pair on the 12 mm shaft is ample**.

**Condition (EXT-AUD-004/006).** The balanced-stop reduction may be credited **only after** the simultaneous-engagement proof required by `LOAD_CASES.md` §8.2: a tolerance analysis plus a bench measurement. Until that proof exists, the single-sided case LC-05 governs the selection (§4), and the baseline below is sized for it.

## 6. Bearing type options

| Arrangement | Advantages | Limitations | Use when |
|---|---|---|---|
| **Pair of deep-groove ball bearings (6001/6201), one located and one floating, or wave-spring preloaded** | Cheap, available in India, tolerant of small misalignment, simple housing | Moderate moment stiffness; needs adequate span | **Recommended baseline**, with a balanced stop |
| Angular-contact pair (for example 7001 back-to-back), preloaded | High moment stiffness and axial capacity; no play | Needs preload control and tighter tolerances; higher cost | If deflection or encoder runout is too high with deep-groove bearings |
| Thin-section / crossed-roller bearing | Very compact axially, high moment capacity, hollow centre (cable or encoder) | Cost and lead time; precise housing needed | A later revision targeting compactness |

## 7. Fits, preload and sealing (proposed, TBC with the vendor's recommendations)

| Item | Proposal |
|---|---|
| Shaft fit (rotating inner ring, light load) | k5 or j5 at the bearing seats |
| Housing fit (stationary outer ring) | H7 for the floating bearing, K7 or J7 for the located bearing |
| Axial location | Shoulder plus circlip, or a nut on the located bearing; the floating bearing slides in an H7 bore |
| Preload (if used) | Wave spring on the floating outer ring, about 20–50 N (TBC) |
| Sealing | 2RS (contact seals) for A1, to keep debris out of the bearings; ZZ if friction must be minimised |
| Lubrication | Factory grease, sealed-for-life |

## 8. Housing and alignment

- Bore both bearing seats in **one set-up**, so that they are coaxial (target ≤ 0.02 mm TIR, TBC).
- The housing seat must not be 3D-printed (SAF-REQ-043). Use aluminium with the bores machined directly, or a steel bearing carrier.
- Bearing clearance plus shaft deflection must stay within the output-encoder air-gap and runout tolerance.

## 9. Recommendation (screening; final selection at M2 with vendor data)

1. **Baseline, sized for the single-sided case LC-05:** step the bearing seats to **15 mm** and use a pair of **6202-size (15 × 35 × 11) deep-groove 2RS bearings**, s0 ≈ 2.1. Alternatively, use an angular-contact pair if stiffness or axial load requires it. The 12 mm shaft diameter is kept between the seats and at the coupling end, so the shaft check in SHAFT_STRENGTH still applies at its 12 mm sections.
2. Adopt a **balanced, two-sided hard stop** reacting into the housing as the preferred design. If simultaneous engagement is later proven (LOAD_CASES §8.2), a **6001/6201 pair on 12 mm seats** may be adopted through a recorded decision (ACT-DEC-019), with this document re-run.
3. Bearing span **≥ 25 mm**, with the shortest practical overhang.
4. Replace the typical catalogue ratings with the **selected vendor's catalogue values**. Add the axial and combined-load cases (static equivalent load P0 = X0·Fr + Y0·Fa), fits, clearance and preload, and the stiffness and encoder-alignment checks, using the CAD geometry.
5. Record the final choice as **ACT-DEC-019**.

**Status of 6202 (EXT-AUD-021).** 6202 is a **candidate baseline, not an approved or released part**. The s0 ≈ 2.08 result is a static screening value from the assumed single-sided 1 000 N flange load and a generic C0 = 3.75 kN; it cannot certify the selection. The selection stays open until CAD reactions, vendor catalogue ratings, axial and moment loads and the final stop configuration are reviewed. The BOM item MB-004 carries status CANDIDATE.

## 10. Verification

| Item | Method | Gate |
|---|---|---|
| Independent recalculation with CAD geometry | Analysis | M2 / Gate A |
| Vendor catalogue values | Inspection of the datasheet | M2 |
| Bore coaxiality and fits | Inspection | M3 |
| No damage after the loaded and impact tests (smooth rotation, no added play) | Inspection and test | Gate B |

## 11. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | Geometry a, L and r_s from CAD | Mechanical Intern | M2 |
| 2 | Stop configuration decision | Mechanical Intern | M2 |
| 3 | Axial load case (orientation, handling) | Mechanical Intern | M2 |
| 4 | Duty cycle, for life (mean speed) | Project Lead | Gate A |
| 5 | Vendor selection and catalogue data | Mechanical Intern | M2 |

## 12. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
| 0.2 | 2026-10-12 | Kritvaos Actuator Team | External audit fixes: single-sided case governs until balanced engagement proven; baseline 6202 on 15 mm seats; vendor/combined-load checks (EXT-AUD-004/006/012) |
| 0.3 | 2026-10-12 | Kritvaos Actuator Team | Re-verification: 6202 stated as candidate, not released (EXT-AUD-021) |
