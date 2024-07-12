from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from . import ids


def render(app: Dash) -> html.Div:
    all_nations = ["South Korea", "China", "Canada"]

    @app.callback(
        Output(ids.NATION_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_NATIONS_BUTTON, "n_clicks"),
    )
    def select_all_nations(_: int) -> list[str]:
        return all_nations

    return html.Div(
        children=[
            html.H4("Nations"),
            dcc.Dropdown(
                id=ids.NATION_DROPDOWN,
                multi=True,
                options=[{"label": nation, "value": nation} for nation in all_nations],
                value=all_nations
            ),
            html.Button(
                className="dropdown-button",
                children=["Selcet All"],
                id=ids.SELECT_ALL_NATIONS_BUTTON
            )
        ]
    )
