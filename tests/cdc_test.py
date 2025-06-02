from fedwrap.cdc_places import get_places_data

data = get_places_data(
    geo='county',
    year='2022',
    measureid='ARTHRITIS',
    datavaluetypid='CrdPrv'
)

print(data.head())
