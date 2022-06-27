import pandas as pd
import folium
import matplotlib.pyplot as plt
from folium.plugins import HeatMap

def map_trysuicides_per_year_population(year):
    df = pd.read_csv("data/violencia/MERGED-TrySuicidiosPopulationGeo.csv")
    # df.drop(columns=["CODE_DPTO", "CODE_MUNICIPIO"], inplace=True) # NOT NEED SINCE I AM KEEPING ONLY LAT AND LONG
    df = df[df["YEAR"] == year]
    # print(df.head())
    # Heat map for count of begin location
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
