# Kritva Actuator: Safety Requirements

| Field | Value |
|---|---|
| Document ID | KA-REQ-SAF |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-11 |
| Document owner | Project Lead |
| Reviewer / Approver | Independent Mechanical Reviewer and Independent Electrical/Firmware Reviewer / Project Lead |
| Applies to | A0, A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** The reaction times, thresholds and limits here are **proposed targets pending approval**. They become binding only when the Project Lead approves them and records the approval in `planning/v1/DECISIONS.md`. This document supports a laboratory development programme. It is **not** a certification-grade safety case.

---

## 1. Purpose

This document identifies the hazards of the Kritva Actuator during development, testing and integration, and specifies the safety requirements (`SAF-REQ-NNN`) that control them.

It defines:

- the safe states;
- the emergency-stop function;
- the fault reactions at system level;
- the safe test procedures;
- the fault-injection verification list;
- the safety review and sign-off process for Gate C.

It derives from `requirements/SYSTEM_REQUIREMENTS.md` section 8.8 (SYS-REQ-080 to 085). The firmware fault table (`requirements/FIRMWARE_REQUIREMENTS.md`, section 13) and the interface fault vocabulary (`requirements/INTERFACE_REQUIREMENTS.md`, section 8.13) implement these requirements.

## 2. Safety philosophy

1. **Experimental device.** The Kritva Actuator is an experimental prototype. It is **not a human-safe joint**. Nothing in A0–A2 establishes that it is safe for human-interactive operation.
2. **Restrained-fixture testing only.** Loaded, peak-torque and fault tests are performed only on a rigid, guarded, instrumented fixture (ACT-DEC-015). Nobody manually resists the actuator, holds it while it is energised under load, or attaches it to a person.
3. **Staged risk reduction.** Testing moves through four stages: low voltage with current limiting, then no load, then representative load, then peak load. Each stage starts only after the protection functions for that stage are verified (SYS-REQ-084).
4. **Hardware first for the most severe hazards.** Overcurrent and emergency stop have hardware paths that do not depend on correct firmware.
5. **Independent review.** No author approves their own safety-critical design (ACT-DEC-014). ChatGPT may act as a remote independent technical reviewer, but it is **not the sole authority** for safety approval. A qualified human reviewer must approve the safety evidence. If no qualified reviewer is available, the item is recorded as `NOT_VERIFIED` and Gate C stays blocked.
6. **Separate review before deployment.** Installation on the humanoid robot, and any human-interactive testing, need a separate system-level safety review (SYS-REQ-085).

## 3. References

| Ref | Document |
|---|---|
| [R1] | `requirements/SYSTEM_REQUIREMENTS.md` (parent) |
| [R2] | `requirements/MECHANICAL_REQUIREMENTS.md` |
| [R3] | `requirements/ELECTRICAL_REQUIREMENTS.md` |
| [R4] | `requirements/FIRMWARE_REQUIREMENTS.md` |
| [R5] | `requirements/INTERFACE_REQUIREMENTS.md` |
| [R6] | `audit/mechanical/MECHANICAL_RISK_REGISTER.md` (mechanical failure modes) |
| [R7] | `planning/v1/RISKS_AND_DEPENDENCIES.md` (project risks) |
| [R8] | `docs/validation/VALIDATION_PLAN.md` (fault-injection execution) |
| [R9] | ISO 12100 (risk assessment and risk reduction): guidance only |
| [R10] | IEC 60204-1 (stop categories 0/1/2, emergency stop): guidance only |
| [R11] | ISO 10218-1/-2 and ISO/TS 15066 (industrial and collaborative robots): guidance for future work |
| [R12] | IEC 61800-5-2 (safe torque off (STO) concept for drives): guidance only |

Standard editions are to be confirmed. The project does not claim compliance with any of them.

## 4. Risk assessment method

Risk is assessed as **Severity × Likelihood**. The method follows the general approach of ISO 12100 and is simplified for laboratory use.

| Severity | Description |
|---|---|
| S1 | Negligible: no injury; minor equipment damage. |
| S2 | Minor: first-aid injury; repairable damage to the actuator or fixture. |
| S3 | Serious: injury needing medical treatment (laceration, crush, burn); destruction of the actuator or test equipment; small fire. |
| S4 | Severe: permanent injury; fire spreading beyond the bench. |

| Likelihood | Description |
|---|---|
| L1 | Remote: not expected during the programme. |
| L2 | Unlikely: could happen once. |
| L3 | Possible: could happen several times. |
| L4 | Likely: expected without controls. |

| Risk score (S × L) | Class | Required action |
|---|---|---|
| 1–3 | Low | Accept and monitor. |
| 4–6 | Medium | Controls required before the related test stage. |
| 8–9 | High | Controls required and verified; Project Lead approval. |
| 12–16 | Very high | Not acceptable. Redesign, or do not perform the activity. |

