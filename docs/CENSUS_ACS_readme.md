🧭 **Overivew** 

A Python wrapper for the U.S. Census Bureau’s American Community Survey (ACS) API. Simplifies fetching ACS datasets such as population, housing, income, and education.

🛠️ **Installation** 

```bash
pip install fedwrap
```

📝 **Instructions**

Calls to the census_acs occurs through functions for each variable in the ACS dataset. The basic structure of a call is: 

```python
get_acs_data(MEASUREID,YEAR,GEO,as_percent)
```
**Years**

The years of the American Communities Survey accessible by API range from 2009 - 2023. 

**Geography**

The following geographical gradations are supported:
- state
- county
- census tract
- zip code
- congressional district 

**Absolute values versus percentage**

The census_acs wrapper is designed to return either absolute values or relative percentages for all variables. The default is absolute, as would be returned by: 

```python
get_acs_data('TOTAL_POP','2023','state')
```

To get the relative amounts for the values of any variable, set the 'as_percent' parameter to True: 

```python
get_acs_data('TOTAL_POP','2023','state',as_percent=True)
```


**Table of MEASUREIDs and Functions**

| Measure ID | Function |
|-|-|
HOUSEHOLD_TYPE | get_household_type|
HOUSEHOLD_RELATIONSHIP|get_household_relationship|
MALE_MARITAL_STATUS|get_male_marital_status|
FEMALE_MARITAL_STATUS|get_female_marital_status|
SCHOOL_ENROLLMENT|get_school_enrollment|
EDUCATIONAL_ATTAINMENT|get_educational_attainment|
VETERAN_STATUS|get_veteran_status|
RESIDENCE_YEAR_AGO|get_residence_year_ago|
PLACE_OF_BIRTH|get_place_of_birth|
US_CITIZENSHIP_STATUS|get_US_citizenship_status|
WORLD_REGION_OF_BIRTH_OF_FOREIGN_BORN|get_world_region_of_birth_of_foreign_born|
LANGUAGE_SPOKEN_AT_HOME|get_language_spoken_at_home|
ANCESTRY|get_ancestry|
COMPUTER_AND_INTERNET_USE|get_computer_and_internet_use|
EMPLOYMENT_STATUS|get_employment_status|
COMMUTING_TO_WORK|get_commuting_to_work|
OCCUPATION|get_occupation|
INDUSTRY|get_industry|
CLASS_OF_WORKER|get_class_of_worker|
HOUSEHOLD_INCOME|get_household_income|
HOUSEHOLDS_WITH_EARNINGS|get_households_with_earnings|
HOUSEHOLDS_WITH_SOCIAL_SECURITY|get_households_with_social_security|
HOUSEHOLDS_WITH_RETIREMENT_INCOME|get_households_with_retirement_income|
HOUSEHOLDS_WITH_SUPPLEMENTAL_SECURITY_INCOME|get_households_with_supplemental_security_income|
HOUSEHOLDS_WITH_CASH_PUBLIC_ASSISTANCE_INCOME|get_households_with_cash_public_assistance_income|
HOUSEHOLDS_WITH_SNAP_BENEFITS|get_households_with_SNAP_benefits|
FAMILY_INCOME|get_family_income|
HEALTH_INSURANCE_COVERAGE|get_health_insurance_coverage|
HOUSING_OCCUPANCY|get_housing_occupancy|
UNITS_IN_STRUCTURE|get_units_in_structure|
YEAR_STRUCTURE_BUILT|get_year_structure_built|
ROOMS|get_rooms|
BEDROOMS|get_bedrooms|
HOUSING_TENURE|get_housing_tenure|
YEAR_HOUSEHOLDER_MOVED_INTO_UNIT|get_year_householder_moved_into_unit|
VEHICLES_AVAILABLE|get_vehicles_available|
HOUSE_HEATING_FUEL|get_house_heating_fuel|
HOUSING_LACKING_COMPLETE_PLUMBING_FACILITIES|get_housing_lacking_complete_plumbing_facilities|
HOUSING_LACKING_COMPLETE_KITCHEN_FACILITIES|get_housing_lacking_complete_kitchen_facilities|
HOUSING_NO_TELEPHONE_SERVICE_AVAILABLE|get_housing_no_telephone_service_available|
OCCUPANTS_PER_ROOM|get_occupants_per_room|
HOUSING_VALUE|get_housing_value|
MORTGAGE_STATUS|get_mortgage_status|
SELECTED_MONTHLY_OWNER_COSTS_WITH_MORTGAGE|get_selected_monthly_owner_costs_with_mortgage|
SELECTED_MONTHLY_OWNER_COSTS_WITHOUT_MORTGAGE|get_selected_monthly_owner_costs_without_mortgage|
SMOCAPI_WITH_MORTGAGE|get_SMOCAPI_with_mortgage|
SMOCAPI_WITHOUT_MORTGAGE|get_SMOCAPI_without_mortgage|
GROSS_RENT|get_gross_rent|
GRAPI|get_GRAPI|
TOTAL_POP|get_total_pop|
POP_SEX|get_pop_sex|
AGE|get_age|
RACE|get_race|

