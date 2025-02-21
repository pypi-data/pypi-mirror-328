"""Exceptions for CRUD operations."""


class DatabaseError(Exception):
    """Base class for database errors."""
    pass


class ValidationError(Exception):
    """Raised when record data is invalid."""
    pass 