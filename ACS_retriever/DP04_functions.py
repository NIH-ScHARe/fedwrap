from .census_API_wrapper import get_demo_data

def get_housing_occupancy(year,geo,as_percent=False):
    
    # set labels
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!HOUSING OCCUPANCY!!Total housing units!!Occupied housing units',
                      'Number!!Estimate!!HOUSING OCCUPANCY!!Total housing units!!Vacant housing units']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!HOUSING OCCUPANCY!!Occupied housing units',
                      'Estimate!!HOUSING OCCUPANCY!!Vacant housing units']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!HOUSING OCCUPANCY!!Total housing units!!Occupied housing units',
                      'Estimate!!HOUSING OCCUPANCY!!Total housing units!!Vacant housing units']
        else: 
            print(f"Error: Unsupported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!HOUSING OCCUPANCY!!Total housing units!!Occupied housing units',
                      'Percent!!Estimate!!HOUSING OCCUPANCY!!Total housing units!!Vacant housing units']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!HOUSING OCCUPANCY!!Occupied housing units',
                      'Percent!!HOUSING OCCUPANCY!!Vacant housing units']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!HOUSING OCCUPANCY!!Total housing units!!Occupied housing units',
                      'Percent!!HOUSING OCCUPANCY!!Total housing units!!Vacant housing units']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!HOUSING OCCUPANCY!!Total housing units!!Occupied housing units',
                      'Percent Estimate!!HOUSING OCCUPANCY!!Total housing units!!Vacant housing units']
        else: 
            print(f"Error: Unsupported year '{year}'")
            return None
    
    return get_demo_data('DP04',year,geo,labels)

def get_units_in_structure(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!UNITS IN STRUCTURE!!1-unit, detached',
                      'Number!!Estimate!!UNITS IN STRUCTURE!!1-unit, attached',
                      'Number!!Estimate!!UNITS IN STRUCTURE!!2 units',
                      'Number!!Estimate!!UNITS IN STRUCTURE!!3 or 4 units',
                      'Number!!Estimate!!UNITS IN STRUCTURE!!5 to 9 units',
                      'Number!!Estimate!!UNITS IN STRUCTURE!!10 to 19 units',
                      'Number!!Estimate!!UNITS IN STRUCTURE!!20 or more units',
                      'Number!!Estimate!!UNITS IN STRUCTURE!!Mobile home',
                      'Number!!Estimate!!UNITS IN STRUCTURE!!Boat, RV, van, etc.']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!UNITS IN STRUCTURE!!1-unit, detached',
                      'Estimate!!UNITS IN STRUCTURE!!1-unit, attached',
                      'Estimate!!UNITS IN STRUCTURE!!2 units',
                      'Estimate!!UNITS IN STRUCTURE!!3 or 4 units',
                      'Estimate!!UNITS IN STRUCTURE!!5 to 9 units',
                      'Estimate!!UNITS IN STRUCTURE!!10 to 19 units',
                      'Estimate!!UNITS IN STRUCTURE!!20 or more units',
                      'Estimate!!UNITS IN STRUCTURE!!Mobile home',
                      'Estimate!!UNITS IN STRUCTURE!!Boat, RV, van, etc.']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!UNITS IN STRUCTURE!!Total housing units!!1-unit, detached',
                      'Estimate!!UNITS IN STRUCTURE!!Total housing units!!1-unit, attached',
                      'Estimate!!UNITS IN STRUCTURE!!Total housing units!!2 units',
                      'Estimate!!UNITS IN STRUCTURE!!Total housing units!!3 or 4 units',
                      'Estimate!!UNITS IN STRUCTURE!!Total housing units!!5 to 9 units',
                      'Estimate!!UNITS IN STRUCTURE!!Total housing units!!10 to 19 units',
                      'Estimate!!UNITS IN STRUCTURE!!Total housing units!!20 or more units',
                      'Estimate!!UNITS IN STRUCTURE!!Total housing units!!Mobile home',
                      'Estimate!!UNITS IN STRUCTURE!!Total housing units!!Boat, RV, van, etc.']
        else:
            print(f"Error: supported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!UNITS IN STRUCTURE!!1-unit, detached',
                      'Percent!!Estimate!!UNITS IN STRUCTURE!!1-unit, attached',
                      'Percent!!Estimate!!UNITS IN STRUCTURE!!2 units',
                      'Percent!!Estimate!!UNITS IN STRUCTURE!!3 or 4 units',
                      'Percent!!Estimate!!UNITS IN STRUCTURE!!5 to 9 units',
                      'Percent!!Estimate!!UNITS IN STRUCTURE!!10 to 19 units',
                      'Percent!!Estimate!!UNITS IN STRUCTURE!!20 or more units',
                      'Percent!!Estimate!!UNITS IN STRUCTURE!!Mobile home',
                      'Percent!!Estimate!!UNITS IN STRUCTURE!!Boat, RV, van, etc.']
        elif year in ['2010','2011','2012']:
            labels = ['Percent!!UNITS IN STRUCTURE!!1-unit, detached',
                      'Percent!!UNITS IN STRUCTURE!!1-unit, attached',
                      'Percent!!UNITS IN STRUCTURE!!2 units',
                      'Percent!!UNITS IN STRUCTURE!!3 or 4 units',
                      'Percent!!UNITS IN STRUCTURE!!5 to 9 units',
                      'Percent!!UNITS IN STRUCTURE!!10 to 19 units',
                      'Percent!!UNITS IN STRUCTURE!!20 or more units',
                      'Percent!!UNITS IN STRUCTURE!!Mobile home',
                      'Percent!!UNITS IN STRUCTURE!!Boat, RV, van, etc.']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!UNITS IN STRUCTURE!!Total housing units!!1-unit, detached',
                      'Percent!!UNITS IN STRUCTURE!!Total housing units!!1-unit, attached',
                      'Percent!!UNITS IN STRUCTURE!!Total housing units!!2 units',
                      'Percent!!UNITS IN STRUCTURE!!Total housing units!!3 or 4 units',
                      'Percent!!UNITS IN STRUCTURE!!Total housing units!!5 to 9 units',
                      'Percent!!UNITS IN STRUCTURE!!Total housing units!!10 to 19 units',
                      'Percent!!UNITS IN STRUCTURE!!Total housing units!!20 or more units',
                      'Percent!!UNITS IN STRUCTURE!!Total housing units!!Mobile home',
                      'Percent!!UNITS IN STRUCTURE!!Total housing units!!Boat, RV, van, etc.']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!UNITS IN STRUCTURE!!Total housing units!!1-unit, detached',
                      'Percent Estimate!!UNITS IN STRUCTURE!!Total housing units!!1-unit, attached',
                      'Percent Estimate!!UNITS IN STRUCTURE!!Total housing units!!2 units',
                      'Percent Estimate!!UNITS IN STRUCTURE!!Total housing units!!3 or 4 units',
                      'Percent Estimate!!UNITS IN STRUCTURE!!Total housing units!!5 to 9 units',
                      'Percent Estimate!!UNITS IN STRUCTURE!!Total housing units!!10 to 19 units',
                      'Percent Estimate!!UNITS IN STRUCTURE!!Total housing units!!20 or more units',
                      'Percent Estimate!!UNITS IN STRUCTURE!!Total housing units!!Mobile home',
                      'Percent Estimate!!UNITS IN STRUCTURE!!Total housing units!!Boat, RV, van, etc.']
        else:
            print(f"Error: supported year '{year}'")
            return None
    
    return get_demo_data('DP04',year,geo,labels) 

