# Kritva Actuator: Interface Control Document (Family)

| Field | Value |
|---|---|
| Document ID | KA-IF-ICD |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 |
| Date | 2026-10-15 |
| Document owner | Project Lead / Integration Owner |
| Reviewer / Approver | Project Lead; Independent Reviewers |
| Applies to | A0, A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** Proposed index and skeleton (ACT-DEC-024). It does not replace the canonical interface documents; it states which interfaces are common to S, M and L and which dimensions each variant must publish. All dimension values are **TBD** until the variant design closes.

---

## 1. Purpose

Four repositories now build one actuator family. This document is the single place that lists what must not differ between variants, and what every child repository must publish so the parent can integrate it.

## 2. Common contracts (owned by the parent, not redefined in children)

| Interface | Canonical document | Owner |
|---|---|---|
| Software API, return codes, fault codes, configuration parameters, USB/UART framing | `docs/interfaces/ACTUATOR_INTERFACE.md` | Integration Owner |
| CAN identifiers, scaling, payloads, timing | `docs/interfaces/CAN_PROTOCOL.md` | Integration Owner |
| Units, sign convention, output-side versus motor-side quantities | `docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md` | Integration Owner |
| Software and hardware boundary | `docs/architecture/SOFTWARE_HARDWARE_BOUNDARY.md` | Integration Owner |
| Requirements | `requirements/*.md` | Project Lead |

A change to any row goes through a design change request in the parent and is reviewed by both the embedded intern and the affected mechanical interns.

## 3. Variant-published data (each child provides; values TBD)

| Item | S | M | L | Consumer |
|---|---|---|---|---|
| Rated and peak output torque, speed | TBD | TBD | TBD | Embedded, integration |
| Gear ratio, motor Kt, pole pairs, resistance, inductance | TBD | TBD | TBD | Embedded (variant configuration) |
| Output-side reflected inertia | TBD | TBD | TBD | Embedded, simulation |
| Encoder type, magnet, mount envelope | TBD | TBD | TBD | Embedded |
| Controller PCB envelope and mounting | TBD | TBD | TBD | Embedded |
| Output flange pattern and mounting interface | TBD | TBD | TBD | Humanoid integration |
| Connector and pinout (power, CAN, encoder) | Common | Common | Common | All |
| Mass and centre of mass | TBD | TBD | TBD | Integration |
| Thermal limits (winding, housing) | TBD | TBD | TBD | Embedded diagnostics |
| Mechanical stop positions and range | TBD | TBD | TBD | Embedded, safety |

Each variant publishes these in `sizing/inputs.json` (inputs) and in its `README.md` interface table (released values), with the Git commit of the source.

## 4. Mechanical-electrical interface

- Controller connector, pinout and wire gauge are common across variants (target; to be fixed in ACT-EMB).
- Each variant keeps its own PCB envelope drawing; the embedded repository's PCB must fit the smallest envelope or have a per-variant outline.
- Output flange pattern is variant-specific; the humanoid-side adapter is outside this repository.

## 5. Change control

1. A child needs a change to a common contract: open a design change request in the parent (`.github/ISSUE_TEMPLATE/design_change_request.md`).
2. The Integration Owner records the decision in `planning/v1/DECISIONS.md` (or its v2 successor).
3. The parent updates the canonical document first; the children then update their pinned parent revision.

## 6. Open items

| Item | Owner |
|---|---|
| Fill the variant table in section 3 once motor and gearbox are chosen per variant | Mechanical Interns |
| Decide whether the controller PCB is one design for all variants | Embedded Intern, Project Lead |
| Decide the flange pattern for each variant | Mechanical Interns, Project Lead |

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-15 | Kritvaos Actuator Team | Initial index and skeleton (ACT-DEC-024) |
