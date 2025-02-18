"""Test the research engine module."""

import unittest
import os
import sys
from pathlib import Path
import asyncio
from unittest.mock import patch, MagicMock, create_autospec
from tests.unit.test_helpers import async_test

# Add the project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from adpa.research.search import ResearchEngine

class TestResearchEngine(unittest.TestCase):
    """Test cases for ResearchEngine class."""

    def setUp(self):
        """Set up test environment."""
        # Store original environment
        self.original_env = dict(os.environ)
        
        # Clear API keys for clean test environment
        for key in ['TAVILY_API_KEY', 'YOUTUBE_API_KEY', 'NEWS_API_KEY']:
            if key in os.environ:
                del os.environ[key]
                
        self.engine = ResearchEngine()

    def tearDown(self):
        """Clean up after each test."""
        # Restore original environment
        os.environ.clear()
        os.environ.update(self.original_env)

    def test_initialization(self):
        """Test engine initialization."""
        self.assertIsNotNone(self.engine.tools)
        # Should only have ArXiv tool by default (no API keys)
        self.assertEqual(len(self.engine.tools), 1)

    @patch.dict(os.environ, {'TAVILY_API_KEY': 'test_key'}, clear=True)
    def test_tavily_search(self):
        """Test Tavily search integration."""
        with patch('adpa.research.search.TavilySearchResults') as mock_tavily:
            # Create a new engine to trigger tool initialization with mock
            engine = ResearchEngine()
            
            # Verify Tavily tool was initialized
            mock_tavily.assert_called_once_with(api_key='test_key')
            self.assertEqual(len(engine.tools), 2)  # Tavily and ArXiv

    def test_arxiv_search(self):
        """Test arXiv search integration."""
        with patch('adpa.research.search.ArxivQueryRun') as mock_arxiv:
            # Create a new engine to trigger tool initialization with mock
            engine = ResearchEngine()
            
            # Verify ArXiv tool was initialized
            mock_arxiv.assert_called_once()
            self.assertEqual(len(engine.tools), 1)  # Only ArXiv (no API keys)

    @patch.dict(os.environ, {'YOUTUBE_API_KEY': 'test_key'}, clear=True)
    def test_youtube_search(self):
        """Test YouTube search integration."""
        with patch('adpa.research.search.YouTubeSearchTool') as mock_youtube:
            # Create a new engine to trigger tool initialization with mock
            engine = ResearchEngine()
            
            # Verify YouTube tool was initialized
            mock_youtube.assert_called_once_with(api_key='test_key')
            self.assertEqual(len(engine.tools), 2)  # YouTube and ArXiv

    @async_test
    async def test_search(self):
        """Test combined search functionality."""
        # Create a mock tool
        mock_tool = MagicMock()
        mock_tool.__class__.__name__ = "MockTool"
        
        # Setup the mock to handle both async and sync calls
        async def mock_ainvoke(*args, **kwargs):
            return [{"title": "Test Result"}]
            
        def mock_invoke(*args, **kwargs):
            return [{"title": "Test Result"}]
            
        mock_tool.ainvoke = mock_ainvoke
        mock_tool.invoke = mock_invoke
        
        # Add mock tool to engine
        self.engine.tools = [mock_tool]
        
        # Perform search
        results = await self.engine.search("test query")
        
        # Verify results
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Test Result")
        self.assertEqual(results[0]["source"], "MockTool")

    def test_format_results(self):
        """Test result formatting."""
        results = [
            {
                "source": "TestTool",
                "title": "Test Title",
                "content": "Test Content",
                "url": "https://example.com"
            }
        ]
        
        formatted = self.engine.format_results(results)
        self.assertIn("Source: TestTool", formatted)
        self.assertIn("Title: Test Title", formatted)
        self.assertIn("Content: Test Content", formatted)
        self.assertIn("URL: https://example.com", formatted)

    def test_parse_tool_results(self):
        """Test parsing of string results."""
        test_string = "Test result string"
        parsed = self.engine._parse_tool_results(test_string)
        self.assertEqual(len(parsed), 1)
        self.assertEqual(parsed[0]["content"], test_string)

def async_test(coro):
    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(coro(*args, **kwargs))
    return wrapper

if __name__ == '__main__':
    unittest.main()
