"""Streamlit app for Text-to-SQL system with vector store integration."""
import streamlit as st
import json
import os
from datetime import datetime, timedelta
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from typing import Dict, List

from .engine import TextToSQLEngine
from .vector_store import VectorStore

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []
if "feedback_data" not in st.session_state:
    st.session_state.feedback_data = []
if "current_page" not in st.session_state:
    st.session_state.current_page = "Query Database"

def init_engine():
    """Initialize the Text-to-SQL engine and vector store."""
    if "engine" not in st.session_state:
        # Load config from file or environment
        config = {
            "host": os.getenv("DB_HOST"),
            "port": os.getenv("DB_PORT"),
            "dbname": os.getenv("DB_NAME"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD")
        }
        
        st.session_state.engine = TextToSQLEngine(config)
        st.session_state.vector_store = VectorStore("./vector_store")

def show_schema_info():
    """Display schema information with enhanced search and visualization."""
    st.subheader("Schema Information")
    
    # Schema search with filters
    col1, col2 = st.columns([3, 1])
    with col1:
        search_term = st.text_input("Search schema:", key="schema_search")
    with col2:
        search_type = st.selectbox("Search by:", ["All", "Table", "Column", "Relationship"])
    
    if search_term:
        relevant_schema = st.session_state.vector_store.find_relevant_schema(search_term)
        
        # Schema visualization
        if relevant_schema:
            fig = create_schema_visualization(relevant_schema)
            st.plotly_chart(fig)
        
        # Detailed schema information
        for schema in relevant_schema:
            with st.expander(f"Table: {schema['table_name']} (Score: {1-schema['similarity_score']:.2f})"):
                st.write(schema['description'])
                
                # Show relationships graph
                if schema.get('relationships'):
                    st.write("Relationships:")
                    fig = create_relationship_graph(schema['relationships'])
                    st.plotly_chart(fig)
                
                # Show detailed metadata
                with st.expander("Technical Details"):
                    st.json(schema['schema_info'])

def show_training_data():
    """Display and manage training data with advanced features."""
    st.subheader("Training Data Management")
    
    tabs = st.tabs(["Add Examples", "Search Examples", "Batch Upload", "Quality Analysis"])
    
    with tabs[0]:
        show_add_training_example()
    
    with tabs[1]:
        show_search_training_examples()
    
    with tabs[2]:
        show_batch_upload()
    
    with tabs[3]:
        show_training_quality_analysis()

def show_add_training_example():
    """Interface for adding individual training examples."""
    col1, col2 = st.columns([2, 1])
    
    with col1:
        question = st.text_input("Natural Language Question:")
        sql = st.text_area("SQL Query:")
        
        # Metadata fields
        complexity = st.slider("Query Complexity", 1, 5, 3)
        tags = st.multiselect("Tags", ["SELECT", "JOIN", "WHERE", "GROUP BY", "HAVING", "Subquery"])
        
    with col2:
        st.write("Preview SQL:")
        if sql:
            st.code(sql, language="sql")
            
        # Validation status
        if sql:
            validation_result = validate_sql(sql)
            if validation_result["valid"]:
                st.success("SQL is valid")
            else:
                st.error(f"SQL Error: {validation_result['error']}")
    
    if st.button("Add Example"):
        if question and sql:
            metadata = {
                "complexity": complexity,
                "tags": tags,
                "validated": True
            }
            st.session_state.vector_store.store_training_example(
                question=question,
                sql=sql,
                metadata=metadata
            )
            st.success("Training example added successfully!")

def show_search_training_examples():
    """Advanced search interface for training examples."""
    col1, col2 = st.columns([3, 1])
    
    with col1:
        search_term = st.text_input("Search training examples:", key="training_search")
    with col2:
        search_filter = st.selectbox("Filter by:", ["All", "Simple", "Complex", "With Joins", "Aggregations"])
    
    if search_term:
        similar = st.session_state.vector_store.find_similar_training(search_term)
        
        # Group examples by complexity
        simple_examples = []
        complex_examples = []
        
        for example in similar:
            if example.get("complexity", 3) <= 3:
                simple_examples.append(example)
            else:
                complex_examples.append(example)
        
        # Display examples with tabs
        tabs = st.tabs(["All Examples", "Simple Queries", "Complex Queries"])
        
        with tabs[0]:
            show_example_list(similar)
        
        with tabs[1]:
            show_example_list(simple_examples)
        
        with tabs[2]:
            show_example_list(complex_examples)

def show_batch_upload():
    """Interface for batch uploading training examples."""
    st.write("Upload multiple training examples")
    
    # File upload
    uploaded_file = st.file_uploader("Upload JSON or CSV file", type=["json", "csv"])
    
    if uploaded_file:
        try:
            if uploaded_file.name.endswith('.json'):
                data = json.load(uploaded_file)
            else:  # CSV
                data = pd.read_csv(uploaded_file).to_dict('records')
            
            # Preview data
            st.write("Preview of uploaded data:")
            st.write(pd.DataFrame(data[:5]))
            
            # Validation
            validation_results = validate_batch_examples(data)
            
            if validation_results["valid"]:
                if st.button("Import Examples"):
                    import_batch_examples(data)
                    st.success(f"Successfully imported {len(data)} examples!")
            else:
                st.error("Validation errors found:")
                for error in validation_results["errors"]:
                    st.write(f"- {error}")
                    
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

def show_training_quality_analysis():
    """Display training data quality analysis."""
    st.write("Training Data Quality Analysis")
    
    # Get analytics
    analytics = st.session_state.vector_store.get_advanced_analytics()
    recommendations = st.session_state.vector_store.get_learning_recommendations()
    
    # Display metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Examples", analytics["summary_metrics"]["total_training_examples"])
    with col2:
        st.metric("Pattern Coverage", f"{len(analytics['pattern_stats']['most_common_patterns'])}/10")
    with col3:
        st.metric("Avg Complexity", f"{analytics['complexity_stats']['avg_training_complexity']:.2f}")
    
    # Show patterns distribution
    st.write("SQL Patterns Distribution")
    pattern_fig = create_pattern_distribution_chart(analytics["pattern_stats"])
    st.plotly_chart(pattern_fig)
    
    # Show recommendations
    st.write("Improvement Recommendations")
    for rec in recommendations:
        show_recommendation_card(rec)

def show_query_interface():
    """Enhanced query interface with real-time feedback."""
    st.subheader("Ask Questions")
    
    # Context sidebar
    with st.sidebar:
        st.write("Query Context")
        show_context_selector()
    
    # Main query interface
    question = st.text_input("Enter your question:")
    
    if question:
        # Real-time suggestions
        show_realtime_suggestions(question)
        
        # Execute query
        if st.button("Run Query"):
            with st.spinner("Generating SQL and executing query..."):
                result = execute_query_with_feedback(question)
                show_query_results(result)

def show_analytics():
    """Enhanced analytics dashboard."""
    st.subheader("System Analytics")
    
    # Time range selector
    time_range = st.selectbox(
        "Time Range",
        ["Last 24 Hours", "Last Week", "Last Month", "All Time"]
    )
    
    # Get analytics data
    analytics = st.session_state.vector_store.get_advanced_analytics()
    
    # Overview metrics
    show_overview_metrics(analytics)
    
    # Detailed analytics tabs
    tabs = st.tabs([
        "Performance Trends",
        "Pattern Analysis",
        "Schema Coverage",
        "Learning Progress"
    ])
    
    with tabs[0]:
        show_performance_trends(analytics)
    
    with tabs[1]:
        show_pattern_analysis(analytics)
    
    with tabs[2]:
        show_schema_coverage(analytics)
    
    with tabs[3]:
        show_learning_progress(analytics)

def show_overview_metrics(analytics: Dict):
    """Display overview metrics with sparklines."""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        show_metric_card(
            "Success Rate",
            f"{analytics['recent_stats']['success_rate_week']*100:.1f}%",
            analytics['learning_curve']['success_rate_trend']
        )
    
    with col2:
        show_metric_card(
            "Queries/Week",
            analytics['recent_stats']['queries_last_week'],
            trend_data=None  # Add trend data if available
        )
    
    with col3:
        show_metric_card(
            "Avg Complexity",
            f"{analytics['recent_stats']['avg_complexity_week']:.2f}",
            analytics['learning_curve']['complexity_trend']
        )
    
    with col4:
        show_metric_card(
            "Pattern Coverage",
            len(analytics['pattern_stats']['most_common_patterns']),
            trend_data=None  # Add trend data if available
        )

def show_performance_trends(analytics: Dict):
    """Display detailed performance trends."""
    # Success rate over time
    fig = go.Figure()
    
    success_data = analytics['learning_curve']['success_rate_trend']
    fig.add_trace(go.Scatter(
        x=[x[0] for x in success_data],
        y=[x[1] for x in success_data],
        name="Success Rate",
        line=dict(color="green")
    ))
    
    fig.update_layout(
        title="Query Success Rate Over Time",
        xaxis_title="Date",
        yaxis_title="Success Rate"
    )
    
    st.plotly_chart(fig)
    
    # Query complexity distribution
    complexity_fig = create_complexity_distribution(
        analytics['complexity_stats']['complexity_distribution']
    )
    st.plotly_chart(complexity_fig)

def show_pattern_analysis(analytics: Dict):
    """Display SQL pattern analysis."""
    # Pattern usage chart
    pattern_fig = create_pattern_usage_chart(
        analytics['pattern_stats']['most_common_patterns']
    )
    st.plotly_chart(pattern_fig)
    
    # Pattern success rates
    success_fig = create_pattern_success_chart(
        analytics['pattern_stats']['pattern_success_rates']
    )
    st.plotly_chart(success_fig)

def show_schema_coverage(analytics: Dict):
    """Display schema coverage analysis."""
    # Table coverage chart
    table_fig = create_table_coverage_chart(
        analytics['schema_coverage']['table_coverage']
    )
    st.plotly_chart(table_fig)
    
    # Column usage heatmap
    column_fig = create_column_usage_heatmap(
        analytics['schema_coverage']['column_coverage']
    )
    st.plotly_chart(column_fig)

def show_learning_progress(analytics: Dict):
    """Display learning progress metrics."""
    # Learning curve
    fig = create_learning_curve_chart(
        analytics['learning_curve']['success_rate_trend'],
        analytics['learning_curve']['complexity_trend']
    )
    st.plotly_chart(fig)
    
    # System health indicators
    show_system_health_indicators(analytics['system_health'])

def main():
    """Enhanced main Streamlit app."""
    st.title("Text-to-SQL Learning System")
    
    # Initialize engine and vector store
    init_engine()
    
    # Sidebar navigation with icons
    st.sidebar.title("Navigation")
    pages = {
        "Query Database": "🔍",
        "Schema Information": "📊",
        "Training Data": "📚",
        "Analytics": "📈",
        "Settings": "⚙️"
    }
    
    selection = st.sidebar.radio(
        "",
        list(pages.keys()),
        format_func=lambda x: f"{pages[x]} {x}"
    )
    
    # Update session state
    st.session_state.current_page = selection
    
    # Show selected page
    if selection == "Query Database":
        show_query_interface()
    elif selection == "Schema Information":
        show_schema_info()
    elif selection == "Training Data":
        show_training_data()
    elif selection == "Analytics":
        show_analytics()
    elif selection == "Settings":
        show_settings()

if __name__ == "__main__":
    main()
