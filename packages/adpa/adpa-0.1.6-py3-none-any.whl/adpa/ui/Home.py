"""ADPA Framework UI Home Page."""

import streamlit as st
from pathlib import Path

def main():
    """Main function for the home page."""
    st.set_page_config(
        page_title="ADPA Framework",
        page_icon="🧠",
        layout="wide"
    )

    # Load custom CSS
    css_path = Path(__file__).parent / "styles" / "base.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Header
    st.title("ADPA Framework")
    st.markdown("### Advanced Data Processing and Analysis Framework")

    # Main sections
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔍 Knowledge Query")
        st.write("""
        Access and query your knowledge base using natural language.
        Get instant answers with source citations.
        """)
        st.button("Go to Knowledge Query", key="knowledge_query")

        st.subheader("🤖 RAG Testing")
        st.write("""
        Test and evaluate RAG agents with different configurations.
        Analyze performance and fine-tune your setup.
        """)
        st.button("Go to RAG Testing", key="rag_testing")

    with col2:
        st.subheader("💾 Vector Store Management")
        st.write("""
        Manage your vector stores, ingest data, and optimize indices.
        Monitor performance and usage statistics.
        """)
        st.button("Go to Vector Store", key="vector_store")

        st.subheader("💡 Store Advisor")
        st.write("""
        Get recommendations for schema design and query optimization.
        Learn best practices for your specific use case.
        """)
        st.button("Go to Store Advisor", key="store_advisor")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
        <p>ADPA Framework v1.4.0 | Documentation | GitHub | Support</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
