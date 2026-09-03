# orders-api

Internal order-lookup service. Exposes a small HTTP API for retrieving order
records from the orders Postgres database. Runs on Kubernetes (namespace
`orders`, deployment `orders-api`), fronted by the internal API gateway.

## Layout
- `src/app.py` — HTTP handlers (FastAPI)
- `src/db.py` — Postgres connection pool
- `src/orders.py` — order lookup logic
- `config/settings.yaml` — service configuration (pool size, timeouts)
- `incident/` — artifacts from the in-progress incident (alert, logs, deploy
  history, metrics snapshot) and the operations runbook

## Local run
`uvicorn src.app:app --port 8080` (requires a reachable `orders` Postgres and
the env vars in `config/settings.yaml`).
