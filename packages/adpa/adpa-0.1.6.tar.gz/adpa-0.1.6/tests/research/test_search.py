"""Tests for the research search functionality."""
import os
import pytest
from unittest.mock import patch, Mock, AsyncMock, MagicMock
from adpa.research.search import ResearchEngine

@pytest.mark.asyncio
async def test_search_with_tavily():
    """Test search using Tavily API."""
    mock_tavily_response = {
        'results': [
            {
                'title': 'Test Article',
                'url': 'https://example.com/article',
                'content': 'Test content'
            }
        ]
    }

    with patch('tavily.TavilyClient') as mock_client:
        mock_client.return_value.search.return_value = mock_tavily_response
        engine = ResearchEngine()
        engine.tavily_client = mock_client.return_value
        results = await engine.tavily_search('test query')
        
        assert len(results) == 1
        assert results[0]['title'] == 'Test Article'
        assert results[0]['content'] == 'Test content'

@pytest.mark.asyncio
async def test_search_with_serper():
    """Test search using Serper API."""
    mock_serper_response = {
        'organic': [
            {
                'title': 'Test Article',
                'link': 'https://example.com/article',
                'snippet': 'Test content'
            }
        ]
    }

    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.json = AsyncMock(return_value=mock_serper_response)

    mock_session = AsyncMock()
    mock_session.__aenter__.return_value = mock_session
    mock_session.post = AsyncMock()
    mock_session.post.return_value = mock_response
    mock_response.__aenter__ = AsyncMock(return_value=mock_response)

    with patch('aiohttp.ClientSession', return_value=mock_session):
        engine = ResearchEngine()
        results = await engine.serper_search('test query')
        
        assert len(results) == 1
        assert results[0]['title'] == 'Test Article'
        assert results[0]['snippet'] == 'Test content'

@pytest.mark.asyncio
async def test_search_with_serpapi():
    """Test search using SerpAPI."""
    mock_serpapi_response = {
        'organic_results': [
            {
                'title': 'Test Article',
                'link': 'https://example.com/article',
                'snippet': 'Test content'
            }
        ]
    }

    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.json = AsyncMock(return_value=mock_serpapi_response)

    mock_session = AsyncMock()
    mock_session.__aenter__.return_value = mock_session
    mock_session.get = AsyncMock()
    mock_session.get.return_value = mock_response
    mock_response.__aenter__ = AsyncMock(return_value=mock_response)

    with patch('aiohttp.ClientSession', return_value=mock_session):
        engine = ResearchEngine()
        results = await engine.serpapi_search('test query')
        
        assert len(results) == 1
        assert results[0]['title'] == 'Test Article'
        assert results[0]['snippet'] == 'Test content'

