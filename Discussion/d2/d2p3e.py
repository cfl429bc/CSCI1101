pennies = int(input("Enter the number of pennies: "))
dollars = int(pennies / 100)
quarters = int((pennies - (dollars * 100)) / 25)
dimes = int((pennies - (dollars * 100) - (quarters * 25)) / 10)
nickels = int((pennies - (dollars * 100) - (quarters * 25) - (dimes * 10)) / 5)
new_pennies = int(pennies - (dollars * 100) - (quarters * 25) - (dimes * 10) - (nickels * 5))

tense_dollars = str("dollars")
if dollars == 1:
    tense_dollars = str("dollar")

tense_quarters = str("quarters")
if quarters == 1:
    tense_quarters = str("quarter")

tense_dimes = str("dimes")
if dimes == 1:
    tense_dimes = str("dime")

tense_nickels = str("nickels")
if nickels == 1:
    tense_nickels = str("nickel")

tense_pennies = str("pennies")
if new_pennies == 1:
    tense_pennies = str("penny")

print(f"That is {dollars} {tense_dollars}, {quarters} {tense_quarters}, {dimes} {tense_dimes}, {nickels} {tense_nickels}, and {new_pennies} {tense_pennies}.")