"""FastAPI backend for SQL testing GUI."""
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel
from typing import Dict, List, Any, Optional
import asyncio
import json
import datetime
from pathlib import Path
import sys
import os

# Add parent directory to path to import our modules
sys.path.append(str(Path(__file__).parent.parent))

from monitoring_dashboard import MonitoringDashboard
from trend_analysis import TrendAnalyzer
from report_exporter import ReportExporter
from report_templates import TemplateType
from test_reporting import TestReport

app = FastAPI(title="SQL Testing GUI")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
dashboard = MonitoringDashboard()
analyzer = TrendAnalyzer()
exporter = ReportExporter()
test_report = TestReport()

# Store background tasks
running_tasks: Dict[str, asyncio.Task] = {}


class TestConfig(BaseModel):
    """Test configuration."""
    test_types: List[str]
    concurrent_users: int = 10
    duration_seconds: int = 60
    template_type: str = "TECHNICAL"


class ReportConfig(BaseModel):
    """Report configuration."""
    format: str
    template_type: str
    compress: bool = False


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "SQL Testing GUI API"}


@app.post("/tests/run")
async def run_tests(config: TestConfig, background_tasks: BackgroundTasks):
    """Run tests with given configuration.
    
    Args:
        config: Test configuration
        background_tasks: FastAPI background tasks
    """
    task_id = str(datetime.datetime.now().timestamp())
    
    async def run_test_suite():
        try:
            # Import test modules based on config
            for test_type in config.test_types:
                if test_type == "unit":
                    from test_generator import run_unit_tests
                    await run_unit_tests()
                elif test_type == "performance":
                    from test_performance import run_performance_tests
                    await run_performance_tests(
                        concurrent_users=config.concurrent_users,
                        duration_seconds=config.duration_seconds
                    )
                elif test_type == "load":
                    from test_load import run_load_tests
                    await run_load_tests(
                        concurrent_users=config.concurrent_users,
                        duration_seconds=config.duration_seconds
                    )
                elif test_type == "error":
                    from test_error_recovery import run_error_tests
                    await run_error_tests()
        except Exception as e:
            print(f"Error running tests: {e}")
    
    # Create task
    task = asyncio.create_task(run_test_suite())
    running_tasks[task_id] = task
    
    return {"task_id": task_id}


@app.get("/tests/status/{task_id}")
async def get_test_status(task_id: str):
    """Get status of test run.
    
    Args:
        task_id: ID of test run
    """
    if task_id not in running_tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task = running_tasks[task_id]
    if task.done():
        if task.exception():
            return {
                "status": "failed",
                "error": str(task.exception())
            }
        return {"status": "completed"}
    return {"status": "running"}


@app.get("/dashboard")
async def get_dashboard_data():
    """Get current dashboard data."""
    return {
        "performance": dashboard.performance_data,
        "errors": dashboard.error_data,
        "resources": dashboard.resource_usage
    }


@app.get("/trends")
async def get_trend_analysis():
    """Get trend analysis."""
    analyzer.load_historical_data()
    return {
        "performance_trends": analyzer.analyze_performance_trends(),
        "error_patterns": analyzer.analyze_error_patterns(),
        "load_trends": analyzer.analyze_load_test_trends()
    }


@app.post("/reports/generate")
async def generate_report(config: ReportConfig):
    """Generate report with given configuration.
    
    Args:
        config: Report configuration
    """
    try:
        # Get latest test data
        data = {
            "performance": dashboard.performance_data,
            "errors": dashboard.error_data,
            "resources": dashboard.resource_usage,
            "trends": await get_trend_analysis()
        }
        
        # Generate report
        template_type = getattr(TemplateType, config.template_type.upper())
        if config.format == "all":
            paths = exporter.export_all(
                data,
                template_type=template_type,
                compress=config.compress
            )
            return {"paths": paths}
        
        # Generate specific format
        if config.format == "html":
            path = exporter.export_html(data, template_type=template_type)
        elif config.format == "pdf":
            path = exporter.export_pdf(data, template_type=template_type)
        elif config.format == "excel":
            path = exporter.export_excel(data, template_type=template_type)
        elif config.format == "json":
            path = exporter.export_json(data, template_type=template_type)
        elif config.format == "markdown":
            path = exporter.export_markdown(data, template_type=template_type)
        elif config.format == "csv":
            paths = exporter.export_csv(data, template_type=template_type)
            return {"paths": paths}
        else:
            raise HTTPException(status_code=400, detail="Invalid format")
        
        # Compress if requested
        if config.compress:
            path = exporter.compress_report(path)
        
        return {"path": path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/reports/download/{filename}")
async def download_report(filename: str):
    """Download generated report.
    
    Args:
        filename: Name of report file to download
    """
    file_path = Path(exporter.data_dir) / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Report not found")
    
    return FileResponse(
        file_path,
        filename=filename,
        media_type="application/octet-stream"
    )


@app.get("/templates")
async def get_templates():
    """Get available report templates."""
    return {
        "templates": [t.value for t in TemplateType],
        "descriptions": {
            "EXECUTIVE": "High-level summary for management",
            "TECHNICAL": "Detailed technical report",
            "PERFORMANCE": "Performance-focused report",
            "SECURITY": "Security-focused report",
            "ERROR": "Error analysis report",
            "LOAD": "Load testing report",
            "TREND": "Trend analysis report",
            "MINIMAL": "Minimal summary report"
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
