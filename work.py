import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample data (replace with your actual data)
# data = {
#     'State': ['State_A', 'State_A', 'State_B', 'State_B', 'State_C', 'State_C'],
#     'Year': [2018, 2019, 2018, 2019, 2018, 2019],
#     'Primary_Boys': [3.6, 8.8, 4.9, 1.97, 9.75, 5.83],
#     'Primary_Girls': [8.8, 6.57, 5.08, 3.57, 1.28, 0.58],
#     'Primary_Total': [8.63, 2.15, 8.51, 0.83, 1.16, 7.23],
#     'Secondary_Boys': [6.54, 8.67, 1.03, 9.33, 9.92, 3.88],
#     'Secondary_Girls': [4.68, 1.86, 4.72, 8.95, 9.45, 1.39],
#     'Secondary_Total': [4.28, 7.6, 8.17, 8.03, 2.5, 8.84]
# }

df = pd.read_csv("Student_Dropout.csv")

# Create the Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Dropout Rates Dashboard"),

    # Dropdown for states
    dcc.Dropdown(
        id='state-dropdown',
        options=[{'label': state, 'value': state} for state in df['State'].unique()],
        value=df['State'].unique()[0],
        multi=False,
        style={'width': '50%'}
    ),

    # Dropdown for years
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': year, 'value': year} for year in df['Year'].unique()],
        value=df['Year'].unique()[0],
        multi=False,
        style={'width': '50%'}
    ),

    # Bar chart
    dcc.Graph(id='bar-chart')
])


# Callback to update the bar chart based on dropdown selections
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('state-dropdown', 'value'),
     Input('year-dropdown', 'value')]
)
def update_bar_chart(selected_state, selected_year):
    filtered_df = df[(df['State'] == selected_state) & (df['Year'] == selected_year)]

    fig = px.bar(
        filtered_df,
        x='Category',
        y='Value',
        color='Value',
        title=f'Dropout Rates for {selected_state} in {selected_year}',
    )

    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
