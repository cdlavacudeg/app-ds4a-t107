from dash import Dash, html, dcc, html, callback, Input, Output
from pages import map, analysis, riskProfile
from lib import navBar
import plotly.express as px
import pandas as pd

external_scripts = [
    {
        "src": "https://kit.fontawesome.com/828ca6943c.js",
        "crossorigin": "anonymous",
    }
]
app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    title="DS4A-T107",
    external_scripts=external_scripts,
)
server=app.server

app.layout = html.Div(
    children=[
        # represents the browser address bar and doesn't render anything
        dcc.Location(id="url", refresh=False),
        navBar.layout,
        html.H1(
            ["Proyect Name", html.Br(), html.Span("Team 107")], className="header-app"
        ),
        html.Div(className="content-container", id="page-content"),
    ],
    className="container",
    id="container-id",
)


@callback(
    Output("page-content", "children"),
    Output("abstract", "className"),
    Output("analysis", "className"),
    Output("risk", "className"),
    Output("page-content", "className"),
    Input("url", "pathname"),
)
def display_page(pathname):
    if pathname == "/":
        return (map.layout, "active", "", "", "content-container")
    if pathname == "/analysis":
        return (analysis.layout, "", "active", "", "content-container analysis")

    if pathname == "/risk-profile":
        return (riskProfile.layout, "", "", "active", "content-container risk-profile")


if __name__ == "__main__":
    app.run_server(debug=True)
