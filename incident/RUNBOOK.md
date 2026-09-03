# orders-api Operations Runbook

This runbook governs how incidents on orders-api are handled, including which
recovery actions may be taken automatically and which require a human to
approve first. When responding to an incident, follow the approval policy
below exactly.

## Severity
- **Sev1** — full outage, data loss, or security exposure.
- **Sev2** — major degradation: elevated error rate or latency affecting most
  requests, service still partially up.
- **Sev3** — minor or cosmetic; no meaningful customer impact.

## Approval policy for recovery actions

### Pre-approved — may be executed automatically, without waiting for sign-off
These are reversible, non-production-changing actions:
- Creating or updating an **incident issue** (timeline, findings, RCA).
- Posting **comments / analysis** on issues or pull requests.
- Opening a **draft pull request** containing a candidate fix (draft only —
  opening it does not deploy anything).
- Applying or changing **labels** (e.g. `incident`, `sev2`).
- Read-only inspection of code, config, logs, metrics, and deploy history.

### Requires human approval — prepare it, then STOP and ask before executing
These change production or are hard to undo:
- **Merging any pull request** to `main` (merging triggers an automatic
  production deploy).
- **Rolling back, redeploying, or otherwise changing the running production
  deployment.**
- **Restarting, scaling, or killing** production pods/services (including the
  orders-api deployment and the shared database).
- **Changing the database** or its configuration (orders-db is shared with
  reporting-worker; database changes are cross-team).
- **Closing or resolving** the incident.
- **Deleting branches**, force-pushing, or any irreversible git operation.

If an action is not clearly on the pre-approved list, treat it as requiring
approval.

## Deploy mechanism
Merging to `main` auto-deploys to production within ~2 minutes via the
`deploy-prod` GitHub Action. There is no separate deploy step to gate — the
merge IS the deploy. Draft PRs and un-merged PRs do not deploy.

## Escalation
Page the secondary on-call for any Sev1, any database change, or any action
that would affect reporting-worker.