def get_year_structure_built(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!YEAR STRUCTURE BUILT!!Built 2005 or later',
                      'Number!!Estimate!!YEAR STRUCTURE BUILT!!Built 2000 to 2004',
                      'Number!!Estimate!!YEAR STRUCTURE BUILT!!Built 1990 to 1999',
                      'Number!!Estimate!!YEAR STRUCTURE BUILT!!Built 1980 to 1989',
                      'Number!!Estimate!!YEAR STRUCTURE BUILT!!Built 1970 to 1979',
                      'Number!!Estimate!!YEAR STRUCTURE BUILT!!Built 1960 to 1969',
                      'Number!!Estimate!!YEAR STRUCTURE BUILT!!Built 1950 to 1959',
                      'Number!!Estimate!!YEAR STRUCTURE BUILT!!Built 1940 to 1949',
                      'Number!!Estimate!!YEAR STRUCTURE BUILT!!Built 1939 or earlier']
        elif year in ['2010','2011']:
            labels = ['Estimate!!YEAR STRUCTURE BUILT!!Built 2005 or later',
                      'Estimate!!YEAR STRUCTURE BUILT!!Built 2000 to 2004',
                      'Estimate!!YEAR STRUCTURE BUILT!!Built 1990 to 1999',
                      'Estimate!!YEAR STRUCTURE BUILT!!Built 1980 to 1989',
                      'Estimate!!YEAR STRUCTURE BUILT!!Built 1970 to 1979',
                      'Estimate!!YEAR STRUCTURE BUILT!!Built 1960 to 1969',
                      'Estimate!!YEAR STRUCTURE BUILT!!Built 1950 to 1959',
                      'Estimate!!YEAR STRUCTURE BUILT!!Built 1940 to 1949',
                      'Estimate!!YEAR STRUCTURE BUILT!!Built 1939 or earlier']
        elif year in ['2012']:
            labels = ['Estimate!!YEAR STRUCTURE BUILT!!Built 2010 or later',
                      'Estimate!!YEAR STRUCTURE BUILT!!Built 2000 to 2009',
                      'Estimate!!YEAR STRUCTURE BUILT!!Built 1990 to 1999',
                      'Estimate!!YEAR STRUCTURE BUILT!!Built 1980 to 1989',
                      'Estimate!!YEAR STRUCTURE BUILT!!Built 1970 to 1979',
                      'Estimate!!YEAR STRUCTURE BUILT!!Built 1960 to 1969',
                      'Estimate!!YEAR STRUCTURE BUILT!!Built 1950 to 1959',
                      'Estimate!!YEAR STRUCTURE BUILT!!Built 1940 to 1949',
                      'Estimate!!YEAR STRUCTURE BUILT!!Built 1939 or earlier']
        elif year in ['2013','2014']:
            labels = ['Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2010 or later',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2000 to 2009',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1990 to 1999',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1980 to 1989',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1970 to 1979',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1960 to 1969',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1950 to 1959',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1940 to 1949',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1939 or earlier']
        elif year in ['2015','2016','2017','2018','2019','2020']:
            labels = ['Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2014 or later',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2010 to 2013',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2000 to 2009',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1990 to 1999',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1980 to 1989',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1970 to 1979',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1960 to 1969',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1950 to 1959',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1940 to 1949',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1939 or earlier']
        elif year in ['2021','2022','2023']:
            labels = ['Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2020 or later',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2010 to 2019',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2000 to 2009',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1990 to 1999',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1980 to 1989',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1970 to 1979',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1960 to 1969',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1950 to 1959',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1940 to 1949',
                      'Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1939 or earlier']
        else:
            print(f"Error: supported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!YEAR STRUCTURE BUILT!!Built 2005 or later',
                      'Percent!!Estimate!!YEAR STRUCTURE BUILT!!Built 2000 to 2004',
                      'Percent!!Estimate!!YEAR STRUCTURE BUILT!!Built 1990 to 1999',
                      'Percent!!Estimate!!YEAR STRUCTURE BUILT!!Built 1980 to 1989',
                      'Percent!!Estimate!!YEAR STRUCTURE BUILT!!Built 1970 to 1979',
                      'Percent!!Estimate!!YEAR STRUCTURE BUILT!!Built 1960 to 1969',
                      'Percent!!Estimate!!YEAR STRUCTURE BUILT!!Built 1950 to 1959',
                      'Percent!!Estimate!!YEAR STRUCTURE BUILT!!Built 1940 to 1949',
                      'Percent!!Estimate!!YEAR STRUCTURE BUILT!!Built 1939 or earlier']
        elif year in ['2010','2011']:
            labels = ['Percent!!YEAR STRUCTURE BUILT!!Built 2005 or later',
                      'Percent!!YEAR STRUCTURE BUILT!!Built 2000 to 2004',
                      'Percent!!YEAR STRUCTURE BUILT!!Built 1990 to 1999',
                      'Percent!!YEAR STRUCTURE BUILT!!Built 1980 to 1989',
                      'Percent!!YEAR STRUCTURE BUILT!!Built 1970 to 1979',
                      'Percent!!YEAR STRUCTURE BUILT!!Built 1960 to 1969',
                      'Percent!!YEAR STRUCTURE BUILT!!Built 1950 to 1959',
                      'Percent!!YEAR STRUCTURE BUILT!!Built 1940 to 1949',
                      'Percent!!YEAR STRUCTURE BUILT!!Built 1939 or earlier']
        elif year in ['2012']:
            labels = ['Percent!!YEAR STRUCTURE BUILT!!Built 2010 or later',
                      'Percent!!YEAR STRUCTURE BUILT!!Built 2000 to 2009',
                      'Percent!!YEAR STRUCTURE BUILT!!Built 1990 to 1999',
                      'Percent!!YEAR STRUCTURE BUILT!!Built 1980 to 1989',
                      'Percent!!YEAR STRUCTURE BUILT!!Built 1970 to 1979',
                      'Percent!!YEAR STRUCTURE BUILT!!Built 1960 to 1969',
                      'Percent!!YEAR STRUCTURE BUILT!!Built 1950 to 1959',
                      'Percent!!YEAR STRUCTURE BUILT!!Built 1940 to 1949',
                      'Percent!!YEAR STRUCTURE BUILT!!Built 1939 or earlier']
        elif year in ['2013','2014']:
            labels = ['Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2010 or later',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2000 to 2009',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1990 to 1999',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1980 to 1989',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1970 to 1979',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1960 to 1969',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1950 to 1959',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1940 to 1949',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1939 or earlier']
        elif year in ['2015','2016']:
            labels = ['Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2014 or later',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2010 to 2013',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2000 to 2009',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1990 to 1999',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1980 to 1989',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1970 to 1979',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1960 to 1969',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1950 to 1959',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1940 to 1949',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1939 or earlier']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2014 or later',
                      'Percent Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2010 to 2013',
                      'Percent Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2000 to 2009',
                      'Percent Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1990 to 1999',
                      'Percent Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1980 to 1989',
                      'Percent Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1970 to 1979',
                      'Percent Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1960 to 1969',
                      'Percent Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1950 to 1959',
                      'Percent Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1940 to 1949',
                      'Percent Estimate!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1939 or earlier']
        elif year in ['2019','2020']:
            labels = ['Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2014 or later',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2010 to 2013',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2000 to 2009',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1990 to 1999',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1980 to 1989',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1970 to 1979',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1960 to 1969',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1950 to 1959',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1940 to 1949',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1939 or earlier']
        elif year in ['2021','2022','2023']:
            labels = ['Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2020 or later',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2010 to 2019',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 2000 to 2009',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1990 to 1999',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1980 to 1989',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1970 to 1979',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1960 to 1969',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1950 to 1959',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1940 to 1949',
                      'Percent!!YEAR STRUCTURE BUILT!!Total housing units!!Built 1939 or earlier']
        else:
            print(f"Error: supported year '{year}'")
            return None
    
    return get_demo_data('DP04',year,geo,labels) 

def get_rooms(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!ROOMS!!1 room',
                      'Number!!Estimate!!ROOMS!!2 rooms',
                      'Number!!Estimate!!ROOMS!!3 rooms',
                      'Number!!Estimate!!ROOMS!!4 rooms',
                      'Number!!Estimate!!ROOMS!!5 rooms',
                      'Number!!Estimate!!ROOMS!!6 rooms',
                      'Number!!Estimate!!ROOMS!!7 rooms',
                      'Number!!Estimate!!ROOMS!!8 rooms',
                      'Number!!Estimate!!ROOMS!!9 rooms or more']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!ROOMS!!1 room',
                      'Estimate!!ROOMS!!2 rooms',
                      'Estimate!!ROOMS!!3 rooms',
                      'Estimate!!ROOMS!!4 rooms',
                      'Estimate!!ROOMS!!5 rooms',
                      'Estimate!!ROOMS!!6 rooms',
                      'Estimate!!ROOMS!!7 rooms',
                      'Estimate!!ROOMS!!8 rooms',
                      'Estimate!!ROOMS!!9 rooms or more']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!ROOMS!!Total housing units!!1 room',
                      'Estimate!!ROOMS!!Total housing units!!2 rooms',
                      'Estimate!!ROOMS!!Total housing units!!3 rooms',
                      'Estimate!!ROOMS!!Total housing units!!4 rooms',
                      'Estimate!!ROOMS!!Total housing units!!5 rooms',
                      'Estimate!!ROOMS!!Total housing units!!6 rooms',
                      'Estimate!!ROOMS!!Total housing units!!7 rooms',
                      'Estimate!!ROOMS!!Total housing units!!8 rooms',
                      'Estimate!!ROOMS!!Total housing units!!9 rooms or more']
        else:
            print(f"Error: supported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!ROOMS!!1 room',
                      'Percent!!Estimate!!ROOMS!!2 rooms',
                      'Percent!!Estimate!!ROOMS!!3 rooms',
                      'Percent!!Estimate!!ROOMS!!4 rooms',
                      'Percent!!Estimate!!ROOMS!!5 rooms',
                      'Percent!!Estimate!!ROOMS!!6 rooms',
                      'Percent!!Estimate!!ROOMS!!7 rooms',
                      'Percent!!Estimate!!ROOMS!!8 rooms',
                      'Percent!!Estimate!!ROOMS!!9 rooms or more']
        elif year in ['2010','2011','2012']: 
            labels = ['Percent!!ROOMS!!1 room',
                      'Percent!!ROOMS!!2 rooms',
                      'Percent!!ROOMS!!3 rooms',
                      'Percent!!ROOMS!!4 rooms',
                      'Percent!!ROOMS!!5 rooms',
                      'Percent!!ROOMS!!6 rooms',
                      'Percent!!ROOMS!!7 rooms',
                      'Percent!!ROOMS!!8 rooms',
                      'Percent!!ROOMS!!9 rooms or more']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!ROOMS!!Total housing units!!1 room',
                      'Percent!!ROOMS!!Total housing units!!2 rooms',
                      'Percent!!ROOMS!!Total housing units!!3 rooms',
                      'Percent!!ROOMS!!Total housing units!!4 rooms',
                      'Percent!!ROOMS!!Total housing units!!5 rooms',
                      'Percent!!ROOMS!!Total housing units!!6 rooms',
                      'Percent!!ROOMS!!Total housing units!!7 rooms',
                      'Percent!!ROOMS!!Total housing units!!8 rooms',
                      'Percent!!ROOMS!!Total housing units!!9 rooms or more']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!ROOMS!!Total housing units!!1 room',
                      'Percent Estimate!!ROOMS!!Total housing units!!2 rooms',
                      'Percent Estimate!!ROOMS!!Total housing units!!3 rooms',
                      'Percent Estimate!!ROOMS!!Total housing units!!4 rooms',
                      'Percent Estimate!!ROOMS!!Total housing units!!5 rooms',
                      'Percent Estimate!!ROOMS!!Total housing units!!6 rooms',
                      'Percent Estimate!!ROOMS!!Total housing units!!7 rooms',
                      'Percent Estimate!!ROOMS!!Total housing units!!8 rooms',
                      'Percent Estimate!!ROOMS!!Total housing units!!9 rooms or more']
        else:
            print(f"Error: supported year '{year}'")
            return None
    
    return get_demo_data('DP04',year,geo,labels) 

