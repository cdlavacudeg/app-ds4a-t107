from pydoc import classname
from dash import html, dcc, Input, Output, callback
from utils import violencia

mapaViolencia = violencia.map_suicides_per_year_population(2016)
mapaViolencia.save("data/violencia/mapa_suicidios.html")
mapContainer = html.Div(
    html.Iframe(
        srcDoc=open("data/violencia/mapa_suicidios.html", "r").read(),
        width="100%",
        height="300",
        id="map-v",
    ),
    className="card",
    id="map-abstract",
)
fig1Container = html.Div(className="card", id="fig1-abstract")
fig2Container = html.Div(className="card", id="fig2-abstract")

layout = [mapContainer, fig1Container, fig2Container]

# @callback(
#     Output("sidebar-id", "className"),
#     Output("container-id", "className"),
#     Input("btn", "n_clicks"),
# )
# def callback(n_clicks, current_classes):
#     print(n_clicks, current_classes)
#     if "active" in current_classes:
#         return "sidebar", "container"
#     return ("sidebar" + " active", "container" + " active")
