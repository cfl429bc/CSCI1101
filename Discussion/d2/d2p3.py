pennies = int(input("Enter the number of pennies: "))
dollars = int(pennies / 100)
cents = int(pennies - (dollars * 100))
print(f"That is ${dollars}.{cents} cents.")