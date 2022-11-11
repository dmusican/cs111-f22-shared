import csv

csvfile = open('wind_turbines.csv', 'r')
datareader = csv.DictReader(csvfile)


for cat in datareader:
    print(cat)








# # Count number of wind turbines in each state
# countByState = {}   # state: count

# for row in datareader:
#     state = row['t_state']
#     if state not in countByState:
#         countByState[state] = 0
#     countByState[state] += 1

# csvfile.close()

# for state in countByState:
#     print(state, countByState[state])
