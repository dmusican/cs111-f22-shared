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

results = sorted(countList, reverse=True)

# Use outfile within this "with" code, and automatically close
with open('results.txt', 'w') as outfile:
    for stateCountPair in results:
        outfile.write(str(stateCountPair[1]) + " " \
                      + str(stateCountPair[0]) + "\n")
