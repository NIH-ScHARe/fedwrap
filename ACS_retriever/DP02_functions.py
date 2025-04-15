from .census_API_wrapper import get_demo_data

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

def get_school_enrollment(year,geo,as_percent=False):
    
    # set labels 
    if as_percent:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!Nursery school, preschool',
                      'Percent!!Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!Kindergarten',
                      'Percent!!Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!Elementary school (grades 1-8)',
                      'Percent!!Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!High school (grades 9-12)',
                      'Percent!!Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!College or graduate school']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!SCHOOL ENROLLMENT!!Nursery school, preschool',
                      'Percent!!SCHOOL ENROLLMENT!!Kindergarten',
                      'Percent!!SCHOOL ENROLLMENT!!Elementary school (grades 1-8)',
                      'Percent!!SCHOOL ENROLLMENT!!High school (grades 9-12)',
                      'Percent!!SCHOOL ENROLLMENT!!College or graduate school']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!Nursery school, preschool',
                      'Percent!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!Kindergarten',
                      'Percent!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!Elementary school (grades 1-8)',
                      'Percent!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!High school (grades 9-12)',
                      'Percent!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!College or graduate school']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!Nursery school, preschool',
                      'Percent Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!Kindergarten',
                      'Percent Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!Elementary school (grades 1-8)',
                      'Percent Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!High school (grades 9-12)',
                      'Percent Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!College or graduate school']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Number!!Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!Nursery school, preschool',
                      'Number!!Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!Kindergarten',
                      'Number!!Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!Elementary school (grades 1-8)',
                      'Number!!Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!High school (grades 9-12)',
                      'Number!!Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!College or graduate school']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!SCHOOL ENROLLMENT!!Nursery school, preschool',
                      'Estimate!!SCHOOL ENROLLMENT!!Kindergarten',
                      'Estimate!!SCHOOL ENROLLMENT!!Elementary school (grades 1-8)',
                      'Estimate!!SCHOOL ENROLLMENT!!High school (grades 9-12)',
                      'Estimate!!SCHOOL ENROLLMENT!!College or graduate school']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!Nursery school, preschool',
                      'Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!Kindergarten',
                      'Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!Elementary school (grades 1-8)',
                      'Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!High school (grades 9-12)',
                      'Estimate!!SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!College or graduate school']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    
    
    return get_demo_data('DP02',year,geo,labels)

def get_educational_attainment(year,geo,as_percent=False):
    
    # set labels 
    if as_percent:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Less than 9th grade',
                      'Percent!!Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!9th to 12th grade, no diploma',
                      'Percent!!Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!High school graduate (includes equivalency)',
                      'Percent!!Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Some college, no degree',
                      'Percent!!Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Associate\'s degree',
                      'Percent!!Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Bachelor\'s degree',
                      'Percent!!Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Graduate or professional degree']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!EDUCATIONAL ATTAINMENT!!Less than 9th grade',
                      'Percent!!EDUCATIONAL ATTAINMENT!!9th to 12th grade, no diploma',
                      'Percent!!EDUCATIONAL ATTAINMENT!!High school graduate (includes equivalency)',
                      'Percent!!EDUCATIONAL ATTAINMENT!!Some college, no degree',
                      'Percent!!EDUCATIONAL ATTAINMENT!!Associate\'s degree',
                      'Percent!!EDUCATIONAL ATTAINMENT!!Bachelor\'s degree',
                      'Percent!!EDUCATIONAL ATTAINMENT!!Graduate or professional degree']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Less than 9th grade',
                      'Percent!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!9th to 12th grade, no diploma',
                      'Percent!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!High school graduate (includes equivalency)',
                      'Percent!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Some college, no degree',
                      'Percent!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Associate\'s degree',
                      'Percent!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Bachelor\'s degree',
                      'Percent!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Graduate or professional degree']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Less than 9th grade',
                      'Percent Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!9th to 12th grade, no diploma',
                      'Percent Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!High school graduate (includes equivalency)',
                      'Percent Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Some college, no degree',
                      'Percent Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Associate\'s degree',
                      'Percent Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Bachelor\'s degree',
                      'Percent Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Graduate or professional degree']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Number!!Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Less than 9th grade',
                      'Number!!Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!9th to 12th grade, no diploma',
                      'Number!!Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!High school graduate (includes equivalency)',
                      'Number!!Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Some college, no degree',
                      'Number!!Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Associate\'s degree',
                      'Number!!Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Bachelor\'s degree',
                      'Number!!Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Graduate or professional degree']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!EDUCATIONAL ATTAINMENT!!Less than 9th grade',
                      'Estimate!!EDUCATIONAL ATTAINMENT!!9th to 12th grade, no diploma',
                      'Estimate!!EDUCATIONAL ATTAINMENT!!High school graduate (includes equivalency)',
                      'Estimate!!EDUCATIONAL ATTAINMENT!!Some college, no degree',
                      'Estimate!!EDUCATIONAL ATTAINMENT!!Associate\'s degree',
                      'Estimate!!EDUCATIONAL ATTAINMENT!!Bachelor\'s degree',
                      'Estimate!!EDUCATIONAL ATTAINMENT!!Graduate or professional degree']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Less than 9th grade',
                      'Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!9th to 12th grade, no diploma',
                      'Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!High school graduate (includes equivalency)',
                      'Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Some college, no degree',
                      'Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Associate\'s degree',
                      'Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Bachelor\'s degree',
                      'Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Graduate or professional degree']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    
    
    return get_demo_data('DP02',year,geo,labels)