The residual risk after controls must be **Low or Medium** before the related test stage begins. A residual **High** risk needs Project Lead approval plus independent reviewer sign-off.

## 5. Hazard analysis

| ID | Hazard | Cause(s) | Consequence | S | L | Initial | Controls (requirements) | Residual |
|---|---|---|---|---|---|---|---|---|
| HAZ-001 | Unexpected motion at enable or mode change | Controller not initialised from the measured state; wrong encoder offset; stale setpoint | Arm swings; impact with a person or the fixture | S3 | L3 | 9 High | Bumpless enable holding the measured position; enable preconditions; clear zone (SAF-REQ-010, 011, 060) | S3 × L1 = 3 Low |
| HAZ-002 | Runaway motion on communication loss | Host crash, cable fault, bus-off, while a velocity or torque command is active | Joint drives into the hard stop or a person | S3 | L3 | 9 High | Command timeout → safe state; bus-off treated as loss (SAF-REQ-020, 021) | S3 × L1 = 3 Low |
| HAZ-003 | Overcurrent leading to power-stage failure, overheating or fire | Phase short, motor stall, control instability, gate-driver fault, overtemperature | MOSFET explosion, burnt PCB, small fire, burns | S3 | L3 | 9 High | Hardware overcurrent trip; fusing; current-limited PSU; thermal monitoring; non-flammable bench (SAF-REQ-030 to 033, 070) | S3 × L1 = 3 Low |
| HAZ-004 | Supply short or wrong polarity | Wiring error; damaged cable; reverse connection | Wiring fire; PSU damage | S3 | L2 | 6 Medium | Reverse-polarity protection; input fuse; keyed connectors (SAF-REQ-034) | S2 × L1 = 2 Low |
| HAZ-005 | Hot surfaces | Continuous 10 N·m test; motor or driver overtemperature | Skin burn on contact | S2 | L3 | 6 Medium | Thermal limits; surface ≤ 60 °C target; warning label; gloves for handling after tests (SAF-REQ-035, 036) | S2 × L1 = 2 Low |
| HAZ-006 | Pinch or crush at the joint | Fingers between the output link and the housing or the hard stop | Finger crush or laceration | S3 | L3 | 9 High | Guarding; hands-off rule while energised; clear zone; pinch-point marking (SAF-REQ-040, 060, 061) | S3 × L1 = 3 Low |
| HAZ-007 | Hard-stop impact damage and part ejection | Firmware fault drives the link into the stop at speed (≈ 1.9 J at 45 RPM) | Stop or fastener fracture; parts ejected; gearbox damage | S3 | L2 | 6 Medium | Soft limits with deceleration; energy-absorbing hard stops sized by calculation; guard enclosure; safety glasses (SAF-REQ-041, 042, 062) | S2 × L1 = 2 Low |
| HAZ-008 | Shaft, bearing or housing fracture under load | Under-designed shaft or housing; 3D-printed load-bearing part; fatigue; overload | Load drops; parts ejected | S3 | L2 | 6 Medium | Calculations reviewed at Gate A; metal load path; staged load increase; post-test inspection (SAF-REQ-043, 044, 063) | S2 × L1 = 2 Low |
| HAZ-009 | Arm falls on power loss or fault | No holding brake; coast safe state; backdrivable gearbox | Forearm or payload drops onto a hand or the fixture | S3 | L3 | 9 High | Fixture supports the arm at the low position; optional active damping; nobody beneath the load (SAF-REQ-012, 045, 064) | S2 × L2 = 4 Medium |
| HAZ-010 | Wrong position from an encoder failure | Magnet loss or slip, SPI error, misalignment, wrong offset | Wrong motion; limits bypassed | S3 | L2 | 6 Medium | Encoder validity checks; motor/output cross-check; calibration validity flag (SAF-REQ-022, 023) | S3 × L1 = 3 Low |
| HAZ-011 | Firmware hang | Software defect, stack overflow, ISR overrun | Last PWM state persists; uncontrolled torque | S3 | L2 | 6 Medium | Independent watchdog with gates off at reset; hardware PWM break (SAF-REQ-024, 025) | S3 × L1 = 3 Low |
| HAZ-012 | Regenerative overvoltage | Fast deceleration or a backdriven arm returns energy to a PSU that cannot sink it | Bus overvoltage; MOSFET or PSU damage | S2 | L3 | 6 Medium | Bus-voltage limiting; brake chopper or clamp; PSU with sink capability or a series diode plus capacitor/clamp (SAF-REQ-037) | S2 × L1 = 2 Low |
| HAZ-013 | Electric shock | 24 V system; mains-powered bench PSU and instruments | Shock from mains equipment (24 V itself is SELV-range) | S3 | L1 | 3 Low | Use certified bench PSUs; no open mains wiring (SAF-REQ-071) | 3 Low |
| HAZ-014 | ESD damage to electronics | Handling without ESD protection | Latent failure leading to an unexpected fault later | S2 | L3 | 6 Medium | ESD mat and wrist strap; ESD protection on external lines (SAF-REQ-072) | S2 × L1 = 2 Low |
| HAZ-015 | Incorrect calibration | Wrong pole pairs, offset or direction; calibration with the load attached | Torque in the wrong direction, runaway, or a jump | S3 | L3 | 9 High | Calibration only in the current-limited CALIBRATING sub-state; procedure; validity flag; direction checks (SAF-REQ-013, 026) | S3 × L1 = 3 Low |
| HAZ-016 | Test-fixture failure | Inadequate clamping; overload of the load arm or torque sensor | Fixture or load moves or falls | S3 | L2 | 6 Medium | Fixture design review; rated clamps; load arm sized for 25 N·m × safety factor (SAF-REQ-063, 065) | S2 × L1 = 2 Low |
| HAZ-017 | Loose fasteners | Vibration, missing thread-locker, missing torque specification | Misalignment; part separation | S2 | L3 | 6 Medium | Tightening torques, thread-locker and witness marks; post-test inspection (SAF-REQ-046) | S2 × L1 = 2 Low |
| HAZ-018 | Gearbox overload at peak torque | Peak command or impact above the gearbox rating | Tooth fracture; the joint loses holding torque | S3 | L2 | 6 Medium | Torque limit ≤ the approved peak and the gearbox rating; I²t limit; impact controls (SAF-REQ-027, 047) | S2 × L1 = 2 Low |
| HAZ-019 | Command sent to the wrong joint | Duplicate or wrong CAN node ID; wrong joint map | Unexpected motion of another joint | S3 | L2 | 6 Medium | Duplicate-ID detection; joint-map verification before enable (SAF-REQ-028) | S3 × L1 = 3 Low |
| HAZ-020 | Unsafe configuration | Limits set outside the hard stops; torque limit above the rating; timeout disabled | Protections ineffective | S3 | L2 | 6 Medium | Atomic validated configure(); safety parameters only when disabled; range checks (SAF-REQ-029) | S3 × L1 = 3 Low |
| HAZ-021 | Cable damage from joint motion | Cable crossing the rotating output; abrasion | Short circuit; signal loss | S2 | L2 | 4 Medium | Cables on the housing side only; strain relief; routing inspection (SAF-REQ-048) | S2 × L1 = 2 Low |
| HAZ-022 | Unintended command from host software | Script error; wrong units (deg vs rad); test-tool bug | Excess speed or wrong position | S3 | L3 | 9 High | Actuator-side limits independent of the host; unit conventions; dry-run in SimulatedActuator first (SAF-REQ-050, 051) | S3 × L1 = 3 Low |

