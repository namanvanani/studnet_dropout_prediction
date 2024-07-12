# ---------------------------------------------------------------------------------------
from dash import Dash, dcc, html
from . import ids
from dash.dependencies import Input, Output
import pandas as pd
from .loader import DataSchema


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_months: list[str] = data["month"].to_list()
    unique_months = sorted(set(all_months), key=int)

    @app.callback(
        Output(ids.MONTH_DROPDOWN, "value"),
        [Input(ids.YEAR_DROPDOWN, "value"),
         Input(ids.SELECT_ALL_MONTH_BUTTON, "n_clicks")]
    )
    def update_months(years: list[str], _: int) -> list[str]:
        filtered_data = data.query("year in @years")
        return sorted(set(filtered_data["month"].to_list()))

    return html.Div(
        children=[
            html.H6("Month"),
            dcc.Dropdown(
                id=ids.MONTH_DROPDOWN,
                options=[{"label": month, "value": month} for month in unique_months],
                value=unique_months,
                multi=True,
            ),
            html.Button(
                children=["Select All"],
                id=ids.SELECT_ALL_MONTH_BUTTON,
                n_clicks=0,
                style={
                    'margin-top': '5px',
                    'width': '100%'
                }
            )
        ],
    )
