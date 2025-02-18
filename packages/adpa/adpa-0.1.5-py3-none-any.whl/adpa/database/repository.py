"""
Base repository implementation.
"""
from typing import TypeVar, Generic, Type, List, Optional, Any, Dict
import logging
from datetime import datetime
from sqlalchemy import select, func
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from adpa.database.session import SessionManager
from adpa.database.models import Base

T = TypeVar("T", bound=Base)
logger = logging.getLogger(__name__)

class BaseRepository(Generic[T]):
    """Generic repository for database operations."""
    
    def __init__(
        self,
        model: Type[T],
        session_manager: SessionManager
    ):
        """Initialize repository.
        
        Args:
            model: SQLAlchemy model class
            session_manager: Session manager instance
        """
        self.model = model
        self.session_manager = session_manager
    
    def create(self, data: Dict[str, Any]) -> T:
        """Create a new record.
        
        Args:
            data: Record data
            
        Returns:
            Created record
            
        Raises:
            SQLAlchemyError: If database operation fails
        """
        try:
            with self.session_manager.session() as session:
                record = self.model(**data)
                session.add(record)
                session.commit()
                session.refresh(record)
                return record
        except SQLAlchemyError as e:
            logger.error(f"Failed to create {self.model.__name__}: {e}")
            raise
    
    def get(self, record_id: Any) -> Optional[T]:
        """Get record by ID.
        
        Args:
            record_id: Record ID
            
        Returns:
            Record if found, None otherwise
            
        Raises:
            SQLAlchemyError: If database operation fails
        """
        try:
            with self.session_manager.session() as session:
                return session.get(self.model, record_id)
        except SQLAlchemyError as e:
            logger.error(f"Failed to get {self.model.__name__}: {e}")
            raise
    
    def get_all(
        self,
        offset: int = 0,
        limit: Optional[int] = None,
        order_by: Optional[str] = None
    ) -> List[T]:
        """Get all records with pagination.
        
        Args:
            offset: Number of records to skip
            limit: Maximum number of records to return
            order_by: Column to order by
            
        Returns:
            List of records
            
        Raises:
            SQLAlchemyError: If database operation fails
        """
        try:
            with self.session_manager.session() as session:
                query = select(self.model)
                
                if order_by:
                    query = query.order_by(order_by)
                
                query = query.offset(offset)
                
                if limit is not None:
                    query = query.limit(limit)
                
                return list(session.scalars(query))
        except SQLAlchemyError as e:
            logger.error(f"Failed to get all {self.model.__name__}: {e}")
            raise
    
    def update(
        self,
        record_id: Any,
        data: Dict[str, Any]
    ) -> Optional[T]:
        """Update a record.
        
        Args:
            record_id: Record ID
            data: Update data
            
        Returns:
            Updated record if found, None otherwise
            
        Raises:
            SQLAlchemyError: If database operation fails
        """
        try:
            with self.session_manager.session() as session:
                record = session.get(self.model, record_id)
                if record:
                    for key, value in data.items():
                        setattr(record, key, value)
                    session.commit()
                    session.refresh(record)
                return record
        except SQLAlchemyError as e:
            logger.error(f"Failed to update {self.model.__name__}: {e}")
            raise
    
    def delete(self, record_id: Any) -> bool:
        """Delete a record.
        
        Args:
            record_id: Record ID
            
        Returns:
            True if record was deleted
            
        Raises:
            SQLAlchemyError: If database operation fails
        """
        try:
            with self.session_manager.session() as session:
                record = session.get(self.model, record_id)
                if record:
                    session.delete(record)
                    session.commit()
                    return True
                return False
        except SQLAlchemyError as e:
            logger.error(f"Failed to delete {self.model.__name__}: {e}")
            raise
    
    def count(self) -> int:
        """Count total records.
        
        Returns:
            Total number of records
            
        Raises:
            SQLAlchemyError: If database operation fails
        """
        try:
            with self.session_manager.session() as session:
                return session.scalar(
                    select(func.count()).select_from(self.model)
                )
        except SQLAlchemyError as e:
            logger.error(f"Failed to count {self.model.__name__}: {e}")
            raise
    
    def exists(self, record_id: Any) -> bool:
        """Check if record exists.
        
        Args:
            record_id: Record ID
            
        Returns:
            True if record exists
            
        Raises:
            SQLAlchemyError: If database operation fails
        """
        try:
            with self.session_manager.session() as session:
                return session.get(self.model, record_id) is not None
        except SQLAlchemyError as e:
            logger.error(f"Failed to check {self.model.__name__}: {e}")
            raise
    
    def bulk_create(self, items: List[Dict[str, Any]]) -> List[T]:
        """Create multiple records.
        
        Args:
            items: List of record data
            
        Returns:
            List of created records
            
        Raises:
            SQLAlchemyError: If database operation fails
        """
        try:
            with self.session_manager.session() as session:
                records = [self.model(**item) for item in items]
                session.add_all(records)
                session.commit()
                for record in records:
                    session.refresh(record)
                return records
        except SQLAlchemyError as e:
            logger.error(f"Failed to bulk create {self.model.__name__}: {e}")
            raise
    
    def bulk_update(
        self,
        items: List[Dict[str, Any]],
        key_field: str = "id"
    ) -> List[T]:
        """Update multiple records.
        
        Args:
            items: List of record data with IDs
            key_field: Field to use as key
            
        Returns:
            List of updated records
            
        Raises:
            SQLAlchemyError: If database operation fails
        """
        try:
            with self.session_manager.session() as session:
                records = []
                for item in items:
                    record_id = item.get(key_field)
                    if record_id is None:
                        continue
                    
                    record = session.get(self.model, record_id)
                    if record:
                        for key, value in item.items():
                            if key != key_field:
                                setattr(record, key, value)
                        records.append(record)
                
                session.commit()
                for record in records:
                    session.refresh(record)
                return records
        except SQLAlchemyError as e:
            logger.error(f"Failed to bulk update {self.model.__name__}: {e}")
            raise
    
    def bulk_delete(self, record_ids: List[Any]) -> int:
        """Delete multiple records.
        
        Args:
            record_ids: List of record IDs
            
        Returns:
            Number of deleted records
            
        Raises:
            SQLAlchemyError: If database operation fails
        """
        try:
            with self.session_manager.session() as session:
                count = 0
                for record_id in record_ids:
                    record = session.get(self.model, record_id)
                    if record:
                        session.delete(record)
                        count += 1
                session.commit()
                return count
        except SQLAlchemyError as e:
            logger.error(f"Failed to bulk delete {self.model.__name__}: {e}")
            raise
