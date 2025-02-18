"""Streamlit interface for testing RAG capabilities."""

import streamlit as st
import tempfile
import os
from pathlib import Path
from typing import List, Dict, Any

from adpa.knowledge import (
    EnhancedVectorStore,
    VectorStoreConfig,
    VectorStoreType
)
from adpa.research import RAGResearcher
from adpa.agents import AgentConfig
from adpa.ui.utils.state import UIState
from adpa.ui.utils.validation import InputValidator

class RAGTestingApp:
    """Streamlit interface for testing RAG capabilities."""
    
    def __init__(self):
        """Initialize the RAG testing interface."""
        self.setup_session_state()
        self.setup_config()
        
    def setup_session_state(self):
        """Initialize session state variables."""
        UIState.init_session_state()
        
    def setup_config(self):
        """Setup configuration for vector store and agent."""
        self.temp_dir = tempfile.mkdtemp()
        self.config = VectorStoreConfig(
            store_type=VectorStoreType.CHROMA,
            persist_directory=self.temp_dir,
            embedding_model="text-embedding-ada-002",
            chunk_size=1000,
            chunk_overlap=200
        )
    
    def initialize_vector_store(self):
        """Initialize or get vector store."""
        if UIState.get('vector_store') is None:
            UIState.set('vector_store', EnhancedVectorStore(self.config))
        return UIState.get('vector_store')
    
    def initialize_researcher(self):
        """Initialize or get RAG researcher."""
        if UIState.get('researcher') is None:
            store = self.initialize_vector_store()
            agent_config = AgentConfig(
                model="gpt-4-1106-preview",
                temperature=0.7,
                max_tokens=2000
            )
            UIState.set('researcher', RAGResearcher(
                vector_store=store,
                agent_config=agent_config
            ))
        return UIState.get('researcher')
    
    def process_uploaded_file(self, uploaded_file) -> bool:
        """Process an uploaded file and add it to the vector store."""
        # Validate file
        is_valid, error = InputValidator.validate_file_upload(
            uploaded_file,
            allowed_types=['txt', 'md', 'pdf'],
            max_size_mb=10
        )
        if not is_valid:
            st.error(error)
            return False

        try:
            # Create temporary file
            temp_file = Path(self.temp_dir) / uploaded_file.name
            with open(temp_file, 'wb') as f:
                f.write(uploaded_file.getvalue())
            
            # Add to vector store
            store = self.initialize_vector_store()
            store.add_documents(
                str(temp_file),
                metadata={"filename": uploaded_file.name}
            )
            
            # Add to session state
            uploaded_files = UIState.get('uploaded_files', [])
            if uploaded_file.name not in uploaded_files:
                uploaded_files.append(uploaded_file.name)
                UIState.set('uploaded_files', uploaded_files)
            
            return True
        except Exception as e:
            st.error(f"Error processing file {uploaded_file.name}: {str(e)}")
            return False
    
    def display_file_list(self):
        """Display list of uploaded files."""
        uploaded_files = UIState.get('uploaded_files', [])
        if uploaded_files:
            st.subheader("Uploaded Documents")
            for file in uploaded_files:
                st.text(f"📄 {file}")
        else:
            st.info("No documents uploaded yet.")
    
    def display_chat_history(self):
        """Display chat history."""
        for msg in UIState.get_chat_history():
            role = msg["role"]
            content = msg["content"]
            
            if role == "user":
                st.write(f"🧑 **You:** {content}")
            elif role == "assistant":
                st.write(f"🤖 **Assistant:** {content}")
                if "sources" in msg:
                    st.info("Sources:")
                    for source in msg["sources"]:
                        st.write(f"- {source}")
    
    def query_documents(self, query: str):
        """Query the documents using RAG."""
        # Validate query
        is_valid, error = InputValidator.validate_query(query)
        if not is_valid:
            st.error(error)
            return

        researcher = self.initialize_researcher()
        
        with st.spinner("Researching your query..."):
            response = researcher.research(
                query,
                return_sources=True,
                max_sources=3
            )
        
        # Add to chat history
        UIState.add_to_chat_history(
            "user",
            query
        )
        UIState.add_to_chat_history(
            "assistant",
            response.answer,
            {"sources": response.sources}
        )
    
    def render(self):
        """Render the Streamlit interface."""
        st.title("RAG Testing Interface")
        
        # Sidebar for file upload
        with st.sidebar:
            st.header("Document Upload")
            uploaded_files = st.file_uploader(
                "Upload documents",
                accept_multiple_files=True,
                type=["txt", "md", "pdf"]
            )
            
            if uploaded_files:
                for file in uploaded_files:
                    if self.process_uploaded_file(file):
                        st.success(f"Processed {file.name}")
            
            st.divider()
            self.display_file_list()
        
        # Main chat interface
        if not UIState.get('uploaded_files'):
            st.warning("Please upload some documents to start querying.")
            return
        
        self.display_chat_history()
        
        # Query input
        query = st.text_input("Ask a question about your documents")
        if query:
            self.query_documents(query)
            # Clear the input
            st.empty()

def main():
    """Main entry point for the Streamlit app."""
    app = RAGTestingApp()
    app.render()

if __name__ == "__main__":
    main()
