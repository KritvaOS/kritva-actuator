# Kritva Actuator: Components, Sourcing, Draft Pricing and Phased Localisation

| Field | Value |
|---|---|
| Document ID | KA-DOC-ARCH-SOURCING |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-14 |
| Document owner | Project Lead |
| Reviewer / Approver | Project Lead; Independent Mechanical Reviewer for the mechanical rows |
| Applies to | A0, A1, A2 |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** This is a **draft consolidation, not a purchase plan or an approved budget.** Prices are of three kinds, marked in every row: **L** = a listing price read from a supplier web page on 2026-10-13 (not a quotation); **E** = an estimate carried from `mechanical/bom/MECHANICAL_BOM.csv` or `hardware/bom/ELECTRICAL_BOM.csv`; **TBD** = no price known, and none is assumed. Sources named without an **L** are candidate suppliers that have **not** been checked. No quotation, shipping, duty or lead time has been obtained. Drivetrain data from the ChatGPT reviewer session are unverified (see `mechanical/calculations/MOTOR_GEARBOX_SHORTLIST.md`).

---

## 1. Scope this document follows

**In scope (first prototype).** One low-voltage rotary actuator prototype; commercial BLDC/PMSM motor; off-the-shelf planetary gearbox for the initial design, subject to requirements review; output-shaft encoder; commercial motor-control development board for initial bring-up; FOC implemented or adapted from a suitable established codebase; closed-loop position control (velocity and torque control only where supported and validated); mechanical CAD, fabrication, assembly and characterisation; basic host communication, with CAN as the target for the smart-actuator stage; fault handling, test evidence and engineering documentation; a custom controller PCB only after the initial motor-control system is validated.

**Out of scope for the first prototype.** Designing and manufacturing a motor from raw materials; manufacturing a precision harmonic-drive gearbox; a production-ready or safety-certified actuator; operating the prototype on a loaded humanoid robot; claiming reliable collision detection from motor current alone; guaranteeing that prototype cost equals eventual production cost.

## 2. Component breakdown, sourcing and phase

Source types: **BUY** = bought as a part; **BUILD** = our design and work; **OUTSOURCE** = our design, made by a supplier.

### 2.1 Mechanical

| ID | Component | Type | External source (candidate) | Price status | Phase |
|---|---|---|---|---|---|
| MB-001 | BLDC/PMSM motor | BUY | CubeMars (store.cubemars.com, India resellers such as Robokits); Robokits Rhino range | L: RI50 ₹8,245, RI60 ₹12,208, RI70 ₹14,885, RI80 ₹19,327 (Robokits); US$61.90 to 132.90 (CubeMars store, ex shipping). BOM estimate ₹4,000 is **too low** | A0 |
| MB-002 | Planetary gearbox | BUY | Neugart, WITTENSTEIN (quotation); NEMA-flange gearheads (not checked) | TBD (no online price found). BOM estimate ₹4,000 is **unverified** | A0 |
| (alt.) | Integrated geared BLDC drivetrain (motor + gearbox in one unit) | BUY | Robokits RMCS-2071 (96:1, 30 RPM, 100 W) | L: ₹7,058 excl. GST, about ₹8,328 incl. 18 % GST (page title shows ₹5,767: confirm) | A0/A1 (alternative to MB-001 + MB-002) |
| MB-003 | Output shaft, 12 mm | OUTSOURCE | Bar stock from an industrial supplier, machined by a local workshop | TBD | A1 |
| MB-004 | Output bearings, 6202-2RS, 2 pcs (candidate baseline, not released) | BUY | Industrial bearing distributors | TBD | A1 |
| MB-005/006 | Housing and motor/gearbox mounting plate, Al 6061-T6 | OUTSOURCE (design: BUILD) | Local CNC machine shop | TBD | A1 (A0 uses simple fixture parts) |
| MB-007 | Coupling gearbox to output shaft | BUY | Standard couplings (Oldham, jaw or bellows) | TBD | A1 |
| MB-008 | Output flange | OUTSOURCE | Local machine shop | TBD | A1 |
| MB-009/010 | Hard-stop pins and lugs; polyurethane bumpers | OUTSOURCE / BUY | Machine shop; bumper stock | TBD | A1 |
| MB-011 | Encoder magnet holder and bracket | BUILD (printed or machined) | In-house or local print/machining | TBD | A1 |
| MB-012/013 | Fasteners, dowels, shims, wave spring | BUY | Fastener distributors | TBD | A1 |
| MB-014 | Fabrication allowance for A0 fixture parts | BUILD / OUTSOURCE | In-house printing, simple machining | E: ₹3,000 | A0 |
| MB-015 | Restrained test fixture | BUILD | Local fabrication | TBD | A1 |

