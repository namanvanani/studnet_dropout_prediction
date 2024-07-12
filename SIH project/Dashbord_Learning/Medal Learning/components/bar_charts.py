from dash import html, Dash, dcc
import plotly.express as px
from dash.dependencies import Input, Output
from . import ids

MEDAL_DATA = px.data.medals_long()


def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        Input(ids.NATION_DROPDOWN, "value")
    )
    def update_bar_chart(nations: list[str]) -> html.Div:
        filterd_data = MEDAL_DATA.query("nation in @nations")

        if filterd_data.shape[0] == 0:
            return html.Div("No Nation Selected")
        fig = px.bar(filterd_data, x="medal", y="count", color="nation", text="nation")
        return html.Div(children=dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)
