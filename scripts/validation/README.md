# scripts/validation

Repository consistency checks. They use the Python 3.8+ standard library only and are run by `make check` and the `docs-checks` CI workflow.

| Script | Make target | What it checks |
|---|---|---|
| `check_docs.py` | `make check-docs` | Every controlled KA- Markdown document (first table contains `Document ID`) has the mandatory header fields, a valid `KA-<AREA>-<NAME>` ID that is unique in the repository, an ISO date, a revision number and a `Revision history` table. It warns about a missing status note, a non-proprietary classification, emoji, or other Markdown files without a header (folder `README.md` files are skipped). |
| `check_links.py` | `make check-links` | Relative Markdown links resolve to existing files and anchors. With `--code-paths`, it also warns about repository paths in inline code that do not exist yet. |
| `check_traceability.py` | `make check-trace` | `audit/requirements_traceability/REQUIREMENTS_TRACEABILITY.csv` has the schema below, valid IDs, valid status values, parents that exist, and a row for every requirement ID defined in `requirements/*.md`. `--summary` prints counts by status. |

All scripts:

- exit with status 0 when there are no errors, and 1 on errors (or on warnings with `--strict`);
- warn rather than crash when a file does not exist yet.

## Traceability CSV schema

```
requirement_id,source_document,requirement_summary,parent_ids,owner,phase,verification_method,verification_procedure,evidence_location,verification_status,audit_document,audit_status,last_updated,notes
```

| Column | Allowed values |
|---|---|
| `verification_status`, `audit_status` | `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `PASS_WITH_ACTIONS`, `FAIL`, `NOT_VERIFIED` |
| `verification_method` | T / A / I / D, alone or combined (for example `A, T`) |
| `phase` | A0, A1, A2 (combinations allowed) |
| `parent_ids` | Required for every non-SYS requirement; separate multiple IDs with `;` |
