from .census_API_wrapper import get_demo_data

def get_employment_status(year,geo,as_percent=False):
    
    # set labels
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Employed',
                      'Number!!Estimate!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Unemployed',
                      'Number!!Estimate!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Armed Forces',
                      'Number!!Estimate!!EMPLOYMENT STATUS!!Population 16 years and over!!Not in labor force']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!EMPLOYMENT STATUS!!In labor force!!Civilian labor force!!Employed',
                      'Estimate!!EMPLOYMENT STATUS!!In labor force!!Civilian labor force!!Unemployed',
                      'Estimate!!EMPLOYMENT STATUS!!In labor force!!Armed Forces',
                      'Estimate!!EMPLOYMENT STATUS!!Not in labor force']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Employed',
                      'Estimate!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Unemployed',
                      'Estimate!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Armed Forces',
                      'Estimate!!EMPLOYMENT STATUS!!Population 16 years and over!!Not in labor force']
        else: 
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Employed',
                      'Percent!!Estimate!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Unemployed',
                      'Percent!!Estimate!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Armed Forces',
                      'Percent!!Estimate!!EMPLOYMENT STATUS!!Population 16 years and over!!Not in labor force']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!EMPLOYMENT STATUS!!In labor force!!Civilian labor force!!Employed',
                      'Percent!!EMPLOYMENT STATUS!!In labor force!!Civilian labor force!!Unemployed',
                      'Percent!!EMPLOYMENT STATUS!!In labor force!!Armed Forces',
                      'Percent!!EMPLOYMENT STATUS!!Not in labor force']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Employed',
                      'Percent!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Unemployed',
                      'Percent!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Armed Forces',
                      'Percent!!EMPLOYMENT STATUS!!Population 16 years and over!!Not in labor force']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Employed',
                      'Percent Estimate!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Unemployed',
                      'Percent Estimate!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Armed Forces',
                      'Percent Estimate!!EMPLOYMENT STATUS!!Population 16 years and over!!Not in labor force']
        else: 
            print(f"Error: Unsupported year '{year}'")
            return None
    
    return get_demo_data('DP03',year,geo,labels)

def get_commuting_to_work(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Car, truck, or van -- drove alone',
                      'Number!!Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Car, truck, or van -- carpooled',
                      'Number!!Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Public transportation (excluding taxicab)',
                      'Number!!Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Walked',
                      'Number!!Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Other means',
                      'Number!!Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Worked at home'] 
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!COMMUTING TO WORK!!Car, truck, or van -- drove alone',
                      'Estimate!!COMMUTING TO WORK!!Car, truck, or van -- carpooled',
                      'Estimate!!COMMUTING TO WORK!!Public transportation (excluding taxicab)',
                      'Estimate!!COMMUTING TO WORK!!Walked',
                      'Estimate!!COMMUTING TO WORK!!Other means',
                      'Estimate!!COMMUTING TO WORK!!Worked at home']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Car, truck, or van -- drove alone',
                      'Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Car, truck, or van -- carpooled',
                      'Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Public transportation (excluding taxicab)',
                      'Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Walked',
                      'Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Other means',
                      'Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Worked at home']
        elif year in ['2019','2020','2021','2022','2023']:
            labels = ['Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Car, truck, or van -- drove alone',
                      'Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Car, truck, or van -- carpooled',
                      'Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Public transportation (excluding taxicab)',
                      'Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Walked',
                      'Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Other means',
                      'Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Worked from home']
        else: 
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Car, truck, or van -- drove alone',
                      'Percent!!Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Car, truck, or van -- carpooled',
                      'Percent!!Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Public transportation (excluding taxicab)',
                      'Percent!!Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Walked',
                      'Percent!!Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Other means',
                      'Percent!!Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Worked at home']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!COMMUTING TO WORK!!Car, truck, or van -- drove alone',
                      'Percent!!COMMUTING TO WORK!!Car, truck, or van -- carpooled',
                      'Percent!!COMMUTING TO WORK!!Public transportation (excluding taxicab)',
                      'Percent!!COMMUTING TO WORK!!Walked',
                      'Percent!!COMMUTING TO WORK!!Other means',
                      'Percent!!COMMUTING TO WORK!!Worked at home']
        elif year in ['2013','2014','2015','2016']:
            labels = ['Percent!!COMMUTING TO WORK!!Workers 16 years and over!!Car, truck, or van -- drove alone',
                      'Percent!!COMMUTING TO WORK!!Workers 16 years and over!!Car, truck, or van -- carpooled',
                      'Percent!!COMMUTING TO WORK!!Workers 16 years and over!!Public transportation (excluding taxicab)',
                      'Percent!!COMMUTING TO WORK!!Workers 16 years and over!!Walked',
                      'Percent!!COMMUTING TO WORK!!Workers 16 years and over!!Other means',
                      'Percent!!COMMUTING TO WORK!!Workers 16 years and over!!Worked at home']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Car, truck, or van -- drove alone',
                      'Percent Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Car, truck, or van -- carpooled',
                      'Percent Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Public transportation (excluding taxicab)',
                      'Percent Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Walked',
                      'Percent Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Other means',
                      'Percent Estimate!!COMMUTING TO WORK!!Workers 16 years and over!!Worked at home']
        elif year in ['2019','2020','2021','2022','2023']:
            labels = ['Percent!!COMMUTING TO WORK!!Workers 16 years and over!!Car, truck, or van -- drove alone',
                      'Percent!!COMMUTING TO WORK!!Workers 16 years and over!!Car, truck, or van -- carpooled',
                      'Percent!!COMMUTING TO WORK!!Workers 16 years and over!!Public transportation (excluding taxicab)',
                      'Percent!!COMMUTING TO WORK!!Workers 16 years and over!!Walked',
                      'Percent!!COMMUTING TO WORK!!Workers 16 years and over!!Other means',
                      'Percent!!COMMUTING TO WORK!!Workers 16 years and over!!Worked from home']
        else: 
            print(f"Error: Unsupported year '{year}'")
            return None
    
    # fetch data 
    data = get_demo_data('DP03',year,geo,labels)
    
    # update work from home column name if needed 
    if int(year) < 2019:
        data = data.rename(columns={'Worked at home':'Worked from home'})
    
    return data

