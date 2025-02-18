# Vector Store Integration

Version 0.7.0

## Overview

ADPA supports multiple vector store backends for efficient similarity search and retrieval. This guide covers the available vector stores, their characteristics, and how to use them effectively.

## Supported Vector Stores

### Chroma (Default)
- **Best for**: Small to medium-sized datasets
- **Features**:
  - Persistent storage
  - Easy setup and maintenance
  - Good performance for typical use cases
  - Supports metadata filtering
- **Use when**:
  - You need a simple, reliable vector store
  - Your dataset is < 1 million documents
  - You want persistent storage without complex setup

### FAISS
- **Best for**: Large-scale similarity search
- **Features**:
  - High-performance in-memory search
  - Multiple index types for different use cases
  - Optimized for dense vectors
- **Use when**:
  - You need fast similarity search
  - Memory is not a constraint
  - Your dataset is large but static

### Milvus
- **Best for**: Distributed, large-scale deployments
- **Features**:
  - Horizontal scalability
  - High availability
  - Rich query operators
  - Real-time search
- **Use when**:
  - You need a distributed vector store
  - Your dataset is very large (>10M documents)
  - You require high availability

## Configuration

### Basic Setup
```python
from adpa.knowledge import EnhancedVectorStore, VectorStoreConfig, VectorStoreType

config = VectorStoreConfig(
    store_type=VectorStoreType.CHROMA,
    persist_directory="./vector_store",
    embedding_model="text-embedding-ada-002"
)

store = EnhancedVectorStore(config)
```

### Environment Variables
```env
VECTOR_STORE_TYPE=chroma  # Options: chroma, faiss, milvus
EMBEDDING_MODEL=text-embedding-ada-002
PERSIST_DIRECTORY=./vector_store
```

## Usage Examples

### Adding Documents
```python
# Add single document
store.add_documents(
    "This is a sample document",
    metadata={"source": "example"}
)

# Add multiple documents
docs = [
    "Document 1 content",
    "Document 2 content"
]
store.add_documents(docs)
```

### Searching
```python
# Basic similarity search
results = store.similarity_search(
    "sample query",
    k=5  # Number of results
)

# Search with metadata filter
results = store.similarity_search(
    "sample query",
    filter={"source": "example"}
)
```

### Hybrid Search
```python
# Combine vector similarity with keyword search
results = store.hybrid_search(
    "sample query",
    hybrid_search_weight=0.5  # Balance between vector and keyword search
)
```

## Performance Considerations

### Chroma
- **Optimal Configuration**:
  ```python
  config = VectorStoreConfig(
      store_type=VectorStoreType.CHROMA,
      chunk_size=512,  # Optimal for most use cases
      chunk_overlap=50,  # ~10% of chunk size
      similarity_top_k=5,
      hybrid_search_weight=0.3  # Favor vector similarity over keyword matching
  )
  ```
- **Scaling Guidelines**:
  - Up to 1M documents: Direct usage
  - 1M-5M documents: Consider sharding
  - >5M documents: Consider FAISS or Milvus
- **Memory Usage**:
  - ~500 bytes per embedding
  - ~2GB RAM for 1M documents
  - Consider SSD for persistence

### FAISS
- **Index Types**:
  ```python
  # Flat index - best accuracy, slower search
  config = VectorStoreConfig(
      store_type=VectorStoreType.FAISS,
      index_type="IndexFlatIP",
      dimension=768
  )
  
  # IVF index - faster search, slight accuracy trade-off
  config = VectorStoreConfig(
      store_type=VectorStoreType.FAISS,
      index_type="IndexIVFFlat",
      n_lists=100,  # Number of Voronoi cells
      n_probes=10   # Number of cells to search
  )
  ```
- **Memory Management**:
  - Pre-allocate memory: `faiss.set_mem_size_flag(gb_ram * 1024 * 1024 * 1024)`
  - Monitor memory: `faiss.get_mem_size_flag()`
- **Performance Tips**:
  - Use batch processing for insertions
  - Adjust `n_probes` based on accuracy needs
  - Consider GPU acceleration for large datasets

