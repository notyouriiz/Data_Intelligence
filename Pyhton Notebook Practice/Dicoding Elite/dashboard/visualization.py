import pandas as pd
import plotly.express as px
from plotly.graph_objs import Figure
import plotly.graph_objects as go
from typing import Optional

def create_pie_chart(dataframe: pd.DataFrame, column: str, label: str, hole: str = 0.0) -> Figure: # --> do float not string
    """
    Creates a pie or donut chart from a specified column in a DataFrame.

    Parameters:
    - dataframe: pd.DataFrame - The DataFrame containing the data.
    - column: str - The name of the column to be counted for the pie chart.
    - label: str - The label for the pie chart slices.
    - hole: float - The size of the hole in the center for a donut chart effect (0 for pie, 0.1-0.9 for donut).

    Returns:
    - fig: Figure - The Plotly figure object for the pie or donut chart.
    """
    # Count the occurrences of each unique value in the specified column
    column_counts = dataframe[column].value_counts().reset_index()
    column_counts.columns = [label, 'Count']

    # Create a pie chart with Plotly, using hole parameter for donut effect
    fig = px.pie(column_counts, names=label, values='Count', title=f"{label} Distribution", hole=hole)
    fig.update_traces(hovertemplate='<b>%{label}</b><br>Total: %{value} person.<extra></extra>')
    return fig

def create_treemap(dataframe: pd.DataFrame, column: str, label: str) -> Figure:
    """
    Creates a treemap from a specified column in a DataFrame.

    Parameters:
    - dataframe: pd.DataFrame - The DataFrame containing the data.
    - column: str - The name of the column to be counted for the treemap.
    - label: str - The label for the treemap.

    Returns:
    - fig: Figure - The Plotly figure object for the treemap.
    """
    # Count the occurrences of each unique value in the specified column
    column_counts = dataframe[column].value_counts().reset_index()
    column_counts.columns = [label, 'Count']

    # Create a treemap with Plotly
    fig = px.treemap(column_counts, path=[label], values='Count', title=f"{label} Proportion")
    fig.update_traces(hovertemplate='<b>%{label}</b><br>Total: %{value} person.<extra></extra>')
    return fig


def create_funnel_chart(dataframe: pd.DataFrame, column: str, label: str,
                        color: Optional[str] = None) -> Figure:
    # Count occurrences for each unique value in the specified column
    if color:
        column_counts = dataframe.groupby([color, column])[column].size().reset_index(name='Count')
        column_counts.columns = [color, label, 'Count']
        fig = px.funnel(column_counts, y=label, x='Count', title=f"{label} Proportion", color=color)
        fig.update_traces(hovertemplate='<b>%{y}</b><br>Total: %{x} person.<extra></extra>')
    else:
        column_counts = dataframe[column].value_counts(ascending=True).reset_index()
        column_counts.columns = [label, 'Count']
        fig = px.funnel_area(column_counts, names=label, values='Count', title=f"{label} Proportion", color=color)
        fig.update_traces(hovertemplate='<b>%{label}</b><br>Total: %{value} person.<extra></extra>')
    return fig


def create_plot_average_by_group(dataframe: pd.DataFrame, group_column: str, value_column: str,
                          title: Optional[str] = None) -> Figure:
    """
    Creates a line chart visualizing the average values for each group in the specified column with Plotly.
    Adds a horizontal line representing the overall mean of the specified value column.

    Parameters:
    - dataframe: pd.DataFrame - The DataFrame containing the data.
    - group_column: str - The name of the column to group by for the x-axis (e.g., 'age_group').
    - value_column: str - The name of the column to calculate the mean for on the y-axis (e.g., 'sleep_duration').
    - title: Optional[str] - The title for the chart. Defaults to "Average <value_column> by <group_column>" if not specified.

    Returns:
    - fig: Figure - A Plotly figure object with the line chart.
    """
    # Calculate the average of the value column by the specified group column
    avg_by_group = dataframe.groupby(group_column)[value_column].mean().reset_index()

    # Calculate the overall mean of the value column
    overall_mean = dataframe[value_column].mean()

    # Define default title if not provided
    title = title or f"Average {value_column.replace('_', ' ').title()} by {group_column.replace('_', ' ').title()}"

    # Create the line chart
    fig = go.Figure()

    # Add line trace for the average values by group
    fig.add_trace(go.Scatter(
        x=avg_by_group[group_column],
        y=avg_by_group[value_column],
        mode='lines+markers+text',
        text=[f'{y:.2f}' for y in avg_by_group[value_column]],
        textposition='top center',
        marker=dict(color='blue', size=8),
        line=dict(color='blue', width=2),
        name=f'Average {value_column.replace("_", " ").title()}',
        hovertemplate="%{y:.2f}<extra></extra>"
    ))

    # Add horizontal line for overall mean
    fig.add_trace(go.Scatter(
        x=avg_by_group[group_column],
        y=[overall_mean] * len(avg_by_group),
        mode='lines',
        line=dict(color='red', dash='dash'),
        name="Overall Mean",
        hovertemplate=f"{overall_mean:.2f}<extra></extra>"  # Only displays text, no extra info
    ))

    # Customize layout with unified hover and title
    fig.update_layout(
        title=title,
        xaxis_title=group_column.replace('_', ' ').title(),
        yaxis_title=f"Average {value_column.replace('_', ' ').title()}",
        hovermode="x unified",  # Hover spans the x-axis
        showlegend=True,
        template="plotly_white"
    )

    return fig
