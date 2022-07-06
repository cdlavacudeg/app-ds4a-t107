# Analysis page
from dash import html, dcc, Input, Output, callback
from utils import violencia, suicidios, intentosS
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Slider of years
slider = dcc.Slider(
    2016,
    2021,
    0,
    marks={
        2016: "2016",
        2017: "2017",
        2018: "2018",
        2019: "2019",
        2020: "2020",
        2021: "2021",
    },
    value=2016,
    id="year-slider",
    className="selector-container"
)

# Selector container of slider and dropdown that controls the figure to be rendered
selectorNormalized = html.Div(
    [
        html.Div(
            [
                html.H3("Variable"),
                dcc.Dropdown(
                    options=["Suicides", "Domestic violence", "Suicide attemps"],
                    value="Suicides",
                    id="figure-dropdown",
                ),
            ],
            className="selector-container",
        ),
        slider,
    ],
    id="selectors-analysis",
)

# Containers of the figures Normalized and not Normalized
figures = html.Div(
    [
        html.Div(
            dcc.Graph(id="figure-analysis-not-normalized"),
            className="figure-analysis-container",
        ),
        html.Div(
            dcc.Graph(id="figure-analysis-normalized"),
            className="figure-analysis-container",
        ),
    ],
    id="figure-analysis",
    className="card",
)

# Layout to be displayed
layout = [selectorNormalized, figures]

# Callback that control the figure displayed
@callback(
    Output("figure-analysis-normalized", "figure"),
    Output("figure-analysis-not-normalized", "figure"),
    Input("figure-dropdown", "value"),
    Input("year-slider", "value"),
)
def callback(figure, year):
    if figure == "Domestic violence":
        normalized = violencia.plot_violencia_per_dpto_year_population(True, year)
        noNormalized = violencia.plot_violencia_per_dpto_year_population(False, year)
    elif figure == "Suicide attemps":
        noNormalized = intentosS.plot_trysuicides_per_dpto_year_population(False, year)
        normalized = intentosS.plot_trysuicides_per_dpto_year_population(True, year)
    else:
        noNormalized = suicidios.plot_suicides_per_dpto_year_population(False, year)
        normalized = suicidios.plot_suicides_per_dpto_year_population(True, year)
    return (normalized, noNormalized)
