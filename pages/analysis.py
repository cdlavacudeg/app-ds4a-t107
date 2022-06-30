from dash import html, dcc, Input, Output, callback
from utils import violencia, suicidios, intentosS
from plotly.subplots import make_subplots
import plotly.graph_objects as go

selectorNormalized = html.Div(
    [
        html.Div(
            [
                html.H3("Normalized"),
                dcc.Dropdown(
                    options=[
                        {"label": "Yes", "value": True},
                        {"label": "No", "value": False},
                    ],
                    value=True,
                    id="normalized-dropdown",
                ),
            ],
            className="selector-container",
        ),
        html.Div(
            [
                html.H3("Select figure"),
                dcc.Dropdown(
                    options=["Suicides", "Domestic violence", "Suicide attemps"],
                    value="Suicides",
                    id="figure-dropdown",
                ),
            ],
            className="selector-container",
        ),
    ],
    id="selectors-analysis",
)


figures = dcc.Graph(id="figure-analysis",className='card')

layout = [selectorNormalized, figures]

@callback(
    Output("figure-analysis", "figure"),
    Input("normalized-dropdown", "value"),
    Input("figure-dropdown", "value"),
)
def callback(normalized, figure):
    if figure == 'Domestic violence':
        return violencia.plot_violencia_per_dpto_year_population(normalized)
    elif figure == 'Suicide attemps':
        return intentosS.plot_trysuicides_per_dpto_year_population(normalized)
    else:
        return suicidios.plot_suicides_per_dpto_year_population(normalized)
