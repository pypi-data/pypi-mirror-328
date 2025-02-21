"""Table management and CRUD operations."""

from typing import Dict, List, Optional

from ..database import Database


class Table:
    """Database table with CRUD operations."""
    
    def __init__(
        self,
        name: str,
        schema: Optional[Dict[str, str]] = None,
        if_not_exists: bool = True
    ):
        """Initialize table.
        
        Args:
            name: Table name
            schema: Column definitions {name: type}
            if_not_exists: Whether to create table only if it doesn't exist
        """
        self.name = name
        self.db = Database()
        
        if schema:
            self.db.create_table(name, schema, if_not_exists)
    
    def create(self, data: Dict) -> Dict:
        """Create a new record.
        
        Args:
            data: Record data
            
        Returns:
            Created record
        """
        return self.db.insert(self.name, data)
    
    def read(self, id: str) -> Optional[Dict]:
        """Read a record.
        
        Args:
            id: Record ID
            
        Returns:
            Record data or None if not found
        """
        results = self.db.select(self.name, where={"id": id})
        return results[0] if results else None
    
    def update(self, id: str, data: Dict) -> Optional[Dict]:
        """Update a record.
        
        Args:
            id: Record ID
            data: Update data
            
        Returns:
            Updated record
        """
        return self.db.update(self.name, data, {"id": id})
    
    def delete(self, id: str) -> bool:
        """Delete a record.
        
        Args:
            id: Record ID
            
        Returns:
            True if record was deleted
        """
        return self.db.delete(self.name, {"id": id})
    
    def list(
        self,
        where: Optional[Dict] = None,
        order_by: Optional[str] = None,
        limit: Optional[int] = None
    ) -> List[Dict]:
        """List records.
        
        Args:
            where: Filter conditions
            order_by: Order by clause
            limit: Result limit
            
        Returns:
            List of records
        """
        return self.db.select(
            self.name,
            where=where,
            order_by=order_by,
            limit=limit
        )
    
    def batch_create(self, records: List[Dict]) -> List[Dict]:
        """Create multiple records.
        
        Args:
            records: Records to create
            
        Returns:
            Created records
        """
        return self.db.batch_insert(self.name, records)
    
    def batch_update(
        self,
        records: List[Dict],
        key_column: str = "id"
    ) -> List[Dict]:
        """Update multiple records.
        
        Args:
            records: Records to update
            key_column: Column to use as key
            
        Returns:
            Updated records
        """
        return self.db.batch_update(self.name, records, key_column) 