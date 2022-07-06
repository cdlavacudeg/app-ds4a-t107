from dash import dcc, html, Input, Output, callback
from utils import api

# List of options
emotionalState = [
    "Conflicto con pareja o ex-pareja",
    "Desamor",
    "Económicas",
    "Enfermedad física o mental",
    "Escolares - educativas",
    "Jurídicas",
    "Laborales",
    "Maltrato físico - sexual - psicológico",
    "Muerte de un familiar o amigo",
    "Suicidio de un familiar o amigo",
    "Otras",
    "Sin información Razon del suicidio",
    "Bullying",
    "Abuso de sustancias y alcohol",
    "Acceso a armas de fuego",
    "Estado de gestación",
    "Orientación sexual diversa",
    "Víctima de hostigamiento",
]
emotionalState.sort()
educationList = [
    "Educación inicial y educación preescolar",
    "Educación básica primaria",
    "Educación básica secundaria o secundaria baja",
    "Educación media o secundaria alta",
    "Educación técnica profesional y tecnológica",
    "Universitario",
    "Especialización, maestría o equivalente",
    "Doctorado o equivalente",
    "Sin escolaridad",
    "Sin información Escolaridad",
]
educationList.sort()

maritalState = [
    "Soltero (a)",
    "Unión libre",
    "Casado (a)",
    "Separado(a), divorciado(a)",
    "Viudo (a)",
    "No aplica",
    "Sin información Estado Conyugal",
]
maritalState.sort()

ageList = [
    "(05 a 09)",
    "(10 a 14)",
    "(15 a 17)",
    "(18 a 19)",
    "(20 a 24)",
    "(25 a 29)",
    "(30 a 34)",
    "(35 a 39)",
    "(40 a 44)",
    "(45 a 49)",
    "(50 a 54)",
    "(55 a 59)",
    "(60 a 64)",
    "(65 a 69)",
    "(70 a 74)",
    "(75 a 79)",
    "(80 y más)",
]
ageList.sort()

vulneraList=[
    'Campesinos (as) y/o trabajadores (as) del campo',
'Consumidores de sustancias psicoactivas (drogas, alcohol, etc.)',
'Persona en condición de desplazamiento',
'Funcionarios judiciales',
'Personas que ejercen actividades relacionadas con la salud en zonas de conflicto',
'Ejercicio de actividades sindicales o gremiales',
'Personas en situación de prostitución'
'Ex convictos (as)',
'Persona habitante de  la calle',
'Maestro - educador',
'Personas bajo custodia',
'Sector social LGBT',
'Personas desmovilizadas o reinsertadas',
'Pertenecientes a grupos étnicos',
'Presos o detenidos',
'Religiosos',
'Otro Factor de vulnerabilidad',
'Sin información Factor de vulnerabilidad',
'Líderes cívicos',
'Miembros de Organizaciones No Gubernamentales (ONG)',
'Persona adicta a una droga natural o sintética',
'Recicladores',
'Ninguno',
'Personas que ejercen actividades políticas',
'Discapacitados',
'Herido y/o enfermo bajo protección sanitaria o médica',
'Lider comunal',
'Personas que ejercen actividades de periodismo',
'Múltiples factores',
'Personas con capacidades diferentes',
]
vulneraList.sort()
selectors = html.Div(
    [
        html.H3("Deparment"),
        dcc.Dropdown(
            options=api.listDepartments(),
            value=5,
            id="normalized-risk-dropdown",
        ),
        html.H3("Municipality"),
        dcc.Dropdown(
            options=api.listMunicipalities(5),
            value=5001,
            id="figure-risk-dropdown",
        ),
        html.H3("Gender"),
        dcc.Dropdown(
            options=["Male", "Female"],
            value="Female",
            id="gender-risk-dropdown",
        ),
        html.H3("Emotional state or cause"),
        dcc.Dropdown(
            options=emotionalState,
            value=emotionalState[0],
            id="cause-risk-dropdown",
        ),
        html.H3("Education"),
        dcc.Dropdown(
            options=educationList,
            value=educationList[0],
            id="gender-risk-dropdown",
        ),
        html.H3("Marital State"),
        dcc.Dropdown(
            options=maritalState,
            value=maritalState[0],
            id="gender-risk-dropdown",
        ),
        html.H3("Age Group"),
        dcc.Dropdown(
            options=ageList,
            value=ageList[0],
            id="gender-risk-dropdown",
        ),
        html.H3("Vulnerability Factor"),
        dcc.Dropdown(
            options=vulneraList,
            value=vulneraList[0],
            id="gender-risk-dropdown",
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

layout = [selectors, figures]

# Callback that control the selectors
@callback(
    Output("figure-risk-dropdown", "options"),
    Output("figure-risk-dropdown", "value"),
    Input("normalized-risk-dropdown", "value"),
)
def callback(department_id):
    data = api.listMunicipalities(department_id)
    return (data, data[0]["value"])