def get_veteran_status(year,geo,as_percent=False):
    
    # set labels 
    if as_percent:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!VETERAN STATUS!!Civilian population 18 years and over!!Civilian veterans']
        elif year in ['2010','2011','2012','2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!VETERAN STATUS!!Civilian population 18 years and over!!Civilian veterans']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!VETERAN STATUS!!Civilian population 18 years and over!!Civilian veterans']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Number!!Estimate!!VETERAN STATUS!!Civilian population 18 years and over!!Civilian veterans']
        elif year in ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!VETERAN STATUS!!Civilian population 18 years and over!!Civilian veterans']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    
    
    return get_demo_data('DP02',year,geo,labels)

def get_residence_year_ago(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent: 
        if year in ['2009']:
            labels = ['Number!!Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Same house',
                      'Number!!Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Different house in the U.S.!!Same county',
                      'Number!!Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Different house in the U.S.!!Different county!!Same state',
                      'Number!!Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Different house in the U.S.!!Different county!!Different state',
                      'Number!!Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Abroad']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!RESIDENCE 1 YEAR AGO!!Same house',
                      'Estimate!!RESIDENCE 1 YEAR AGO!!Different house in the U.S.!!Same county',
                      'Estimate!!RESIDENCE 1 YEAR AGO!!Different house in the U.S.!!Different county!!Same state',
                      'Estimate!!RESIDENCE 1 YEAR AGO!!Different house in the U.S.!!Different county!!Different state',
                      'Estimate!!RESIDENCE 1 YEAR AGO!!Abroad']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Same house',
                      'Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Different house in the U.S.!!Same county',
                      'Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Different house in the U.S.!!Different county!!Same state',
                      'Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Different house in the U.S.!!Different county!!Different state',
                      'Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Abroad']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Same house',
                      'Percent!!Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Different house in the U.S.!!Same county',
                      'Percent!!Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Different house in the U.S.!!Different county!!Same state',
                      'Percent!!Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Different house in the U.S.!!Different county!!Different state',
                      'Percent!!Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Abroad']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!RESIDENCE 1 YEAR AGO!!Same house',
                      'Percent!!RESIDENCE 1 YEAR AGO!!Different house in the U.S.!!Same county',
                      'Percent!!RESIDENCE 1 YEAR AGO!!Different house in the U.S.!!Different county!!Same state',
                      'Percent!!RESIDENCE 1 YEAR AGO!!Different house in the U.S.!!Different county!!Different state',
                      'Percent!!RESIDENCE 1 YEAR AGO!!Abroad']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Same house',
                      'Percent!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Different house in the U.S.!!Same county',
                      'Percent!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Different house in the U.S.!!Different county!!Same state',
                      'Percent!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Different house in the U.S.!!Different county!!Different state',
                      'Percent!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Abroad']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Same house',
                      'Percent Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Different house in the U.S.!!Same county',
                      'Percent Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Different house in the U.S.!!Different county!!Same state',
                      'Percent Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Different house in the U.S.!!Different county!!Different state',
                      'Percent Estimate!!RESIDENCE 1 YEAR AGO!!Population 1 year and over!!Abroad']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    
    return get_demo_data('DP02',year,geo,labels)

