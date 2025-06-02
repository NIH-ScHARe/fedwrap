from fedwrap.census_acs import get_educational_attainment


data = get_educational_attainment('2022', 'county', as_percent=True)
print(data.head())
