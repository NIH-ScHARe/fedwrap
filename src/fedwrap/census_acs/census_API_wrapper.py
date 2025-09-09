import requests 
import pandas as pd
from bs4 import BeautifulSoup

# ===================================
# Helper Functions
# ===================================

def get_variable_name(table,label,return_index=0):
    
    """
    Retrieve the variable family name corresponding to a given label from the ACS metadata table.

    Parameters:
        table (pd.DataFrame): A DataFrame containing ACS metadata, with at least 'Label' and 'Name' columns.
        label (str): The descriptive label to search for in the 'Label' column.

    Returns:
        str or None: The corresponding variable name from the 'Name' column if the label is found;
                     otherwise, returns None.
    """
    
    match = table.loc[table['Label'] == label, 'Name']
    
    # return none if no match 
    if match.empty:
        return None

    # if length is longer than 1, return with return index, otherwise return 0
    return match.iloc[return_index if len(match) > 1 else 0]
    
    
def extract_label_name(labels):
    
    """
    Extract short label names from a list of detailed label strings.

    This function parses a list of label strings from ACS metadata
    and extracts the most specific descriptor from each by splitting on '!!'.
    It also prepends 'ucgid' to the list, which refers to a geographic identifier.

    Parameters:
        labels (list of str): A list of detailed label strings using '!!' as a delimiter.

    Returns:
        list of str: A new list of short label names with 'ucgid' as the first element.
    """
    
    short_labels = ['ucgid']
    for label in labels:
        short_labels.append(label.split('!!')[-1])
    
    return short_labels

# ===================================
# Utility Functions
# ===================================

def get_ACS_metadata(year,table):
    
    # define URL
    url = 'https://api.census.gov/data/' + year + '/acs/acs5/profile/groups/' + table + '.html'

    # Fetch HTML content 
    response = requests.get(url)

    # Parse HTML 
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table 
    table = soup.find("table")

    # Extract headers 
    headers = [th.text.strip() for th in table.find_all("th")]

    # Extract rows
    rows = []
    for tr in table.find_all("tr")[2:]:  # Skip header and variable number rows
        cells = [td.text.strip() for td in tr.find_all("td")]
        rows.append(cells)

    # Return DataFrame
    return pd.DataFrame(rows, columns=headers)

def get_variables(table, year, labels, return_index=0):
    
    # get metadata table 
    variable_table = get_ACS_metadata(year,table)
    
    # iterate through each label and return variable name from table 
    variables = []
    for label in labels:
        variables.append(get_variable_name(variable_table, label,return_index))
    
    # return list of variable names 
    return variables 

def get_api_dataframe(url):
    
    table = requests.get(url)
    
    df = pd.DataFrame(table.json())
    
    df.columns = df.iloc[0]
    df = df[1:].reset_index(drop=True)

    return df

def get_ACS_url(year,table,geo):
    
    geo_pseudo_map = {
        'country': 'pseudo(0100000US$000)',
        'state': 'pseudo(0100000US$0400000)',
        'county': 'pseudo(0100000US$0500000)',
        'census tract': 'pseudo(0100000US$1400000)',
        'zip code': 'pseudo(0100000US$8600000)',
        'congressional district': 'pseudo(0100000US$5000000)',
        'MSA': 'pseudo(0100000US$31000M1)'
    }
    
    return 'https://api.census.gov/data/' + year + '/acs/acs5/profile?get=group(' + table + ')&ucgid=' + geo_pseudo_map.get(geo) 

# ===================================
# Public API Functions
# ===================================

def get_demo_data(table,year,geo,labels,return_index=0):
    
    # get url for API call 
    url = get_ACS_url(year,table,geo)
    
    # get data from API request and format into dataframe 
    all_data = get_api_dataframe(url)

    # get variable names based on labels  
    variables = get_variables(table,year,labels,return_index)

    # append ucgid code 
    variables.insert(0,'ucgid')

    # make a copy of the dataframe with selected variables 
    data = all_data[variables].copy()
    
    # set dataframe labels 
    data.columns = extract_label_name(labels)
    
    # convert to float values 
    data[data.columns[1:]] = data[data.columns[1:]].astype(float)
    
    return data