def get_place_of_birth(year,geo,as_percent=False):
    
    # set labels 
    if as_percent:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!PLACE OF BIRTH!!Total population!!Native!!Born in United States!!State of residence',
                      'Percent!!Estimate!!PLACE OF BIRTH!!Total population!!Native!!Born in United States!!Different state',
                      'Percent!!Estimate!!PLACE OF BIRTH!!Total population!!Native!!Born in Puerto Rico, U.S. Island areas, or born abroad to American parent(s)',
                      'Percent!!Estimate!!PLACE OF BIRTH!!Total population!!Foreign born']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!PLACE OF BIRTH!!Native!!Born in United States!!State of residence',
                      'Percent!!PLACE OF BIRTH!!Native!!Born in United States!!Different state',
                      'Percent!!PLACE OF BIRTH!!Native!!Born in Puerto Rico, U.S. Island areas, or born abroad to American parent(s)',
                      'Percent!!PLACE OF BIRTH!!Foreign born']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!PLACE OF BIRTH!!Total population!!Native!!Born in United States!!State of residence',
                      'Percent!!PLACE OF BIRTH!!Total population!!Native!!Born in United States!!Different state',
                      'Percent!!PLACE OF BIRTH!!Total population!!Native!!Born in Puerto Rico, U.S. Island areas, or born abroad to American parent(s)',
                      'Percent!!PLACE OF BIRTH!!Total population!!Foreign born']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!PLACE OF BIRTH!!Total population!!Native!!Born in United States!!State of residence',
                      'Percent Estimate!!PLACE OF BIRTH!!Total population!!Native!!Born in United States!!Different state',
                      'Percent Estimate!!PLACE OF BIRTH!!Total population!!Native!!Born in Puerto Rico, U.S. Island areas, or born abroad to American parent(s)',
                      'Percent Estimate!!PLACE OF BIRTH!!Total population!!Foreign born']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Number!!Estimate!!PLACE OF BIRTH!!Total population!!Native!!Born in United States!!State of residence',
                      'Number!!Estimate!!PLACE OF BIRTH!!Total population!!Native!!Born in United States!!Different state',
                      'Number!!Estimate!!PLACE OF BIRTH!!Total population!!Native!!Born in Puerto Rico, U.S. Island areas, or born abroad to American parent(s)',
                      'Number!!Estimate!!PLACE OF BIRTH!!Total population!!Foreign born']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!PLACE OF BIRTH!!Native!!Born in United States!!State of residence',
                      'Estimate!!PLACE OF BIRTH!!Native!!Born in United States!!Different state',
                      'Estimate!!PLACE OF BIRTH!!Native!!Born in Puerto Rico, U.S. Island areas, or born abroad to American parent(s)',
                      'Estimate!!PLACE OF BIRTH!!Foreign born']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!PLACE OF BIRTH!!Total population!!Native!!Born in United States!!State of residence',
                      'Estimate!!PLACE OF BIRTH!!Total population!!Native!!Born in United States!!Different state',
                      'Estimate!!PLACE OF BIRTH!!Total population!!Native!!Born in Puerto Rico, U.S. Island areas, or born abroad to American parent(s)',
                      'Estimate!!PLACE OF BIRTH!!Total population!!Foreign born']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    
    
    return get_demo_data('DP02',year,geo,labels)

def get_US_citizenship_status(year,geo,as_percent=False):
    
    # set labels 
    if as_percent:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!U.S. CITIZENSHIP STATUS!!Foreign-born population!!Naturalized U.S. citizen',
                      'Percent!!Estimate!!U.S. CITIZENSHIP STATUS!!Foreign-born population!!Not a U.S. citizen']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!U.S. CITIZENSHIP STATUS!!Naturalized U.S. citizen',
                      'Percent!!U.S. CITIZENSHIP STATUS!!Not a U.S. citizen']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!U.S. CITIZENSHIP STATUS!!Foreign-born population!!Naturalized U.S. citizen',
                      'Percent!!U.S. CITIZENSHIP STATUS!!Foreign-born population!!Not a U.S. citizen']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!U.S. CITIZENSHIP STATUS!!Foreign-born population!!Naturalized U.S. citizen',
                      'Percent Estimate!!U.S. CITIZENSHIP STATUS!!Foreign-born population!!Not a U.S. citizen']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Number!!Estimate!!U.S. CITIZENSHIP STATUS!!Foreign-born population!!Naturalized U.S. citizen',
                      'Number!!Estimate!!U.S. CITIZENSHIP STATUS!!Foreign-born population!!Not a U.S. citizen']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!U.S. CITIZENSHIP STATUS!!Naturalized U.S. citizen',
                      'Estimate!!U.S. CITIZENSHIP STATUS!!Not a U.S. citizen']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!U.S. CITIZENSHIP STATUS!!Foreign-born population!!Naturalized U.S. citizen',
                      'Estimate!!U.S. CITIZENSHIP STATUS!!Foreign-born population!!Not a U.S. citizen']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    
    
    return get_demo_data('DP02',year,geo,labels)

