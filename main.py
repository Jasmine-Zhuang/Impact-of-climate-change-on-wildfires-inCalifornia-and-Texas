"""Climate change and wildfire."""
import data
import figure
import datetime


if __name__ == '__main__':
    ca_temp = data.Temperature('CA', 'ca_climate.csv', 'DATE', 'TAVG', 'TMAX', 'TMIN')
    ca_prcp = data.Precipitation('CA', 'ca_climate.csv', 'DATE', 'PRCP')
    ca_wildfire = data.Wildfire('CA', 'wildfire_data.csv', 'STATE', 'FIRE_YEAR', 'DISCOVERY_DOY', 'FIRE_SIZE')
    tx_temp = data.Temperature('TX', 'tx_climate.csv', 'DATE', 'TAVG', 'TMAX', 'TMIN')
    tx_prcp = data.Precipitation('TX', 'tx_climate.csv', 'DATE', 'PRCP')
    tx_wildfire = data.Wildfire('TX', 'wildfire_data.csv', 'STATE', 'FIRE_YEAR', 'DISCOVERY_DOY', 'FIRE_SIZE')
    ca = data.State('CA', ca_temp, ca_prcp, ca_wildfire)
    tx = data.State('TX', tx_temp, tx_prcp, tx_wildfire)
    begin = 2001
    end = 2005
    time = figure.get_time_list(begin, end)
    # figure.figure_line('time-max temp-CA', 'date', time, 'temp', ca_temp.max_months(begin, end))
    # figure.figure_line('time-min temp-CA', 'date', time, 'temp', ca_temp.min_months(begin, end))
    # figure.figure_line('time-mean temp-CA', 'date', time, 'temp', ca_temp.mean_months(begin, end))
    # figure.figure_line('time-prcp-CA', 'date', time, 'prcp', ca_prcp.total_months(begin, end))
    # figure.figure_dot('max temp-wildfire frequency-CA', 'temp', ca_temp.max_months(begin, end),
    #                               'frequency', ca_wildfire.frequency_months(begin, end))
    # figure.figure_dot('min temp-wildfire frequency-CA', 'temp', ca_temp.min_months(begin, end),
    #                               'frequency', ca_wildfire.frequency_months(begin, end))
    # figure.figure_dot('mean temp-wildfire frequency-CA', 'temp', ca_temp.mean_months(begin, end),
    #                               'frequency', ca_wildfire.frequency_months(begin, end))
    # figure.figure_dot('prcp-wildfire frequency-CA', 'prcp', ca_prcp.total_months(begin, end),
    #                               'frequency', ca_wildfire.frequency_months(begin, end))
    # figure.figure_dot('max temp-wildfire size-CA', 'temp', ca_temp.max_months(begin, end),
    #                               'frequency', ca_wildfire.mean_size_months(begin, end))
    # figure.figure_dot('min temp-wildfire size-CA', 'temp', ca_temp.min_months(begin, end),
    #                               'frequency', ca_wildfire.mean_size_months(begin, end))
    # figure.figure_dot('mean temp-wildfire size-CA', 'temp', ca_temp.mean_months(begin, end),
    #                               'frequency', ca_wildfire.mean_size_months(begin, end))
    # figure.figure_dot('prcp-wildfire size-CA', 'prcp', ca_prcp.total_months(begin, end),
    #                               'frequency', ca_wildfire.mean_size_months(begin, end))

    # figure.figure_line('time-max temp-TX', 'date', time, 'temp', tx_temp.max_months(begin, end))
    # figure.figure_line('time-min temp-TX', 'date', time, 'temp', tx_temp.min_months(begin, end))
    # figure.figure_line('time-mean temp-TX', 'date', time, 'temp', tx_temp.mean_months(begin, end))
    # figure.figure_line('time-prcp-TX', 'date', time, 'prcp', tx_prcp.total_months(begin, end))
    # figure.figure_dot('max temp-wildfire frequency-TX', 'temp', tx_temp.max_months(begin, end),
    #                               'frequency', tx_wildfire.frequency_months(begin, end))
    # figure.figure_dot('min temp-wildfire frequency-TX', 'temp', tx_temp.min_months(begin, end),
    #                               'frequency', tx_wildfire.frequency_months(begin, end))
    # figure.figure_dot('mean temp-wildfire frequency-TX', 'temp', tx_temp.mean_months(begin, end),
    #                               'frequency', tx_wildfire.frequency_months(begin, end))
    # figure.figure_dot('prcp-wildfire frequency-TX', 'prcp', tx_prcp.total_months(begin, end),
    #                               'frequency', tx_wildfire.frequency_months(begin, end))
    # figure.figure_dot('max temp-wildfire size-TX', 'temp', tx_temp.max_months(begin, end),
    #                               'frequency', tx_wildfire.mean_size_months(begin, end))
    # figure.figure_dot('min temp-wildfire size-TX', 'temp', tx_temp.min_months(begin, end),
    #                               'frequency', tx_wildfire.mean_size_months(begin, end))
    # figure.figure_dot('mean temp-wildfire size-TX', 'temp', tx_temp.mean_months(begin, end),
    #                               'frequency', tx_wildfire.mean_size_months(begin, end))
    # figure.figure_dot('prcp-wildfire size-TX', 'prcp', tx_prcp.total_months(begin, end),
    #                               'frequency', tx_wildfire.mean_size_months(begin, end))
