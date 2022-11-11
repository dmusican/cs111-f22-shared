import csv

csvfile = open('wind_turbines.csv', 'r')
datareader = csv.DictReader(csvfile)

# Count number of wind turbines in each state
countByState = {}   # state: count

for row in datareader:
    state = row['t_state']
    if state not in countByState:
        countByState[state] = 0
    countByState[state] += 1

csvfile.close()

# Sort results by state
countList = []
for state in countByState:
    countList.append( (countByState[state], state)  )

results = sorted(countList)
print(results)
for stateCountPair in results:
    print(stateCountPair[0], stateCountPair[1])
