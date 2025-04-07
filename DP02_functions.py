from census_API_wrapper import get_demo_data

def get_household_type(year,geo,as_percent=False):
    
    # set labels 
    if as_percent:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Married-couple family',
                      'Percent!!Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Male householder, no wife present, family',
                      'Percent!!Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Female householder, no husband present, family',
                      'Percent!!Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!HOUSEHOLDS BY TYPE!!Family households (families)!!Married-couple family',
                      'Percent!!HOUSEHOLDS BY TYPE!!Family households (families)!!Male householder, no wife present, family',
                      'Percent!!HOUSEHOLDS BY TYPE!!Family households (families)!!Female householder, no husband present, family',
                      'Percent!!HOUSEHOLDS BY TYPE!!Nonfamily households']
        elif year in ['2013','2014','2015','2016','2017','2018']:
            labels = ['Percent!!HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!Married-couple family',
                      'Percent!!HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!Male householder, no wife present, family',
                      'Percent!!HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!Female householder, no husband present, family',
                      'Percent!!HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households']
        elif year in ['2019']:
            labels = ['Percent!!HOUSEHOLDS BY TYPE!!Total households!!Married-couple family',
                      'Percent!!HOUSEHOLDS BY TYPE!!Total households!!Cohabiting couple household',
                      'Percent!!HOUSEHOLDS BY TYPE!!Total households!!Male householder, no spouse/partner present',
                      'Percent!!HOUSEHOLDS BY TYPE!!Total households!!Female householder, no spouse/partner present']
        elif year in ['2020','2021','2022','2023']:
            labels = ['Percent!!HOUSEHOLDS BY TYPE!!Total households!!Married-couple household',
                      'Percent!!HOUSEHOLDS BY TYPE!!Total households!!Cohabiting couple household',
                      'Percent!!HOUSEHOLDS BY TYPE!!Total households!!Male householder, no spouse/partner present',
                      'Percent!!HOUSEHOLDS BY TYPE!!Total households!!Female householder, no spouse/partner present']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Number!!Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Married-couple family',
                      'Number!!Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Male householder, no wife present, family',
                      'Number!!Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Female householder, no husband present, family',
                      'Number!!Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!HOUSEHOLDS BY TYPE!!Family households (families)!!Married-couple family',
                      'Estimate!!HOUSEHOLDS BY TYPE!!Family households (families)!!Male householder, no wife present, family',
                      'Estimate!!HOUSEHOLDS BY TYPE!!Family households (families)!!Female householder, no husband present, family',
                      'Estimate!!HOUSEHOLDS BY TYPE!!Nonfamily households']
        elif year in ['2013','2014','2015','2016','2017','2018']:
            labels = ['Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!Married-couple family',
                      'Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!Male householder, no wife present, family',
                      'Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!Female householder, no husband present, family',
                      'Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households']
        elif year in ['2019']:
            labels = ['Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Married-couple family',
                      'Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Cohabiting couple household',
                      'Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Male householder, no spouse/partner present',
                      'Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Female householder, no spouse/partner present']
        elif year in ['2020','2021','2022','2023']:
            labels = ['Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Married-couple household',
                      'Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Cohabiting couple household',
                      'Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Male householder, no spouse/partner present',
                      'Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Female householder, no spouse/partner present']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    
    return get_demo_data('DP02',year,geo,labels)



