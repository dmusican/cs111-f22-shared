import csv

# Figure out average year that wind turbines are built per state
with open('wind_turbines.csv', 'r') as csvfile:
    datareader = csv.DictReader(csvfile)
    for row in datareader:
        state = row['t_state']
        year = row['p_year']
        #print(state, year)

    datareader = csv.DictReader(csvfile)
    for row in datareader:
        state = row['t_state']
        year = row['p_year']
        print(state, year)
