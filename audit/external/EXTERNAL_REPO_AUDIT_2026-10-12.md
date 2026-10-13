# Kritva Actuator: External Repository Audit, 2026-10-12

| Field | Value |
|---|---|
| Document ID | KA-AUD-EXT-20261012 |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.4 (Draft: proposed, pending approval) |
| Date | 2026-10-12 |
| Document owner | Project Lead (record keeper); findings owned by the external reviewer |
| Reviewer / Approver | External reviewer: ChatGPT (remote documentary audit) / Project Lead |
| Applies to | A0, A1 |
| Classification | Proprietary and confidential |

> **Status note.** This records a **remote documentary and calculation audit** of the public repository at commit `58d7e6f` (`ACT-03-006: Add documentation baseline v0.1`). It was performed by ChatGPT acting as an external technical reviewer.
>
> Per ACT-DEC-014 this review is **not** a qualified human sign-off, and it does not close any gate on its own. It is an input to M0 and to repository governance. Findings are owned by the reviewer; the dispositions below are the author's responses, which the reviewer must verify.

---

## 1. Scope and result

| Item | Value |
|---|---|
| Commit reviewed | `58d7e6fa39a12b06a53664ba2e5205608caa8a7b` (main) |
| Scope | Baseline alignment; cross-document consistency; engineering calculations; acceptance and traceability; repository hygiene, licence, CI and templates |
| Reviewer disposition | **M0: FAIL / NOT READY TO CLOSE.** Component selection and fabrication release: **BLOCKED**. Repository and documentation framework: substantially aligned, with findings open. No CRITICAL finding; multiple HIGH findings |
| Arithmetic verified by the reviewer | T_g = 6.082 N·m; 10/6.082 = 1.64×; 45 RPM = 4.712 rad/s; 47.1 W output; 55.4 W motor at η 0.85; 900 RPM and 0.588 N·m at 20:1; E = 1.90 J (point mass); τ = 73.7 MPa at 25 N·m (12 mm); bearing reactions 1 800 N / 800 N for the stated model. **No arithmetic error found** |
| Main concern | Assumptions, incomplete load paths, and missing validated component and acceptance evidence |

## 2. Findings and dispositions

The disposition states what was changed in the follow-up commit. **CLOSED-BY-AUTHOR** means the author considers the documentation action done; the external reviewer must still verify it. **OPEN** findings need data, a decision or design work that documents alone cannot supply.

