import pandas as pd
import folium
import matplotlib.pyplot as plt
from folium.plugins import HeatMap
import plotly.express as px


def plot_suicides_per_dpto_year_population(normalized, year):
    df = pd.read_csv("data/violencia/MERGED-2016-2022-Suicidios-Geo-Pop.csv")
    df.drop(
        columns=["CODE_DPTO", "CODE_MUNICIPIO", "MUNICIPIO", "LONGITUD", "LATITUD"],
        inplace=True,
    )
    df_dpto = df[df["YEAR"] == year]
    df_dpto = (
        df_dpto.groupby(["DPTO"])
        .sum()
        .sort_values("SUI_COUNTER", ascending=False)
        .reset_index()
    )
    COLNAME = "SUI_COUNTER"
    if normalized == True:
        COLNAMENEW = COLNAME + "_OVER_POP"
        df_dpto[COLNAMENEW] = 100000.0 * df_dpto[COLNAME] / df_dpto["POPULATION"]
        df_dpto = df_dpto.sort_values(COLNAMENEW, ascending=False).reset_index()
        COLNAME = COLNAMENEW

    df_dpto = df_dpto.head(20)

    fig = px.bar(
        df_dpto,
        x="DPTO",
        y=COLNAME,
        labels={
            "DPTO": "Department",
            "SUI_COUNTER": "Number of suicides",
            "SUI_COUNTER_OVER_POP": "Suicides per 100k habitants",
        },
        color="DPTO",
        color_discrete_sequence=px.colors.sequential.haline,
    )
    title_aux = "normalized" if normalized else ""
    fig.update_layout(
        showlegend=False, title_text=f"Suicides in Colombia {title_aux}", title_x=0.5
    )
    return fig


def map_suicides_per_year_population(year):
    df = pd.read_csv("data/violencia/MERGED-2016-2022-Suicidios-Geo-Pop.csv")
    # df.drop(columns=["CODE_DPTO", "CODE_MUNICIPIO"], inplace=True) # NOT NEED SINCE I AM KEEPING ONLY LAT AND LONG
    df = df[df["YEAR"] == year]
    # print(df.head())
    START_COORDS = [4.7110, -74.0721]
    map_aux = folium.Map(location=START_COORDS, zoom_start=5)
    # Create and clean the heat dataframe
    heat_df = df[["LATITUD", "LONGITUD"]].dropna()
    # Create the list of lists
    heat_df = [
        [row["LATITUD"], row["LONGITUD"]] for index, row in heat_df.iterrows()
    ]  # THIS IS SLOW!
    # Add the data to the map and plot
    HeatMap(heat_df, radius=10, blur=15, control=True).add_to(map_aux)
    return map_aux
