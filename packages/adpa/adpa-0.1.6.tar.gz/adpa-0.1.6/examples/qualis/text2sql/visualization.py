"""Visualization utilities for the Text-to-SQL Streamlit app."""
from typing import Dict, List, Any, Optional
import plotly.graph_objects as go
import plotly.express as px
import networkx as nx
import pandas as pd
from datetime import datetime

def create_schema_visualization(schema_data: List[Dict]) -> go.Figure:
    """Create an interactive schema visualization."""
    G = nx.Graph()
    
    # Add nodes for tables
    for schema in schema_data:
        table_name = schema['table_name']
        G.add_node(table_name, type='table')
        
        # Add nodes for columns
        schema_info = schema['schema_info']
        for col_name in schema_info.get('columns', {}):
            node_name = f"{table_name}.{col_name}"
            G.add_node(node_name, type='column')
            G.add_edge(table_name, node_name)
    
    # Add relationships
    for schema in schema_data:
        for rel in schema.get('relationships', []):
            source = schema['table_name']
            target = rel['target_table']
            G.add_edge(source, target, relationship=True)
    
    # Create layout
    pos = nx.spring_layout(G)
    
    # Create visualization
    fig = go.Figure()
    
    # Add table nodes
    table_pos = {n: pos[n] for n in G.nodes() if G.nodes[n]['type'] == 'table'}
    if table_pos:
        fig.add_trace(go.Scatter(
            x=[pos[0] for pos in table_pos.values()],
            y=[pos[1] for pos in table_pos.values()],
            mode='markers+text',
            name='Tables',
            text=list(table_pos.keys()),
            marker=dict(size=30, color='lightblue'),
            textposition='bottom center'
        ))
    
    # Add column nodes
    column_pos = {n: pos[n] for n in G.nodes() if G.nodes[n]['type'] == 'column'}
    if column_pos:
        fig.add_trace(go.Scatter(
            x=[pos[0] for pos in column_pos.values()],
            y=[pos[1] for pos in column_pos.values()],
            mode='markers+text',
            name='Columns',
            text=[n.split('.')[-1] for n in column_pos.keys()],
            marker=dict(size=20, color='lightgreen'),
            textposition='bottom center'
        ))
    
    # Add edges
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
    
    fig.add_trace(go.Scatter(
        x=edge_x,
        y=edge_y,
        mode='lines',
        line=dict(width=1, color='gray'),
        hoverinfo='none'
    ))
    
    # Update layout
    fig.update_layout(
        showlegend=True,
        hovermode='closest',
        title='Schema Visualization',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
    )
    
    return fig

def create_relationship_graph(relationships: List[Dict]) -> go.Figure:
    """Create a graph visualization of table relationships."""
    G = nx.DiGraph()
    
    # Add relationships
    for rel in relationships:
        source = rel['source_table']
        target = rel['target_table']
        G.add_edge(source, target, columns=rel['columns'])
    
    # Create layout
    pos = nx.spring_layout(G)
    
    # Create visualization
    fig = go.Figure()
    
    # Add nodes
    for node in G.nodes():
        x, y = pos[node]
        fig.add_trace(go.Scatter(
            x=[x],
            y=[y],
            mode='markers+text',
            name=node,
            text=[node],
            marker=dict(size=30, color='lightblue'),
            textposition='bottom center'
        ))
    
    # Add edges with labels
    for edge in G.edges(data=True):
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        
        # Edge line
        fig.add_trace(go.Scatter(
            x=[x0, x1],
            y=[y0, y1],
            mode='lines+text',
            line=dict(width=1),
            text=[', '.join(edge[2]['columns'])],
            textposition='middle center',
            hoverinfo='text',
            showlegend=False
        ))
    
    # Update layout
    fig.update_layout(
        showlegend=True,
        hovermode='closest',
        title='Table Relationships',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
    )
    
    return fig

def create_pattern_distribution_chart(pattern_stats: Dict) -> go.Figure:
    """Create a bar chart of SQL pattern distribution."""
    patterns = []
    counts = []
    success_rates = []
    
    for pattern, count in pattern_stats['most_common_patterns']:
        patterns.append(pattern)
        counts.append(count)
        success_rates.append(pattern_stats['pattern_success_rates'].get(pattern, 0))
    
    fig = go.Figure()
    
    # Add usage count bars
    fig.add_trace(go.Bar(
        x=patterns,
        y=counts,
        name='Usage Count',
        marker_color='lightblue'
    ))
    
    # Add success rate line
    fig.add_trace(go.Scatter(
        x=patterns,
        y=success_rates,
        name='Success Rate',
        yaxis='y2',
        line=dict(color='green', width=2)
    ))
    
    # Update layout
    fig.update_layout(
        title='SQL Pattern Distribution and Success Rates',
        xaxis_title='Pattern Type',
        yaxis_title='Usage Count',
        yaxis2=dict(
            title='Success Rate',
            overlaying='y',
            side='right',
            range=[0, 1]
        ),
        barmode='group'
    )
    
    return fig

