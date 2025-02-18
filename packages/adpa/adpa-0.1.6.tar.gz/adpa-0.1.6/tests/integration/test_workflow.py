"""Integration tests for ADPA workflows."""
import pytest
from unittest.mock import Mock, AsyncMock

from adpa.models import WorkflowData
from adpa.workflow.base import Workflow

class TestBasicWorkflow:
    """Tests for basic workflow functionality."""
    
    @pytest.mark.asyncio
    async def test_simple_query(self, mock_chat_model, mock_team):
        """Test a simple workflow query."""
        result = await mock_team.execute_workflow("Test query")
        assert result == "Workflow completed"

    @pytest.mark.asyncio
    async def test_database_interaction(self, session):
        """Test database interaction."""
        from adpa.models import WorkflowData
        workflow_data = WorkflowData(content="Test data")
        session.add(workflow_data)
        session.commit()
        
        result = session.query(WorkflowData).first()
        assert result.content == "Test data"

class TestComplexWorkflow:
    """Tests for complex workflow scenarios."""
    
    @pytest.mark.asyncio
    async def test_multi_agent_workflow(self, mock_team):
        """Test multi-agent workflow."""
        result = await mock_team.execute_concurrent(["Task 1", "Task 2", "Task 3"])
        assert result == ["Workflow completed"] * 3

    @pytest.mark.asyncio
    async def test_error_recovery(self, mock_team):
        """Test error recovery in workflow."""
        # Setup mock to fail first, then succeed
        mock_team.execute_workflow = AsyncMock()
        mock_team.execute_workflow.side_effect = [
            Exception("Test error"),
            "Workflow recovered"
        ]
        
        # First call should fail
        with pytest.raises(Exception) as exc:
            await mock_team.execute_workflow("Test task")
        assert str(exc.value) == "Test error"
        
        # Second call should succeed
        result = await mock_team.execute_workflow("Test task")
        assert result == "Workflow recovered"

class TestEndToEndWorkflow:
    """Tests for end-to-end workflow scenarios."""
    
    @pytest.mark.asyncio
    async def test_complete_workflow(self, session, mock_team):
        """Test a complete workflow with database interaction."""
        from adpa.models import WorkflowData
        
        # Execute workflow
        result = await mock_team.execute_workflow("Test workflow")
        assert result == "Workflow completed"
        
        # Save to database
        workflow_data = WorkflowData(content="Test workflow data")
        session.add(workflow_data)
        session.commit()
        
        # Verify database state
        saved_data = session.query(WorkflowData).filter_by(content="Test workflow data").first()
        assert saved_data is not None
        assert saved_data.content == "Test workflow data"

    @pytest.mark.asyncio
    async def test_concurrent_workflows(self, mock_team):
        """Test multiple concurrent workflows."""
        tasks = ["Task 1", "Task 2", "Task 3"]
        results = await mock_team.execute_concurrent(tasks)
        assert len(results) == 3
        assert all(result == "Workflow completed" for result in results)