**List of Values**

Household Type (*get_household_type*()) 
- Married-couple household
- Cohabiting couple household
- Male householder, no spouse/partner present
- Female householder, no spouse/partner present

Household Relationship (*get_household_relationship*())
- Householder
- Spouse
- Unmarried partner
- Child
- Other relatives
- Nonrelatives

Male Marital Status (*get_male_marital_status*())
- Never married
- Now married, except separated
- Separated
- Widowed
- Divorced

Female Martial Status (*get_female_marital_status*())
- Never married
- Now married, except separated
- Separated
- Widowed
- Divorced

School Enrollment (*get_school_enrollment*())
- Nursery school, preschool
- Kindergarten
- Elementary school (grades 1-8)
- High school (grades 9-12)
- College or graduate school

Educational Attainment (*get_educational_attainment*())
- Less than 9th grade
- 9th to 12th grade, no diploma
- High school graduate (includes equivalency)
- Some college, no degree
- Associate\'s degree
- Bachelor\'s degree
- Graduate or professional degree

Veteran Status (*get_veteran_status*())
- Civilian veterans 

Residence One Year Ago (*get_residence_year_ago*())
- Same house
- Same county
- Same state
- Different state
- Abroad

Place of Birth (*get_place_of_birth*())
- State of residence
- Different state
- Born in Puerto Rico, U.S. Island areas, or born abroad to American parent(s)
- Foreign born

US Citizenship (*get_US_citizenship_status*())
- Naturalized U.S. citizen
- Not a U.S. citizen

World Region of Foreign Born (*get_world_region_of_birth_of_foreign_born*())
- Europe
- Asia
- Africa
- Oceania
- Latin America
- Northern America

Language Spoken at Home (*get_language_spoken_at_home*())
- English only
- Spanish
- Other Indo-European languages
- Asian and Pacific Islander languages
- Other languages

Ancestry (*get_ancestry*())
- American
- Arab
- Czech
- Danish
- Dutch
- English
- French (except Basque)
- French Canadian
- German
- Greek
- Hungarian
- Irish
- Italian
- Lithuanian
- Norwegian
- Polish
- Portuguese
- Russian
- Scotch-Irish
- Scottish
- Slovak
- Subsaharan African
- Swedish
- Swiss
- Ukrainian
- Welsh
- West Indian (excluding Hispanic origin groups)

Computer and Internet Use (*get_computer_and_internet_use*())
- With a computer
- With a broadband Internet subscription

Employment Status (*get_employment_status*())
- Employed
- Unemployed
- Armed Forces
- Not in labor force

Commuting Method (*get_commuting_to_work())
- Car, truck, or van -- drove alone
- Car, truck, or van -- carpooled
- Public transportation (excluding taxicab)
- Walked
- Other means
- Worked at home

Occupation (*get_occupation*())
- Management, business, science, and arts occupations
- Service occupations
- Sales and office occupations
- Natural resources, construction, and maintenance occupations
- Production, transportation, and material moving occupations

Industry (*get_industry*())
- Agriculture, forestry, fishing and hunting, and mining
- Construction
- Manufacturing
- Wholesale trade
- Retail trade
- Transportation and warehousing, and utilities
- Information
- Finance and insurance, and real estate and rental and leasing
- Professional, scientific, and management, and administrative and waste management services
- Educational services, and health care and social assistance
- Arts, entertainment, and recreation, and accommodation and food services
- Other services, except public administration
- Public administration

Worker Class (*get_class_of_worker*())
- Private wage and salary workers
- Government workers
- Self-employed in own not incorporated business workers
- Unpaid family workers

Household Income (*get_household_income*())
- Less than $10,000
- $10,000 to $14,999
- $15,000 to $24,999
- $25,000 to $34,999
- $35,000 to $49,999
- $50,000 to $74,999
- $75,000 to $99,999
- $100,000 to $149,999
- $150,000 to $199,999
- $200,000 or more

Percent of Households with Earnings (*get_households_with_earnings())
- With earnings

