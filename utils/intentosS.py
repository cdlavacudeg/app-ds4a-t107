import pandas as pd
import folium
import matplotlib.pyplot as plt
from folium.plugins import HeatMap
import plotly.express as px
from utils import api

def plot_trysuicides_per_dpto_year_population(normalized, year):
    df = api.suicidesAttempsApi(year)
    df.drop(
        columns=["longitude", "latitude", "municipality_name", "municipality_code"],
        inplace=True,
    )
    COLNAME = "suicide_attempts"
    df_dpto = (
        df.groupby(["department_name"])
        .sum()
        .sort_values(COLNAME, ascending=False)
        .reset_index()
    )

    if normalized == True:
        COLNAMENEW = COLNAME + "_OVER_POP"
        df_dpto[COLNAMENEW] = 100000.0 * df_dpto[COLNAME] / df_dpto["population"]
        df_dpto = df_dpto.sort_values(COLNAMENEW, ascending=False).reset_index()
        COLNAME = COLNAMENEW
    df_dpto = df_dpto.head(20)

    fig = px.bar(
        df_dpto,
        x="department_name",
        y=COLNAME,
        labels={
            "department_name": "Department",
            "suicide_attempts": "Suicide attemps",
            "suicide_attempts_OVER_POP": "SA per 100k habitants",
        },
        color="department_name",
        color_discrete_sequence=px.colors.sequential.haline,
    )
    title_aux = "normalized" if normalized else ""
    fig.update_layout(
        showlegend=False,
        title_text=f"Suicide attemps in Colombia {title_aux}",
        title_x=0.5,
    )

    return fig


def map_trysuicides_per_year_population(year):
    df = api.suicidesAttempsApi(year)
    # Heat map for count of begin location
    START_COORDS = [4.7110, -74.0721]
    map_aux = folium.Map(location=START_COORDS, zoom_start=5)
    # Create and clean the heat dataframe
    df["cases_norm"] = 100000 * df["suicide_attempts"] / df["population"]
    df.drop(
        columns=[
            "suicide_attempts",
            "population",
            "municipality_name",
            "municipality_code",
            "department_name",
            "department_code",
        ],
        inplace=True,
    )
    heat_df = df[["latitude", "longitude","cases_norm"]].dropna()
    # Create the list of lists
    heat_df = [
        [row["latitude"], row["longitude"],row["cases_norm"]] for index, row in heat_df.iterrows()
    ]  # THIS IS SLOW!
    # Add the data to the map and plot
    HeatMap(heat_df, radius=10, blur=15, control=True).add_to(map_aux)
    return map_aux
