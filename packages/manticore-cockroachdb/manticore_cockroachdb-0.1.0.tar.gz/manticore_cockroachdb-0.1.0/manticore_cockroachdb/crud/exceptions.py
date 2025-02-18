"""Exceptions for CRUD operations."""


class DatabaseError(Exception):
    """Base class for database errors."""

    pass


class ValidationError(Exception):
    """Raised when data validation fails."""

    pass


class NotFoundError(DatabaseError):
    """Raised when a record is not found."""

    pass


class DuplicateError(DatabaseError):
    """Raised when a duplicate record is found."""

    pass
