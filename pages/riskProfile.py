from dash import dcc, html, Input, Output, callback

selectors = html.Div(
    [
        html.H3("Deparment"),
        dcc.Dropdown(
            options=[
                {"label": "Yes", "value": True},
                {"label": "No", "value": False},
            ],
            value=True,
            id="normalized-dropdown",
        ),
        html.H3("Select figure"),
        dcc.Dropdown(
            options=['Suicides','Violence','Suicides attemps'],
            value='Suicides',
            id="figure-dropdown",
        ),
    ],
    id='selectors-risk'
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
    id="figure-risk",
)

layout = [selectors,figures]

# @callback(Output("page-1-display-value", "children"), Input("page-1-dropdown", "value"))
# def display_value(value):
#     return f"You have selected {value}"
