import requests 
import pandas as pd
from bs4 import BeautifulSoup

def get_api_dataframe(url):
    
    table = requests.get(url)
    
    df = pd.DataFrame(table.json())
    
    df.columns = df.iloc[0]
    df = df[1:].reset_index(drop=True)

    return df

def get_ACS_url(year,table,geo):
    
    geo_pseudo_map = {
        'state': 'pseudo(0100000US$0400000)',
        'county': 'pseudo(0100000US$0500000)',
        'congressional district': 'pseudo(0100000US$5000000)'
    }
    
    return 'https://api.census.gov/data/' + year + '/acs/acs5/profile?get=group(' + table + ')&ucgid=' + geo_pseudo_map.get(geo) 

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

def get_variable_name(table,label):
    
    match = table.loc[table['Label'] == label, 'Name']
    return match.iloc[0] if not match.empty else None

def get_variables(table, year, labels):
    
    # get metadata table 
    variable_table = get_ACS_metadata(year,table)
    
    # iterate through each label and return variable name from table 
    variables = []
    for label in labels:
        variables.append(get_variable_name(variable_table, label))
    
    # return list of variable names 
    return variables 

def extract_label_name(labels):
    
    short_labels = ['ucgid']
    for label in labels:
        short_labels.append(label.split('!!')[-1])
    
    return short_labels

def get_demo_data(table,year,geo,labels):
    
    # get url for API call 
    url = get_ACS_url(year,table,geo)
    
    # get data from API request and format into dataframe 
    all_data = get_api_dataframe(url)

    # get variable names based on labels  
    variables = get_variables(table,year,labels)

    # append ucgid code 
    variables.insert(0,'ucgid')

    # make a copy of the dataframe with selected variables 
    data = all_data[variables].copy()
    
    # set dataframe labels 
    data.columns = extract_label_name(labels)
    
    # convert to float values 
    data[data.columns[1:]] = data[data.columns[1:]].astype(float)
    
    return data


