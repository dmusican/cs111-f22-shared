import csv

csvfile = open('wind_turbines.csv', 'r')
datareader = csv.DictReader(csvfile)

# Find how many wind turbines there are in each state

for row in datareader:
    # row... is a DICTIONARY!!!!!
    print(row['t_state'])
