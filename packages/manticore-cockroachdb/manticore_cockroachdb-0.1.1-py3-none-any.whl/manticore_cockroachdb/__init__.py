"""CockroachDB database wrapper.

This package provides a high-level interface for managing CockroachDB databases.
"""

from .crud import DatabaseError, Table, ValidationError
from .database import Database, Transaction
from .migration import Migration, Migrator

__version__ = "0.1.1"
__all__ = [
    "Database",
    "Transaction",
    "Migration",
    "Migrator",
    "Table",
    "DatabaseError",
    "ValidationError",
] 