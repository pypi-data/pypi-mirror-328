# Manticore CockroachDB

A professional-grade Python wrapper for CockroachDB, developed and maintained by Manticore Technologies. This package provides a clean and efficient interface for working with CockroachDB, featuring CRUD operations, schema migrations, and transaction management.

## Features

- 🔒 Secure connection management with SSL support
- 🔄 Automatic transaction retries with exponential backoff
- 📦 Easy CRUD operations with schema validation
- 🔧 Database migrations with versioning
- 🎯 Type hints and comprehensive test coverage
- 📝 Detailed logging and error handling

## Installation

```bash
pip install manticore-cockroachdb
```

## Quick Start

```python
from manticore_cockroachdb import init_db
from manticore_cockroachdb.crud import Table

# Initialize database connection
init_db("postgresql://user:password@host:26257/dbname?sslmode=verify-full")

# Define a table schema
users = Table("users", {
    "id": "UUID PRIMARY KEY DEFAULT gen_random_uuid()",
    "name": "TEXT NOT NULL",
    "email": "TEXT UNIQUE NOT NULL",
    "status": "TEXT DEFAULT 'active'",
    "created_at": "TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP"
})

# Create a record
user = users.create({
    "name": "Alice",
    "email": "alice@example.com"
})

# Read a record
found = users.read(user["id"])

# Update a record
updated = users.update(user["id"], {
    "status": "inactive"
})

# Delete a record
users.delete(user["id"])
```

## Database Migrations

```python
from manticore_cockroachdb.migrations import Migration, migrate

class CreateUsersTable(Migration):
    version = "20240217_01"
    name = "create_users_table"
    
    def up(self, cur):
        cur.execute("""
            CREATE TABLE users (
                id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
            )
        """)
    
    def down(self, cur):
        cur.execute("DROP TABLE users")

# Apply migrations
migrate([CreateUsersTable()])
```

## Transaction Management

```python
from manticore_cockroachdb import run_transaction

def transfer_funds(conn, from_id, to_id, amount):
    with conn.cursor() as cur:
        # Debit source account
        cur.execute(
            "UPDATE accounts SET balance = balance - %s WHERE id = %s",
            (amount, from_id)
        )
        # Credit destination account
        cur.execute(
            "UPDATE accounts SET balance = balance + %s WHERE id = %s",
            (amount, to_id)
        )

# Run with automatic retries
run_transaction(lambda conn: transfer_funds(conn, "id1", "id2", 100))
```

## Development

1. Clone the repository:
```bash
git clone https://github.com/manticore-tech/manticore-cockroachdb.git
cd manticore-cockroachdb
```

2. Install development dependencies:
```bash
pip install -e ".[dev]"
```

3. Set up test database:
```bash
# Start a local CockroachDB instance
docker run -d \
  --name=cockroach \
  -p 26257:26257 \
  -p 8080:8080 \
  cockroachdb/cockroach:latest \
  start-single-node \
  --insecure

# Set environment variable for tests
export DATABASE_URL="postgresql://root@localhost:26257/defaultdb?sslmode=disable"
```

4. Run tests:
```bash
pytest
```

5. Format code:
```bash
black .
isort .
```

6. Run type checks:
```bash
mypy .
```

7. Build package:
```bash
python -m build
```

8. Run tests with coverage:
```bash
pytest --cov=manticore_cockroachdb --cov-report=term-missing
```

## Test Coverage

The test suite aims to provide comprehensive coverage of the codebase. Current coverage levels:

- `__init__.py`: 100% - Core module initialization
- `exceptions.py`: 100% - Exception classes
- `database.py`: 25% - Database connection management
  - Missing: Error paths and edge cases
  - TODO: Add tests for connection pool management
- `crud/table.py`: 11% - Table operations
  - Missing: Error handling paths
  - TODO: Add tests for schema validation
  - TODO: Add tests for index management
- `crud/__init__.py`: 50% - High-level CRUD operations
  - Missing: Error handling paths
  - TODO: Add tests for bulk operations

To improve coverage:

1. Run tests with coverage report:
```bash
pytest --cov=manticore_cockroachdb --cov-report=html
```

2. View detailed coverage report:
```bash
open htmlcov/index.html
```

3. Focus on adding tests for:
   - Error handling paths
   - Edge cases
   - Concurrent operations
   - Connection pool management
   - Schema validation
   - Index management
   - Bulk operations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - Copyright (c) 2024 Manticore Technologies 