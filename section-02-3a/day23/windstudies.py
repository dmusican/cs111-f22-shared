import csv

csvfile = open('wind_turbines.csv', 'r')
datareader = csv.DictReader(csvfile)

for row in datareader:
    #print(row)
    print(row['t_state'], row['t_county'])
    print()

csvfile.close()
