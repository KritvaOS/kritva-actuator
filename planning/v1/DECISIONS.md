# Kritva Actuator v1: Decision Log

| Field | Value |
|---|---|
| Document ID | KA-PLAN-DECISIONS |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 1.4 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead |
| Reviewer / Approver | Project Lead (with specialist reviewers where noted) |
| Applies to | A0, A1, A2 |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** This log is the **only place** where a proposed value or choice becomes binding. A requirement value marked "proposed pending approval" elsewhere in the repository becomes binding only when it is covered by an `ACCEPTED` entry here.

---

## 1. Purpose

This log records the project's significant technical and organisational decisions. For each one it gives the context, the alternatives considered, the rationale, the consequences, and the validation still required. Anyone joining the project can then see *why* the actuator is the way it is, and what evidence would justify changing it.

## 2. Decision process

1. **Raise.** Anyone may propose a decision by opening a GitHub Issue with the `design_change_request` template, or by adding a `PROPOSED` entry here in a pull request.
2. **Analyse.** The owner documents the context, alternatives and rationale. Calculations and data live in their canonical places (for example `mechanical/calculations/`) and are linked here.
3. **Review.**
   - Technical decisions are reviewed by the affected workstream owners.
   - Safety-relevant decisions are also reviewed by the relevant independent reviewer. If no qualified reviewer is available, the review is recorded as `NOT_VERIFIED`, and the decision cannot be used to pass a gate (ACT-DEC-014).
4. **Approve.** The Project Lead sets the status and date.
5. **Supersede.** A decision is never edited to reverse it. A new entry is created, and the old entry's status becomes `SUPERSEDED by ACT-DEC-NNN`.

| Status | Meaning |
|---|---|
| `PROPOSED` | Under evaluation. It must not be treated as binding. |
| `ACCEPTED` | Approved by the Project Lead. Binding until superseded. |
| `ACCEPTED (BASELINE)` | Approved as the working baseline, with named validation still pending. |
| `REJECTED` | Considered and not adopted (kept for the record). |
| `SUPERSEDED` | Replaced by a later decision. |

### 2.1 Entry template

```
### ACT-DEC-NNN — <title>
| Field | Value |
|---|---|
| Date | YYYY-MM-DD |
| Status | PROPOSED / ACCEPTED / ... |
| Owner | <role> |
| Approver | Project Lead |
| Related requirements | SYS-REQ-..., ... |
| Related tasks | ACT-0X-00Y |

**Context.** ...
**Decision.** ...
**Alternatives considered.** (table: option, advantages, limitations, verdict)
**Rationale.** ...
**Consequences.** ...
**Deferred.** ...
**Validation / release gate.** ...
```

## 3. Decision index

| ID | Title | Status | Date |
|---|---|---|---|
| ACT-DEC-001 | Project direction: Option C | ACCEPTED | 2026-10-11 |
| ACT-DEC-002 | Development Level 2 (buy motor, gearbox, encoder, bearings; build the rest) | ACCEPTED | 2026-10-11 |
| ACT-DEC-003 | Initial reduction mechanism: commercial planetary gearbox | ACCEPTED (BASELINE) for A0/A1; gearbox model pending validation | 2026-10-11 |
| ACT-DEC-004 | Motor-control MCU family: STM32G4 (C2000 alternative) | PROPOSED | 2026-10-11 |
| ACT-DEC-005 | A0 motor-control development board | PROPOSED (selection in ACT-01-002) | 2026-10-11 |
| ACT-DEC-006 | Communication: USB/UART for A0, CAN for A1, EtherCAT deferred | ACCEPTED | 2026-10-11 |
| ACT-DEC-007 | Target joint: humanoid elbow with a meaningful arm and link load | ACCEPTED | 2026-10-11 |
| ACT-DEC-008 | Elbow design load case and performance targets | PROPOSED | 2026-10-11 |
| ACT-DEC-009 | Independent 12 mm output shaft on a dedicated bearing pair | PROPOSED | 2026-10-11 |
| ACT-DEC-010 | Output-side encoder for joint position | ACCEPTED | 2026-10-11 |
| ACT-DEC-011 | Repository structure and ownership rules | ACCEPTED | 2026-10-11 |
| ACT-DEC-012 | Licence: proprietary, all rights reserved; superseded by ACT-DEC-035 | SUPERSEDED | 2026-10-11 |
| ACT-DEC-013 | Supply voltage 24 V DC nominal | ACCEPTED | 2026-10-11 |
| ACT-DEC-014 | Independent review rule and the NOT_VERIFIED gate block | ACCEPTED | 2026-10-11 |
| ACT-DEC-015 | Restrained-fixture testing; no human-interactive testing without a safety review | ACCEPTED | 2026-10-11 |
| ACT-DEC-023 | Repository visibility: private (EXT-AUD-001); superseded by ACT-DEC-034 | SUPERSEDED | 2026-10-13 |
| ACT-DEC-024 | Repository architecture: parent plus four submodules | PROPOSED | 2026-10-15 |
| ACT-DEC-025 | Actuator family S/M/L; M is the A0 reference | PROPOSED | 2026-10-15 |
| ACT-DEC-026 | Shared sizing engine in the parent | PROPOSED | 2026-10-15 |
| ACT-DEC-027 | Align with kritva-program V2: status reporting, crosswalk, mechanical HOLD | PROPOSED | 2026-10-16 |
| ACT-DEC-028 | 12-month roadmap (weeks 25-47) as the planning baseline | ACCEPTED (planning only) | 2026-10-18 |
| ACT-DEC-029 | Mechanical HOLD lifted; week 1 = 14 Sep 2026 | ACCEPTED | 2026-10-18 |
| ACT-DEC-030 | 48-week reforecast overlay (P1 = 19 Oct 2026, to 19 Sep 2027) | ACCEPTED (planning only) | 2026-10-18 |
| ACT-DEC-031 | Resourcing: three mechanical interns and one embedded intern from 1 Nov 2026 | ACCEPTED (planning input) | 2026-10-18 |
| ACT-DEC-032 | A0 exit extended to P12 (10 Jan 2027) | ACCEPTED (planning only) | 2026-10-18 |
| ACT-DEC-033 | Gate A to M fabrication gap of two weeks; re-sequenced reforecast | ACCEPTED (items 1-3); 58-week horizon PROPOSED | 2026-10-18 |
| ACT-DEC-034 | Repositories stay public; supersedes the private position of ACT-DEC-023 | ACCEPTED | 2026-10-24 |
| ACT-DEC-035 | Licence: Apache-2.0; supersedes ACT-DEC-012 | ACCEPTED | 2026-10-24 |

