"""Utility functions for test reporting and analysis in the ADPA Framework."""

import os
import xml.etree.ElementTree as ET
from datetime import datetime
import glob
from typing import Dict, List, Tuple, Optional, Any
from pathlib import Path
import json

from .file_utils import ensure_dir

def parse_robot_results(output_xml: str) -> Optional[Tuple[Dict[str, Any], List[Dict[str, Any]]]]:
    """Parse Robot Framework output.xml and return test statistics.
    
    Args:
        output_xml: Path to Robot Framework output.xml file
        
    Returns:
        Tuple containing:
        - Dictionary with overall statistics (total, passed, failed, duration)
        - List of dictionaries with individual test details
        Returns None if the output file doesn't exist or is invalid
    """
    if not os.path.exists(output_xml):
        return None
    
    try:
        tree = ET.parse(output_xml)
        root = tree.getroot()
        
        # Initialize default stats
        stats = {
            'total': 0,
            'passed': 0,
            'failed': 0,
            'skipped': 0,
            'start_time': root.get('generated', datetime.now().isoformat()),
            'duration': 0.0
        }
        
        # Try to get statistics from the XML
        statistics = root.find('statistics')
        if statistics is not None:
            total = statistics.find('total')
            if total is not None:
                stat = total.find('stat')
                if stat is not None:
                    stats.update({
                        'total': int(stat.get('pass', 0)) + int(stat.get('fail', 0)) + int(stat.get('skip', 0)),
                        'passed': int(stat.get('pass', 0)),
                        'failed': int(stat.get('fail', 0)),
                        'skipped': int(stat.get('skip', 0))
                    })
        
        # Try to get duration
        suite = root.find('suite')
        if suite is not None:
            elapsed = suite.get('elapsedtime')
            if elapsed is not None:
                try:
                    stats['duration'] = float(elapsed) / 1000  # Convert to seconds
                except (ValueError, TypeError):
                    pass
        
        # Get test case details
        tests = []
        for test in root.findall('.//test'):
            test_data = {
                'name': test.get('name', 'Unknown Test'),
                'status': 'UNKNOWN',
                'elapsed': 0.0,
                'message': '',
                'tags': [],
                'critical': test.get('critical', 'yes') == 'yes'
            }
            
            # Get tags
            tags = test.find('tags')
            if tags is not None:
                test_data['tags'] = [tag.text for tag in tags.findall('tag')]
            
            # Get status and timing
            status = test.find('status')
            if status is not None:
                test_data.update({
                    'status': status.get('status', 'UNKNOWN'),
                    'message': status.text or ''
                })
                
                # Try to get test duration
                elapsed = status.get('elapsedtime')
                if elapsed is not None:
                    try:
                        test_data['elapsed'] = float(elapsed) / 1000
                    except (ValueError, TypeError):
                        pass
            
            tests.append(test_data)
        
        return stats, tests
        
    except (ET.ParseError, KeyError, ValueError, TypeError, AttributeError) as e:
        print(f"Error parsing Robot Framework results: {str(e)}")
        return None

def load_screenshots(
    report_dir: str = "reports/screenshots",
    patterns: List[str] = ["*.png", "*.jpg", "*.jpeg"]
) -> List[Dict[str, Any]]:
    """Load screenshots from the reports directory.
    
    Args:
        report_dir: Directory containing screenshots
        patterns: List of file patterns to match
        
    Returns:
        List of dictionaries containing screenshot information:
        - name: Screenshot filename
        - path: Full path to screenshot
        - timestamp: When the screenshot was taken
        - size: File size in bytes
        - metadata: Any additional metadata
    """
    screenshots = []
    report_dir = Path(report_dir)
    
    if not report_dir.exists():
        return screenshots
    
    for pattern in patterns:
        for file_path in report_dir.glob(pattern):
            try:
                stat = file_path.stat()
                screenshot = {
                    'name': file_path.name,
                    'path': str(file_path),
                    'timestamp': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    'size': stat.st_size,
                    'metadata': {}
                }
                
                # Try to load metadata from companion JSON file
                meta_path = file_path.with_suffix('.json')
                if meta_path.exists():
                    with open(meta_path, 'r') as f:
                        screenshot['metadata'] = json.load(f)
                
                screenshots.append(screenshot)
            except Exception as e:
                print(f"Error loading screenshot {file_path}: {str(e)}")
    
    return sorted(screenshots, key=lambda x: x['timestamp'], reverse=True)