def get_occupation(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2010','2011','2012']:
            labels = ['Estimate!!OCCUPATION!!Management, business, science, and arts occupations',
                      'Estimate!!OCCUPATION!!Service occupations',
                      'Estimate!!OCCUPATION!!Sales and office occupations',
                      'Estimate!!OCCUPATION!!Natural resources, construction, and maintenance occupations',
                      'Estimate!!OCCUPATION!!Production, transportation, and material moving occupations']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!OCCUPATION!!Civilian employed population 16 years and over!!Management, business, science, and arts occupations',
                      'Estimate!!OCCUPATION!!Civilian employed population 16 years and over!!Service occupations',
                      'Estimate!!OCCUPATION!!Civilian employed population 16 years and over!!Sales and office occupations',
                      'Estimate!!OCCUPATION!!Civilian employed population 16 years and over!!Natural resources, construction, and maintenance occupations',
                      'Estimate!!OCCUPATION!!Civilian employed population 16 years and over!!Production, transportation, and material moving occupations']
        else: 
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2010','2011','2012']:
            labels = ['Percent!!OCCUPATION!!Management, business, science, and arts occupations',
                      'Percent!!OCCUPATION!!Service occupations',
                      'Percent!!OCCUPATION!!Sales and office occupations',
                      'Percent!!OCCUPATION!!Natural resources, construction, and maintenance occupations',
                      'Percent!!OCCUPATION!!Production, transportation, and material moving occupations']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!OCCUPATION!!Civilian employed population 16 years and over!!Management, business, science, and arts occupations',
                      'Percent!!OCCUPATION!!Civilian employed population 16 years and over!!Service occupations',
                      'Percent!!OCCUPATION!!Civilian employed population 16 years and over!!Sales and office occupations',
                      'Percent!!OCCUPATION!!Civilian employed population 16 years and over!!Natural resources, construction, and maintenance occupations',
                      'Percent!!OCCUPATION!!Civilian employed population 16 years and over!!Production, transportation, and material moving occupations']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!OCCUPATION!!Civilian employed population 16 years and over!!Management, business, science, and arts occupations',
                      'Percent Estimate!!OCCUPATION!!Civilian employed population 16 years and over!!Service occupations',
                      'Percent Estimate!!OCCUPATION!!Civilian employed population 16 years and over!!Sales and office occupations',
                      'Percent Estimate!!OCCUPATION!!Civilian employed population 16 years and over!!Natural resources, construction, and maintenance occupations',
                      'Percent Estimate!!OCCUPATION!!Civilian employed population 16 years and over!!Production, transportation, and material moving occupations']
        else: 
            print(f"Error: Unsupported year '{year}'")
            return None
     
    return get_demo_data('DP03',year,geo,labels)

