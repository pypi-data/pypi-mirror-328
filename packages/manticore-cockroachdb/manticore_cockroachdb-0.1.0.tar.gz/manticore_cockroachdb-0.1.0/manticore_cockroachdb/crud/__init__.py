"""CRUD operations for database tables."""

from typing import Dict

from .exceptions import DatabaseError, ValidationError
from .table import Table


def create_table(name: str, schema: Dict[str, str], if_not_exists: bool = True) -> Table:
    """Create a new table.

    Args:
        name: Table name
        schema: Column definitions {name: type}
        if_not_exists: Whether to create table only if it doesn't exist

    Returns:
        Table object
    """
    return Table(name, schema, if_not_exists)


def get_table(name: str) -> Table:
    """Get an existing table.

    Args:
        name: Table name

    Returns:
        Table object
    """
    return Table(name)


def create_record(table: str, data: dict) -> dict:
    """Create a new record in the table.
    
    Args:
        table: Table name
        data: Record data
        
    Returns:
        Created record
    """
    table_obj = Table(table)
    return table_obj.create(data)


def read_record(table: str, id: str) -> dict:
    """Read a record from the table.
    
    Args:
        table: Table name
        id: Record ID
        
    Returns:
        Record data
    """
    table_obj = Table(table)
    return table_obj.read(id)


def update_record(table: str, id: str, data: dict) -> dict:
    """Update a record in the table.
    
    Args:
        table: Table name
        id: Record ID
        data: Update data
        
    Returns:
        Updated record
    """
    table_obj = Table(table)
    return table_obj.update(id, data)


def delete_record(table: str, id: str) -> bool:
    """Delete a record from the table.
    
    Args:
        table: Table name
        id: Record ID
        
    Returns:
        True if record was deleted
    """
    table_obj = Table(table)
    return table_obj.delete(id)


__all__ = [
    "Table",
    "create_table",
    "get_table",
    "create_record",
    "read_record",
    "update_record",
    "delete_record",
    "DatabaseError",
    "ValidationError",
]
