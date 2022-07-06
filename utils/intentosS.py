# This file Contains the Data processing of Suicide attemps
import pandas as pd
import folium
from folium.plugins import HeatMap
import plotly.express as px
from utils import api


def plot_trysuicides_per_dpto_year_population(normalized, year):
    """
    Bar plot of suicide attemps in a specific year and normalized (or not)
    """
    # Call API Data
    df = api.suicidesAttempsApi(year)
    # Drop unused columns
    df.drop(
        columns=["longitude", "latitude", "municipality_name", "municipality_code"],
        inplace=True,
    )
    COLNAME = "suicide_attempts"
    # Group data for department name and sorted desending
    df_dpto = (
        df.groupby(["department_name"])
        .sum()
        .sort_values(COLNAME, ascending=False)
        .reset_index()
    )
    # If normalized is required execute the respective calculation.
    if normalized == True:
        COLNAMENEW = COLNAME + "_OVER_POP"
        df_dpto[COLNAMENEW] = 100000.0 * df_dpto[COLNAME] / df_dpto["population"]
        df_dpto = df_dpto.sort_values(COLNAMENEW, ascending=False).reset_index()
        COLNAME = COLNAMENEW
    # Select only the 20 deparments with more cases
    df_dpto = df_dpto.head(20)

    # Create the bar Plot
    fig = px.bar(
        df_dpto,
        x="department_name",
        y=COLNAME,
        labels={
            "department_name": "Department",
            "suicide_attempts": "Suicide attemps",
            "suicide_attempts_OVER_POP": "SA per 100k habitants",
        },
        color="department_name",  # Color from deparment
        color_discrete_sequence=px.colors.sequential.haline,  # Colorscheme
    )
    # Title of the graphic depending if normalized is True
    title_aux = "normalized" if normalized else ""
    fig.update_layout(
        showlegend=False,
        title_text=f"Suicide attemps in Colombia {title_aux}",
        title_x=0.5,
    )

    return fig


def map_trysuicides_per_year_population(year):
    """
    Create the HeatMap of suicide attemps in Colombia
    """
    # Call Data from the API
    df = api.suicidesAttempsApi(year)
    # Create the base map with folium
    START_COORDS = [4.7110, -74.0721]
    map_aux = folium.Map(location=START_COORDS, zoom_start=5)
    # Create normalized data and clean the unused columns
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
    # Drop NA
    heat_df = df[["latitude", "longitude", "cases_norm"]].dropna()
    # Create the list of lists of the data that folium HeatMap needs
    heat_df = [
        [row["latitude"], row["longitude"], row["cases_norm"]]
        for index, row in heat_df.iterrows()
    ]
    # Process the data with the HeatMap and add it to the map and plot
    HeatMap(heat_df, radius=10, blur=15, control=True).add_to(map_aux)
    return map_aux
