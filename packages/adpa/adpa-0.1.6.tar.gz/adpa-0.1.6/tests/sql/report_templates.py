"""Report templates for different use cases."""
from typing import Dict, Any
from enum import Enum


class TemplateType(Enum):
    """Available report templates."""
    EXECUTIVE = "executive"  # High-level summary for management
    TECHNICAL = "technical"  # Detailed technical report
    PERFORMANCE = "performance"  # Performance-focused report
    SECURITY = "security"  # Security-focused report
    ERROR = "error"  # Error analysis report
    LOAD = "load"  # Load testing report
    TREND = "trend"  # Trend analysis report
    MINIMAL = "minimal"  # Minimal summary report


class ReportTemplates:
    """Report templates for different use cases."""

    @staticmethod
    def get_template(template_type: TemplateType) -> Dict[str, Any]:
        """Get template configuration.
        
        Args:
            template_type: Type of template to get
            
        Returns:
            Template configuration
        """
        templates = {
            TemplateType.EXECUTIVE: {
                "sections": [
                    "executive_summary",
                    "key_metrics",
                    "trends",
                    "recommendations"
                ],
                "charts": [
                    "performance_overview",
                    "error_trends",
                    "resource_usage"
                ],
                "metrics": [
                    "pass_rate",
                    "response_time",
                    "error_rate",
                    "resource_efficiency"
                ],
                "style": "executive",
                "compression": False
            },
            TemplateType.TECHNICAL: {
                "sections": [
                    "test_details",
                    "performance_metrics",
                    "error_analysis",
                    "resource_usage",
                    "code_coverage",
                    "technical_debt"
                ],
                "charts": [
                    "performance_details",
                    "error_distribution",
                    "coverage_map",
                    "dependency_graph"
                ],
                "metrics": [
                    "test_counts",
                    "response_times",
                    "error_details",
                    "coverage_metrics",
                    "complexity_metrics"
                ],
                "style": "technical",
                "compression": True
            },
            TemplateType.PERFORMANCE: {
                "sections": [
                    "performance_summary",
                    "response_times",
                    "throughput",
                    "resource_usage",
                    "bottlenecks",
                    "optimizations"
                ],
                "charts": [
                    "response_time_distribution",
                    "throughput_over_time",
                    "resource_usage_timeline",
                    "bottleneck_analysis"
                ],
                "metrics": [
                    "avg_response_time",
                    "p95_response_time",
                    "max_response_time",
                    "throughput_metrics",
                    "resource_metrics"
                ],
                "style": "performance",
                "compression": True
            },
            TemplateType.SECURITY: {
                "sections": [
                    "security_summary",
                    "vulnerability_analysis",
                    "access_patterns",
                    "security_metrics",
                    "recommendations"
                ],
                "charts": [
                    "vulnerability_trends",
                    "access_patterns",
                    "security_score_timeline"
                ],
                "metrics": [
                    "vulnerability_count",
                    "security_score",
                    "access_metrics",
                    "patch_status"
                ],
                "style": "security",
                "compression": True
            },
            TemplateType.ERROR: {
                "sections": [
                    "error_summary",
                    "error_details",
                    "impact_analysis",
                    "root_causes",
                    "recommendations"
                ],
                "charts": [
                    "error_distribution",
                    "error_timeline",
                    "impact_heatmap"
                ],
                "metrics": [
                    "error_counts",
                    "error_rates",
                    "impact_scores",
                    "recovery_metrics"
                ],
                "style": "error",
                "compression": False
            },
            TemplateType.LOAD: {
                "sections": [
                    "load_summary",
                    "concurrent_users",
                    "response_times",
                    "resource_usage",
                    "bottlenecks"
                ],
                "charts": [
                    "user_count_timeline",
                    "response_time_distribution",
                    "resource_usage_timeline"
                ],
                "metrics": [
                    "concurrent_users",
                    "response_times",
                    "error_rates",
                    "resource_metrics"
                ],
                "style": "load",
                "compression": True
            },
            TemplateType.TREND: {
                "sections": [
                    "trend_summary",
                    "performance_trends",
                    "error_trends",
                    "resource_trends",
                    "predictions"
                ],
                "charts": [
                    "trend_timeline",
                    "regression_analysis",
                    "forecast_chart"
                ],
                "metrics": [
                    "trend_indicators",
                    "growth_rates",
                    "prediction_metrics"
                ],
                "style": "trend",
                "compression": True
            },
            TemplateType.MINIMAL: {
                "sections": [
                    "summary",
                    "key_metrics"
                ],
                "charts": [
                    "overview_chart"
                ],
                "metrics": [
                    "essential_metrics"
                ],
                "style": "minimal",
                "compression": False
            }
        }
        
        return templates[template_type]

    @staticmethod
    def get_markdown_template(template_type: TemplateType) -> str:
        """Get markdown template.
        
        Args:
            template_type: Type of template to get
            
        Returns:
            Markdown template string
        """
        templates = {
            TemplateType.EXECUTIVE: """
# Executive Summary Report
Generated: {{ timestamp }}

## Overview
- Total Tests: {{ total_tests }}
- Pass Rate: {{ pass_rate }}%
- Trend: {{ trend }}

## Key Metrics
{% for metric in key_metrics %}
### {{ metric.name }}
- Value: {{ metric.value }}
- Trend: {{ metric.trend }}
- Status: {{ metric.status }}
{% endfor %}

## Recommendations
{% for rec in recommendations %}
- {{ rec }}
{% endfor %}
""",
            TemplateType.TECHNICAL: """
# Technical Test Report
Generated: {{ timestamp }}

## Test Details
Total Tests: {{ total_tests }}
- Passed: {{ passed_tests }}
- Failed: {{ failed_tests }}
- Skipped: {{ skipped_tests }}

## Performance Metrics
{% for metric in performance_metrics %}
### {{ metric.name }}
- Average: {{ metric.average }}
- P95: {{ metric.p95 }}
- Max: {{ metric.max }}
{% endfor %}

## Error Analysis
{% for error in errors %}
### {{ error.type }}
- Count: {{ error.count }}
- Impact: {{ error.impact }}
- Resolution: {{ error.resolution }}
{% endfor %}

## Code Coverage
- Line Coverage: {{ coverage.line }}%
- Branch Coverage: {{ coverage.branch }}%
- Function Coverage: {{ coverage.function }}%
""",
            # Add other templates here...
        }
        
        return templates.get(template_type, templates[TemplateType.MINIMAL])

    @staticmethod
    def get_csv_template(template_type: TemplateType) -> Dict[str, Any]:
        """Get CSV template configuration.
        
        Args:
            template_type: Type of template to get
            
        Returns:
            CSV template configuration
        """
        templates = {
            TemplateType.EXECUTIVE: {
                "files": [
                    {
                        "name": "summary",
                        "headers": [
                            "Metric",
                            "Value",
                            "Trend",
                            "Status"
                        ]
                    },
                    {
                        "name": "recommendations",
                        "headers": [
                            "Priority",
                            "Recommendation",
                            "Impact",
                            "Effort"
                        ]
                    }
                ]
            },
            TemplateType.TECHNICAL: {
                "files": [
                    {
                        "name": "test_results",
                        "headers": [
                            "Test Name",
                            "Status",
                            "Duration",
                            "Error Message"
                        ]
                    },
                    {
                        "name": "performance",
                        "headers": [
                            "Metric",
                            "Average",
                            "P95",
                            "Max",
                            "Trend"
                        ]
                    },
                    {
                        "name": "errors",
                        "headers": [
                            "Error Type",
                            "Count",
                            "Impact",
                            "Resolution"
                        ]
                    }
                ]
            },
            # Add other templates here...
        }
        
        return templates.get(template_type, {
            "files": [
                {
                    "name": "summary",
                    "headers": [
                        "Metric",
                        "Value"
                    ]
                }
            ]
        })

    @staticmethod
    def get_html_styles(template_type: TemplateType) -> str:
        """Get HTML styles for template.
        
        Args:
            template_type: Type of template to get
            
        Returns:
            CSS styles string
        """
        styles = {
            TemplateType.EXECUTIVE: """
                body { font-family: 'Arial', sans-serif; line-height: 1.6; }
                .header { background: linear-gradient(45deg, #1a237e, #0d47a1); color: white; padding: 2rem; }
                .metric { background: white; border-radius: 8px; padding: 1.5rem; margin: 1rem 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
                .chart { margin: 2rem 0; }
                .recommendations { background: #f5f5f5; padding: 1.5rem; border-radius: 8px; }
            """,
            TemplateType.TECHNICAL: """
                body { font-family: 'Consolas', monospace; line-height: 1.4; }
                .header { background: #263238; color: #e0e0e0; padding: 1rem; }
                .metric { font-family: monospace; background: #f5f5f5; padding: 1rem; margin: 0.5rem 0; }
                .code { background: #263238; color: #e0e0e0; padding: 1rem; border-radius: 4px; }
            """,
            # Add other styles here...
        }
        
        return styles.get(template_type, """
            body { font-family: sans-serif; }
            .header { background: #f5f5f5; padding: 1rem; }
            .metric { margin: 1rem 0; }
        """)


if __name__ == "__main__":
    # Example usage
    template = ReportTemplates.get_template(TemplateType.EXECUTIVE)
    print("Executive template sections:", template["sections"])
    
    markdown = ReportTemplates.get_markdown_template(TemplateType.TECHNICAL)
    print("\nTechnical markdown template preview:")
    print(markdown[:200] + "...")