def get_industry(year,geo,as_percent=False):
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Agriculture, forestry, fishing and hunting, and mining',
                      'Number!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Construction',
                      'Number!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Manufacturing',
                      'Number!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Wholesale trade',
                      'Number!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Retail trade',
                      'Number!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Transportation and warehousing, and utilities',
                      'Number!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Information',
                      'Number!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Finance and insurance, and real estate and rental and leasing',
                      'Number!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Professional, scientific, and management, and administrative and waste management services',
                      'Number!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Educational services, and health care and social assistance',
                      'Number!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Arts, entertainment, and recreation, and accommodation and food services',
                      'Number!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Other services, except public administration',
                      'Number!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Public administration']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!INDUSTRY!!Agriculture, forestry, fishing and hunting, and mining',
                      'Estimate!!INDUSTRY!!Construction',
                      'Estimate!!INDUSTRY!!Manufacturing',
                      'Estimate!!INDUSTRY!!Wholesale trade',
                      'Estimate!!INDUSTRY!!Retail trade',
                      'Estimate!!INDUSTRY!!Transportation and warehousing, and utilities',
                      'Estimate!!INDUSTRY!!Information',
                      'Estimate!!INDUSTRY!!Finance and insurance, and real estate and rental and leasing',
                      'Estimate!!INDUSTRY!!Professional, scientific, and management, and administrative and waste management services',
                      'Estimate!!INDUSTRY!!Educational services, and health care and social assistance',
                      'Estimate!!INDUSTRY!!Arts, entertainment, and recreation, and accommodation and food services',
                      'Estimate!!INDUSTRY!!Other services, except public administration',
                      'Estimate!!INDUSTRY!!Public administration']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Agriculture, forestry, fishing and hunting, and mining',
                      'Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Construction',
                      'Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Manufacturing',
                      'Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Wholesale trade',
                      'Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Retail trade',
                      'Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Transportation and warehousing, and utilities',
                      'Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Information',
                      'Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Finance and insurance, and real estate and rental and leasing',
                      'Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Professional, scientific, and management, and administrative and waste management services',
                      'Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Educational services, and health care and social assistance',
                      'Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Arts, entertainment, and recreation, and accommodation and food services',
                      'Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Other services, except public administration',
                      'Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Public administration']
        else: 
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Agriculture, forestry, fishing and hunting, and mining',
                      'Percent!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Construction',
                      'Percent!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Manufacturing',
                      'Percent!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Wholesale trade',
                      'Percent!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Retail trade',
                      'Percent!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Transportation and warehousing, and utilities',
                      'Percent!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Information',
                      'Percent!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Finance and insurance, and real estate and rental and leasing',
                      'Percent!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Professional, scientific, and management, and administrative and waste management services',
                      'Percent!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Educational services, and health care and social assistance',
                      'Percent!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Arts, entertainment, and recreation, and accommodation and food services',
                      'Percent!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Other services, except public administration',
                      'Percent!!Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Public administration']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!INDUSTRY!!Agriculture, forestry, fishing and hunting, and mining',
                      'Percent!!INDUSTRY!!Construction',
                      'Percent!!INDUSTRY!!Manufacturing',
                      'Percent!!INDUSTRY!!Wholesale trade',
                      'Percent!!INDUSTRY!!Retail trade',
                      'Percent!!INDUSTRY!!Transportation and warehousing, and utilities',
                      'Percent!!INDUSTRY!!Information',
                      'Percent!!INDUSTRY!!Finance and insurance, and real estate and rental and leasing',
                      'Percent!!INDUSTRY!!Professional, scientific, and management, and administrative and waste management services',
                      'Percent!!INDUSTRY!!Educational services, and health care and social assistance',
                      'Percent!!INDUSTRY!!Arts, entertainment, and recreation, and accommodation and food services',
                      'Percent!!INDUSTRY!!Other services, except public administration',
                      'Percent!!INDUSTRY!!Public administration']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!INDUSTRY!!Civilian employed population 16 years and over!!Agriculture, forestry, fishing and hunting, and mining',
                      'Percent!!INDUSTRY!!Civilian employed population 16 years and over!!Construction',
                      'Percent!!INDUSTRY!!Civilian employed population 16 years and over!!Manufacturing',
                      'Percent!!INDUSTRY!!Civilian employed population 16 years and over!!Wholesale trade',
                      'Percent!!INDUSTRY!!Civilian employed population 16 years and over!!Retail trade',
                      'Percent!!INDUSTRY!!Civilian employed population 16 years and over!!Transportation and warehousing, and utilities',
                      'Percent!!INDUSTRY!!Civilian employed population 16 years and over!!Information',
                      'Percent!!INDUSTRY!!Civilian employed population 16 years and over!!Finance and insurance, and real estate and rental and leasing',
                      'Percent!!INDUSTRY!!Civilian employed population 16 years and over!!Professional, scientific, and management, and administrative and waste management services',
                      'Percent!!INDUSTRY!!Civilian employed population 16 years and over!!Educational services, and health care and social assistance',
                      'Percent!!INDUSTRY!!Civilian employed population 16 years and over!!Arts, entertainment, and recreation, and accommodation and food services',
                      'Percent!!INDUSTRY!!Civilian employed population 16 years and over!!Other services, except public administration',
                      'Percent!!INDUSTRY!!Civilian employed population 16 years and over!!Public administration']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Agriculture, forestry, fishing and hunting, and mining',
                      'Percent Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Construction',
                      'Percent Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Manufacturing',
                      'Percent Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Wholesale trade',
                      'Percent Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Retail trade',
                      'Percent Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Transportation and warehousing, and utilities',
                      'Percent Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Information',
                      'Percent Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Finance and insurance, and real estate and rental and leasing',
                      'Percent Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Professional, scientific, and management, and administrative and waste management services',
                      'Percent Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Educational services, and health care and social assistance',
                      'Percent Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Arts, entertainment, and recreation, and accommodation and food services',
                      'Percent Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Other services, except public administration',
                      'Percent Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Public administration']
        else: 
            print(f"Error: Unsupported year '{year}'")
            return None
     
    return get_demo_data('DP03',year,geo,labels)

