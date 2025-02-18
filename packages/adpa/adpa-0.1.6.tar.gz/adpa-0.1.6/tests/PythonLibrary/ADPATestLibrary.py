"""Robot Framework test library for ADPA Framework."""
from typing import Dict, List, Any, Optional
from adpa.core import ADPAFramework
from adpa.agents import BaseAgent
import yaml
import json
import time

class ADPATestLibrary:
    """Test library for ADPA Framework testing."""
    
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    
    def __init__(self):
        self.framework = None
        self.test_data = {}
        self.results = {}
        
    def initialize_framework(self):
        """Initialize ADPA Framework instance."""
        self.framework = ADPAFramework()
        return self.framework is not None
        
    def load_test_configuration(self, config_file: str):
        """Load test configuration from YAML file."""
        with open(config_file, 'r') as f:
            self.config = yaml.safe_load(f)
            
    def get_test_content(self, content_type: str) -> Dict[str, Any]:
        """Get test content for specific ADPA component."""
        content_file = self.config['test_data'][content_type]
        with open(content_file, 'r') as f:
            return json.load(f)
            
    def process_attention(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """Process content through attention component."""
        return self.framework.process_attention(content)
        
    def process_desire(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """Process content through desire component."""
        return self.framework.process_desire(content)
        
    def process_position(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """Process content through position component."""
        return self.framework.process_position(content)
        
    def process_action(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """Process content through action component."""
        return self.framework.process_action(content)
        
    def verify_attention_score(self, result: Dict[str, Any]):
        """Verify attention score is within acceptable range."""
        score = result.get('attention_score', 0)
        assert 0 <= score <= 1, f"Attention score {score} out of range [0,1]"
        
    def verify_desire_score(self, result: Dict[str, Any]):
        """Verify desire score is within acceptable range."""
        score = result.get('desire_score', 0)
        assert 0 <= score <= 1, f"Desire score {score} out of range [0,1]"
        
    def verify_position_score(self, result: Dict[str, Any]):
        """Verify position score is within acceptable range."""
        score = result.get('position_score', 0)
        assert 0 <= score <= 1, f"Position score {score} out of range [0,1]"
        
    def verify_action_score(self, result: Dict[str, Any]):
        """Verify action score is within acceptable range."""
        score = result.get('action_score', 0)
        assert 0 <= score <= 1, f"Action score {score} out of range [0,1]"
        
    def create_custom_agent(self, agent_name: str) -> BaseAgent:
        """Create a custom test agent."""
        class TestAgent(BaseAgent):
            def analyze(self, content: Dict[str, Any]) -> Dict[str, Any]:
                return {
                    'attention_score': 0.8,
                    'desire_score': 0.7,
                    'position_score': 0.9,
                    'action_score': 0.75,
                    'recommendations': ['Test recommendation']
                }
        
        return TestAgent()
        
    def register_custom_agent(self, agent: BaseAgent):
        """Register custom agent with framework."""
        self.framework.register_agent(agent)
        
    def verify_agent_registration(self):
        """Verify agent was properly registered."""
        assert len(self.framework.agents) > 0, "No agents registered"
        
    def create_test_items(self, count: int) -> List[Dict[str, Any]]:
        """Create test items for batch processing."""
        return [{'id': i, 'content': f'Test content {i}'} for i in range(count)]
        
    def process_items(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process multiple items through framework."""
        start_time = time.time()
        results = [self.framework.process(item) for item in items]
        self.processing_time = time.time() - start_time
        return results
        
    def verify_batch_results(self, results: List[Dict[str, Any]]):
        """Verify batch processing results."""
        assert len(results) > 0, "No results returned"
        for result in results:
            assert all(key in result for key in ['attention_score', 'desire_score', 
                                               'position_score', 'action_score'])
            
    def verify_processing_time(self):
        """Verify batch processing time is acceptable."""
        assert hasattr(self, 'processing_time'), "No processing time recorded"
        assert self.processing_time < 30, f"Processing time {self.processing_time}s exceeds limit"
        
    def cleanup_framework_resources(self):
        """Clean up framework resources after testing."""
        if self.framework:
            self.framework.cleanup()
        self.test_data.clear()
        self.results.clear()
