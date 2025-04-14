from census_API_wrapper import get_demo_data

def get_total_pop(year,geo):
    
    # set labels 
    labels = ['Estimate!!SEX AND AGE!!Total population']
    if year == '2009':
        labels = ['Number!!Estimate!!SEX AND AGE!!Total population']
   
    return get_demo_data('DP05',year,geo,labels)

def get_pop_sex(year,geo,as_percent=False):
    
    # set labels 
    if as_percent:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!SEX AND AGE!!Total population!!Male',
                      'Percent!!Estimate!!SEX AND AGE!!Total population!!Female']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!SEX AND AGE!!Male',
                      'Percent!!SEX AND AGE!!Female']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!SEX AND AGE!!Total population!!Male',
                      'Percent!!SEX AND AGE!!Total population!!Female']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!SEX AND AGE!!Total population!!Male',
                      'Percent Estimate!!SEX AND AGE!!Total population!!Female']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Number!!Estimate!!SEX AND AGE!!Total population!!Male',
                      'Number!!Estimate!!SEX AND AGE!!Total population!!Female']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!SEX AND AGE!!Male',
                      'Estimate!!SEX AND AGE!!Female']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!SEX AND AGE!!Total population!!Male',
                      'Estimate!!SEX AND AGE!!Total population!!Female']
        elif year in ['2017','2018']:
            labels = ['Estimate!!SEX AND AGE!!Total population!!Male',
                      'Estimate!!SEX AND AGE!!Total population!!Female']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    
    return get_demo_data('DP05',year,geo,labels)

