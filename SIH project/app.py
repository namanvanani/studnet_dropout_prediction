import dash
import dash.dcc as dcc
import dash.html as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import json

# Sample population data
population_data = {'State': ['Maharashtra', 'Karnataka', 'Uttar Pradesh', 'Bihar', 'West Bengal'],
                   'Population': [112374333, 61130704, 199812341, 104099452, 91276115],
                   'Colors': ['red', 'green', 'blue', 'orange', 'violet']}

population_df = pd.DataFrame(population_data)

with open('Indian_st.geojson', 'r') as file:
    geojson_data = json.load(file)

# Create Dash app
app = dash.Dash(__name__)

# Function to generate choropleth map figure
def get_bar_chart():
    fig = px.bar(population_data, x='State', y='Population', color='Colors')
    return fig

# App layout
app.layout = html.Div(children=[
    html.H1("This is Bar Chart"),
    dcc.Graph(id='chart', figure=get_bar_chart())
])

if __name__ == '__main__':
    app.run_server(debug=True)

