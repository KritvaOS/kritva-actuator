# Kritva Actuator: Actuator Family Specification (S, M, L)

| Field | Value |
|---|---|
| Document ID | KA-ARCH-FAMILY |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | 2026-10-15 |
| Document owner | Project Lead |
| Reviewer / Approver | Project Lead; Independent Mechanical Reviewer |
| Applies to | A0, A1 |
| Classification | Proprietary and confidential |

> **Status note.** The S, M and L classes are **provisional planning envelopes proposed by the external reviewer, not approved requirements and not guaranteed motor or gearbox ratings** (ACT-DEC-025, PROPOSED). Torque is defined at the **output shaft**. Each speed states whether it is no-load, rated-load or maximum; until a class says otherwise it means rated-load speed at the continuous torque. Only the M row carries the existing elbow baseline, which is itself not frozen (M0 blockers B1 to B6 are open).

---

## 1. Principle

The three mechanical interns develop **three variants of one platform**, not three independent actuator projects. All variants share the same controller, interfaces, protocol, units and acceptance method. They differ in size, motor, gearbox, housing and bearings.

## 2. Provisional classes

| Variant | Continuous output torque | Peak output torque | Speed | Intended role (proposal) | Owner |
|---|---|---|---|---|---|
| Kritva-S | 2 to 5 N·m | 5 to 10 N·m | up to about 60 RPM | Small joints and light mechanisms (for example wrist, neck) | Mechanical Intern 1 |
| Kritva-M | 10 N·m | 20 to 25 N·m (stretch) | 45 RPM | Elbow and reference joint; **the existing baseline** (`requirements/ACTUATOR_SPECIFICATION.md`, ACT-DEC-008) | Mechanical Intern 2 |
| Kritva-L | 25 to 40 N·m | 50 to 80 N·m | about 20 to 40 RPM | Higher-load joints (for example hip, knee), subject to mass, power and thermal feasibility | Mechanical Intern 3 |

Every number in the S and L rows is a placeholder for requirements to be defined by ACT-S-001 and ACT-L-001 and approved by the Project Lead.

## 3. What is common and what varies

| Common to all variants (parent-owned) | Variant-specific (child-owned) |
|---|---|
| Supply voltage class (24 V nominal, ACT-DEC-013) and electrical interface | Motor and gearbox selection, ratio |
| Actuator API, CAN protocol, signal and unit conventions | Housing, mounting, output flange, bearings, shaft |
| Output-side encoder principle (ACT-DEC-010) and the interface to the controller | Encoder mount geometry |
| Sizing method, load-case definitions, safety factors policy | Sizing inputs, results, design decisions |
| Safety requirements, restrained-fixture rule (ACT-DEC-015) | Fixture details, variant test data |
| BOM schema, CAD naming, review and release checklists | The variant's BOM and CAD |

Common electrical limits (maximum bus current, connector pinout, encoder interface) must cover the L class or the embedded design must declare which variants it supports. This is an open item for the interface control document (`docs/interfaces/INTERFACE_CONTROL_DOCUMENT.md`).

## 4. Reference actuator and schedule (proposal)

- **A0 reference actuator: Kritva-M**, the elbow, because it validates the intended application. A0 stays a low-voltage, bench-mounted prototype using a commercial motor and gearbox and a development controller. It is not a human-interactive joint.
- **12-week plan** = the A0 checkpoint inside the **24-week programme**, not a competing schedule (`planning/v2/ROADMAP_24_WEEKS.md`).
- **S and L** reach reviewed design packages (CAD, BOM, interfaces, risks) by week 24. Fabricating and validating all three is a separate commitment that depends on budget, supplier lead time and test capacity.

## 5. Status per variant

Each variant and the embedded platform carry their own status in `docs/standards/RELEASE_CHECKLIST.md`: Concept, Designed, Fabricated, Bench-tested, Validated.

## 6. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-15 | Kritvaos Actuator Team | Initial provisional S, M, L classes and reference-actuator proposal |
