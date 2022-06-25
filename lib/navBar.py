from pydoc import classname
from dash import html, dcc, Input, Output, State, callback

logo = html.Div(
    [html.Div([html.Div("DS4A", className="logo_name")], className="logo")],
    className="logo_content",
)

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
            [ # 2 selectores, normalizado, 
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
            [   # 4 Selectores , edad , genero(MF), Departamento -> Municipio, 
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


layout = html.Div(
    [logo, html.I(className="fa-solid fa-bars", id="btn"), ulNav],
    className="sidebar",
    id="sidebar-id",
)


@callback(
    Output("sidebar-id", "className"),
    Output("container-id", "className"),
    Input("btn", "n_clicks"),
    State("sidebar-id", "className"),
    prevent_initial_call=True,
)
def callback(n_clicks, current_classes):
    print(n_clicks, current_classes)
    if "active" in current_classes:
        return "sidebar", "container"
    return ("sidebar" + " active", "container" + " active")