def get_world_region_of_birth_of_foreign_born(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Europe',
                      'Number!!Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Asia',
                      'Number!!Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Africa',
                      'Number!!Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Oceania',
                      'Number!!Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Latin America',
                      'Number!!Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Northern America']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Europe',
                      'Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Asia',
                      'Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Africa',
                      'Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Oceania',
                      'Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Latin America',
                      'Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Northern America']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']:
            labels = ['Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Europe',
                      'Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Asia',
                      'Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Africa',
                      'Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Oceania',
                      'Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Latin America',
                      'Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Northern America']
        elif year in ['2023']:
            labels = ['Estimate!!WORLD REGION OF BIRTH OF FOREIGN-BORN!!Foreign-born population, excluding population born at sea!!Europe',
                      'Estimate!!WORLD REGION OF BIRTH OF FOREIGN-BORN!!Foreign-born population, excluding population born at sea!!Asia',
                      'Estimate!!WORLD REGION OF BIRTH OF FOREIGN-BORN!!Foreign-born population, excluding population born at sea!!Africa',
                      'Estimate!!WORLD REGION OF BIRTH OF FOREIGN-BORN!!Foreign-born population, excluding population born at sea!!Oceania',
                      'Estimate!!WORLD REGION OF BIRTH OF FOREIGN-BORN!!Foreign-born population, excluding population born at sea!!Latin America',
                      'Estimate!!WORLD REGION OF BIRTH OF FOREIGN-BORN!!Foreign-born population, excluding population born at sea!!Northern America']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Europe',
                      'Percent!!Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Asia',
                      'Percent!!Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Africa',
                      'Percent!!Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Oceania',
                      'Percent!!Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Latin America',
                      'Percent!!Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Northern America']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Europe',
                      'Percent!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Asia',
                      'Percent!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Africa',
                      'Percent!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Oceania',
                      'Percent!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Latin America',
                      'Percent!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Northern America']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022']:
            labels = ['Percent!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Europe',
                      'Percent!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Asia',
                      'Percent!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Africa',
                      'Percent!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Oceania',
                      'Percent!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Latin America',
                      'Percent!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Northern America']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Europe',
                      'Percent Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Asia',
                      'Percent Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Africa',
                      'Percent Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Oceania',
                      'Percent Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Latin America',
                      'Percent Estimate!!WORLD REGION OF BIRTH OF FOREIGN BORN!!Foreign-born population, excluding population born at sea!!Northern America']
        elif year in ['2023']:
            labels = ['Percent!!WORLD REGION OF BIRTH OF FOREIGN-BORN!!Foreign-born population, excluding population born at sea!!Europe',
                      'Percent!!WORLD REGION OF BIRTH OF FOREIGN-BORN!!Foreign-born population, excluding population born at sea!!Asia',
                      'Percent!!WORLD REGION OF BIRTH OF FOREIGN-BORN!!Foreign-born population, excluding population born at sea!!Africa',
                      'Percent!!WORLD REGION OF BIRTH OF FOREIGN-BORN!!Foreign-born population, excluding population born at sea!!Oceania',
                      'Percent!!WORLD REGION OF BIRTH OF FOREIGN-BORN!!Foreign-born population, excluding population born at sea!!Latin America',
                      'Percent!!WORLD REGION OF BIRTH OF FOREIGN-BORN!!Foreign-born population, excluding population born at sea!!Northern America']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    
    return get_demo_data('DP02',year,geo,labels)

def get_language_spoken_at_home(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!English only',
                      'Number!!Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Spanish',
                      'Number!!Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Other Indo-European languages',
                      'Number!!Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Asian and Pacific Islander languages',
                      'Number!!Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Other languages']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!LANGUAGE SPOKEN AT HOME!!English only',
                      'Estimate!!LANGUAGE SPOKEN AT HOME!!Language other than English!!Spanish',
                      'Estimate!!LANGUAGE SPOKEN AT HOME!!Language other than English!!Other Indo-European languages',
                      'Estimate!!LANGUAGE SPOKEN AT HOME!!Language other than English!!Asian and Pacific Islander languages',
                      'Estimate!!LANGUAGE SPOKEN AT HOME!!Language other than English!!Other languages']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!English only',
                      'Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Spanish',
                      'Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Other Indo-European languages',
                      'Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Asian and Pacific Islander languages',
                      'Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Other languages']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!English only',
                      'Percent!!Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Spanish',
                      'Percent!!Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Other Indo-European languages',
                      'Percent!!Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Asian and Pacific Islander languages',
                      'Percent!!Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Other languages']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!LANGUAGE SPOKEN AT HOME!!English only',
                      'Percent!!LANGUAGE SPOKEN AT HOME!!Language other than English!!Spanish',
                      'Percent!!LANGUAGE SPOKEN AT HOME!!Language other than English!!Other Indo-European languages',
                      'Percent!!LANGUAGE SPOKEN AT HOME!!Language other than English!!Asian and Pacific Islander languages',
                      'Percent!!LANGUAGE SPOKEN AT HOME!!Language other than English!!Other languages']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!English only',
                      'Percent!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Spanish',
                      'Percent!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Other Indo-European languages',
                      'Percent!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Asian and Pacific Islander languages',
                      'Percent!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Other languages']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!English only',
                      'Percent Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Spanish',
                      'Percent Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Other Indo-European languages',
                      'Percent Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Asian and Pacific Islander languages',
                      'Percent Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Other languages']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    
    return get_demo_data('DP02',year,geo,labels)
        