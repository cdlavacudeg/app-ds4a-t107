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


def listDepartments():
    """
    Get all the departments of Colombia
    """
    res = req.get(f"{baseUrl}/departments")
    array = res.json()["data"]  # [{"code": int , "name": string}]
    options = [
        {"label": x["name"], "value": x["code"]} for x in array
    ]  # [{"label":string; "value":int}]
    return options


def listMunicipalities(deparment_id):
    """
    Get all the municipalities of a especific deparment
    """
    res = req.get(f"{baseUrl}/municipalities", params={"department_id": deparment_id})
    array = res.json()[
        "data"
    ]  # [{"code": int , "name": string, "lat": float, "lon":float}]
    options = [{"label": x["name"], "value": x["code"]} for x in array]
    return options


def modelExecute(
    department,
    municipality,
    gender,
    age_group,
    cause,
    marital_status,
    scolarship,
    vulnerability_factor
):
    data = {
        "department": department,
        "municipality": municipality,
        "gender": gender,
        "age_group": age_group,
        "cause": cause,
        "marital_status": marital_status,
        "scolarship": scolarship,
        "vulnerability_factor": vulnerability_factor,
    }
    postData={}
    for key in data:
        if data[key] != None:
            postData[key] = data[key]
    

    res = req.post(
        "https://ei6jgctli3.execute-api.us-east-1.amazonaws.com/predict/", json=data
    )
    return res.json()["global"]
