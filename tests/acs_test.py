from fedwrap.census_acs import get_residence_year_ago

# data = get_educational_attainment('2022', 'county', as_percent=True)
# print(data.head())

data = get_residence_year_ago('2022', 'county', as_percent=True)
print(data.head())
