from fedwrap import get_svi

# get data for Washington State Counties in 2022
print("Test 1: WA Counties in 2022")
df = get_svi(year=2022, geography="county", state="WA")
print(df.head())
print('\n')

# get data for MA Census Tracts in 2022
print("Test 2: MA Tracts in 2000")
df = get_svi(year=2000, geography="tract", state="MA")
print(df.head())
print('\n')