---

## 4. Decision entries

### ACT-DEC-001: Project direction, Option C

| Field | Value |
|---|---|
| Date | 2026-10-11 |
| Status | ACCEPTED |
| Owner | Project Lead |
| Related requirements | SYS-REQ-001, 006 |
| Related tasks | All |

**Context.** The first in-house actuator could have one of three primary objectives: (A) an educational motor-control platform, (B) a humanoid joint actuator, or (C) both, with the first evolving into the second. Each objective leads to different choices of motor, gearbox, sensors and controller.

**Decision.** Adopt **Option C**: *Educational motor-control platform → Smart actuator → Humanoid joint actuator*. The project runs as the **Kritva Actuator Development Platform**, in three milestones: A0 Educational Motor Control, A1 Humanoid Smart Actuator, A2 KritvaOS Integration.

**Alternatives considered.**

| Option | Advantages | Limitations | Verdict |
|---|---|---|---|
| A. Motor-control platform only | Fast, low risk, strong learning on FOC | No usable joint; work may not carry forward | Rejected |
| B. Humanoid joint immediately | Directly useful hardware | High risk; electronics and control not yet validated; failures hard to diagnose | Rejected |
| **C. Both, evolving** | Validates electronics and control independently before committing the mechanics; reusable IP | Requires discipline to keep interfaces reusable | **Accepted** |

**Rationale.** Option C validates the motor-control electronics and firmware first, then reuses them in a complete geared actuator. It follows the principle "build once, evolve through iterations": the first prototype is low cost, but it is not disposable.

**Consequences.** Interfaces (electrical, firmware configuration, mounting, communication, tests) must be designed for reuse from A0 onwards (SYS-REQ-006, 037).

**Validation / release gate.** Milestone exits as defined in `planning/v1/MILESTONE.md`.

---

### ACT-DEC-002: Development Level 2

| Field | Value |
|---|---|
| Date | 2026-10-11 |
| Status | ACCEPTED |
| Owner | Project Lead |
| Related requirements | SYS-REQ-002, 003, 005 |

**Context.** Development can range from Level 1 (commercial actuator plus KritvaOS integration) through Level 2 (in-house actuator using a commercial motor and gearbox) to Level 3 (custom motor and transmission).

**Decision.** Use **Level 2**.

- **Buy:** a commercial BLDC/PMSM motor, a planetary gearbox, the encoder(s) and the bearings.
- **Develop in-house:** the mechanical housing and output-shaft assembly, the motor driver and controller (development board in A0, custom PCB in A1), FOC and joint-control firmware, the communication interface, the safety mechanisms and the KritvaOS integration.

**Alternatives considered.**

| Level | Indicative effort | Verdict |
|---|---|---|
| 1: Commercial actuator + integration | 2–4 weeks | Rejected: little engineering ownership |
| **2: In-house actuator with a commercial motor and gearbox** | 8–12 weeks | **Accepted** |
| 3: Custom motor and transmission | 6–12+ months | Rejected for v1 |

**Explicitly excluded from the first milestone:**

- designing a motor from raw steel and magnets;
- a custom harmonic drive;
- a high-voltage inverter;
- FOC before the sensing hardware is validated;
- a complete humanoid joint before bench validation;
- relying on motor current alone for collision detection;
- operating an unvalidated actuator on a loaded humanoid joint.

---

### ACT-DEC-003: Initial actuator reduction mechanism

| Field | Value |
|---|---|
| Date | 2026-10-11 |
| Status | ACCEPTED (BASELINE) for A0/A1; final gearbox model pending validation |
| Owner | Mechanical Intern (evaluation), Project Lead (approval) |
| Related requirements | SYS-REQ-003, 004, 027, 028; MECH-REQ gearbox section |
| Related tasks | ACT-02-002 |

**Context.** The elbow needs a torque multiplication of the order of 15–25× from a commercial motor, in a compact coaxial package, at a low prototype budget.

