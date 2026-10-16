# Kritva Actuator: Repository Architecture (Parent and Four Submodules)

| Field | Value |
|---|---|
| Document ID | KA-ARCH-REPO |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.3 (Draft: proposed, pending approval) |
| Date | 2026-10-15 |
| Document owner | Project Lead |
| Reviewer / Approver | Project Lead; Independent Mechanical Reviewer; Independent Electrical/Firmware Reviewer |
| Applies to | A0, A1, A2 |
| Classification | Proprietary and confidential |

> **Status note.** This document records the proposed restructuring of this repository for the four-intern implementation plan: three Mechanical Interns (Kritva-S, Kritva-M, Kritva-L) and one Embedded Intern. It follows the external reviewer's recommendation of 2026-10-15 (ChatGPT session, branch of the Kritva OS project) and is **proposed, pending Project Lead approval** (ACT-DEC-024). **Status (2026-10-16): Stages 1 to 4 are complete and the four submodules are added (Stage 5 implemented, not yet verified by a passing full parent CI on a fresh recursive clone). Stage 6 (audit and release) has not started.** The migration is staged and tracked in `planning/v2/MIGRATION_PLAN.md`; every existing file has a recorded destination in `planning/v2/MIGRATION_MANIFEST.csv`.

---

## 1. Decision in one paragraph

`KritvaOS/kritva-actuator` stays the **parent (program and integration) repository**. Four independent repositories are added beneath it as Git submodules: three mechanical repositories (one per actuator variant) and one embedded repository. The parent owns the system-level contracts, the common sizing method, the integration tests and the audit record. Each child owns its own implementation and its own raw evidence. The parent records the exact reviewed commit of each child, so an integrated configuration is reproducible.

## 2. Repositories and owners

The four child repositories were created (private, empty) on 2026-10-15: `https://github.com/KritvaOS/kritva-actuator-{s,m,l,embedded}`. Their scaffolds are pushed by `scripts/integration/bootstrap_children.sh`.

| Repository | Owner | Contents | Must not redefine |
|---|---|---|---|
| `KritvaOS/kritva-actuator` (parent) | Project Lead / Integration Owner | Requirements, architecture, interface contracts, common sizing method, planning, audits, traceability, integration tests and results, CI | Variant CAD, firmware implementation |
| `KritvaOS/kritva-actuator-s` | Mechanical Intern 1 | Kritva-S CAD, drawings, BOM, sizing inputs and results, mechanical tests and evidence | Common interface, protocol |
| `KritvaOS/kritva-actuator-m` | Mechanical Intern 2 | Kritva-M CAD, drawings, BOM, sizing inputs and results, mechanical tests and evidence. Holds the elbow reference baseline | Common interface, protocol |
| `KritvaOS/kritva-actuator-l` | Mechanical Intern 3 | Kritva-L CAD, drawings, BOM, sizing inputs and results, mechanical tests and evidence | Common interface, protocol |
| `KritvaOS/kritva-actuator-embedded` | Embedded Intern | Firmware, controller hardware, electronics and firmware documents, electronics BOM, firmware and hardware tests and bring-up evidence | Variant mechanical design |

The child repository names and the three variant classes are proposals (see `ACTUATOR_FAMILY_SPEC.md`).

## 3. Target layout of the parent

```
kritva-actuator/
  README.md  LICENSE  CONTRIBUTING.md  CHANGELOG.md  Makefile  .gitmodules
  docs/
    architecture/   system and actuator architecture, family spec, sourcing and cost, this document
    interfaces/     actuator interface, CAN protocol, unit conventions, interface control document
    validation/     system validation plan, test equipment, performance characterisation
    standards/      CAD naming, BOM, design review, release, submodule workflow
  requirements/     system, actuator, mechanical, electrical, firmware, interface, safety requirements
  planning/
    v1/             historical plan, decisions log, task history (kept, never renumbered)
    v2/             four-intern plan: migration plan and manifest, workstreams, 24-week roadmap, task ID mapping
  audit/            external, requirements traceability, release, and the independent review records
  scripts/          validation, bom, integration (submodule and manifest checks)
  mechanical/
    common-sizing/  shared sizing engine, golden results, methodology   (Stage 4)
    actuator-s/     submodule
    actuator-m/     submodule
    actuator-l/     submodule
  embedded/
    kritva-actuator-embedded/   submodule
  tests/integration/  results/integration/
  software/         actuator_interface and the KritvaOS-facing driver (parent-owned contracts)
```

Today the parent still holds the pre-migration folders (`mechanical/`, `hardware/`, `firmware/`, `communication/`, `software/`, `tests/`, `results/`). They are moved or split in Stage 4 using the manifest, not before.

## 4. Ownership of existing content

The authoritative per-file map is `planning/v2/MIGRATION_MANIFEST.csv`. The rules behind it:

