"""Tests for RAG testing interface."""

import pytest
from unittest.mock import Mock, patch
import streamlit as st
import tempfile
from pathlib import Path

from adpa.ui.pages.rag.testing import RAGTestingApp
from adpa.ui.utils.state import UIState
from adpa.knowledge import EnhancedVectorStore, VectorStoreConfig
from adpa.research import RAGResearcher

@pytest.fixture
def app():
    """Create a test instance of RAGTestingApp."""
    return RAGTestingApp()

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
    assert UIState.get('vector_store') is None
    assert UIState.get('uploaded_files') == []
    assert UIState.get('researcher') is None
    assert UIState.get('chat_history') == []

def test_setup_config(app):
    """Test configuration setup."""
    app.setup_config()
    assert app.config.store_type == "CHROMA"
    assert app.config.embedding_model == "text-embedding-ada-002"
    assert app.config.chunk_size == 1000
    assert app.config.chunk_overlap == 200

def test_initialize_vector_store(app):
    """Test vector store initialization."""
    store = app.initialize_vector_store()
    assert isinstance(store, EnhancedVectorStore)
    assert UIState.get('vector_store') is not None

def test_initialize_researcher(app):
    """Test researcher initialization."""
    researcher = app.initialize_researcher()
    assert isinstance(researcher, RAGResearcher)
    assert UIState.get('researcher') is not None

def test_process_uploaded_file_valid(app, mock_file):
    """Test processing a valid uploaded file."""
    with patch('pathlib.Path.write_bytes'):
        result = app.process_uploaded_file(mock_file)
        assert result is True
        assert mock_file.name in UIState.get('uploaded_files', [])

def test_process_uploaded_file_invalid(app):
    """Test processing an invalid uploaded file."""
    mock_file = Mock()
    mock_file.name = "test.invalid"
    mock_file.getvalue = lambda: b"Test content"
    
    result = app.process_uploaded_file(mock_file)
    assert result is False
    assert UIState.get('uploaded_files', []) == []

@patch('streamlit.text')
def test_display_file_list(mock_text, app):
    """Test file list display."""
    UIState.set('uploaded_files', ['test1.txt', 'test2.txt'])
    app.display_file_list()
    assert mock_text.call_count >= 2

@patch('streamlit.write')
def test_display_chat_history(mock_write, app):
    """Test chat history display."""
    UIState.add_to_chat_history("user", "Test question")
    UIState.add_to_chat_history("assistant", "Test answer", {"sources": ["doc1.txt"]})
    app.display_chat_history()
    assert mock_write.call_count >= 2

def test_query_documents(app):
    """Test document querying."""
    # Setup mock researcher
    mock_researcher = Mock()
    mock_response = Mock()
    mock_response.answer = "Test answer"
    mock_response.sources = ["doc1.txt"]
    mock_researcher.research.return_value = mock_response
    
    with patch.object(app, 'initialize_researcher', return_value=mock_researcher):
        app.query_documents("Test query")
        
        # Verify chat history was updated
        chat_history = UIState.get_chat_history()
        assert len(chat_history) == 2
        assert chat_history[0]["content"] == "Test query"
        assert chat_history[1]["content"] == "Test answer"

@patch('streamlit.sidebar')
@patch('streamlit.file_uploader')
def test_render(mock_file_uploader, mock_sidebar, app):
    """Test interface rendering."""
    # Setup mock file uploader
    mock_file = Mock()
    mock_file.name = "test.txt"
    mock_file_uploader.return_value = [mock_file]
    
    # Setup uploaded files
    UIState.set('uploaded_files', ['test.txt'])
    
    with patch.object(app, 'process_uploaded_file', return_value=True):
        app.render()
        
        # Verify file was processed
        assert mock_file_uploader.called
        assert UIState.get('uploaded_files') == ['test.txt']
