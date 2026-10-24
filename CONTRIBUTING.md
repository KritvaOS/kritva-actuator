# Contributing to Kritva Actuator

This guide is for everyone working in the `KritvaOS/kritva-actuator` repository: the Project Lead, interns, reviewers and contractors. The repository is **public** and licensed under **Apache-2.0** ([LICENSE](LICENSE)); your contributions are accepted under the same licence. Do not commit confidential third-party material (supplier quotes, NDA-covered files, personal data, credentials).

## 1. Before you start

1. Read [README.md](README.md), [requirements/SYSTEM_REQUIREMENTS.md](requirements/SYSTEM_REQUIREMENTS.md) and [planning/v1/TASKS.md](planning/v1/TASKS.md).
2. Work only on tasks with status `READY` or `IN_PROGRESS` that are assigned to you. If no task fits your work, ask the Project Lead to create one.
3. Lab work also requires reading [requirements/SAFETY_REQUIREMENTS.md](requirements/SAFETY_REQUIREMENTS.md) and signing the lab-safety briefing (SAF-REQ-061).

## 2. Branches

| Branch | Use |
|---|---|
| `main` | Protected. Reviewed and approved content only. No direct pushes. |
| `feature/ACT-0X-00Y-short-name` | Work on a task, for example `feature/ACT-02-003-shaft-calcs`. |
| `fix/short-name` | Small corrections linked to an Issue. |
| `release/A0`, `release/A1`, `release/A2` | Release stabilisation, when needed. |

Keep branches short-lived. Rebase onto, or merge from, `main` regularly.

## 3. Commits

- Use the Kritva commit standard (kritva-program D-053, adopted under D-070): header `type(scope): summary` of at most 90 characters, types feat, fix, docs, refactor, test, build, ci, chore, perf, revert, security.
- End with exactly one footer line, `Task: ACT-02-003` or `Tasks: ACT-02-003, ACT-02-004`. A docs or chore commit that implements no task uses `Tasks: None (reason)`.
- Example: `feat(shaft): add combined-stress check for 12 mm shaft`, then a blank line, then `Task: ACT-02-003`.
- Use the imperative mood. Write the detail after a blank line.
- Check your commits with `python3 scripts/security/check_commit_format.py --range origin/main..HEAD`; the `commit-message-check` workflow runs the same check.
- Make one logical change per commit. Never commit secrets, credentials or personal data.

## 4. Pull requests

1. Open a PR into `main` using the [PR template](.github/PULL_REQUEST_TEMPLATE.md).
2. Link the task ID and the requirement IDs affected.
3. Run `make check` locally. CI runs the same checks.
4. Update the traceability CSV if you change requirements or verification evidence.
5. **Review requirements:**

| Change type | Minimum reviewer |
|---|---|
| Documentation or non-safety code | One peer (the other intern or the Project Lead) |
| Requirement values or new requirements | Project Lead |
| Safety-critical mechanical items (shaft, bearings, housing, hard stops, fixture) | Independent Mechanical Reviewer (not the author) |
| Safety-critical electrical or firmware items (power stage, protections, fault manager, limits, state machine, watchdog) | Independent Electrical/Firmware Reviewer (not the author) |
| Gate or release records | Project Lead plus the relevant reviewer |

If a required reviewer is unavailable, the PR may be merged only as a draft record with status `NOT_VERIFIED`. The related gate stays blocked (ACT-DEC-014).

### 4.1 Folder responsibilities (CODEOWNERS-style)

Some paths below are owned by child repositories, not by this parent: `hardware/`, `firmware/`, `docs/electronics/`, `docs/firmware/` and the electronics and firmware tests live in `KritvaOS/kritva-actuator-embedded` (submodule `embedded/kritva-actuator-embedded`), and `mechanical/` variant work lives in `kritva-actuator-s`, `-m` and `-l`. Follow each child repository's own `AGENTS.md` and README for contributions there. Paths that do not exist yet in the parent are planned, not owned today.