Mechanical failure modes are analysed in more depth in [R6]. Project risks are in [R7]. Neither duplicates this table.

## 6. Safe states

| Safe state | Definition | Used for |
|---|---|---|
| **SS0: Power stage off (coast)** | All gate outputs off; the motor windings are floating; no motor torque. With no holding brake, the arm moves under gravity and backdrive. | Default for every FAULT and CRITICAL fault, and for the e-stop (hardware). |
| **SS1: Active damping** (optional, configurable) | Low-side MOSFETs on (phase short) or a firmware-controlled damping current. This produces braking torque proportional to speed, and no holding torque at standstill. | Selected faults where control is lost but the power stage is healthy. Only after [R1] SAF-REQ-012 approval. |
| **SS2: Controlled stop, then SS0 or hold** | Deceleration at the configured maximum to zero speed using the remaining valid feedback, then SS0 (or hold, if configured and still safe). | Thermal warning escalation, output-encoder fault with a valid motor encoder, undervoltage warning, soft-limit violation. |

Stop categories, by analogy with [R10]:

- The e-stop and immediate faults behave as **category 0**: immediate removal of power.
- The controlled stop is **category 1**: stop, then remove power.

## 7. Safety requirements

### 7.1 Motion at enable, calibration and power loss

| ID | Requirement | Hazard(s) | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| SAF-REQ-010 | Enabling shall hold the **measured position** with bumpless controller initialisation. The torque step at enable shall not exceed the configured limit. | HAZ-001 | T | Under the gravity load, the deviation at enable is ≤ 1° (TBC) over 20 trials. | `tests/safety/` | SYS-REQ-080 | A1 | M |
| SAF-REQ-011 | enable() shall be refused unless the actuator is configured, calibrated, fault-free, the e-stop is released, the bus voltage is in range and the encoders are valid. | HAZ-001, HAZ-015 | T | Each missing precondition returns its specific code ([R5] section 8.8). | `tests/safety/` | SYS-REQ-080 | A1 | M |
| SAF-REQ-012 | The safe-state option (SS0 or SS1) shall be selected per fault class, documented, and approved by the Project Lead and the independent reviewer before loaded testing. | HAZ-009 | I | Approved configuration recorded in DECISIONS.md. | `planning/v1/DECISIONS.md` | SYS-REQ-080 | A1 | M |
| SAF-REQ-013 | Calibration shall run only in the current-limited CALIBRATING sub-state (≤ 30 % rated current, TBC), with the output free or mounted on the fixture, following `docs/firmware/CALIBRATION_PROCEDURE.md`. | HAZ-015 | T, I | Calibration refused while ENABLED; current limit observed. | `tests/firmware/` | SYS-REQ-083 | A0 | M |

