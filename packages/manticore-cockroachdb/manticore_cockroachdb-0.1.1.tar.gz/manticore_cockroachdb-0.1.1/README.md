"""# Manticore CockroachDB Client

A high-performance, production-ready CockroachDB client library for Python with connection pooling, transaction retries, and comprehensive CRUD operations.

Copyright (c) 2024 Manticore Technologies. All rights reserved.

## Features

- Connection pooling for optimal performance
- Automatic transaction retries with exponential backoff
- Comprehensive CRUD operations with batch support
- Schema migrations with versioning and rollback support
- Type-safe operations with proper error handling
- Extensive test coverage (90%+)
- Production-ready with logging and monitoring

## Installation

```bash
pip install manticore-cockroachdb
```

For development:
```bash
pip install manticore-cockroachdb[dev]
```

## Quick Start

```python
from manticore_cockroachdb import Database

# Initialize database connection
db = Database(
    host="localhost",
    port=26257,
    database="mydb",
    user="root",
    password="",
    sslmode="disable"
)

# Create a table
db.create_table(
    "users",
    {
        "id": "UUID PRIMARY KEY DEFAULT gen_random_uuid()",
        "name": "TEXT NOT NULL",
        "email": "TEXT UNIQUE NOT NULL",
        "created_at": "TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP"
    }
)

# Insert a record
user = db.insert("users", {
    "name": "John Doe",
    "email": "john@example.com"
})

# Query records
users = db.select(
    "users",
    where={"email": "john@example.com"}
)

# Update a record
updated = db.update(
    "users",
    {"name": "John Smith"},
    {"email": "john@example.com"}
)

# Delete a record
db.delete("users", {"email": "john@example.com"})

# Batch operations
users_data = [
    {"name": "User 1", "email": "user1@example.com"},
    {"name": "User 2", "email": "user2@example.com"}
]
created = db.batch_insert("users", users_data)
```

## Transaction Management

```python
# Using transaction context manager
with db.transaction() as conn:
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE accounts SET balance = balance - %s WHERE id = %s",
            [100, "acc1"]
        )
        cur.execute(
            "UPDATE accounts SET balance = balance + %s WHERE id = %s",
            [100, "acc2"]
        )

# Using transaction with retry logic
def transfer_funds(conn, from_id, to_id, amount):
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE accounts SET balance = balance - %s WHERE id = %s",
            [amount, from_id]
        )
        cur.execute(
            "UPDATE accounts SET balance = balance + %s WHERE id = %s",
            [amount, to_id]
        )

db.run_in_transaction(lambda conn: transfer_funds(conn, "acc1", "acc2", 100))
```

## Schema Migrations

```python
from manticore_cockroachdb import Database, Migrator

db = Database()
migrator = Migrator(db)

# Create a migration
migrator.create_migration(
    "create_users",
    """
    CREATE TABLE users (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    """,
    "DROP TABLE users"
)

# Apply migrations
migrator.migrate()  # Apply all pending migrations
migrator.migrate(target_version=1)  # Apply up to version 1
migrator.migrate(target_version=0)  # Revert all migrations
```

## Development

1. Clone the repository:
```bash
git clone https://github.com/manticore-tech/manticore-cockroachdb.git
cd manticore-cockroachdb
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install development dependencies:
```bash
pip install -e .[dev]
```

4. Run tests:
```bash
pytest tests/
```

## License

This software is proprietary and confidential. Copyright (c) 2024 Manticore Technologies. All rights reserved.

## Support

For enterprise support, please contact support@manticoretech.com or visit our website at https://manticoretech.com.

For bug reports and feature requests, please open an issue on our GitHub repository.""" 