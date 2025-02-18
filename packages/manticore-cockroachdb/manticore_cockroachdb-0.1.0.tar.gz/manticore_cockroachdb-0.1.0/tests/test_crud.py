#!/usr/bin/env python3
"""Test CRUD operations."""

import logging
import os
import pytest
import time
from datetime import datetime

from manticore_cockroachdb import init_db, close_db
from manticore_cockroachdb.crud import Table
from manticore_cockroachdb.crud.exceptions import (
    ValidationError,
    DatabaseError
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

@pytest.fixture
def users_table():
    """Create a users table for testing."""
    schema = {
        "id": "UUID PRIMARY KEY DEFAULT gen_random_uuid()",
        "name": "TEXT NOT NULL",
        "email": "TEXT UNIQUE NOT NULL",
        "status": "TEXT DEFAULT 'active'",
        "created_at": "TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP",
        "updated_at": "TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP"
    }
    table = Table("users", schema)
    yield table
    # Clean up after each test
    table._drop_table()
    time.sleep(1)  # Wait for DDL to complete

def test_crud_operations(users_table):
    """Test CRUD operations."""
    # Test create
    logger.info("Testing record creation...")
    user = users_table.create({
        "name": "Test User",
        "email": "crud_test@example.com"
    })
    assert user["id"] is not None
    assert user["name"] == "Test User"
    assert user["email"] == "crud_test@example.com"
    assert user["status"] == "active"
    
    # Test read
    logger.info("Testing record retrieval...")
    found = users_table.read(user["id"])
    assert found is not None
    assert found["name"] == user["name"]
    assert found["email"] == user["email"]
    
    # Test update
    logger.info("Testing record update...")
    updated = users_table.update(user["id"], {
        "name": "Updated User",
        "status": "inactive"
    })
    assert updated is not None
    assert updated["name"] == "Updated User"
    assert updated["status"] == "inactive"
    assert updated["email"] == user["email"]
    
    # Test find
    logger.info("Testing record search...")
    results = users_table.find({"status": "inactive"})
    assert len(results) == 1
    assert results[0]["id"] == user["id"]
    
    # Test delete
    logger.info("Testing record deletion...")
    deleted = users_table.delete(user["id"])
    assert deleted is True
    
    # Verify deletion
    found = users_table.read(user["id"])
    assert found is None

def test_validation_errors(users_table):
    """Test validation error cases."""
    # Test missing required field
    with pytest.raises(ValidationError) as exc_info:
        users_table.create({
            "name": "Invalid User"
            # Missing required email
        })
    assert "Missing required fields" in str(exc_info.value)
    
    # Test unknown field
    with pytest.raises(ValidationError) as exc_info:
        users_table.create({
            "name": "Invalid User",
            "email": "test@example.com",
            "invalid_field": "value"
        })
    assert "Unknown fields" in str(exc_info.value)
    
    # Test duplicate unique field
    users_table.create({
        "name": "User 1",
        "email": "test@example.com"
    })
    with pytest.raises(DatabaseError) as exc_info:
        users_table.create({
            "name": "User 2",
            "email": "test@example.com"  # Duplicate email
        })
    assert "duplicate key value" in str(exc_info.value).lower()

def test_high_level_crud_functions(users_table):
    """Test high-level CRUD functions."""
    # Test create_record
    user = users_table.create({
        "name": "High Level User",
        "email": "highlevel@example.com"
    })
    assert user["id"] is not None
    assert user["name"] == "High Level User"
    
    # Test read_record
    found = users_table.read(user["id"])
    assert found is not None
    assert found["name"] == user["name"]
    
    # Test update_record
    updated = users_table.update(user["id"], {
        "name": "Updated High Level User"
    })
    assert updated["name"] == "Updated High Level User"
    
    # Test delete_record
    assert users_table.delete(user["id"]) is True
    
    # Test read non-existent record
    assert users_table.read(user["id"]) is None

def test_edge_cases(users_table):
    """Test edge cases for table operations."""
    # Test creating a user with unique email
    user = users_table.create({
        "name": "Edge",
        "email": "edge_case@example.com"
    })
    assert user["email"] == "edge_case@example.com"
    
    # Test creating multiple users
    for i in range(5):
        email = f"edge_user{i}@example.com"
        users_table.create({
            "name": f"User {i}",
            "email": email
        })
        time.sleep(0.1)  # Ensure distinct timestamps
    
    # Test reading non-existent user
    with pytest.raises(DatabaseError):
        users_table.read({"id": 999})
    
    # Test updating non-existent user
    with pytest.raises(DatabaseError):
        users_table.update(
            {"id": 999},
            {"name": "Updated"}
        )
    
    # Test deleting non-existent user
    with pytest.raises(DatabaseError):
        users_table.delete({"id": 999})

def test_table_operations():
    """Test table creation and schema validation."""
    # Test invalid schema
    with pytest.raises(DatabaseError):
        Table("invalid", {
            "id": "INVALID_TYPE"
        })
    
    # Test empty schema
    with pytest.raises(ValidationError):
        Table("empty", {})
    
    # Test minimal valid schema
    minimal = Table("minimal", {
        "id": "UUID PRIMARY KEY"
    })
    assert minimal is not None
    
    # Test complex schema
    complex_table = Table("complex", {
        "id": "UUID PRIMARY KEY DEFAULT gen_random_uuid()",
        "int_field": "INTEGER NOT NULL CHECK (int_field > 0)",
        "text_field": "TEXT DEFAULT 'default'",
        "bool_field": "BOOLEAN DEFAULT FALSE",
        "timestamp_field": (
            "TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP"
        )
    })
    
    # Test complex insert
    record = complex_table.create({
        "int_field": 42,
        "text_field": "custom",
        "bool_field": True
    })
    assert record["int_field"] == 42
    assert record["text_field"] == "custom"
    assert record["bool_field"] is True
    assert "timestamp_field" in record

if __name__ == "__main__":
    test_crud_operations()