def get_age(year,geo,as_percent=False):

    # set labels 
    if as_percent:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!SEX AND AGE!!Total population!!Under 5 years',
                      'Percent!!Estimate!!SEX AND AGE!!Total population!!5 to 9 years',
                      'Percent!!Estimate!!SEX AND AGE!!Total population!!10 to 14 years',
                      'Percent!!Estimate!!SEX AND AGE!!Total population!!15 to 19 years',
                      'Percent!!Estimate!!SEX AND AGE!!Total population!!20 to 24 years',
                      'Percent!!Estimate!!SEX AND AGE!!Total population!!25 to 34 years',
                      'Percent!!Estimate!!SEX AND AGE!!Total population!!35 to 44 years',
                      'Percent!!Estimate!!SEX AND AGE!!Total population!!45 to 54 years',
                      'Percent!!Estimate!!SEX AND AGE!!Total population!!55 to 59 years',
                      'Percent!!Estimate!!SEX AND AGE!!Total population!!60 to 64 years',
                      'Percent!!Estimate!!SEX AND AGE!!Total population!!65 to 74 years',
                      'Percent!!Estimate!!SEX AND AGE!!Total population!!75 to 84 years',
                      'Percent!!Estimate!!SEX AND AGE!!Total population!!85 years and over']
        elif year in ['2010','2011','2012','2013','2014','2015','2016']:
            labels = ['Percent!!SEX AND AGE!!Under 5 years',
                      'Percent!!SEX AND AGE!!5 to 9 years',
                      'Percent!!SEX AND AGE!!10 to 14 years',
                      'Percent!!SEX AND AGE!!15 to 19 years',
                      'Percent!!SEX AND AGE!!20 to 24 years',
                      'Percent!!SEX AND AGE!!25 to 34 years',
                      'Percent!!SEX AND AGE!!35 to 44 years',
                      'Percent!!SEX AND AGE!!45 to 54 years',
                      'Percent!!SEX AND AGE!!55 to 59 years',
                      'Percent!!SEX AND AGE!!60 to 64 years',
                      'Percent!!SEX AND AGE!!65 to 74 years',
                      'Percent!!SEX AND AGE!!75 to 84 years',
                      'Percent!!SEX AND AGE!!85 years and over']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!SEX AND AGE!!Total population!!Under 5 years',
                      'Percent Estimate!!SEX AND AGE!!Total population!!5 to 9 years',
                      'Percent Estimate!!SEX AND AGE!!Total population!!10 to 14 years',
                      'Percent Estimate!!SEX AND AGE!!Total population!!15 to 19 years',
                      'Percent Estimate!!SEX AND AGE!!Total population!!20 to 24 years',
                      'Percent Estimate!!SEX AND AGE!!Total population!!25 to 34 years',
                      'Percent Estimate!!SEX AND AGE!!Total population!!35 to 44 years',
                      'Percent Estimate!!SEX AND AGE!!Total population!!45 to 54 years',
                      'Percent Estimate!!SEX AND AGE!!Total population!!55 to 59 years',
                      'Percent Estimate!!SEX AND AGE!!Total population!!60 to 64 years',
                      'Percent Estimate!!SEX AND AGE!!Total population!!65 to 74 years',
                      'Percent Estimate!!SEX AND AGE!!Total population!!75 to 84 years',
                      'Percent Estimate!!SEX AND AGE!!Total population!!85 years and over']
        elif year in ['2019','2020','2021','2022','2023']:
            labels = ['Percent!!SEX AND AGE!!Total population!!Under 5 years',
                      'Percent!!SEX AND AGE!!Total population!!5 to 9 years',
                      'Percent!!SEX AND AGE!!Total population!!10 to 14 years',
                      'Percent!!SEX AND AGE!!Total population!!15 to 19 years',
                      'Percent!!SEX AND AGE!!Total population!!20 to 24 years',
                      'Percent!!SEX AND AGE!!Total population!!25 to 34 years',
                      'Percent!!SEX AND AGE!!Total population!!35 to 44 years',
                      'Percent!!SEX AND AGE!!Total population!!45 to 54 years',
                      'Percent!!SEX AND AGE!!Total population!!55 to 59 years',
                      'Percent!!SEX AND AGE!!Total population!!60 to 64 years',
                      'Percent!!SEX AND AGE!!Total population!!65 to 74 years',
                      'Percent!!SEX AND AGE!!Total population!!75 to 84 years',
                      'Percent!!SEX AND AGE!!Total population!!85 years and over']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Number!!Estimate!!SEX AND AGE!!Total population!!Under 5 years',
                      'Number!!Estimate!!SEX AND AGE!!Total population!!5 to 9 years',
                      'Number!!Estimate!!SEX AND AGE!!Total population!!10 to 14 years',
                      'Number!!Estimate!!SEX AND AGE!!Total population!!15 to 19 years',
                      'Number!!Estimate!!SEX AND AGE!!Total population!!20 to 24 years',
                      'Number!!Estimate!!SEX AND AGE!!Total population!!25 to 34 years',
                      'Number!!Estimate!!SEX AND AGE!!Total population!!35 to 44 years',
                      'Number!!Estimate!!SEX AND AGE!!Total population!!45 to 54 years',
                      'Number!!Estimate!!SEX AND AGE!!Total population!!55 to 59 years',
                      'Number!!Estimate!!SEX AND AGE!!Total population!!60 to 64 years',
                      'Number!!Estimate!!SEX AND AGE!!Total population!!65 to 74 years',
                      'Number!!Estimate!!SEX AND AGE!!Total population!!75 to 84 years',
                      'Number!!Estimate!!SEX AND AGE!!Total population!!85 years and over']
        elif year in ['2010','2011','2012','2013','2014','2015','2016']:
            labels = ['Estimate!!SEX AND AGE!!Under 5 years',
                      'Estimate!!SEX AND AGE!!5 to 9 years',
                      'Estimate!!SEX AND AGE!!10 to 14 years',
                      'Estimate!!SEX AND AGE!!15 to 19 years',
                      'Estimate!!SEX AND AGE!!20 to 24 years',
                      'Estimate!!SEX AND AGE!!25 to 34 years',
                      'Estimate!!SEX AND AGE!!35 to 44 years',
                      'Estimate!!SEX AND AGE!!45 to 54 years',
                      'Estimate!!SEX AND AGE!!55 to 59 years',
                      'Estimate!!SEX AND AGE!!60 to 64 years',
                      'Estimate!!SEX AND AGE!!65 to 74 years',
                      'Estimate!!SEX AND AGE!!75 to 84 years',
                      'Estimate!!SEX AND AGE!!85 years and over']
        elif year in ['2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!SEX AND AGE!!Total population!!Under 5 years',
                      'Estimate!!SEX AND AGE!!Total population!!5 to 9 years',
                      'Estimate!!SEX AND AGE!!Total population!!10 to 14 years',
                      'Estimate!!SEX AND AGE!!Total population!!15 to 19 years',
                      'Estimate!!SEX AND AGE!!Total population!!20 to 24 years',
                      'Estimate!!SEX AND AGE!!Total population!!25 to 34 years',
                      'Estimate!!SEX AND AGE!!Total population!!35 to 44 years',
                      'Estimate!!SEX AND AGE!!Total population!!45 to 54 years',
                      'Estimate!!SEX AND AGE!!Total population!!55 to 59 years',
                      'Estimate!!SEX AND AGE!!Total population!!60 to 64 years',
                      'Estimate!!SEX AND AGE!!Total population!!65 to 74 years',
                      'Estimate!!SEX AND AGE!!Total population!!75 to 84 years',
                      'Estimate!!SEX AND AGE!!Total population!!85 years and over']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    
    
    return get_demo_data('DP05',year,geo,labels)

