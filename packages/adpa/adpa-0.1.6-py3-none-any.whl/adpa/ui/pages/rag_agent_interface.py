"""RAG agent interface for the ADPA Framework."""

from typing import Dict, List, Optional, Any
import streamlit as st
from datetime import datetime
import json

from adpa.core.rag import RAGAgent
from adpa.core.types import AgentConfig, Document, Query, Response
from adpa.utils.logger import get_logger
from adpa.utils.stability import with_retry, safe_state_operation
from adpa.database.models.agent_interaction import AgentInteraction
from adpa.ui.config.database import get_db

# Setup logging
logger = get_logger(__name__)

# Constants
MAX_HISTORY_ITEMS = 50
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 1000

class RAGAgentUI:
    """RAG agent interface component."""
    
    def __init__(self):
        """Initialize RAG agent interface."""
        self._initialize_session_state()
        self._initialize_agent()
    
    def _initialize_session_state(self) -> None:
        """Initialize or restore session state."""
        with safe_state_operation():
            if "agent_history" not in st.session_state:
                st.session_state.agent_history = []
            if "current_agent_config" not in st.session_state:
                st.session_state.current_agent_config = self._get_default_config()
            if "error_message" not in st.session_state:
                st.session_state.error_message = None
    
    def _get_default_config(self) -> AgentConfig:
        """Get default agent configuration.
        
        Returns:
            Default agent configuration
        """
        return AgentConfig(
            model_name="gpt-4",
            temperature=DEFAULT_TEMPERATURE,
            max_tokens=DEFAULT_MAX_TOKENS,
            top_p=0.95,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
    
    def _initialize_agent(self) -> None:
        """Initialize RAG agent with current configuration."""
        try:
            self.agent = RAGAgent(
                config=st.session_state.current_agent_config
            )
        except Exception as e:
            logger.error(f"Failed to initialize agent: {str(e)}")
            st.session_state.error_message = str(e)
            raise
    
    @with_retry(retries=3, delay=1.0)
    def _process_query(self, query: str) -> Response:
        """Process a query through the RAG agent.
        
        Args:
            query: User query string
            
        Returns:
            Agent's response
            
        Raises:
            Exception: If query processing fails
        """
        try:
            # Create query object
            query_obj = Query(
                text=query,
                timestamp=datetime.utcnow(),
                metadata={"source": "rag_agent_ui"}
            )
            
            # Process through agent
            response = self.agent.process_query(query_obj)
            
            # Save to history
            self._save_to_history(query_obj, response)
            
            return response
            
        except Exception as e:
            logger.error(f"Agent query processing failed: {str(e)}")
            raise
    
    def _save_to_history(
        self,
        query: Query,
        response: Response
    ) -> None:
        """Save interaction to history.
        
        Args:
            query: Query object
            response: Response object
        """
        try:
            # Save to session state
            history_item = {
                "query": query.text,
                "response": response.text,
                "timestamp": query.timestamp.isoformat(),
                "metadata": response.metadata
            }
            
            st.session_state.agent_history.append(history_item)
            if len(st.session_state.agent_history) > MAX_HISTORY_ITEMS:
                st.session_state.agent_history.pop(0)
            
            # Save to database
            with get_db() as db:
                interaction = AgentInteraction(
                    query_text=query.text,
                    response_text=response.text,
                    agent_config=json.dumps(
                        st.session_state.current_agent_config.dict()
                    ),
                    metadata=json.dumps(response.metadata)
                )
                db.add(interaction)
                db.commit()
                
        except Exception as e:
            logger.error(f"Failed to save to history: {str(e)}")
    
    def _update_agent_config(self) -> None:
        """Update agent configuration from UI inputs."""
        try:
            # Get values from UI
            model = st.session_state.get("model_name", "gpt-4")
            temperature = st.session_state.get(
                "temperature",
                DEFAULT_TEMPERATURE
            )
            max_tokens = st.session_state.get(
                "max_tokens",
                DEFAULT_MAX_TOKENS
            )
            
            # Create new config
            config = AgentConfig(
                model_name=model,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=0.95,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            
            # Update session state and agent
            st.session_state.current_agent_config = config
            self._initialize_agent()
            
        except Exception as e:
            logger.error(f"Failed to update agent config: {str(e)}")
            st.session_state.error_message = str(e)
    
    def _render_config_sidebar(self) -> None:
        """Render agent configuration sidebar."""
        st.sidebar.header("Agent Configuration")
        
        # Model selection
        st.sidebar.selectbox(
            "Model",
            options=["gpt-4", "gpt-3.5-turbo"],
            key="model_name",
            on_change=self._update_agent_config
        )
        
        # Temperature slider
        st.sidebar.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.0,
            value=DEFAULT_TEMPERATURE,
            step=0.1,
            key="temperature",
            on_change=self._update_agent_config
        )
        
        # Max tokens slider
        st.sidebar.slider(
            "Max Tokens",
            min_value=100,
            max_value=2000,
            value=DEFAULT_MAX_TOKENS,
            step=100,
            key="max_tokens",
            on_change=self._update_agent_config
        )
    
    def _display_history(self) -> None:
        """Display interaction history."""
        if st.session_state.agent_history:
            st.markdown("### Recent Interactions")
            for item in reversed(st.session_state.agent_history[-5:]):
                with st.expander(f"{item['timestamp']}: {item['query'][:50]}..."):
                    st.write("**Query:**", item["query"])
                    st.write("**Response:**", item["response"])
                    if item["metadata"]:
                        st.markdown("**Metadata:**")
                        st.json(item["metadata"])
    
    def render(self) -> None:
        """Render the RAG agent interface."""
        st.title("RAG Agent Interface")
        
        # Render configuration sidebar
        self._render_config_sidebar()
        
        # Query input
        query = st.text_area("Enter your query:", height=100)
        
        # Process query
        if st.button("Submit Query"):
            if not query:
                st.error("Please enter a query.")
                return
            
            try:
                with st.spinner("Processing query..."):
                    response = self._process_query(query)
                    
                st.markdown("### Response")
                st.write(response.text)
                
                if response.metadata:
                    st.markdown("### Response Metadata")
                    st.json(response.metadata)
                
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
    """Main entry point for RAG agent interface page."""
    try:
        ui = RAGAgentUI()
        ui.render()
    except Exception as e:
        st.error(f"Failed to initialize RAG agent interface: {str(e)}")
        logger.error(f"RAG agent interface error: {str(e)}")


if __name__ == "__main__":
    main()
