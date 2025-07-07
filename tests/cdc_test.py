from fedwrap.cdc_places import get_places_data

data = get_places_data(
    geo='state',
    year='2022',
    measureid='FOODSTAMP',
    datavaluetypid='AgeAdjPrv'
)

print(data.head(50))