def get_bedrooms(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!BEDROOMS!!No bedroom',
                      'Number!!Estimate!!BEDROOMS!!1 bedroom',
                      'Number!!Estimate!!BEDROOMS!!2 bedrooms',
                      'Number!!Estimate!!BEDROOMS!!3 bedrooms',
                      'Number!!Estimate!!BEDROOMS!!4 bedrooms',
                      'Number!!Estimate!!BEDROOMS!!5 or more bedrooms']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!BEDROOMS!!No bedroom',
                      'Estimate!!BEDROOMS!!1 bedroom',
                      'Estimate!!BEDROOMS!!2 bedrooms',
                      'Estimate!!BEDROOMS!!3 bedrooms',
                      'Estimate!!BEDROOMS!!4 bedrooms',
                      'Estimate!!BEDROOMS!!5 or more bedrooms']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!BEDROOMS!!Total housing units!!No bedroom',
                      'Estimate!!BEDROOMS!!Total housing units!!1 bedroom',
                      'Estimate!!BEDROOMS!!Total housing units!!2 bedrooms',
                      'Estimate!!BEDROOMS!!Total housing units!!3 bedrooms',
                      'Estimate!!BEDROOMS!!Total housing units!!4 bedrooms',
                      'Estimate!!BEDROOMS!!Total housing units!!5 or more bedrooms']
        else:
            print(f"Error: supported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!BEDROOMS!!No bedroom',
                      'Percent!!Estimate!!BEDROOMS!!1 bedroom',
                      'Percent!!Estimate!!BEDROOMS!!2 bedrooms',
                      'Percent!!Estimate!!BEDROOMS!!3 bedrooms',
                      'Percent!!Estimate!!BEDROOMS!!4 bedrooms',
                      'Percent!!Estimate!!BEDROOMS!!5 or more bedrooms']
        elif year in ['2010','2011','2012']: 
            labels = ['Percent!!BEDROOMS!!No bedroom',
                      'Percent!!BEDROOMS!!1 bedroom',
                      'Percent!!BEDROOMS!!2 bedrooms',
                      'Percent!!BEDROOMS!!3 bedrooms',
                      'Percent!!BEDROOMS!!4 bedrooms',
                      'Percent!!BEDROOMS!!5 or more bedrooms']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!BEDROOMS!!Total housing units!!No bedroom',
                      'Percent!!BEDROOMS!!Total housing units!!1 bedroom',
                      'Percent!!BEDROOMS!!Total housing units!!2 bedrooms',
                      'Percent!!BEDROOMS!!Total housing units!!3 bedrooms',
                      'Percent!!BEDROOMS!!Total housing units!!4 bedrooms',
                      'Percent!!BEDROOMS!!Total housing units!!5 or more bedrooms']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!BEDROOMS!!Total housing units!!No bedroom',
                      'Percent Estimate!!BEDROOMS!!Total housing units!!1 bedroom',
                      'Percent Estimate!!BEDROOMS!!Total housing units!!2 bedrooms',
                      'Percent Estimate!!BEDROOMS!!Total housing units!!3 bedrooms',
                      'Percent Estimate!!BEDROOMS!!Total housing units!!4 bedrooms',
                      'Percent Estimate!!BEDROOMS!!Total housing units!!5 or more bedrooms']
        else:
            print(f"Error: supported year '{year}'")
            return None
    
    return get_demo_data('DP04',year,geo,labels) 

