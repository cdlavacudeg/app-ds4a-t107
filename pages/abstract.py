from pydoc import classname
from dash import html, dcc, Input, Output

mapContainer = html.Div(className="card", id="map-abstract")
fig1Container = html.Div(className="card", id="fig1-abstract")
fig2Container = html.Div(className="card", id="fig2-abstract")

layout = [mapContainer, fig1Container, fig2Container]
