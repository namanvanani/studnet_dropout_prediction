# ------------------------------------------------------------------------------------------
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from .loader import DataSchema
from . import ids
import pandas as pd
import plotly.graph_objects as go


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.PIE_CHART, "children"),
        [Input(ids.YEAR_DROPDOWN, "value"),
         Input(ids.MONTH_DROPDOWN, "value"),
         Input(ids.CATEGORY_DROPDOWN, "value"), ]
    )
    def update_pie_chart(years: list[str], months: list[str], categories: list[str]) -> html.Div:
        filtered_data = data.query("year in @years and month in @months and category in @categories")
        if filtered_data.shape[0] == 0:
            return html.Div("No Year or Month or Category is Selected", id=ids.PIE_CHART)

        pie = go.Pie(
            labels=filtered_data["category"].to_list(),
            values=filtered_data["amount"].to_list(),
            hole=0.5,
        )
        fig = go.Figure(data=[pie])
        fig.update_traces(hovertemplate="%{label}<br>$%{value:.2f}<extra></extra>")

        return html.Div(id=ids.PIE_CHART, children=dcc.Graph(figure=fig))

    return html.Div(id=ids.PIE_CHART)
