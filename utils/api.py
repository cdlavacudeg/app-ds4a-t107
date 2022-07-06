# This file contain all of the funtions that comunicate with the API
import requests as req
import pandas as pd
from dotenv import load_dotenv
import os

# Configure Enviroment varibles
load_dotenv()
baseUrl = os.getenv("API_BASE_URL")


def violenceApi(year):
    """
    Get all of the data of domestic violence in Colombia from 2016 to 2022
    """
    # Response of the api
    res = req.get(f"{baseUrl}/interfamily_violence", params={"year": year})
    # Convert the JSON response to a DataFrame and return it
    df = pd.DataFrame(res.json()["data"])
    return df


def suicideApi(year):
    """
    Get all of the data of suicides in Colombia from 2016 to 2022
    """
    res = req.get(f"{baseUrl}/suicides", params={"year": year})
    df = pd.DataFrame(res.json()["data"])
    return df


def suicidesAttempsApi(year):
    """
    Get all of the data of suicide attemps in Colombia from 2016 to 2022
    """
    res = req.get(f"{baseUrl}/suicide_attempts", params={"year": year})
    df = pd.DataFrame(res.json()["data"])
    return df
