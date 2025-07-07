from fedwrap.census_acs import get_educational_attainment, get_race

# data = get_educational_attainment('2022', 'county', as_percent=True)
# print(data.head())

data = get_race('2022', 'county', as_percent=True)
print(data.head())
