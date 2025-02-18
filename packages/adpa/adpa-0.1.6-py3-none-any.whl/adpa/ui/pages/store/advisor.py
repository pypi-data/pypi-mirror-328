"""Enhanced Streamlit interface for RAG/Vector Store advisor with advanced visualizations."""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import List, Dict, Optional
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
from adpa.ui.utils.state import UIState
from adpa.ui.utils.validation import InputValidator

class StoreAdvisorUI:
    """UI class for store advisor functionality."""
    
    def __init__(self):
        """Initialize the store advisor UI."""
        self.advisor = StoreAdvisor()
        self.setup_session_state()
    
    def setup_session_state(self):
        """Initialize session state variables."""
        UIState.init_session_state()
        if 'recommendations' not in st.session_state:
            st.session_state.recommendations = []
    
    def plot_radar_comparison(self, recommendations: List[StoreRecommendation]) -> go.Figure:
        """Create an enhanced radar chart comparing store capabilities.
        
        Args:
            recommendations: List of store recommendations to compare
            
        Returns:
            Plotly figure object
        """
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
    
    def plot_performance_comparison(self, recommendations: List[StoreRecommendation]) -> go.Figure:
        """Create performance comparison charts.
        
        Args:
            recommendations: List of store recommendations to compare
            
        Returns:
            Plotly figure object
        """
        data = {
            'Store': [],
            'Query Latency (ms)': [],
            'Indexing Speed (docs/s)': [],
            'Memory Usage (GB)': []
        }
        
        for rec in recommendations[:3]:
            data['Store'].append(rec.store_type)
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
    
    def render_advisor_tab(self):
        """Render the advisor tab content."""
        st.write("""
        This advisor helps you choose the best RAG (Retrieval-Augmented Generation) and 
        vector store solution for your specific use case.
        """)
        
        # Use case form
        with st.form("use_case_form"):
            data_size = st.selectbox(
                "Data Size",
                options=[e.value for e in DataSize]
            )
            
            update_freq = st.selectbox(
                "Update Frequency",
                options=[e.value for e in UpdateFrequency]
            )
            
            query_latency = st.selectbox(
                "Required Query Latency",
                options=[e.value for e in QueryLatency]
            )
            
            deployment = st.selectbox(
                "Deployment Type",
                options=[e.value for e in Deployment]
            )
            
            budget = st.selectbox(
                "Budget Range",
                options=[e.value for e in Budget]
            )
            
            col1, col2, col3 = st.columns(3)
            with col1:
                requires_filtering = st.checkbox("Requires Filtering")
            with col2:
                requires_hybrid = st.checkbox("Requires Hybrid Search")
            with col3:
                requires_reranking = st.checkbox("Requires Reranking")
            
            submitted = st.form_submit_button("Get Recommendations")
            
            if submitted:
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
                
                with st.spinner("Analyzing use case..."):
                    recommendations = self.advisor.get_recommendations(use_case)
                    UIState.set('recommendations', recommendations)
                    st.session_state.recommendations = recommendations
    
    def render_comparison_tab(self):
        """Render the comparison tab content."""
        if not st.session_state.recommendations:
            st.info("Get recommendations first to see comparisons.")
            return
        
        # Display radar chart
        st.plotly_chart(
            self.plot_radar_comparison(st.session_state.recommendations),
            use_container_width=True
        )
        
        # Display performance comparison
        st.plotly_chart(
            self.plot_performance_comparison(st.session_state.recommendations),
            use_container_width=True
        )
        
        # Detailed comparison table
        comparison_df = pd.DataFrame([
            {
                "Store": rec.store_type,
                "Confidence": f"{rec.confidence:.0%}",
                "Est. Cost": rec.estimated_cost,
                "Pros": "\n".join(rec.pros),
                "Cons": "\n".join(rec.cons)
            }
            for rec in st.session_state.recommendations[:3]
        ])
        st.dataframe(comparison_df)
    
    def render_export_tab(self):
        """Render the export tab content."""
        if not st.session_state.recommendations:
            st.info("Get recommendations first to export.")
            return
        
        st.download_button(
            "Download Recommendations",
            data=self.advisor.export_recommendations(st.session_state.recommendations),
            file_name="store_recommendations.json",
            mime="application/json"
        )
    
    def render_benchmarks_tab(self):
        """Render the benchmarks tab content."""
        st.write("### Vector Store Benchmarks")
        
        # Sample benchmark data
        benchmark_data = pd.DataFrame({
            "Store": ["Chroma", "FAISS", "Milvus", "Qdrant"],
            "1K docs": [45, 35, 55, 50],
            "10K docs": [85, 75, 95, 90],
            "100K docs": [250, 200, 180, 190]
        })
        
        st.dataframe(benchmark_data)
        
        # Plot benchmark trends
        fig = px.line(
            benchmark_data.melt(
                id_vars=["Store"],
                var_name="Dataset Size",
                value_name="Query Time (ms)"
            ),
            x="Dataset Size",
            y="Query Time (ms)",
            color="Store",
            title="Query Performance vs Dataset Size"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    def render(self):
        """Render the main UI."""
        st.title("RAG/Vector Store Advisor")
        
        tab1, tab2, tab3, tab4 = st.tabs([
            "Advisor", "Comparison Guide", "Import/Export", "Benchmarks"
        ])
        
        with tab1:
            self.render_advisor_tab()
        
        with tab2:
            self.render_comparison_tab()
        
        with tab3:
            self.render_export_tab()
        
        with tab4:
            self.render_benchmarks_tab()

def main():
    """Main entry point for the Streamlit app."""
    app = StoreAdvisorUI()
    app.render()

if __name__ == "__main__":
    main()
