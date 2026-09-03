# PR #47 — "Refactor get_order to reduce duplication"

Merged 2026-09-02 14:38 UTC by rlong. Deployed 14:40 UTC.

Intent (from the PR description): "get_order and list_orders_for_customer both
open a connection with the same boilerplate. Simplifying get_order since it
only does a single fetch."

## Diff (src/orders.py)

```diff
 def get_order(order_id: str):
     conn = get_conn()
-    try:
-        cur = conn.cursor()
-        cur.execute(
-            "SELECT id, customer_id, status, total_cents, created_at "
-            "FROM orders WHERE id = %s",
-            (order_id,),
-        )
-        row = cur.fetchone()
-        cur.close()
-        return row
-    finally:
-        release_conn(conn)
+    cur = conn.cursor()
+    cur.execute(
+        "SELECT id, customer_id, status, total_cents, created_at "
+        "FROM orders WHERE id = %s",
+        (order_id,),
+    )
+    row = cur.fetchone()
+    cur.close()
+    return row
```

The refactor removed the `try/finally` that returned the borrowed connection
to the pool with `release_conn(conn)`. list_orders_for_customer (same file)
still uses the try/finally pattern.
