"""
Test data generator for Store Advisor testing.
"""
import random
from faker import Faker
import json
import os
from typing import List, Dict
import pandas as pd
import numpy as np

fake = Faker()

class TestDataGenerator:
    """Generate test data for Store Advisor testing."""
    
    def __init__(self):
        self.data_sizes = ["Small (<100K docs)", "Medium (100K-1M docs)", "Large (1M-10M docs)", "Very Large (>10M docs)"]
        self.update_freqs = ["Static (rarely updated)", "Daily updates", "Hourly updates", "Real-time updates"]
        self.latencies = ["High (>500ms)", "Medium (100-500ms)", "Low (<100ms)", "Very Low (<50ms)"]
        self.deployments = ["Self-hosted", "Cloud-based", "Hybrid"]
        self.budgets = ["Low (<$100/month)", "Medium ($100-$500/month)", "High ($500-$2000/month)", "Enterprise (>$2000/month)"]
    
    def generate_use_case(self) -> Dict:
        """Generate a random use case."""
        return {
            "data_size": random.choice(self.data_sizes),
            "update_frequency": random.choice(self.update_freqs),
            "query_latency": random.choice(self.latencies),
            "deployment": random.choice(self.deployments),
            "budget": random.choice(self.budgets),
            "requires_filtering": random.choice([True, False]),
            "requires_hybrid_search": random.choice([True, False]),
            "requires_reranking": random.choice([True, False])
        }
    
    def generate_test_documents(self, num_docs: int, output_dir: str):
        """Generate test documents with embeddings."""
        os.makedirs(output_dir, exist_ok=True)
        
        for i in range(num_docs):
            doc = {
                "title": fake.catch_phrase(),
                "content": fake.text(max_nb_chars=1000),
                "metadata": {
                    "author": fake.name(),
                    "date": fake.date(),
                    "category": random.choice(["technical", "business", "research"]),
                    "tags": [fake.word() for _ in range(3)]
                },
                "embedding": list(np.random.rand(384))  # Simulated embedding
            }
            
            with open(f"{output_dir}/doc_{i}.json", 'w') as f:
                json.dump(doc, f, indent=2)
    
    def generate_performance_data(self, num_samples: int) -> pd.DataFrame:
        """Generate performance test data."""
        data = {
            'store_type': [],
            'data_size': [],
            'query_latency_ms': [],
            'indexing_speed_docs_per_sec': [],
            'memory_usage_gb': [],
            'timestamp': []
        }
        
        store_types = ['chromadb', 'faiss', 'milvus', 'qdrant', 'weaviate']
        
        for _ in range(num_samples):
            store = random.choice(store_types)
            size = random.choice(self.data_sizes)
            
            # Generate realistic performance metrics based on store type and size
            base_latency = {
                'chromadb': 100,
                'faiss': 45,
                'milvus': 85,
                'qdrant': 90,
                'weaviate': 95
            }[store]
            
            size_multiplier = {
                "Small (<100K docs)": 1,
                "Medium (100K-1M docs)": 1.5,
                "Large (1M-10M docs)": 2,
                "Very Large (>10M docs)": 3
            }[size]
            
            data['store_type'].append(store)
            data['data_size'].append(size)
            data['query_latency_ms'].append(base_latency * size_multiplier * random.uniform(0.8, 1.2))
            data['indexing_speed_docs_per_sec'].append(random.randint(5000, 15000) / size_multiplier)
            data['memory_usage_gb'].append(random.uniform(2, 16) * size_multiplier)
            data['timestamp'].append(fake.date_time_this_month())
        
        return pd.DataFrame(data)
    
    def generate_config_files(self, num_configs: int, output_dir: str):
        """Generate vector store configuration files."""
        os.makedirs(output_dir, exist_ok=True)
        
        embedding_models = [
            "sentence-transformers/all-mpnet-base-v2",
            "openai/text-embedding-ada-002",
            "sentence-transformers/all-MiniLM-L6-v2"
        ]
        
        store_configs = {
            "chromadb": {
                "persist_directory": "./chroma_db",
                "collection_name": "default"
            },
            "faiss": {
                "index_type": ["IndexFlatIP", "IndexIVFFlat"],
                "store_path": "./faiss_index"
            },
            "milvus": {
                "collection_name": "default",
                "consistency_level": ["Strong", "Session", "Bounded"],
                "index_type": ["IVF_FLAT", "HNSW"]
            }
        }
        
        for i in range(num_configs):
            store_type = random.choice(list(store_configs.keys()))
            base_config = store_configs[store_type].copy()
            
            # Randomize configurable parameters
            for key, value in base_config.items():
                if isinstance(value, list):
                    base_config[key] = random.choice(value)
            
            config = {
                "store_type": store_type,
                "embedding_model": random.choice(embedding_models),
                "dimension": random.choice([384, 768, 1024]),
                "metric": random.choice(["cosine", "euclidean", "dot"]),
                **base_config
            }
            
            with open(f"{output_dir}/config_{i}.json", 'w') as f:
                json.dump(config, f, indent=2)
    
    def generate_test_suite(self, output_dir: str):
        """Generate complete test suite data."""
        # Create directory structure
        os.makedirs(f"{output_dir}/documents", exist_ok=True)
        os.makedirs(f"{output_dir}/configs", exist_ok=True)
        os.makedirs(f"{output_dir}/performance", exist_ok=True)
        
        # Generate test documents
        self.generate_test_documents(10, f"{output_dir}/documents")
        
        # Generate configurations
        self.generate_config_files(5, f"{output_dir}/configs")
        
        # Generate performance data
        perf_data = self.generate_performance_data(100)
        perf_data.to_csv(f"{output_dir}/performance/metrics.csv", index=False)
        
        # Generate use cases
        use_cases = [self.generate_use_case() for _ in range(10)]
        with open(f"{output_dir}/use_cases.json", 'w') as f:
            json.dump(use_cases, f, indent=2)
