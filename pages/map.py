from dash import html, dcc, Input, Output, callback
from utils import violencia, suicidios, intentosS

slider = dcc.Slider(
    2016,
    2022,
    0,
    marks={
        2016: "2016",
        2017: "2017",
        2018: "2018",
        2019: "2019",
        2020: "2020",
        2021: "2021",
        2022: "2022",
    },
    value=2016,
    id="year-slider",
)
principalMap = html.Div(
    [
        html.H2("Suicides map for year"),
        html.Iframe(
            srcDoc=open("maps/mapa_suicidios.html", "r").read(),
            width="100%",
            height="300",
            id="map-principal",
        ),
        slider,
    ],
    className="card",
    id="map-abstract",
)

secondaryMap = html.Div(
    [
        html.H2("Violence map for year"),
        html.Iframe(
            srcDoc=open("maps/mapa_violencia.html", "r").read(),
            width="100%",
            height="300",
            id="map-secondary",
        ),
    ],
    className="card",
    id="map-secondary",
)

tertiaryMap = html.Div(
    [
        html.H2("Suicide attempts  map for year"),
        html.Iframe(
            srcDoc=open("maps/mapa_intentos_suicidio.html", "r").read(),
            width="100%",
            height="300",
            id="map-tertiary",
        ),
    ],
    className="card",
    id="fig2-abstract",
)

layout = [principalMap, secondaryMap, tertiaryMap]


@callback(
    Output("map-principal", "srcDoc"),
    Output("map-secondary", "srcDoc"),
    Output("map-tertiary", "srcDoc"),
    Input("year-slider", "value"),
)
def callback(value):
    mapaSuicidios = suicidios.map_suicides_per_year_population(value)
    mapaSuicidios.save("maps/mapa_suicidios.html")
    srcPrincipal = open("maps/mapa_suicidios.html", "r").read()

    mapaViolencia = violencia.map_violencia_per_year_population(value)
    mapaViolencia.save("maps/mapa_violencia.html")
    srcSecond = open("maps/mapa_violencia.html", "r").read()

    mapaIntentos = intentosS.map_trysuicides_per_year_population(value)
    mapaIntentos.save("maps/mapa_intentos_suicidio.html")
    srcThird = open("maps/mapa_intentos_suicidio.html", "r").read()

    return (srcPrincipal, srcSecond, srcThird)
