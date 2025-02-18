"""
Query history management for Text2SQL module.
"""
from typing import List, Dict, Optional
from datetime import datetime
import json
from pathlib import Path

from adpa.text2sql.types import (
    QueryResult,
    QueryContext,
    QueryMetrics
)

class QueryHistory:
    """Manage and analyze query history."""
    
    def __init__(
        self,
        history_path: Optional[str] = None,
        max_entries: int = 1000
    ):
        """Initialize query history.
        
        Args:
            history_path: Path to store history. If None, uses in-memory storage
            max_entries: Maximum number of entries to store
        """
        self.history_path = Path(history_path) if history_path else None
        self.max_entries = max_entries
        self.entries: List[Dict] = []
        
        if history_path and Path(history_path).exists():
            self.load()
    
    def add_entry(
        self,
        natural_query: str,
        sql_query: str,
        context: Optional[QueryContext] = None,
        metrics: Optional[QueryMetrics] = None,
        result: Optional[QueryResult] = None
    ) -> None:
        """Add a new entry to history.
        
        Args:
            natural_query: Original natural language query
            sql_query: Generated SQL query
            context: Optional query context
            metrics: Optional query metrics
            result: Optional query result
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "natural_query": natural_query,
            "sql_query": sql_query,
            "context": context.dict() if context else {},
            "metrics": metrics.dict() if metrics else {},
            "result": result.dict() if result else {}
        }
        
        self.entries.insert(0, entry)
        
        # Enforce size limit
        if len(self.entries) > self.max_entries:
            self.entries.pop()
        
        # Save if path specified
        if self.history_path:
            self.save()
    
    def get_entries(
        self,
        limit: Optional[int] = None,
        offset: int = 0,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[Dict]:
        """Get history entries with filtering.
        
        Args:
            limit: Maximum number of entries to return
            offset: Number of entries to skip
            start_date: Filter entries after this date
            end_date: Filter entries before this date
            
        Returns:
            List of history entries
        """
        entries = self.entries
        
        # Apply date filters
        if start_date or end_date:
            filtered = []
            for entry in entries:
                entry_date = datetime.fromisoformat(entry["timestamp"])
                if start_date and entry_date < start_date:
                    continue
                if end_date and entry_date > end_date:
                    continue
                filtered.append(entry)
            entries = filtered
        
        # Apply pagination
        if offset:
            entries = entries[offset:]
        if limit:
            entries = entries[:limit]
        
        return entries
    
    def search(
        self,
        query: str,
        limit: int = 10,
        threshold: float = 0.5
    ) -> List[Dict]:
        """Search history for similar queries.
        
        Args:
            query: Search query
            limit: Maximum number of results
            threshold: Similarity threshold (0-1)
            
        Returns:
            List of matching entries
        """
        # Simple substring matching for now
        query = query.lower()
        results = []
        
        for entry in self.entries:
            natural = entry["natural_query"].lower()
            sql = entry["sql_query"].lower()
            
            # Calculate simple similarity score
            if query in natural or query in sql:
                score = max(
                    len(query) / len(natural) if query in natural else 0,
                    len(query) / len(sql) if query in sql else 0
                )
                
                if score >= threshold:
                    result = entry.copy()
                    result["similarity"] = score
                    results.append(result)
        
        # Sort by similarity and limit results
        results.sort(key=lambda x: x["similarity"], reverse=True)
        return results[:limit]
    
    def get_stats(self) -> Dict:
        """Get history statistics.
        
        Returns:
            Dictionary with statistics
        """
        if not self.entries:
            return {
                "total_entries": 0,
                "date_range": None,
                "common_tables": {},
                "avg_generation_time": None
            }
        
        # Calculate statistics
        dates = [datetime.fromisoformat(e["timestamp"]) for e in self.entries]
        tables = {}
        total_time = 0
        count_with_time = 0
        
        for entry in self.entries:
            # Count table usage
            if "tables" in entry.get("metrics", {}):
                for table in entry["metrics"]["tables"]:
                    tables[table] = tables.get(table, 0) + 1
            
            # Sum generation times
            if "generation_time" in entry.get("metrics", {}):
                total_time += entry["metrics"]["generation_time"]
                count_with_time += 1
        
        return {
            "total_entries": len(self.entries),
            "date_range": {
                "first": min(dates).isoformat(),
                "last": max(dates).isoformat()
            },
            "common_tables": dict(
                sorted(
                    tables.items(),
                    key=lambda x: x[1],
                    reverse=True
                )[:10]
            ),
            "avg_generation_time": (
                total_time / count_with_time if count_with_time > 0 else None
            )
        }
    
    def save(self) -> None:
        """Save history to disk."""
        if not self.history_path:
            return
        
        # Create directory if needed
        self.history_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save as JSON
        with open(str(self.history_path), "w") as f:
            json.dump({
                "max_entries": self.max_entries,
                "entries": self.entries
            }, f, indent=2)
    
    def load(self) -> None:
        """Load history from disk."""
        if not self.history_path or not self.history_path.exists():
            return
        
        # Load from JSON
        with open(str(self.history_path)) as f:
            data = json.load(f)
            self.max_entries = data["max_entries"]
            self.entries = data["entries"]
    
    def clear(self) -> None:
        """Clear all history entries."""
        self.entries = []
        
        if self.history_path:
            self.save()