Percent of Households with Social Security (*get_households_with_social_security*())
- With Social Security 

Percent of Households with Retirement Income (*get_households_with_retirement_income*())
- With retirement income 

Percent of Households with Supplemental Security Income (*get_households_with_supplemental_security_income*())
- With Supplemental Security Income 

Percent of Households with Cash Public Assistance Income (*get_households_with_cash_public_assistance_income*())
- With cash public assistance income

Percent of Households with SNAP Benefits (*get_households_with_SNAP_benefit*())
- With Food Stamp/SNAP benefits in the past 12 months

Family Income (*get_family_income*())
- Less than $10,000
- $10,000 to $14,999
- $15,000 to $24,999
- $25,000 to $34,999
- $35,000 to $49,999
- $50,000 to $74,999
- $75,000 to $99,999
- $100,000 to $149,999
- $150,000 to $199,999
- $200,000 or more

Health Insurance Coverage (*get_health_insurance_coverage*())
- With private health insurance
- With public coverage
- No health insurance coverage

Housing Occupancy (*get_housing_occupancy*())
- Occupied housing units
- Vacant housing units

Number of Units in Housing Structures (*get_units_in_structure*())
- 1-unit, detached
- 1-unit, attached
- 2 units
- 3 or 4 units
- 5 to 9 units
- 10 to 19 units
- 20 or more units
- Mobile home
- Boat, RV, van, etc.

Year Housing Structures Built (*get_year_structure_built*())

- 2009-2011
  - Built 2005 or later
  - Built 2000 to 2004
  - Built 1990 to 1999
  - Built 1980 to 1989
  - Built 1970 to 1979
  - Built 1960 to 1969
  - Built 1950 to 1959
  - Built 1940 to 1949
  - Built 1939 or earlier
- 2012-2014
  - Built 2010 or later
  - Built 2000 to 2009
  - Built 1990 to 1999
  - Built 1980 to 1989
  - Built 1970 to 1979
  - Built 1960 to 1969
  - Built 1950 to 1959
  - Built 1940 to 1949
  - Built 1939 or earlier
- 2015-2020
  - Built 2014 or later
  - Built 2010 to 2013
  - Built 2000 to 2009
  - Built 1990 to 1999
  - Built 1980 to 1989
  - Built 1970 to 1979
  - Built 1960 to 1969
  - Built 1950 to 1959
  - Built 1940 to 1949
  - Built 1939 or earlier
- 2021-2023
  - Built 2020 or later
  - Built 2010 to 2019
  - Built 2000 to 2009
  - Built 1990 to 1999
  - Built 1980 to 1989
  - Built 1970 to 1979
  - Built 1960 to 1969
  - Built 1950 to 1959
  - Built 1940 to 1949
  - Built 1939 or earlier

Number of Rooms (*get_rooms*())
- 1 room
- 2 rooms
- 3 rooms
- 4 rooms
- 5 rooms 
- 6 rooms
- 7 rooms
- 8 rooms 
- 9 rooms or more 

Number of Bedrooms (*get_bedrooms*())
- No bedroom
- 1 bedroom
- 2 bedrooms
- 3 bedrooms
- 4 bedrooms
- 5 or more bedrooms 

Housing Tenure (*get_housing_tenure*())
- Owner-occupied
- Renter-occupied

Year Householder Moved into Unit (*get_year_householder_moved_into_unit*())
- 2009-2011
  - Moved in 2005 or later
  - Moved in 2000 to 2004
  - Moved in 1990 to 1999
  - Moved in 1980 to 1989
  - Moved in 1970 to 1979
  - Moved in 1969 or earlier
- 2012-2014
  - Moved in 2010 or later
  - Moved in 2000 to 2009
  - Moved in 1990 to 1999
  - Moved in 1980 to 1989
  - Moved in 1970 to 1979
  - Moved in 1969 or earlier
- 2015-2017
  - Moved in 2015 or later
  - Moved in 2010 to 2014
  - Moved in 2000 to 2009
  - Moved in 1990 to 1999
  - Moved in 1980 to 1989
  - Moved in 1979 and earlier
- 2018-2019
  - Moved in 2017 or later
  - Moved in 2015 to 2016
  - Moved in 2010 to 2014
  - Moved in 2000 to 2009
  - Moved in 1990 to 1999
  - Moved in 1989 and earlier
- 2020-2021
  - Moved in 2019 or later
  - Moved in 2015 to 2018
  - Moved in 2010 to 2014
  - Moved in 2000 to 2009
  - Moved in 1990 to 1999
  - Moved in 1989 and earlier
