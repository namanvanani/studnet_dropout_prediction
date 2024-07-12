from dash import Dash
from components.layout import create_layout
from dash_bootstrap_components.themes import BOOTSTRAP
from components import loader

DATA_PATH = "./data/transactions.csv"


def main() -> None:
    data = loader.load_transaction_data(DATA_PATH)

    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Financial Dashbord"
    app.layout = create_layout(app, data)
    app.run(debug=True)


if __name__ == "__main__":
    main()