### 7.2 Communication, feedback and firmware integrity

| ID | Requirement | Hazard(s) | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| SAF-REQ-020 | When no valid command is received within the **command timeout** (50 ms default, TBC; configurable 10–1000 ms; cannot be disabled while ENABLED), the actuator shall enter the configured safe state within **timeout + 5 ms (TBC)**. | HAZ-002 | T | Unplugging the host cable during a velocity command gives a safe state within the limit (10 trials). | `tests/safety/` | SYS-REQ-063 | A1 | M |
| SAF-REQ-021 | CAN bus-off, or loss of the active command interface, shall be treated as communication loss. | HAZ-002 | T | Shorting CAN_H to CAN_L gives the safe state. | `tests/safety/` | SYS-REQ-063 | A1 | M |
| SAF-REQ-022 | Motor- and output-encoder faults (invalid data, magnet-field status, implausible jump) shall be detected within **3 samples** of the respective loop. Motor-encoder fault → SS0. Output-encoder fault → SS2, then SS0. | HAZ-010 | T | Disconnecting each encoder triggers the specified reaction. | `tests/safety/` | SYS-REQ-080 | A1 | M |
| SAF-REQ-023 | Output and motor positions shall be cross-checked (FIRMWARE CTRL-REQ-005). A mismatch beyond backlash plus tolerance → FAULT. | HAZ-010 | T | An injected output-encoder offset triggers `ENCODER_MISMATCH`. | `tests/safety/` | SYS-REQ-080 | A1 | M |
| SAF-REQ-024 | An **independent watchdog** shall reset the MCU within **≤ 20 ms (TBC)** of a firmware stall. Gate outputs shall default to off through reset and boot. | HAZ-011 | T | ISR-stall injection: reset observed; gates measured low throughout. | `tests/safety/` | SYS-REQ-080 | A0 | M |
| SAF-REQ-025 | Gate-driver inputs shall have **hardware pull-downs** (or a driver enable that defaults to off), so that floating MCU pins cannot switch the power stage. | HAZ-011 | I, T | Schematic review; MCU held in reset with gates measured off. | `audit/electronics/ELECTRONICS_DESIGN_AUDIT.md` | SYS-REQ-080 | A1 | M |
| SAF-REQ-026 | Calibration data shall carry a validity flag and a CRC. Invalid data shall prevent enable. | HAZ-015 | T | Corrupted calibration leads to enable refusal. | `tests/firmware/` | SYS-REQ-080 | A0 | M |
| SAF-REQ-027 | The firmware torque limit shall not be configurable above the **lower** of the approved peak rating and the gearbox manufacturer's peak rating. An I²t limit shall enforce the peak duration. | HAZ-018 | T, I | Configuration above the limit is rejected; a sustained peak is reduced after the configured time. | `tests/firmware/` | SYS-REQ-080 | A1 | M |
| SAF-REQ-028 | The host shall detect **duplicate node IDs** and verify the joint map (node ID, versions, configuration CRC) before enabling any actuator. | HAZ-019 | T | Duplicate-ID and wrong-map tests block enabling. | `tests/integration/` | SYS-REQ-063 | A2 | M |
| SAF-REQ-029 | Safety-relevant parameters (limits, timeout, safe-state option, node ID) shall be writable only while disabled, by an atomic, validated configure(). | HAZ-020 | T | A partially invalid set is rejected entirely. | `tests/firmware/` | SYS-REQ-080 | A1 | M |

### 7.3 Electrical and thermal protection

