from pydoc import classname
from dash import html, dcc,Input, Output, callback

logo = html.Div(
    [   
        html.Div([
            html.Div("DS4A",className="logo_name")
        ],className="logo")
    ],
    className="logo_content"
)

ulNav = html.Ul([
    html.Li([
        dcc.Link([
            html.I(className="fa-solid fa-file-waveform"),
            html.Span("Abstract",className="links_name")
        ],href="/abstract")
    ]),
    html.Li([
        dcc.Link([
            html.I(className="fa-solid fa-chart-pie"),
            html.Span("Analysis",className="links_name")
        ],href="/analysis")
    ]),
    html.Li([
        dcc.Link([
            html.I(className="fa-solid fa-circle-exclamation"),
            html.Span("Risk profile",className="links_name")
        ],href="/risk-profile")
    ])
],className="nav_list")


layout = html.Div(
    [
        logo,
        html.I(className="fa-solid fa-bars",id="btn"),
        ulNav
    ],
    className="sidebar",
)