**Decision.** Use a **commercially available planetary gearbox** for the initial actuator. Evaluate **20:1 first**, with **15:1 and 25:1** as alternatives, against the approved torque, speed, backlash, load and cost requirements. 20:1 is the initial evaluation candidate. It is **not** a mandatory specification and is not frozen until the motor torque-speed data are available.

**Alternatives considered.**

| Reduction approach | Advantages | Limitations | Verdict for Kritva |
|---|---|---|---|
| **Planetary gearbox** | Compact, coaxial, good torque density, readily available, straightforward motor integration | Backlash varies with gearbox quality; efficiency and load capacity depend on the design | **Selected for A0/A1** |
| Cycloidal gearbox | High reduction in a compact package; can achieve low backlash; suitable for robotic joints | Demanding mechanical design; tight tolerances; bearing and pin design complexity | Evaluate in a future iteration |
| Harmonic / strain-wave drive | Compact, high reduction, low backlash, good positioning precision | Higher cost; specialised components; flexspline fatigue | Deferred due to cost |
| Belt reduction | Inexpensive, easy to make, quiet, flexible packaging | Belt compliance; tensioning; less compact coaxial integration | Not the baseline |
| Direct drive | No gearbox backlash; mechanically simple | Needs a motor with enough torque at the required speed; larger motor and higher cost | Not the baseline |

**Rationale.**

- Reduces mechanical design complexity for the first prototype.
- Supports a compact, coaxial motor-and-gearbox assembly.
- Lets the interns concentrate on motor control, mechanical integration and joint characterisation.
- Provides a reusable foundation for later Kritva smart-actuator development.

**Consequences.** The gearbox must be selected from verified ratings (continuous and peak torque, efficiency, backlash, life, input speed, permitted output loads), and never from the ratio alone. External arm loads must not be carried by the gearbox output bearing unless its ratings explicitly permit them (see ACT-DEC-009). Reflected inertia, backdrivability and friction must be evaluated for their effect on compliant control.

**Deferred.** Custom cycloidal and harmonic/strain-wave mechanisms are reconsidered only when measured prototype limitations or future joint requirements justify the extra engineering effort and cost.

**Validation / release gate.** The selected gearbox must satisfy the documented requirements and pass the mechanical design audit and the acceptance audit (`audit/mechanical/MECHANICAL_DESIGN_AUDIT.md`, `MECHANICAL_ACCEPTANCE_AUDIT.md`) before the actuator design is approved for release.

**Superseded values (for the record).** Earlier provisional targets are **superseded by ACT-DEC-008** and must not be used:

- the educational-joint targets: 1–2 N·m continuous, 3–5 N·m peak, a 10 mm final joint shaft, and 5:1 / 10:1 / 15:1 ratios with 10:1 as the candidate;
- the interim table: 6–8 N·m continuous, 15–20 N·m peak, 30–60 RPM, and 10:1 / 15:1 / 20:1 ratios.

---

### ACT-DEC-004: Motor-control MCU family

| Field | Value |
|---|---|
| Date | 2026-10-11 |
| Status | **PROPOSED** |
| Owner | Electronics/Embedded Intern |
| Related requirements | SYS-REQ-055; ELEC-REQ MCU section; FW-REQ-002 |
| Related tasks | ACT-01-002, ACT-01-002a |

**Context.** FOC needs motor-control-grade peripherals:

- ADC sampling synchronised with PWM;
- complementary PWM with dead-time insertion;
- a hardware break/fault input;
- an FPU or sufficient compute;
- CAN/FDCAN;
- encoder interfaces;
- a watchdog.

Not every MCU or board is suitable.

**Proposed decision.** Use the **STM32G4 family** (for example STM32G431 or STM32G474, candidates). **TI C2000** is the evaluated alternative.

**Alternatives considered.**

| MCU family | Advantages | Considerations | Proposed verdict |
|---|---|---|---|
| **STM32G4** | Motor-control timers, fast ADCs, op-amps/comparators, FDCAN; large ecosystem; matches the intern skill profile (STM32); the moteus reference design is STM32G4-based | Careful peripheral and firmware configuration needed | **Proposed default** |
| TI C2000 | Strong motor-control ecosystem and control-oriented peripherals | Different toolchain and workflow | Alternative |
| STM32F4 | Good general-purpose platform | Check timer/ADC capabilities for the specific part | Not preferred |
| ESP32 family | Accessible ecosystem | Real-time behaviour, analog and peripheral support, safety need evaluation | Not preferred for FOC |

**Validation.** ACT-01-002a confirms the choice against the development-board availability in India, the toolchain, and the peripheral check list in `requirements/ELECTRICAL_REQUIREMENTS.md`. Status then changes to `ACCEPTED`.

---

### ACT-DEC-005: A0 motor-control development board

| Field | Value |
|---|---|
| Date | 2026-10-11 |
| Status | **PROPOSED** (selection in ACT-01-002a) |
| Owner | Electronics/Embedded Intern |
| Related requirements | SYS-REQ-005, 045; ELEC-REQ development-board section |

**Context.** A0 uses a commercial motor-control development board, so that motor-control learning is separated from power-stage design risk. A custom PCB follows in A1. A custom PCB is **not** a prerequisite for A0 success.

**Candidates to evaluate** (verify availability, current rating at 24 V, current-sensing topology, CAN access and price):