| ID | Requirement | Hazard(s) | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| SAF-REQ-030 | A **hardware overcurrent trip** (comparator → PWM break input) shall disable the gates within **< 10 µs (TBC)** of the threshold crossing, without firmware involvement. | HAZ-003 | T | Injected comparator trip: gate-off time measured with an oscilloscope. | `results/motor_control/` | SYS-REQ-080 | A0 (if the board supports it), A1 | M |
| SAF-REQ-031 | A software overcurrent check shall run at the current-loop rate (FIRMWARE fault table). | HAZ-003 | T | Injected current command above the limit triggers `OVERCURRENT_SW`. | `tests/safety/` | SYS-REQ-080 | A0 | M |
| SAF-REQ-032 | Motor and controller temperatures shall be monitored, with a warning, derating and fault thresholds derived from component datasheets (TBD). If no winding sensor is fitted, a validated thermal model shall be used. | HAZ-003, HAZ-005 | T | Continuous-torque thermal test: warning before fault; fault before any datasheet limit. | `results/thermal/` | SYS-REQ-080 | A1 | M |
| SAF-REQ-033 | The 24 V input shall be **fused** (rating TBD from the peak input current and the wiring rating) so that a power-stage short cannot overheat the wiring. | HAZ-003 | A, I | Fuse rating calculation in ELECTRONICS_DESIGN_AUDIT. | `audit/electronics/` | SYS-REQ-080 | A1 | M |
| SAF-REQ-034 | Reverse-polarity protection and keyed or polarised power connectors shall be provided. | HAZ-004 | T, I | Reverse connection on a current-limited PSU causes no damage. | `results/integration/` | SYS-REQ-041 | A1 | M |
| SAF-REQ-035 | External touchable surfaces should not exceed **60 °C (TBC)** in the continuous-torque test at the reference ambient. Otherwise they shall carry a warning label and handling instructions. | HAZ-005 | T | Thermocouple record. | `results/thermal/` | SYS-REQ-080 | A1 | H |
| SAF-REQ-036 | After any thermal or peak test, the actuator shall not be handled until its surface temperature is measured below 45 °C (TBC), or gloves are used. | HAZ-005 | I | Procedure step in the test plan. | `docs/validation/VALIDATION_PLAN.md` | SYS-REQ-083 | A1 | H |
| SAF-REQ-037 | Bus overvoltage from regeneration shall be limited to **≤ 32 V (TBC)** by firmware current limiting plus a hardware clamp or brake chopper, and/or a PSU able to sink current. The bench setup shall be documented. | HAZ-012 | T | Deceleration and backdrive tests keep the bus ≤ limit. | `results/motor_control/` | SYS-REQ-041 | A1 | M |

### 7.4 Mechanical

| ID | Requirement | Hazard(s) | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| SAF-REQ-040 | Pinch points between the output link, the housing and the hard stops shall be identified on the drawings, and guarded or marked. | HAZ-006 | I | Gate C pinch-point review record. | `audit/mechanical/MECHANICAL_RELEASE_CHECKLIST.md` | SYS-REQ-082 | A1 | M |
| SAF-REQ-041 | Mechanical hard stops shall be designed to absorb the full kinetic energy at maximum speed (≈ 1.9 J at 45 RPM with J = 0.171 kg·m², to be recalculated with CAD inertia) without damage to the gearbox. The stop torque shall stay within the gearbox peak rating, using compliant bumpers if needed. | HAZ-007, HAZ-018 | A, T | Calculation in `mechanical/calculations/`; impact test at reduced speed then full speed on the fixture; no damage. | `results/mechanical/` | SYS-REQ-035, SYS-REQ-082 | A1 | M |
| SAF-REQ-042 | Soft limits shall be inside the hard stops (≥ 5° margin, TBC), with velocity ramp-down near the limits (FIRMWARE CTRL-REQ-031/032). | HAZ-007 | T | Maximum-speed approach stops before the hard stop. | `results/mechanical/` | SYS-REQ-082 | A1 | M |
| SAF-REQ-043 | Load-bearing parts (shaft, bearing seats, gearbox and motor mounts, output flange, hard stops) shall be made of metal or another material justified by a reviewed calculation. 3D-printed parts shall not be in the primary load path unless analysis and test justify it. | HAZ-008 | A, I | Gate A material review. | `audit/mechanical/MECHANICAL_DESIGN_AUDIT.md` | SYS-REQ-038 | A1 | M |
| SAF-REQ-044 | Shaft, bearing and housing calculations shall be independently reviewed before the first loaded test (Gate A). | HAZ-008 | I | Audit record with reviewer ≠ author. | `audit/mechanical/` | SYS-REQ-106 | A1 | M |
| SAF-REQ-045 | Without a holding brake, the arm will fall on power loss. The fixture shall provide a **mechanical rest or catch** at the low position, and nobody shall place any body part beneath the load. | HAZ-009 | I | Fixture inspection. | `results/mechanical/` | SYS-REQ-083 | A1 | M |
| SAF-REQ-046 | Fasteners shall have defined tightening torques and thread-locking. Witness marks shall be applied and inspected after loaded tests. | HAZ-017 | I | Inspection record after each loaded campaign. | `results/mechanical/` | SYS-REQ-092 | A1 | M |
| SAF-REQ-047 | Impact events (hard-stop contact, tracking-error trips) shall be counted, and the gearbox shall be inspected after a defined number of impacts (TBD). | HAZ-018 | I | Inspection log. | `results/mechanical/` | SYS-REQ-091 | A1 | H |
| SAF-REQ-048 | No cable shall cross the rotating output. Cables shall be strain-relieved on the housing side. | HAZ-021 | I | Routing inspection. | `audit/mechanical/MECHANICAL_RELEASE_CHECKLIST.md` | SYS-REQ-082 | A1 | M |

