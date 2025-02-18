# -*- coding: utf-8 -*-
"""Test data generation utilities."""

import random
import string
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any

class TestDataGenerator:
    """Generate test data for various test scenarios."""
    
    @staticmethod
    def generate_agent_data(count: int = 1) -> List[Dict[str, Any]]:
        """Generate test agent data.
        
        Args:
            count: Number of agents to generate
            
        Returns:
            List of agent data dictionaries
        """
        agents = []
        for i in range(count):
            agent = {
                'name': f'TestAgent_{i}_{TestDataGenerator._random_string(5)}',
                'prompt': f'Test prompt for agent {i}',
                'model': random.choice(['gpt-4', 'gpt-3.5-turbo']),
                'configuration': {
                    'temperature': round(random.uniform(0, 1), 1),
                    'max_tokens': random.randint(100, 1000)
                }
            }
            agents.append(agent)
        return agents
    
    @staticmethod
    def generate_conversation_data(
        agent_name: str, 
        message_count: int = 5
    ) -> List[Dict[str, Any]]:
        """Generate test conversation data.
        
        Args:
            agent_name: Name of the agent
            message_count: Number of messages to generate
            
        Returns:
            List of conversation messages
        """
        messages = []
        for i in range(message_count):
            message = {
                'agent': agent_name,
                'role': random.choice(['user', 'assistant']),
                'content': f'Test message {i}: {TestDataGenerator._random_string(20)}',
                'timestamp': (
                    datetime.now() - timedelta(minutes=i)
                ).isoformat()
            }
            messages.append(message)
        return messages
    
    @staticmethod
    def generate_tool_data(count: int = 1) -> List[Dict[str, Any]]:
        """Generate test tool data.
        
        Args:
            count: Number of tools to generate
            
        Returns:
            List of tool data dictionaries
        """
        tools = []
        for i in range(count):
            tool = {
                'name': f'TestTool_{i}_{TestDataGenerator._random_string(5)}',
                'description': f'Test tool description {i}',
                'configuration': {
                    'timeout': random.randint(10, 60),
                    'retry_count': random.randint(1, 5)
                }
            }
            tools.append(tool)
        return tools
    
    @staticmethod
    def generate_research_data(count: int = 1) -> List[Dict[str, Any]]:
        """Generate test research data.
        
        Args:
            count: Number of research items to generate
            
        Returns:
            List of research data dictionaries
        """
        items = []
        for i in range(count):
            item = {
                'title': f'Research_{i}_{TestDataGenerator._random_string(10)}',
                'content': TestDataGenerator._random_string(100),
                'url': f'https://example.com/research/{i}',
                'metadata': {
                    'author': f'Author_{TestDataGenerator._random_string(5)}',
                    'date': datetime.now().isoformat(),
                    'tags': [
                        TestDataGenerator._random_string(5) 
                        for _ in range(3)
                    ]
                }
            }
            items.append(item)
        return items
    
    @staticmethod
    def generate_team_data(
        count: int = 1, 
        members_per_team: int = 3
    ) -> List[Dict[str, Any]]:
        """Generate test team data.
        
        Args:
            count: Number of teams to generate
            members_per_team: Number of members per team
            
        Returns:
            List of team data dictionaries
        """
        teams = []
        for i in range(count):
            team = {
                'name': f'TestTeam_{i}_{TestDataGenerator._random_string(5)}',
                'members': [
                    {
                        'name': f'Member_{j}_{TestDataGenerator._random_string(5)}',
                        'role': random.choice(['developer', 'researcher', 'manager']),
                        'skills': [
                            TestDataGenerator._random_string(5) 
                            for _ in range(3)
                        ]
                    }
                    for j in range(members_per_team)
                ]
            }
            teams.append(team)
        return teams
    
    @staticmethod
    def _random_string(length: int) -> str:
        """Generate a random string.
        
        Args:
            length: Length of string to generate
            
        Returns:
            Random string
        """
        return ''.join(
            random.choices(
                string.ascii_letters + string.digits, 
                k=length
            )
        )

def generate_test_user():
    """Generate test user data."""
    return {
        'username': 'test_user',
        'email': 'test@example.com',
        'password': 'test_password'
    }

def generate_test_project():
    """Generate test project data."""
    return {
        'name': 'test_project',
        'description': 'Test project for automated testing'
    }

def generate_test_agent():
    """Generate test agent data."""
    return {
        'name': 'test_agent',
        'model': 'gpt-3.5-turbo',
        'system_prompt': 'You are a helpful assistant.'
    }

def generate_test_tool():
    """Generate test tool data."""
    return {
        'name': 'test_tool',
        'description': 'Test tool for automated testing',
        'type': 'utility'
    }