| ID | Sev. | Finding (summary) | Disposition | Status |
|---|---|---|---|---|
| EXT-AUD-001 | HIGH | The repository is **public**, but the LICENSE and documents say proprietary and confidential | Needs a Project Lead decision: make the repository private, or split out a public subset with a licence/IP review. Recorded as pending decision **ACT-DEC-023**. README status table flags it. **2026-10-13: the Project Lead moved the repository to private (ACT-DEC-023 ACCEPTED).** Reviewer to verify the GitHub setting | **CLOSED-BY-AUTHOR** (verify) |
| EXT-AUD-002 | HIGH | M0 is NOT VERIFIED. Centre of mass, α, duty cycle, holding duration, peak repetition and limits are TBD. ACT-DEC-008 is PROPOSED | Accepted. These are the M0 blockers (section 3). M0 stays FAIL until they are closed | **OPEN: data / decision** |
| EXT-AUD-003 | HIGH | The hard-stop model (linear 2E/θ, point-mass J) is not a validated design load | `LOAD_CASES.md` §8.1 added: model limitations; effective-inertia table including the forearm's centroidal inertia and the reflected rotor (2.1–2.8 J instead of 1.90 J); required bumper force–deflection characterisation; +20 % energy margin; approach speed set from the characterised curve; instrumented FI-24/DU-03. The final value still needs CAD inertia plus a bumper test | Doc: CLOSED-BY-AUTHOR. Design: **OPEN** |
| EXT-AUD-004 | HIGH | The balanced stop is not proven: contact simultaneity, pin/lug/housing/fastener loads, and torque through the gearbox are unchecked | `LOAD_CASES.md` §8.2 added. **Design rule: the single-contact case LC-05 governs** until a tolerance analysis and bench proof show simultaneous engagement. M2 component checks are listed (pins, lugs, housing, fasteners, coupling/gearbox torque, rotor-inertia share). `BEARING_SELECTION`, `SHAFT_STRENGTH`, `MECHANICAL_DESIGN_SPECIFICATION` and the risk register updated | Doc: CLOSED-BY-AUTHOR. Design: **OPEN** |
| EXT-AUD-005 | HIGH | The 12 mm shaft SF depends on unverified geometry, Kt and material data | `SHAFT_STRENGTH.md` §7: the result is conditional, and the shaft is **not frozen**. Recompute with CAD, actual Kt and certified material. Repeated stop fatigue added as a separate case | Doc: CLOSED-BY-AUTHOR. Design: **OPEN** |
| EXT-AUD-006 | HIGH | Bearing selection is screening only; axial and combined loads are TBD; 6001/6201 are adequate only with a balanced stop | `BEARING_SELECTION.md` §9: **baseline changed to 6202 (15 × 35 × 11) on 15 mm seats**, sized for single contact. 6001/6201 allowed only after the balanced stop is proven. Vendor catalogue, P0 = X0·Fr + Y0·Fa, fits, preload and stiffness required at M2. BOM MB-004 and the design specification updated | Doc: CLOSED-BY-AUTHOR. Design: **OPEN** |
| EXT-AUD-007 | HIGH | Motor/gearbox sizing is a trade study, not a verified operating point | Accepted. Joint selection with real datasheets and quotations in ACT-02-002 (M1). The 20:1 ratio is not frozen by default (already ACT-DEC-003) | **OPEN: ACT-02-002** |
| EXT-AUD-008 | MED | The Kv→Kt/current conversion has no frozen convention | `TORQUE_AND_SPEED.md` §2.1 added: Kv, Ke, Kt, current and resistance conventions with conversion rules (line-to-line vs phase, RMS vs peak; Kt = (√3/2)·Ke_LL = 8.27/Kv). `MOTOR_CONTROLLER_SPECIFICATION` references it. Kt, R and L are measured in A0 before E2 | CLOSED-BY-AUTHOR |
| EXT-AUD-009 | HIGH | Several acceptance criteria are not numeric pass/fail | Accepted. Each limit is a **blocker** for its gate (section 3). The limits must be approved before the corresponding test (already a rule in VALIDATION_PLAN §2) | **OPEN: Project Lead** |
| EXT-AUD-010 | MED | Traceability rows point to generic or placeholder procedures and evidence | `check_traceability.py` now **errors** if a row claims PASS, PASS_WITH_ACTIONS or FAIL without a concrete `results/` record and a requirement-specific procedure with a test ID. It reports the placeholder count. CSV procedures are now mapped per requirement family to specific procedures (PC-, BU-, FI-, CAN-, CT-, MI- IDs) | CLOSED-BY-AUTHOR (per-requirement procedure IDs are refined as tests are written) |
| EXT-AUD-011 | MED | Calculation CI is a smoke run, with no document consistency check | `scripts/validation/check_calcs.py` plus `mechanical/calculations/expected_results.json` added: a regression check of 14 key results and a check that each appears in its document. Added to `make check` and the CI workflow | CLOSED-BY-AUTHOR |
| EXT-AUD-012 | MED | The governing stop geometry can change the shaft and bearing load path | Final stop configuration plus CAD dimensions made a **prerequisite** for closing SHAFT_STRENGTH and BEARING_SELECTION (§8.2 design rule; M2-03/04/05) | Doc: CLOSED-BY-AUTHOR. Design: **OPEN** |
| EXT-AUD-013 | MED | The README baseline could be read as approved | README section 1.1 renamed "Proposed design baseline (NOT approved, NOT frozen)", with an explicit status block naming ACT-DEC-008/009 as PROPOSED and M0 open | CLOSED-BY-AUTHOR |
| EXT-AUD-014 | MED | A green firmware workflow could be mistaken for a firmware pass | `firmware-build.yml` now emits a **warning annotation and a job summary**: "SKIPPED (not applicable) … not a firmware PASS" | CLOSED-BY-AUTHOR |
| EXT-AUD-015 | MED | No CODEOWNERS; branch protection not verified | `.github/CODEOWNERS` added (placeholders defaulting to the repository owner; replace with the role accounts). **Branch protection must be set by an administrator:** require PR, code-owner review and the `docs-checks` status on `main` | CODEOWNERS: CLOSED-BY-AUTHOR. Protection: **OPEN: admin** |
| EXT-AUD-016 | LOW | Opaque `Claude outputs/kritva-protected-files.zip` committed | It was a delivery archive of `Makefile` and `.github/`, now extracted. `Claude outputs/` added to `.gitignore`. **The committed copy must be removed** with `git rm -r "Claude outputs"` in a reviewed commit | **OPEN: delete in git** |
| EXT-AUD-017 | OBS | Baseline alignment is generally good | Noted | CLOSED |
| EXT-AUD-018 | MED | (re-verification) `Claude outputs/kritva-protected-files.zip` is still tracked in `main` (Git LFS pointer); `.gitignore` cannot untrack it | Same action as EXT-AUD-016: `git rm -r "Claude outputs"` in a reviewed commit | **OPEN: delete in git** |
| EXT-AUD-019 | HIGH | (re-verification) `check_calcs.py` regression covered only the point-mass 1.90 J / 47.5 N·m values, not the 2.1–2.8 J effective-inertia range | `actuator_sizing.py` gains `effective_inertia()`; `expected_results.json` / `check_calcs.py` now regression-test J_rod, E_rod and the low, mid and high rotor corner cases (J and E) and the rotor share, and check they appear in `LOAD_CASES.md` §8.1. The point-mass 1.90 J is stated as illustrative only. The check also caught a documentation error (low-end rotor share is 2 %, not 4 %), now corrected | CLOSED-BY-AUTHOR (24 results checked) |
| EXT-AUD-020 | MED | (re-verification) CODEOWNERS does not enforce review: branch protection is off and handles are placeholders | Unchanged from EXT-AUD-015: replace the handles, then an administrator enables required PR review, CODEOWNERS review and the `docs-checks` status check on `main` | **OPEN: admin** |
| EXT-AUD-021 | MED | (re-verification) The 6202 baseline is still a conditional static screening result | `BEARING_SELECTION.md` §9 now states that 6202 is a candidate baseline, not an approved or released part, and BOM MB-004 is CANDIDATE. Selection stays open until CAD reactions and vendor data are reviewed | Doc: CLOSED-BY-AUTHOR. Design: **OPEN** |