### 7.5 Host and test software

| ID | Requirement | Hazard(s) | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| SAF-REQ-050 | Actuator-side limits shall apply regardless of the host software. Host-side limits are an additional layer, not a replacement. | HAZ-022 | T | A command beyond the limit from a raw CAN tool is clamped or rejected by the actuator. | `tests/firmware/` | SYS-REQ-051 | A1 | M |
| SAF-REQ-051 | New motion scripts shall first be run against **SimulatedActuator**, then on the fixture at reduced limits, before they are used at full limits. | HAZ-022 | I | Test-plan step and log. | `docs/validation/VALIDATION_PLAN.md` | SYS-REQ-083 | A2 | H |

### 7.6 Emergency stop

| ID | Requirement | Hazard(s) | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| SAF-REQ-055 | Every powered test setup shall have a **latching, red/yellow emergency-stop** device within reach of the operator. It shall remove motor power through a **hardware path** independent of firmware: it de-asserts the gate-driver enable (STO-like) and/or opens a contactor or relay in the 24 V motor supply. | HAZ-001, 002, 003, 006 | T, I | E-stop pressed during motion: power stage disabled within **≤ 10 ms (TBC)**; verified with firmware deliberately not reacting (test build). | `tests/safety/` | SYS-REQ-081 | A0 (bench), A1 (actuator input) | M |
| SAF-REQ-056 | Releasing the e-stop shall **not** restart motion. Recovery requires an explicit acknowledgement, after which the actuator enters DISABLED, then an explicit enable(). | HAZ-001 | T | Release with no acknowledgement leaves no motion. | `tests/safety/` | SYS-REQ-081 | A1 | M |
| SAF-REQ-057 | The e-stop state shall be reported to firmware and host (`ESTOP_ACTIVE`). A wire break in the e-stop circuit shall be treated as e-stop asserted (fail-safe wiring). | HAZ-002 | T | Disconnecting the e-stop cable asserts e-stop. | `tests/safety/` | SYS-REQ-081 | A1 | M |
| SAF-REQ-058 | In A0, if the development board has no hardware enable input, the bench e-stop shall open the 24 V supply to the board's power stage through a rated relay or contactor (DC-rated for the PSU current). | HAZ-003 | I, T | Bench wiring inspection; test. | `results/motor_control/` | SYS-REQ-081 | A0 | M |

### 7.7 Test conduct and laboratory

| ID | Requirement | Hazard(s) | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| SAF-REQ-060 | A **clear zone** (≥ arm reach + 0.5 m, TBC) shall be marked around the fixture. Nobody shall be inside the zone while the actuator is enabled. | HAZ-001, 006 | I | Lab layout photo in the test record. | `results/` | SYS-REQ-083 | A1 | M |
| SAF-REQ-061 | **No manual resistance.** The actuator shall never be resisted by hand, held while energised under load, or attached to a person. | HAZ-006 | I | Briefing record signed by each operator. | `planning/v1/tasks/` | SYS-REQ-083 | A0–A2 | M |
| SAF-REQ-062 | Safety glasses shall be worn during loaded, peak and impact tests. A transparent guard shall surround the moving link for peak and impact tests. | HAZ-007, 008 | I | Test-record checklist. | `results/` | SYS-REQ-083 | A1 | M |
| SAF-REQ-063 | Load shall be increased in **stages**: no load → 25 % → 50 % → 100 % of continuous → peak. Each stage needs a pass of the previous stage and an inspection. | HAZ-008, 016 | I | Test plan and records show the staged sequence. | `docs/validation/VALIDATION_PLAN.md` | SYS-REQ-084 | A1 | M |
| SAF-REQ-064 | Loaded tests (≥ 50 % of continuous torque) and all peak and impact tests shall be performed with **two people present** (TBC): an operator at the e-stop and an observer. | HAZ-009, 016 | I | Test record lists both names. | `results/` | SYS-REQ-083 | A1 | H |
| SAF-REQ-065 | The test fixture (frame, clamps, load arm, torque sensor) shall be rated for ≥ 2 × the peak test torque (25 N·m → 50 N·m design, TBC), and reviewed before first use. | HAZ-016 | A, I | Fixture review record. | `docs/validation/TEST_EQUIPMENT.md` | SYS-REQ-083 | A1 | M |
| SAF-REQ-066 | Bring-up shall start on a **current-limited bench PSU**, with the limit set to the lowest value that allows the test step. The limit shall only be raised after protections are verified. | HAZ-003 | I | Test-record field "PSU current limit". | `results/motor_control/` | SYS-REQ-045, SYS-REQ-084 | A0 | M |
| SAF-REQ-070 | The bench surface shall be non-flammable. A CO₂ or dry-powder extinguisher rated for electrical fires shall be available in the lab. | HAZ-003 | I | Lab inspection. | `docs/validation/TEST_EQUIPMENT.md` | SYS-REQ-083 | A0 | M |
| SAF-REQ-071 | Only certified mains equipment (bench PSU, oscilloscope) shall be used. There shall be no open mains wiring. When probing ground-referenced nodes in the power stage, isolated or differential probes shall be used. | HAZ-013 | I | Equipment list. | `docs/validation/TEST_EQUIPMENT.md` | SYS-REQ-083 | A0 | M |
| SAF-REQ-072 | ESD-safe handling (mat, wrist strap) shall be used for PCB work. | HAZ-014 | I | Lab inspection. | `docs/validation/TEST_EQUIPMENT.md` | SYS-REQ-083 | A0 | H |