def create_complexity_distribution(complexity_stats: List[float]) -> go.Figure:
    """Create a box plot of query complexity distribution."""
    fig = go.Figure()
    
    fig.add_trace(go.Box(
        y=complexity_stats,
        name='Query Complexity',
        boxpoints='all',
        jitter=0.3,
        pointpos=-1.8
    ))
    
    fig.update_layout(
        title='Query Complexity Distribution',
        yaxis_title='Complexity Score',
        showlegend=False
    )
    
    return fig

def create_learning_curve_chart(success_trend: List, complexity_trend: List) -> go.Figure:
    """Create a dual-axis chart showing learning progress."""
    fig = go.Figure()
    
    # Convert data
    dates = [datetime.fromisoformat(x[0]) for x in success_trend]
    success_rates = [x[1] for x in success_trend]
    complexity_scores = [x[1] for x in complexity_trend]
    
    # Add success rate line
    fig.add_trace(go.Scatter(
        x=dates,
        y=success_rates,
        name='Success Rate',
        line=dict(color='green', width=2)
    ))
    
    # Add complexity line
    fig.add_trace(go.Scatter(
        x=dates,
        y=complexity_scores,
        name='Avg Complexity',
        yaxis='y2',
        line=dict(color='blue', width=2)
    ))
    
    # Update layout
    fig.update_layout(
        title='Learning Progress Over Time',
        xaxis_title='Date',
        yaxis_title='Success Rate',
        yaxis2=dict(
            title='Average Complexity',
            overlaying='y',
            side='right'
        )
    )
    
    return fig

def show_metric_card(title: str, value: Any, trend_data: Optional[List] = None) -> None:
    """Display a metric card with optional sparkline."""
    import streamlit as st
    
    st.metric(
        label=title,
        value=value,
        delta=_calculate_trend_delta(trend_data) if trend_data else None
    )
    
    if trend_data:
        fig = go.Figure()
        
        # Add sparkline
        fig.add_trace(go.Scatter(
            y=[x[1] for x in trend_data[-10:]],
            mode='lines',
            line=dict(width=1, color='gray'),
            showlegend=False
        ))
        
        fig.update_layout(
            height=50,
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
        )
        
        st.plotly_chart(fig, use_container_width=True)

def _calculate_trend_delta(trend_data: List) -> float:
    """Calculate the trend delta for metrics."""
    if not trend_data or len(trend_data) < 2:
        return 0.0
    
    current = trend_data[-1][1]
    previous = trend_data[-2][1]
    
    return ((current - previous) / previous) * 100 if previous != 0 else 0.0

def show_system_health_indicators(health_data: Dict) -> None:
    """Display system health indicators."""
    import streamlit as st
    
    # Create columns for each health metric
    cols = st.columns(len(health_data))
    
    for col, (metric, status) in zip(cols, health_data.items()):
        with col:
            color = "green" if status == "good" else "orange"
            st.markdown(
                f"""
                <div style='text-align: center; color: {color};'>
                    <h3>{metric.replace('_', ' ').title()}</h3>
                    <p>{status.replace('_', ' ').title()}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

def show_recommendation_card(recommendation: Dict) -> None:
    """Display a recommendation card."""
    import streamlit as st
    
    color_map = {
        "pattern_improvement": "#FFE1E1",
        "schema_coverage": "#E1F5FE",
        "complexity_gap": "#FFF3E0"
    }
    
    background_color = color_map.get(recommendation["type"], "#FFFFFF")
    
    st.markdown(
        f"""
        <div style='
            background-color: {background_color};
            padding: 1rem;
            border-radius: 0.5rem;
            margin: 0.5rem 0;
        '>
            <h4>{recommendation["type"].replace("_", " ").title()}</h4>
            <p>{recommendation["suggestion"]}</p>
            {_format_recommendation_details(recommendation)}
        </div>
        """,
        unsafe_allow_html=True
    )

def _format_recommendation_details(recommendation: Dict) -> str:
    """Format additional recommendation details."""
    details = ""
    
    if "current_success_rate" in recommendation:
        details += f"Current Success Rate: {recommendation['current_success_rate']:.1%}<br>"
    
    if "current_coverage" in recommendation:
        details += f"Current Coverage: {recommendation['current_coverage']:.1%}<br>"
    
    if "current_gap" in recommendation:
        details += f"Complexity Gap: {recommendation['current_gap']:.2f}<br>"
    
    return f"<p><small>{details}</small></p>" if details else ""