### 2.2 Electronics and sensing

| ID | Component | Type | External source (candidate) | Price status | Phase |
|---|---|---|---|---|---|
| EB-001 | Motor-control development board | BUY | STMicroelectronics (B-G431B-ESC1, NUCLEO-G474RE with a motor-control shield) or an ODrive-class board; Indian electronics distributors | E: ₹5,000 | A0 |
| EB-002 | Output-side magnetic encoder IC or board plus magnet | BUY | ams OSRAM AS5047P-class boards (candidate) | E: ₹1,500 | A0 |
| EB-003 | PSU wiring, fuse, DC-rated e-stop relay and button | BUY | Electronics distributors | E: ₹2,500 | A0 |
| EB-004 | Cables, terminals, heat-shrink, USB cable | BUY | Electronics distributors | E: ₹2,000 | A0 |
| EB-005 to EB-013 | Custom controller: MCU, gate driver, MOSFETs, current sense, protection, regulators, CAN transceiver, thermistors, connectors | BUY (components) | Electronics distributors | TBD | A1, only after the A0 system is validated |
| EB-014 | Custom controller PCB, fabrication and assembly | OUTSOURCE (design: BUILD) | PCB fabrication and assembly house | TBD | A1 |
| EB-015 | USB-CAN adapter for the host PC | BUY | Electronics distributors | TBD | A1 |
| EB-016 | Stationary output-encoder PCB | BUILD (design) / OUTSOURCE (fab) | PCB house | TBD | A1 |

### 2.3 Firmware, software and documentation (no purchase cost, effort only)

| Item | Type | Note | Phase |
|---|---|---|---|
| FOC and current-loop firmware | BUILD / ADAPT | Adapt an **established, suitably licensed** FOC codebase (selection in ACT-01-002; the licence must be checked against ACT-DEC-012 before any code is copied) | A0 to A1 |
| Closed-loop position control | BUILD | Velocity and torque control only where supported and validated | A0 to A1 |
| Fault handling and diagnostics | BUILD | ACT-01-004 | A0 to A1 |
| CAN firmware and protocol | BUILD | ACT-01-006, ACT-03-002 | A1 |
| Actuator interface, KritvaOS driver, host tools, simulation | BUILD | ACT-03-001 to ACT-03-004 | A1 to A2 |
| CAD, drawings, calculations, test procedures, evidence, audits | BUILD | Mechanical and Electronics interns, reviewers | A0 to A2 |
| Laboratory equipment (bench PSU, scope, torque/load instruments) | BUY or borrow | Excluded from the budget bands | A0 |

## 3. Draft pricing structure

### 3.1 Structure

The BOM is priced in three layers so that estimates are never mistaken for quotes:

1. **Line price status:** `ESTIMATE` (E), `QUOTED`, `PURCHASED`, or `TBD`, as in the BOM files.
2. **Landed cost per line** (to be recorded when known): unit price, shipping, import duty (for foreign purchases), GST (18 % applies to the Robokits listing; confirm per item), minus GST input credit where the organisation can claim it.
3. **Cumulative cost per milestone** against the provisional bands: A0 ₹10,000 to 15,000; A1 ₹20,000 to 30,000 cumulative. The bands are not supplier-verified (SYS-REQ-100).

### 3.2 A0 total from the BOM as written

