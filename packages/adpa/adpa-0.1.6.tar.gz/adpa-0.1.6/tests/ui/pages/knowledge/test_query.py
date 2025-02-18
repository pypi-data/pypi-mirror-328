"""Tests for knowledge query page."""

import pytest
from unittest.mock import Mock, patch
import streamlit as st
from pathlib import Path
import tempfile

from adpa.ui.pages.knowledge.query import KnowledgeQueryApp
from adpa.ui.utils.state import UIState

@pytest.fixture
def app():
    """Create a test instance of KnowledgeQueryApp."""
    return KnowledgeQueryApp()

@pytest.fixture
def mock_file():
    """Create a mock uploaded file."""
    mock = Mock()
    mock.name = "test.txt"
    mock.getvalue = lambda: b"Test content"
    return mock

def test_setup_session_state(app):
    """Test session state initialization."""
    app.setup_session_state()
    assert 'documents' in st.session_state
    assert 'vector_store' in st.session_state
    assert 'chat_history' in st.session_state
    assert 'agent' in st.session_state

def test_setup_embeddings(app):
    """Test embedding options setup."""
    app.setup_embeddings()
    assert 'OpenAI' in app.embedding_options
    assert 'HuggingFace (all-MiniLM-L6-v2)' in app.embedding_options

def test_setup_vector_stores(app):
    """Test vector store options setup."""
    app.setup_vector_stores()
    assert 'Chroma' in app.vector_store_options
    assert 'FAISS' in app.vector_store_options
    assert 'Milvus' in app.vector_store_options

def test_setup_agents(app):
    """Test agent options setup."""
    app.setup_agents()
    assert 'RAG Agent' in app.agent_options
    assert 'Research Agent' in app.agent_options
    assert 'QA Agent' in app.agent_options

def test_load_document_txt(app, mock_file):
    """Test loading a text document."""
    with patch('tempfile.mkdtemp') as mock_mkdtemp:
        mock_mkdtemp.return_value = tempfile.gettempdir()
        documents = app.load_document(mock_file)
        assert len(documents) > 0

def test_load_document_invalid_type(app):
    """Test loading an invalid document type."""
    mock_file = Mock()
    mock_file.name = "test.invalid"
    with pytest.raises(ValueError):
        app.load_document(mock_file)

def test_process_documents(app):
    """Test document processing."""
    mock_docs = [Mock(page_content="Test content " * 100)]
    processed = app.process_documents(mock_docs)
    assert len(processed) > 1  # Should split into multiple chunks

@patch('streamlit.write')
def test_render_chat_history(mock_write, app):
    """Test chat history rendering."""
    UIState.add_to_chat_history("human", "Test question")
    UIState.add_to_chat_history("ai", "Test answer")
    app.render_chat_history()
    assert mock_write.call_count >= 2

@patch('streamlit.selectbox')
@patch('streamlit.text_input')
def test_agent_query(mock_text_input, mock_selectbox, app):
    """Test agent query processing."""
    # Setup mocks
    mock_text_input.return_value = "Test query"
    mock_selectbox.return_value = "RAG Agent"
    
    # Create mock vector store
    mock_vector_store = Mock()
    UIState.set('vector_store', mock_vector_store)
    
    # Run query
    with patch.object(app.agent_options['RAG Agent'], 'run') as mock_run:
        mock_run.return_value = "Test response"
        app.run()
        
        # Verify agent was called
        chat_history = UIState.get_chat_history()
        assert len(chat_history) > 0
        assert "Test query" in str(chat_history)
