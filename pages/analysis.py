from dash import html, dcc, Input, Output, callback

selectors = dcc.Slider(
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
    id="map-abstract",
)

layout = [selectors,figures]