| Path | Primary owner | Required reviewer for safety items |
|---|---|---|
| `requirements/`, `planning/` | Project Lead | — |
| `mechanical/`, `docs/mechanical/` | Mechanical Intern | Independent Mechanical Reviewer |
| `hardware/`, `docs/electronics/` | Electronics/Embedded Intern | Independent Electrical/Firmware Reviewer |
| `firmware/`, `docs/firmware/`, `communication/can/firmware/` | Electronics/Embedded Intern | Independent Electrical/Firmware Reviewer |
| `docs/interfaces/`, `communication/can/protocol/`, `software/` | Project Lead / Integration Owner | Independent Electrical/Firmware Reviewer |
| `tests/`, `results/` | Owner of the tested item | Reviewer of that domain |
| `audit/` | Reviewers (findings); Project Lead (gates) | — |

## 5. Documentation standard

Every controlled Markdown document starts with this header table:

```
| Field | Value |
|---|---|
| Document ID | KA-<AREA>-<NAME> |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 (Draft: proposed, pending approval) |
| Date | YYYY-MM-DD |
| Document owner | <role> |
| Reviewer / Approver | <role> / <role> |
| Applies to | A0 / A1 / A2 |
| Classification | Public (Apache-2.0, see `LICENSE`) |
```

Then:

- a short status note;
- numbered sections;
- an "Open items" section where relevant;
- a **Revision history** table at the end.

Folder `README.md` guides do not need the header.

- **Units:** SI, following [docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md](docs/interfaces/SIGNAL_AND_UNIT_CONVENTIONS.md).
- **No duplication:** link to the canonical document.
- **Assumptions:** label them as proposed, TBD or TBC. Never present an assumption as a fact.
- **Supplier data:** never invent prices or test results. Candidate parts are labelled "candidate: verify against datasheet".
- `make check-docs` enforces the header and the revision history.

## 6. Requirement and decision changes

1. Raise a `design_change_request` Issue describing the change, its rationale and its impact on other requirements.
2. The Project Lead approves or rejects it. Approved changes are recorded in [planning/v1/DECISIONS.md](planning/v1/DECISIONS.md).
3. Update the requirement document and its revision history, the dependent documents and the traceability CSV, all in the same PR.
4. Never edit an accepted decision to reverse it. Add a new decision that supersedes it.

## 7. CAD, drawings and large files

- Commit **native CAD** (source) together with **neutral exports** (STEP for models, PDF for drawings) for review.
- CAD and binary formats are tracked with **Git LFS** (see [.gitattributes](.gitattributes)). Run `git lfs install` once per machine.
- Name files `<part-number>_<name>_rev<X>.<ext>`, for example `KA-MEC-0003_output_shaft_revA.step`.
- Do not commit generated build outputs, CAD temporary or lock files, or raw high-rate logs larger than about 50 MB. Store large raw data according to the agreed storage approach, and link to it from `results/`.

## 8. Firmware coding standard (summary)

The full rules are in [requirements/FIRMWARE_REQUIREMENTS.md](requirements/FIRMWARE_REQUIREMENTS.md) section 18:

- C11, or a restricted C++17 subset.
- A MISRA-inspired rule set; all warnings enabled and treated as errors.
- No dynamic allocation after initialisation; no blocking calls in ISRs or control loops.
- Vendor and HAL code only in `firmware/platform/`.
- Host unit tests for platform-independent modules.
- Third-party code is registered, with its licence, in `firmware/README.md`, and reused only after a licence review.

## 9. Test evidence

- Test procedures live in `tests/`. Measured results live in `results/<area>/YYYY-MM-DD_<test-id>_<short-name>/`.
- Every record includes the hardware revision and serial number, firmware version and hash, supply voltage, load, ambient temperature, instruments with calibration status, operator, observer, procedure version and measured results with a pass/fail against the **pre-approved** criterion.
- A requirement is never marked `PASS` without this evidence.

## 10. Definition of done

A task is done when all of the following are true:

- its deliverables are in their canonical location;
- its acceptance criteria are met with evidence;
- traceability is updated;
- the review is complete (independent where required);
- no CRITICAL or HIGH finding is open;
- the Project Lead has set the status to `DONE`.

## 11. Lab safety rules (summary)

- Test only on a restrained, guarded, instrumented fixture.
- **Never** resist the actuator by hand or attach it to a person.
- Use a current-limited PSU for bring-up, with a hardware e-stop within reach.
- Keep the clear zone empty while the actuator is enabled. Wear safety glasses for loaded, peak and impact tests.
- Follow the two-person rule for loaded tests (TBC).
- Report every incident or near miss to the Project Lead on the same day.
