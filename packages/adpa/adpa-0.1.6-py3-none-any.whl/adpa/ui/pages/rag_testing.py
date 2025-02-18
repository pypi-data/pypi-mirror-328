"""RAG testing interface for the ADPA Framework."""

from typing import Dict, List, Optional, Any
import streamlit as st
from datetime import datetime
import json
from pathlib import Path

from adpa.core.rag import RAGPipeline
from adpa.core.types import Document, Query, Response, TestResult
from adpa.utils.logger import get_logger
from adpa.utils.stability import with_retry, safe_state_operation
from adpa.utils.test_results import TestResultManager
from adpa.database.models.test_result import TestResultRecord
from adpa.ui.config.database import get_db
from adpa.ui.config.rag_testing_config import (
    TestSuite,
    TestCase,
    load_test_suite,
    save_test_suite,
    get_default_config
)

# Setup logging
logger = get_logger(__name__)

# Constants
MAX_HISTORY_ITEMS = 50
DEFAULT_TEST_SUITE_PATH = Path("test_suites")


class RAGTestingUI:
    """RAG testing interface component."""
    
    def __init__(self):
        """Initialize RAG testing interface."""
        self.rag_pipeline = RAGPipeline()
        self.result_manager = TestResultManager()
        self._initialize_session_state()
        self._ensure_test_suite_directory()
    
    def _initialize_session_state(self) -> None:
        """Initialize or restore session state."""
        with safe_state_operation():
            if "test_suites" not in st.session_state:
                st.session_state.test_suites = {}
            if "current_suite" not in st.session_state:
                st.session_state.current_suite = None
            if "test_results" not in st.session_state:
                st.session_state.test_results = {}
            if "error_message" not in st.session_state:
                st.session_state.error_message = None
    
    def _ensure_test_suite_directory(self) -> None:
        """Ensure test suite directory exists."""
        DEFAULT_TEST_SUITE_PATH.mkdir(parents=True, exist_ok=True)
    
    def _load_available_test_suites(self) -> None:
        """Load available test suites from disk."""
        try:
            for path in DEFAULT_TEST_SUITE_PATH.glob("*.json"):
                if path.stem not in st.session_state.test_suites:
                    try:
                        suite = load_test_suite(path)
                        st.session_state.test_suites[path.stem] = suite
                    except Exception as e:
                        logger.error(f"Failed to load test suite {path}: {str(e)}")
        except Exception as e:
            logger.error(f"Failed to load test suites: {str(e)}")
    
    @with_retry(retries=3, delay=1.0)
    def _run_test_case(self, case: TestCase) -> TestResult:
        """Run a single test case.
        
        Args:
            case: Test case to run
            
        Returns:
            Test result
            
        Raises:
            Exception: If test execution fails
        """
        try:
            # Create query
            query = Query(
                text=case.query,
                timestamp=datetime.utcnow(),
                metadata={"test_case_id": case.id}
            )
            
            # Process through pipeline
            response, sources = self.rag_pipeline.process(
                query,
                similarity_threshold=0.8,
                max_sources=5
            )
            
            # Evaluate result
            result = self.result_manager.evaluate_test(
                case=case,
                response=response,
                sources=sources
            )
            
            # Save result
            self._save_test_result(case, result)
            
            return result
            
        except Exception as e:
            logger.error(f"Test case execution failed: {str(e)}")
            raise
    
    def _save_test_result(
        self,
        case: TestCase,
        result: TestResult
    ) -> None:
        """Save test result.
        
        Args:
            case: Test case
            result: Test result
        """
        try:
            # Save to session state
            if case.id not in st.session_state.test_results:
                st.session_state.test_results[case.id] = []
            st.session_state.test_results[case.id].append(result)
            
            # Trim history if needed
            if len(st.session_state.test_results[case.id]) > MAX_HISTORY_ITEMS:
                st.session_state.test_results[case.id].pop(0)
            
            # Save to database
            with get_db() as db:
                record = TestResultRecord(
                    test_case_id=case.id,
                    query_text=case.query,
                    expected_answer=case.expected_answer,
                    actual_answer=result.response.text,
                    metrics=json.dumps(result.metrics),
                    metadata=json.dumps(result.metadata)
                )
                db.add(record)
                db.commit()
                
        except Exception as e:
            logger.error(f"Failed to save test result: {str(e)}")
    
    def _create_test_suite(self) -> None:
        """Create a new test suite."""
        try:
            st.subheader("Create New Test Suite")
            
            # Basic info
            name = st.text_input("Suite Name")
            description = st.text_area("Description")
            version = st.text_input("Version", value="1.0.0")
            
            if st.button("Create Suite"):
                if not name or not description:
                    st.error("Please fill in all required fields.")
                    return
                
                # Create suite
                suite = TestSuite(
                    name=name,
                    description=description,
                    version=version,
                    test_cases=[],
                    config=get_default_config()
                )
                
                # Save to disk
                path = DEFAULT_TEST_SUITE_PATH / f"{name.lower()}.json"
                save_test_suite(suite, path)
                
                # Update session state
                st.session_state.test_suites[name.lower()] = suite
                st.session_state.current_suite = name.lower()
                
                st.success("Test suite created successfully!")
                
        except Exception as e:
            logger.error(f"Failed to create test suite: {str(e)}")
            st.error(f"Failed to create test suite: {str(e)}")
    
    def _add_test_case(self) -> None:
        """Add a test case to current suite."""
        try:
            st.subheader("Add Test Case")
            
            # Basic info
            case_id = st.text_input("Test Case ID")
            query = st.text_area("Query")
            expected = st.text_area("Expected Answer")
            
            if st.button("Add Case"):
                if not case_id or not query or not expected:
                    st.error("Please fill in all required fields.")
                    return
                
                # Create case
                case = TestCase(
                    id=case_id,
                    query=query,
                    expected_answer=expected
                )
                
                # Add to suite
                suite = st.session_state.test_suites[st.session_state.current_suite]
                suite.test_cases.append(case)
                
                # Save suite
                path = DEFAULT_TEST_SUITE_PATH / f"{suite.name.lower()}.json"
                save_test_suite(suite, path)
                
                st.success("Test case added successfully!")
                
        except Exception as e:
            logger.error(f"Failed to add test case: {str(e)}")
            st.error(f"Failed to add test case: {str(e)}")
    
    def _run_test_suite(self) -> None:
        """Run current test suite."""
        try:
            suite = st.session_state.test_suites[st.session_state.current_suite]
            
            with st.spinner("Running test suite..."):
                results = []
                for case in suite.test_cases:
                    result = self._run_test_case(case)
                    results.append(result)
                
                # Display results
                st.subheader("Test Results")
                
                for case, result in zip(suite.test_cases, results):
                    with st.expander(f"Test Case: {case.id}"):
                        st.write("**Query:**", case.query)
                        st.write("**Expected:**", case.expected_answer)
                        st.write("**Actual:**", result.response.text)
                        st.markdown("**Metrics:**")
                        st.json(result.metrics)
                
                # Summary
                success = sum(1 for r in results if r.metrics["accuracy"] > 0.8)
                st.success(f"Tests completed: {success}/{len(results)} passed")
                
        except Exception as e:
            logger.error(f"Failed to run test suite: {str(e)}")
            st.error(f"Failed to run test suite: {str(e)}")
    
    def render(self) -> None:
        """Render the RAG testing interface."""
        st.title("RAG Testing Interface")
        
        # Load available test suites
        self._load_available_test_suites()
        
        # Test suite selection
        st.header("Test Suites")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.session_state.test_suites:
                suite_names = list(st.session_state.test_suites.keys())
                selected = st.selectbox(
                    "Select Test Suite",
                    options=suite_names,
                    index=suite_names.index(st.session_state.current_suite)
                    if st.session_state.current_suite in suite_names
                    else 0
                )
                st.session_state.current_suite = selected
        
        with col2:
            if st.button("Create New Suite"):
                st.session_state.current_suite = None
        
        # Create new suite or work with existing
        if st.session_state.current_suite is None:
            self._create_test_suite()
        else:
            # Add test case
            if st.button("Add Test Case"):
                self._add_test_case()
            
            # Run suite
            if st.button("Run Test Suite"):
                self._run_test_suite()


def main():
    """Main entry point for RAG testing page."""
    try:
        ui = RAGTestingUI()
        ui.render()
    except Exception as e:
        st.error(f"Failed to initialize RAG testing interface: {str(e)}")
        logger.error(f"RAG testing interface error: {str(e)}")


if __name__ == "__main__":
    main()
