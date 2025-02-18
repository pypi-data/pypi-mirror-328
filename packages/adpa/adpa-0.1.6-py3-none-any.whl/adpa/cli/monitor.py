"""
Monitoring CLI module.
"""
import click
import json
from typing import Optional
from datetime import datetime, timedelta

from adpa.monitoring import Monitor


@click.group(name="monitor")
def monitor_cli():
    """Monitoring system commands."""
    pass


@monitor_cli.command()
@click.option("--from-time", help="Start time (ISO format)")
@click.option("--to-time", help="End time (ISO format)")
@click.option("--last", help="Last n minutes/hours/days (e.g., '30m', '24h', '7d')")
@click.option("--output", "-o", help="Output file path")
def metrics(from_time: Optional[str], to_time: Optional[str], 
           last: Optional[str], output: Optional[str]):
    """Get system metrics."""
    monitor = Monitor()
    
    # Parse time range
    if last:
        unit = last[-1]
        value = int(last[:-1])
        now = datetime.now()
        if unit == 'm':
            from_time = (now - timedelta(minutes=value)).isoformat()
        elif unit == 'h':
            from_time = (now - timedelta(hours=value)).isoformat()
        elif unit == 'd':
            from_time = (now - timedelta(days=value)).isoformat()
        to_time = now.isoformat()
    
    # Get metrics
    metrics = monitor.get_metrics(
        from_time=from_time,
        to_time=to_time
    )
    
    # Output results
    if output:
        with open(output, "w") as f:
            json.dump(metrics, f, indent=2)
        click.echo(f"Metrics written to {output}")
    else:
        click.echo(json.dumps(metrics, indent=2))


@monitor_cli.command()
def status():
    """Get monitoring system status."""
    monitor = Monitor()
    status = monitor.get_status()
    click.echo(json.dumps(status, indent=2))


@monitor_cli.command()
@click.argument("alert_config")
def configure_alerts(alert_config: str):
    """Configure monitoring alerts."""
    with open(alert_config) as f:
        config = json.load(f)
    
    monitor = Monitor()
    monitor.configure_alerts(config)
    click.echo("Alert configuration updated")


def main():
    """Entry point for monitor CLI."""
    monitor_cli()
