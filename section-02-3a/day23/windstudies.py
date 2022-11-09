import csv

csvfile = open('wind_turbines.csv', 'r')
datareader = csv.DictReader(csvfile)

# Count number of wind turbines in each state
countByState = {}   # state: count

for row in datareader:
    #print(row)
    #print(row['t_state'], row['t_county'])
    state = row['t_state']
    #if state not in countByState:
    #    countByState[state] = 1
    #else:
    #    countByState[state] += 1

    if state not in countByState:
        countByState[state] = 0
   countByState[state] += 1

csvfile.close()

print(countByState)
