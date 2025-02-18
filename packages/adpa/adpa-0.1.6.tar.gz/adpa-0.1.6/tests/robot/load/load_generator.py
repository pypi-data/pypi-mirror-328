"""Load generator for performance testing."""
import asyncio
import aiohttp
import time
import random
import json
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass

@dataclass
class LoadConfig:
    """Configuration for load test."""
    users: int
    ramp_up: int
    duration: int
    target_rps: Optional[int] = None
    think_time: Optional[float] = None

class LoadGenerator:
    """Generates load for performance testing."""

    def __init__(self, config: LoadConfig):
        """Initialize load generator."""
        self.config = config
        self.active_users = 0
        self.start_time = None
        self.metrics = {
            'requests': 0,
            'errors': 0,
            'response_times': [],
            'timeouts': 0
        }
        self.session = None
        self.running = False
        self.logger = logging.getLogger(__name__)

    async def start(self):
        """Start load generation."""
        self.start_time = time.time()
        self.running = True
        self.session = aiohttp.ClientSession()
        
        # Start user tasks
        user_tasks = []
        users_per_second = self.config.users / self.config.ramp_up
        
        for i in range(self.config.users):
            delay = i / users_per_second
            user_task = asyncio.create_task(self._user_task(i, delay))
            user_tasks.append(user_task)
            
        # Start metrics collection
        metrics_task = asyncio.create_task(self._collect_metrics())
        
        # Wait for completion
        await asyncio.gather(*user_tasks, metrics_task)
        await self.session.close()

    async def _user_task(self, user_id: int, delay: float):
        """Simulate user behavior."""
        await asyncio.sleep(delay)
        self.active_users += 1
        
        while self.running and (time.time() - self.start_time) < self.config.duration:
            try:
                await self._execute_scenario(user_id)
                if self.config.think_time:
                    await asyncio.sleep(self.config.think_time)
            except Exception as e:
                self.logger.error(f"User {user_id} error: {str(e)}")
                self.metrics['errors'] += 1
        
        self.active_users -= 1

    async def _execute_scenario(self, user_id: int):
        """Execute test scenario."""
        scenarios = {
            'api_endpoints': self._api_scenario,
            'database_operations': self._database_scenario,
            'research_operations': self._research_scenario,
            'file_uploads': self._upload_scenario,
            'search_operations': self._search_scenario,
            'realtime_updates': self._realtime_scenario
        }
        
        start_time = time.time()
        try:
            scenario_func = random.choice(list(scenarios.values()))
            await scenario_func(user_id)
            response_time = (time.time() - start_time) * 1000
            self.metrics['response_times'].append(response_time)
            self.metrics['requests'] += 1
        except asyncio.TimeoutError:
            self.metrics['timeouts'] += 1
            raise

    async def _api_scenario(self, user_id: int):
        """Execute API test scenario."""
        endpoints = ['/api/data', '/api/query', '/api/update']
        async with self.session.get(f'http://localhost:8000{random.choice(endpoints)}') as response:
            await response.json()

    async def _database_scenario(self, user_id: int):
        """Execute database test scenario."""
        operations = ['query', 'insert', 'update', 'delete']
        operation = random.choice(operations)
        async with self.session.post('http://localhost:8000/db', 
                                   json={'operation': operation, 'data': self._generate_test_data()}) as response:
            await response.json()

    async def _research_scenario(self, user_id: int):
        """Execute research operation scenario."""
        operations = ['analyze', 'process', 'visualize']
        async with self.session.post('http://localhost:8000/research', 
                                   json={'operation': random.choice(operations)}) as response:
            await response.json()

    async def _upload_scenario(self, user_id: int):
        """Execute file upload scenario."""
        data = self._generate_test_file()
        async with self.session.post('http://localhost:8000/upload', data=data) as response:
            await response.json()

    async def _search_scenario(self, user_id: int):
        """Execute search scenario."""
        terms = ['quantum', 'physics', 'chemistry', 'biology']
        async with self.session.get(f'http://localhost:8000/search?q={random.choice(terms)}') as response:
            await response.json()

    async def _realtime_scenario(self, user_id: int):
        """Execute realtime update scenario."""
        async with self.session.ws_connect('ws://localhost:8000/updates') as ws:
            await ws.send_json({'subscribe': 'updates'})
            await ws.receive()

    async def _collect_metrics(self):
        """Collect and log metrics."""
        while self.running:
            current_metrics = {
                'active_users': self.active_users,
                'requests_per_second': self.metrics['requests'] / (time.time() - self.start_time),
                'error_rate': self.metrics['errors'] / max(self.metrics['requests'], 1),
                'avg_response_time': sum(self.metrics['response_times']) / max(len(self.metrics['response_times']), 1)
            }
            self.logger.info(f"Current metrics: {json.dumps(current_metrics, indent=2)}")
            await asyncio.sleep(5)

    def _generate_test_data(self) -> Dict[str, Any]:
        """Generate test data."""
        return {
            'id': random.randint(1, 1000000),
            'timestamp': datetime.now().isoformat(),
            'value': random.random()
        }

    def _generate_test_file(self) -> bytes:
        """Generate test file data."""
        return b'x' * random.randint(1000, 10000)

    def stop(self):
        """Stop load generation."""
        self.running = False

def run_load_test(config: LoadConfig, scenario: str):
    """Run load test with given configuration."""
    generator = LoadGenerator(config)
    try:
        asyncio.run(generator.start())
    except KeyboardInterrupt:
        generator.stop()
    finally:
        return generator.metrics

if __name__ == '__main__':
    # Example usage
    config = LoadConfig(
        users=100,
        ramp_up=30,
        duration=300,
        target_rps=50,
        think_time=2
    )
    metrics = run_load_test(config, 'api_endpoints')
    print(json.dumps(metrics, indent=2))