| Candidate | Notes |
|---|---|
| ST B-G431B-ESC1 | Low-cost STM32G431 ESC; check its continuous current against the selected motor |
| NUCLEO-G474RE + X-NUCLEO-IHM08M1-class power board | Flexible lab setup; separates the MCU and power boards |
| ODrive-class controller | Mature reference platform for motor control; use as a reference or alternative |

**Decision criteria.** These are defined in `requirements/ELECTRICAL_REQUIREMENTS.md` section 7. The A0 budget is ₹3,000–₹5,000 for the board, against the ₹10,000–₹15,000 A0 total (provisional).

---

### ACT-DEC-006: Communication interfaces

| Field | Value |
|---|---|
| Date | 2026-10-11 |
| Status | ACCEPTED |
| Owner | Project Lead / Integration Owner |
| Related requirements | SYS-REQ-060, 061, 067; IF-REQ CAN section |

**Decision.** Use **USB/UART** for A0, and for debugging in all phases. Use **CAN** for A1 real-time command, feedback and diagnostics (classic CAN 2.0B at 1 Mbit/s baseline; CAN FD-capable hardware preferred, TBC). **EtherCAT** is deferred and will be introduced only if the robot needs deterministic coordination across many joints.

**Rationale.** CAN keeps the hardware and firmware simple, is well supported by STM32G4 FDCAN, and is adequate for a first multi-joint bus.

---

### ACT-DEC-007: Target joint

| Field | Value |
|---|---|
| Date | 2026-10-11 |
| Status | ACCEPTED |
| Owner | Project Lead |
| Related requirements | SYS-REQ-001 |

**Context.** Initially a small educational tabletop joint was considered.

**Decision.** The first actuator shall **support a humanoid elbow joint with a meaningful arm and link load**. The elbow was chosen over the hip or knee as a manageable starting point that still reuses the electronics and firmware for larger joints later.

**Consequences.** Torque targets, shaft, bearings and gearbox were upgraded from the educational baseline (see ACT-DEC-008).

---

### ACT-DEC-008: Elbow design load case and performance targets

| Field | Value |
|---|---|
| Date | 2026-10-11 |
| Status | **PROPOSED** |
| Owner | Project Lead; calculations by the Mechanical Intern |
| Related requirements | SYS-REQ-010–014, 020–022, 042 |
| Related tasks | ACT-02-001, ACT-02-002 |

**Load case.**

- Forearm and hand: 1.5 kg, centre of mass at **180 mm** (provisional assumption, to be replaced from CAD or measurement).
- Payload: 1.0 kg at 350 mm.
- Worst case: arm horizontal.
- Static gravity torque: **T_g = 1.5·9.81·0.18 + 1.0·9.81·0.35 = 2.65 + 3.43 = 6.08 N·m**.

**Targets (proposed).**

| Rating | Target | Basis |
|---|---|---|
| Continuous output torque | 10 N·m | ≈ 1.64 × T_g |
| Peak output torque | 20 N·m minimum, 25 N·m stretch | Dynamic reserve; duration and duty TBD |
| Output speed | up to 45 RPM (4.71 rad/s) | Approved speed target |
| Output power at 10 N·m, 45 RPM | 47.1 W | — |
| Motor | 75–100 W continuous mechanical candidate, 24 V | Losses plus thermal margin |
| Gearbox continuous rating | ≥ 10 N·m at the operating conditions | — |
| Gearbox peak rating | ≥ 25 N·m if the 25 N·m target is adopted | Verify the manufacturer's definition |

**Still required before ACCEPTED:**

- a measured centre of mass;
- the angular acceleration requirement;
- the duty cycle and continuous horizontal holding duration;
- the peak duration, repetition rate and recovery;
- the choice between 20 and 25 N·m.

---

### ACT-DEC-009: Output shaft and support

| Field | Value |
|---|---|
| Date | 2026-10-11 |
| Status | **PROPOSED** |
| Owner | Mechanical Intern |
| Related requirements | SYS-REQ-030–034; MECH-REQ-002, 003 |
| Related tasks | ACT-02-003 |

**Decision (proposed).**

- Use an **independent output shaft with a 12 mm nominal initial CAD diameter**, supported on a **dedicated bearing pair** in the joint housing.
- External radial, axial and bending loads go through the shaft, bearings and housing, **bypassing the gearbox and motor bearings**.
- The motor shaft is used as supplied (typically 5–6 mm). The gearbox output interface is preferably ≥ 8 mm.

**Notes.**

- The nominal torsional shear in a 12 mm solid shaft is 29.5 / 58.9 / 73.7 MPa at 10 / 20 / 25 N·m. These figures exclude bending, stress concentration and fatigue.
- Bearing type (deep-groove pair, angular-contact pair or crossed-roller) is chosen **after** the load calculation.
- A 12 mm shaft can still fail if it is poorly supported or has a long overhang. Bearing spacing and load paths matter as much as the nominal diameter.

**Validation.** Gate A items 3 and 4, and the independent review of SHAFT_STRENGTH.md and BEARING_SELECTION.md.

---

### ACT-DEC-010: Output-side encoder

| Field | Value |
|---|---|
| Date | 2026-10-11 |
| Status | ACCEPTED |
| Related requirements | SYS-REQ-024, 052 |

