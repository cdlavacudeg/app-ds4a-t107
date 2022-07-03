import requests as req
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

baseUrl=os.getenv('API_BASE_URL')

def violenceApi(year):
    res=req.get(f'{baseUrl}/interfamily_violence',params={'year':year})
    df = pd.DataFrame(res.json()['data'])
    return df
            
def suicideApi(year):
    res=req.get(f'{baseUrl}/suicides',params={'year':year})
    df=pd.DataFrame(res.json()['data'])
    return df

def suicidesAttempsApi(year):
    res=req.get(f'{baseUrl}/suicide_attempts',params={'year':year})
    df=pd.DataFrame(res.json()['data'])
    return df
