"""Export test reports in various formats."""
import json
import datetime
import gzip
import zipfile
import csv
from typing import Dict, List, Any, Optional, Union
from pathlib import Path
import pandas as pd
import pdfkit
import xlsxwriter
from jinja2 import Environment, FileSystemLoader
import plotly.io as pio
import base64
from weasyprint import HTML
from io import BytesIO, StringIO
from report_templates import ReportTemplates, TemplateType

class ReportExporter:
    """Export test reports in various formats."""

    def __init__(self, data_dir: str = "test_reports"):
        """Initialize report exporter.
        
        Args:
            data_dir: Directory containing test data
        """
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
        # Set up Jinja2 environment
        self.template_dir = Path(__file__).parent / "templates"
        self.template_dir.mkdir(exist_ok=True)
        self.env = Environment(loader=FileSystemLoader(str(self.template_dir)))
        
        # Create export templates if they don't exist
        self._create_templates()

    def _create_templates(self) -> None:
        """Create export templates."""
        # HTML template
        html_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>{{ title }}</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                .section { margin: 20px 0; padding: 20px; border: 1px solid #ddd; }
                .metric { margin: 10px 0; }
                .chart { margin: 20px 0; max-width: 100%; }
                .success { color: green; }
                .warning { color: orange; }
                .error { color: red; }
                table { border-collapse: collapse; width: 100%; margin: 10px 0; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                th { background-color: #f5f5f5; }
                .header { 
                    background-color: #2c3e50; 
                    color: white; 
                    padding: 20px;
                    margin-bottom: 20px;
                }
                .summary-box {
                    background-color: #f8f9fa;
                    border-radius: 5px;
                    padding: 15px;
                    margin: 10px 0;
                }
                .trend-indicator {
                    font-weight: bold;
                    margin-left: 10px;
                }
                .trend-up { color: #2ecc71; }
                .trend-down { color: #e74c3c; }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>{{ title }}</h1>
                <p>Generated: {{ timestamp }}</p>
            </div>

            <div class="section">
                <h2>Executive Summary</h2>
                <div class="summary-box">
                    <h3>Test Results</h3>
                    <div class="metric">Total Tests: {{ total_tests }}</div>
                    <div class="metric">Passed: <span class="success">{{ passed_tests }}</span></div>
                    <div class="metric">Failed: <span class="error">{{ failed_tests }}</span></div>
                    <div class="metric">Pass Rate: {{ pass_rate }}%</div>
                </div>
                
                <div class="summary-box">
                    <h3>Performance Summary</h3>
                    <div class="metric">
                        Average Response Time: {{ avg_response_time }}ms
                        <span class="trend-indicator {{ response_time_trend_class }}">
                            {{ response_time_trend }}
                        </span>
                    </div>
                    <div class="metric">
                        Peak Memory Usage: {{ peak_memory }}MB
                        <span class="trend-indicator {{ memory_trend_class }}">
                            {{ memory_trend }}
                        </span>
                    </div>
                </div>
            </div>

            <div class="section">
                <h2>Performance Metrics</h2>
                {% for metric in performance_metrics %}
                <div class="metric">
                    <h3>{{ metric.name }}</h3>
                    <table>
                        <tr>
                            <th>Metric</th>
                            <th>Value</th>
                            <th>Trend</th>
                        </tr>
                        <tr>
                            <td>Average</td>
                            <td>{{ metric.average }}</td>
                            <td>{{ metric.trend }}</td>
                        </tr>
                        <tr>
                            <td>P95</td>
                            <td>{{ metric.p95 }}</td>
                            <td>{{ metric.p95_trend }}</td>
                        </tr>
                        <tr>
                            <td>Max</td>
                            <td>{{ metric.max }}</td>
                            <td>{{ metric.max_trend }}</td>
                        </tr>
                    </table>
                </div>
                {% endfor %}
            </div>

            <div class="section">
                <h2>Error Analysis</h2>
                <table>
                    <tr>
                        <th>Error Type</th>
                        <th>Count</th>
                        <th>Impact</th>
                        <th>Trend</th>
                        <th>Recommendation</th>
                    </tr>
                    {% for error in errors %}
                    <tr>
                        <td>{{ error.type }}</td>
                        <td>{{ error.count }}</td>
                        <td class="{{ error.severity }}">{{ error.impact }}</td>
                        <td>{{ error.trend }}</td>
                        <td>{{ error.recommendation }}</td>
                    </tr>
                    {% endfor %}
                </table>
            </div>

            <div class="section">
                <h2>Charts</h2>
                {% for chart in charts %}
                <div class="chart">
                    <h3>{{ chart.title }}</h3>
                    <img src="data:image/png;base64,{{ chart.data }}" 
                         alt="{{ chart.title }}"
                         style="max-width: 100%;">
                </div>
                {% endfor %}
            </div>
        </body>
        </html>
        """
        
        (self.template_dir / "export_template.html").write_text(html_template)

    def export_html(self, data: Dict[str, Any], output_path: Optional[str] = None) -> str:
        """Export report as HTML.
        
        Args:
            data: Report data
            output_path: Optional output path
            
        Returns:
            Path to exported HTML file
        """
        if output_path is None:
            output_path = str(self.data_dir / f"report_{int(datetime.datetime.now().timestamp())}.html")
        
        template = self.env.get_template("export_template.html")
        
        # Convert chart images to base64
        for chart in data.get("charts", []):
            if "path" in chart:
                with open(chart["path"], "rb") as f:
                    img_data = base64.b64encode(f.read()).decode()
                    chart["data"] = img_data
        
        # Add timestamp
        data["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Render template
        html_content = template.render(**data)
        
        # Save HTML file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        return output_path

    def export_pdf(self, data: Dict[str, Any], output_path: Optional[str] = None) -> str:
        """Export report as PDF.
        
        Args:
            data: Report data
            output_path: Optional output path
            
        Returns:
            Path to exported PDF file
        """
        if output_path is None:
            output_path = str(self.data_dir / f"report_{int(datetime.datetime.now().timestamp())}.pdf")
        
        # First export as HTML
        html_path = self.export_html(data)
        
        # Convert HTML to PDF using WeasyPrint
        HTML(html_path).write_pdf(output_path)
        
        return output_path

    def export_excel(self, data: Dict[str, Any], output_path: Optional[str] = None) -> str:
        """Export report as Excel workbook.
        
        Args:
            data: Report data
            output_path: Optional output path
            
        Returns:
            Path to exported Excel file
        """
        if output_path is None:
            output_path = str(self.data_dir / f"report_{int(datetime.datetime.now().timestamp())}.xlsx")
        
        with xlsxwriter.Workbook(output_path) as workbook:
            # Summary sheet
            summary_sheet = workbook.add_worksheet("Summary")
            summary_sheet.write("A1", "Test Summary")
            summary_sheet.write("A2", "Total Tests")
            summary_sheet.write("B2", data.get("total_tests", 0))
            summary_sheet.write("A3", "Passed Tests")
            summary_sheet.write("B3", data.get("passed_tests", 0))
            summary_sheet.write("A4", "Failed Tests")
            summary_sheet.write("B4", data.get("failed_tests", 0))
            
            # Performance metrics sheet
            perf_sheet = workbook.add_worksheet("Performance")
            perf_sheet.write("A1", "Performance Metrics")
            
            row = 2
            for metric in data.get("performance_metrics", []):
                perf_sheet.write(f"A{row}", metric["name"])
                perf_sheet.write(f"B{row}", "Average")
                perf_sheet.write(f"C{row}", metric["average"])
                row += 1
                perf_sheet.write(f"B{row}", "P95")
                perf_sheet.write(f"C{row}", metric["p95"])
                row += 1
                perf_sheet.write(f"B{row}", "Max")
                perf_sheet.write(f"C{row}", metric["max"])
                row += 2
            
            # Error analysis sheet
            error_sheet = workbook.add_worksheet("Errors")
            error_sheet.write("A1", "Error Analysis")
            error_sheet.write("A2", "Error Type")
            error_sheet.write("B2", "Count")
            error_sheet.write("C2", "Impact")
            error_sheet.write("D2", "Trend")
            
            for i, error in enumerate(data.get("errors", []), start=3):
                error_sheet.write(f"A{i}", error["type"])
                error_sheet.write(f"B{i}", error["count"])
                error_sheet.write(f"C{i}", error["impact"])
                error_sheet.write(f"D{i}", error["trend"])
        
        return output_path

    def export_json(self, data: Dict[str, Any], output_path: Optional[str] = None) -> str:
        """Export report as JSON.
        
        Args:
            data: Report data
            output_path: Optional output path
            
        Returns:
            Path to exported JSON file
        """
        if output_path is None:
            output_path = str(self.data_dir / f"report_{int(datetime.datetime.now().timestamp())}.json")
        
        # Add metadata
        data["metadata"] = {
            "generated_at": datetime.datetime.now().isoformat(),
            "version": "1.0.0",
            "generator": "ReportExporter"
        }
        
        # Save JSON file
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2)
        
        return output_path

    def export_markdown(self, data: Dict[str, Any], template_type: TemplateType = TemplateType.TECHNICAL, output_path: Optional[str] = None) -> str:
        """Export report as Markdown.
        
        Args:
            data: Report data
            template_type: Type of template to use
            output_path: Optional output path
            
        Returns:
            Path to exported Markdown file
        """
        if output_path is None:
            output_path = str(self.data_dir / f"report_{int(datetime.datetime.now().timestamp())}.md")
        
        # Get markdown template
        template = ReportTemplates.get_markdown_template(template_type)
        
        # Add timestamp
        data["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Render template
        md_content = Environment(loader=FileSystemLoader(str(self.template_dir))).from_string(template).render(**data)
        
        # Save markdown file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        
        return output_path

    def export_csv(self, data: Dict[str, Any], template_type: TemplateType = TemplateType.TECHNICAL, output_dir: Optional[str] = None) -> List[str]:
        """Export report as CSV files.
        
        Args:
            data: Report data
            template_type: Type of template to use
            output_dir: Optional output directory
            
        Returns:
            List of paths to exported CSV files
        """
        if output_dir is None:
            output_dir = self.data_dir / f"report_{int(datetime.datetime.now().timestamp())}_csv"
        else:
            output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True)
        
        # Get CSV template configuration
        template = ReportTemplates.get_csv_template(template_type)
        output_paths = []
        
        # Create CSV files
        for file_config in template["files"]:
            file_path = output_dir / f"{file_config['name']}.csv"
            
            with open(file_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(file_config["headers"])
                
                # Write data based on file type
                if file_config["name"] == "test_results":
                    for test in data.get("tests", []):
                        writer.writerow([
                            test.get("name", ""),
                            test.get("status", ""),
                            test.get("duration", ""),
                            test.get("error", "")
                        ])
                elif file_config["name"] == "performance":
                    for metric in data.get("performance_metrics", []):
                        writer.writerow([
                            metric.get("name", ""),
                            metric.get("average", ""),
                            metric.get("p95", ""),
                            metric.get("max", ""),
                            metric.get("trend", "")
                        ])
                # Add other file types as needed
            
            output_paths.append(str(file_path))
        
        return output_paths

    def compress_report(self, file_path: str, compression: str = "gzip") -> str:
        """Compress a report file.
        
        Args:
            file_path: Path to file to compress
            compression: Compression format (gzip or zip)
            
        Returns:
            Path to compressed file
        """
        input_path = Path(file_path)
        
        if compression == "gzip":
            output_path = input_path.with_suffix(input_path.suffix + ".gz")
            with open(input_path, "rb") as f_in:
                with gzip.open(output_path, "wb") as f_out:
                    f_out.write(f_in.read())
        else:  # zip
            output_path = input_path.with_suffix(".zip")
            with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
                zip_file.write(input_path, input_path.name)
        
        return str(output_path)

    def export_all(self, data: Dict[str, Any], template_type: TemplateType = TemplateType.TECHNICAL, base_path: Optional[str] = None, compress: bool = False) -> Dict[str, Union[str, List[str]]]:
        """Export report in all formats.
        
        Args:
            data: Report data
            template_type: Type of template to use
            base_path: Optional base path for output files
            compress: Whether to compress the output files
            
        Returns:
            Dictionary mapping format to output path(s)
        """
        if base_path is None:
            base_path = str(self.data_dir / f"report_{int(datetime.datetime.now().timestamp())}")
        
        # Get template configuration
        template = ReportTemplates.get_template(template_type)
        
        # Export in all formats
        outputs = {
            "html": self.export_html(data, f"{base_path}.html"),
            "pdf": self.export_pdf(data, f"{base_path}.pdf"),
            "excel": self.export_excel(data, f"{base_path}.xlsx"),
            "json": self.export_json(data, f"{base_path}.json"),
            "markdown": self.export_markdown(data, template_type, f"{base_path}.md"),
            "csv": self.export_csv(data, template_type, f"{base_path}_csv")
        }
        
        # Compress files if requested
        if compress:
            compressed = {}
            for format_name, path in outputs.items():
                if isinstance(path, str):
                    compressed[format_name] = self.compress_report(path, "gzip")
                else:  # List of paths (CSV)
                    # Create a zip file containing all CSV files
                    zip_path = f"{base_path}_csv.zip"
                    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
                        for csv_path in path:
                            zip_file.write(csv_path, Path(csv_path).name)
                    compressed[format_name] = zip_path
            outputs = compressed
        
        return outputs


if __name__ == "__main__":
    # Example usage
    exporter = ReportExporter()
    
    # Sample data
    data = {
        "title": "SQL Test Report",
        "total_tests": 100,
        "passed_tests": 95,
        "failed_tests": 5,
        "pass_rate": 95,
        "avg_response_time": 150,
        "peak_memory": 512,
        "response_time_trend": "↓ -5%",
        "response_time_trend_class": "trend-down",
        "memory_trend": "↑ +2%",
        "memory_trend_class": "trend-up",
        "performance_metrics": [
            {
                "name": "Query Performance",
                "average": "120ms",
                "trend": "↓ -5%",
                "p95": "200ms",
                "p95_trend": "↓ -3%",
                "max": "300ms",
                "max_trend": "↓ -10%"
            }
        ],
        "errors": [
            {
                "type": "ConnectionError",
                "count": 3,
                "severity": "error",
                "impact": "High",
                "trend": "↑ +2",
                "recommendation": "Check network stability"
            }
        ],
        "tests": [
            {
                "name": "test_simple_query",
                "status": "passed",
                "duration": "0.1s",
                "error": None
            },
            {
                "name": "test_complex_query",
                "status": "failed",
                "duration": "0.5s",
                "error": "Timeout exceeded"
            }
        ]
    }
    
    # Export with template and compression
    output_paths = exporter.export_all(
        data,
        template_type=TemplateType.TECHNICAL,
        compress=True
    )
    
    print("Reports exported:")
    for format_name, path in output_paths.items():
        print(f"- {format_name}: {path}")
