import csv

csvfile = open('wind_turbines.csv', 'r')
datareader = csv.DictReader(csvfile)

for row in datareader:
    # row... is a DICTIONARY!!!!!
    print(row)
