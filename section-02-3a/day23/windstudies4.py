
# Find average year of wind turbine construction per state
with open('wind_turbines.csv', 'r') as csvfile:
    datareader = csv.DictReader(csvfile)

for row in datareader:
    print(row['t_state'], row['p_year'])
