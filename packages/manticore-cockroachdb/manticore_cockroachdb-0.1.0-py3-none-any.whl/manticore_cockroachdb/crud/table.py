"""CRUD operations for database tables."""

import logging
from typing import Any, Dict, List, Optional, Tuple, Union
from datetime import datetime
import uuid
import time
from psycopg.rows import dict_row
from psycopg.errors import UndefinedTable, DuplicateTable

from ..database import get_conn
from .exceptions import DatabaseError, ValidationError
from ..exceptions import DatabaseError as ManticoreDBError

logger = logging.getLogger(__name__)

class Table:
    """Base class for database tables with CRUD operations."""
    
    def __init__(self, name: str, schema: Optional[Dict[str, str]] = None, if_not_exists: bool = True) -> None:
        """Initialize table.
        
        Args:
            name: Table name
            schema: Column definitions {name: type}. If None, table must already exist
            if_not_exists: Whether to create table only if it doesn't exist
            
        Raises:
            ValidationError: If schema is invalid
            DatabaseError: If table operations fail
        """
        self.name = name
        self.schema = schema
        
        # If schema provided, create/update table
        if schema is not None:
            if not schema:
                raise ValidationError("Schema cannot be empty")
            if if_not_exists:
                self._create_table_if_not_exists()
            else:
                self._drop_table()
                self._create_table()
    
    def _drop_table(self) -> None:
        """Drop table if it exists."""
        query = f'DROP TABLE IF EXISTS "{self.name}" CASCADE'
        
        conn = get_conn()
        with conn.cursor() as cur:
            try:
                cur.execute(query)
                conn.commit()
                logger.info(f"Dropped table {self.name}")
                # Wait for DDL to complete
                time.sleep(1)
            except Exception as e:
                conn.rollback()
                raise DatabaseError(f"Failed to drop table {self.name}: {e}")
    
    def _create_table(self) -> None:
        """Create table."""
        columns = [f"{name} {type_}" for name, type_ in self.schema.items()]
        query = f'CREATE TABLE "{self.name}" ({", ".join(columns)})'
        
        conn = get_conn()
        with conn.cursor() as cur:
            try:
                cur.execute(query)
                conn.commit()
                logger.info(f"Created table {self.name}")
                # Wait for DDL to complete
                time.sleep(1)
            except Exception as e:
                conn.rollback()
                raise DatabaseError(f"Failed to create table {self.name}: {e}")
    
    def _create_table_if_not_exists(self) -> None:
        """Create table if it doesn't exist."""
        columns = [f"{name} {type_}" for name, type_ in self.schema.items()]
        query = f'CREATE TABLE IF NOT EXISTS "{self.name}" ({", ".join(columns)})'
        
        conn = get_conn()
        with conn.cursor() as cur:
            try:
                cur.execute(query)
                conn.commit()
                logger.info(f"Created table {self.name} (if not exists)")
                # Wait for DDL to complete
                time.sleep(1)
            except Exception as e:
                conn.rollback()
                raise DatabaseError(f"Failed to create table {self.name}: {e}")
    
    def add_column(self, name: str, type_: str) -> None:
        """Add a column to the table.
        
        Args:
            name: Column name
            type_: Column type definition
        """
        query = f'ALTER TABLE "{self.name}" ADD COLUMN IF NOT EXISTS {name} {type_}'
        
        conn = get_conn()
        with conn.cursor() as cur:
            try:
                cur.execute(query)
                conn.commit()
                logger.info(f"Added column {name} to table {self.name}")
                # Wait for DDL to complete
                time.sleep(1)
            except Exception as e:
                conn.rollback()
                raise DatabaseError(f"Failed to add column {name} to table {self.name}: {e}")
    
    def drop_column(self, name: str) -> None:
        """Drop a column from the table.
        
        Args:
            name: Column name
        """
        query = f'ALTER TABLE "{self.name}" DROP COLUMN IF EXISTS {name} CASCADE'
        
        conn = get_conn()
        with conn.cursor() as cur:
            try:
                cur.execute(query)
                conn.commit()
                logger.info(f"Dropped column {name} from table {self.name}")
                # Wait for DDL to complete
                time.sleep(1)
            except Exception as e:
                conn.rollback()
                raise DatabaseError(f"Failed to drop column {name} from table {self.name}: {e}")
    
    def add_index(self, name: str, columns: List[str], unique: bool = False) -> None:
        """Add an index to the table.
        
        Args:
            name: Index name
            columns: List of column names to index
            unique: Whether the index should be unique
        """
        unique_str = "UNIQUE" if unique else ""
        query = f'CREATE {unique_str} INDEX IF NOT EXISTS "{name}" ON "{self.name}" ({", ".join(columns)})'
        
        conn = get_conn()
        with conn.cursor() as cur:
            try:
                cur.execute(query)
                conn.commit()
                logger.info(f"Created index {name} on table {self.name}")
                # Wait for DDL to complete
                time.sleep(1)
            except Exception as e:
                conn.rollback()
                raise DatabaseError(f"Failed to create index {name} on table {self.name}: {e}")
    
    def drop_index(self, name: str) -> None:
        """Drop an index from the table.
        
        Args:
            name: Index name
        """
        query = f'DROP INDEX IF EXISTS "{name}" CASCADE'
        
        conn = get_conn()
        with conn.cursor() as cur:
            try:
                cur.execute(query)
                conn.commit()
                logger.info(f"Dropped index {name}")
                # Wait for DDL to complete
                time.sleep(1)
            except Exception as e:
                conn.rollback()
                raise DatabaseError(f"Failed to drop index {name}: {e}")

    def get_schema(self) -> Dict[str, str]:
        """Get current table schema.
        
        Returns:
            Dictionary of column definitions {name: type}
        """
        query = """
            SELECT column_name, data_type, character_maximum_length,
                   numeric_precision, numeric_scale, is_nullable, column_default
            FROM information_schema.columns 
            WHERE table_name = %s
            ORDER BY ordinal_position
        """
        
        conn = get_conn()
        with conn.cursor() as cur:
            try:
                cur.execute(query, [self.name])
                columns = {}
                for row in cur.fetchall():
                    name = row[0]
                    type_parts = [row[1].upper()]
                    
                    # Add length/precision
                    if row[2]:  # character_maximum_length
                        type_parts.append(f"({row[2]})")
                    elif row[3]:  # numeric_precision
                        if row[4]:  # numeric_scale
                            type_parts.append(f"({row[3]},{row[4]})")
                        else:
                            type_parts.append(f"({row[3]})")
                    
                    # Add nullability
                    if row[5] == 'NO':
                        type_parts.append('NOT NULL')
                    
                    # Add default
                    if row[6]:
                        type_parts.append(f"DEFAULT {row[6]}")
                    
                    columns[name] = ' '.join(type_parts)
                
                return columns
            except Exception as e:
                raise DatabaseError(f"Failed to get schema for table {self.name}: {e}")

    def get_indexes(self) -> List[Dict[str, Any]]:
        """Get table indexes.
        
        Returns:
            List of index definitions
        """
        query = """
            SELECT i.relname as index_name,
                   array_agg(a.attname ORDER BY k.n) as column_names,
                   ix.indisunique as is_unique
            FROM pg_class t,
                 pg_class i,
                 pg_index ix,
                 pg_attribute a,
                 generate_subscripts(ix.indkey, 1) k(n)
            WHERE t.oid = ix.indrelid
              AND i.oid = ix.indexrelid
              AND a.attrelid = t.oid
              AND a.attnum = ix.indkey[k.n]
              AND t.relname = %s
            GROUP BY i.relname, ix.indisunique
            ORDER BY i.relname;
        """
        
        conn = get_conn()
        with conn.cursor() as cur:
            try:
                cur.execute(query, [self.name])
                return [
                    {
                        'name': row[0],
                        'columns': row[1],
                        'unique': row[2]
                    }
                    for row in cur.fetchall()
                ]
            except Exception as e:
                raise DatabaseError(f"Failed to get indexes for table {self.name}: {e}")

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create new record.
        
        Args:
            data: Record data
            
        Returns:
            Created record
            
        Raises:
            ValidationError: If data is invalid
        """
        # Validate data
        self._validate_data(data)
        
        # Add timestamps
        if 'created_at' in self.schema:
            data['created_at'] = datetime.now()
        if 'updated_at' in self.schema:
            data['updated_at'] = datetime.now()
            
        # Generate UUID if needed
        if 'id' in self.schema and 'id' not in data:
            data['id'] = uuid.uuid4()
        
        # Build query
        columns = list(data.keys())
        values = [data[col] for col in columns]
        placeholders = [f"%s" for _ in range(len(values))]
        
        query = f"INSERT INTO {self.name} ({', '.join(columns)}) VALUES ({', '.join(placeholders)}) RETURNING *"
        
        logger.debug(f"Query: {query}")
        logger.debug(f"Values: {values}")
        
        conn = get_conn()
        with conn.cursor(row_factory=dict_row) as cur:
            try:
                cur.execute(query, values)
                record = cur.fetchone()
                conn.commit()
                logger.debug(f"Created record in {self.name}: {record}")
                return dict(record)
            except Exception as e:
                conn.rollback()
                logger.error(f"Query: {query}")
                logger.error(f"Values: {values}")
                raise DatabaseError(f"Failed to create record in {self.name}: {e}")
    
    def read(self, id: Union[str, int]) -> Optional[Dict[str, Any]]:
        """Read record by ID.
        
        Args:
            id: Record ID
            
        Returns:
            Record data or None if not found
        """
        query = f"SELECT * FROM {self.name} WHERE id = %s"
        
        conn = get_conn()
        with conn.cursor(row_factory=dict_row) as cur:
            try:
                cur.execute(query, [id])
                record = cur.fetchone()
                return dict(record) if record else None
            except Exception as e:
                raise DatabaseError(f"Failed to read record from {self.name}: {e}")
    
    def update(self, id: Union[str, int], data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Update record by ID.
        
        Args:
            id: Record ID
            data: Update data
            
        Returns:
            Updated record
            
        Raises:
            ValidationError: If data is invalid
            DatabaseError: If record not found or update fails
        """
        # Validate data
        self._validate_data(data, partial=True)
        
        # Add updated timestamp
        if 'updated_at' in self.schema:
            data['updated_at'] = datetime.now()
        
        # Build query
        updates = [f"{key} = %s" for key in data.keys()]
        values = list(data.values()) + [id]
        
        query = f"UPDATE {self.name} SET {', '.join(updates)} WHERE id = %s RETURNING *"
        
        conn = get_conn()
        with conn.cursor(row_factory=dict_row) as cur:
            try:
                cur.execute(query, values)
                record = cur.fetchone()
                if not record:
                    conn.rollback()
                    raise DatabaseError(f"Record not found in {self.name} with id {id}")
                conn.commit()
                return dict(record)
            except Exception as e:
                conn.rollback()
                raise DatabaseError(f"Failed to update record in {self.name}: {e}")
    
    def delete(self, id: Union[str, int]) -> bool:
        """Delete record by ID.
        
        Args:
            id: Record ID
            
        Returns:
            True if record was deleted, False if not found
        """
        query = f"DELETE FROM {self.name} WHERE id = %s"
        
        conn = get_conn()
        with conn.cursor() as cur:
            try:
                cur.execute(query, [id])
                deleted = cur.rowcount > 0
                conn.commit()
                return deleted
            except Exception as e:
                conn.rollback()
                raise DatabaseError(f"Failed to delete record from {self.name}: {e}")
    
    def find(self, conditions: Dict[str, Any], order_by: Optional[str] = None,
            limit: Optional[int] = None, offset: Optional[int] = None) -> List[Dict[str, Any]]:
        """Find records matching conditions.
        
        Args:
            conditions: Field conditions {name: value}
            order_by: Optional order by clause
            limit: Optional result limit
            offset: Optional result offset
            
        Returns:
            List of matching records
        """
        # Build where clause
        where_clauses = [f"{key} = %s" for key in conditions.keys()]
        where_clause = " AND ".join(where_clauses) if where_clauses else "TRUE"
        
        # Build query
        query = f"SELECT * FROM {self.name} WHERE {where_clause}"
        if order_by:
            query += f" ORDER BY {order_by}"
        if limit:
            query += f" LIMIT {limit}"
        if offset:
            query += f" OFFSET {offset}"
        
        conn = get_conn()
        with conn.cursor(row_factory=dict_row) as cur:
            try:
                cur.execute(query, list(conditions.values()))
                return [dict(record) for record in cur.fetchall()]
            except Exception as e:
                raise DatabaseError(f"Failed to find records in {self.name}: {e}")
    
    def _validate_data(self, data: Dict[str, Any], partial: bool = False) -> None:
        """Validate record data against schema.
        
        Args:
            data: Record data
            partial: Whether this is a partial update
            
        Raises:
            ValidationError: If data is invalid
        """
        # Check for unknown fields
        unknown = set(data.keys()) - set(self.schema.keys())
        if unknown:
            raise ValidationError(f"Unknown fields: {unknown}")
        
        # Check required fields
        if not partial:
            missing = set()
            for field, type_def in self.schema.items():
                if field not in data and field not in {'id', 'created_at', 'updated_at'}:
                    # Field is required if it has NOT NULL and no DEFAULT
                    if 'NOT NULL' in type_def.upper() and 'DEFAULT' not in type_def.upper():
                        missing.add(field)
            
            if missing:
                raise ValidationError(f"Missing required fields: {missing}")
    
    def _format_value(self, value: Any) -> str:
        """Format value for SQL query.
        
        Args:
            value: Value to format
            
        Returns:
            Formatted value
        """
        if value is None:
            return 'NULL'
        elif isinstance(value, bool):
            return str(value).upper()
        elif isinstance(value, (int, float)):
            return str(value)
        elif isinstance(value, datetime):
            return f"'{value.isoformat()}'"
        elif isinstance(value, uuid.UUID):
            return f"'{str(value)}'"
        else:
            return f"'{str(value)}'"

    def _create_table(self, schema: Dict[str, str], if_not_exists: bool = True) -> None:
        """Create a new table with the given schema."""
        columns = [
            f"{name} {type_}"
            for name, type_ in schema.items()
        ]
        columns_str = ", ".join(columns)
        exists_clause = "IF NOT EXISTS" if if_not_exists else ""
        
        query = (
            f"CREATE TABLE {exists_clause} {self.name} "
            f"({columns_str})"
        )
        
        try:
            with self.db.transaction() as txn:
                txn.execute(query)
        except DatabaseError as e:
            raise ManticoreDBError(f"Failed to create table {self.name}: {str(e)}")

    def add_column(
        self, 
        name: str, 
        type_: str, 
        if_not_exists: bool = True
    ) -> None:
        """Add a new column to the table."""
        exists_clause = "IF NOT EXISTS" if if_not_exists else ""
        query = (
            f"ALTER TABLE {self.name} "
            f"ADD COLUMN {exists_clause} {name} {type_}"
        )
        
        try:
            with self.db.transaction() as txn:
                txn.execute(query)
        except DatabaseError as e:
            raise ManticoreDBError(
                f"Failed to add column {name} to table {self.name}: {str(e)}"
            )

    def create_index(
        self, 
        name: str, 
        columns: List[str], 
        unique: bool = False,
        if_not_exists: bool = True
    ) -> None:
        """Create an index on the specified columns."""
        unique_str = "UNIQUE" if unique else ""
        exists_clause = "IF NOT EXISTS" if if_not_exists else ""
        columns_str = ", ".join(columns)
        
        query = (
            f"CREATE {unique_str} INDEX {exists_clause} "
            f"{name} ON {self.name} ({columns_str})"
        )
        
        try:
            with self.db.transaction() as txn:
                txn.execute(query)
        except DatabaseError as e:
            raise ManticoreDBError(
                f"Failed to create index {name} on table {self.name}: {str(e)}"
            ) 