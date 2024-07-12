from dash import html, Dash
from . import nation_dropdown, bar_charts



def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className='dropdown-container',
                children=[nation_dropdown.render(app)]
            ),
            bar_charts.render(app)

        ]
    )
