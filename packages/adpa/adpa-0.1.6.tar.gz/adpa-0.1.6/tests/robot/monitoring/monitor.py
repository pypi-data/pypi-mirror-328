"""Test monitoring and reporting utilities."""

import os
import json
import sqlite3
from datetime import datetime
from typing import Dict, List, Any
from pathlib import Path

class TestMonitor:
    """Monitor and track test execution metrics."""
    
    def __init__(self, db_path: str = "test_results/monitoring.db"):
        """Initialize test monitor.
        
        Args:
            db_path: Path to SQLite database
        """
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        """Initialize the monitoring database."""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            
            # Test runs table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS test_runs (
                    id INTEGER PRIMARY KEY,
                    start_time TIMESTAMP,
                    end_time TIMESTAMP,
                    total_tests INTEGER,
                    passed_tests INTEGER,
                    failed_tests INTEGER,
                    skipped_tests INTEGER,
                    duration REAL,
                    git_commit TEXT,
                    git_branch TEXT
                )
            """)
            
            # Test cases table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS test_cases (
                    id INTEGER PRIMARY KEY,
                    run_id INTEGER,
                    name TEXT,
                    status TEXT,
                    duration REAL,
                    error_message TEXT,
                    tags TEXT,
                    FOREIGN KEY (run_id) REFERENCES test_runs(id)
                )
            """)
            
            # Performance metrics table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS performance_metrics (
                    id INTEGER PRIMARY KEY,
                    run_id INTEGER,
                    metric_name TEXT,
                    metric_value REAL,
                    timestamp TIMESTAMP,
                    FOREIGN KEY (run_id) REFERENCES test_runs(id)
                )
            """)
            
            conn.commit()
    
    def start_test_run(self) -> int:
        """Start a new test run.
        
        Returns:
            Test run ID
        """
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO test_runs (
                    start_time, 
                    git_commit, 
                    git_branch
                ) VALUES (?, ?, ?)
            """, (
                datetime.now().isoformat(),
                self._get_git_commit(),
                self._get_git_branch()
            ))
            conn.commit()
            return cur.lastrowid
    
    def end_test_run(
        self, 
        run_id: int, 
        results: Dict[str, Any]
    ):
        """End a test run.
        
        Args:
            run_id: Test run ID
            results: Test results dictionary
        """
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
                UPDATE test_runs SET
                    end_time = ?,
                    total_tests = ?,
                    passed_tests = ?,
                    failed_tests = ?,
                    skipped_tests = ?,
                    duration = ?
                WHERE id = ?
            """, (
                datetime.now().isoformat(),
                results['total'],
                results['passed'],
                results['failed'],
                results['skipped'],
                results['duration'],
                run_id
            ))
            conn.commit()
    
    def record_test_case(
        self, 
        run_id: int, 
        test_case: Dict[str, Any]
    ):
        """Record a test case result.
        
        Args:
            run_id: Test run ID
            test_case: Test case data
        """
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO test_cases (
                    run_id,
                    name,
                    status,
                    duration,
                    error_message,
                    tags
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                run_id,
                test_case['name'],
                test_case['status'],
                test_case['duration'],
                test_case.get('error'),
                ','.join(test_case.get('tags', []))
            ))
            conn.commit()
    
    def record_performance_metric(
        self, 
        run_id: int, 
        metric: Dict[str, Any]
    ):
        """Record a performance metric.
        
        Args:
            run_id: Test run ID
            metric: Performance metric data
        """
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO performance_metrics (
                    run_id,
                    metric_name,
                    metric_value,
                    timestamp
                ) VALUES (?, ?, ?, ?)
            """, (
                run_id,
                metric['name'],
                metric['value'],
                datetime.now().isoformat()
            ))
            conn.commit()
    
    def get_test_history(
        self, 
        days: int = 7
    ) -> List[Dict[str, Any]]:
        """Get test run history.
        
        Args:
            days: Number of days of history
            
        Returns:
            List of test run data
        """
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT 
                    id,
                    start_time,
                    end_time,
                    total_tests,
                    passed_tests,
                    failed_tests,
                    skipped_tests,
                    duration,
                    git_commit,
                    git_branch
                FROM test_runs
                WHERE start_time >= datetime('now', ?)
                ORDER BY start_time DESC
            """, (f'-{days} days',))
            
            columns = [col[0] for col in cur.description]
            return [dict(zip(columns, row)) for row in cur.fetchall()]
    
    def get_performance_trends(
        self, 
        metric_name: str, 
        days: int = 7
    ) -> List[Dict[str, Any]]:
        """Get performance metric trends.
        
        Args:
            metric_name: Name of metric to retrieve
            days: Number of days of history
            
        Returns:
            List of metric data points
        """
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT 
                    metric_value,
                    timestamp
                FROM performance_metrics
                WHERE 
                    metric_name = ? AND
                    timestamp >= datetime('now', ?)
                ORDER BY timestamp DESC
            """, (metric_name, f'-{days} days'))
            
            return [
                {
                    'value': row[0],
                    'timestamp': row[1]
                }
                for row in cur.fetchall()
            ]
    
    @staticmethod
    def _get_git_commit() -> str:
        """Get current git commit hash."""
        try:
            import git
            repo = git.Repo(search_parent_directories=True)
            return repo.head.object.hexsha
        except:
            return 'unknown'
    
    @staticmethod
    def _get_git_branch() -> str:
        """Get current git branch name."""
        try:
            import git
            repo = git.Repo(search_parent_directories=True)
            return repo.active_branch.name
        except:
            return 'unknown'
