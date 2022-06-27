from dash import html, dcc, Input, Output, callback

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
            className="selector-container"
        ),
        html.Div(
            [
                html.H3("Select figure"),
                dcc.Dropdown(
                    options=["Suicides", "Violence", "Suicides attemps"],
                    value="Suicides",
                    id="figure-dropdown",
                ),
            ],
            className="selector-container"
        ),
    ],
    id="selectors-analysis",
)


figures = html.Div(
    [
        html.H2("Suicides map for year"),
        html.Iframe(
            srcDoc=open("data/violencia/mapa_suicidios.html", "r").read(),
            width="100%",
            height="300",
            id="map-principal",
        ),
    ],
    className="card",
    id="figure-analysis",
)

layout = [selectorNormalized, figures]
