"""orders-api HTTP handlers."""
from fastapi import FastAPI, HTTPException
from .orders import get_order, list_orders_for_customer

app = FastAPI(title="orders-api")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/orders/{order_id}")
def read_order(order_id: str):
    row = get_order(order_id)
    if row is None:
        # Wording clarified in PR #48 (2026-09-02 14:56).
        raise HTTPException(status_code=404, detail="order not found")
    return {
        "id": row[0],
        "customer_id": row[1],
        "status": row[2],
        "total_cents": row[3],
        "created_at": str(row[4]),
    }


@app.get("/customers/{customer_id}/orders")
def read_customer_orders(customer_id: str):
    return [
        {"id": r[0], "status": r[1], "total_cents": r[2], "created_at": str(r[3])}
        for r in list_orders_for_customer(customer_id)
    ]