**Decision.** Mount the position encoder on the joint/output side of the gearbox, so that the controller measures the true joint position, including backlash and compliance effects. Motor-side feedback is used for commutation and motor-side measurement. A magnetic absolute encoder is proposed; the IC is selected in ACT-01-003. An encoder alone cannot eliminate mechanical backlash.

---

### ACT-DEC-011: Repository structure and ownership rules

| Field | Value |
|---|---|
| Date | 2026-10-11 |
| Status | ACCEPTED |
| Related requirements | SYS-REQ-102–107 |

**Decision.** Adopt the repository structure in `README.md`, with these ownership rules:

- `requirements/` is the canonical source of *what* the actuator must do.
- `planning/v1/` holds planned work, owners and approvals.
- `docs/` holds architecture, procedures, interfaces and the validation approach.
- `mechanical/`, `hardware/`, `firmware/`, `communication/` and `software/` hold the implementation.
- `tests/` holds test code and procedures. `results/` holds measured evidence.
- `audit/` holds independent reviews and gate decisions, never duplicate design documents.
- `.github/` holds collaboration templates and CI.
- There is one canonical home per artefact.
- Folders are populated incrementally. Placeholder `.gitkeep` files may mark agreed but empty folders.

---

### ACT-DEC-012: Licence

**Status:** SUPERSEDED by ACT-DEC-035 (Apache-2.0), 2026-10-24. Original decision (2026-10-11): the repository is proprietary and confidential, with all rights reserved by Kritvaos. Reuse of third-party open-source code (for example SimpleFOC under MIT, or moteus under Apache-2.0) requires a licence-compatibility review approved by the Project Lead (FW-REQ-074).

---

### ACT-DEC-013: Supply voltage

**Status:** ACCEPTED. **Decision:** 24 V DC nominal. The operating range, withstand voltage including regeneration, and reverse-polarity behaviour are specified in `requirements/ELECTRICAL_REQUIREMENTS.md` (proposed 20–28 V operating and ≥ 32 V withstand, TBC). Bench bring-up uses a current-limited PSU.

---

### ACT-DEC-014: Independent review rule

**Status:** ACCEPTED.

**Decision.**

- No author is the sole approver of their own safety-critical design.
  - The Mechanical Intern does not approve their own shaft, bearing or housing calculations.
  - The Electronics/Embedded Intern is not the sole approver of power-stage protection or motor-control safety.
- If no qualified independent reviewer is available, the review is recorded as `NOT_VERIFIED`, and the related release gate stays blocked.
- ChatGPT may act as a remote independent technical reviewer, but it is not the sole authority for safety-critical approval. Qualified human review is required.
- A safety-critical defect can never be treated as non-blocking to meet a deadline.

---

### ACT-DEC-015: Test conduct

**Status:** ACCEPTED.

**Decision.**

- Loaded, peak-torque and fault tests are performed only on a **restrained, guarded, instrumented fixture**.
- Testing by manually resisting the actuator, or by attaching it to a person, is prohibited.
- No human-interactive testing takes place until a qualified human reviewer has approved the mechanical and electrical safety evidence.
- Deployment on the humanoid needs a separate system-level safety review.

See `requirements/SAFETY_REQUIREMENTS.md`.

### ACT-DEC-024: Repository architecture (parent plus four submodules)

**Status:** PROPOSED (external reviewer recommendation 2026-10-15; the Project Lead adopted the plan of three Mechanical Interns and one Embedded Intern).

**Decision.** `KritvaOS/kritva-actuator` stays the parent (program and integration). Four child repositories are added as submodules: `kritva-actuator-s`, `-m`, `-l` (mechanical, one intern each) and `kritva-actuator-embedded`. The parent owns requirements, interface contracts, common sizing, planning, audits and integration tests, and pins reviewed child commits. Migration is staged and non-destructive (`planning/v2/MIGRATION_PLAN.md`). Details: `docs/architecture/REPOSITORY_ARCHITECTURE.md`.

**Supersedes in part.** The two-intern split in `planning/v1/TASKS.md` for new work. Legacy IDs remain valid (`planning/v2/TASK_ID_MAPPING.csv`). ACT-DEC-001 (project direction) is not changed.

---

### ACT-DEC-025: Actuator family S, M, L

**Status:** PROPOSED.

**Decision.** The three mechanical interns build three variants of one platform. M is the elbow reference baseline and the A0 reference. S and L start from the M template after M passes the design review checklist. The S, M and L torque and speed classes in `docs/architecture/ACTUATOR_FAMILY_SPEC.md` are **provisional planning envelopes, not approved requirements**.

---

### ACT-DEC-026: Shared sizing engine

**Status:** PROPOSED.

**Decision.** One sizing engine (`actuator_sizing.py`) and its regression expected values live in the parent at `mechanical/common-sizing/`. Each variant supplies its own `sizing/inputs.json`. Results are stored in the variant repository with the parent commit used. The A0 reference calculation documents stay in the parent (`mechanical/calculations/`). The standard-library-only constraint is kept, hence JSON inputs.

---

### ACT-DEC-027: Alignment with kritva-program V2

**Status:** PROPOSED (external program audit 2026-10-16; Project Lead approval pending).