def get_class_of_worker(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Private wage and salary workers',
                      'Number!!Estimate!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Government workers',
                      'Number!!Estimate!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Self-employed in own not incorporated business workers',
                      'Number!!Estimate!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Unpaid family workers']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!CLASS OF WORKER!!Private wage and salary workers',
                      'Estimate!!CLASS OF WORKER!!Government workers',
                      'Estimate!!CLASS OF WORKER!!Self-employed in own not incorporated business workers',
                      'Estimate!!CLASS OF WORKER!!Unpaid family workers']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Private wage and salary workers',
                      'Estimate!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Government workers',
                      'Estimate!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Self-employed in own not incorporated business workers',
                      'Estimate!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Unpaid family workers']
        else: 
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Private wage and salary workers',
                      'Percent!!Estimate!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Government workers',
                      'Percent!!Estimate!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Self-employed in own not incorporated business workers',
                      'Percent!!Estimate!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Unpaid family workers']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!CLASS OF WORKER!!Private wage and salary workers',
                      'Percent!!CLASS OF WORKER!!Government workers',
                      'Percent!!CLASS OF WORKER!!Self-employed in own not incorporated business workers',
                      'Percent!!CLASS OF WORKER!!Unpaid family workers']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Private wage and salary workers',
                      'Percent!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Government workers',
                      'Percent!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Self-employed in own not incorporated business workers',
                      'Percent!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Unpaid family workers']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Private wage and salary workers',
                      'Percent Estimate!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Government workers',
                      'Percent Estimate!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Self-employed in own not incorporated business workers',
                      'Percent Estimate!!CLASS OF WORKER!!Civilian employed population 16 years and over!!Unpaid family workers']
    
    return get_demo_data('DP03',year,geo,labels)

