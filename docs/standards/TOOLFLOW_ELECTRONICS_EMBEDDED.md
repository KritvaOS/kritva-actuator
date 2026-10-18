# Kritva Actuator: Tool Flow for Electronics and Embedded Users (ACT-EMB)

| Field | Value |
|---|---|
| Document ID | KA-STD-TOOLFLOW-EMB |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 |
| Date | 2026-10-18 |
| Document owner | Project Lead / Integration Owner |
| Reviewer / Approver | Project Lead |
| Applies to | A0, A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** Proposed working guide, derived from `OPEN_SOURCE_TOOLFLOW.md` (KA-STD-TOOLFLOW), which holds the full reasoning, licence notes and the checked reference list. The toolchain is **not yet frozen**; versions and commands are placeholders until the owner records the freeze in `planning/v1/DECISIONS.md`. Builds, ERC/DRC, unit tests, simulation and CI passes are evidence inputs only. They never close Gate A, B or C or replace independent electrical/firmware review (ACT-DEC-014). The mechanical HOLD was lifted by ACT-DEC-029; fabrication, procurement and loaded testing still need the gates.

---

## 1. Who this is for and where you work

| Workstream | Repository | Parent path |
|---|---|---|
| ACT-EMB | `kritva-actuator-embedded` | `embedded/kritva-actuator-embedded` |

Contents: `firmware/`, `hardware/`, `docs/electronics`, `docs/firmware`. Work on a branch and open a pull request in your repository. The interface, CAN protocol and units are owned by the parent (`docs/interfaces/`); change them through a design change request, never in your repository. One parameterised firmware supports S, M and L (variant configuration for motor, gear ratio, encoder and limits). Do not fork it per variant.

## 2. Tools

| Purpose | Tool | Status |
|---|---|---|
| PCB design | KiCad (`kicad-cli` for checks and exports) | Proposed to freeze |
| PCB automation | KiBot | Optional, AGPL-3.0, external tool only |
| Compiler | Arm GNU toolchain (`arm-none-eabi-gcc`) | Proposed to freeze |
| Build | CMake with a toolchain file | Proposed to freeze |
| Peripheral layer | STM32CubeG4 (HAL/LL) with CMSIS | Candidate; pin release and record licences per component |
| Unit tests | Unity (C), GoogleTest (C++ if needed), pytest (Python) | Freeze one C framework and pytest |
| CAN | python-can, cantools, SavvyCAN, can-utils | Proposed |
| Logs and plots | pandas, Matplotlib; PlotJuggler optional | Proposed |
| Simulation | Renode, MuJoCo, Python joint model | Optional |
| Alternatives | libopencm3, Zephyr, PlatformIO | Only by decision; no second official build |

## 3. Electronics steps (custom controller PCB)

1. **Requirements.** Take limits from `requirements/ELECTRICAL_REQUIREMENTS.md` and the hand-offs in section 6.
2. **Schematic.** Use approved symbols and footprints, with part number and manufacturer fields filled.
3. **Run ERC.** Through `kicad-cli sch erc`. No unwaived errors.
4. **Layout.** Stack-up, current paths, thermal copper, clearances, connector pinouts, debug access.
5. **Run DRC.** Through `kicad-cli pcb drc`. Document every accepted exception; do not use a blanket ignore.
6. **BOM and outputs.** `kicad-cli` for BOM, Gerbers and drill files, plus the existing BOM scripts. Outputs must come from one reviewed PCB commit.
7. **Review.** Independent electronics review (E0-E4) before fabrication is authorised.

Confirm `kicad-cli` options against the frozen KiCad release before writing CI scripts. ERC and DRC do not show electrical or thermal safety. The reviewer still checks phase-current and DC bus ratings, MOSFET and gate-driver choice, current-sense chain, ADC and PWM timing, regeneration, thermal paths and fault paths. Gerbers and BOM are manufacturing outputs, not design acceptance.

## 4. Firmware steps