**Decision.** The actuator repositories adopt the kritva-program V2 reporting method as a target operating model without giving up their stricter local rules: (1) each repository publishes task facts in `status/status.json` (schema 2.0, generated from `status/tasks.csv` by `scripts/status/gen_status.py`); review and acceptance stay in kritva-program `approvals.json`; (2) the actuator workstreams are mapped to program workstreams and local milestones to program phases only through `planning/v2/PROGRAM_CROSSWALK.csv`, never by similar names or numbers; (3) the status files are not registered in kritva-program `sources.json` until the program owner approves the workstream IDs, baseline tasks and evidence rules (ONBOARDING.md); (4) mechanical work is on HOLD at program level, so the 24-week plan is planning-only until the owner reopens it, and the local safety gates (ACT-DEC-014, ACT-DEC-015, Gates A/B/C) are unaffected by program status. Details: `docs/standards/PROGRAM_ALIGNMENT.md`.

---

### ACT-DEC-028: 12-month roadmap as the planning baseline

**Status:** ACCEPTED (planning only), 2026-10-18. Approver: Project Lead (Dinesh). Approval was conveyed in the working session of 2026-10-18 by Sangeetha (sangeetha@kritvaos.in) on the Project Lead's behalf; the Project Lead may confirm it in the pull request.

**Decision.** `planning/v2/ROADMAP_12_MONTHS.md` (rev 0.2) is the planning baseline for weeks 25 to 47 (indicative 5 Apr to 12 Sep 2027), extending `ROADMAP_24_WEEKS.md` to the kritva-program V2 horizon. Weeks 1 to 24 are unchanged. Week numbers are actuator-local; dates are indicative.

**Not decided by this entry** (each remains open and needs its own decision):
- Lifting the mechanical HOLD (kritva-program D-003), or the week-1 start date.
- The optional A2-SW checkpoint at week 12, and which of the v1 and v2 calendars applies (crosswalk in `ROADMAP_12_MONTHS.md` section 3.2). A2 remains one milestone; its exit criteria in `planning/v1/MILESTONE.md` are unchanged.
- ACT-DEC-027, which stays PROPOSED.
- Resourcing of weeks 25 to 47, and registration of the horizon in `planning/v2/PROGRAM_CROSSWALK.csv`.

**Consequences.** The roadmap stays planning-only. It does not authorise procurement, fabrication, CAD release or loaded testing, does not change any gate, task ID or status file, and creates no program credit. Safety gates (ACT-DEC-014, ACT-DEC-015, Gates A/B/C) apply unchanged. Independent review was not required because the change is planning-only and not safety-relevant.

---

### ACT-DEC-029: Mechanical HOLD lifted; week 1 = 14 Sep 2026

**Status:** ACCEPTED, 2026-10-18. Approver: Project Lead (Dinesh). Approval was conveyed in the working session of 2026-10-18 by Sangeetha (sangeetha@kritvaos.in) on the Project Lead's behalf; the Project Lead may confirm it in the pull request.

**Decision.** The mechanical HOLD (kritva-program D-003, not to be confused with `ACT-DEC-003`, the gearbox decision) is lifted, and actuator program week 1 is Mon 14 Sep 2026. This does not authorise CAD release, procurement, fabrication, design freeze or loaded testing by itself: Gate A, the pending decisions in section 5, ACT-DEC-014 and ACT-DEC-015 apply. The lift must also be recorded in kritva-program, which this repository cannot do. ACT-DEC-027 stays PROPOSED.

---

### ACT-DEC-030: 48-week reforecast overlay

**Status:** ACCEPTED (planning only), 2026-10-18. Approver: Project Lead (Dinesh). Approval was conveyed in the working session of 2026-10-18 by Sangeetha (sangeetha@kritvaos.in) on the Project Lead's behalf; the Project Lead may confirm it in the pull request.

**Decision.** `planning/v2/ROADMAP_48_WEEKS.md` (rev 0.1) is the planning reforecast. (1) Horizon: 48 weeks, P1 = Mon 19 Oct 2026, forecast end 19 Sep 2027. (2) Official week 1 stays 14 Sep 2026 (ACT-DEC-029); the P-weeks are a dated overlay, P(n) = official week n + 5. (3) ACT-DEC-028 is amended only in that its reserve end (12 Sep 2027) is extended by one week; its original text stands. (4) A0 exits at P6, the M prototype checkpoint is P12, and A1 completes only through Gates A/B/C. The custom PCB and CAN firmware remain the A1 baseline; a development-board substitute is a reviewed deviation. (5) One PCB respin window (P23-P27), used only with evidence and Project Lead approval. (6) S/L design and A2-SW may run in parallel after M Gate A. (7) P46-P48 is reserve only.

**Not decided by this entry.** How the M prototype checkpoint (P12) and Gate A (P9-P12) are reconciled; the A0 exit date against actual evidence; the torque classes, which stay as in ACT-DEC-025 (PROPOSED), with no broader range becoming a requirement without an approved load case; candidate shoulder and ankle applications; registration in kritva-program.

**Consequences.** Planning only. No gate, task ID, status file or approved value changes. v1 targets (A1 weeks 11-12, A2 week 12) are superseded as planning targets only; their text stays. Independent review was not required because the change is planning-only and not safety-relevant.

---

### ACT-DEC-031: Resourcing from 1 Nov 2026

**Status:** ACCEPTED (planning input), 2026-10-18. Approver: Project Lead (Dinesh). Approval was conveyed in the working session of 2026-10-18 by Sangeetha (sangeetha@kritvaos.in) on the Project Lead's behalf; the Project Lead may confirm it in the pull request.

