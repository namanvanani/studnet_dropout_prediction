# ------------------------------------------------------------------------------------------
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from .loader import DataSchema
from . import ids
import pandas as pd


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        [Input(ids.YEAR_DROPDOWN, "value"),
         Input(ids.MONTH_DROPDOWN, "value"),
         Input(ids.CATEGORY_DROPDOWN, "value"), ]
    )
    def update_bar_charts(years: list[str], months: list[str], categories: list[str]) -> html.Div:
        filtered_data = data.query("year in @years and month in @months and category in @categories")
        total_amount = filtered_data.sum()["amount"]
        if filtered_data.shape[0] == 0:
            return html.Div("No Year or Month or Category is Selected")

        def create_pivot_table() -> pd.DataFrame:
            pt = filtered_data.pivot_table(
                values="amount",
                index=["category"],
                aggfunc="sum",
                fill_value=0
            )
            return pt.reset_index().sort_values(by="amount", ascending=False)

        fig = px.bar(
            create_pivot_table(),
            x="category",
            y="amount",
            color="category",
            labels={'amount': 'Amount', 'category': 'Category'},  # Set axis labels
        )

        return html.Div(
            id=ids.BAR_CHART,
            children=[html.H1(f"Total Expense: {int(total_amount)} $"),
                      dcc.Graph(figure=fig)]
        )

    return html.Div(id=ids.BAR_CHART)
