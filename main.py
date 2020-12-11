"""Climate change and wildfire."""
import data
import figure


if __name__ == '__main__':
    ca_temp = data.Temperature('CA', 'ca_climate.csv', 'DATE', 'TAVG', 'TMAX', 'TMIN')
    ca_prcp = data.Precipitation('CA', 'ca_climate.csv', 'DATE', 'PRCP')
    ca_wildfire = data.Wildfire('CA', 'wildfire_data.csv', 'STATE', 'FIRE_YEAR', 'DISCOVERY_DOY', 'FIRE_SIZE')
    tx_temp = data.Temperature('TX', 'tx_climate.csv', 'DATE', 'TAVG', 'TMAX', 'TMIN')
    tx_prcp = data.Precipitation('TX', 'tx_climate.csv', 'DATE', 'PRCP')
    tx_wildfire = data.Wildfire('TX', 'wildfire_data.csv', 'STATE', 'FIRE_YEAR', 'DISCOVERY_DOY', 'FIRE_SIZE')
    ca = data.State('CA', ca_temp, ca_prcp, ca_wildfire)
    tx = data.State('TX', tx_temp, tx_prcp, tx_wildfire)