def get_household_relationship(year,geo,as_percent=False):
    
    if as_percent:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!RELATIONSHIP!!Population in households!!Householder',
                      'Percent!!Estimate!!RELATIONSHIP!!Population in households!!Spouse',
                      'Percent!!Estimate!!RELATIONSHIP!!Population in households!!Child',
                      'Percent!!Estimate!!RELATIONSHIP!!Population in households!!Other relatives',
                      'Percent!!Estimate!!RELATIONSHIP!!Population in households!!Nonrelatives',
                      'Percent!!Estimate!!RELATIONSHIP!!Population in households!!Nonrelatives!!Unmarried partner']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!RELATIONSHIP!!Householder',
                      'Percent!!RELATIONSHIP!!Spouse',
                      'Percent!!RELATIONSHIP!!Child',
                      'Percent!!RELATIONSHIP!!Other relatives',
                      'Percent!!RELATIONSHIP!!Nonrelatives',
                      'Percent!!RELATIONSHIP!!Nonrelatives!!Unmarried partner']
        elif year in ['2013','2014','2015','2016','2017','2018']:
            labels = ['Percent!!RELATIONSHIP!!Population in households!!Householder',
                      'Percent!!RELATIONSHIP!!Population in households!!Spouse',
                      'Percent!!RELATIONSHIP!!Population in households!!Child',
                      'Percent!!RELATIONSHIP!!Population in households!!Other relatives',
                      'Percent!!RELATIONSHIP!!Population in households!!Nonrelatives',
                      'Percent!!RELATIONSHIP!!Population in households!!Nonrelatives!!Unmarried partner']
        elif year in ['2019','2020','2021','2022','2023']:
            labels = ['Percent!!RELATIONSHIP!!Population in households!!Householder',
                      'Percent!!RELATIONSHIP!!Population in households!!Spouse',
                      'Percent!!RELATIONSHIP!!Population in households!!Unmarried partner',
                      'Percent!!RELATIONSHIP!!Population in households!!Child',
                      'Percent!!RELATIONSHIP!!Population in households!!Other relatives',
                      'Percent!!RELATIONSHIP!!Population in households!!Other nonrelatives']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Number!!Estimate!!RELATIONSHIP!!Population in households!!Householder',
                      'Number!!Estimate!!RELATIONSHIP!!Population in households!!Spouse',
                      'Number!!Estimate!!RELATIONSHIP!!Population in households!!Child',
                      'Number!!Estimate!!RELATIONSHIP!!Population in households!!Other relatives',
                      'Number!!Estimate!!RELATIONSHIP!!Population in households!!Nonrelatives',
                      'Number!!Estimate!!RELATIONSHIP!!Population in households!!Nonrelatives!!Unmarried partner']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!RELATIONSHIP!!Householder',
                      'Estimate!!RELATIONSHIP!!Spouse',
                      'Estimate!!RELATIONSHIP!!Child',
                      'Estimate!!RELATIONSHIP!!Other relatives',
                      'Estimate!!RELATIONSHIP!!Nonrelatives',
                      'Estimate!!RELATIONSHIP!!Nonrelatives!!Unmarried partner']
        elif year in ['2013','2014','2015','2016','2017','2018']:
            labels = ['Estimate!!RELATIONSHIP!!Population in households!!Householder',
                      'Estimate!!RELATIONSHIP!!Population in households!!Spouse',
                      'Estimate!!RELATIONSHIP!!Population in households!!Child',
                      'Estimate!!RELATIONSHIP!!Population in households!!Other relatives',
                      'Estimate!!RELATIONSHIP!!Population in households!!Nonrelatives',
                      'Estimate!!RELATIONSHIP!!Population in households!!Nonrelatives!!Unmarried partner']
        elif year in ['2019','2020','2021','2022','2023']:
            labels = ['Estimate!!RELATIONSHIP!!Population in households!!Householder',
                      'Estimate!!RELATIONSHIP!!Population in households!!Spouse',
                      'Estimate!!RELATIONSHIP!!Population in households!!Unmarried partner',
                      'Estimate!!RELATIONSHIP!!Population in households!!Child',
                      'Estimate!!RELATIONSHIP!!Population in households!!Other relatives',
                      'Estimate!!RELATIONSHIP!!Population in households!!Other nonrelatives']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    
    data = get_demo_data('DP02',year,geo,labels)
    
    # for years 2009 - 2018, break out unmarried partner from nonrelatives 
    if int(year) < 2019:
        data['Other nonrelatives'] = data['Nonrelatives'] - data['Unmarried partner']
        data = data.drop(columns='Nonrelatives')
    
    return data



def get_male_marital_status(year,geo,as_percent=False):
    
    # set labels 
    if as_percent:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!MARITAL STATUS!!Males 15 years and over!!Never married',
                      'Percent!!Estimate!!MARITAL STATUS!!Males 15 years and over!!Now married, except separated',
                      'Percent!!Estimate!!MARITAL STATUS!!Males 15 years and over!!Separated',
                      'Percent!!Estimate!!MARITAL STATUS!!Males 15 years and over!!Widowed',
                      'Percent!!Estimate!!MARITAL STATUS!!Males 15 years and over!!Divorced']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!MARITAL STATUS!!Never married',
                      'Percent!!MARITAL STATUS!!Now married, except separated',
                      'Percent!!MARITAL STATUS!!Separated',
                      'Percent!!MARITAL STATUS!!Widowed',
                      'Percent!!MARITAL STATUS!!Divorced']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!MARITAL STATUS!!Males 15 years and over!!Never married',
                      'Percent!!MARITAL STATUS!!Males 15 years and over!!Now married, except separated',
                      'Percent!!MARITAL STATUS!!Males 15 years and over!!Separated',
                      'Percent!!MARITAL STATUS!!Males 15 years and over!!Widowed',
                      'Percent!!MARITAL STATUS!!Males 15 years and over!!Divorced']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!MARITAL STATUS!!Males 15 years and over!!Never married',
                      'Percent Estimate!!MARITAL STATUS!!Males 15 years and over!!Now married, except separated',
                      'Percent Estimate!!MARITAL STATUS!!Males 15 years and over!!Separated',
                      'Percent Estimate!!MARITAL STATUS!!Males 15 years and over!!Widowed',
                      'Percent Estimate!!MARITAL STATUS!!Males 15 years and over!!Divorced']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Number!!Estimate!!MARITAL STATUS!!Males 15 years and over!!Never married',
                      'Number!!Estimate!!MARITAL STATUS!!Males 15 years and over!!Now married, except separated',
                      'Number!!Estimate!!MARITAL STATUS!!Males 15 years and over!!Separated',
                      'Number!!Estimate!!MARITAL STATUS!!Males 15 years and over!!Widowed',
                      'Number!!Estimate!!MARITAL STATUS!!Males 15 years and over!!Divorced']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!MARITAL STATUS!!Never married',
                      'Estimate!!MARITAL STATUS!!Now married, except separated',
                      'Estimate!!MARITAL STATUS!!Separated',
                      'Estimate!!MARITAL STATUS!!Widowed',
                      'Estimate!!MARITAL STATUS!!Divorced']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!MARITAL STATUS!!Males 15 years and over!!Never married',
                      'Estimate!!MARITAL STATUS!!Males 15 years and over!!Now married, except separated',
                      'Estimate!!MARITAL STATUS!!Males 15 years and over!!Separated',
                      'Estimate!!MARITAL STATUS!!Males 15 years and over!!Widowed',
                      'Estimate!!MARITAL STATUS!!Males 15 years and over!!Divorced']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
            
    return get_demo_data('DP02',year,geo,labels)