- 2022-2023
  - Moved in 2021 or later
  - Moved in 2018 to 2020
  - Moved in 2010 to 2017
  - Moved in 2000 to 2009
  - Moved in 1990 to 1999
  - Moved in 1989 and earlier

Vehicles Available (*get_vehicles_available*())
- No vehicles available
- 1 vehicle available
- 2 vehicles available
- 3 or more vehicles available

House Heating Fuel Source (*get_house_heating_fuel*())
- Utility gas
- Bottled, tank, or LP gas
- Electricity
- Fuel oil, kerosene, etc.
- Coal or coke
- Wood
- Solar energy
- Other fuel
- No fuel used

Percent of Houses Lacking Complete Plumbing Facilities (*get_housing_lacking_complete_plumbing_facilities*())
- Lacking complete plumbing facilities

Percent of Houses Lacking Complete Kitchen Facilities (*get_housing_lacking_complete_kitchen_facilities*())
- Lacking complete kitchen facilities

Percent of Houses with no Telephone Service Available (*get_housing_no_telephone_service_available*())
- No telephone service available

Occupants per Room (*get_occupants_per_room*())
- 1.00 or less
- 1.01 to 1.50
- 1.51 or more

Housing Value (*get_housing_value*())
- Less than $50,000
- $50,000 to $99,999
- $100,000 to $149,999
- $150,000 to $199,999
- $200,000 to $299,999
- $300,000 to $499,999
- $500,000 to $999,999
- $1,000,000 or more

Mortgage Status (*get_mortgage_status*())
- Housing units with a mortgage
- Housing units without a mortgage

Monthly Owner Costs for Housing Units with a Mortgage (*get_selected_monthly_owner_costs_with_mortgage*())
- 2009-2014
  - Less than $300
  - $300 to $499
  - $500 to $699
  - $700 to $999
  - $1,000 to $1,499
  - $1,500 to $1,999
  - $2,000 or more
- 2015-2023
  - Less than $500
  - $500 to $999
  - $1,000 to $1,499
  - $1,500 to $1,999
  - $2,000 to $2,499
  - $2,500 to $2,999
  - $3,000 or more

Monthly Owner Costs for Housing Units without a Mortgage (*get_selected_monthly_owner_costs_without_mortgage*())
- 2009-2014
  - Less than $100
  - $100 to $199
  - $200 to $299
  - $300 to $399
  - $400 or more
- 2015-2023
  - Less than $250
  - $250 to $399
  - $400 to $599
  - $600 to $799
  - $800 to $999
  - $1,000 or more

Monthly Owner Costs as a Percentage of Household Income for Housing Units with a Mortgage (*get_SMOCAPI_with_mortgage*())
- Less than 20.0 percent
- 20.0 to 24.9 percent
- 25.0 to 29.9 percent
- 30.0 to 34.9 percent
- 35.0 percent or more

Monthly Owner Costs as a Percentage of Household Income for Housing Units without a Mortgage (*get_SMOCAPI_without_mortgage*())
- Less than 10.0 percent
- 10.0 to 14.9 percent
- 15.0 to 19.9 percent
- 20.0 to 24.9 percent
- 25.0 to 29.9 percent
- 30.0 to 34.9 percent
- 35.0 percent or more

Gross Rent (*get_gross_rent*())
- 2009-2014
  - Less than $200
  - $200 to $299
  - $300 to $499
  - $500 to $749
  - $750 to $999
  - $1,000 to $1,499
  - $1,500 or more
- 2015-2023
  - Less than $500
  - $500 to $999
  - $1,000 to $1,499
  - $1,500 to $1,999
  - $2,000 to $2,499
  - $2,500 to $2,999
  - $3,000 or more

Gross Rent as a Percentage of Household Income (*get_GRAPI*())
- Less than 15.0 percent
- 15.0 to 19.9 percent
- 20.0 to 24.9 percent
- 25.0 to 29.9 percent
- 30.0 to 34.9 percent
- 35.0 percent or more

Total Population (*get_total_pop*())
- Total population 

Population by Sex (*get_pop_sex*())
- Male
- Female 

Population by Age Bracket (*get_age*())
- Under 5 years 
- 5 to 9 years 
- 10 to 14 years 
- 15 to 19 years
- 20 to 24 years 
- 25 to 34 years
- 35 to 44 years
- 45 to 54 years
- 55 to 59 years
- 60 to 64 years
- 65 to 74 years
- 75 to 84 years
- 85 years and over

Population by Race (*get_race*())
- White
- Black or African American
- American Indian and Alaska Native
- Asian
- Native Hawaiian and Other Pacific Islander
- Some other race