## 3. M0 blockers (must close before M0 can PASS)

| # | Blocker | Finding | Owner | Needed by |
|---|---|---|---|---|
| B1 | Forearm and hand mass properties from CAD or measurement (replace 180 mm) | 002 | Mechanical Intern | M0 |
| B2 | Approved angular acceleration, duty cycle, horizontal holding duration | 002 | Project Lead | M0 |
| B3 | Peak torque (20 vs 25 N·m) with duration, repetition and recovery | 002, 009 | Project Lead | M0 |
| B4 | Final joint range and mass/envelope budget | 009 | Project Lead + Mechanical Intern | M0 |
| B5 | Numerical limits: position error, repeatability, backlash, thermal-stability criterion | 009 | Project Lead | Before M1 / tests |
| B6 | ACT-DEC-008 accepted (or explicit blockers recorded) | 002 | Project Lead | M0 |
| B7 | Repository visibility decision (ACT-DEC-023): **closed 2026-10-13, private** | 001 | Project Lead | Done |

The design items (stop architecture, shaft, bearings, motor/gearbox) are **M1/M2** closures (EXT-AUD-003 to 007, 012) and are tracked in `audit/mechanical/MECHANICAL_DESIGN_AUDIT.md` §5.

## 4. Reviewer verification of closure

| Finding | Closure evidence (commit / file) | Verified by external reviewer | Date |
|---|---|---|---|
| 008, 010 (checker), 013, 014, 016 (ignore rule) | Commit `894860e` (`ACT-03-006: Address external audit findings EXT-AUD-003..016`) | **VERIFIED** by the external reviewer | 2026-10-13 |
| 003, 004, 005, 006, 011, 012, 015 (CODEOWNERS) | Commit `894860e` | **PARTIAL**: documentation action accepted, design validation or enforcement still open | 2026-10-13 |
| 018, 019, 020, 021 (new) | Raised in the re-verification; 019 and 021 addressed in the second follow-up commit | Pending | — |

Re-verification result (2026-10-13): CI `docs-checks` green at `894860e`. **M0 remains FAIL / NOT READY TO CLOSE**, unchanged by the verified items. The reviewer found no change to the headline architecture.

## 5. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-12 | Kritvaos Actuator Team | Initial record of external audit EXT-AUD-001..017 with dispositions |
| 0.2 | 2026-10-13 | Kritvaos Actuator Team | Re-verification of commit 894860e recorded; new findings EXT-AUD-018..021 with dispositions |
| 0.3 | 2026-10-13 | Kritvaos Actuator Team | EXT-AUD-001: deferral and conditions recorded |
| 0.4 | 2026-10-13 | Kritvaos Actuator Team | EXT-AUD-001 and blocker B7 closed (repository private) |
