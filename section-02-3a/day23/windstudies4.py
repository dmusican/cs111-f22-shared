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


# Determine count and average for each state
for state in yearByState:
    yearList = yearByState[state]
    total = 0
    count = 0
    for year in yearList:
        if year != '':
            total = total + int(year)
            count = count + 1
    average = total / count
    print(state, average)
