import csv

# Find average year of wind turbine construction per state
yearByState = {}
with open('wind_turbines.csv', 'r') as csvfile:
    datareader = csv.DictReader(csvfile)

    for row in datareader:
        state = row['t_state']
        year = row['p_year']
        if state not in yearByState:
            yearByState[state] = []
        yearByState[state].append(year)

print(yearByState['MN'])
