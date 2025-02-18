"""
Enhanced Streamlit interface for RAG/Vector Store advisor with advanced visualizations.
"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json
from typing import List, Dict
from datetime import datetime

from adpa.knowledge.store_advisor import (
    StoreAdvisor,
    UseCase,
    DataSize,
    UpdateFrequency,
    QueryLatency,
    Deployment,
    Budget,
    StoreRecommendation
)

from adpa.core.store import VectorStoreManager
from adpa.core.types import Document, StoreConfig, StoreMetrics
from adpa.utils.logger import get_logger
from adpa.utils.stability import with_retry, safe_state_operation
from adpa.database.models.store_operation import StoreOperation
from adpa.ui.config.database import get_db

# Setup logging
logger = get_logger(__name__)

# Constants
MAX_HISTORY_ITEMS = 50
DEFAULT_CHUNK_SIZE = 512
DEFAULT_CHUNK_OVERLAP = 128


class StoreAdvisorUI:
    """Store advisor interface component."""
    
    def __init__(self):
        """Initialize store advisor interface."""
        self.store_manager = VectorStoreManager()
        self._initialize_session_state()
    
    def _initialize_session_state(self) -> None:
        """Initialize or restore session state."""
        with safe_state_operation():
            if "store_operations" not in st.session_state:
                st.session_state.store_operations = []
            if "current_store" not in st.session_state:
                st.session_state.current_store = None
            if "store_metrics" not in st.session_state:
                st.session_state.store_metrics = {}
            if "error_message" not in st.session_state:
                st.session_state.error_message = None
    
    def _get_default_config(self) -> StoreConfig:
        """Get default store configuration.
        
        Returns:
            Default store configuration
        """
        return StoreConfig(
            chunk_size=DEFAULT_CHUNK_SIZE,
            chunk_overlap=DEFAULT_CHUNK_OVERLAP,
            similarity_threshold=0.8,
            embedding_model="text-embedding-ada-002",
            store_type="chroma"
        )
    
    @with_retry(retries=3, delay=1.0)
    def _create_store(self, name: str, config: StoreConfig) -> None:
        """Create a new vector store.
        
        Args:
            name: Store name
            config: Store configuration
            
        Raises:
            Exception: If store creation fails
        """
        try:
            # Create store
            self.store_manager.create_store(name, config)
            
            # Update session state
            st.session_state.current_store = name
            
            # Save operation
            self._save_operation(
                operation_type="create",
                store_name=name,
                config=config
            )
            
        except Exception as e:
            logger.error(f"Store creation failed: {str(e)}")
            raise
    
    @with_retry(retries=3, delay=1.0)
    def _add_documents(
        self,
        files: List[Any],
        metadata: Optional[Dict] = None
    ) -> None:
        """Add documents to current store.
        
        Args:
            files: List of uploaded files
            metadata: Optional metadata for documents
            
        Raises:
            Exception: If document addition fails
        """
        try:
            if not st.session_state.current_store:
                raise ValueError("No store selected")
            
            # Process files
            for file in files:
                # Add to store
                self.store_manager.add_document(
                    store_name=st.session_state.current_store,
                    file_path=file,
                    metadata=metadata or {"filename": file.name}
                )
            
            # Save operation
            self._save_operation(
                operation_type="add_documents",
                store_name=st.session_state.current_store,
                metadata={"num_files": len(files)}
            )
            
        except Exception as e:
            logger.error(f"Document addition failed: {str(e)}")
            raise
    
    def _save_operation(
        self,
        operation_type: str,
        store_name: str,
        config: Optional[StoreConfig] = None,
        metadata: Optional[Dict] = None
    ) -> None:
        """Save store operation to history.
        
        Args:
            operation_type: Type of operation
            store_name: Name of store
            config: Optional store configuration
            metadata: Optional operation metadata
        """
        try:
            # Save to session state
            operation = {
                "type": operation_type,
                "store": store_name,
                "timestamp": datetime.utcnow().isoformat(),
                "config": config.dict() if config else None,
                "metadata": metadata
            }
            
            st.session_state.store_operations.append(operation)
            if len(st.session_state.store_operations) > MAX_HISTORY_ITEMS:
                st.session_state.store_operations.pop(0)
            
            # Save to database
            with get_db() as db:
                record = StoreOperation(
                    operation_type=operation_type,
                    store_name=store_name,
                    config=json.dumps(config.dict()) if config else None,
                    metadata=json.dumps(metadata) if metadata else None
                )
                db.add(record)
                db.commit()
                
        except Exception as e:
            logger.error(f"Failed to save operation: {str(e)}")
    
    def _update_metrics(self) -> None:
        """Update store metrics."""
        try:
            if not st.session_state.current_store:
                return
            
            # Get metrics
            metrics = self.store_manager.get_metrics(
                st.session_state.current_store
            )
            
            # Update session state
            st.session_state.store_metrics[
                st.session_state.current_store
            ] = metrics
            
        except Exception as e:
            logger.error(f"Failed to update metrics: {str(e)}")
    
    def _display_metrics(self) -> None:
        """Display store metrics."""
        if not st.session_state.current_store:
            return
            
        metrics = st.session_state.store_metrics.get(
            st.session_state.current_store
        )
        
        if not metrics:
            return
            
        st.subheader("Store Metrics")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Total Documents",
                metrics.total_documents
            )
        
        with col2:
            st.metric(
                "Total Chunks",
                metrics.total_chunks
            )
        
        with col3:
            st.metric(
                "Store Size (MB)",
                round(metrics.store_size_mb, 2)
            )
    
    def _display_operations(self) -> None:
        """Display operation history."""
        if st.session_state.store_operations:
            st.markdown("### Recent Operations")
            for op in reversed(st.session_state.store_operations[-5:]):
                with st.expander(
                    f"{op['timestamp']}: {op['type']} - {op['store']}"
                ):
                    st.write("**Type:**", op["type"])
                    st.write("**Store:**", op["store"])
                    if op["config"]:
                        st.markdown("**Configuration:**")
                        st.json(op["config"])
                    if op["metadata"]:
                        st.markdown("**Metadata:**")
                        st.json(op["metadata"])
    
    def render(self) -> None:
        """Render the store advisor interface."""
        st.title("Store Advisor")
        
        # Store selection/creation
        st.header("Vector Store Management")
        
        col1, col2 = st.columns(2)
        
        with col1:
            stores = self.store_manager.list_stores()
            if stores:
                selected = st.selectbox(
                    "Select Store",
                    options=stores,
                    index=stores.index(st.session_state.current_store)
                    if st.session_state.current_store in stores
                    else 0
                )
                st.session_state.current_store = selected
        
        with col2:
            if st.button("Create New Store"):
                st.session_state.current_store = None
        
        # Create new store
        if st.session_state.current_store is None:
            st.subheader("Create New Store")
            
            name = st.text_input("Store Name")
            
            config = self._get_default_config()
            
            # Configuration options
            st.markdown("### Store Configuration")
            
            col1, col2 = st.columns(2)
            
            with col1:
                config.chunk_size = st.number_input(
                    "Chunk Size",
                    min_value=128,
                    max_value=2048,
                    value=DEFAULT_CHUNK_SIZE,
                    step=128
                )
                
                config.chunk_overlap = st.number_input(
                    "Chunk Overlap",
                    min_value=0,
                    max_value=512,
                    value=DEFAULT_CHUNK_OVERLAP,
                    step=64
                )
            
            with col2:
                config.store_type = st.selectbox(
                    "Store Type",
                    options=["chroma", "faiss", "milvus"]
                )
                
                config.embedding_model = st.selectbox(
                    "Embedding Model",
                    options=[
                        "text-embedding-ada-002",
                        "text-embedding-3-small",
                        "text-embedding-3-large"
                    ]
                )
            
            if st.button("Create Store"):
                if not name:
                    st.error("Please enter a store name.")
                    return
                
                try:
                    with st.spinner("Creating store..."):
                        self._create_store(name, config)
                    st.success("Store created successfully!")
                except Exception as e:
                    st.error(f"Failed to create store: {str(e)}")
        
        # Work with existing store
        else:
            # Document upload
            st.subheader("Add Documents")
            
            files = st.file_uploader(
                "Upload Documents",
                accept_multiple_files=True,
                type=["txt", "pdf", "md", "doc", "docx"]
            )
            
            if files and st.button("Add Documents"):
                try:
                    with st.spinner("Adding documents..."):
                        self._add_documents(files)
                    st.success("Documents added successfully!")
                    self._update_metrics()
                except Exception as e:
                    st.error(f"Failed to add documents: {str(e)}")
            
            # Display metrics
            self._display_metrics()
        
        # Display operations
        self._display_operations()


def plot_radar_comparison(recommendations: List[StoreRecommendation]):
    """Create an enhanced radar chart comparing store capabilities."""
    categories = [
        'Scalability', 'Query Speed', 'Update Speed', 
        'Features', 'Cost-Efficiency', 'Ease of Use'
    ]
    
    fig = go.Figure()
    colors = px.colors.qualitative.Set3
    
    for idx, rec in enumerate(recommendations[:3]):
        values = [
            0.9 if rec.store_type in ['milvus', 'weaviate', 'pinecone'] else 0.6,
            0.9 if 'Fast query performance' in rec.pros else 0.7,
            0.8 if 'Real-time updates' in rec.pros else 0.5,
            0.9 if 'hybrid search' not in rec.cons else 0.6,
            0.8 if 'Higher cost' not in rec.cons else 0.7,
            0.9 if rec.store_type in ['chromadb', 'qdrant'] else 0.6,
        ]
        values.append(values[0])
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories + [categories[0]],
            name=rec.store_type,
            fill='toself',
            line_color=colors[idx]
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1],
                ticktext=['Low', 'Medium', 'High'],
                tickvals=[0.3, 0.6, 0.9]
            )
        ),
        showlegend=True,
        title="Vector Store Capability Comparison",
        height=500
    )
    
    return fig

def plot_performance_comparison(recommendations: List[StoreRecommendation]):
    """Create performance comparison charts."""
    # Sample performance data (replace with actual benchmarks)
    data = {
        'Store': [],
        'Query Latency (ms)': [],
        'Indexing Speed (docs/s)': [],
        'Memory Usage (GB)': []
    }
    
    for rec in recommendations[:3]:
        data['Store'].append(rec.store_type)
        # Add performance metrics based on store type
        if rec.store_type in ['faiss', 'redis']:
            data['Query Latency (ms)'].append(45)
            data['Indexing Speed (docs/s)'].append(10000)
            data['Memory Usage (GB)'].append(4)
        elif rec.store_type in ['milvus', 'qdrant']:
            data['Query Latency (ms)'].append(85)
            data['Indexing Speed (docs/s)'].append(8000)
            data['Memory Usage (GB)'].append(6)
        else:
            data['Query Latency (ms)'].append(100)
            data['Indexing Speed (docs/s)'].append(5000)
            data['Memory Usage (GB)'].append(8)
    
    df = pd.DataFrame(data)
    
    fig = go.Figure()
    
    # Add bars for each metric
    fig.add_trace(go.Bar(
        name='Query Latency (ms)',
        x=df['Store'],
        y=df['Query Latency (ms)'],
        marker_color='rgb(55, 83, 109)'
    ))
    
    fig.add_trace(go.Bar(
        name='Indexing Speed (K docs/s)',
        x=df['Store'],
        y=df['Indexing Speed (docs/s)'] / 1000,
        marker_color='rgb(26, 118, 255)'
    ))
    
    fig.add_trace(go.Bar(
        name='Memory Usage (GB)',
        x=df['Store'],
        y=df['Memory Usage (GB)'],
        marker_color='rgb(158, 202, 225)'
    ))
    
    fig.update_layout(
        title="Performance Comparison",
        barmode='group',
        height=400
    )
    
    return fig

def export_recommendations(recommendations: List[StoreRecommendation], use_case: UseCase):
    """Export recommendations to JSON."""
    export_data = {
        "timestamp": datetime.now().isoformat(),
        "use_case": {
            "data_size": use_case.data_size.value,
            "update_frequency": use_case.update_frequency.value,
            "query_latency": use_case.query_latency.value,
            "deployment": use_case.deployment.value,
            "budget": use_case.budget.value,
            "requires_filtering": use_case.requires_filtering,
            "requires_hybrid_search": use_case.requires_hybrid_search,
            "requires_reranking": use_case.requires_reranking
        },
        "recommendations": [
            {
                "store_type": rec.store_type,
                "embedding_type": rec.embedding_type,
                "confidence": rec.confidence,
                "explanation": rec.explanation,
                "configuration": rec.configuration,
                "estimated_cost": rec.estimated_cost,
                "pros": rec.pros,
                "cons": rec.cons
            }
            for rec in recommendations
        ]
    }
    return json.dumps(export_data, indent=2)

def import_recommendations(json_str: str) -> tuple[UseCase, List[StoreRecommendation]]:
    """Import recommendations from JSON."""
    data = json.loads(json_str)
    
    use_case = UseCase(
        data_size=DataSize(data["use_case"]["data_size"]),
        update_frequency=UpdateFrequency(data["use_case"]["update_frequency"]),
        query_latency=QueryLatency(data["use_case"]["query_latency"]),
        deployment=Deployment(data["use_case"]["deployment"]),
        budget=Budget(data["use_case"]["budget"]),
        requires_filtering=data["use_case"]["requires_filtering"],
        requires_hybrid_search=data["use_case"]["requires_hybrid_search"],
        requires_reranking=data["use_case"]["requires_reranking"]
    )
    
    recommendations = [
        StoreRecommendation(
            store_type=rec["store_type"],
            embedding_type=rec["embedding_type"],
            confidence=rec["confidence"],
            explanation=rec["explanation"],
            configuration=rec["configuration"],
            estimated_cost=rec["estimated_cost"],
            pros=rec["pros"],
            cons=rec["cons"]
        )
        for rec in data["recommendations"]
    ]
    
    return use_case, recommendations

def store_advisor_page():
    """Enhanced Streamlit interface for store advisor."""
    st.title("RAG/Vector Store Advisor")
    
    # Add tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs([
        "Advisor", "Comparison Guide", "Import/Export", "Benchmarks"
    ])
    
    with tab1:
        st.write("""
        This advisor helps you choose the best RAG (Retrieval-Augmented Generation) and 
        vector store solution for your specific use case.
        """)
        
        # Use case form
        with st.form("use_case_form"):
            st.header("Use Case Details")
            
            col1, col2 = st.columns(2)
            
            with col1:
                data_size = st.selectbox(
                    "Data Size",
                    options=[size.value for size in DataSize],
                    help="How many documents will you store?"
                )
                
                update_freq = st.selectbox(
                    "Update Frequency",
                    options=[freq.value for freq in UpdateFrequency],
                    help="How often will your data be updated?"
                )
                
                query_latency = st.selectbox(
                    "Required Query Latency",
                    options=[lat.value for lat in QueryLatency],
                    help="What's your maximum acceptable query response time?"
                )
            
            with col2:
                deployment = st.selectbox(
                    "Deployment Preference",
                    options=[dep.value for dep in Deployment],
                    help="Where do you want to deploy?"
                )
                
                budget = st.selectbox(
                    "Budget Level",
                    options=[b.value for b in Budget],
                    help="What's your budget range?"
                )
            
            # Advanced requirements
            with st.expander("Advanced Requirements"):
                requires_filtering = st.checkbox(
                    "Requires Metadata Filtering",
                    help="Do you need to filter results based on metadata?"
                )
                
                requires_hybrid = st.checkbox(
                    "Requires Hybrid Search",
                    help="Do you need both vector and keyword search?"
                )
                
                requires_reranking = st.checkbox(
                    "Requires Reranking",
                    help="Do you need advanced result reranking?"
                )
            
            submitted = st.form_submit_button("Get Recommendations")
        
        if submitted:
            # Create use case
            use_case = UseCase(
                data_size=DataSize(data_size),
                update_frequency=UpdateFrequency(update_freq),
                query_latency=QueryLatency(query_latency),
                deployment=Deployment(deployment),
                budget=Budget(budget),
                requires_filtering=requires_filtering,
                requires_hybrid_search=requires_hybrid,
                requires_reranking=requires_reranking
            )
            
            # Get recommendations
            advisor = StoreAdvisor()
            recommendations = advisor.get_recommendation(use_case)
            
            if recommendations:
                st.header("Recommendations")
                
                # Plot comparison
                st.plotly_chart(plot_radar_comparison(recommendations))
                
                # Display recommendations
                for i, rec in enumerate(recommendations, 1):
                    with st.expander(f"#{i} {rec.store_type.upper()} ({rec.confidence:.2f} confidence)"):
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.subheader("Overview")
                            st.write(rec.explanation)
                            st.write(f"**Estimated Cost:** {rec.estimated_cost}")
                            
                            st.subheader("Pros")
                            for pro in rec.pros:
                                st.write(f"✓ {pro}")
                        
                        with col2:
                            st.subheader("Configuration")
                            st.json(rec.configuration)
                            
                            st.subheader("Cons")
                            for con in rec.cons:
                                st.write(f"⚠ {con}")
                
                # Quick setup button
                if st.button("Set Up Selected Store"):
                    # Get the top recommendation
                    top_rec = recommendations[0]
                    
                    # Save configuration
                    st.session_state["vector_store_config"] = {
                        "store_type": top_rec.store_type,
                        "embedding_type": top_rec.embedding_type,
                        **top_rec.configuration
                    }
                    
                    st.success(f"Configuration saved! Go to Vector Store Management to complete setup.")
            else:
                st.error("No suitable recommendations found for your use case. Please adjust your requirements.")
    
    with tab2:
        st.header("Vector Store Comparison Guide")
        with open("docs/guides/vector-store-comparison.md", "r") as f:
            st.markdown(f.read())
    
    with tab3:
        st.header("Import/Export Recommendations")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Export")
            if "current_recommendations" in st.session_state:
                export_data = export_recommendations(
                    st.session_state.current_recommendations,
                    st.session_state.current_use_case
                )
                st.download_button(
                    "Download Recommendations",
                    export_data,
                    "recommendations.json",
                    "application/json"
                )
        
        with col2:
            st.subheader("Import")
            uploaded_file = st.file_uploader(
                "Upload Recommendations",
                type="json"
            )
            if uploaded_file:
                json_str = uploaded_file.getvalue().decode()
                use_case, recommendations = import_recommendations(json_str)
                st.session_state.current_use_case = use_case
                st.session_state.current_recommendations = recommendations
                st.success("Recommendations imported successfully!")
    
    with tab4:
        st.header("Performance Benchmarks")
        
        if "current_recommendations" in st.session_state:
            st.plotly_chart(
                plot_performance_comparison(
                    st.session_state.current_recommendations
                )
            )
        else:
            st.info("Run the advisor to see performance benchmarks.")

def main():
    """Main entry point for store advisor page."""
    try:
        ui = StoreAdvisorUI()
        ui.render()
    except Exception as e:
        st.error(f"Failed to initialize store advisor: {str(e)}")
        logger.error(f"Store advisor error: {str(e)}")


if __name__ == "__main__":
    main()
