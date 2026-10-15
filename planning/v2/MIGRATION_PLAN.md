# Kritva Actuator: Repository Migration Plan (Parent + 4 Submodules)

| Field | Value |
|---|---|
| Document ID | KA-PLAN-MIGRATION |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.3 |
| Date | 2026-10-15 |
| Document owner | Project Lead |
| Reviewer / Approver | Project Lead; Independent Reviewer |
| Applies to | A0, A1 |
| Classification | Proprietary and confidential |

> **Status note.** Proposed plan (ACT-DEC-024), pending Project Lead approval. Stages 1 to 3 are delivered as additive files; **no existing file has been moved or deleted**. Stage 4 onward is run by the repository owner with the git steps in section 4.

---

## 1. Principles

1. Do not do a big-bang move. Each stage ends with a repository that still passes `make check`.
2. Every existing file has a destination in `MIGRATION_MANIFEST.csv`. Files not in the manifest are reported by `scripts/validation/check_manifest.py`.
3. Legacy task IDs (`ACT-01/02/03-xxx`) stay immutable. New IDs are listed in `TASK_ID_MAPPING.csv`.
4. Contracts (interfaces, units, CAN protocol, sizing method) are frozen in the parent before the children diverge.
5. CI success never promotes a design to Validated. Per-variant status is one of Concept, Designed, Fabricated, Bench-tested, Validated, set by review.
6. The parent pins an exact reviewed commit of each child. Nothing is integrated from a moving branch.

## 2. Stages

| Stage | Name | Outcome | Who | Moves files? |
|---|---|---|---|---|
| 1 | Freeze and inventory | Tag the current state; manifest and task mapping written | Project Lead | No |
| 2 | Contracts | Interface Control Document, family spec, standards, repository architecture reviewed | Project Lead, interns | No |
| 3 | Create child repositories | **Repos created (2026-10-15).** Remaining: push the scaffolds, branch protection, CODEOWNERS handles, deploy keys | Project Lead | No (new, empty repos) |
| 4 | Migrate by workstream | Embedded first, then M, then S and L from the M template; manifest rows set to MIGRATED | Each intern, reviewed | Yes |
| 5 | Integrate as submodules | `git submodule add` of four repos at pinned SHAs; parent CI uses recursive checkout | Project Lead | Yes (parent) |
| 6 | Audit and release | Manifest has no PLANNED rows; submodule SHAs recorded in a release note; audit re-run | Project Lead, reviewers | No |

## 3. Stage detail

### Stage 1: freeze and inventory
- Resolve open items that would be copied into history: `git rm -r "Claude outputs"` (EXT-AUD-018) and a secrets scan.
- Tag the parent `pre-restructure-2026-10-15`.
- Confirm `planning/v2/MIGRATION_MANIFEST.csv` and `TASK_ID_MAPPING.csv` cover every tracked file (`make check-manifest`).

### Stage 2: contracts
- Approve `docs/architecture/REPOSITORY_ARCHITECTURE.md`, `ACTUATOR_FAMILY_SPEC.md` and `docs/interfaces/INTERFACE_CONTROL_DOCUMENT.md`.
- Approve the standards under `docs/standards/` (CAD naming, BOM, design review, release, submodule workflow).
- Decide ACT-DEC-024, 025 and 026.

### Stage 3: create child repositories
Status: the four repositories exist (created 2026-10-15 by the Project Lead):

| Repository | URL |
|---|---|
| Embedded | https://github.com/KritvaOS/kritva-actuator-embedded |
| Kritva-S | https://github.com/KritvaOS/kritva-actuator-s |
| Kritva-M | https://github.com/KritvaOS/kritva-actuator-m |
| Kritva-L | https://github.com/KritvaOS/kritva-actuator-l |

Remaining Stage 3 work: run `scripts/integration/bootstrap_children.sh` (pushes the scaffold as the first commit of each repo), then the items below.

- Confirm the four repositories are **private** (Settings, General).
- Copy the matching scaffold from `child-repos/` (delivered separately) as the first commit.
- Add a read-only deploy key per child to the parent, or a scoped GitHub App token. `GITHUB_TOKEN` cannot read other private repositories.
- Enable branch protection and CODEOWNERS in each child.

### Stage 4: migrate by workstream
Order: embedded, M, then S and L.