def get_household_income(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2010']:
            labels = ['Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!Less than $10,000',
                      'Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$10,000 to $14,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$15,000 to $24,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$25,000 to $34,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$35,000 to $49,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$50,000 to $74,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$75,000 to $99,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$100,000 to $149,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$150,000 to $199,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$200,000 or more']
        elif year in ['2011']:
            labels = ['Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!Less than $10,000',
                      'Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$10,000 to $14,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$15,000 to $24,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$25,000 to $34,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$35,000 to $49,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$50,000 to $74,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$75,000 to $99,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$100,000 to $149,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$150,000 to $199,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$200,000 or more']
        elif year in ['2012']:
            labels = ['Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!Less than $10,000',
                      'Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$10,000 to $14,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$15,000 to $24,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$25,000 to $34,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$35,000 to $49,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$50,000 to $74,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$75,000 to $99,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$100,000 to $149,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$150,000 to $199,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$200,000 or more']
        elif year in ['2013']:
            labels = ['Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2014']:
            labels = ['Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2015']:
            labels = ['Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2016']:
            labels = ['Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2017']:
            labels = ['Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2018']:
            labels = ['Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2019']:
            labels = ['Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2020']:
            labels = ['Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2021']:
            labels = ['Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2022']:
            labels = ['Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2023']:
            labels = ['Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2010']:
            labels = ['Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!Less than $10,000',
                      'Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$10,000 to $14,999',
                      'Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$15,000 to $24,999',
                      'Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$25,000 to $34,999',
                      'Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$35,000 to $49,999',
                      'Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$50,000 to $74,999',
                      'Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$75,000 to $99,999',
                      'Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$100,000 to $149,999',
                      'Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$150,000 to $199,999',
                      'Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$200,000 or more']
        elif year in ['2011']:
            labels = ['Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!Less than $10,000',
                      'Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$10,000 to $14,999',
                      'Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$15,000 to $24,999',
                      'Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$25,000 to $34,999',
                      'Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$35,000 to $49,999',
                      'Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$50,000 to $74,999',
                      'Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$75,000 to $99,999',
                      'Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$100,000 to $149,999',
                      'Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$150,000 to $199,999',
                      'Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$200,000 or more']
        elif year in ['2012']:
            labels = ['Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!Less than $10,000',
                      'Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$10,000 to $14,999',
                      'Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$15,000 to $24,999',
                      'Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$25,000 to $34,999',
                      'Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$35,000 to $49,999',
                      'Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$50,000 to $74,999',
                      'Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$75,000 to $99,999',
                      'Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$100,000 to $149,999',
                      'Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$150,000 to $199,999',
                      'Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$200,000 or more']
        elif year in ['2013']:
            labels = ['Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2014']:
            labels = ['Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2015']:
            labels = ['Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2016']:
            labels = ['Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2017']:
            labels = ['Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2018']:
            labels = ['Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2019']:
            labels = ['Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2020']:
            labels = ['Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2021']:
            labels = ['Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2022']:
            labels = ['Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        elif year in ['2023']:
            labels = ['Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                      'Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                      'Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                      'Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                      'Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                      'Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                      'Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                      'Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                      'Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                      'Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    
    return get_demo_data('DP03', year, geo, labels)

def get_households_with_earnings(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        
        # define dictionary 
        year_label_dict = {
            '2009': ['Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!With earnings'],
            '2010': ['Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!With earnings'],
            '2011': ['Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!With earnings'],
            '2012': ['Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!With earnings'],
            '2013': ['Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!With earnings'],
            '2014': ['Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!With earnings'],
            '2015': ['Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!With earnings'],
            '2016': ['Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!With earnings'],
            '2017': ['Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!With earnings'],
            '2018': ['Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!With earnings'], 
            '2019': ['Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!With earnings'],
            '2020': ['Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!With earnings'],
            '2021': ['Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!With earnings'],
            '2022': ['Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!With earnings'],
            '2023': ['Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!With earnings']
        }
        
        labels = year_label_dict.get(year, "Year not found")
    else:
        # define dictionary 
        year_label_dict = {
            '2009': ['Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!With earnings'],
            '2010': ['Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!With earnings'],
            '2011': ['Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!With earnings'],
            '2012': ['Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!With earnings'],
            '2013': ['Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!With earnings'],
            '2014': ['Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!With earnings'],
            '2015': ['Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!With earnings'],
            '2016': ['Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!With earnings'],
            '2017': ['Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!With earnings'],
            '2018': ['Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!With earnings'], 
            '2019': ['Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!With earnings'],
            '2020': ['Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!With earnings'],
            '2021': ['Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!With earnings'],
            '2022': ['Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!With earnings'],
            '2023': ['Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!With earnings']
        }
        
        labels = year_label_dict.get(year, "Year not found")
    
    return get_demo_data('DP03', year, geo, labels)

def get_households_with_social_security(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        
        # define dictionary 
        year_label_dict = {
            '2009': ['Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Social Security'],
            '2010': ['Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!With Social Security'],
            '2011': ['Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!With Social Security'],
            '2012': ['Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!With Social Security'],
            '2013': ['Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!With Social Security'],
            '2014': ['Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!With Social Security'],
            '2015': ['Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!With Social Security'],
            '2016': ['Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!With Social Security'],
            '2017': ['Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Social Security'],
            '2018': ['Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Social Security'], 
            '2019': ['Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Social Security'],
            '2020': ['Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Social Security'],
            '2021': ['Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Social Security'],
            '2022': ['Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Social Security'],
            '2023': ['Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Social Security']
        }
        
        labels = year_label_dict.get(year, "Year not found")
    else:
        # define dictionary 
        year_label_dict = {
            '2009': ['Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Social Security'],
            '2010': ['Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!With Social Security'],
            '2011': ['Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!With Social Security'],
            '2012': ['Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!With Social Security'],
            '2013': ['Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!With Social Security'],
            '2014': ['Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!With Social Security'],
            '2015': ['Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!With Social Security'],
            '2016': ['Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!With Social Security'],
            '2017': ['Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Social Security'],
            '2018': ['Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Social Security'], 
            '2019': ['Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Social Security'],
            '2020': ['Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Social Security'],
            '2021': ['Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Social Security'],
            '2022': ['Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Social Security'],
            '2023': ['Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Social Security']
        }
        
        labels = year_label_dict.get(year, "Year not found")
    
    return get_demo_data('DP03', year, geo, labels)

def get_households_with_retirement_income(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        
        # define dictionary 
        year_label_dict = {
            '2009': ['Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!With retirement income'],
            '2010': ['Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!With retirement income'],
            '2011': ['Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!With retirement income'],
            '2012': ['Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!With retirement income'],
            '2013': ['Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!With retirement income'],
            '2014': ['Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!With retirement income'],
            '2015': ['Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!With retirement income'],
            '2016': ['Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!With retirement income'],
            '2017': ['Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!With retirement income'],
            '2018': ['Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!With retirement income'], 
            '2019': ['Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!With retirement income'],
            '2020': ['Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!With retirement income'],
            '2021': ['Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!With retirement income'],
            '2022': ['Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!With retirement income'],
            '2023': ['Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!With retirement income']
        }
        
        labels = year_label_dict.get(year, "Year not found")
    else:
        # define dictionary 
        year_label_dict = {
            '2009': ['Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!With retirement income'],
            '2010': ['Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!With retirement income'],
            '2011': ['Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!With retirement income'],
            '2012': ['Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!With retirement income'],
            '2013': ['Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!With retirement income'],
            '2014': ['Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!With retirement income'],
            '2015': ['Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!With retirement income'],
            '2016': ['Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!With retirement income'],
            '2017': ['Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!With retirement income'],
            '2018': ['Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!With retirement income'], 
            '2019': ['Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!With retirement income'],
            '2020': ['Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!With retirement income'],
            '2021': ['Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!With retirement income'],
            '2022': ['Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!With retirement income'],
            '2023': ['Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!With retirement income']
        }
        
        labels = year_label_dict.get(year, "Year not found")
    
    return get_demo_data('DP03', year, geo, labels)

def get_households_with_supplemental_security_income(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        
        # define dictionary 
        year_label_dict = {
            '2009': ['Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income'],
            '2010': ['Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!With Supplemental Security Income'],
            '2011': ['Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!With Supplemental Security Income'],
            '2012': ['Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!With Supplemental Security Income'],
            '2013': ['Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!With Supplemental Security Income'],
            '2014': ['Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!With Supplemental Security Income'],
            '2015': ['Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!With Supplemental Security Income'],
            '2016': ['Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!With Supplemental Security Income'],
            '2017': ['Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income'],
            '2018': ['Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income'], 
            '2019': ['Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income'],
            '2020': ['Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income'],
            '2021': ['Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income'],
            '2022': ['Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income'],
            '2023': ['Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income']
        }
        
        labels = year_label_dict.get(year, "Year not found")
    else:
        # define dictionary 
        year_label_dict = {
            '2009': ['Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income'],
            '2010': ['Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!With Supplemental Security Income'],
            '2011': ['Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!With Supplemental Security Income'],
            '2012': ['Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!With Supplemental Security Income'],
            '2013': ['Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!With Supplemental Security Income'],
            '2014': ['Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!With Supplemental Security Income'],
            '2015': ['Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!With Supplemental Security Income'],
            '2016': ['Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!With Supplemental Security Income'],
            '2017': ['Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income'],
            '2018': ['Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income'], 
            '2019': ['Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income'],
            '2020': ['Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income'],
            '2021': ['Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income'],
            '2022': ['Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income'],
            '2023': ['Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income']
        }
        
        labels = year_label_dict.get(year, "Year not found")
    
    return get_demo_data('DP03', year, geo, labels)

def get_households_with_cash_public_assistance_income(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        
        # define dictionary 
        year_label_dict = {
            '2009': ['Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income'],
            '2010': ['Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!With cash public assistance income'],
            '2011': ['Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!With cash public assistance income'],
            '2012': ['Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!With cash public assistance income'],
            '2013': ['Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!With cash public assistance income'],
            '2014': ['Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!With cash public assistance income'],
            '2015': ['Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!With cash public assistance income'],
            '2016': ['Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!With cash public assistance income'],
            '2017': ['Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income'],
            '2018': ['Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income'], 
            '2019': ['Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income'],
            '2020': ['Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income'],
            '2021': ['Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income'],
            '2022': ['Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income'],
            '2023': ['Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income']
        }
        
        labels = year_label_dict.get(year, "Year not found")
    else:
        # define dictionary 
        year_label_dict = {
            '2009': ['Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income'],
            '2010': ['Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!With cash public assistance income'],
            '2011': ['Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!With cash public assistance income'],
            '2012': ['Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!With cash public assistance income'],
            '2013': ['Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!With cash public assistance income'],
            '2014': ['Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!With cash public assistance income'],
            '2015': ['Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!With cash public assistance income'],
            '2016': ['Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!With cash public assistance income'],
            '2017': ['Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income'],
            '2018': ['Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income'], 
            '2019': ['Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income'],
            '2020': ['Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income'],
            '2021': ['Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income'],
            '2022': ['Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income'],
            '2023': ['Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income']
        }
        
        labels = year_label_dict.get(year, "Year not found")
    
    return get_demo_data('DP03', year, geo, labels)

def get_households_with_SNAP_benefits(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        
        # define dictionary 
        year_label_dict = {
            '2009': ['Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2010': ['Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2011': ['Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2012': ['Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2013': ['Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2014': ['Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2015': ['Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2016': ['Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2017': ['Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2018': ['Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months'], 
            '2019': ['Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2020': ['Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2021': ['Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2022': ['Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2023': ['Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months']
        }
        
        labels = year_label_dict.get(year, "Year not found")
    else:
        # define dictionary 
        year_label_dict = {
            '2009': ['Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2010': ['Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2011': ['Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2012': ['Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2013': ['Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2014': ['Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2015': ['Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2016': ['Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2017': ['Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2018': ['Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months'], 
            '2019': ['Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2020': ['Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2021': ['Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2022': ['Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months'],
            '2023': ['Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months']
        }
        
        labels = year_label_dict.get(year, "Year not found")
    
    return get_demo_data('DP03', year, geo, labels)

def get_family_income(year,geo,as_percent=False,return_index=0):
    
    # set labels 
    if not as_percent:
        
        # define dictionary 
        year_label_dict = {
            '2009': ['Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Number!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2010': ['Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!Less than $10,000',
                     'Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$10,000 to $14,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$15,000 to $24,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$25,000 to $34,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$35,000 to $49,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$50,000 to $74,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$75,000 to $99,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$100,000 to $149,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$150,000 to $199,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$200,000 or more'],
            '2011': ['Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!Less than $10,000',
                     'Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$10,000 to $14,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$15,000 to $24,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$25,000 to $34,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$35,000 to $49,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$50,000 to $74,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$75,000 to $99,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$100,000 to $149,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$150,000 to $199,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$200,000 or more'],
            '2012': ['Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!Less than $10,000',
                     'Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$10,000 to $14,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$15,000 to $24,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$25,000 to $34,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$35,000 to $49,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$50,000 to $74,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$75,000 to $99,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$100,000 to $149,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$150,000 to $199,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$200,000 or more'],
            '2013': ['Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2014': ['Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2015': ['Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2016': ['Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2017': ['Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2018': ['Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'], 
            '2019': ['Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2020': ['Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2021': ['Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2022': ['Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2023': ['Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more']
        }
        
        labels = year_label_dict.get(year, "Year not found")
    else:
        # define dictionary 
        year_label_dict = {
            '2009': ['Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Percent!!Estimate!!INCOME AND BENEFITS (IN 2009 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2010': ['Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!Less than $10,000',
                     'Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$10,000 to $14,999',
                     'Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$15,000 to $24,999',
                     'Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$25,000 to $34,999',
                     'Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$35,000 to $49,999',
                     'Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$50,000 to $74,999',
                     'Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$75,000 to $99,999',
                     'Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$100,000 to $149,999',
                     'Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$150,000 to $199,999',
                     'Percent!!INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!$200,000 or more'],
            '2011': ['Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!Less than $10,000',
                     'Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$10,000 to $14,999',
                     'Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$15,000 to $24,999',
                     'Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$25,000 to $34,999',
                     'Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$35,000 to $49,999',
                     'Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$50,000 to $74,999',
                     'Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$75,000 to $99,999',
                     'Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$100,000 to $149,999',
                     'Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$150,000 to $199,999',
                     'Percent!!INCOME AND BENEFITS (IN 2011 INFLATION-ADJUSTED DOLLARS)!!$200,000 or more'],
            '2012': ['Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!Less than $10,000',
                     'Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$10,000 to $14,999',
                     'Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$15,000 to $24,999',
                     'Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$25,000 to $34,999',
                     'Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$35,000 to $49,999',
                     'Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$50,000 to $74,999',
                     'Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$75,000 to $99,999',
                     'Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$100,000 to $149,999',
                     'Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$150,000 to $199,999',
                     'Percent!!INCOME AND BENEFITS (IN 2012 INFLATION-ADJUSTED DOLLARS)!!$200,000 or more'],
            '2013': ['Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Percent!!INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2014': ['Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Percent!!INCOME AND BENEFITS (IN 2014 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2015': ['Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Percent!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2016': ['Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Percent!!INCOME AND BENEFITS (IN 2016 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2017': ['Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Percent Estimate!!INCOME AND BENEFITS (IN 2017 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2018': ['Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Percent Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'], 
            '2019': ['Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Percent!!INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2020': ['Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Percent!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2021': ['Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Percent!!INCOME AND BENEFITS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2022': ['Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Percent!!INCOME AND BENEFITS (IN 2022 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more'],
            '2023': ['Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!Less than $10,000',
                     'Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!$10,000 to $14,999',
                     'Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!$15,000 to $24,999',
                     'Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!$25,000 to $34,999',
                     'Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!$35,000 to $49,999',
                     'Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!$50,000 to $74,999',
                     'Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!$75,000 to $99,999',
                     'Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!$100,000 to $149,999',
                     'Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!$150,000 to $199,999',
                     'Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Families!!$200,000 or more']
        }
        
        labels = year_label_dict.get(year, "Year not found")
        
    # correct for years with multiple labels 
    if year in ['2010','2011','2012']:
        return_index = 1
    
    return get_demo_data('DP03', year, geo, labels,return_index)

def get_health_insurance_coverage(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2012']:
            labels = ['Estimate!!HEALTH INSURANCE COVERAGE!!With health insurance coverage!!With private health insurance',
                      'Estimate!!HEALTH INSURANCE COVERAGE!!With health insurance coverage!!With public coverage',
                      'Estimate!!HEALTH INSURANCE COVERAGE!!No health insurance coverage']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!With health insurance coverage!!With private health insurance',
                      'Estimate!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!With health insurance coverage!!With public coverage',
                      'Estimate!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!No health insurance coverage']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2012']:
            labels = ['Percent!!HEALTH INSURANCE COVERAGE!!With health insurance coverage!!With private health insurance',
                      'Percent!!HEALTH INSURANCE COVERAGE!!With health insurance coverage!!With public coverage',
                      'Percent!!HEALTH INSURANCE COVERAGE!!No health insurance coverage']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!With health insurance coverage!!With private health insurance',
                      'Percent!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!With health insurance coverage!!With public coverage',
                      'Percent!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!No health insurance coverage']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!With health insurance coverage!!With private health insurance',
                      'Percent Estimate!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!With health insurance coverage!!With public coverage',
                      'Percent Estimate!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!No health insurance coverage']
        else:
            print(f"Error: Unsupported year '{year}'")
            return None
        
    return get_demo_data('DP03', year, geo, labels)
        
    