def get_housing_tenure(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!HOUSING TENURE!!Occupied housing units!!Owner-occupied',
                      'Number!!Estimate!!HOUSING TENURE!!Occupied housing units!!Renter-occupied']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!HOUSING TENURE!!Owner-occupied',
                      'Estimate!!HOUSING TENURE!!Renter-occupied']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!HOUSING TENURE!!Occupied housing units!!Owner-occupied',
                      'Estimate!!HOUSING TENURE!!Occupied housing units!!Renter-occupied']
        else:
            print(f"Error: supported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!HOUSING TENURE!!Occupied housing units!!Owner-occupied',
                      'Percent!!Estimate!!HOUSING TENURE!!Occupied housing units!!Renter-occupied']
        elif year in ['2010','2011','2012']: 
            labels = ['Percent!!HOUSING TENURE!!Owner-occupied',
                      'Percent!!HOUSING TENURE!!Renter-occupied']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!HOUSING TENURE!!Occupied housing units!!Owner-occupied',
                      'Percent!!HOUSING TENURE!!Occupied housing units!!Renter-occupied']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!HOUSING TENURE!!Occupied housing units!!Owner-occupied',
                      'Percent Estimate!!HOUSING TENURE!!Occupied housing units!!Renter-occupied']
        else:
            print(f"Error: supported year '{year}'")
            return None
    
    return get_demo_data('DP04',year,geo,labels) 


