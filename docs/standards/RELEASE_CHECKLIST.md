# Kritva Actuator: Release Checklist

| Field | Value |
|---|---|
| Document ID | KA-STD-RELEASE |
| Repository | `KritvaOS/kritva-actuator` |
| Revision | 0.1 |
| Date | 2026-10-15 |
| Document owner | Project Lead |
| Reviewer / Approver | Project Lead; Independent Reviewers |
| Applies to | A0, A1, A2 |
| Classification | Public (Apache-2.0, see `LICENSE`) |

> **Status note.** Proposed standard (ACT-DEC-024). It applies to all four repositories once approved.

---

## 1. Variant status

| Status | Meaning | Who sets it |
|---|---|---|
| Concept | Sizing and concept CAD | Variant owner |
| Designed | Design review checklist passed | Independent reviewer |
| Fabricated | Parts made and inspected | Variant owner, inspection record |
| Bench-tested | Characterisation on the restrained fixture, results in the repository | Reviewer |
| Validated | Validation plan executed and release audit signed | Project Lead and reviewers |

CI success does not set a status.

## 2. Release steps (per tagged parent release)

1. Each child has a signed tag and a clean `make check`.
2. The parent updates the submodule pointers to those tags in one pull request.
3. `make check-submodules` passes (pinned SHAs fetchable, no credentials in URLs).
4. Integration tests run against the pinned set; results go to `results/integration/`.
5. The release note lists the four SHAs, per-variant status, open audit findings and known limits.
6. Safety statement: tests only on restrained, guarded, instrumented fixtures.

## Revision history

| Rev | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-10-15 | Kritvaos Actuator Team | Initial draft |
