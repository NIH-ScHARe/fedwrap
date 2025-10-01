import requests 
import pandas as pd 
from .config import BRFSS_ENDPOINTS, Geography, Measure, Year, BreakOutCategory

def get_endpoint(geo: Geography | str, measure: Measure | str) -> str:
    """
    Get the appropriate BRFSS endpoint based on geography and measure.
    
    Args: 
        geo (Geography | str): Geography type, either 'state' or 'msa'.
        measure (Measure | str): Measure type, either 'crude' or 'age-adjusted'.
    Returns: 
        str: The corresponding BRFSS endpoint URL.
    """

    try:
        return BRFSS_ENDPOINTS[geo][measure]
    except KeyError:
        valid_geos = list(BRFSS_ENDPOINTS.keys())
        valid_measures = list(next(iter(BRFSS_ENDPOINTS.values())).keys())
        raise ValueError(
            f"Invalid combination: geo={geo}, measure={measure}. "
            f"Valid geos: {valid_geos}, valid measures: {valid_measures}"
        )

def check_question(question_id: str, year: Year) -> bool:
    """
    Check if a given question ID is valid for the specified year.
    
    Args:
        question_id (str): The question ID to validate.
        year (Year): The year to check the question against.
    Returns:
        bool: True if the question ID is valid for the year, False otherwise.
    """

    QUESTION_ENDPOINT = BRFSS_ENDPOINTS["questions"]

    # get all questions for the specified year 
    try:
        params = {"year": year}
        response = requests.get(QUESTION_ENDPOINT, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        questions = pd.DataFrame(response.json())
        return question_id in questions['variablename'].values
    except requests.RequestException as e:
        print(f"Error querying API: {e}")
        return False

def api_call(url: str, params: dict) -> pd.DataFrame | None: 

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return pd.DataFrame(response.json())
    except requests.RequestException as e:
        print(f"Error querying API: {e}")
        return None

def check_breakout(geo, measure, break_out_category) -> bool:
    """
    Validates the break_out_category based on the geo and measure.
    Args:
        geo (str): Geography type, either 'state' or 'msa'.
        measure (str): Measure type, either 'crude' or 'age-adjusted'.
        break_out_category (str): The break out category to validate.
    Returns:
        bool: True if the break_out_category is valid for the given geo and measure, False otherwise.
    """
    
    if not (geo == "state" and measure == "crude"):
        # For all other datasets, break_out_category MUST be Overall
        if break_out_category != "Overall":
            return False 
    return True 
            
def pivot_response_columns(df, break_out_category):
    """
    Takes the raw data response and consolidates response columns

    Args:
        df (pd.DataFrame): Raw data response from the API.
        break_out_category (str): The break out category used in the query.
    Returns:
        pd.DataFrame: Pivoted DataFrame with consolidated response columns.
    """

    # if there is a breakout category, pivot both on rponse and category 
    if break_out_category != "Overall":
        columns = ['break_out','response']
    else:
        columns = ['response']

    # force the data value column to numeric 
    df['data_value'] = pd.to_numeric(df['data_value'], errors="coerce")

    # pivot the table 
    wide = (
        df.pivot_table(
            index='locationabbr',
            columns=columns,
            values='data_value',
        )
        .sort_index()
        .sort_index(axis=1)
    )

    # flatten multiindex columns if necessary
    if isinstance(wide.columns, pd.MultiIndex):
        wide.columns = [f"{str(g)} - {str(r)}" for g, r in wide.columns.to_list()]

    # fill NaNs with 0s
    wide = wide.fillna(0)

    # reset index and clean up column names
    wide.columns.name = None
    wide = wide.reset_index().rename(columns={wide.index.name or "index": "locationabbr"})

    return wide

def get_brfss_data(
    geo: Geography | str,
    measure: Measure | str,
    year: Year, 
    question_id: str, 
    break_out_category: BreakOutCategory | str = 'Overall'
) -> pd.DataFrame | None:

    # 1. Check question_id validity 
    if not check_question(question_id, year):
        raise ValueError(f"Invalid question ID '{question_id}' for year {year}. Please check the question ID and try again.")

    # 2. Validate break_out_category rule
    if not check_breakout(geo, measure, break_out_category):
        raise ValueError(
                f"break_out_category can only be something other than 'Overall' "
                f"for the state crude dataset. You passed geo='{geo}', measure='{measure}', "
                f"break_out_category='{break_out_category}'."
            )

    # 3. Resolve endpoint 
    url = get_endpoint(geo, measure)

    # 4. Set params 
    params = {
            "year" : year,
            "questionid" : question_id,
            "break_out_category" : break_out_category
        }
    
    # 5. Make API call 
    raw_df = api_call(url, params)

    # 6. Pivot the table and return 
    return pivot_response_columns(raw_df, break_out_category)



