"""Knowledge tools page for ADPA Framework."""
import streamlit as st
from typing import Dict, List, Optional
import yaml

from adpa.core.knowledge import KnowledgeManager
from adpa.core.types import Document, SearchQuery, SearchResult
from adpa.utils.logger import get_logger
from adpa.utils.config import load_config
from adpa.database.models.document import DocumentModel
from adpa.ui.config.database import get_db

# Setup logging
logger = get_logger(__name__)

def render_knowledge_page():
    """Render the knowledge tools page."""
    st.title("📚 Knowledge Tools")
    
    # Initialize knowledge manager
    knowledge_manager = KnowledgeManager()
    
    # Sidebar
    st.sidebar.markdown("### Knowledge Actions")
    action = st.sidebar.selectbox(
        "Select Action",
        ["Search Documents", "Upload Documents", "Manage Collections"]
    )
    
    if action == "Search Documents":
        search_documents(knowledge_manager)
    elif action == "Upload Documents":
        upload_documents(knowledge_manager)
    else:
        manage_collections(knowledge_manager)

def search_documents(knowledge_manager: KnowledgeManager):
    """Search through documents."""
    st.subheader("Search Documents")
    
    # Search configuration
    col1, col2 = st.columns(2)
    
    with col1:
        collection = st.selectbox(
            "Collection",
            knowledge_manager.list_collections()
        )
        search_type = st.selectbox(
            "Search Type",
            ["semantic", "keyword", "hybrid"]
        )
    
    with col2:
        max_results = st.number_input(
            "Max Results",
            min_value=1,
            max_value=100,
            value=10
        )
        threshold = st.slider(
            "Similarity Threshold",
            min_value=0.0,
            max_value=1.0,
            value=0.7
        )
    
    # Search query
    query = st.text_area("Search Query")
    
    if st.button("Search"):
        if not query:
            st.warning("Please enter a search query.")
            return
        
        try:
            search_config = SearchQuery(
                query=query,
                collection=collection,
                search_type=search_type,
                max_results=max_results,
                threshold=threshold
            )
            
            results = knowledge_manager.search(search_config)
            display_search_results(results)
            
        except Exception as e:
            logger.error(f"Search failed: {str(e)}")
            st.error(f"Search failed: {str(e)}")

def display_search_results(results: List[SearchResult]):
    """Display search results."""
    if not results:
        st.info("No results found.")
        return
    
    st.markdown("### Search Results")
    
    for result in results:
        with st.expander(f"Score: {result.score:.2f} - {result.document.title}"):
            st.markdown(f"**Source**: {result.document.source}")
            st.markdown(f"**Type**: {result.document.type}")
            st.markdown(f"**Created**: {result.document.created_at}")
            st.markdown("**Content**:")
            st.markdown(result.content)

def upload_documents(knowledge_manager: KnowledgeManager):
    """Upload documents to collections."""
    st.subheader("Upload Documents")
    
    collection = st.selectbox(
        "Collection",
        knowledge_manager.list_collections()
    )
    
    files = st.file_uploader(
        "Upload Documents",
        accept_multiple_files=True,
        type=["txt", "pdf", "md", "doc", "docx"]
    )
    
    if files:
        metadata = {}
        
        st.markdown("### Document Metadata")
        col1, col2 = st.columns(2)
        
        with col1:
            metadata["author"] = st.text_input("Author")
            metadata["category"] = st.text_input("Category")
        
        with col2:
            metadata["tags"] = st.text_input("Tags (comma-separated)")
            metadata["description"] = st.text_area("Description")
        
        if st.button("Upload"):
            try:
                with st.spinner("Processing documents..."):
                    for file in files:
                        knowledge_manager.add_document(
                            collection=collection,
                            file=file,
                            metadata=metadata
                        )
                    
                st.success(f"Successfully uploaded {len(files)} documents!")
                
            except Exception as e:
                logger.error(f"Upload failed: {str(e)}")
                st.error(f"Upload failed: {str(e)}")

def manage_collections(knowledge_manager: KnowledgeManager):
    """Manage document collections."""
    st.subheader("Manage Collections")
    
    # Create new collection
    st.markdown("### Create Collection")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Collection Name")
        description = st.text_area("Description")
    
    with col2:
        collection_type = st.selectbox(
            "Collection Type",
            ["vector", "text", "hybrid"]
        )
        index_type = st.selectbox(
            "Index Type",
            ["faiss", "elasticsearch", "milvus"]
        )
    
    if st.button("Create Collection"):
        try:
            knowledge_manager.create_collection(
                name=name,
                description=description,
                collection_type=collection_type,
                index_type=index_type
            )
            st.success(f"Collection '{name}' created successfully!")
            
        except Exception as e:
            logger.error(f"Failed to create collection: {str(e)}")
            st.error(f"Failed to create collection: {str(e)}")
    
    # List collections
    st.markdown("### Existing Collections")
    collections = knowledge_manager.list_collections()
    
    if not collections:
        st.info("No collections found.")
        return
    
    for collection in collections:
        with st.expander(f"Collection: {collection.name}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**Description**: {collection.description}")
                st.markdown(f"**Type**: {collection.type}")
                st.markdown(f"**Index**: {collection.index_type}")
            
            with col2:
                st.markdown(f"**Documents**: {collection.document_count}")
                st.markdown(f"**Size**: {collection.size_mb:.2f} MB")
                st.markdown(f"**Last Updated**: {collection.last_updated}")
            
            if st.button(f"Delete {collection.name}", key=collection.name):
                try:
                    knowledge_manager.delete_collection(collection.name)
                    st.success(f"Collection '{collection.name}' deleted successfully!")
                    st.rerun()
                    
                except Exception as e:
                    logger.error(f"Failed to delete collection: {str(e)}")
                    st.error(f"Failed to delete collection: {str(e)}")

def main():
    """Main entry point for knowledge tools page."""
    try:
        render_knowledge_page()
    except Exception as e:
        st.error(f"Failed to render knowledge tools page: {str(e)}")
        logger.error(f"Knowledge tools page error: {str(e)}")

if __name__ == "__main__":
    main()
