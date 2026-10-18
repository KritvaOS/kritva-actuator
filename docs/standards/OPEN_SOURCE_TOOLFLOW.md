# Kritva Actuator: Open-Source Tool Flow (Mechanical, Electronics, Embedded)

| Field | Value |
|---|---|
| Document ID | KA-STD-TOOLFLOW |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 |
| Date | 2026-10-18 |
| Document owner | Project Lead / Integration Owner |
| Reviewer / Approver | Project Lead |
| Applies to | A0, A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** Proposed standard, not approved. No decision number is assigned: the owner records the toolchain freeze in `planning/v1/DECISIONS.md`. The flow was drafted in a review with an external planning discussion (ChatGPT, 2026-10-18) and then checked here: each repository and link in section 6 was opened and its description and licence read on 2026-10-18. Items not verified are marked. Versions are not chosen here. Tool outputs, exports, simulations and CI passes are evidence inputs only; none closes Gate A, B or C or replaces independent review (ACT-DEC-014) or restrained-fixture testing (ACT-DEC-015).

---

## 1. Principles

1. A small, reproducible toolchain beats many overlapping tools. Kritva-M (the reference) is made reproducible first; S and L reuse the approved interfaces and method but keep their own sizing, CAD, BOM and verification evidence.
2. The existing flow stays: Python sizing engine, `make check` (docs, links, traceability, BOM, calculations, manifest, submodules, status), GitHub Actions. New checks are added as owner-approved `make` targets, not by replacing existing ones.
3. Interfaces, units, CAN protocol and shared limits stay in the parent (`docs/interfaces/`, `requirements/`).
4. Each release records the source commit, tool versions, component revisions and checksums of generated files. The parent pins reviewed child SHAs.
5. Generated designs, manufacturing data and test logs stay private. Do not publish them as public CI artifacts, and do not commit third-party datasheets without checking redistribution rights.

## 2. Mechanical flow

```text
Approved requirements and limits (requirements/)
  -> Python sizing engine + check_calcs   (mechanical/common-sizing, calculations/)
  -> Parametric CAD of Kritva-M           (FreeCAD)
  -> Shaft, bearing, gearbox calculations (existing documents; vendor ratings checked)
  -> Design review and Gate A
  -> Drawings, assembly definition, BOM
  -> Fabrication, inspection, restrained-fixture tests
  -> Independent review, Gates B/C
  -> Variant baseline; S and L reuse
```

| Stage | Tool | Artefact | CI check (proposed) |
|---|---|---|---|
| Sizing | Existing Python engine, `check_calcs` | Torque, speed, loads, variant results | Existing `make check`; golden-case regression; input and unit validation |
| CAD | FreeCAD (freeze) | Native model, STEP, STL, drawing PDFs | Export exists and is non-empty; geometry check (valid solids, bounding box, volume ranges) on changed files |
| Scripted geometry | CadQuery (optional) | Python CAD source, STEP | Only for fixtures and repeated features; never a second master of a load-bearing part |
| Simple jigs | OpenSCAD (optional) | `.scad`, STL | Non-load-bearing parts only |
| FEA | FreeCAD FEM with CalculiX (optional) | Mesh, loads, results report | Input, solver run and a small benchmark only; full FEA is not a per-commit check |
| BOM | Existing `check_bom` and BOM CSV | `MECHANICAL_BOM.csv` | Required columns, unique IDs, part number, manufacturer, revision |
| Large files | Git LFS where justified | Versioned binaries | Git LFS not verified in this review; decide at freeze |

Rules: compare STEP files by geometry with tolerances, not byte hashes. A released STEP or drawing is tied to one child commit and is never silently regenerated. A finished FEA solve does not show that the load case, constraints, mesh and convergence are right. A Python calculation does not replace checking that the selected gearbox supports the operating point.

## 3. Electronics flow (custom controller PCB)

| Stage | Tool | Artefact | CI check (proposed) |
|---|---|---|---|
| Schematic and layout | KiCad (freeze version and libraries) | `.kicad_sch`, `.kicad_pcb` | Schematic ERC and PCB DRC through `kicad-cli`; no unwaived errors |
| Libraries | KiCad libraries, project symbols and footprints | Approved parts with MPN metadata | Symbols resolve to footprints; metadata complete |
| BOM | `kicad-cli` and existing BOM scripts | `ELECTRICAL_BOM.csv` | Required fields, duplicates, quantities, sourcing |
| Fabrication outputs | `kicad-cli` | Gerbers, drill, outline | Expected layers present, non-empty, from the same PCB commit |
| Automation (optional) | KiBot | Same outputs from a config | Alternative to hand-written scripts; AGPL-3.0, so use as an external tool only |

