import requests 
from .config import API_ENDPOINTS, DATA_DICTIONARY_ENDPOINT, Year, Geography, MeasureType, MeasureID
import pandas as pd
from fedwrap.census_acs import get_acs_data 

def query_api(url, params=None):
    """
    Queries the CDC Places API with the given URL and parameters.

    Args:
        url (str): The API endpoint URL.
        params (dict, optional): A dictionary of query parameters to include in the request.

    Returns:
        dict: The JSON response from the API if the request is successful.
        None: If the request fails or an error occurs.
    """
    try:
        # Ensure params is a dict and set the $limit parameter to 100000
        if params is None:
            params = {}
        params["$limit"] = 100000
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return pd.DataFrame(response.json())
    except requests.RequestException as e:
        print(f"Error querying API: {e}")
        return None


def get_release_for_year(
        measureid: MeasureID, 
        year: Year
    ):
    """
    Looks up the name of the data release for a given measure ID and year.
    
    Args:
        measureid (str): The measure ID to look up.
        year (int): The desired year of data.
    
    Returns:
        str: The name of the data release for the specified measure ID and year.
    """

    # get the data dictionary 
    response = requests.get(DATA_DICTIONARY_ENDPOINT)

    # convert the response to a pandas dataframe
    dataDict = pd.DataFrame(response.json())

    # get the row matching the measureid
    if measureid not in dataDict['measureid'].values:
        print(f"Measure ID {measureid} not found in the data dictionary.")
        return None
    row = dataDict[dataDict['measureid'] == measureid]

    # return the column name that matches the year
    if row.empty:
        print(f"No data found for measure ID: {measureid}")
        return None
    return row.columns[(row == str(year)).iloc[0]].tolist()[0]

def get_endpoint_for_geo(
        geo: Geography | str, 
        release_name: str
    ) -> str | None:
    """
    Retrieves the API endpoint for a given geographic level and data release name.

    Args:
        geo (str): The geographic level (e.g., 'county', 'census', 'zcta', 'places').
        release_name (str): The name of the data release (e.g., 'places_release_2024').

    Returns:
        str: The API endpoint URL for the specified geographic level and data release.
    """
    if geo not in API_ENDPOINTS:
        print(f"Geographic level '{geo}' is not supported.")
        return None
    if release_name not in API_ENDPOINTS[geo]:
        print(f"Data release '{release_name}' is not available for geographic level '{geo}'.")
        return None
    return API_ENDPOINTS[geo][release_name]

def set_query_params(
        geo: Geography | str, 
        year: Year, 
        measureid: MeasureID | str=None, 
        datavaluetypeid: MeasureType | str=None
    ) -> tuple[str, dict]:
    
    # get the API endpoint for the specified geographic level and year
    url = get_endpoint_for_geo(geo, get_release_for_year(measureid, year))

    # initialize an empty dictionary for parameters
    params = {}
    if measureid:
        params["measureid"] = measureid
    if datavaluetypeid:
        params["datavaluetypeid"] = datavaluetypeid

    return url, params

def get_places_state_data(
        year: Year,
        measureid: MeasureID | str,
        datavaluetypid: MeasureType | str ="CrdPrv"
    ):

    # get county level data for requested measure
    county_data = get_places_data('county',year,measureid,datavaluetypid)
    county_data['data_value'] = county_data['data_value'].astype('float64')

    # get population data for each county 
    population_data = get_acs_data('TOTAL_POP',year,'county')
    
    # rename FIPS column 
    population_data['ucgid'] = population_data['ucgid'].astype(str).str[-5:]
    population_data = population_data.rename(columns={'ucgid':'locationid'})

    # merge on the FIPS code 
    county_data = county_data.merge(population_data,on='locationid',how='left')

    # compute the population-weighted prevalance 
    county_data['weighted_p'] = county_data['data_value'] * county_data['Total population'] / 100

    # compute the sum of weighted_p and total population across all counties in each state 
    state_summary = county_data.groupby('stateabbr')[['weighted_p', 'Total population']].sum().reset_index()
    
    # compute the statewide prevalance by dividing the weighted prevalance by the total population 
    state_summary['data_value'] = (state_summary['weighted_p'] / state_summary['Total population'] * 100).round(1)
    
    # drop the us row 
    state_summary = state_summary[state_summary['stateabbr'] != 'US']

    return state_summary[['stateabbr','data_value']]


def get_places_data(
        geo: Geography | str, 
        year: Year, 
        measureid: MeasureID | str, 
        datavaluetypid: MeasureType | str ="CrdPrv"
    ) -> pd.DataFrame | None:

    # if state level is requested, compute state values from counties 
    if geo=='state':
        return get_places_state_data(year,measureid,datavaluetypid)
    
    # otherwise, call the corresponding geography 
    else:

        # construct the URL and parameters for the API query
        url, params = set_query_params(
            geo=geo,
            year=year,
            measureid=measureid,  
            datavaluetypeid=datavaluetypid  
        )

        # query the API with the constructed URL and parameters
        return query_api(url, params)