| Existing path | Owner | Rule |
|---|---|---|
| `requirements/`, `docs/architecture/`, `docs/interfaces/`, `docs/validation/`, `planning/`, `audit/`, `scripts/` | Parent | Kept. Single authoritative home |
| `mechanical/calculations/actuator_sizing.py`, `expected_results.json` | Parent | Shared deterministic sizing engine and golden regression; each variant supplies its own inputs |
| `mechanical/calculations/*.md` | Parent methodology, M results | Method stays in the parent; Kritva-M's inputs and results move to the M repository when the engine reads external inputs |
| `mechanical/bom/`, `cad/`, `drawings/`, `assembly/` | S, M, L | The existing reference design becomes Kritva-M; S and L receive the same skeleton |
| `hardware/`, `firmware/`, `docs/electronics/`, `docs/firmware/` | Embedded | Moved with their tests and results |
| `communication/can/protocol`, `software/actuator_interface` | Parent | Single source of truth for IDs, payloads, units, timing, versioning and fault semantics |
| `communication/can/firmware` | Embedded | MCU-side implementation |
| `software/kritva_driver`, `host_tools`, `simulation`, `communication/can/tools` | Split | KritvaOS-facing and generic tools in the parent; MCU-specific tools in the embedded repository; variant models in the variant repository |
| `tests/integration/`, `tests/safety/`, `tests/performance/` | Parent | System acceptance and comparable metrics; children keep their own raw results |
| `tests/firmware/`, `tests/unit/`, `tests/hardware/` | Embedded | Implementation-level tests |
| `tests/mechanical/`, `results/mechanical/` | S, M, L | Variant tests and raw data |

A directory whose contents span ownership is **split by file**. Each destination is recorded in the manifest, and a pointer file may be left at the old location.

## 5. Rules that apply from now on

1. **One authoritative owner per artefact.** Children reference the parent's contracts and record deviations; they never fork them.
2. **The parent contains no duplicate editable CAD, firmware or BOM.**
3. **Pinned commits.** The parent records a reviewed commit for each submodule. CI tests the pinned commits, never a floating `main`.
4. **Child changes first.** A change inside a submodule is committed and pushed to that repository, reviewed, and only then is the parent pointer updated (see `docs/standards/SUBMODULE_WORKFLOW.md`).
5. **Audit continuity.** Restructuring is not evidence that any engineering finding is closed. Open findings (M0 blockers, EXT-AUD items) carry forward unchanged until evidence closes them.
6. **No silent drops.** Every original file has a destination or a recorded disposition (`scripts/validation/check_manifest.py`).
7. **Statuses are per variant.** Concept, Designed, Fabricated, Bench-tested and Validated are recorded separately for S, M, L and the embedded platform (`docs/standards/RELEASE_CHECKLIST.md`). CI success alone never promotes a design to Validated.

## 6. CI responsibilities

| Check | Parent CI | Child CI |
|---|---|---|
| Documentation headers, links | Yes | Yes, for the child's own documents |
| Traceability | Parent requirements, acceptance criteria, task mapping, and that referenced child files exist at the pinned commits | Local requirement to design to test traceability |
| Calculations | Shared sizing-engine regression; each variant's `sizing/inputs.json` run through the shared engine where practical | Variant calculations and expected-result tolerances |
| BOM | Not duplicated | `scripts/check_bom.py` on the child's BOM |
| Interface compatibility | Protocol and API schemas, cross-variant integration tests | Conformance to the pinned interface contract |
| Submodule integrity | `scripts/integration/check_submodules.py`: four expected submodules, no credentials in URLs, pins valid | n/a |
| Firmware build, unit tests, static analysis | No | Embedded repository |

Parent CI checks out submodules recursively over HTTPS. While the children are public the default token is enough. When they are private, the default `GITHUB_TOKEN` cannot read them, so use a **fine-grained personal access token or GitHub App token with read-only Contents access to the four children**, stored as the Actions secret `CHILD_REPOS_TOKEN` (the workflow uses it when present). Secrets live in Actions secrets and never in `.gitmodules`, URLs, logs or artefacts.

## 7. Open items

| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | Approve ACT-DEC-024 (this architecture), ACT-DEC-025 (variant family) and ACT-DEC-026 (shared sizing engine) | Project Lead | Before Stage 3 |
| 2 | Create the four child repositories from the scaffolds | Project Lead | Stage 3 |
| 3 | Choose the history method (filtered history or documented import commit) | Project Lead | Stage 4 |
| 4 | Make `software/` ownership final once ACT-03-001 is approved | Project Lead / Embedded Intern | Stage 4 |
| 5 | When the children return to private: create the read-only token and store it as `CHILD_REPOS_TOKEN` | Repository administrator | Before making the repositories private again |

## 8. Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-15 | Kritvaos Actuator Team | Initial proposal: parent plus four submodules, ownership rules, CI split |
| 0.2 | 2026-10-15 | Kritvaos Actuator Team | Child repositories created on GitHub; bootstrap step recorded |
| 0.3 | 2026-10-15 | Kritvaos Actuator Team | CI access via HTTPS submodules and a read-only token instead of deploy keys |
