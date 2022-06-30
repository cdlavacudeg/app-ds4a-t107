import pandas as pd
import folium
import matplotlib.pyplot as plt
from folium.plugins import HeatMap
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Selector para tres opciones
def plot_violencia_per_dpto_year_population(normalized):
    df = pd.read_csv("data/violencia/MERGED-ViolenciaPopulationGeo.csv")
    df.drop(
        columns=["CODE_DPTO", "CODE_MUNICIPIO", "MUNICIPIO", "LONGITUD", "LATITUD"],
        inplace=True,
    )
    years_arr = [2016, 2017, 2018, 2019, 2020, 2021]
    fig = make_subplots(
        rows=3,
        cols=2,
        shared_xaxes=True,
        shared_yaxes=True,
        subplot_titles=([f"Domestic violence in {x}" for x in years_arr]),
        vertical_spacing=0.05,
        horizontal_spacing=0.05,
    )

    row_fig = [1, 1, 2, 2, 3, 3]
    column_fig = [1, 2, 1, 2, 1, 2]
    for index, year in enumerate(years_arr):
        dfvi = df[df["YEAR"] == year]
        dfvi_dpto = (
            dfvi.groupby(["DPTO"])
            .sum()
            .sort_values("CANTIDAD", ascending=False)
            .reset_index()
        )
        COLNAME = "CANTIDAD"
        if normalized == True:
            COLNAMENEW = COLNAME + "OVER_POP"
            dfvi_dpto[COLNAMENEW] = (
                100000.0 * dfvi_dpto[COLNAME] / dfvi_dpto["POPULATION"]
            )
            dfvi_dpto = dfvi_dpto.sort_values(COLNAMENEW, ascending=False).reset_index()
            COLNAME = COLNAMENEW
        df_dpto = dfvi_dpto.head(20)
        fig.add_trace(
            go.Bar(x=df_dpto["DPTO"], y=df_dpto[COLNAME], showlegend=False),
            row=row_fig[index],
            col=column_fig[index],
        )
        fig.update_layout(
            height=900, width=900, title_text="Domestic violence Colombia", title_x=0.5
        )
    return fig


def map_violencia_per_year_population(year):
    df = pd.read_csv("data/violencia/MERGED-ViolenciaPopulationGeo.csv")
    df.drop(columns=["CODE_DPTO", "CODE_MUNICIPIO"], inplace=True)
    df = df[df["YEAR"] == year]
    # print(df.head())
    # Heat map for count of begin location
    START_COORDS = [4.7110, -74.0721]
    map_violencia = folium.Map(location=START_COORDS, zoom_start=5)
    # Create and clean the heat dataframe
    heat_df = df[["LATITUD", "LONGITUD"]].dropna()
    # Create the list of lists
    heat_df = [
        [row["LATITUD"], row["LONGITUD"]] for index, row in heat_df.iterrows()
    ]  # THIS IS SLOW!
    # Add the data to the map and plot
    HeatMap(heat_df, radius=10, blur=15, control=True).add_to(map_violencia)
    return map_violencia
