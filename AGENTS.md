# Kritva Actuator (parent) Agent Instructions

These instructions apply to the `kritva-actuator` parent repository. Child repositories `kritva-actuator-s`, `-m`, `-l` and `-embedded` are tracked as submodules.

## Boundaries

- The mechanical HOLD (kritva-program D-003) was lifted by Dinesh in ACT-DEC-029 (2026-10-18). That does not authorise CAD release, procurement, fabrication or design freeze work by itself: these need Gate A and the pending decisions in `planning/v1/DECISIONS.md`, with independent review (ACT-DEC-014). Do not treat any check in this repository as physical safety or design acceptance.
- Status reports (`status/status.json`, schema 2.0) are planning-only. Regenerate them from `status/tasks.csv`; do not edit them by hand, and do not mark tasks accepted. Nothing here creates program credit.
- Interface, CAN protocol, units and shared requirements are owned by the parent `kritva-actuator` repository (ICD at `docs/interfaces/`). Do not redefine them in a child repository.
- Submodule pointers (`mechanical/actuator-s|m|l`, `embedded/kritva-actuator-embedded`) are bumped deliberately, one reviewed change at a time. Content inside a child is governed by that child's own rules and CODEOWNERS.
- `planning/v2/TASK_ID_MAPPING.csv` maps actuator task IDs to the program inventory. Do not change IDs or rows without an owner decision.
- The independent-review rule (ACT-DEC-014) applies to safety-relevant changes.

## Validation before a pull request

    make check

(`make help` lists the individual targets: docs, links, traceability, BOM, calculations, manifest, submodules, status.) When `README.md` changes, also run `make check-readme` (Kritva README standard, kritva-program D-055); it checks structure, metadata fields and local links only, not accuracy or approval.

## Secrets and data

- Never commit credentials, tokens, private keys, production data or personal data. Use obviously fake values in examples and mark them as such.
- If a secret is committed by mistake, tell the Security Owner (Dinesh, D-032) at once. Removing it in a later commit does not make it safe; it must be revoked or rotated.
- The `secret-scan` workflow (gitleaks) runs on every push and pull request. Do not add allowlist entries to silence it; propose them to the owner with the reason.

## Commits and pull requests

- Work on a branch and open a pull request. Do not push to `main`. Do not force-push shared branches or rewrite history without the owner's explicit approval.
- Use short imperative messages in the repository's existing style (`type(scope): summary`).
- Do not add `Claude-Session:` or session-URL trailers to commit messages or pull request descriptions. The `commit-message-check` workflow rejects them. A `Co-Authored-By:` line is allowed.
- Commit and PR standard (kritva-program D-053, v2/planning/ACCEPTANCE_STANDARD.md section 4): `type(scope): summary` (types feat, fix, docs, refactor, test, build, ci, chore, perf, revert, security) with one `Task:` or `Tasks:` footer, `Tasks: None (reason)` only on a docs or chore commit that implements no task; the merge method is a merge commit; PR text follows `.github/PULL_REQUEST_TEMPLATE.md`. Check with `python3 scripts/security/check_commit_format.py --range origin/main..HEAD`. This repository adopted the format under D-070: `commit-message-check` runs this check on every pull request. This repository keeps its own hardware-specific PR template.
- `main` is protected by a ruleset that requires `secret-scan`, `commit-message-check` and Code Owner review (owner statement, D-040; not independently verified). With one owner, the PR author cannot self-approve: ask the owner to merge using the bypass or add a second reviewer.

## When unsure

Say what you do not know and ask the owner. Do not invent evidence, test results, hardware behaviour or approvals, and do not claim a check passed unless you ran it.