### 7.8 Review and deployment

| ID | Requirement | Hazard(s) | Verif. | Acceptance criterion | Evidence location | Parent | Phase | Prio |
|---|---|---|---|---|---|---|---|---|
| SAF-REQ-080 | All SAF-REQ items shall be verified, with evidence, before Gate C. Items without qualified independent review shall be recorded as `NOT_VERIFIED`, and Gate C shall stay blocked. | All | I | `audit/release/RELEASE_AUDIT.md` safety section complete. | `audit/release/` | SYS-REQ-106 | A1 | M |
| SAF-REQ-081 | Human-interactive testing is **prohibited** until a qualified human reviewer has approved the mechanical and electrical safety evidence, and the approval is recorded in DECISIONS.md. | All | I | Approval record. | `planning/v1/DECISIONS.md` | SYS-REQ-083 | A2 | M |
| SAF-REQ-082 | Deployment on the humanoid robot shall require a separate system-level safety review covering robot-level hazards (falls, multiple joints, collisions). Passing the A2 software exit gate does not establish this. | All | I | Separate review document (future). | `audit/release/` | SYS-REQ-085 | A2 | M |
| SAF-REQ-083 | Any safety-critical defect found at a gate shall be classed as blocking. It shall not be downgraded to "pass with actions" to meet a schedule. | All | I | Audit finding records. | `audit/` | SYS-REQ-106 | A0–A2 | M |

## 8. Fault-injection verification list

The tests are executed per `docs/validation/VALIDATION_PLAN.md`. Each test is run with the actuator on the fixture, at reduced limits first, and recorded per SYS-REQ-103.

| # | Inject | Method | Expected reaction | Pass criterion | Requirements |
|---|---|---|---|---|---|
| FI-01 | Hardware overcurrent | Lower the comparator threshold, or pulse the test input | PWM off in hardware; `OVERCURRENT_HW`; FAULT | Gate-off < 10 µs (TBC) | SAF-REQ-030 |
| FI-02 | Software overcurrent | Command above the limit with a lowered software threshold | `OVERCURRENT_SW`; SS0 | Within 3 current-loop samples | SAF-REQ-031 |
| FI-03 | Gate-driver fault | Force the nFAULT pin | `GATE_DRIVER_FAULT`; SS0 | Immediate | CTRL-REQ-003 |
| FI-04 | Overvoltage | Raise the PSU to the threshold (no load) or regen test | Warning, then fault at the threshold | Bus never exceeds the limit | SAF-REQ-037 |
| FI-05 | Undervoltage | Lower the PSU during motion | Warning, controlled stop, fault | No uncontrolled motion | Firmware fault table |
| FI-06 | Motor overtemperature | Heat the sensor, or offset the thermal-model input | Warning → derate → fault | Order and thresholds as configured | SAF-REQ-032 |
| FI-07 | Temperature-sensor open or short | Disconnect or short the NTC | `TEMP_SENSOR_FAULT` | Detected within 100 ms | SAF-REQ-032 |
| FI-08 | Motor-encoder loss | Disconnect the motor encoder during motion | `ENCODER_MOTOR_FAULT`; SS0 | Within 3 samples | SAF-REQ-022 |
| FI-09 | Output-encoder loss | Disconnect the output encoder | `ENCODER_OUTPUT_FAULT`; SS2 → SS0 | Controlled stop, then off | SAF-REQ-022 |
| FI-10 | Encoder mismatch | Inject an output offset in a test build | `ENCODER_MISMATCH` | Detected | SAF-REQ-023 |
| FI-11 | Communication loss | Unplug USB or CAN during a velocity command | `COMM_TIMEOUT`; safe state | Within timeout + 5 ms | SAF-REQ-020 |
| FI-12 | CAN bus-off | Short CAN_H to CAN_L | `CAN_BUS_OFF`; safe state | Within timeout | SAF-REQ-021 |
| FI-13 | Firmware stall | Debug command entering an infinite loop in the ISR (test build) | Watchdog reset; gates off; `WATCHDOG_RESET` reported | Reset ≤ 20 ms; gates low | SAF-REQ-024 |
| FI-14 | E-stop | Press during motion; also with firmware reaction disabled (test build) | Power removed by hardware | ≤ 10 ms | SAF-REQ-055 |
| FI-15 | E-stop wire break | Disconnect the e-stop loop | E-stop asserted | Immediate | SAF-REQ-057 |
| FI-16 | E-stop release | Release with no acknowledgement | No motion | No motion | SAF-REQ-056 |
| FI-17 | Tracking error | Block the output with the fixture brake | `TRACKING_ERROR`; safe state | Within the configured time | CTRL-REQ-034 |
| FI-18 | Soft-limit approach at maximum speed | Command a position beyond the soft limit at v_max | Stops inside the limit | No hard-stop contact | SAF-REQ-042 |
| FI-19 | Invalid configuration | Soft limit outside the hard stop; torque above the rating | `E_CONFIG_REJECTED`; previous set kept | Rejected | SAF-REQ-029, 027 |
| FI-20 | Invalid and malformed commands | Fuzzed frames; out-of-range values | Rejected, counted, no motion | No crash | FW-REQ-053 |
| FI-21 | Duplicate node ID | Two nodes with the same ID | Host refuses to enable | Refused | SAF-REQ-028 |
| FI-22 | Enable under gravity load | Enable at the horizontal pose | Holds the measured position | ≤ 1° deviation | SAF-REQ-010 |
| FI-23 | Power loss during motion | Switch off the PSU | Coast or damping as configured; the arm lands on the fixture rest | No damage | SAF-REQ-045, 012 |
| FI-24 | Hard-stop impact | Firmware limits relaxed in a test build; reduced speed, then full speed | Stop absorbs the energy | No damage; inspection pass | SAF-REQ-041 |

