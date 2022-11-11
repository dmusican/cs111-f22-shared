import csv

csvfile = open('wind_turbines.csv', 'r')
datareader = csv.DictReader(csvfile)

# Find how many wind turbines there are in each state
countByState = {}

for row in datareader:
    state = row['t_state']
    if state not in countByState:
        countByState[state] = 0

    countByState[state] += 1
    # countByState[state] = countByState[state] + 1

#print(countByState)
for state in countByState:
    print(state, countByState[state])

# Want to sort, so copy into a list
countList = []
for state in countByState:
    countList.append(  (state, countByState[state])   )

results = sorted(countList)

print(results)
