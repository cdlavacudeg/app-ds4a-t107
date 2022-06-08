from pydoc import classname
from dash import Dash,dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.

layout = html.Div(
    [
        html.H2("DS4A",className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Abstract", href="/fig1",active="exact"),
                dbc.NavLink("Analisis", href="/fig2",active="exact"),
                dbc.NavLink("Risk Profile", href="/dashboard",active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

