# Kritva Actuator: Motor and Gearbox Shortlist (ACT-02-002)

| Field | Value |
|---|---|
| Document ID | KA-MECH-CALC-SHORTLIST |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.2 (Draft: proposed, pending approval) |
| Date | 2026-10-13 |
| Document owner | Mechanical Intern |
| Reviewer / Approver | Independent Mechanical Reviewer / Project Lead |
| Applies to | A1 |
| Classification | Proprietary and confidential |

> **Status note.** This is a **screening shortlist for supplier quotation. It is not a component selection and does not close ACT-DEC-003, ACT-DEC-016 or ACT-DEC-017.** The candidate data were gathered by the ChatGPT reviewer session on 2026-10-13 (it labelled each figure DATASHEET-VERIFIED or UNVERIFIED) and have **not** been independently re-checked against the vendor pages; web search is not enabled for this project's Claude sessions. Fit calculations in §3 are the author's, using `TORQUE_AND_SPEED.md` conventions. Operating point values remain provisional (M0 blockers B1 to B6 are open, see `planning/v1/M0_DECISION_SHEET.md`).

---

## 1. Provisional operating point

| Item | Value | Source |
|---|---|---|
| Supply | 24 V DC | ACT-DEC-013 |
| Output torque, continuous | 10 N·m | ACT-DEC-008 (PROPOSED) |
| Output torque, peak | 20 N·m minimum, 25 N·m stretch; duration, repetition and recovery **not yet set** (B3) | ACT-DEC-008, M0 sheet |
| Output speed | 45 RPM | ACT-DEC-008 |
| Ratio | 20:1 first; 15:1 and 25:1 alternatives | ACT-DEC-003 |
| Motor speed at 20:1 | 900 RPM | 45 RPM × 20 |
| Gearbox efficiency for sizing | **0.85** (repository baseline). The ChatGPT session used 0.92; the datasheet range quoted is 92 to 98 % at best operating point, so 0.85 stays the conservative sizing value until measured | `TORQUE_AND_SPEED.md` |
| Stop-impact torque (screening) | 47.5 N·m at 45 RPM, 2 mm bumper, 25 mm radius | `LOAD_CASES.md` §8 (screening, not a design load) |

Required motor shaft torque at 20:1: continuous 0.588 N·m (η 0.85) or 0.543 N·m (η 0.92); 20 N·m peak 1.176 N·m; 25 N·m peak 1.471 N·m (η 0.85).

## 2. Candidate data (as reported by the ChatGPT reviewer session)

Label meaning: **DV** = reported as appearing in the linked manufacturer specification; **UV** = not established, or an indicative retail listing only. Links are the manufacturer pages named in the session; re-open them before quoting.

### 2.1 Motors (frameless inrunner BLDC/PMSM, manufacturer CubeMars)

| Model | Rated torque (N·m) | Peak torque (N·m) | Kv (RPM/V) | Kt (N·m/A) | R phase-phase (Ω) | Rated speed at 24 V (RPM) | Rated power (W) | Mass (g) | Price and availability |
|---|---|---|---|---|---|---|---|---|---|
| RI50 KV100 | 0.58 DV | 1.67 DV | 100 DV | 0.120 DV | 1.420 DV | 1 090 DV | 100 max continuous DV | 180.8 DV | See §2.2 |
| RI60 KV120 | 0.57 DV | 1.63 DV | 120 DV | 0.100 DV | 0.900 DV | 1 440 DV | 85 DV | 155.9 DV | See §2.2 |
| RI70 KV95 | 0.94 DV | 2.68 DV | 95 DV | UV (not confirmed) | 0.418 DV | 1 270 DV | 125 DV | 270.4 DV | See §2.2 |
| RI80 V2.0 KV75 | 1.45 DV | 4.1 DV | 75 DV | 0.155 DV | 0.330 DV | 1 135 DV | 172 DV | 411 DV | See §2.2 |

### 2.2 Online pricing check (2026-10-13, author, built-in browser)

Prices read directly from the listing pages on 2026-10-13. Listings change; they are **not quotations**. Neither shipping, import duty nor GST was visible without starting a checkout, which was not done.

| Motor | CubeMars store (USD, "from", ex shipping) | Robokits India (INR, "with Hall sensor" listing) | Other |
|---|---|---|---|
| RI50 KV100 | $61.90 | ₹8,245 | none checked |
| RI60 KV120 | $98.90 | ₹12,208 | IndiaMART supplier listing ₹16,520; DigiKey India lists it (page blocked by a bot check, price not read) |
| RI70 KV95 | $123.90 (style: without or with Hall sensor) | ₹14,885 | none checked |
| RI80 V2.0 KV75 | $132.90 | ₹19,327 | none checked |

Observations:

