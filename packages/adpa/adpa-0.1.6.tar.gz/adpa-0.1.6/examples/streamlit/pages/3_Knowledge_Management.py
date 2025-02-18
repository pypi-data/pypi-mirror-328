import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Knowledge Management - ADPA Framework",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Knowledge Management")

# Main Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "Knowledge Overview",
    "Document Management",
    "Vector Store",
    "Analytics"
])

with tab1:
    st.header("Knowledge Overview")
    
    # Quick Stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Documents", "1,245", "↑ 23")
    with col2:
        st.metric("Vector Embeddings", "85,632", "↑ 156")
    with col3:
        st.metric("Search Queries/Hour", "342", "↑ 12")
    with col4:
        st.metric("Avg Response Time", "0.12s", "↓ 0.02s")
    
    # Knowledge Categories
    st.subheader("Knowledge Categories")
    categories = {
        "Technical Documentation": {
            "documents": 456,
            "embeddings": 32450,
            "last_updated": "2024-01-15",
            "status": "Active"
        },
        "API References": {
            "documents": 234,
            "embeddings": 18920,
            "last_updated": "2024-01-14",
            "status": "Active"
        },
        "User Guides": {
            "documents": 189,
            "embeddings": 15680,
            "last_updated": "2024-01-16",
            "status": "Active"
        },
        "Training Data": {
            "documents": 366,
            "embeddings": 18582,
            "last_updated": "2024-01-13",
            "status": "Active"
        }
    }
    
    for category, details in categories.items():
        with st.expander(category, expanded=True):
            col1, col2, col3, col4, col5 = st.columns([2,1,1,1,1])
            with col1:
                st.write(f"**{category}**")
            with col2:
                st.write(f"Docs: {details['documents']}")
            with col3:
                st.write(f"Vectors: {details['embeddings']}")
            with col4:
                st.write(f"Updated: {details['last_updated']}")
            with col5:
                status_color = "🟢" if details['status'] == 'Active' else "🔴"
                st.write(f"{status_color} {details['status']}")

with tab2:
    st.header("Document Management")
    
    # Document Actions
    col1, col2 = st.columns([3,1])
    with col1:
        st.subheader("Manage Documents")
    with col2:
        st.button("➕ Upload Documents", type="primary")
    
    # Document Browser
    documents = {
        "API Documentation": {
            "type": "Technical",
            "format": "Markdown",
            "size": "1.2 MB",
            "vectors": 850,
            "last_accessed": "2024-01-16"
        },
        "User Manual": {
            "type": "Guide",
            "format": "PDF",
            "size": "2.8 MB",
            "vectors": 1240,
            "last_accessed": "2024-01-15"
        },
        "Training Dataset": {
            "type": "Data",
            "format": "JSON",
            "size": "4.5 MB",
            "vectors": 2100,
            "last_accessed": "2024-01-14"
        },
        "Code Examples": {
            "type": "Technical",
            "format": "Python",
            "size": "0.8 MB",
            "vectors": 620,
            "last_accessed": "2024-01-16"
        }
    }
    
    for doc, details in documents.items():
        with st.expander(doc):
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Document Details**")
                st.text_input("Document Name", value=doc, key=f"name_{doc}")
                st.selectbox(
                    "Document Type",
                    ["Technical", "Guide", "Data", "Reference"],
                    key=f"type_{doc}"
                )
                st.text_area(
                    "Description",
                    value="Document description...",
                    key=f"desc_{doc}"
                )
            with col2:
                st.write("**Processing Settings**")
                st.selectbox(
                    "Processing Model",
                    ["text-embedding-3-small", "text-embedding-3-large"],
                    key=f"model_{doc}"
                )
                st.number_input(
                    "Chunk Size",
                    100, 2000, 512,
                    key=f"chunk_{doc}"
                )
                st.number_input(
                    "Overlap",
                    0, 200, 50,
                    key=f"overlap_{doc}"
                )
            
            # Document Actions
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.button("Update", key=f"update_{doc}")
            with col2:
                st.button("Reprocess", key=f"reprocess_{doc}")
            with col3:
                st.button("Download", key=f"download_{doc}")
            with col4:
                st.button("Delete", key=f"delete_{doc}")

