"""
Streamlit interface for vector store management.
"""
import streamlit as st
import os
from pathlib import Path
import json
from typing import Optional

from adpa.knowledge.enhanced_vectorstore import (
    EnhancedVectorStore,
    VectorStoreConfig,
    VectorStoreType,
    EmbeddingType
)

def load_existing_config() -> Optional[dict]:
    """Load existing configuration if available."""
    config_path = "config/vectorstore_config.json"
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)
    return None

def save_config(config: dict):
    """Save configuration to file."""
    os.makedirs("config", exist_ok=True)
    with open("config/vectorstore_config.json", 'w') as f:
        json.dump(config, f, indent=2)

def vector_store_management():
    """Streamlit interface for vector store management."""
    st.title("Vector Store Management")
    
    # Load existing configuration
    existing_config = load_existing_config()
    
    with st.sidebar:
        st.header("Configuration")
        
        # Vector Store Selection
        store_type = st.selectbox(
            "Vector Store Type",
            options=[t.value for t in VectorStoreType],
            index=0 if not existing_config else 
                  [t.value for t in VectorStoreType].index(
                      existing_config["store_type"]
                  )
        )
        
        # Embedding Model Selection
        embedding_type = st.selectbox(
            "Embedding Type",
            options=[t.value for t in EmbeddingType],
            index=0 if not existing_config else
                  [t.value for t in EmbeddingType].index(
                      existing_config["embedding_type"]
                  )
        )
        
        embedding_model = st.text_input(
            "Embedding Model",
            value=existing_config["embedding_model"] if existing_config
                  else "text-embedding-ada-002"
        )
        
        # Advanced Configuration
        with st.expander("Advanced Configuration"):
            chunk_size = st.number_input(
                "Chunk Size",
                min_value=100,
                max_value=8192,
                value=existing_config["chunk_size"] if existing_config else 1000
            )
            
            chunk_overlap = st.number_input(
                "Chunk Overlap",
                min_value=0,
                max_value=chunk_size,
                value=existing_config["chunk_overlap"] if existing_config else 200
            )
            
            similarity_top_k = st.number_input(
                "Similarity Top K",
                min_value=1,
                max_value=100,
                value=existing_config["similarity_top_k"] if existing_config else 5
            )
            
            reranking_top_k = st.number_input(
                "Reranking Top K",
                min_value=1,
                max_value=similarity_top_k,
                value=existing_config["reranking_top_k"] if existing_config else 3
            )
            
            hybrid_search_weight = st.slider(
                "Hybrid Search Weight",
                min_value=0.0,
                max_value=1.0,
                value=existing_config["hybrid_search_weight"] if existing_config
                      else 0.5
            )
    
    # Main content area
    tab1, tab2, tab3 = st.tabs(["Document Management", "Query Interface", "Performance Metrics"])
    
    with tab1:
        st.header("Document Management")
        
        # Document upload
        uploaded_files = st.file_uploader(
            "Upload Documents",
            accept_multiple_files=True,
            type=["txt", "md", "pdf"]
        )
        
        if uploaded_files:
            doc_paths = []
            for file in uploaded_files:
                # Save uploaded file temporarily
                path = f"temp/{file.name}"
                os.makedirs("temp", exist_ok=True)
                with open(path, "wb") as f:
                    f.write(file.getvalue())
                doc_paths.append(path)
            
            if st.button("Process Documents"):
                config = VectorStoreConfig(
                    store_type=VectorStoreType(store_type),
                    embedding_type=EmbeddingType(embedding_type),
                    persist_directory="vectorstore",
                    embedding_model=embedding_model,
                    chunk_size=chunk_size,
                    chunk_overlap=chunk_overlap,
                    similarity_top_k=similarity_top_k,
                    reranking_top_k=reranking_top_k,
                    hybrid_search_weight=hybrid_search_weight
                )
                
                vector_store = EnhancedVectorStore(config)
                with st.spinner("Processing documents..."):
                    vector_store.add_documents(doc_paths)
                st.success("Documents processed successfully!")
                
                # Clean up temporary files
                for path in doc_paths:
                    os.remove(path)
    
    with tab2:
        st.header("Query Interface")
        
        query = st.text_input("Enter your query")
        use_reranking = st.checkbox("Use Reranking", value=True)
        
        if query and st.button("Search"):
            config = VectorStoreConfig(
                store_type=VectorStoreType(store_type),
                embedding_type=EmbeddingType(embedding_type),
                persist_directory="vectorstore",
                embedding_model=embedding_model,
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
                similarity_top_k=similarity_top_k,
                reranking_top_k=reranking_top_k,
                hybrid_search_weight=hybrid_search_weight
            )
            
            vector_store = EnhancedVectorStore(config)
            with st.spinner("Searching..."):
                results = vector_store.query(
                    query,
                    num_results=similarity_top_k,
                    rerank=use_reranking
                )
            
            for i, doc in enumerate(results, 1):
                with st.expander(f"Result {i}"):
                    st.write(f"Source: {doc.metadata.get('source', 'Unknown')}")
                    st.write(f"Content: {doc.page_content}")
    
    with tab3:
        st.header("Performance Metrics")
        
        if st.button("Run Performance Test"):
            config = VectorStoreConfig(
                store_type=VectorStoreType(store_type),
                embedding_type=EmbeddingType(embedding_type),
                persist_directory="vectorstore",
                embedding_model=embedding_model,
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
                similarity_top_k=similarity_top_k,
                reranking_top_k=reranking_top_k,
                hybrid_search_weight=hybrid_search_weight
            )
            
            vector_store = EnhancedVectorStore(config)
            
            with st.spinner("Running performance test..."):
                import time
                
                # Test queries
                test_queries = [
                    "What is the main purpose of this system?",
                    "How do I configure the database?",
                    "What are the security features?"
                ]
                
                times = []
                for query in test_queries:
                    start = time.time()
                    vector_store.query(query, rerank=True)
                    times.append(time.time() - start)
                
                st.write("Average query time:", sum(times) / len(times))
                st.write("Max query time:", max(times))
                st.write("Min query time:", min(times))
    
    # Save configuration
    if st.sidebar.button("Save Configuration"):
        config = {
            "store_type": store_type,
            "embedding_type": embedding_type,
            "embedding_model": embedding_model,
            "chunk_size": chunk_size,
            "chunk_overlap": chunk_overlap,
            "similarity_top_k": similarity_top_k,
            "reranking_top_k": reranking_top_k,
            "hybrid_search_weight": hybrid_search_weight
        }
        save_config(config)
        st.sidebar.success("Configuration saved successfully!")

if __name__ == "__main__":
    vector_store_management()
