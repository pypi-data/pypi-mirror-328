# Vector Store API Reference

## Overview
API documentation for the vector store components used in semantic search and similarity matching.

## Core Components

### VectorStore
```python
class VectorStore:
    def __init__(
        self,
        dimension: int,
        store_path: Optional[str] = None,
        distance_metric: str = "cosine"
    ) -> None:
        """Initialize vector store.

        Args:
            dimension: Vector dimension
            store_path: Optional path to store vectors
            distance_metric: Distance metric (cosine, l2, ip)
        """

    async def add_vectors(
        self,
        vectors: List[np.ndarray],
        metadata: List[Dict[str, Any]]
    ) -> List[str]:
        """Add vectors to store.

        Args:
            vectors: List of vectors to add
            metadata: List of metadata for each vector

        Returns:
            List of vector IDs

        Raises:
            VectorStoreError: If addition fails
        """

    async def search(
        self,
        query_vector: np.ndarray,
        k: int = 10,
        filter_metadata: Optional[Dict[str, Any]] = None
    ) -> List[Tuple[str, float, Dict[str, Any]]]:
        """Search for similar vectors.

        Args:
            query_vector: Query vector
            k: Number of results
            filter_metadata: Optional metadata filter

        Returns:
            List of (id, distance, metadata) tuples
        """

    async def delete(
        self,
        vector_ids: List[str]
    ) -> None:
        """Delete vectors from store.

        Args:
            vector_ids: List of vector IDs to delete
        """
```

### FAISSStore
```python
class FAISSStore(VectorStore):
    def __init__(
        self,
        dimension: int,
        index_type: str = "Flat",
        nlist: int = 100,
        nprobe: int = 10
    ) -> None:
        """Initialize FAISS store.

        Args:
            dimension: Vector dimension
            index_type: FAISS index type
            nlist: Number of clusters
            nprobe: Number of clusters to probe
        """

    async def build_index(
        self,
        vectors: List[np.ndarray]
    ) -> None:
        """Build FAISS index.

        Args:
            vectors: Vectors to build index from
        """

    async def save_index(
        self,
        path: str
    ) -> None:
        """Save FAISS index.

        Args:
            path: Path to save index
        """

    @classmethod
    async def load_index(
        cls,
        path: str
    ) -> 'FAISSStore':
        """Load FAISS index.

        Args:
            path: Path to load index from

        Returns:
            FAISSStore instance
        """
```

## Models

### SearchResult
```python
class SearchResult(BaseModel):
    id: str
    score: float
    vector: Optional[np.ndarray]
    metadata: Dict[str, Any]
    distance: float

    class Config:
        arbitrary_types_allowed = True
        frozen = True
```

### IndexConfig
```python
class IndexConfig(BaseModel):
    dimension: int
    metric_type: str = Field(default="cosine")
    store_type: str = Field(default="faiss")
    index_params: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        frozen = True
```

## Utility Functions

### vector_operations
```python
def normalize_vector(
    vector: np.ndarray
) -> np.ndarray:
    """Normalize vector to unit length.

    Args:
        vector: Input vector

    Returns:
        Normalized vector
    """

def compute_similarity(
    vector1: np.ndarray,
    vector2: np.ndarray,
    metric: str = "cosine"
) -> float:
    """Compute similarity between vectors.

    Args:
        vector1: First vector
        vector2: Second vector
        metric: Similarity metric

    Returns:
        Similarity score
    """
```

## Constants

### Default Configuration
```python
DEFAULT_CONFIG = {
    "dimension": 768,
    "metric": "cosine",
    "store_type": "faiss",
    "cache_size": 10000,
    "batch_size": 1000
}
```

### Index Types
```python
INDEX_TYPES = {
    "Flat": {
        "description": "Exact search",
        "params": {}
    },
    "IVF": {
        "description": "Inverted file",
        "params": {
            "nlist": 100,
            "nprobe": 10
        }
    },
    "HNSW": {
        "description": "Hierarchical NSW",
        "params": {
            "M": 16,
            "efConstruction": 200
        }
    }
}
```

## Error Types

### VectorStoreError
```python
class VectorStoreError(Exception):
    """Base error for vector store operations."""
    pass
```

### IndexError
```python
class IndexError(VectorStoreError):
    """Raised for index-related errors."""
    pass
```

## Best Practices

### 1. Performance Optimization

- Use appropriate index type
- Batch operations when possible
- Monitor memory usage
- Implement caching

### 2. Data Management

- Regular index maintenance
- Backup strategies
- Version control for indices
- Data validation

### 3. Search Quality

- Normalize vectors
- Use appropriate metrics
- Tune search parameters
- Validate results

## Examples

### Basic Usage
```python
# Initialize store
store = FAISSStore(dimension=768)

# Add vectors
vectors = [np.random.rand(768) for _ in range(1000)]
metadata = [{"id": i} for i in range(1000)]
ids = await store.add_vectors(vectors, metadata)

# Search
query = np.random.rand(768)
results = await store.search(query, k=5)
```

### Advanced Usage
```python
# Custom index configuration
config = IndexConfig(
    dimension=768,
    metric_type="cosine",
    store_type="faiss",
    index_params={
        "type": "IVF",
        "nlist": 100,
        "nprobe": 10
    }
)

# Initialize with config
store = FAISSStore(
    dimension=config.dimension,
    index_type=config.index_params["type"],
    nlist=config.index_params["nlist"],
    nprobe=config.index_params["nprobe"]
)

# Build and save index
await store.build_index(vectors)
await store.save_index("index.faiss")

# Load existing index
loaded_store = await FAISSStore.load_index("index.faiss")
