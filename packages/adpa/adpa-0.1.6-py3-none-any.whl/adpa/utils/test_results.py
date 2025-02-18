"""Test results utilities for the ADPA Framework."""

import os
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any, Union
import json

from sqlalchemy.orm import Session
from sqlalchemy import desc

from adpa.models.test_results import TestResult
from .file_utils import ensure_dir, safe_file_write

def save_test_result(
    session: Session,
    version: str,
    return_code: int,
    files_tested: int,
    summary: Optional[str] = None,
    details: Optional[str] = None,
    errors: Optional[str] = None,
    test_files: Optional[List[str]] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> TestResult:
    """Save test result to database.
    
    Args:
        session: Database session
        version: Test version
        return_code: Return code
        files_tested: Number of files tested
        summary: Test summary
        details: Test details
        errors: Error output
        test_files: List of test files
        metadata: Additional metadata to store
        
    Returns:
        TestResult: Saved test result
    """
    result = TestResult(
        version=version,
        timestamp=datetime.utcnow(),
        return_code=return_code,
        files_tested=files_tested,
        summary=summary,
        details=details,
        errors=errors,
        test_files=test_files or [],
        metadata=metadata or {}
    )
    
    session.add(result)
    session.commit()
    return result

def get_latest_test_result(session: Session) -> Optional[TestResult]:
    """Get latest test result.
    
    Args:
        session: Database session
        
    Returns:
        Optional[TestResult]: Latest test result or None
    """
    return session.query(TestResult).order_by(desc(TestResult.timestamp)).first()

def get_test_results_by_version(
    session: Session,
    version: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None
) -> List[TestResult]:
    """Get test results by version.
    
    Args:
        session: Database session
        version: Version to filter by
        limit: Maximum number of results to return
        offset: Number of results to skip
        
    Returns:
        List[TestResult]: List of test results
    """
    query = session.query(TestResult).filter(TestResult.version == version)
    
    if offset is not None:
        query = query.offset(offset)
    if limit is not None:
        query = query.limit(limit)
        
    return query.all()

def export_test_result_to_md(
    result: TestResult,
    output_dir: Union[str, Path],
    include_metadata: bool = True
) -> Path:
    """Export test result to markdown file.
    
    Args:
        result: Test result to export
        output_dir: Output directory
        include_metadata: Whether to include metadata in export
        
    Returns:
        Path: Path to output file
    """
    output_dir = Path(output_dir)
    ensure_dir(output_dir)
    
    timestamp = result.timestamp.strftime('%Y%m%d_%H%M%S')
    output_file = output_dir / f"test_result_{timestamp}.md"
    
    md_lines = [
        f"# ADPA Test Results",
        f"\nGenerated on: {result.timestamp.strftime('%Y-%m-%d %H:%M:%S')}",
        f"\n## Test Configuration",
        f"- Version: {result.version}",
        f"- Return Code: {result.return_code}",
        f"- Files Tested: {result.files_tested}",
        "\n### Test Files"
    ]
    
    # Add test files
    for test_file in result.test_files:
        md_lines.append(f"- {test_file}")
    
    # Add summary if present
    if result.summary:
        md_lines.extend(["\n## Summary", result.summary])
    
    # Add details if present
    if result.details:
        md_lines.extend(["\n## Details", result.details])
    
    # Add errors if present
    if result.errors:
        md_lines.extend(["\n## Errors", "```", result.errors, "```"])
    
    # Add metadata if present and requested
    if include_metadata and result.metadata:
        md_lines.extend(["\n## Metadata", "```json"])
        md_lines.append(json.dumps(result.metadata, indent=2))
        md_lines.append("```")
    
    # Write to file
    safe_file_write(output_file, "\n".join(md_lines))
    return output_file

def analyze_test_results(
    session: Session,
    version: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
) -> Dict[str, Any]:
    """Analyze test results and generate statistics.
    
    Args:
        session: Database session
        version: Optional version to filter by
        start_date: Optional start date for analysis
        end_date: Optional end date for analysis
        
    Returns:
        Dict containing analysis results:
        - total_runs: Total number of test runs
        - success_rate: Percentage of successful runs
        - avg_files_tested: Average number of files tested
        - common_errors: Most common error messages
        - trend: Success rate trend over time
    """
    query = session.query(TestResult)
    
    if version:
        query = query.filter(TestResult.version == version)
    if start_date:
        query = query.filter(TestResult.timestamp >= start_date)
    if end_date:
        query = query.filter(TestResult.timestamp <= end_date)
    
    results = query.all()
    
    if not results:
        return {
            "total_runs": 0,
            "success_rate": None,
            "avg_files_tested": None,
            "common_errors": [],
            "trend": []
        }
    
    # Calculate statistics
    total_runs = len(results)
    successful_runs = sum(1 for r in results if r.return_code == 0)
    success_rate = (successful_runs / total_runs) * 100
    avg_files_tested = sum(r.files_tested for r in results) / total_runs
    
    # Analyze errors
    error_counts = {}
    for result in results:
        if result.errors:
            error_counts[result.errors] = error_counts.get(result.errors, 0) + 1
    
    common_errors = sorted(
        [{"error": k, "count": v} for k, v in error_counts.items()],
        key=lambda x: x["count"],
        reverse=True
    )[:5]
    
    # Calculate trend
    from collections import defaultdict
    trend_data = defaultdict(list)
    for result in sorted(results, key=lambda x: x.timestamp):
        date = result.timestamp.date()
        trend_data[date].append(result.return_code == 0)
    
    trend = [
        {
            "date": date.isoformat(),
            "success_rate": (sum(successes) / len(successes)) * 100
        }
        for date, successes in trend_data.items()
    ]
    
    return {
        "total_runs": total_runs,
        "success_rate": success_rate,
        "avg_files_tested": avg_files_tested,
        "common_errors": common_errors,
        "trend": trend
    }
