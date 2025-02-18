#!/usr/bin/env python3
"""Test psycopg3 with CockroachDB."""

import logging
import os
import ssl
import uuid

import pytest
from psycopg.errors import SerializationFailure

from manticore_cockroachdb import (
    close_db,
    get_conn,
    get_dsn,
    get_ssl_context,
    init_db,
    run_transaction,
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def setup_db():
    """Set up test database."""
    dsn = os.getenv("DATABASE_URL")
    if not dsn:
        pytest.skip("DATABASE_URL environment variable not set")
    init_db(dsn, "test_db")
    yield
    close_db()


def test_connection_management():
    """Test database connection management."""
    # Save original environment variable
    original_dsn = os.environ.get("DATABASE_URL")

    # Test get_dsn with missing environment variable
    os.environ.pop("DATABASE_URL", None)
    with pytest.raises(ValueError):
        get_dsn()

    # Test SSL context
    ssl_context = get_ssl_context()
    assert ssl_context.verify_mode == ssl.CERT_REQUIRED
    assert ssl_context.check_hostname is True

    # Test connection with invalid DSN
    with pytest.raises(Exception):
        init_db("postgresql://invalid:invalid@invalid:26257/invalid")

    # Test get_conn without initialization
    close_db()
    with pytest.raises(RuntimeError):
        get_conn()

    # Test double close
    close_db()  # Should not raise

    # Restore environment variable
    if original_dsn:
        os.environ["DATABASE_URL"] = original_dsn


def test_transaction_retries():
    """Test transaction retry logic."""
    conn = get_conn()

    # Create test table
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE retry_test (
                id UUID PRIMARY KEY,
                counter INTEGER
            )
            """
        )

    test_id = uuid.uuid4()

    # Simulate serialization failures
    retry_count = [0]

    def failing_operation(conn):
        retry_count[0] += 1
        if retry_count[0] <= 2:  # Fail twice
            raise SerializationFailure("Simulated conflict")

        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO retry_test (id, counter)
                VALUES (%s, %s)
                """,
                (test_id, retry_count[0])
            )
            return retry_count[0]

    # Should succeed after retries
    result = run_transaction(failing_operation)
    assert result == 3  # Third attempt succeeds

    # Verify the insert
    with conn.cursor() as cur:
        cur.execute(
            "SELECT counter FROM retry_test WHERE id = %s",
            (test_id,)
        )
        assert cur.fetchone()[0] == 3

    # Test max retries exceeded
    retry_count[0] = 0
    with pytest.raises(ValueError) as exc_info:
        run_transaction(failing_operation, max_retries=2)  # Only allow 2 retries
    assert "Transaction failed after 2 retries" in str(exc_info.value)


def test_transaction_operations():
    """Test basic transaction operations."""
    conn = get_conn()

    # Create test accounts
    logger.info("Creating test accounts...")
    ids = create_accounts(conn)
    initial_balances = print_balances(conn)

    # Transfer funds
    amount = 100
    to_id = ids.pop()
    from_id = ids.pop()

    logger.info(f"Transferring ${amount} from {from_id} to {to_id}...")
    run_transaction(
        lambda conn: transfer_funds(conn, from_id, to_id, amount)
    )

    final_balances = print_balances(conn)

    # Verify balances
    from_balance = next(b[1] for b in final_balances if b[0] == from_id)
    to_balance = next(b[1] for b in final_balances if b[0] == to_id)

    initial_from = next(b[1] for b in initial_balances if b[0] == from_id)
    initial_to = next(b[1] for b in initial_balances if b[0] == to_id)

    assert from_balance == initial_from - amount
    assert to_balance == initial_to + amount

    # Test insufficient funds
    with pytest.raises(ValueError) as exc_info:
        run_transaction(
            lambda conn: transfer_funds(conn, from_id, to_id, 10000)
        )  # Too much
    assert "Insufficient funds" in str(exc_info.value)

    # Verify balances unchanged after failed transfer
    unchanged_balances = print_balances(conn)
    assert unchanged_balances == final_balances

    # Clean up
    delete_accounts(conn)


def create_accounts(conn):
    """Create test accounts table and insert sample data."""
    id1 = uuid.uuid4()
    id2 = uuid.uuid4()
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS accounts (
                id UUID PRIMARY KEY,
                balance INT
            )
            """
        )
        cur.execute(
            """
            UPSERT INTO accounts (id, balance)
            VALUES (%s, 1000), (%s, 250)
            """,
            (id1, id2)
        )
        logger.debug("create_accounts(): status message: %s", cur.statusmessage)
    return [id1, id2]


def delete_accounts(conn):
    """Delete all accounts."""
    with conn.cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS accounts")
        cur.execute("DROP TABLE IF EXISTS retry_test")
        logger.debug("delete_accounts(): status message: %s", cur.statusmessage)


def print_balances(conn):
    """Get all account balances."""
    with conn.cursor() as cur:
        balances = []
        for row in cur.execute("SELECT id, balance FROM accounts"):
            balances.append((row.id, row.balance))
        return balances


def transfer_funds(conn, from_id, to_id, amount):
    """Transfer funds between accounts."""
    with conn.cursor() as cur:
        # Check source account balance
        cur.execute(
            "SELECT balance FROM accounts WHERE id = %s",
            (from_id,)
        )
        from_balance = cur.fetchone()[0]
        if from_balance < amount:
            raise ValueError(
                f"Insufficient funds in {from_id}: "
                f"have ${from_balance}, need ${amount}"
            )

        # Perform transfer
        cur.execute(
            "UPDATE accounts SET balance = balance - %s WHERE id = %s",
            (amount, from_id)
        )
        cur.execute(
            "UPDATE accounts SET balance = balance + %s WHERE id = %s",
            (amount, to_id)
        )
        logger.debug("transfer_funds(): status message: %s", cur.statusmessage)
