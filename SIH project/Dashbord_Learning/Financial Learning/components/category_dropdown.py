# ---------------------------------------------------------------------------------------
from dash import Dash, dcc, html
from . import ids
from dash.dependencies import Input, Output
import pandas as pd
from .loader import DataSchema


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_category: list[str] = data["category"].to_list()
    unique_categories = sorted(set(all_category))

    @app.callback(
        Output(ids.CATEGORY_DROPDOWN, "value"),
        [Input(ids.YEAR_DROPDOWN, "value"),
         Input(ids.MONTH_DROPDOWN, "value"),
         Input(ids.SELECT_ALL_CATEGORY_BUTTON, "n_clicks")]
    )
    def update_months(years: list[str], months:list[str], _: int) -> list[str]:
        filtered_data = data.query("year in @years and month in @months")
        return sorted(set(filtered_data["category"].to_list()))

    return html.Div(
        children=[
            html.H6("Category", id="total-amount"),
            dcc.Dropdown(
                id=ids.CATEGORY_DROPDOWN,
                options=[{"label": month, "value": month} for month in unique_categories],
                value=unique_categories,
                multi=True,
            ),
            html.Button(
                children=["Select All"],
                id=ids.SELECT_ALL_CATEGORY_BUTTON,
                n_clicks=0,
                style={
                    'margin-top': '5px',
                    'width': '100%'
                }
            )
        ],
    )
