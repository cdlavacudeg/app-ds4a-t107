import pandas as pd
import folium
from folium.plugins import HeatMap
import plotly.express as px
from utils import api


def plot_suicides_per_dpto_year_population(normalized, year):
    """
    Bar plot of suicides in a specific year and normalized (or not)
    """
    # Call API Data
    df = api.suicideApi(year)
    # Drop unused columns
    df.drop(
        columns=["longitude", "latitude", "municipality_name", "municipality_code"],
        inplace=True,
    )
    # Group data for department name and sorted desending
    df_dpto = (
        df.groupby(["department_name"])
        .sum()
        .sort_values("suicides", ascending=False)
        .reset_index()
    )
    COLNAME = "suicides"
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
            "suicides": "Number of suicides",
            "suicides_OVER_POP": "Suicides per 100k habitants",
        },
        color="department_name",
        color_discrete_sequence=px.colors.sequential.haline,
    )
        
    # Title of the graphic depending if normalized is True
    title_aux = "normalized" if normalized else ""
    fig.update_layout(
        showlegend=False, title_text=f"Suicides in Colombia {title_aux}", title_x=0.5
    )
    return fig


def map_suicides_per_year_population(year):
    """
    Create the HeatMap of suicides in Colombia in a respective year
    """
    df = api.suicideApi(year)
    START_COORDS = [4.7110, -74.0721]
    map_aux = folium.Map(location=START_COORDS, zoom_start=5)

    df["cases_norm"] = 100000 * df["suicides"] / df["population"]
    df.drop(
        columns=[
            "suicides",
            "population",
            "municipality_name",
            "municipality_code",
            "department_name",
            "department_code",
        ],
        inplace=True,
    )
    heat_df = df[["latitude", "longitude", "cases_norm"]].dropna()
    maxvalue = heat_df["cases_norm"].max()
    minvalue = heat_df["cases_norm"].min()

    heat_df = [
        [
            row["latitude"],
            row["longitude"],
            (row["cases_norm"] - minvalue) / (maxvalue - minvalue),
        ]
        for index, row in heat_df.iterrows()
    ]

    
    HeatMap(heat_df, radius=10, blur=15, control=True).add_to(map_aux)
    return map_aux
