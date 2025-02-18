"""Configuration for RAG testing interface."""

from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class RAGTestingConfig:
    """Configuration for RAG testing interface."""
    
    # Vector store settings
    supported_vector_stores = [
        "chroma",
        "faiss",
        "milvus"
    ]
    default_vector_store = "chroma"
    
    # Document processing
    supported_file_types = [
        "txt",
        "md",
        "pdf",
        "doc",
        "docx"
    ]
    max_file_size_mb = 10
    
    # Embedding settings
    default_embedding_model = "text-embedding-ada-002"
    chunk_size = 1000
    chunk_overlap = 200
    
    # Agent settings
    default_agent_model = "gpt-4-1106-preview"
    temperature = 0.7
    max_tokens = 2000
    
    # UI settings
    max_chat_history = 50
    max_sources_display = 3
    
    # Performance settings
    batch_size = 10
    max_concurrent_requests = 5
    
    @classmethod
    def get_vector_store_options(cls) -> Dict[str, Any]:
        """Get vector store configuration options."""
        return {
            "chroma": {
                "name": "Chroma",
                "description": "Persistent, easy to use vector store",
                "config": {
                    "persist_directory": "./chroma_db"
                }
            },
            "faiss": {
                "name": "FAISS",
                "description": "High-performance in-memory vector store",
                "config": {
                    "index_type": "IndexFlatIP"
                }
            },
            "milvus": {
                "name": "Milvus",
                "description": "Distributed vector database",
                "config": {
                    "host": "localhost",
                    "port": 19530
                }
            }
        }
    
    @classmethod
    def get_embedding_models(cls) -> Dict[str, str]:
        """Get available embedding models."""
        return {
            "text-embedding-ada-002": "OpenAI Ada 002 (Default)",
            "text-embedding-3-small": "OpenAI 3 Small",
            "text-embedding-3-large": "OpenAI 3 Large"
        }
    
    @classmethod
    def get_agent_models(cls) -> Dict[str, str]:
        """Get available agent models."""
        return {
            "gpt-4-1106-preview": "GPT-4 Turbo",
            "gpt-4": "GPT-4",
            "gpt-3.5-turbo": "GPT-3.5 Turbo"
        }