1. **Architecture.** Layers: CAN and protocol, supervisory state machine, position/speed/torque loops, FOC current loop, PWM/ADC/encoder sensing. Define loop rates, interrupt priorities and fault reactions for the selected hardware.
2. **Build.** Arm GCC, CMake, pinned peripheral layer. Build M, S and L configurations from the same source.
3. **Host unit tests.** Build control logic against mocked hardware and test: FOC mathematics and limits, encoder rollover and invalid readings, state machine (start, enable, command timeout, faults), CAN encode/decode and version checks, variant configuration limits, fault recognition. Use compiler warnings and static analysis. Coverage is supporting evidence, not proof of safety.
4. **CAN protocol tests.** Run without hardware first. Message IDs, scaling, units, timeouts and fault vocabulary come from the parent ICD (`docs/interfaces/CAN_PROTOCOL.md`).
5. **Bench and hardware-in-loop.** Only on a restrained, guarded, instrumented fixture with a test-readiness record (ACT-DEC-015). Record timestamp, configuration ID, firmware commit, procedure revision, command, measured feedback, supply conditions and faults. Store raw logs with the firmware SHA and hardware configuration.
6. **Release.** Emit ELF and binary or HEX, linker map, build log, configuration manifest and checksums. Record compiler, HAL and variant configuration in the evidence.

A compile does not show that the motor, current sensing, PWM timing, gearbox and encoder behave correctly together. Hosted CI never starts a loaded motor test after an ordinary merge. A log processor may report a pass against a criterion declared before the test; it never closes a gate.

## 5. FOC references and code reuse

| Project | Licence | Use |
|---|---|---|
| SimpleFOC | MIT | Learning and concept reference |
| moteus | Apache-2.0 | Controller architecture, diagnostics, host tools |
| ODrive (legacy v3.x) | MIT | Historical reference only |
| VESC firmware | GPL-3.0 | Study only. No code copied into proprietary firmware without a licence decision |

Before reusing source, record the component, licence, version or commit, modified files and notices. A reference design is not validated for Kritva hardware.

## 6. Hand-offs with the mechanical workstreams

| You give ACT-M, ACT-S, ACT-L | You get from them |
|---|---|
| Controller footprint, connector pinout, thermal limits | Motor choice, torque constant, pole pairs, gear ratio, encoder mount envelope, PCB envelope |

Record each hand-off in the parent as a dependency with your child commit SHA.

## 7. References (checked 2026-10-18)

| Item | Link |
|---|---|
| KiCad development / mirror | https://gitlab.com/kicad/code/kicad / https://github.com/KiCad/kicad-source-mirror |
| KiCad learning resources | https://www.kicad.org/help/learning-resources/ |
| KiCad video series, Chris Gammell (Contextual Electronics), 7 parts about 2.5 hours | https://www.youtube.com/user/contextualelectronic/playlists |
| KiCad getting started, 9.0 (named by external review, not opened here) | https://docs.kicad.org/9.0/en/getting_started_in_kicad/getting_started_in_kicad.html |
| KiBot | https://github.com/INTI-CMNB/KiBot |
| CMake | https://github.com/Kitware/CMake |
| CMSIS 6 | https://github.com/ARM-software/CMSIS_6 |
| STM32CubeG4 | https://github.com/STMicroelectronics/STM32CubeG4 |
| libopencm3 | https://github.com/libopencm3/libopencm3 |
| Zephyr | https://github.com/zephyrproject-rtos/zephyr |
| Unity | https://github.com/ThrowTheSwitch/Unity |
| GoogleTest | https://github.com/google/googletest |
| SimpleFOC | https://github.com/simplefoc/Arduino-FOC |
| SimpleFOC YouTube channel (project updates; no single video cited) | https://www.youtube.com/@theskura |
| moteus | https://github.com/mjbots/moteus |
| ODrive | https://github.com/odriverobotics/ODrive |
| VESC firmware | https://github.com/vedderb/bldc |
| python-can | https://github.com/hardbyte/python-can |
| cantools | https://github.com/cantools/cantools |
| SavvyCAN | https://github.com/collin80/SavvyCAN |
| can-utils | https://github.com/linux-can/can-utils |
| Renode | https://github.com/renode/renode |
| MuJoCo | https://github.com/google-deepmind/mujoco |
| PlotJuggler | https://github.com/facontidavide/PlotJuggler |

Not opened in the review: Arm GNU toolchain / `gcc-mirror/gcc`, PlatformIO Core, pytest, pandas and Matplotlib. Confirm them before relying on them. Licences are in `OPEN_SOURCE_TOOLFLOW.md`; GPL and LGPL code needs a review before it is linked into distributed firmware. Tutorials teach concepts only.

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-18 | Kritvaos Actuator Team | Initial electronics and embedded guide split from KA-STD-TOOLFLOW |
