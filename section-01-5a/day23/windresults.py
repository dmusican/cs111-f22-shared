import csv

csvfile = open('wind_turbines.csv', 'r')

for row in csvfile:
    print(row)
