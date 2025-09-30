import requests 
import pandas as pd 
import json 

def fetch_api_key():
    # read in api key json file 
    with open("secrets/api_keys.json") as f: 
        secrets = json.load(f)
    
    return secrets["API_Key"]

def get_brfss_data(geo: str, year: int, question_id: str, break_out: str = 'Overall'):

    if geo == "state":
        url = "https://data.cdc.gov/resource/dttw-5yxu.json"
    else:
        url = "https://data.cdc.gov/resource/j32a-sa6u.json"

    try:
        
        params = {
            "year" : year,
            "questionid" : question_id,
            "break_out" : break_out
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return pd.DataFrame(response.json())
    except requests.RequestException as e:
        print(f"Error querying API: {e}")
        return None

data = get_brfss_data("MMSA", 2023, "ADDEPEV3")

data.to_csv("src/fedwrap/cdc_brfss/query_result.csv",index=False)