with tab3:
    st.header("Vector Store")
    
    # Vector Store Actions
    col1, col2 = st.columns([3,1])
    with col1:
        st.subheader("Vector Database")
    with col2:
        st.button("🔄 Reindex All", type="primary")
    
    # Vector Store Settings
    with st.expander("Vector Store Configuration"):
        col1, col2 = st.columns(2)
        with col1:
            st.selectbox(
                "Vector Store Type",
                ["Chroma", "FAISS", "Pinecone", "Weaviate"]
            )
            st.text_input("Database URL")
            st.text_input("API Key", type="password")
        with col2:
            st.number_input("Dimension Size", 384, 1536, 1536)
            st.number_input("Index Shards", 1, 10, 3)
            st.selectbox("Distance Metric", ["cosine", "euclidean", "dot"])
    
    # Collection Management
    st.subheader("Collections")
    collections = {
        "technical_docs": {
            "vectors": 32450,
            "dimension": 1536,
            "size": "124 MB"
        },
        "user_guides": {
            "vectors": 15680,
            "dimension": 1536,
            "size": "58 MB"
        },
        "training_data": {
            "vectors": 18582,
            "dimension": 1536,
            "size": "72 MB"
        }
    }
    
    for collection, details in collections.items():
        with st.expander(collection):
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Collection Details**")
                st.text_input("Collection Name", value=collection, key=f"name_{collection}")
                st.text_area(
                    "Description",
                    value="Collection description...",
                    key=f"desc_{collection}"
                )
            with col2:
                st.write("**Statistics**")
                st.write(f"Vectors: {details['vectors']}")
                st.write(f"Dimension: {details['dimension']}")
                st.write(f"Size: {details['size']}")
            
            # Collection Actions
            col1, col2, col3 = st.columns(3)
            with col1:
                st.button("Optimize", key=f"optimize_{collection}")
            with col2:
                st.button("Backup", key=f"backup_{collection}")
            with col3:
                st.button("Delete", key=f"delete_{collection}")

with tab4:
    st.header("Knowledge Analytics")
    
    # Time Range Selection
    col1, col2 = st.columns([3,1])
    with col1:
        st.subheader("Usage Analytics")
    with col2:
        timeframe = st.selectbox(
            "Timeframe",
            ["Last Hour", "Last 24 Hours", "Last 7 Days", "Last 30 Days"]
        )
    
    # Analytics Charts
    col1, col2 = st.columns(2)
    
    # Query Volume
    with col1:
        times = [datetime.now() - timedelta(hours=i) for i in range(24)]
        query_data = {
            'Technical Docs': [320 + (i % 50) for i in range(24)],
            'User Guides': [280 + (i % 40) for i in range(24)],
            'Training Data': [180 + (i % 30) for i in range(24)]
        }
        
        fig = go.Figure()
        for category, data in query_data.items():
            fig.add_trace(go.Scatter(
                x=times,
                y=data,
                mode='lines',
                name=category
            ))
        fig.update_layout(title="Query Volume by Category")
        st.plotly_chart(fig)
    
    # Response Time
    with col2:
        response_data = {
            'Technical Docs': [0.12 + (i % 5) * 0.01 for i in range(24)],
            'User Guides': [0.11 + (i % 4) * 0.01 for i in range(24)],
            'Training Data': [0.13 + (i % 6) * 0.01 for i in range(24)]
        }
        
        fig = go.Figure()
        for category, data in response_data.items():
            fig.add_trace(go.Scatter(
                x=times,
                y=data,
                mode='lines',
                name=category
            ))
        fig.update_layout(title="Response Time by Category")
        st.plotly_chart(fig)
    
    # Usage Distribution
    st.subheader("Usage Distribution")
    usage_data = pd.DataFrame({
        'Category': list(categories.keys()),
        'Documents': [d['documents'] for d in categories.values()],
        'Embeddings': [d['embeddings'] for d in categories.values()]
    })
    
    fig = px.treemap(
        usage_data,
        path=['Category'],
        values='Documents',
        color='Embeddings',
        title="Knowledge Base Distribution"
    )
    st.plotly_chart(fig)

# Sidebar
with st.sidebar:
    st.header("Quick Actions")
    
    # Knowledge Actions
    st.subheader("Documents")
    col1, col2 = st.columns(2)
    with col1:
        st.button("Import")
    with col2:
        st.button("Export")
    
    # Vector Store
    st.subheader("Vector Store")
    col1, col2 = st.columns(2)
    with col1:
        st.button("Backup")
    with col2:
        st.button("Restore")
    
    # Monitoring
    st.subheader("Monitoring")
    st.toggle("Auto Refresh", value=True)
    st.number_input("Refresh Interval (s)", 1, 3600, 60)
    
    # Documentation
    st.subheader("Help")
    st.markdown("[Knowledge Base Guide](https://docs.adpa.dev/knowledge)")
    st.markdown("[Vector Store Guide](https://docs.adpa.dev/vectors)")
    st.markdown("[Best Practices](https://docs.adpa.dev/best-practices)")
