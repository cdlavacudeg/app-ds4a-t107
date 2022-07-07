from dash import dcc, html, Input, Output, State,callback
from utils import api, optionsLists, model
import math
deparmentList = api.listDepartments()
municipalityList = api.listMunicipalities(5)

selectors = html.Div(
    [
        html.H3("Deparment"),
        dcc.Dropdown(
            options=deparmentList,
            value=5,
            id="department-dropdown",
        ),
        html.H3("Municipality"),
        dcc.Dropdown(
            options=municipalityList,
            value=5001,
            id="municipality-dropdown",
        ),
        html.H3("Gender"),
        dcc.Dropdown(
            options=["Masculino", "Femenino"],
            value="Femenino",
            id="gender-dropdown",
        ),
        html.H3("Age Group"),
        dcc.Dropdown(
            options=optionsLists.ageList,
            value=optionsLists.ageList[0],
            id="age-dropdown",
        ),
        html.H3("Emotional state or cause"),
        dcc.Dropdown(
            options=optionsLists.emotionalState,
            value=optionsLists.emotionalState[0],
            id="emotionalState-dropdown",
        ),
        html.H3("Marital State"),
        dcc.Dropdown(
            options=optionsLists.maritalState,
            value=optionsLists.maritalState[0],
            id="maritalState-dropdown",
        ),
        html.H3("Education"),
        dcc.Dropdown(
            options=optionsLists.educationList,
            value=optionsLists.educationList[0],
            id="education-dropdown",
        ),
        html.H3("Vulnerability Factor"),
        dcc.Dropdown(
            options=optionsLists.vulneraList,
            value=optionsLists.vulneraList[0],
            id="vulnerability-dropdown",
        ),
        html.Div([html.Button("Submit", id="btn-risk")], className="btn-container"),
    ],
    id="selectors-risk",
)

figures = html.Div(
    [
        html.H2("Risk Factor"),
        html.Div(
            dcc.Graph(figure=model.renderFigure(10), id="gauge-chart"),
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
def municipalityListUpdate(department_id):
    data = api.listMunicipalities(department_id)
    return (data, data[0]["value"])


@callback(
    Output("gauge-chart", "figure"),
    Input("btn-risk", "n_clicks"),
    State("department-dropdown", "value"),
    State("department-dropdown", "options"),
    State("municipality-dropdown", "value"),
    State("municipality-dropdown", "options"),
    State("gender-dropdown", "value"),
    State("age-dropdown", "value"),
    State("emotionalState-dropdown", "value"),
    State("maritalState-dropdown", "value"),
    State("education-dropdown", "value"),
    State("vulnerability-dropdown", "value"),
    prevent_initial_call=True,
)
def calculateModel(
    n_clicks,
    department_code,
    department_array,
    municipality_code,
    municipality_array,
    gender,
    age_group,
    cause,
    marital_status,
    scolarship,
    vulnerability_factor
):
    # Extract deparment in department options
    department = [
        x["label"] for x in department_array if x["value"] == department_code
    ][0]
    # Extract municipality in deparment options
    municipality = [
        x["label"] for x in municipality_array if x["value"] == municipality_code
    ][0]
    value=api.modelExecute(
        department,
        municipality,
        gender,
        age_group,
        cause,
        marital_status,
        scolarship,
        vulnerability_factor
    )
    
    return model.renderFigure(math.floor(value*100))