def get_female_marital_status(year,geo,as_percent=False,return_index=0):
    
    # set labels 
    if as_percent:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!MARITAL STATUS!!Females 15 years and over!!Never married',
                      'Percent!!Estimate!!MARITAL STATUS!!Females 15 years and over!!Now married, except separated',
                      'Percent!!Estimate!!MARITAL STATUS!!Females 15 years and over!!Separated',
                      'Percent!!Estimate!!MARITAL STATUS!!Females 15 years and over!!Widowed',
                      'Percent!!Estimate!!MARITAL STATUS!!Females 15 years and over!!Divorced']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!MARITAL STATUS!!Never married',
                      'Percent!!MARITAL STATUS!!Now married, except separated',
                      'Percent!!MARITAL STATUS!!Separated',
                      'Percent!!MARITAL STATUS!!Widowed',
                      'Percent!!MARITAL STATUS!!Divorced']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!MARITAL STATUS!!Females 15 years and over!!Never married',
                      'Percent!!MARITAL STATUS!!Females 15 years and over!!Now married, except separated',
                      'Percent!!MARITAL STATUS!!Females 15 years and over!!Separated',
                      'Percent!!MARITAL STATUS!!Females 15 years and over!!Widowed',
                      'Percent!!MARITAL STATUS!!Females 15 years and over!!Divorced']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!MARITAL STATUS!!Females 15 years and over!!Never married',
                      'Percent Estimate!!MARITAL STATUS!!Females 15 years and over!!Now married, except separated',
                      'Percent Estimate!!MARITAL STATUS!!Females 15 years and over!!Separated',
                      'Percent Estimate!!MARITAL STATUS!!Females 15 years and over!!Widowed',
                      'Percent Estimate!!MARITAL STATUS!!Females 15 years and over!!Divorced']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Number!!Estimate!!MARITAL STATUS!!Females 15 years and over!!Never married',
                      'Number!!Estimate!!MARITAL STATUS!!Females 15 years and over!!Now married, except separated',
                      'Number!!Estimate!!MARITAL STATUS!!Females 15 years and over!!Separated',
                      'Number!!Estimate!!MARITAL STATUS!!Females 15 years and over!!Widowed',
                      'Number!!Estimate!!MARITAL STATUS!!Females 15 years and over!!Divorced']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!MARITAL STATUS!!Never married',
                      'Estimate!!MARITAL STATUS!!Now married, except separated',
                      'Estimate!!MARITAL STATUS!!Separated',
                      'Estimate!!MARITAL STATUS!!Widowed',
                      'Estimate!!MARITAL STATUS!!Divorced']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!MARITAL STATUS!!Females 15 years and over!!Never married',
                      'Estimate!!MARITAL STATUS!!Females 15 years and over!!Now married, except separated',
                      'Estimate!!MARITAL STATUS!!Females 15 years and over!!Separated',
                      'Estimate!!MARITAL STATUS!!Females 15 years and over!!Widowed',
                      'Estimate!!MARITAL STATUS!!Females 15 years and over!!Divorced']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    
    # correct for years with multiple labels 
    if year in ['2010','2011','2012']:
        return_index = 1
    
    return get_demo_data('DP02',year,geo,labels,return_index)


female_marital_data = get_female_marital_status('2020', 'state',as_percent=True)
