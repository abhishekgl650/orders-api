# Metrics snapshot (Datadog), 2026-09-02 UTC

## orders-api: DB connections checked out (of pool_max 20)
Baseline before 14:40 hovered at 3-5 (normal). After the 14:40 deploy it
climbs steadily and does not come back down — the signature of connections
not being returned to the pool, not a traffic spike.

| Time  | Checked-out | Request rate (req/s) | 5xx ratio |
|-------|-------------|----------------------|-----------|
| 14:35 | 4           | 41                   | 0%        |
| 14:40 | 5           | 42                   | 0%        |  <- PR #47 deploy
| 14:44 | 10          | 40                   | 0%        |
| 14:48 | 17          | 43                   | 0%        |
| 14:50 | 20          | 42                   | 4%        |
| 14:52 | 20          | 42                   | 23%       |  <- alert fires
| 14:56 | 20          | 41                   | 25%       |  <- PR #48 deploy
| 15:00 | 20          | 42                   | 27%       |

Request rate is flat (~42 req/s) the whole window — this is not a load spike.
Connections climb monotonically from the 14:40 deploy until the pool is
exhausted at 14:50, then stay pinned at 20.

## reporting-worker: CPU
88% since 14:31, matching the nightly rollup job's normal schedule. Returns to
baseline when the job finishes (~15:15 most nights). Unrelated to orders-api
request handling; separate pod, shares only the database.