| Item | ₹ | Status |
|---|---|---|
| MB-001 motor | 4,000 | E |
| MB-002 gearbox | 4,000 | E |
| EB-001 development board | 5,000 | E |
| EB-002 encoder | 1,500 | E |
| EB-003 e-stop and wiring | 2,500 | E |
| EB-004 cables and misc | 2,000 | E |
| MB-014 fabrication allowance | 3,000 | E |
| **Total** | **22,000** | all E; **above the A0 band** |

### 3.3 A0 total if the motor estimate is replaced with listed prices

The motor estimate (₹4,000) is lower than every listed price for the candidate motors. Replacing it, with all other lines unchanged:

| Drivetrain scenario | Motor and gearbox lines replaced by | A0 total (₹) | Position vs ₹10,000 to 15,000 |
|---|---|---|---|
| S1 RI70 + gearbox (estimate ₹4,000 unchanged) | 14,885 (L) + 4,000 (E) | 32,885 | Well above |
| S2 RI60 + gearbox (estimate unchanged) | 12,208 (L) + 4,000 (E) | 30,208 | Well above |
| S3 RI50 + gearbox (estimate unchanged) | 8,245 (L) + 4,000 (E) | 26,245 | Above |
| S4 integrated RMCS-2071 (replaces both lines) | 8,328 (L, incl. GST) | 22,328 | Above |

The gearbox line is still an estimate in S1 to S3 and could be higher; no industrial gearbox price is known. Totals mix listings with estimates and are **indicative only**.

### 3.4 Reading the result

No scenario fits the A0 band as the BOM stands. The levers, in order of effect, are: the drivetrain (this section); deferring the housing, shaft and fixture to A1; a smaller torque target (a decision on ACT-DEC-008); and re-estimating the development board and wiring lines against real prices.

## 4. What can be developed locally, in phases

| Phase | Locally developed (BUILD) | Still bought | Gate |
|---|---|---|---|
| **A0** educational motor control | FOC adaptation, current sensing checks, encoder driver, position loop, host UART, bring-up procedures, test fixture parts (printed or simple machined) | Development board, motor, gearbox, encoder, PSU, wiring | E1, A0 exit criteria |
| **A1** smart actuator | Housing, mounting plate, output shaft design, bearing seats, hard stops, encoder mount, custom controller PCB (after A0 is validated), CAN firmware, test fixture, characterisation | Motor, gearbox, bearings, encoder IC and magnet, PCB components | M1 to M4, E2 to E4, F1 to F4 |
| **A2** integration | KritvaOS driver, Edge/Nexus integration, diagnostics, simulation model | Host PC, USB-CAN adapter | Gate C |
| **Later, optional (outside the first prototype)** | Research on a low-cost in-house gearbox (printed or machined planetary or cycloidal stage) as a replacement for the bought gearbox; local second source for the housing, shaft and PCB assembly | Bearings, fasteners | New decision (would change ACT-DEC-002/003) |
| **Not planned** | Motor from raw materials; precision harmonic-drive gearbox | | Out of scope |

Localisation order of preference, lowest risk first: encoder bracket and fixture parts; housing, plate, flange and shaft machining (local workshop); custom controller PCB and its assembly; coupling; and only later, an in-house gearbox.

## 5. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | Obtain gearbox quotations (Neugart or other) and a drivetrain price for each scenario | Mechanical Intern | M1 |
| 2 | Re-price the BOM: motor, gearbox, development board, wiring | Both interns | M1 |
| 3 | Choose the drivetrain scenario and the torque target (ACT-DEC-008 / new decision) | Project Lead | Before purchase |
| 4 | Confirm GST treatment, shipping and import duty for each supplier | Project Lead | Before purchase |
| 5 | Identify local workshops for machining and PCB assembly; get quotes | Mechanical Intern, Electronics/Embedded Intern | A1 |
| 6 | Select the established FOC codebase and check its licence (ACT-01-002) | Electronics/Embedded Intern | A0 |
| 7 | Verify the candidate sources named without an L | Both interns | M1 |

## 6. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-14 | Kritvaos Actuator Team | Initial consolidation: components, sources, draft pricing structure and phased localisation, based on the stated scope |
