"""Knowledge query interface for the ADPA Framework."""

from typing import Dict, List, Optional, Tuple, Any
import streamlit as st
from datetime import datetime
import json

from adpa.core.rag import RAGPipeline
from adpa.core.types import Document, Query, Response
from adpa.utils.logger import get_logger
from adpa.utils.stability import with_retry, safe_state_operation
from adpa.database.models.query_history import QueryHistory
from adpa.ui.config.database import get_db

# Setup logging
logger = get_logger(__name__)

# Constants
MAX_HISTORY_ITEMS = 50
SIMILARITY_THRESHOLD = 0.8
MAX_SOURCES = 5

class KnowledgeQueryUI:
    """Knowledge query interface component."""
    
    def __init__(self):
        """Initialize knowledge query interface."""
        self.rag_pipeline = RAGPipeline()
        self._initialize_session_state()
    
    def _initialize_session_state(self) -> None:
        """Initialize or restore session state."""
        with safe_state_operation():
            if "query_history" not in st.session_state:
                st.session_state.query_history = []
            if "current_response" not in st.session_state:
                st.session_state.current_response = None
            if "error_message" not in st.session_state:
                st.session_state.error_message = None
    
    @with_retry(retries=3, delay=1.0)
    def _process_query(self, query: str) -> Tuple[Response, List[Document]]:
        """Process a query through the RAG pipeline.
        
        Args:
            query: User query string
            
        Returns:
            Tuple containing:
            - Response object with answer
            - List of relevant source documents
            
        Raises:
            Exception: If query processing fails
        """
        try:
            # Create query object
            query_obj = Query(
                text=query,
                timestamp=datetime.utcnow(),
                metadata={"source": "knowledge_query_ui"}
            )
            
            # Process through pipeline
            response, sources = self.rag_pipeline.process(
                query_obj,
                similarity_threshold=SIMILARITY_THRESHOLD,
                max_sources=MAX_SOURCES
            )
            
            # Save to history
            self._save_to_history(query_obj, response, sources)
            
            return response, sources
            
        except Exception as e:
            logger.error(f"Query processing failed: {str(e)}")
            raise
    
    def _save_to_history(
        self,
        query: Query,
        response: Response,
        sources: List[Document]
    ) -> None:
        """Save query and response to history.
        
        Args:
            query: Query object
            response: Response object
            sources: List of source documents
        """
        try:
            # Save to session state
            history_item = {
                "query": query.text,
                "response": response.text,
                "sources": [doc.metadata.get("title", "Unknown") for doc in sources],
                "timestamp": query.timestamp.isoformat()
            }
            
            st.session_state.query_history.append(history_item)
            if len(st.session_state.query_history) > MAX_HISTORY_ITEMS:
                st.session_state.query_history.pop(0)
            
            # Save to database
            with get_db() as db:
                history = QueryHistory(
                    query_text=query.text,
                    response_text=response.text,
                    sources=json.dumps([doc.to_dict() for doc in sources]),
                    metadata=json.dumps(query.metadata)
                )
                db.add(history)
                db.commit()
                
        except Exception as e:
            logger.error(f"Failed to save to history: {str(e)}")
    
    def _display_response(
        self,
        response: Response,
        sources: List[Document]
    ) -> None:
        """Display query response and sources.
        
        Args:
            response: Response object
            sources: List of source documents
        """
        # Display response
        st.markdown("### Answer")
        st.write(response.text)
        
        # Display sources
        if sources:
            st.markdown("### Sources")
            for i, doc in enumerate(sources, 1):
                with st.expander(f"Source {i}: {doc.metadata.get('title', 'Unknown')}"):
                    st.write(doc.page_content)
                    st.markdown("**Metadata:**")
                    st.json(doc.metadata)
    
    def _display_history(self) -> None:
        """Display query history."""
        if st.session_state.query_history:
            st.markdown("### Recent Queries")
            for item in reversed(st.session_state.query_history[-5:]):
                with st.expander(f"{item['timestamp']}: {item['query'][:50]}..."):
                    st.write("**Query:**", item["query"])
                    st.write("**Response:**", item["response"])
                    st.write("**Sources:**", ", ".join(item["sources"]))
    
    def render(self) -> None:
        """Render the knowledge query interface."""
        st.title("Knowledge Query")
        
        # Query input
        query = st.text_area("Enter your query:", height=100)
        
        # Process query
        if st.button("Submit Query"):
            if not query:
                st.error("Please enter a query.")
                return
            
            try:
                with st.spinner("Processing query..."):
                    response, sources = self._process_query(query)
                    
                self._display_response(response, sources)
                st.session_state.error_message = None
                
            except Exception as e:
                st.error(f"Error processing query: {str(e)}")
                st.session_state.error_message = str(e)
        
        # Display error if present
        if st.session_state.error_message:
            st.error(st.session_state.error_message)
        
        # Display history
        self._display_history()


def main():
    """Main entry point for knowledge query page."""
    try:
        ui = KnowledgeQueryUI()
        ui.render()
    except Exception as e:
        st.error(f"Failed to initialize knowledge query interface: {str(e)}")
        logger.error(f"Knowledge query interface error: {str(e)}")


if __name__ == "__main__":
    main()
