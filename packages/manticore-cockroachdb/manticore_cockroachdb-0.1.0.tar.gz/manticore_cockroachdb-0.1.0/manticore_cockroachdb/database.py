"""Database connection management."""

import logging
import os
import random
import ssl
import time
from typing import Any, Callable, Optional
from urllib.parse import urlparse

import psycopg
from psycopg.errors import SerializationFailure
from psycopg.rows import namedtuple_row

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global connection
_conn: Optional[psycopg.Connection] = None


def get_ssl_context() -> ssl.SSLContext:
    """Create SSL context for CockroachDB Cloud.
    
    Returns:
        SSL context configured for CockroachDB Cloud
    """
    ssl_context = ssl.create_default_context()
    ssl_context.verify_mode = ssl.CERT_REQUIRED
    ssl_context.check_hostname = True
    return ssl_context


def get_dsn() -> str:
    """Get database connection string from environment.
    
    Returns:
        Database connection string
        
    Raises:
        ValueError: If DATABASE_URL environment variable not set
    """
    dsn = os.environ.get("DATABASE_URL")
    if not dsn:
        raise ValueError("DATABASE_URL environment variable not set")
    return dsn


def create_database(dsn: str, db_name: str = "test_db") -> None:
    """Create database if it doesn't exist.

    Args:
        dsn: Database connection string
        db_name: Name of database to create
    """
    # Parse the DSN to get components
    parsed = urlparse(dsn)

    # Create a DSN without database name for initial connection
    admin_dsn = f"{parsed.scheme}://{parsed.netloc}/defaultdb"
    if parsed.query:
        admin_dsn += f"?{parsed.query}"

    try:
        # Connect to default database
        with psycopg.connect(admin_dsn) as conn:
            conn.autocommit = True
            with conn.cursor() as cur:
                # Check if database exists
                cur.execute(
                    "SELECT 1 FROM pg_database WHERE datname = %s",
                    (db_name,)
                )
                exists = cur.fetchone() is not None

                if not exists:
                    # Create database
                    cur.execute(f'CREATE DATABASE "{db_name}"')
                    logger.info(f"Created database {db_name}")
                else:
                    logger.info(f"Database {db_name} already exists")
    except Exception as e:
        logger.error(f"Failed to create database: {e}")
        raise


def get_conn() -> psycopg.Connection:
    """Get database connection.

    Returns:
        Database connection

    Raises:
        RuntimeError: If database not initialized
    """
    global _conn
    if _conn is None:
        raise RuntimeError("Database not initialized")
    return _conn


def init_db(dsn: Optional[str] = None, db_name: str = "test_db") -> None:
    """Initialize database connection.

    Args:
        dsn: Optional database connection string
        db_name: Name of database to use/create
    """
    global _conn
    if dsn is None:
        dsn = get_dsn()

    try:
        # Create database if needed
        create_database(dsn, db_name)

        # Parse the DSN and replace database name
        parsed = urlparse(dsn)
        base_dsn = f"{parsed.scheme}://{parsed.netloc}/{db_name}"
        if parsed.query:
            base_dsn += f"?{parsed.query}"

        # Connect with application name and SSL
        conninfo = psycopg.conninfo.make_conninfo(
            base_dsn,
            application_name="manticore-trading",
            sslmode="verify-full"
        )
        _conn = psycopg.connect(conninfo, row_factory=namedtuple_row)
        logger.info(f"Connected to database {db_name}")

    except Exception as e:
        logger.error(f"Failed to connect to database: {e}")
        raise


def close_db() -> None:
    """Close database connection."""
    global _conn
    if _conn:
        _conn.close()
        _conn = None
        logger.info("Closed database connection")


def run_transaction(
    op: Callable[[psycopg.Connection], Any],
    max_retries: int = 3
) -> Any:
    """Run operation in a transaction with retry logic.

    Args:
        op: Operation to run
        max_retries: Maximum number of retry attempts

    Returns:
        Operation result

    Raises:
        ValueError: If transaction fails after max retries
    """
    conn = get_conn()

    for retry in range(1, max_retries + 1):
        try:
            with conn.transaction():
                return op(conn)

        except SerializationFailure as e:
            logger.debug(
                f"Transaction failed (attempt {retry}/{max_retries}): {e}"
            )
            if retry == max_retries:
                raise ValueError(
                    f"Transaction failed after {max_retries} retries"
                )

            # Exponential backoff
            sleep_ms = (2**retry) * 100 * (random.random() + 0.5)
            time.sleep(sleep_ms / 1000)

        except Exception as e:
            logger.error(f"Transaction failed: {e}")
            raise
