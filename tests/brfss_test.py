from fedwrap import get_brfss_data

data = get_brfss_data("state", "crude", 2023, "CHECKUP1")
print(data.head(10))