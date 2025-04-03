import requests 
import pandas as pd

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

def get_demo_data(year,geo,variables,labels):
    
    # get url for API call 
    url = get_ACS_url(year,'DP05',geo)
    
    # get data from API request and format into dataframe 
    all_data = get_api_dataframe(url)

    # make a copy of the dataframe with selected variables 
    data = all_data[variables].copy()
    
    # set dataframe labels 
    data.columns = labels
    
    # convert to float values 
    data[data.columns[1:]] = data[data.columns[1:]].astype(float)
    
    return data

def get_age_percent(year,geo):

    # set variables from codebook 
    variables = ['ucgid','DP05_0005PE','DP05_0006PE','DP05_0007PE','DP05_0008PE',
                     'DP05_0009PE','DP05_0010PE','DP05_0011PE','DP05_0012PE',
                     'DP05_0013PE','DP05_0014PE','DP05_0015PE','DP05_0016PE',
                     'DP05_0017PE']
    
    # set new labels 
    labels = ['ucgid','under 5','5-9','10-14','15-19','20-24','25-34','35-44','45-54',
              '55-59','60-64','65-74','75-84','85+']
    
    return get_demo_data(year,geo,variables,labels)

def get_race_percent(year,geo):

    # set variables from codebook 
    variables = ['ucgid','DP05_0037PE','DP05_0038PE','DP05_0039PE',
                 'DP05_0044PE','DP05_0052PE','DP05_0057PE','DP05_0058PE']
    
    # set new labels 
    labels = ['ucgid','White','Black or African American',
              'American Indian and Alaska Native','Asian',
              'Native Hawaiian and Other Pacific Islander',
              'Some other race','Two or more races']
    
    return get_demo_data(year,geo,variables,labels)

age_data = get_age_percent('2023','state')
race_data = get_race_percent('2023','state')




