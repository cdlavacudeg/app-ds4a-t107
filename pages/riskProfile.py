from dash import dcc, html, Input, Output, callback
from utils import api, optionsLists, model

selectors = html.Div(
    [
        html.H3("Deparment"),
        dcc.Dropdown(
            options=api.listDepartments(),
            value=5,
            id="department-dropdown",
        ),
        html.H3("Municipality"),
        dcc.Dropdown(
            options=api.listMunicipalities(5),
            value=5001,
            id="municipality-dropdown",
        ),
        html.H3("Gender"),
        dcc.Dropdown(
            options=["Hombre", "Mujer"],
            value="Mujer",
            id="gender-dropdown",
        ),
        html.H3("Emotional state or cause"),
        dcc.Dropdown(
            options=optionsLists.emotionalState,
            value=optionsLists.emotionalState[0],
            id="emotionalState-dropdown",
        ),
        html.H3("Education"),
        dcc.Dropdown(
            options=optionsLists.educationList,
            value=optionsLists.educationList[0],
            id="education-dropdown",
        ),
        html.H3("Marital State"),
        dcc.Dropdown(
            options=optionsLists.maritalState,
            value=optionsLists.maritalState[0],
            id="maritalState-dropdown",
        ),
        html.H3("Age Group"),
        dcc.Dropdown(
            options=optionsLists.ageList,
            value=optionsLists.ageList[0],
            id="age-dropdown",
        ),
        html.H3("Vulnerability Factor"),
        dcc.Dropdown(
            options=optionsLists.vulneraList,
            value=optionsLists.vulneraList[0],
            id="vulnerability-dropdown",
        ),
    ],
    id="selectors-risk",
)
figures = html.Div(
    [
        html.H2("Suicides map for year"),
        html.Iframe(
            srcDoc=open("maps/mapa_suicidios.html", "r").read(),
            width="100%",
            height="300",
            id="map-principal",
        ),
    ],
    className="card",
    id="figure-risk",
)
figures = html.Div(
    [
        html.H2("Risk Factor"),
        html.Div(
            dcc.Graph(figure=model.fig, id="gauge-chart"),
            className="gauge-container",
        ),
    ],
    id="figure-risk",
    className="card",
)

layout = [selectors, figures]

# Callback that control the selectors
@callback(
    Output("municipality-dropdown", "options"),
    Output("municipality-dropdown", "value"),
    Input("department-dropdown", "value"),
)
def callback(department_id):
    data = api.listMunicipalities(department_id)
    return (data, data[0]["value"])
