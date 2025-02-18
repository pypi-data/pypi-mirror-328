"""
Database session management.
"""
from typing import Optional, Dict, Any
import logging
from contextlib import contextmanager
from sqlalchemy.orm import Session

from adpa.database.connection import DatabaseConnection

logger = logging.getLogger(__name__)

class SessionManager:
    """Manage database sessions."""
    
    def __init__(self, connection: DatabaseConnection):
        """Initialize session manager.
        
        Args:
            connection: Database connection
        """
        self.connection = connection
        self._active_sessions: Dict[str, Session] = {}
    
    @contextmanager
    def session(self, session_id: Optional[str] = None) -> Session:
        """Get a database session.
        
        Args:
            session_id: Optional session identifier
            
        Yields:
            Database session
        """
        if session_id and session_id in self._active_sessions:
            session = self._active_sessions[session_id]
            try:
                yield session
            finally:
                pass  # Keep session open
        else:
            with self.connection.session() as session:
                if session_id:
                    self._active_sessions[session_id] = session
                try:
                    yield session
                finally:
                    if session_id:
                        self._active_sessions.pop(session_id, None)
    
    def close_session(self, session_id: str) -> None:
        """Close a specific session.
        
        Args:
            session_id: Session identifier
        """
        if session_id in self._active_sessions:
            session = self._active_sessions.pop(session_id)
            session.close()
    
    def close_all_sessions(self) -> None:
        """Close all active sessions."""
        for session in self._active_sessions.values():
            session.close()
        self._active_sessions.clear()
    
    def get_active_sessions(self) -> Dict[str, Dict[str, Any]]:
        """Get information about active sessions.
        
        Returns:
            Dictionary with session information
        """
        return {
            session_id: {
                "transaction_count": len(session.transaction._connections),
                "is_active": session.is_active
            }
            for session_id, session in self._active_sessions.items()
        }