### Milvus
- **Deployment Options**:
  ```python
  # Standalone deployment
  config = VectorStoreConfig(
      store_type=VectorStoreType.MILVUS,
      host="localhost",
      port=19530,
      consistency_level="Strong"
  )
  
  # Cluster deployment
  config = VectorStoreConfig(
      store_type=VectorStoreType.MILVUS,
      hosts=["node1:19530", "node2:19530"],
      consistency_level="Bounded",
      replica_number=2
  )
  ```
- **Partitioning Strategy**:
  ```python
  # Create partitioned collection
  store.create_partition("2024_data")
  store.create_partition("2023_data")
  
  # Insert into specific partition
  store.add_documents(
      docs_2024,
      partition_name="2024_data"
  )
  
  # Search specific partitions
  results = store.similarity_search(
      "query",
      partition_names=["2024_data"]
  )
  ```
- **Consistency Levels**:
  - `Strong`: Immediate consistency, higher latency
  - `Bounded`: Staleness < 1 second
  - `Session`: Changes visible in same session
  - `Eventually`: Lowest latency, eventual consistency

## Advanced Usage

### Hybrid Search
```python
# Combine vector similarity with keyword search
results = store.hybrid_search(
    query="machine learning research papers",
    hybrid_search_weight=0.7,  # 70% vector, 30% keyword
    filter={"year": 2024}
)
```

### Metadata Filtering
```python
# Complex metadata filters
results = store.similarity_search(
    "deep learning",
    filter={
        "year": {"$gte": 2023},
        "category": {"$in": ["AI", "ML"]},
        "citations": {"$gt": 10}
    }
)
```

### Batch Operations
```python
# Efficient batch processing
docs = [
    Document(content="...", metadata={"id": 1}),
    Document(content="...", metadata={"id": 2})
]

# Add in batches
for batch in chunked(docs, 100):
    store.add_documents(batch)

# Batch search
queries = ["query1", "query2", "query3"]
results = store.batch_similarity_search(
    queries,
    k=5,
    batch_size=10
)
```

## Monitoring and Observability

### Health Checks
```python
# Basic health check
status = store.health_check()
print(f"Store Status: {status}")

# Detailed diagnostics
diagnostics = store.get_diagnostics()
print(f"Index Size: {diagnostics['index_size']}")
print(f"Memory Usage: {diagnostics['memory_usage']}")
print(f"Query Latency (p95): {diagnostics['query_latency_p95']}")
```

### Performance Metrics
```python
# Enable performance tracking
store.enable_metrics()

# Get performance metrics
metrics = store.get_metrics()
print(f"Average Query Time: {metrics['avg_query_time']}")
print(f"Index Size: {metrics['index_size']}")
print(f"Memory Usage: {metrics['memory_usage']}")
```

### Logging and Debugging
```python
import logging

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("vector_store")

# Add custom handler
handler = logging.FileHandler("vector_store.log")
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)
```

## Testing

### Unit Tests
```python
def test_vector_store_basic():
    store = EnhancedVectorStore(config)
    store.add_documents("test document")
    results = store.similarity_search("test")
    assert len(results) > 0
```

### Integration Tests
```bash
# Run all vector store tests
robot tests/robot/vector_stores.robot

# Run specific test categories
robot -i basic tests/robot/vector_stores.robot
robot -i performance tests/robot/vector_stores.robot
robot -i stress tests/robot/vector_stores.robot
```

### Performance Testing
```python
# Measure insertion performance
start_time = time.time()
store.add_documents(large_dataset)
insert_time = time.time() - start_time

# Measure query performance
latencies = []
for query in test_queries:
    start_time = time.time()
    store.similarity_search(query)
    latencies.append(time.time() - start_time)

print(f"P95 Latency: {np.percentile(latencies, 95)}")
```

## Troubleshooting

### Common Issues

1. **High Memory Usage**
   ```python
   # Monitor memory usage
   import psutil
   
   def check_memory():
       process = psutil.Process()
       memory_info = process.memory_info()
       print(f"RSS: {memory_info.rss / 1024 / 1024} MB")
       print(f"VMS: {memory_info.vms / 1024 / 1024} MB")
   ```

