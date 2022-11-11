import csv

csvfile = open('wind_turbines.csv', 'r')
datareader = csv.DictReader(csvfile)

# Find how many wind turbines there are in each state
countByState = {}

for row in datareader:
    print(row)
    print('--------')
    state = row['t_state']
    if state not in countByState:
        countByState[state] = 0

    countByState[state] += 1
    # countByState[state] = countByState[state] + 1

print(countByState)
