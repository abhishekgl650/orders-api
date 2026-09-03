# Deploy history (most recent first)

Production deploys happen automatically when a PR merges to `main`
(`deploy-prod` Action, ~2 min lag). Times are UTC, 2026-09-02.

| Merged (UTC) | PR | Title | Author | Deployed |
|---|---|---|---|---|
| 14:56 | #48 | Clarify log message on order-not-found | dpatel | 14:58 |
| 14:38 | #47 | Refactor get_order to reduce duplication | rlong | 14:40 |
| (2026-08-30) 09:12 | #45 | Bump psycopg2 2.9.6 -> 2.9.9 | s.ahmed | 09:14 |
| (2026-08-27) 16:40 | #44 | Add /customers/{id}/orders endpoint | rlong | 16:42 |

Notes:
- #48 is a one-line change to an error string (see src/app.py, the 404 detail).
- #47 rewrote get_order. Diff in incident/pr-47-diff.md.
- #45 was a patch-level dependency bump; service has run on it cleanly for 3 days.
- Pool size (pool_max: 20) has not been changed by any recent deploy.