2. **Slow Queries**
   ```python
   # Profile query performance
   import cProfile
   
   profiler = cProfile.Profile()
   profiler.enable()
   store.similarity_search("slow query")
   profiler.disable()
   profiler.print_stats(sort='cumulative')
   ```

3. **Index Corruption**
   ```python
   # Verify index integrity
   store.verify_index()
   
   # Rebuild index if necessary
   store.rebuild_index()
   ```

## Best Practices

1. **Data Preparation**
   ```python
   # Normalize text
   from adpa.utils.text import normalize_text
   
   normalized_docs = [normalize_text(doc) for doc in docs]
   store.add_documents(normalized_docs)
   ```

2. **Resource Management**
   ```python
   # Use context manager for cleanup
   with EnhancedVectorStore(config) as store:
       store.add_documents(docs)
       results = store.similarity_search("query")
   ```

3. **Error Handling**
   ```python
try:
       store.add_documents(docs)
   except VectorStoreError as e:
       logger.error(f"Failed to add documents: {e}")
       # Implement retry logic or fallback
   ```

## Next Steps
- Explore [RAG Implementation Guide](guides/rag-and-vectors.md)
- Check [Performance Optimization Guide](guides/performance.md)
- Review [Integration Examples](guides/integration.md)

## Vector Store Implementation

Version: 1.0.0

## Overview
The ADPA Framework includes a powerful vector store implementation using Elasticsearch for efficient semantic search capabilities.

## Features
- Semantic search using dense vectors
- Hybrid search combining semantic and keyword matching
- Advanced metadata filtering
- Multi-language support (English and German)
- Comprehensive answer generation

## Components

### Search Types
1. **Semantic Search**
   - Pure vector similarity search
   - Uses sentence transformers for embedding generation
   - Cosine similarity scoring

2. **Hybrid Search**
   - Combines vector similarity with keyword matching
   - Configurable weights for semantic vs keyword importance
   - Enhanced relevance scoring

3. **Advanced Hybrid Search**
   - All features of hybrid search
   - Metadata filtering capabilities
   - Category and type-based filtering

### Answer Generation
- Automatic answer compilation from search results
- Context-aware formatting based on query type
- Source attribution and metadata inclusion
- Multi-language support

## Implementation Details

### Elasticsearch Configuration
```json
{
    "mappings": {
        "properties": {
            "text": {"type": "text"},
            "vector_field": {
                "type": "dense_vector",
                "dims": 384,
                "index": true,
                "similarity": "cosine"
            }
        }
    }
}
```

### Document Structure
```json
{
    "text": "Document content",
    "vector_field": [...],  // 384-dimensional vector
    "metadata": {
        "category": "Category name",
        "type": "Content type"
    }
}
```

## Usage Examples

### Basic Search
```python
from elasticsearch_service import ElasticsearchService

es_service = ElasticsearchService()
results = es_service.vector_search("What is machine learning?", top_k=5)
```

### Hybrid Search
```python
results = es_service.hybrid_search(
    query="AI applications in healthcare",
    keyword="neural networks",
    semantic_weight=0.7,
    keyword_weight=0.3
)
```

### Advanced Search with Metadata
```python
results = es_service.hybrid_search(
    query="machine learning applications",
    keyword="neural networks",
    semantic_weight=0.7,
    keyword_weight=0.3,
    filter_metadata={
        "category": "AI",
        "type": "technical"
    }
)
```

## User Interface
The implementation includes a Streamlit-based user interface (`streamlit_app/search_app.py`) with the following features:
- Document management (single, batch, file upload)
- Multiple search types
- Configurable search parameters
- Comprehensive answer generation
- Result visualization and explanation

## Dependencies
- Elasticsearch 8.x
- sentence-transformers
- streamlit
- pandas
- requests

## Recent Updates
- Added comprehensive answer generation
- Added multi-language support (English/German)
- Enhanced metadata filtering
- Improved result visualization
- Added document count tracking
