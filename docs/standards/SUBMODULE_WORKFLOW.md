# Kritva Actuator: Submodule Workflow

| Field | Value |
|---|---|
| Document ID | KA-STD-SUBMODULE |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.2 |
| Date | 2026-10-15 |
| Document owner | Project Lead / Integration Owner |
| Reviewer / Approver | Project Lead |
| Applies to | A0, A1 |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** Proposed standard (ACT-DEC-024). It applies to all four repositories once approved.

---

## 1. Layout

| Path in parent | Repository |
|---|---|
| `mechanical/actuator-s` | `KritvaOS/kritva-actuator-s` |
| `mechanical/actuator-m` | `KritvaOS/kritva-actuator-m` |
| `mechanical/actuator-l` | `KritvaOS/kritva-actuator-l` |
| `embedded/kritva-actuator-embedded` | `KritvaOS/kritva-actuator-embedded` |

## 2. Daily work

```text
git clone --recurse-submodules https://github.com/KritvaOS/kritva-actuator.git
git submodule update --init --recursive
```

Interns work in their own repository, on a branch, with a pull request reviewed by the owner and the CODEOWNERS reviewers. They do not push to the parent.

## 3. Updating the parent pointer

Only the Integration Owner does this, after the child change is merged and tagged:

```text
git -C mechanical/actuator-m fetch && git -C mechanical/actuator-m checkout <tag>
git add mechanical/actuator-m
git commit -m "Pin kritva-actuator-m to <tag>"
```

## 4. Rules

1. Never commit in a submodule while on a detached HEAD without a branch.
2. Push the child before the parent; the parent must never point to an unpushed commit.
3. No credentials in `.gitmodules` or in URLs. `.gitmodules` uses HTTPS URLs; to push over SSH from your machine run once: `git config --global url."git@github.com:".pushInsteadOf "https://github.com/"`.
4. Parent CI uses a recursive checkout. The children are public (ACT-DEC-034), so the default token works. If a child is ever made private, store a fine-grained personal access token (or GitHub App token) with read-only Contents access to the four children as the secret `CHILD_REPOS_TOKEN`. The default `GITHUB_TOKEN` cannot read other private repositories.
5. Interface changes start in the parent, not in a child.

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-15 | Kritvaos Actuator Team | Initial draft |
| 0.2 | 2026-10-15 | Kritvaos Actuator Team | HTTPS submodule URLs and token-based CI access |
