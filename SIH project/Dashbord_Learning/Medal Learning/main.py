from dash import Dash, html
from components.layout import create_layout
from dash_bootstrap_components.themes import BOOTSTRAP


def main() -> None:
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Medal Dashbord"
    app.layout = create_layout(app)
    app.run(debug=True)


if __name__ == "__main__":
    main()
