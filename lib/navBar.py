from dash import html, dcc, Input, Output, State, callback

# Logo DS4A in the Navbar
logo = html.Div(
    [html.Div([html.Div("DS4A", className="logo_name")], className="logo")],
    className="logo_content",
)

# List of links of the Navbar, it use icons from FontAwesome (ClassName)
ulNav = html.Ul(
    [
        html.Li(
            [
                dcc.Link(
                    [
                        html.I(className="fa-solid fa-file-waveform"),
                        html.Span("Maps", className="links_name"),
                    ],
                    href="/",
                    id="abstract",
                )
            ]
        ),
        html.Li(
            [
                dcc.Link(
                    [
                        html.I(className="fa-solid fa-chart-pie"),
                        html.Span("Analysis", className="links_name"),
                    ],
                    href="/analysis",
                    id="analysis",
                )
            ]
        ),
        html.Li(
            [
                dcc.Link(
                    [
                        html.I(className="fa-solid fa-circle-exclamation"),
                        html.Span("Risk profile", className="links_name"),
                    ],
                    href="/risk-profile",
                    id="risk",
                )
            ]
        ),
    ],
    className="nav_list",
)

# Return the layout that app.py is goin to render
layout = html.Div(
    [logo, html.I(className="fa-solid fa-bars", id="btn"), ulNav],
    className="sidebar",
    id="sidebar-id",
)

# Callback that control the active link style
@callback(
    Output("sidebar-id", "className"),
    Output("container-id", "className"),
    Input("btn", "n_clicks"),
    State("sidebar-id", "className"),
    prevent_initial_call=True,
)
def callback(n_clicks, current_classes):
    if "active" in current_classes:
        return "sidebar", "container"
    return ("sidebar active", "container active")