def get_race(year,geo,as_percent=False):

    # set new labels 
    if as_percent:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!Race alone or in combination with one or more other races!!Total population!!White',
                      'Percent!!Estimate!!Race alone or in combination with one or more other races!!Total population!!Black or African American',
                      'Percent!!Estimate!!Race alone or in combination with one or more other races!!Total population!!American Indian and Alaska Native',
                      'Percent!!Estimate!!Race alone or in combination with one or more other races!!Total population!!Asian',
                      'Percent!!Estimate!!Race alone or in combination with one or more other races!!Total population!!Native Hawaiian and Other Pacific Islander',
                      'Percent!!Estimate!!Race alone or in combination with one or more other races!!Total population!!Some other race']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!RACE!!White',
                      'Percent!!RACE!!Black or African American',
                      'Percent!!RACE!!American Indian and Alaska Native',
                      'Percent!!RACE!!Asian',
                      'Percent!!RACE!!Native Hawaiian and Other Pacific Islander',
                      'Percent!!RACE!!Some other race']
        elif year in ['2013','2014','2015','2016']:
            labels = ['Percent!!RACE!!Race alone or in combination with one or more other races!!Total population!!White',
                      'Percent!!RACE!!Race alone or in combination with one or more other races!!Total population!!Black or African American',
                      'Percent!!RACE!!Race alone or in combination with one or more other races!!Total population!!American Indian and Alaska Native',
                      'Percent!!RACE!!Race alone or in combination with one or more other races!!Total population!!Asian',
                      'Percent!!RACE!!Race alone or in combination with one or more other races!!Total population!!Native Hawaiian and Other Pacific Islander',
                      'Percent!!RACE!!Race alone or in combination with one or more other races!!Total population!!Some other race']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!Race alone or in combination with one or more other races!!Total population!!White',
                      'Percent Estimate!!Race alone or in combination with one or more other races!!Total population!!Black or African American',
                      'Percent Estimate!!Race alone or in combination with one or more other races!!Total population!!American Indian and Alaska Native',
                      'Percent Estimate!!Race alone or in combination with one or more other races!!Total population!!Asian',
                      'Percent Estimate!!Race alone or in combination with one or more other races!!Total population!!Native Hawaiian and Other Pacific Islander',
                      'Percent Estimate!!Race alone or in combination with one or more other races!!Total population!!Some other race']
        elif year in ['2019','2020','2021','2022','2023']:
            labels = ['Percent!!Race alone or in combination with one or more other races!!Total population!!White',
                      'Percent!!Race alone or in combination with one or more other races!!Total population!!Black or African American',
                      'Percent!!Race alone or in combination with one or more other races!!Total population!!American Indian and Alaska Native',
                      'Percent!!Race alone or in combination with one or more other races!!Total population!!Asian',
                      'Percent!!Race alone or in combination with one or more other races!!Total population!!Native Hawaiian and Other Pacific Islander',
                      'Percent!!Race alone or in combination with one or more other races!!Total population!!Some other race']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Number!!Estimate!!Race alone or in combination with one or more other races!!Total population!!White',
                      'Number!!Estimate!!Race alone or in combination with one or more other races!!Total population!!Black or African American',
                      'Number!!Estimate!!Race alone or in combination with one or more other races!!Total population!!American Indian and Alaska Native',
                      'Number!!Estimate!!Race alone or in combination with one or more other races!!Total population!!Asian',
                      'Number!!Estimate!!Race alone or in combination with one or more other races!!Total population!!Native Hawaiian and Other Pacific Islander',
                      'Number!!Estimate!!Race alone or in combination with one or more other races!!Total population!!Some other race']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!RACE!!White',
                      'Estimate!!RACE!!Black or African American',
                      'Estimate!!RACE!!American Indian and Alaska Native',
                      'Estimate!!RACE!!Asian',
                      'Estimate!!RACE!!Native Hawaiian and Other Pacific Islander',
                      'Estimate!!RACE!!Some other race']
        elif year in ['2013','2014','2015','2016']:
            labels = ['Estimate!!RACE!!Race alone or in combination with one or more other races!!Total population!!White',
                      'Estimate!!RACE!!Race alone or in combination with one or more other races!!Total population!!Black or African American',
                      'Estimate!!RACE!!Race alone or in combination with one or more other races!!Total population!!American Indian and Alaska Native',
                      'Estimate!!RACE!!Race alone or in combination with one or more other races!!Total population!!Asian',
                      'Estimate!!RACE!!Race alone or in combination with one or more other races!!Total population!!Native Hawaiian and Other Pacific Islander',
                      'Estimate!!RACE!!Race alone or in combination with one or more other races!!Total population!!Some other race']
        elif year in ['2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!Race alone or in combination with one or more other races!!Total population!!White',
                      'Estimate!!Race alone or in combination with one or more other races!!Total population!!Black or African American',
                      'Estimate!!Race alone or in combination with one or more other races!!Total population!!American Indian and Alaska Native',
                      'Estimate!!Race alone or in combination with one or more other races!!Total population!!Asian',
                      'Estimate!!Race alone or in combination with one or more other races!!Total population!!Native Hawaiian and Other Pacific Islander',
                      'Estimate!!Race alone or in combination with one or more other races!!Total population!!Some other race']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    
    return get_demo_data('DP05',year,geo,labels)