def get_year_householder_moved_into_unit(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2005 or later',
                      'Number!!Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2000 to 2004',
                      'Number!!Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1990 to 1999',
                      'Number!!Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1980 to 1989',
                      'Number!!Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1970 to 1979',
                      'Number!!Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1969 or earlier']
        elif year in ['2010','2011']:
            labels = ['Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 2005 or later',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 2000 to 2004',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 1990 to 1999',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 1980 to 1989',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 1970 to 1979',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 1969 or earlier']
        elif year in ['2012']:
            labels = ['Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 2010 or later',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 2000 to 2009',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 1990 to 1999',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 1980 to 1989',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 1970 to 1979',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 1969 or earlier']
        elif year in ['2013','2014']:
            labels = ['Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2010 or later',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2000 to 2009',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1990 to 1999',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1980 to 1989',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1970 to 1979',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1969 or earlier']
        elif year in ['2015','2016','2017']:
            labels = ['Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2015 or later',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2010 to 2014',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2000 to 2009',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1990 to 1999',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1980 to 1989',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1979 and earlier']
        elif year in ['2018','2019']:
            labels = ['Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2017 or later',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2015 to 2016',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2010 to 2014',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2000 to 2009',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1990 to 1999',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1989 and earlier']
        elif year in ['2020','2021']:
            labels = ['Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2019 or later',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2015 to 2018',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2010 to 2014',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2000 to 2009',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1990 to 1999',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1989 and earlier']
        elif year in ['2022','2023']:
            labels = ['Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2021 or later',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2018 to 2020',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2010 to 2017',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2000 to 2009',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1990 to 1999',
                      'Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1989 and earlier']
        else:
            print(f"Error: supported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2005 or later',
                      'Percent!!Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2000 to 2004',
                      'Percent!!Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1990 to 1999',
                      'Percent!!Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1980 to 1989',
                      'Percent!!Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1970 to 1979',
                      'Percent!!Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1969 or earlier']
        elif year in ['2010','2011']: 
            labels = ['Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 2005 or later',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 2000 to 2004',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 1990 to 1999',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 1980 to 1989',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 1970 to 1979',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 1969 or earlier']
        elif year in ['2012']:
            labels = ['Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 2010 or later',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 2000 to 2009',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 1990 to 1999',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 1980 to 1989',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 1970 to 1979',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Moved in 1969 or earlier']
        elif year in ['2013','2014']:
            labels = ['Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2010 or later',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2000 to 2009',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1990 to 1999',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1980 to 1989',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1970 to 1979',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1969 or earlier']
        elif year in ['2015','2016']:
            labels = ['Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2015 or later',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2010 to 2014',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2000 to 2009',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1990 to 1999',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1980 to 1989',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1979 and earlier']
        elif year in ['2017']:
            labels = ['Percent Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2015 or later',
                      'Percent Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2010 to 2014',
                      'Percent Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2000 to 2009',
                      'Percent Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1990 to 1999',
                      'Percent Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1980 to 1989',
                      'Percent Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1979 and earlier']
        elif year in ['2018']:
            labels = ['Percent Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2017 or later',
                      'Percent Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2015 to 2016',
                      'Percent Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2010 to 2014',
                      'Percent Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2000 to 2009',
                      'Percent Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1990 to 1999',
                      'Percent Estimate!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1989 and earlier']
        elif year in ['2019']:
            labels = ['Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2017 or later',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2015 to 2016',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2010 to 2014',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2000 to 2009',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1990 to 1999',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1989 and earlier']
        elif year in ['2020','2021']:
            labels = ['Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2019 or later',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2015 to 2018',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2010 to 2014',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2000 to 2009',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1990 to 1999',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1989 and earlier']
        elif year in ['2022','2023']:
            labels = ['Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2021 or later',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2018 to 2020',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2010 to 2017',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 2000 to 2009',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1990 to 1999',
                      'Percent!!YEAR HOUSEHOLDER MOVED INTO UNIT!!Occupied housing units!!Moved in 1989 and earlier']
        else:
            print(f"Error: supported year '{year}'")
            return None
    
    return get_demo_data('DP04',year,geo,labels) 

def get_vehicles_available(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!VEHICLES AVAILABLE!!Occupied housing units!!No vehicles available',
                      'Number!!Estimate!!VEHICLES AVAILABLE!!Occupied housing units!!1 vehicle available',
                      'Number!!Estimate!!VEHICLES AVAILABLE!!Occupied housing units!!2 vehicles available',
                      'Number!!Estimate!!VEHICLES AVAILABLE!!Occupied housing units!!3 or more vehicles available']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!VEHICLES AVAILABLE!!No vehicles available',
                      'Estimate!!VEHICLES AVAILABLE!!1 vehicle available',
                      'Estimate!!VEHICLES AVAILABLE!!2 vehicles available',
                      'Estimate!!VEHICLES AVAILABLE!!3 or more vehicles available']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!VEHICLES AVAILABLE!!Occupied housing units!!No vehicles available',
                      'Estimate!!VEHICLES AVAILABLE!!Occupied housing units!!1 vehicle available',
                      'Estimate!!VEHICLES AVAILABLE!!Occupied housing units!!2 vehicles available',
                      'Estimate!!VEHICLES AVAILABLE!!Occupied housing units!!3 or more vehicles available']
        else:
            print(f"Error: supported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!VEHICLES AVAILABLE!!Occupied housing units!!No vehicles available',
                      'Percent!!Estimate!!VEHICLES AVAILABLE!!Occupied housing units!!1 vehicle available',
                      'Percent!!Estimate!!VEHICLES AVAILABLE!!Occupied housing units!!2 vehicles available',
                      'Percent!!Estimate!!VEHICLES AVAILABLE!!Occupied housing units!!3 or more vehicles available']
        elif year in ['2010','2011','2012']: 
            labels = ['Percent!!VEHICLES AVAILABLE!!No vehicles available',
                      'Percent!!VEHICLES AVAILABLE!!1 vehicle available',
                      'Percent!!VEHICLES AVAILABLE!!2 vehicles available',
                      'Percent!!VEHICLES AVAILABLE!!3 or more vehicles available']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!VEHICLES AVAILABLE!!Occupied housing units!!No vehicles available',
                      'Percent!!VEHICLES AVAILABLE!!Occupied housing units!!1 vehicle available',
                      'Percent!!VEHICLES AVAILABLE!!Occupied housing units!!2 vehicles available',
                      'Percent!!VEHICLES AVAILABLE!!Occupied housing units!!3 or more vehicles available']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!VEHICLES AVAILABLE!!Occupied housing units!!No vehicles available',
                      'Percent Estimate!!VEHICLES AVAILABLE!!Occupied housing units!!1 vehicle available',
                      'Percent Estimate!!VEHICLES AVAILABLE!!Occupied housing units!!2 vehicles available',
                      'Percent Estimate!!VEHICLES AVAILABLE!!Occupied housing units!!3 or more vehicles available']
        else:
            print(f"Error: supported year '{year}'")
            return None
    
    return get_demo_data('DP04',year,geo,labels) 

def get_house_heating_fuel(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Utility gas',
                      'Number!!Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Bottled, tank, or LP gas',
                      'Number!!Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Electricity',
                      'Number!!Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Fuel oil, kerosene, etc.',
                      'Number!!Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Coal or coke',
                      'Number!!Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Wood',
                      'Number!!Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Solar energy',
                      'Number!!Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Other fuel',
                      'Number!!Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!No fuel used']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!HOUSE HEATING FUEL!!Utility gas',
                      'Estimate!!HOUSE HEATING FUEL!!Bottled, tank, or LP gas',
                      'Estimate!!HOUSE HEATING FUEL!!Electricity',
                      'Estimate!!HOUSE HEATING FUEL!!Fuel oil, kerosene, etc.',
                      'Estimate!!HOUSE HEATING FUEL!!Coal or coke',
                      'Estimate!!HOUSE HEATING FUEL!!Wood',
                      'Estimate!!HOUSE HEATING FUEL!!Solar energy',
                      'Estimate!!HOUSE HEATING FUEL!!Other fuel',
                      'Estimate!!HOUSE HEATING FUEL!!No fuel used']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Utility gas',
                      'Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Bottled, tank, or LP gas',
                      'Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Electricity',
                      'Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Fuel oil, kerosene, etc.',
                      'Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Coal or coke',
                      'Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Wood',
                      'Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Solar energy',
                      'Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Other fuel',
                      'Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!No fuel used']
        else:
            print(f"Error: supported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Utility gas',
                      'Percent!!Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Bottled, tank, or LP gas',
                      'Percent!!Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Electricity',
                      'Percent!!Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Fuel oil, kerosene, etc.',
                      'Percent!!Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Coal or coke',
                      'Percent!!Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Wood',
                      'Percent!!Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Solar energy',
                      'Percent!!Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Other fuel',
                      'Percent!!Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!No fuel used']
        elif year in ['2010','2011','2012']: 
            labels = ['Percent!!HOUSE HEATING FUEL!!Utility gas',
                      'Percent!!HOUSE HEATING FUEL!!Bottled, tank, or LP gas',
                      'Percent!!HOUSE HEATING FUEL!!Electricity',
                      'Percent!!HOUSE HEATING FUEL!!Fuel oil, kerosene, etc.',
                      'Percent!!HOUSE HEATING FUEL!!Coal or coke',
                      'Percent!!HOUSE HEATING FUEL!!Wood',
                      'Percent!!HOUSE HEATING FUEL!!Solar energy',
                      'Percent!!HOUSE HEATING FUEL!!Other fuel',
                      'Percent!!HOUSE HEATING FUEL!!No fuel used']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!HOUSE HEATING FUEL!!Occupied housing units!!Utility gas',
                      'Percent!!HOUSE HEATING FUEL!!Occupied housing units!!Bottled, tank, or LP gas',
                      'Percent!!HOUSE HEATING FUEL!!Occupied housing units!!Electricity',
                      'Percent!!HOUSE HEATING FUEL!!Occupied housing units!!Fuel oil, kerosene, etc.',
                      'Percent!!HOUSE HEATING FUEL!!Occupied housing units!!Coal or coke',
                      'Percent!!HOUSE HEATING FUEL!!Occupied housing units!!Wood',
                      'Percent!!HOUSE HEATING FUEL!!Occupied housing units!!Solar energy',
                      'Percent!!HOUSE HEATING FUEL!!Occupied housing units!!Other fuel',
                      'Percent!!HOUSE HEATING FUEL!!Occupied housing units!!No fuel used']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Utility gas',
                      'Percent Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Bottled, tank, or LP gas',
                      'Percent Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Electricity',
                      'Percent Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Fuel oil, kerosene, etc.',
                      'Percent Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Coal or coke',
                      'Percent Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Wood',
                      'Percent Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Solar energy',
                      'Percent Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!Other fuel',
                      'Percent Estimate!!HOUSE HEATING FUEL!!Occupied housing units!!No fuel used']
        else:
            print(f"Error: supported year '{year}'")
            return None
    
    return get_demo_data('DP04',year,geo,labels) 

def get_housing_lacking_complete_plumbing_facilities(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!SELECTED CHARACTERISTICS!!Occupied housing units!!Lacking complete plumbing facilities']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!SELECTED CHARACTERISTICS!!Lacking complete plumbing facilities']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!SELECTED CHARACTERISTICS!!Occupied housing units!!Lacking complete plumbing facilities']
        else:
            print(f"Error: supported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!SELECTED CHARACTERISTICS!!Occupied housing units!!Lacking complete plumbing facilities']
        elif year in ['2010','2011','2012']: 
            labels = ['Percent!!SELECTED CHARACTERISTICS!!Lacking complete plumbing facilities']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!SELECTED CHARACTERISTICS!!Occupied housing units!!Lacking complete plumbing facilities']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!SELECTED CHARACTERISTICS!!Occupied housing units!!Lacking complete plumbing facilities']
        else:
            print(f"Error: supported year '{year}'")
            return None
    
    return get_demo_data('DP04',year,geo,labels) 

def get_housing_lacking_complete_kitchen_facilities(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!SELECTED CHARACTERISTICS!!Occupied housing units!!Lacking complete kitchen facilities']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!SELECTED CHARACTERISTICS!!Lacking complete kitchen facilities']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!SELECTED CHARACTERISTICS!!Occupied housing units!!Lacking complete kitchen facilities']
        else:
            print(f"Error: supported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!SELECTED CHARACTERISTICS!!Occupied housing units!!Lacking complete kitchen facilities']
        elif year in ['2010','2011','2012']: 
            labels = ['Percent!!SELECTED CHARACTERISTICS!!Lacking complete kitchen facilities']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!SELECTED CHARACTERISTICS!!Occupied housing units!!Lacking complete kitchen facilities']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!SELECTED CHARACTERISTICS!!Occupied housing units!!Lacking complete kitchen facilities']
        else:
            print(f"Error: supported year '{year}'")
            return None
    
    return get_demo_data('DP04',year,geo,labels) 

def get_housing_no_telephone_service_available(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!SELECTED CHARACTERISTICS!!Occupied housing units!!No telephone service available']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!SELECTED CHARACTERISTICS!!No telephone service available']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!SELECTED CHARACTERISTICS!!Occupied housing units!!No telephone service available']
        else:
            print(f"Error: supported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!SELECTED CHARACTERISTICS!!Occupied housing units!!No telephone service available']
        elif year in ['2010','2011','2012']: 
            labels = ['Percent!!SELECTED CHARACTERISTICS!!No telephone service available']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!SELECTED CHARACTERISTICS!!Occupied housing units!!No telephone service available']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!SELECTED CHARACTERISTICS!!Occupied housing units!!No telephone service available']
        else:
            print(f"Error: supported year '{year}'")
            return None
    
    return get_demo_data('DP04',year,geo,labels) 

def get_occupants_per_room(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2009']:
            labels = ['Number!!Estimate!!OCCUPANTS PER ROOM!!Occupied housing units!!1.00 or less',
                      'Number!!Estimate!!OCCUPANTS PER ROOM!!Occupied housing units!!1.01 to 1.50',
                      'Number!!Estimate!!OCCUPANTS PER ROOM!!Occupied housing units!!1.51 or more']
        elif year in ['2010','2011','2012']:
            labels = ['Estimate!!OCCUPANTS PER ROOM!!1.00 or less',
                      'Estimate!!OCCUPANTS PER ROOM!!1.01 to 1.50',
                      'Estimate!!OCCUPANTS PER ROOM!!1.51 or more']
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = ['Estimate!!OCCUPANTS PER ROOM!!Occupied housing units!!1.00 or less',
                      'Estimate!!OCCUPANTS PER ROOM!!Occupied housing units!!1.01 to 1.50',
                      'Estimate!!OCCUPANTS PER ROOM!!Occupied housing units!!1.51 or more']
        else:
            print(f"Error: supported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = ['Percent!!Estimate!!OCCUPANTS PER ROOM!!Occupied housing units!!1.00 or less',
                      'Percent!!Estimate!!OCCUPANTS PER ROOM!!Occupied housing units!!1.01 to 1.50',
                      'Percent!!Estimate!!OCCUPANTS PER ROOM!!Occupied housing units!!1.51 or more']
        elif year in ['2010','2011','2012']: 
            labels = ['Percent!!OCCUPANTS PER ROOM!!1.00 or less',
                      'Percent!!OCCUPANTS PER ROOM!!1.01 to 1.50',
                      'Percent!!OCCUPANTS PER ROOM!!1.51 or more']
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = ['Percent!!OCCUPANTS PER ROOM!!Occupied housing units!!1.00 or less',
                      'Percent!!OCCUPANTS PER ROOM!!Occupied housing units!!1.01 to 1.50',
                      'Percent!!OCCUPANTS PER ROOM!!Occupied housing units!!1.51 or more']
        elif year in ['2017','2018']:
            labels = ['Percent Estimate!!OCCUPANTS PER ROOM!!Occupied housing units!!1.00 or less',
                      'Percent Estimate!!OCCUPANTS PER ROOM!!Occupied housing units!!1.01 to 1.50',
                      'Percent Estimate!!OCCUPANTS PER ROOM!!Occupied housing units!!1.51 or more']
        else:
            print(f"Error: supported year '{year}'")
            return None
    
    return get_demo_data('DP04',year,geo,labels) 

def get_data(year,geo,as_percent=False):
    
    # set labels 
    if not as_percent:
        if year in ['2009']:
            labels = []
        elif year in ['2010','2011','2012']:
            labels = []
        elif year in ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']:
            labels = []
        else:
            print(f"Error: supported year '{year}'")
            return None
    else:
        if year in ['2009']:
            labels = []
        elif year in ['2010','2011','2012']: 
            labels = []
        elif year in ['2013','2014','2015','2016','2019','2020','2021','2022','2023']:
            labels = []
        elif year in ['2017','2018']:
            labels = []
        else:
            print(f"Error: supported year '{year}'")
            return None
    
    return get_demo_data('DP04',year,geo,labels) 