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

# Average years for each state
for state in yearsByState:
    yearList = yearsByState[state]
    total = 0
    count = 0
    for year in yearList:
        count = count + 1
        print("Year is", year)
        total = total + int(year)
    average = total / count
    print(state, average)
