import pandas as pd
import folium
from folium.plugins import HeatMap
import plotly.express as px
from utils import api

# Selector para tres opciones
def plot_violencia_per_dpto_year_population(normalized, year):
    df = api.violenceApi(year)
    df.drop(
        columns=["code", "longitude", "latitude"],
        inplace=True,
    )
    dfvi = df
    dfvi_dpto = (
        dfvi.groupby(["name"])
        .sum()
        .sort_values("violence_cases", ascending=False)
        .reset_index()
    )
    COLNAME = "violence_cases"
    if normalized == True:
        COLNAMENEW = COLNAME + "OVER_POP"
        dfvi_dpto[COLNAMENEW] = 100000.0 * dfvi_dpto[COLNAME] / dfvi_dpto["population"]
        dfvi_dpto = dfvi_dpto.sort_values(COLNAMENEW, ascending=False).reset_index()
        COLNAME = COLNAMENEW
    df_dpto = dfvi_dpto.head(20)
    fig = px.bar(
        df_dpto,
        x="name",
        y=COLNAME,
        labels={
            "name": "Municipality",
            "violence_cases": "Domestic violence count",
            "violence_casesOVER_POP": "DV per 100k habitants",
        },
        color="name",
        color_discrete_sequence=px.colors.sequential.haline,
    )
    title_aux = "normalized" if normalized else ""
    fig.update_layout(
        showlegend=False,
        title_text=f"Suicide violence in Colombia {title_aux}",
        title_x=0.5,
    )

    return fig


def map_violencia_per_year_population(year):
    df = api.violenceApi(year)
    df["cases_norm"] = 100000 * df["violence_cases"] / df["population"]
    df.drop(
        columns=[
            "violence_cases",
            "population",
            "municipality_name",
            "municipality_code",
            "department_name",
            "department_code"
        ],
        inplace=True,
    )
    # Heat map for count of begin location
    START_COORDS = [4.7110, -74.0721]
    map_violencia = folium.Map(location=START_COORDS, zoom_start=5)
    # Create and clean the heat dataframe
    heat_df = df[["latitude", "longitude", "cases_norm"]].dropna()
    # Create the list of lists
    heat_df = [[row["latitude"], row["longitude"], row["cases_norm"]] for index, row in heat_df.iterrows()]
    # Add the data to the map and plot
    HeatMap(heat_df, radius=10, blur=15, control=True).add_to(map_violencia)
    return map_violencia
