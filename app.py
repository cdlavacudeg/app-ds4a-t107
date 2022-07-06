from dash import Dash, html, dcc, html, callback, Input, Output
from pages import map, analysis, riskProfile
from lib import navBar

## Basic dash app configuration

# Fontawsome icons for navBar
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
server = app.server

# Principal layout to be display
app.layout = html.Div(
    children=[
        # represents the browser address bar and doesn't render anything, for the multi page app
        dcc.Location(id="url", refresh=False),
        # Navbar
        navBar.layout,
        # Header
        html.H1(
            [
                "Using Data Science to prevent suicides",
                html.Br(),
                html.Span("Team 107"),
            ],
            className="header-app",
        ),
        # Content controled by the callback
        html.Div(className="content-container", id="page-content"),
    ],
    className="container",
    id="container-id",
)

# Callback that control the multi page content, and control the css classNames for the layouts
@callback(
    Output("page-content", "children"),
    Output("abstract", "className"),
    Output("analysis", "className"),
    Output("risk", "className"),
    Output("page-content", "className"),
    Input("url", "pathname"),
)
def display_page(pathname):
    # Display a diferent content from the path of the url
    if pathname == "/":
        return (map.layout, "active", "", "", "content-container")
    if pathname == "/analysis":
        return (analysis.layout, "", "active", "", "content-container analysis")

    if pathname == "/risk-profile":
        return (riskProfile.layout, "", "", "active", "content-container risk-profile")


# Run the server
if __name__ == "__main__":
    app.run_server(debug=True)
