"""Order lookup logic.

NOTE: get_order was refactored in PR #47 ("Refactor get_order to reduce
duplication", merged 2026-09-02 14:38) to drop a small helper. See
incident/pr-47-diff.md for the before/after.
"""
from .db import get_conn, release_conn


def get_order(order_id: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, customer_id, status, total_cents, created_at "
        "FROM orders WHERE id = %s",
        (order_id,),
    )
    row = cur.fetchone()
    cur.close()
    return row


def list_orders_for_customer(customer_id: str, limit: int = 50):
    conn = get_conn()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT id, status, total_cents, created_at "
            "FROM orders WHERE customer_id = %s ORDER BY created_at DESC LIMIT %s",
            (customer_id, limit),
        )
        rows = cur.fetchall()
        cur.close()
        return rows
    finally:
        release_conn(conn)