Confirm `kicad-cli` options against the frozen KiCad release before freezing scripts. ERC and DRC do not show electrical or thermal safety. Review still covers phase-current and bus ratings, gate-driver and MOSFET choice, current-sense chain, ADC and PWM timing, regeneration, thermal paths, clearances, connector pinouts, and fault paths. Gerbers and BOM are manufacturing outputs, not design acceptance.

## 4. Embedded flow

One shared firmware for S, M and L, with a variant configuration (motor parameters, gear ratio, encoder, limits). No forks.

| Stage | Tool | Notes |
|---|---|---|
| Compiler | Arm GNU toolchain (`arm-none-eabi-gcc`) | Freeze release, binutils and runtime libraries |
| Build | CMake with an explicit toolchain file | One official release build path |
| Peripheral layer | STM32CubeG4 HAL/LL and CMSIS (candidate) | Pin the release and record components used; licences differ by component |
| Alternatives (optional) | libopencm3 (LGPL), Zephyr, PlatformIO | Adopt only by decision; avoid a second, separately configured build |
| Host unit tests | Unity (C), GoogleTest (C++, if needed), pytest (Python) | Test FOC mathematics, encoder rollover and invalid readings, state machine, CAN encode/decode, variant configuration, fault recognition |
| CAN tools | python-can, cantools (DBC), SavvyCAN, can-utils | Protocol and message tests without hardware; bench capture and decode |
| Logging and plots | pandas, Matplotlib; PlotJuggler (optional) | Evidence from bench runs |
| Simulation (optional) | Renode, MuJoCo, Python joint model | Only where a defined use exists; Renode may not model the power stage or motor |

Each release emits the ELF and binary or HEX image, linker map, build log, configuration manifest and checksums. CI matrix: host tests, compile, configuration validation and protocol tests for M, S and L. A compile does not show that motor, current sensing, PWM timing, gearbox and encoder work together. Bench or hardware-in-loop tests need a guarded, restrained, instrumented fixture and a test-readiness record. Hosted CI never starts a loaded motor test after an ordinary merge. A log processor may report a pass against a predeclared criterion; it never closes a gate.

### FOC reference designs and code reuse

| Project | Licence | Use |
|---|---|---|
| SimpleFOC | MIT | Learning and concept reference |
| moteus | Apache-2.0 | Controller architecture, diagnostics and host-tool reference |
| ODrive (legacy v3.x firmware) | MIT | Historical reference; not a default dependency |
| VESC firmware | GPL-3.0 | Study only. Do not copy code into proprietary firmware without an explicit licence decision |

Before reusing any source, record the component, licence, version or commit, modified files and required notices. A reference implementation is not validated for Kritva hardware.

## 5. Licence policy

Using an open-source application to make a design does not by itself put the CAD, PCB or firmware under that application's licence. Incorporating or linking library source into distributed firmware is a different question. Apache-2.0, MIT and BSD components are generally straightforward (keep notices). LGPL needs a linking and relink review. GPL code must not enter proprietary firmware without a decision. Packages such as STM32CubeG4 carry component-by-component licences, so read `LICENSE.md` for what is actually used. Keep a third-party licence inventory with the toolchain freeze. This is an engineering summary, not legal advice; the owner may want a legal check before distribution.

## 6. References

Opened and read on 2026-10-18 unless marked. Licence as shown on the project page.

### Source repositories

| Tool | Repository | Licence |
|---|---|---|
| FreeCAD | https://github.com/FreeCAD/FreeCAD | LGPL-2.1 |
| CadQuery | https://github.com/CadQuery/cadquery | Apache-2.0 |
| OpenSCAD | https://github.com/openscad/openscad | Not confirmed on the page; see `COPYING` |
| CalculiX | http://www.calculix.de/ (official site) | GPL-2.0 or later (copyright notice) |
| KiCad | https://gitlab.com/kicad/code/kicad (development); https://github.com/KiCad/kicad-source-mirror (mirror) | GPL-3.0 or later; some components under other licences |
| KiBot | https://github.com/INTI-CMNB/KiBot | AGPL-3.0 |
| CMake | https://github.com/Kitware/CMake | BSD-3-Clause |
| CMSIS 6 | https://github.com/ARM-software/CMSIS_6 | Apache-2.0 |
| STM32CubeG4 | https://github.com/STMicroelectronics/STM32CubeG4 | Per component; see `LICENSE.md` |
| libopencm3 | https://github.com/libopencm3/libopencm3 | LGPL-3.0 or later |
| Zephyr | https://github.com/zephyrproject-rtos/zephyr | Apache-2.0 |
| Unity | https://github.com/ThrowTheSwitch/Unity | MIT |
| GoogleTest | https://github.com/google/googletest | BSD-3-Clause |
| SimpleFOC | https://github.com/simplefoc/Arduino-FOC | MIT |
| moteus | https://github.com/mjbots/moteus | Apache-2.0 |
| ODrive | https://github.com/odriverobotics/ODrive | MIT (legacy firmware; newer firmware not public) |
| VESC firmware | https://github.com/vedderb/bldc | GPL-3.0 |
| python-can | https://github.com/hardbyte/python-can | LGPL-3.0 |
| cantools | https://github.com/cantools/cantools | MIT |
| SavvyCAN | https://github.com/collin80/SavvyCAN | MIT |
| can-utils | https://github.com/linux-can/can-utils | Per utility; see `LICENSES` |
| Renode | https://github.com/renode/renode | MIT |
| MuJoCo | https://github.com/google-deepmind/mujoco | Apache-2.0 (documentation CC BY 4.0) |
| PlotJuggler | https://github.com/facontidavide/PlotJuggler | MPL-2.0 |

