CPI_1966 = 17.5
CPI_2013 = 122.8
wage_1966 = 3500
wage_2013 = 125000

# Adjusting 1966 wages to 2013 dollars
wage_1966_in_2013 = wage_1966 * (CPI_2013 / CPI_1966)

# Adjusting 2013 wages to 1966 dollars
wage_2013_in_1966 = wage_2013 * (CPI_1966 / CPI_2013)

print(wage_1966_in_2013, wage_2013_in_1966)