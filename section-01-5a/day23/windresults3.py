import csv

# Figure out average year that wind turbines are built per state
yearsByState = {}
with open('wind_turbines.csv', 'r') as csvfile:
    datareader = csv.DictReader(csvfile)
    for row in datareader:
        state = row['t_state']
        year = row['p_year']
        if state not in yearsByState:
            yearsByState[state] = []

        yearsByState[state].append(year)

print(yearsByState['MN'])