Not independently opened in this review (named in the external discussion; confirm before relying on them): Arm GNU toolchain / `gcc-mirror/gcc`, PlatformIO Core, pytest, pandas, Matplotlib, NumPy, SciPy, SymPy, Git LFS. The external discussion also named `GeneralElectric/CalculiX` on GitHub as a distribution; it was not verified and is not used here. Use the official CalculiX site above.

### Documentation and video

| Topic | Link | Check |
|---|---|---|
| FreeCAD documentation | https://www.freecad.org/documentation/ | Named by the external discussion; not opened here |
| FreeCAD tutorial video | https://www.youtube.com/watch?v=LrFmUwd8HXs | Title "FreeCAD Parametric Modelling Tutorial – Master the Basics of 3D Design", channel Open Source CNC (confirmed through YouTube oEmbed). Use for concepts, not for the frozen FreeCAD version |
| CadQuery documentation | https://cadquery.readthedocs.io/ | Named by the external discussion; not opened here |
| KiCad learning resources | https://www.kicad.org/help/learning-resources/ | Opened; lists the Contextual Electronics series |
| KiCad getting started (9.0) | https://docs.kicad.org/9.0/en/getting_started_in_kicad/getting_started_in_kicad.html | Named by the external discussion; not opened here. Written for KiCad 9.0 |
| KiCad video series (Chris Gammell, Contextual Electronics) | https://www.youtube.com/user/contextualelectronic/playlists | Linked from the KiCad page: "7 parts ~2.5 hours" |
| SimpleFOC channel | https://www.youtube.com/@theskura | Channel for the SimpleFOC project updates and projects. No individual video is cited |

Tutorial material teaches concepts. It is not evidence that the Kritva motor and controller combination is valid.

## 7. Freeze first, keep optional

| Area | Freeze for the first baseline | Optional until needed |
|---|---|---|
| CAD | FreeCAD version, file and drawing conventions, export workflow | CadQuery, OpenSCAD |
| Calculations | Existing Python engine and `check_calcs` | Extra numerical libraries |
| FEA | Nothing until a workflow is accepted | CalculiX, FreeCAD FEM |
| PCB | KiCad version, libraries, design rules, CLI commands | KiBot, other EDA suites |
| Firmware | Arm GCC, CMake, selected STM32G4 peripheral layer, build configuration | PlatformIO, Zephyr, libopencm3 |
| Tests | One C unit-test framework and pytest | Several competing frameworks |
| CAN | Protocol version, DBC or message definitions, log format | SavvyCAN, other analysers |
| Simulation | Deterministic Python joint model | Renode, MuJoCo |
| CI | `make check`, pinned workflows, evidence conventions | Automatic hardware tests |

Pin CI images, toolchain versions and GitHub Actions to reviewed immutable references. Lock Python dependencies. Do not let build scripts fetch the newest tool silently. Qualify a headless CAD export or DRC step in the CI environment before making it merge-blocking, and do not present a file-presence check as geometric or electrical verification.

## 8. Suggested order

1. Record the toolchain, versions and licences in the decision log.
2. Make the sizing engine and `make check` reproducible in the pinned CI environment.
3. Freeze Kritva-M FreeCAD conventions, drawing exports, BOM fields and export checks.
4. Set up KiCad, ERC/DRC and the manufacturing-export flow.
5. Set up GCC and CMake builds, per-variant configuration, host unit tests and protocol tests.
6. Add CAN logging, bench or hardware-in-loop tests and any simulation.
7. Extend the proven flow to Kritva-S and Kritva-L.

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-18 | Kritvaos Actuator Team | Initial proposal with checked repository and video references |
