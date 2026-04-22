from fedwrap import get_brfss_data

# data = get_brfss_data("state", "crude", 2023, "CHECKUP1", "Sex")
data = get_brfss_data("msa", "crude", 2016, "GENHLTH", "Overall")
print(data.head(10))