- **History.** Preferred: `git filter-repo --path <paths>` on a fresh clone to keep history of moved files. Acceptable: one documented import commit that states the source SHA.
- **Embedded.** `firmware/`, `hardware/`, `docs/electronics`, `docs/firmware`, `tests/firmware|unit|hardware`, `results/motor_control`, `communication/can/firmware`.
- **M.** `mechanical/bom/MECHANICAL_BOM.csv`, M results split from `mechanical/calculations`, copy of the folder skeleton.
- **Shared sizing.** `actuator_sizing.py` and `expected_results.json` move inside the parent to `mechanical/common-sizing/`; update `scripts/validation/check_calcs.py` paths in the same commit.
- **S and L.** Start from a copy of the M skeleton; `sizing/inputs.json` carries the variant inputs. Status is Concept.
- After each move set the manifest row status to MIGRATED and run `make check`.
- **Scripted for MOVE rows:** `scripts/integration/stage4_migrate.sh embedded` (or `m`) pushes the files to a branch `stage4/import-from-parent` of the child (open a pull request), then `git rm`s them in the parent, marks the manifest rows MIGRATED and rewrites traceability and BOM references to the submodule path. Merge the child pull request first, then commit the parent. SPLIT and COPY_TEMPLATE rows are done by hand.
- Expected after the embedded move: `check_docs` warns that `firmware/` and `hardware/` are absent, and `check_bom` / traceability warn that evidence files are not present until Stage 5 adds the submodule. These warnings are temporary.

### Stage 5: integrate as submodules
Paths: `mechanical/actuator-s`, `mechanical/actuator-m`, `mechanical/actuator-l`, `embedded/kritva-actuator-embedded`. Use `scripts/integration/check_submodules.py` to verify `.gitmodules`, pinned SHAs and the absence of credentials in URLs.

### Stage 6: audit and release
- Manifest has no PLANNED rows.
- Traceability CSV paths updated to submodule paths.
- Release note lists the four pinned SHAs and per-variant status.

## 4. Runbook (git steps run by the repository owner)

```text
# Stage 1
git tag pre-restructure-2026-10-15 && git push origin pre-restructure-2026-10-15
git rm -r "Claude outputs"          # EXT-AUD-018

# Stage 3 (repos already exist; push the scaffolds)
mkdir -p ~/kritva-scaffold && unzip kritva-child-repos.zip -d ~/kritva-scaffold
scripts/integration/bootstrap_children.sh ~/kritva-scaffold/child-repos

# Stage 4 (history-preserving example for embedded)
git clone --no-local kritva-actuator kritva-actuator-embedded-import
cd kritva-actuator-embedded-import
git filter-repo --path firmware --path hardware --path docs/electronics --path docs/firmware
# then push this to the embedded repo, or import as one documented commit

# Stage 5 (in the parent, after the content is in the children)
git submodule add git@github.com:KritvaOS/kritva-actuator-embedded.git embedded/kritva-actuator-embedded
git submodule add git@github.com:KritvaOS/kritva-actuator-m.git mechanical/actuator-m
git submodule add git@github.com:KritvaOS/kritva-actuator-s.git mechanical/actuator-s
git submodule add git@github.com:KritvaOS/kritva-actuator-l.git mechanical/actuator-l
```

`scripts/integration/add_submodules.sh` runs the four `submodule add` commands once the children hold their content.

Move files in the parent with `git mv`, never delete and recreate.

## 5. Risks

| Risk | Mitigation |
|---|---|
| Interns diverge on interfaces | Interface Control Document in the parent; change by design change request |
| Parent CI cannot read private children | Deploy keys or GitHub App; checked in `check_submodules.py` and the CI notes |
| Detached-HEAD or unpushed submodule commits | Submodule workflow standard; CI fails if a pinned SHA is not fetchable |
| History loss | filter-repo or documented import commit with source SHA |
| Three variants triple the review load | Same template, same checklists; M first, S and L only after M passes the Design review |

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-15 | Kritvaos Actuator Team | Initial draft: six-stage migration plan and runbook (ACT-DEC-024) |
| 0.2 | 2026-10-15 | Kritvaos Actuator Team | Stage 3: four child repositories created; bootstrap and submodule scripts added |
| 0.3 | 2026-10-15 | Kritvaos Actuator Team | Stage 4 script for MOVE rows (embedded, m) |
