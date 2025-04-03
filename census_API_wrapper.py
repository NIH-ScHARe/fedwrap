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

def get_demo_data(table,year,geo,variables,labels):
    
    # get url for API call 
    url = get_ACS_url(year,table,geo)
    
    # get data from API request and format into dataframe 
    all_data = get_api_dataframe(url)

    # make a copy of the dataframe with selected variables 
    data = all_data[variables].copy()
    
    # set dataframe labels 
    data.columns = labels
    
    # convert to float values 
    data[data.columns[1:]] = data[data.columns[1:]].astype(float)
    
    return data

def get_total_pop(year,geo):
    
    # set variables from codebook 
    variables = ['ucgid','DP05_0001E']
    
    # set new labels 
    labels = ['ucgid','Total population']
    
    return get_demo_data('DP05',year,geo,variables,labels)

def get_pop_sex_percent(year,geo):
    
    # set variables from codebook 
    variables = ['ucgid','DP05_0002PE','DP05_0003PE']
    
    # set new labels 
    labels = ['ucgid','Male','Female']
    
    return get_demo_data('DP05',year,geo,variables,labels)

def get_age_percent(year,geo):

    # set variables from codebook 
    variables = ['ucgid','DP05_0005PE','DP05_0006PE','DP05_0007PE','DP05_0008PE',
                     'DP05_0009PE','DP05_0010PE','DP05_0011PE','DP05_0012PE',
                     'DP05_0013PE','DP05_0014PE','DP05_0015PE','DP05_0016PE',
                     'DP05_0017PE']
    
    # set new labels 
    labels = ['ucgid','under 5','5-9','10-14','15-19','20-24','25-34','35-44','45-54',
              '55-59','60-64','65-74','75-84','85+']
    
    return get_demo_data('DP05',year,geo,variables,labels)

def get_race_percent(year,geo):

    # set variables from codebook 
    variables = ['ucgid','DP05_0037PE','DP05_0038PE','DP05_0039PE',
                 'DP05_0044PE','DP05_0052PE','DP05_0057PE','DP05_0058PE']
    
    # set new labels 
    labels = ['ucgid','White','Black or African American',
              'American Indian and Alaska Native','Asian',
              'Native Hawaiian and Other Pacific Islander',
              'Some other race','Two or more races']
    
    return get_demo_data('DP05',year,geo,variables,labels)

def get_household_type(year,geo):
    
    # set variables from codebook 
    variables = ['ucgid','DP02_0002PE','DP02_0004PE','DP02_0006PE',
                 'DP02_0010PE']
    
    # set new labels 
    labels = ['ucgid','Married-couple household',
              'Cohabiting couple household',
              'Male householder, no spouse/partner present',
              'Female householder, no spouse/partner present']
    
    return get_demo_data('DP02',year,geo,variables,labels)

def get_household_relationships(year,geo):
    
    # set variables from codebook 
    variables = ['ucgid','DP02_0019PE','DP02_0020PE','DP02_0021PE',
                 'DP02_0022PE','DP02_0023PE','DP02_0024PE']
    
    # set new labels 
    labels = ['ucgid','Householder','Spouse','Unmarried partner','Child',
              'Other relatives','Other nonrelatives']
    
    return get_demo_data('DP02',year,geo,variables,labels)

def get_male_marital_status(year,geo):
    
    # set variables from codebook 
    variables = ['ucgid','DP02_0026PE','DP02_0027PE','DP02_0028PE',
                 'DP02_0029PE','DP02_0030PE']
    
    # set new labels 
    labels = ['ucgid','Never married','Now married, except separated',
              'Separated','Widowed','Divorced']
    
    return get_demo_data('DP02',year,geo,variables,labels)

def get_female_marital_status(year,geo):
    
    # set variables from codebook 
    variables = ['ucgid','DP02_0032PE','DP02_0033PE','DP02_0034PE',
                 'DP02_0035PE','DP02_0036PE']
    
    # set new labels 
    labels = ['ucgid','Never married','Now married, except separated',
              'Separated','Widowed','Divorced']
    
    return get_demo_data('DP02',year,geo,variables,labels)

def get_school_enrollment(year,geo):
    
    # set variables from codebook 
    variables = ['ucgid','DP02_0054PE','DP02_0055PE','DP02_0056PE',
                 'DP02_0057PE','DP02_0058PE']
    
    # set new labels 
    labels = ['ucgid','Nursery school, preschool','Kindergarten',
              'Elementary school (grades 1-8)',
              'High school (grades 9-12)',
              'College or graduate school']
    
    return get_demo_data('DP02',year,geo,variables,labels)

def get_education_level(year,geo):
    
    # set variables from codebook 
    variables = ['ucgid','DP02_0060PE','DP02_0061PE','DP02_0062PE',
                 'DP02_0063PE','DP02_0064PE','DP02_0065PE','DP02_0066PE']
    
    # set new labels 
    labels = ['ucgid','Less than 9th grade','9th to 12th grade, no diploma',
              'High school graduate (includes equivalency)',
              'Some college, no degree','Associate\'s degree',
              'Bachelor\'s degree','Graduate or professional degree']
    
    return get_demo_data('DP02',year,geo,variables,labels)

def get_veteran_status(year,geo):
    
    # set variables from codebook 
    variables = ['ucgid','DP02_0070PE']
    
    # set new labels 
    labels = ['ucgid','Civilian veterans']
    
    return get_demo_data('DP02',year,geo,variables,labels)

def get_disability_status(year,geo):
    
    # set variables from codebook 
    variables = ['ucgid','DP02_0072PE']
    
    # set new labels 
    labels = ['ucgid','With a disability (%)']
    
    return get_demo_data('DP02',year,geo,variables,labels)

def get_residence_year_ago(year,geo):
    
    # set variables from codebook 
    variables = ['ucgid','DP02_0079E','DP02_0080E','DP02_0083E','DP02_0085E',
                 'DP02_0086E','DP02_0087E']
    
    labels = ['ucgid',
              'Population 1 year and over',
              'Same house',
              'Different house in the U.S., Same county',
              'Different house in the U.S., Same state, Different county',
              'Different house in the U.S., Different state',
              'Abroad']

    abs_data = get_demo_data('DP02',year,geo,variables,labels)

    category_columns = abs_data.columns[2::]

    perc_data = abs_data[category_columns].div(abs_data['Population 1 year and over'], axis=0)
    perc_data = perc_data.multiply(100).round(1)

    perc_data['ucgid'] = abs_data['ucgid']
    
    return perc_data

# pop_data = get_total_pop('2022','county')
# age_data = get_age_percent('2023','state')
# race_data = get_race_percent('2023','state')

# household_data = get_household_relationships('2022', 'state')

# male_marital_data = get_male_marital_status('2020', 'state')
# enrollment_data = get_education_level('2020', 'state')
# veteran_data = get_veteran_status('2023', 'state')
previous_residence_data = get_residence_year_ago('2023', 'state')