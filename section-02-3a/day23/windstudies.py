import csv

csvfile = open('wind_turbines.csv', 'r')
datareader = csv.DictReader(csvfile)

for row in datareader:
    print(row)
    print()

csvfile.close()
