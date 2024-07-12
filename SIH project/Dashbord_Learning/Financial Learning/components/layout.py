from dash import dcc, html, Dash
import pandas as pd
from . import year_dropdown, month_dropdown, bar_charts, category_dropdown, pie_chart

def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H4(app.title),
            html.Hr(),  # Darker border color
            html.Div(
                className="dropdown-container",
                children=[
                    year_dropdown.render(app, data),
                    month_dropdown.render(app, data),
                    category_dropdown.render(app, data),
                ],
            ),
            html.Div(
                className="bar-charts-container",
                children=[
                    bar_charts.render(app, data),
                ]
            ),
            html.Div(
                className="bar-charts-container",
                children=[
                    pie_chart.render(app, data),
                ]
            ),

        ]
    )
