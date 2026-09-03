"""Postgres connection pool for orders-api.

A single process-wide pool is created at import time. Handlers borrow a
connection with `get_conn()` and MUST return it with `release_conn()` when
done, otherwise the pool leaks and eventually cannot hand out connections.
"""
import os
import psycopg2
from psycopg2 import pool

# Pool sizing comes from config/settings.yaml (see DB_POOL_MAX).
# maxconn is the hard ceiling; once all connections are checked out and not
# returned, getconn() blocks and then times out.
_MIN = int(os.getenv("DB_POOL_MIN", "2"))
_MAX = int(os.getenv("DB_POOL_MAX", "20"))

connection_pool = pool.ThreadedConnectionPool(
    minconn=_MIN,
    maxconn=_MAX,
    host=os.getenv("DB_HOST", "orders-db.internal"),
    dbname=os.getenv("DB_NAME", "orders"),
    user=os.getenv("DB_USER", "orders_api"),
    connect_timeout=int(os.getenv("DB_CONNECT_TIMEOUT", "5")),
)


def get_conn():
    """Borrow a connection from the pool."""
    return connection_pool.getconn()


def release_conn(conn):
    """Return a connection to the pool. Must be called for every get_conn()."""
    connection_pool.putconn(conn)
