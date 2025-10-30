from fedwrap.cdc_places import get_places_data

# data = get_places_data(
#     geo='state',
#     year='2022',
#     measureid='FOODSTAMP',
#     datavaluetypid='AgeAdjPrv'
# )

data = get_places_data(
    geo='census',
    year='2018',
    measureid='ARTHRITIS',
    datavaluetypid='CrdPrv'
)

print(data.head(50))