def get_test_history(
    output_dir: str = "test-output",
    days: Optional[int] = None
) -> List[Dict[str, Any]]:
    """Get historical test execution data from output files.
    
    Args:
        output_dir: Directory containing test output files
        days: Optional number of days to look back
        
    Returns:
        List of dictionaries containing test execution history:
        - timestamp: When tests were run
        - total: Total number of tests
        - passed: Number of passed tests
        - failed: Number of failed tests
        - duration: Test execution duration in seconds
        - coverage: Test coverage data if available
    """
    history = []
    output_dir = Path(output_dir)
    
    if not output_dir.exists():
        return history
    
    # Calculate cutoff date if days specified
    if days is not None:
        cutoff = datetime.now() - timedelta(days=days)
    else:
        cutoff = None
    
    # Find all output.xml files
    for xml_file in output_dir.rglob('output.xml'):
        try:
            # Parse Robot Framework results
            results = parse_robot_results(str(xml_file))
            if results is None:
                continue
            
            stats, tests = results
            timestamp = datetime.fromisoformat(stats['start_time'])
            
            # Skip if before cutoff
            if cutoff and timestamp < cutoff:
                continue
            
            # Try to load coverage data
            coverage_data = {}
            coverage_file = xml_file.parent / 'coverage.json'
            if coverage_file.exists():
                with open(coverage_file, 'r') as f:
                    coverage_data = json.load(f)
            
            history_entry = {
                'timestamp': timestamp.isoformat(),
                'total': stats['total'],
                'passed': stats['passed'],
                'failed': stats['failed'],
                'skipped': stats.get('skipped', 0),
                'duration': stats['duration'],
                'coverage': coverage_data
            }
            
            history.append(history_entry)
            
        except Exception as e:
            print(f"Error processing {xml_file}: {str(e)}")
    
    return sorted(history, key=lambda x: x['timestamp'], reverse=True)

def analyze_test_trends(history: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyze trends in test execution history.
    
    Args:
        history: List of test execution history entries
        
    Returns:
        Dictionary containing trend analysis:
        - success_rate_trend: Success rate over time
        - duration_trend: Test duration over time
        - coverage_trend: Coverage metrics over time
        - failure_patterns: Common test failure patterns
    """
    if not history:
        return {
            'success_rate_trend': [],
            'duration_trend': [],
            'coverage_trend': [],
            'failure_patterns': []
        }
    
    trends = {
        'success_rate_trend': [],
        'duration_trend': [],
        'coverage_trend': [],
        'failure_patterns': []
    }
    
    # Calculate trends
    for entry in sorted(history, key=lambda x: x['timestamp']):
        timestamp = entry['timestamp']
        total = entry['total']
        
        if total > 0:
            success_rate = (entry['passed'] / total) * 100
            trends['success_rate_trend'].append({
                'timestamp': timestamp,
                'value': success_rate
            })
        
        trends['duration_trend'].append({
            'timestamp': timestamp,
            'value': entry['duration']
        })
        
        if 'coverage' in entry and entry['coverage']:
            trends['coverage_trend'].append({
                'timestamp': timestamp,
                'value': entry['coverage'].get('total_coverage', 0)
            })
    
    # Analyze failure patterns
    failure_counts = {}
    for entry in history:
        if entry.get('failed', 0) > 0:
            pattern = f"{entry['failed']}/{entry['total']} tests failed"
            failure_counts[pattern] = failure_counts.get(pattern, 0) + 1
    
    trends['failure_patterns'] = [
        {'pattern': k, 'count': v}
        for k, v in sorted(failure_counts.items(), key=lambda x: x[1], reverse=True)
    ]
    
    return trends
