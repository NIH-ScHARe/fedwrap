from fedwrap import get_acs_data

# data = get_educational_attainment('2022', 'county', as_percent=True)
# print(data.head())

# data = get_residence_year_ago('2022', 'county', as_percent=True)

data = get_acs_data('RACE', "2023", 'MSA', as_percent=True)
print(data.head())
