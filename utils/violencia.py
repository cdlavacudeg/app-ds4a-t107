import pandas as pd
import folium
import matplotlib.pyplot as plt
from folium.plugins import HeatMap

# Selector para tres opciones
def plot_violencia_per_dpto_year_population(normalized):
    df = pd.read_csv("data/violencia/MERGED-ViolenciaPopulationGeo.csv")
    df.drop(
        columns=["CODE_DPTO", "CODE_MUNICIPIO", "MUNICIPIO", "LONGITUD", "LATITUD"],
        inplace=True,
    )
    fig, ax = plt.subplots(3, 2, figsize=(13, 10), sharex=True, sharey=True)
    ax = ax.flatten()
    for ii, year in enumerate([2016, 2017, 2018, 2019, 2020, 2021]):
        dfvi = df[df["YEAR"] == year]
        # group by department
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
        dfvi_dpto.plot(
            x="DPTO", y=COLNAME, kind="bar", title=f"Intra-family, {year}", ax=ax[ii]
        )


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
