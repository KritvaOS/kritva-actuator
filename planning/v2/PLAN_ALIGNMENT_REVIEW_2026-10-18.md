# Kritva Actuator: Alignment Review of the External Implementation Plan (2026-10-18)

| Field | Value |
|---|---|
| Document ID | KA-PLAN-ALIGN-REVIEW |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.2 |
| Date | 2026-10-18 |
| Document owner | Project Lead |
| Reviewer / Approver | Project Lead |
| Applies to | A0, A1, A2 |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** Review record. An external planning discussion (ChatGPT, "Actuator Implementation Plan", 2026-10-18) proposed milestones M0 to M6, task formats, a document layout and a tool flow. This record compares it with the repository as it stands and lists what was adopted, adapted or not adopted. The discussion is advice, not a source of requirements or approvals. No existing ID, status file, gate or baseline was changed.

---

## 1. Summary

The discussion's overall principles agree with the repository: stable task IDs, evidence tied to commit and CI, independent review, pinned child commits, planning dates kept separate from approved commitments, no waiver of a failed safety test. Most of its structure already exists here. The differences are in dates, task naming, document layout and one possible duplication of status reporting.

## 2. Comparison

| Topic | External proposal | Repository today | Disposition |
|---|---|---|---|
| Program horizon | 14 Sep 2026 to 13 Sep 2027 | 24-week roadmap only (`ROADMAP_24_WEEKS.md`) | **Adopted** as `ROADMAP_12_MONTHS.md` (weeks 25-47 proposed) |
| Milestones | M0 to M6 on calendar months | A0, A1, A2 plus Gates A/B/C (`planning/v1/MILESTONE.md`); A0 week 6 (electronics) and week-12 checkpoint (M); A1 weeks 11-12; A2 week 12 | **Adapted.** Local milestones stay authoritative. The layer is renamed Program Planning Overlay (PPO) because `M0`-`M4` already name mechanical audit gates. Migration readiness is tracked separately from the HOLD |
| A0/A1/A2 timing | A0 Nov-Dec, A1 Jan-Mar, A2 Apr-Jun | Earlier (weeks 6-12), depends on motor and gearbox lead times | **Not adopted for A0/A1.** A2 stays one milestone with two staged gates: A2-SW (week 12, optional, owner approval) and A2-HW (weeks 25-36, after A1). v1 and v2 calendars conflict; crosswalk in `ROADMAP_12_MONTHS.md` section 3.2 |
| Task IDs | `ACT-INT-M0-001` style | `ACT-EMB/M/S/L/INT-nnn`, legacy via `TASK_ID_MAPPING.csv`; AGENTS.md forbids changing IDs without an owner decision | **Not adopted.** No new IDs were invented |
| Task tracking | `TASKS.md`, `ACCEPTANCE_CRITERIA.md` per repo | `status/tasks.csv` generates `status/status.json` (schema 2.0, not hand-edited); v1 task folders hold acceptance criteria | **Not adopted.** No new fields in `tasks.csv`. Dependencies and effort stay in planning records, verification methods in requirements and the validation plan. Evidence flow needs agreement with the kritva-program schema owner (the generator emits an empty evidence array) |
| Repository layout | `submodules/ACT-S` etc., `tests/`, `tools/` | `mechanical/actuator-s/m/l`, `embedded/kritva-actuator-embedded` | **Not adopted.** The discussion itself says the layout is logical only |
| Mechanical HOLD | Mentions P6 HOLD | HOLD at program level (kritva-program D-003); `ACT-DEC-027` is still PROPOSED; `ACT-DEC-003` is the gearbox decision | **Consistent.** Roadmap uses the full name D-003 and does not call ACT-DEC-027 accepted |
| Status reporting | Report via kritva-program schema | Done per repo; workstream IDs provisional, not registered in kritva-program | **Consistent.** Do not claim program credit |
| Reference actuator values (24 V, 10 N·m continuous, 20 N·m peak, 45 RPM, 20:1, STM32G4) | Stated as current baseline | `requirements/` owns the limits | **Not copied.** Verify against `requirements/` and `ACTUATOR_FAMILY_SPEC.md` before use; S and L ranges in the discussion are preliminary |
| Program baseline figures (31 tasks, weight 104, 46.15%) | Quoted from its own context | Not in this repository | **Not copied.** Unverified here |
| Safety gating | Human safety review; CI cannot close a safety gate | ACT-DEC-014/015, Gates A/B/C | **Consistent** |
| Tool flow | GitHub, CI, hardware validation, pinned submodules | `make check`, workflows, `SUBMODULE_WORKFLOW.md` | **Consistent.** Stage 5 is implemented but not yet verified |

## 2a. Second-round review (ChatGPT, 2026-10-18)

The comparison above was sent back to the external discussion for challenge. It agreed with the dispositions and added: keep A2 as one milestone with A2-SW and A2-HW gates; resolve the v1/v2 calendar conflict by owner decision; rename the overlay; separate migration readiness, HOLD and test readiness; reserve recovery time before release; do not add fields to `tasks.csv`; call the HOLD kritva-program D-003. It also raised seven risks, now in `ROADMAP_12_MONTHS.md` section 8. Its claim to have read the public `main` branch was not verified here. `ACT-DEC-027` PROPOSED and `ACT-DEC-003` as the gearbox decision were checked against `planning/v1/DECISIONS.md`.

## 3. Items the repository should still settle

1. Stage 5 (submodules) needs parent CI and fresh-clone evidence before M0-equivalent readiness can be claimed (`MIGRATION_PLAN.md`).
2. The owner decides the HOLD lift date, which anchors every calendar date.
3. Whether the 12-month horizon should appear in `PROGRAM_CROSSWALK.csv`.
4. Whether `tasks.csv` needs a dependency or verification-method column. The discussion's task fields suggest it, but the schema is vendored from kritva-program, so this is a program decision.
5. Tasks for weeks 25 to 47 do not exist yet. They are for the owner to create.

## 4. Files changed with this review

| File | Change |
|---|---|
| `planning/v2/ROADMAP_12_MONTHS.md` | New (rev 0.2 after second-round review) |
| `planning/v2/PLAN_ALIGNMENT_REVIEW_2026-10-18.md` | New (this file) |
| `planning/v2/README.md` | Two index rows added |

Not run: `make check`, including the manifest check. The new files may need rows in `MIGRATION_MANIFEST.csv`.

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-18 | Kritvaos Actuator Team | Initial review |
| 0.2 | 2026-10-18 | Kritvaos Actuator Team | Second-round review outcomes applied |
