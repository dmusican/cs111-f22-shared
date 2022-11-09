import csv

csvfile = open('wind_turbines.csv', 'r')
for line in csvfile:
    print(line)

csvfile.close()