@pytest.mark.asyncio
async def test_extract_content_with_scrapingbee():
    """Test content extraction using ScrapingBee."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b'{"title": "Test Title", "content": "Test content"}'

    mock_client = Mock()
    mock_client.get.return_value = mock_response

    with patch('scrapingbee.ScrapingBeeClient', return_value=mock_client):
        engine = ResearchEngine()
        engine.scrapingbee_client = mock_client
        content = await engine.scrapingbee_extract('https://example.com')
        
        assert content['title'] == 'Test Title'
        assert content['content'] == 'Test content'

@pytest.fixture
def research_engine():
    """Create a research engine instance with mocked clients."""
    engine = ResearchEngine()
    engine.tavily_client = Mock()
    engine.scrapingbee_client = Mock()
    return engine

@pytest.mark.asyncio
async def test_tavily_search(research_engine):
    """Test Tavily search functionality."""
    # Mock response
    research_engine.tavily_client.search.return_value = {
        "results": [
            {"title": "Test Result", "content": "Test Content"}
        ]
    }

    results = await research_engine.tavily_search("test query")
    
    assert len(results) == 1
    assert results[0]["title"] == "Test Result"
    assert results[0]["content"] == "Test Content"

@pytest.mark.asyncio
async def test_serper_search(research_engine):
    """Test Serper search functionality."""
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.json = AsyncMock(return_value={
        "organic": [
            {"title": "Test Result", "snippet": "Test Snippet"}
        ]
    })

    mock_session = AsyncMock()
    mock_session.__aenter__.return_value = mock_session
    mock_session.post = AsyncMock()
    mock_session.post.return_value = mock_response
    mock_response.__aenter__ = AsyncMock(return_value=mock_response)

    with patch("aiohttp.ClientSession", return_value=mock_session):
        results = await research_engine.serper_search("test query")
        
        assert len(results) == 1
        assert results[0]["title"] == "Test Result"
        assert results[0]["snippet"] == "Test Snippet"

@pytest.mark.asyncio
async def test_serpapi_search(research_engine):
    """Test SerpAPI search functionality."""
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.json = AsyncMock(return_value={
        "organic_results": [
            {"title": "Test Result", "snippet": "Test Snippet"}
        ]
    })

    mock_session = AsyncMock()
    mock_session.__aenter__.return_value = mock_session
    mock_session.get = AsyncMock()
    mock_session.get.return_value = mock_response
    mock_response.__aenter__ = AsyncMock(return_value=mock_response)

    with patch("aiohttp.ClientSession", return_value=mock_session):
        results = await research_engine.serpapi_search("test query")
        
        assert len(results) == 1
        assert results[0]["title"] == "Test Result"
        assert results[0]["snippet"] == "Test Snippet"

@pytest.mark.asyncio
async def test_scrapingbee_extract(research_engine):
    """Test ScrapingBee content extraction."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b'{"title": "Test Title", "content": "Test Content"}'

    research_engine.scrapingbee_client.get.return_value = mock_response

    result = await research_engine.scrapingbee_extract("http://test.com")
    
    assert result["title"] == "Test Title"
    assert result["content"] == "Test Content"

@pytest.mark.asyncio
async def test_comprehensive_search(research_engine):
    """Test comprehensive search functionality."""
    # Mock individual search results
    research_engine.tavily_search = AsyncMock(return_value=[{"source": "tavily"}])
    research_engine.serper_search = AsyncMock(return_value=[{"source": "serper"}])
    research_engine.serpapi_search = AsyncMock(return_value=[{"source": "serpapi"}])
    research_engine.duckduckgo_search = AsyncMock(return_value=[{"source": "duckduckgo"}])
    research_engine.arxiv_search = AsyncMock(return_value=[{"source": "arxiv"}])
    research_engine.google_scholar_search = AsyncMock(return_value=[{"source": "scholar"}])

    results = await research_engine.comprehensive_search("test query", include_academic=True)
    
    assert "tavily" in results
    assert "serper" in results
    assert "serpapi" in results
    assert "duckduckgo" in results
    assert "arxiv" in results
    assert "google_scholar" in results
    
    for source, source_results in results.items():
        assert len(source_results) == 1
        assert source_results[0]["source"] == source.replace("_", "") if source != "google_scholar" else "scholar"

@pytest.mark.asyncio
async def test_extract_article_content(research_engine):
    """Test article content extraction."""
    # Mock ScrapingBee extraction
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b'{"title": "Test Title", "content": "Test Content"}'
    research_engine.scrapingbee_client.get.return_value = mock_response

    # Mock newspaper3k
    mock_article = Mock()
    mock_article.title = "Test Title"
    mock_article.text = "Test Text"
    mock_article.summary = "Test Summary"
    mock_article.keywords = ["test", "keywords"]
    mock_article.authors = ["Test Author"]
    mock_article.publish_date = None
    mock_article.download = Mock()
    mock_article.parse = Mock()
    mock_article.nlp = Mock()

    with patch("newspaper.Article", return_value=mock_article):
        result = await research_engine.extract_article_content("http://test.com")
        
        assert result["title"] == "Test Title"
        assert result["content"] == "Test Content"

@pytest.mark.asyncio
async def test_error_handling(research_engine):
    """Test error handling in search functions."""
    # Mock a failed search
    research_engine.tavily_client.search.side_effect = Exception("API Error")

    results = await research_engine.tavily_search("test query")
    assert results == []  # Should return empty list instead of raising