1. The Robokits INR prices match the figures the ChatGPT session reported for the RI60 (₹12,208) and differ for the RI80 (₹19,327 now, ₹22,929 reported), so the session's retail figures are **not reliable for the RI80**. Use this section, and re-check before ordering.
2. The cost gap between RI60 and RI70 is about ₹2,700 at Robokits. That is small against the benefit of the RI70's continuous-torque margin (§3.1).
3. Price differences between the CubeMars store (US$, "from" price, likely the without-Hall variant) and the Indian retailer (with Hall sensor, local stock) cannot be compared without shipping, duty and GST; ask for a delivered quotation.
4. **No online price was found for any gearbox.** Neugart and WITTENSTEIN list configured products by quotation. The gearbox is likely to be the largest cost item and the one most at risk against the A1 budget (₹20,000 to ₹30,000 cumulative, `MECHANICAL_BOM.csv`); no figure is assumed here.
5. The motors are frameless kits sold as rotor and stator. Any housing, bearings, coupling and encoder come on top (see §3.4).

### 2.3 Planetary gearboxes (2-stage, 20:1 available; series-level ranges, not part-number ratings)

| Model | Continuous (N·m) | Maximum (N·m) | Emergency stop (N·m) | Backlash (arcmin) | Efficiency | Mass (kg) | Price and availability |
|---|---|---|---|---|---|---|---|
| Neugart PLE 040 | 6 to 17 DV | 12 to 32 DV | 27 to 40 DV | 15 to 22 DV | 92 to 98 % DV | 0.4 to 0.5 DV | UV: configured quotation |
| Neugart PLE 060 | 15 to 37 DV | 28 to 70 DV | 80 to 88 DV | 10 to 15 DV | 92 to 98 % DV | 0.9 to 1.3 DV | UV: configured quotation |
| Neugart PLPE 050 | 4 to 13 DV | 8 to 24 DV | 27 to 40 DV | 15 to 19 DV | 97 to 98 % DV | 0.6 to 0.8 DV | UV: configured quotation |
| WITTENSTEIN alpha DP+ (benchmark) | exact model UV | 50 to 825 DV (family) | UV | ≤ 3 DV (DP+), ≤ 1 (High Torque) DV | UV | UV | UV |

## 3. Fit against the provisional operating point (author's calculation)

### 3.1 Motors at 20:1, 900 RPM

Motor torque demand as a share of the motor's rated (continuous) and peak torque. Copper loss is an **estimate** from I²R with the vendor Kt and the phase-to-phase resistance, P = 1.5·I²·R_LL; it assumes the vendor Kt is per A of the same current used in this formula (see §3.3) and ignores iron, friction and inverter losses.

| Motor | Continuous demand η 0.85 | Continuous demand η 0.92 | 25 N·m peak demand (η 0.85) | Speed vs 24 V rated | Copper loss at continuous torque (estimate) |
|---|---|---|---|---|---|
| RI50 KV100 | **101 %** of rated | 94 % | 88 % of peak | 83 % | about 51 W |
| RI60 KV120 | **103 %** of rated | 95 % | 90 % of peak | 62 % | about 47 W |
| RI70 KV95 | 63 % of rated | 58 % | 55 % of peak | 71 % | about 14 W (Kt estimated, UV) |
| RI80 V2.0 KV75 | 41 % of rated | 37 % | 36 % of peak | 79 % | about 7 W |

Findings:

1. **With the repository's 0.85 efficiency, RI50 and RI60 are at or just above their rated torque** at the 10 N·m continuous target, and about 90 % of peak at 25 N·m. They only fit with the optimistic 0.92 efficiency, with no margin for the holding and cycle duty that is still undefined (B2, B3). Their estimated copper loss (40 to 50 W) is close to the 47 W output power, so thermal behaviour, not torque, will decide whether they work.
2. **RI70 has comfortable torque margin** (63 % of rated) and an estimated copper loss of about 14 W, but is above the preferred 75 to 100 W class (125 W rated, 270 g).
3. RI80 is oversized (411 g, 172 W) and is a fallback and benchmark only.
4. All four motors reach 900 RPM at 24 V with margin (62 to 83 % of rated speed). The repository's Kv floor for 20:1 (59.5 RPM/V, `TORQUE_AND_SPEED.md`) is met by all four.

### 3.2 Gearboxes against the requirements

| Requirement | PLE 040 | PLE 060 | PLPE 050 |
|---|---|---|---|
| Continuous ≥ 10 N·m | Only the upper variants (6 to 17) | Yes (15 to 37) | Only the upper variants (4 to 13), marginal |
| Maximum ≥ 20 N·m (25 stretch) | Only upper variants (12 to 32) | Yes (28 to 70) | Only the upper end (8 to 24), cannot reach 25 |
| Emergency stop ≥ 47.5 N·m screening stop torque | **No** (27 to 40) | Yes (80 to 88) | **No** (27 to 40) |
| Backlash ≤ 0.5° discussion figure | Yes (0.25° to 0.37°) | Yes (0.17° to 0.25°) | Yes (0.25° to 0.32°) |
| Mass | 0.4 to 0.5 kg | 0.9 to 1.3 kg | 0.6 to 0.8 kg |

The stop-impact torque is a screening value (`LOAD_CASES.md` §8.1) that will fall once the approach speed is limited and the bumper is characterised, but until then **only PLE 060 clears it**. Backlash in arcmin is converted to degrees at the gearbox output (1 arcmin = 1/60°).

