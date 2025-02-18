"""
Vector store integration for Text2SQL module.
"""
from typing import List, Dict, Optional
import numpy as np
from datetime import datetime
from pathlib import Path

from adpa.text2sql.types import (
    QueryContext,
    QueryResult,
    QueryMetrics
)

class VectorStore:
    """Vector store for query embeddings and schema information."""
    
    def __init__(
        self,
        store_path: Optional[str] = None,
        dimension: int = 768,
        max_entries: int = 10000
    ):
        """Initialize vector store.
        
        Args:
            store_path: Path to store vectors. If None, uses in-memory storage
            dimension: Embedding dimension
            max_entries: Maximum number of entries to store
        """
        self.store_path = Path(store_path) if store_path else None
        self.dimension = dimension
        self.max_entries = max_entries
        self.vectors = np.zeros((0, dimension))
        self.metadata = []
        
        if store_path and Path(store_path).exists():
            self.load()
    
    def add_entry(
        self,
        query: str,
        sql: str,
        embedding: np.ndarray,
        context: Optional[QueryContext] = None,
        metrics: Optional[QueryMetrics] = None
    ) -> None:
        """Add a new entry to the store.
        
        Args:
            query: Natural language query
            sql: Generated SQL query
            embedding: Query embedding vector
            context: Optional query context
            metrics: Optional query metrics
        """
        if embedding.shape[0] != self.dimension:
            raise ValueError(
                f"Expected embedding dimension {self.dimension}, "
                f"got {embedding.shape[0]}"
            )
        
        # Add vector
        self.vectors = np.vstack([self.vectors, embedding])
        
        # Add metadata
        self.metadata.append({
            "query": query,
            "sql": sql,
            "context": context.dict() if context else {},
            "metrics": metrics.dict() if metrics else {},
            "timestamp": datetime.now().isoformat()
        })
        
        # Enforce size limit
        if len(self.metadata) > self.max_entries:
            self.vectors = self.vectors[-self.max_entries:]
            self.metadata = self.metadata[-self.max_entries:]
        
        # Save if path specified
        if self.store_path:
            self.save()
    
    def search(
        self,
        embedding: np.ndarray,
        k: int = 5,
        threshold: float = 0.8
    ) -> List[Dict]:
        """Search for similar queries.
        
        Args:
            embedding: Query embedding to search for
            k: Number of results to return
            threshold: Similarity threshold (0-1)
            
        Returns:
            List of similar entries with metadata
        """
        if len(self.vectors) == 0:
            return []
        
        # Calculate cosine similarities
        similarities = np.dot(self.vectors, embedding) / (
            np.linalg.norm(self.vectors, axis=1) * np.linalg.norm(embedding)
        )
        
        # Get top k indices above threshold
        indices = np.where(similarities >= threshold)[0]
        if len(indices) == 0:
            return []
        
        top_k_indices = indices[np.argsort(similarities[indices])[-k:]]
        
        # Return results with similarities
        results = []
        for idx in top_k_indices:
            result = self.metadata[idx].copy()
            result["similarity"] = float(similarities[idx])
            results.append(result)
        
        return list(reversed(results))
    
    def save(self) -> None:
        """Save vectors and metadata to disk."""
        if not self.store_path:
            return
        
        # Create directory if needed
        self.store_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save vectors
        np.save(
            str(self.store_path.with_suffix(".npy")),
            self.vectors
        )
        
        # Save metadata
        import json
        with open(str(self.store_path.with_suffix(".json")), "w") as f:
            json.dump({
                "dimension": self.dimension,
                "max_entries": self.max_entries,
                "metadata": self.metadata
            }, f, indent=2)
    
    def load(self) -> None:
        """Load vectors and metadata from disk."""
        if not self.store_path:
            return
        
        vector_path = self.store_path.with_suffix(".npy")
        metadata_path = self.store_path.with_suffix(".json")
        
        if not vector_path.exists() or not metadata_path.exists():
            return
        
        # Load vectors
        self.vectors = np.load(str(vector_path))
        
        # Load metadata
        import json
        with open(str(metadata_path)) as f:
            data = json.load(f)
            self.dimension = data["dimension"]
            self.max_entries = data["max_entries"]
            self.metadata = data["metadata"]
    
    def clear(self) -> None:
        """Clear all entries."""
        self.vectors = np.zeros((0, self.dimension))
        self.metadata = []
        
        if self.store_path:
            self.save()
    
    def get_stats(self) -> Dict:
        """Get store statistics.
        
        Returns:
            Dictionary with store statistics
        """
        return {
            "num_entries": len(self.metadata),
            "dimension": self.dimension,
            "max_entries": self.max_entries,
            "store_path": str(self.store_path) if self.store_path else None,
            "memory_usage": {
                "vectors_mb": self.vectors.nbytes / 1024 / 1024,
                "metadata_entries": len(self.metadata)
            }
        }