**Decision.** Three mechanical interns and one embedded intern work on the project from 1 Nov 2026 (first working day Mon 2 Nov, P3). The assignment of the mechanical interns to M, S and L is not decided here. The embedded intern's ramp-up inside P3 to P6 puts the A0 exit date at risk; confirm or reforecast it from actual evidence. Review capacity is unchanged.

---

### ACT-DEC-032: A0 exit extended to P12

**Status:** ACCEPTED (planning only), 2026-10-18. Approver: Project Lead (Dinesh). Approval was conveyed in the working session of 2026-10-18 by Sangeetha (sangeetha@kritvaos.in) on the Project Lead's behalf; the Project Lead may confirm it in the pull request.

**Decision.** The instruction was to extend the A0 (Educational Motor Control) exit by 4 to 8 weeks beyond P6. P12 (ending Sun 10 Jan 2027, six weeks later) was chosen on the recommendation of an external planning discussion, within the instructed range: the embedded intern starts at P3, so P12 gives about ten weeks for bring-up, debugging and review. A0 exit requires the reviewed evidence package in `planning/v2/ROADMAP_48_WEEKS.md` section 4 and is never declared from the calendar. A0 exit does not prove loaded M torque capability, PCB readiness or A1 Gate B/C acceptance. This amends ACT-DEC-030 item 4 (A0 exit at P6) and mitigates the ramp-up risk in ACT-DEC-031; the original entries stand.

**Consequences.** Planning only. No gate, task ID, status file or approved value changes. The v1 target (A0 at week 6) is superseded as a planning target only; its text stays in `MILESTONE.md`.

---

### ACT-DEC-033: Gate A to fabrication gap; re-sequenced reforecast

**Status:** ACCEPTED (planning only) for items 1 to 3, 2026-10-18; item 4 PROPOSED. Approver: Project Lead (Dinesh). Approval was conveyed in the working session of 2026-10-18 by Sangeetha (sangeetha@kritvaos.in) on the Project Lead's behalf; the Project Lead may confirm it in the pull request.

**Decision.** (1) M fabrication starts after Gate A passes plus a two-week fabrication release and procurement gap, chosen within the instructed 2 to 4 weeks: Gate A by P14 (24 Jan 2027), release and procurement P15-P16, M fabrication and assembly from P17. Nothing is fabricated against an unapproved design. (2) The M prototype checkpoint moves to P23 (22-28 Mar 2027); it is not an A1 release. (3) The sequence in `planning/v2/ROADMAP_48_WEEKS.md` rev 0.2 applies: custom PCB first spin after A0 exit and Gate A (P24-P28), Gate B P29-P33, contingency respin P34-P38, Gate B regression P39-P40, Gate C P41, S/L design from P15, A2-SW from P24, A2-HW P42-P46, qualification P47-P52, release P53-P54, reserve P55-P58. (4) **PROPOSED:** the forecast end becomes Sun 28 Nov 2027 (58 weeks), replacing the 48-week horizon of ACT-DEC-030; the Project Lead is asked to confirm. The respin window and reserve were not squeezed to protect a date.

**Prerequisite for Gate A.** The pending decisions ACT-DEC-016 to 021 (section 5) are recorded, and independent review (ACT-DEC-014) is done. The "needed by" gates in section 5 were set against the earlier plan and should be re-dated to P11-P14.

**Consequences.** Planning only. Gates A/B/C, independent review and restrained-fixture testing are unchanged; a failed gate moves downstream dates and is never waived. The resourcing from ACT-DEC-031 is a planning input; review capacity is unchanged.

### ACT-DEC-034: Repositories stay public

**Status:** ACCEPTED, 2026-10-24. Approver: Project Lead (Dinesh), stated in the working session of 2026-10-24.

**Decision.** `KritvaOS/kritva-actuator` and the four child repositories (`kritva-actuator-s`, `-m`, `-l`, `-embedded`) stay **public**. This supersedes the private position of ACT-DEC-023 and its amendments (the planned return to private, exit conditions and review date of 2026-11-16 no longer apply).

**Consequences.** Documents that described the repository as private were updated on 2026-10-24 (README, SECURITY.md, REPOSITORY_ARCHITECTURE.md, SUBMODULE_WORKFLOW.md, MIGRATION_PLAN.md, the docs-checks workflow comment). The default `GITHUB_TOKEN` is enough for submodule checkout; `CHILD_REPOS_TOKEN` is needed only if a child is ever made private. Because the repositories are public, nothing that must stay confidential (supplier quotes, personal data, credentials, third-party datasheets without redistribution rights) may be committed. The licence is handled separately in ACT-DEC-035.

### ACT-DEC-035: Licence is Apache-2.0

**Status:** ACCEPTED, 2026-10-24. Approver: Project Lead (Dinesh), stated in the working session of 2026-10-24. Supersedes ACT-DEC-012.

**Decision.** The parent repository is licensed under the **Apache License, Version 2.0** (`LICENSE`, `NOTICE`), for code, firmware, hardware design files and documentation alike. Copyright is held by Kritvaos. Contributions are accepted under the same licence. Reuse of third-party code still needs a licence-compatibility review approved by the Project Lead (FW-REQ-074); permissive licences (MIT, BSD, Apache-2.0) are compatible, and copyleft code (GPL, and LGPL without a linking review) must not be included without a recorded decision.