### 3.3 Convention check: vendor Kt versus the repository's Kt = 8.27/Kv

The repository convention (`TORQUE_AND_SPEED.md` §2.1) gives Kt = 8.27/Kv per A phase-peak. The vendor Kt values are **about 1.4 to 1.45 times larger** (RI50: 0.120 vs 0.083; RI60: 0.100 vs 0.069; RI80: 0.155 vs 0.110). The ratio is close to √2, which suggests the vendor quotes Kt per A RMS, but **this is an unconfirmed inference.** Ask the vendor for its Kt definition, and measure Kt, R and L on the bench before E2 (as the convention document already requires). Current and copper-loss figures above change by up to about 2× if this is wrong, so treat them as indicative only.

### 3.4 Mechanical interface risk (not evaluated by the reviewer)

The motors are frameless kits. A frameless rotor and stator have no housing or bearings of their own, so the motor shaft, rotor mounting, motor bearings and a coupling to the gearbox input are **in-house design work** (ACT-02-003 and the housing design). A 60 mm gearbox flange and a 60 mm motor are not automatically compatible. Ask the gearbox supplier for the input-shaft and adapter options, and decide between a frameless kit and a housed motor (with a standard flange) before freezing the pair. UV.

## 4. Comparison and recommendation

| | Option A: RI60 + PLE 060 (ChatGPT quote-first) | Option B: RI70 + PLE 060 (author preference) |
|---|---|---|
| Continuous torque margin at η 0.85 | None (103 % of rated) | Yes (63 % of rated) |
| Peak 25 N·m margin | 90 % of motor peak | 55 % of motor peak |
| Estimated motor heat at 10 N·m | about 47 W (UV) | about 14 W (UV) |
| Mass (motor + gearbox) | about 1.1 to 1.5 kg | about 1.2 to 1.6 kg |
| Power class | Within 75 to 100 W (85 W rated) | Above (125 W rated) |
| Cost | Lower (about ₹12k motor, UV) | Unknown |

**Recommendation (proposed, pending approval).**

- Request quotations for **both** pairs, as ChatGPT suggested, with the **PLE 060 at 20:1** (and 15:1 and 25:1) as the common gearbox. The PLE 060 is the only listed gearbox that clears the continuous, peak and emergency-stop requirements.
- Treat **Option B (RI70)** as the preferred technical candidate until the RI60 is shown to hold 10 N·m continuously within temperature limits, because at the repository's conservative efficiency the RI60 has no continuous margin. If the vendor's torque-speed and thermal data show the RI60 is acceptable, its lower mass and cost make it the better choice. This view differs from the ChatGPT ordering (RI60 first) and the reason is the efficiency assumption: 0.85 here, 0.92 in the session.
- Keep PLE 040 and PLPE 050 only as lightweight alternatives if the stop energy is limited by design below their emergency-stop rating and the supplier confirms the exact model's continuous rating.
- Keep WITTENSTEIN alpha DP+ as a benchmark only (oversize and cost).

## 5. Questions for suppliers

1. Exact configured part numbers, 20:1, 15:1 and 25:1.
2. Motor: torque-speed curve at 24 V, continuous torque at 900 RPM, winding temperature limit and thermal resistance, phase resistance and inductance, the definition of Kt (peak or RMS, phase or line), permitted peak torque and duration, frameless kit contents (shaft, bearings, hall or encoder).
3. Gearbox: continuous output torque at 45 RPM, peak torque with allowed repetitions and recovery, efficiency at the operating point, backlash, life, radial and axial output load ratings, input shaft and motor adapter options.
4. Mass, dimensions and interface drawings, lead time, warranty, and delivered price to India including shipping, duties and taxes.
5. Compatibility with an STM32G4 FOC drive and a separate output-side encoder.

## 6. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 0 | Obtain gearbox quotations (no online price exists); compare with the A1 budget | Mechanical Intern | M1 |
| 1 | Re-check every candidate figure against the vendor pages; record datasheets in `mechanical/bom/` (no vendor documents are committed yet) | Mechanical Intern | M1 |
| 2 | Obtain quotations and confirm 20:1 configurations and prices | Mechanical Intern | M1 |
| 3 | Vendor definition of Kt; reconcile with `TORQUE_AND_SPEED.md` §2.1 | Electronics/Embedded Intern | Before E2 |
| 4 | Decide frameless kit versus housed motor; motor-to-gearbox coupling concept | Both interns | M1/M2 |
| 5 | Approve peak duration, repetition and duty (B2, B3) so thermal margin can be calculated | Project Lead | Before motor and gearbox freeze |
| 6 | Record decisions ACT-DEC-016 (gearbox) and ACT-DEC-017 (motor) | Both interns | M1/E1 |

## 7. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-13 | Kritvaos Actuator Team | Initial shortlist from the ChatGPT session data, with fit calculations |
| 0.2 | 2026-10-13 | Kritvaos Actuator Team | Online price check added (§2.2): CubeMars store and Robokits India; no gearbox prices available online |