## 9. Safety review and sign-off (Gate C)

1. **Preparation.** The Mechanical and Electronics Interns compile the evidence for every SAF-REQ: calculations, schematics, test records and the fault-injection results.
2. **Independent review.** The Independent Mechanical Reviewer and the Independent Electrical/Firmware Reviewer review the evidence. They record findings with severity (CRITICAL / HIGH / MEDIUM / LOW / OBSERVATION) in the relevant `audit/` documents.
3. **Disposition.** Every finding is closed with evidence, or accepted with a recorded rationale. CRITICAL and HIGH findings must be closed. Safety-critical defects cannot be deferred (SAF-REQ-083).
4. **Sign-off.** The Project Lead signs Gate C in `audit/release/RELEASE_AUDIT.md` only when every SAF-REQ is `PASS` or `PASS_WITH_ACTIONS` (non-safety actions only), and no item is `NOT_VERIFIED`.
5. **Scope statement.** The sign-off states that it covers **bench operation on a restrained fixture** only.

## 10. Allocation check against the parent

| SYS-REQ | Covered by |
|---|---|
| SYS-REQ-080 | SAF-REQ-010 to 012, 022 to 027, 029 to 033 |
| SYS-REQ-081 | SAF-REQ-055 to 058 |
| SYS-REQ-082 | SAF-REQ-040 to 042, 048 |
| SYS-REQ-083 | SAF-REQ-013, 036, 045, 051, 060 to 072, 081 |
| SYS-REQ-084 | SAF-REQ-063, 066 |
| SYS-REQ-085 | SAF-REQ-082 |
| SYS-REQ-063 | SAF-REQ-020, 021, 028 |

## 11. Open items

| # | Item | Requirement | Owner | Needed by |
|---|---|---|---|---|
| 1 | Reaction-time targets (overcurrent, e-stop, timeout) confirmed against the selected hardware | SAF-REQ-020, 030, 055 | Electronics/Embedded Intern | E2 / F1 |
| 2 | Safe-state option per fault class (SS0 vs SS1) | SAF-REQ-012 | Project Lead + reviewer | Before loaded tests |
| 3 | Hard-stop design energy recalculated with CAD inertia | SAF-REQ-041 | Mechanical Intern | Gate A |
| 4 | Two-person rule threshold confirmation | SAF-REQ-064 | Project Lead | Before loaded tests |
| 5 | Fixture rating and design | SAF-REQ-065 | Mechanical Intern | Before Gate B |
| 6 | Qualified independent human reviewers named | SAF-REQ-080 | Project Lead | Gate A |
| 7 | Regeneration handling on the bench PSU | SAF-REQ-037 | Electronics/Embedded Intern | A0 bring-up |

## 12. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-11 | Kritvaos Actuator Team | Initial draft |
