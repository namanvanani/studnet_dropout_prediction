from dash import Dash, dcc, html
from . import ids
from dash.dependencies import Input, Output
import pandas as pd
from .loader import DataSchema


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_year: list[str] = data["year"].to_list()
    unique_years = sorted(set(all_year), key=int)

    @app.callback(
        Output(ids.YEAR_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_BUTTON, "n_clicks")
    )
    def update_dropdown(_: int) -> list[str]:
        return unique_years

    return html.Div(
        children=[
            html.H6("Year"),
            dcc.Dropdown(
                id=ids.YEAR_DROPDOWN,
                options=[{"label": year, "value": year} for year in unique_years],
                value=unique_years,
                multi=True,
            ),
            html.Button(
                children=["Select All"],
                id=ids.SELECT_ALL_BUTTON,
                n_clicks=0,
                style={
                    'margin-top': '5px',
                    'width': '100%'
                }
            )
        ],
    )