#     # set variables from codebook 
#     variables = ['ucgid','DP02_0026PE','DP02_0027PE','DP02_0028PE',
#                  'DP02_0029PE','DP02_0030PE']
    
#     # set new labels 
#     labels = ['ucgid','Never married','Now married, except separated',
#               'Separated','Widowed','Divorced']
    
#     return get_demo_data('DP02',year,geo,variables,labels)

# def get_female_marital_status(year,geo):
    
#     # set variables from codebook 
#     variables = ['ucgid','DP02_0032PE','DP02_0033PE','DP02_0034PE',
#                  'DP02_0035PE','DP02_0036PE']
    
#     # set new labels 
#     labels = ['ucgid','Never married','Now married, except separated',
#               'Separated','Widowed','Divorced']
    
#     return get_demo_data('DP02',year,geo,variables,labels)

# def get_school_enrollment(year,geo):
    
#     # set variables from codebook 
#     variables = ['ucgid','DP02_0054PE','DP02_0055PE','DP02_0056PE',
#                  'DP02_0057PE','DP02_0058PE']
    
#     # set new labels 
#     labels = ['ucgid','Nursery school, preschool','Kindergarten',
#               'Elementary school (grades 1-8)',
#               'High school (grades 9-12)',
#               'College or graduate school']
    
#     return get_demo_data('DP02',year,geo,variables,labels)

# def get_education_level(year,geo):
    
#     # set variables from codebook 
#     variables = ['ucgid','DP02_0060PE','DP02_0061PE','DP02_0062PE',
#                  'DP02_0063PE','DP02_0064PE','DP02_0065PE','DP02_0066PE']
    
#     # set new labels 
#     labels = ['ucgid','Less than 9th grade','9th to 12th grade, no diploma',
#               'High school graduate (includes equivalency)',
#               'Some college, no degree','Associate\'s degree',
#               'Bachelor\'s degree','Graduate or professional degree']
    
#     return get_demo_data('DP02',year,geo,variables,labels)

# def get_veteran_status(year,geo):
    
#     # set variables from codebook 
#     variables = ['ucgid','DP02_0070PE']
    
#     # set new labels 
#     labels = ['ucgid','Civilian veterans']
    
#     return get_demo_data('DP02',year,geo,variables,labels)

# def get_disability_status(year,geo):
    
#     # set variables from codebook 
#     variables = ['ucgid','DP02_0072PE']
    
#     # set new labels 
#     labels = ['ucgid','With a disability (%)']
    
#     return get_demo_data('DP02',year,geo,variables,labels)

# def get_residence_year_ago(year,geo):
    
#     # set variables from codebook 
#     variables = ['ucgid','DP02_0079E','DP02_0080E','DP02_0083E','DP02_0085E',
#                  'DP02_0086E','DP02_0087E']
    
#     labels = ['ucgid',
#               'Population 1 year and over',
#               'Same house',
#               'Different house in the U.S., Same county',
#               'Different house in the U.S., Same state, Different county',
#               'Different house in the U.S., Different state',
#               'Abroad']

#     abs_data = get_demo_data('DP02',year,geo,variables,labels)

#     category_columns = abs_data.columns[2::]

#     perc_data = abs_data[category_columns].div(abs_data['Population 1 year and over'], axis=0)
#     perc_data = perc_data.multiply(100).round(1)

#     perc_data['ucgid'] = abs_data['ucgid']
    
#     return perc_data

# pop_data = get_total_pop('2009','state')
# pop_sex_data = get_pop_sex('2020', 'state',as_percent=True)
# pop_sex_data = get_pop_sex_percent('2009', 'county')
# age_data = get_age_percent('2015','state')
# race_data = get_race_percent('2015','state')

# household_type_data = get_household_type('2023', 'state',as_percent=False)
# household_data = get_household_relationships('2022', 'state')

# male_marital_data = get_male_marital_status('2020', 'state')
# enrollment_data = get_education_level('2020', 'state')
# veteran_data = get_veteran_status('2023', 'state')
# previous_residence_data = get_residence_year_ago('2023', 'state')