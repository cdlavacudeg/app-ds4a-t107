# Load your libraries
import os
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc

import plotly.express as px

# Create the app

# workspace_user = os.getenv('JUPYTERHUB_USER')  # Get DS4A Workspace user name
# request_path_prefix = None
# if workspace_user:
#     request_path_prefix = '/user/' + workspace_user + '/proxy/8050/'

app = Dash(__name__, #requests_pathname_prefix=request_path_prefix, external_stylesheets=[dbc.themes.FLATLY],
                meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])
app.title = 'Bars - Correlation One'                 
                          
# Layout

app.layout = dbc.Container(
    [
           html.H1(['Hello Dash'], className="h-100 p-5 bg-light border rounded-3"),

           html.Div(children='''
                Dash: A web application framework for Python.
            '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )  

    ])



# Callbacks

# Start the server
if __name__ == '__main__':
    app.run_server(host="localhost", port="8050", debug=True)