**Consequences.** The `LICENSE` text, source-file headers, the document `Classification` field (now `Public (Apache-2.0, see LICENSE)`), `check_docs.py`, CONTRIBUTING, CODE_OF_CONDUCT and the licence wording in the requirements and standards were updated on 2026-10-24. Apache-2.0 is a software-oriented licence; if a hardware-specific licence (for example CERN-OHL) is wanted for CAD and PCB files later, that is a new decision. The four child repositories need their own `LICENSE` and `NOTICE`; this decision does not change them. Files that already carried a third-party licence keep it. Historical audit records under `audit/` are not rewritten.

---

## 5. Pending decisions (to be raised)

| Topic | Expected ID | Owner | Needed by |
|---|---|---|---|
| Final gearbox model and ratio | ACT-DEC-016 | Mechanical Intern + Electronics/Embedded Intern | M1 gate |
| Motor model | ACT-DEC-017 | Both interns | M1/E1 gates |
| Output encoder IC and magnet | ACT-DEC-018 | Electronics/Embedded Intern + Mechanical Intern | ACT-01-003 |
| Output bearing type and arrangement | ACT-DEC-019 | Mechanical Intern | Gate A |
| Safe-state option per fault class (coast vs active damping) | ACT-DEC-020 | Project Lead + reviewer | Before loaded tests |
| Peak torque rating (20 vs 25 N·m) and duration | ACT-DEC-021 | Project Lead | Motor/gearbox freeze |
| CAN payload encoding (scaled integers vs float) | ACT-DEC-022 | Project Lead / Integration Owner | F1 |

**ACT-DEC-023 amendment (2026-10-15, Project Lead).** The parent and the four child repositories were made **temporarily public** so that tooling and the external reviewer can read them while the restructure is finished. This is a time-limited exception to the private position; the repositories must return to private before any further proprietary content is added (see `docs/architecture/REPOSITORY_ARCHITECTURE.md` open item 5 for the CI token). Everything currently in them is proprietary and confidential by classification.

**ACT-DEC-023 amendment, exit conditions (2026-10-16, Project Lead).** The temporary public state continues while task, folder, milestone and status-reporting structure is aligned across the program repositories and the external audits are running. Owner: Project Lead (approval authority). Return to private when that alignment is agreed, or earlier if any supplier quote, controller firmware, fabrication drawing or personal data is about to be committed. Before the change: a secrets and history scan of all five repositories, a review of known forks and cached copies, and an IP and licensing check. Review date: 2026-11-16, or at the next audit, whichever is earlier. A later change to private does not recall copies already made.

**ACT-DEC-023 resolved (2026-10-13, Project Lead).** The repository was moved to **private** (EXT-AUD-001). It supersedes the earlier interim position (stay public until the specification is filled in). Follow-up: GitHub visibility is recorded here as the owner's action; the history and tracked-artifact review (EXT-AUD-018, `git rm -r "Claude outputs"`) and a secrets scan remain recommended before any external sharing or a future public subset.

## 6. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
| 0.2 | 2026-10-12 | Kritvaos Actuator Team | Pending decision ACT-DEC-023 repository visibility (EXT-AUD-001) |
| 0.3 | 2026-10-13 | Kritvaos Actuator Team | ACT-DEC-023: interim position (stay public until the specification is filled in; conditions recorded) |
| 0.4 | 2026-10-13 | Kritvaos Actuator Team | ACT-DEC-023 ACCEPTED: repository private |
| 0.5 | 2026-10-15 | Kritvaos Actuator Team | ACT-DEC-024 to 026 PROPOSED: four-submodule architecture, actuator family, shared sizing engine |
| 0.6 | 2026-10-15 | Kritvaos Actuator Team | ACT-DEC-026: A0 reference calculation documents stay in the parent |
| 0.7 | 2026-10-15 | Kritvaos Actuator Team | ACT-DEC-023 amendment: repositories temporarily public |
| 0.8 | 2026-10-16 | Kritvaos Actuator Team | ACT-DEC-027 PROPOSED (kritva-program V2 alignment); ACT-DEC-023 exit conditions |
| 0.9 | 2026-10-18 | Kritvaos Actuator Team | ACT-DEC-028 ACCEPTED: 12-month roadmap as planning baseline |
| 1.0 | 2026-10-18 | Kritvaos Actuator Team | ACT-DEC-029 ACCEPTED: mechanical HOLD lifted, week 1 = 14 Sep 2026 |
| 1.1 | 2026-10-18 | Kritvaos Actuator Team | ACT-DEC-030 (48-week reforecast overlay) and ACT-DEC-031 (resourcing) ACCEPTED |
| 1.2 | 2026-10-18 | Kritvaos Actuator Team | ACT-DEC-032 (A0 exit P12) and ACT-DEC-033 (Gate A to fabrication gap, 58-week reforecast proposed) |
| 1.3 | 2026-10-24 | Kritvaos Actuator Team | ACT-DEC-034 ACCEPTED: repositories stay public; supersedes ACT-DEC-023 |
| 1.4 | 2026-10-24 | Kritvaos Actuator Team | ACT-DEC-035 ACCEPTED: Apache-2.0 licence; supersedes ACT-DEC-012 |
