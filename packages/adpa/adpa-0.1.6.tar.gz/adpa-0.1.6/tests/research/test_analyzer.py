"""Tests for the research analyzer functionality."""
import pytest
from datetime import datetime
from adpa.research.analyzer import ResearchAnalyzer

@pytest.fixture
def sample_search_results():
    """Create sample search results for testing."""
    return {
        "tavily": [
            {
                "title": "Machine Learning Advances",
                "content": "Significant advances in AI research. Important findings show improvements.",
                "published": "2024-01-15T10:00:00Z"
            }
        ],
        "serper": [
            {
                "title": "Data Science Trends",
                "snippet": "Research indicates new trends in data science. Key developments in 2024.",
                "published": "2024-01-20T15:30:00Z"
            }
        ],
        "google_scholar": [
            {
                "title": "Neural Networks Study",
                "summary": "Study reveals breakthrough in neural network architecture.",
                "publish_date": "2024-01-10T08:00:00Z"
            }
        ]
    }

@pytest.fixture
def analyzer():
    """Create an analyzer instance."""
    return ResearchAnalyzer()

def test_extract_key_findings(analyzer, sample_search_results):
    """Test extraction of key findings from search results."""
    findings = analyzer.extract_key_findings(sample_search_results)
    
    assert "source_distribution" in findings
    assert "top_topics" in findings
    assert "date_range" in findings
    assert "key_points" in findings
    
    # Check source distribution
    assert findings["source_distribution"]["tavily"] == 1
    assert findings["source_distribution"]["serper"] == 1
    assert findings["source_distribution"]["google_scholar"] == 1
    
    # Check topics extraction
    topics = [topic for topic, _ in findings["top_topics"]]
    assert "Machine Learning" in topics or "Data Science" in topics
    
    # Check date range
    assert findings["date_range"]["earliest"] is not None
    assert findings["date_range"]["latest"] is not None

def test_extract_topics(analyzer):
    """Test topic extraction from text."""
    text = "Artificial Intelligence and Machine Learning are transforming Data Science"
    topics = analyzer._extract_topics(text)
    
    assert "Artificial Intelligence" in topics
    assert "Machine Learning" in topics
    assert "Data Science" in topics
    
    # Should not extract short or lowercase phrases
    assert "and" not in topics
    assert "are" not in topics

def test_extract_key_points(analyzer):
    """Test key points extraction from text."""
    text = """
    This is a regular sentence. Important findings show that AI is advancing.
    Research indicates significant progress. This is another regular sentence.
    The study reveals breakthrough results. Not an important sentence.
    """
    
    key_points = analyzer._extract_key_points(text)
    
    assert len(key_points) == 3
    assert any("Important findings" in point for point in key_points)
    assert any("Research indicates" in point for point in key_points)
    assert any("study reveals" in point for point in key_points)
    assert not any("regular sentence" in point for point in key_points)

def test_get_date_range(analyzer):
    """Test date range extraction."""
    dates = [
        "2024-01-01T10:00:00Z",
        "2024-01-15T15:30:00Z",
        "2024-01-30T20:00:00Z"
    ]
    
    date_range = analyzer._get_date_range(dates)
    
    assert date_range["earliest"] == "2024-01-01T10:00:00+00:00"
    assert date_range["latest"] == "2024-01-30T20:00:00+00:00"

def test_get_date_range_empty(analyzer):
    """Test date range extraction with empty input."""
    date_range = analyzer._get_date_range([])
    
    assert date_range["earliest"] is None
    assert date_range["latest"] is None

def test_get_date_range_invalid_dates(analyzer):
    """Test date range extraction with invalid dates."""
    dates = [
        "invalid_date",
        "2024-01-15T15:30:00Z",
        "not_a_date"
    ]
    
    date_range = analyzer._get_date_range(dates)
    
    assert date_range["earliest"] == "2024-01-15T15:30:00+00:00"
    assert date_range["latest"] == "2024-01-15T15:30:00+00:00"

def test_generate_summary(analyzer):
    """Test summary generation from findings."""
    findings = {
        "source_distribution": {"tavily": 2, "serper": 1},
        "date_range": {
            "earliest": "2024-01-01T00:00:00Z",
            "latest": "2024-01-31T00:00:00Z"
        },
        "top_topics": [
            ("Machine Learning", 5),
            ("Artificial Intelligence", 3),
            ("Data Science", 2)
        ],
        "key_points": [
            "Important finding about AI",
            "Significant progress in ML",
            "Key developments in 2024"
        ]
    }
    
    summary = analyzer.generate_summary(findings)
    
    assert "Sources:" in summary
    assert "Date Range:" in summary
    assert "Main Topics:" in summary
    assert "Key Points:" in summary
    
    assert "tavily (2 results)" in summary
    assert "Machine Learning (5 mentions)" in summary
    assert "1. Important finding about AI" in summary

def test_generate_summary_empty_findings(analyzer):
    """Test summary generation with empty findings."""
    findings = {
        "source_distribution": {},
        "date_range": {"earliest": None, "latest": None},
        "top_topics": [],
        "key_points": []
    }
    
    summary = analyzer.generate_summary(findings)
    
    assert summary.strip() != ""  # Should not be completely empty
    assert "Key Points:" not in summary  # Should not include empty sections
