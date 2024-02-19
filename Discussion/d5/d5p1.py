# atm problem
import sys

balance = 1000
func = str("start")
print("Welcome to your friendly ATM!")
while func != "quit":
    print(f"Current balance: ${balance:.2f}")
    func = str(input("What you want to do (deposit, withdraw, quit)? "))
    if func == "deposit":
        amt = float(input("How much? $"))
        if amt < 0:
            print("Can't deposit negative amounts!")
        else:
            balance += amt
    elif func == "withdraw":
        amt = float(input("How much? $"))
        if amt < 0:
            print("Can't withdraw negative amounts!")
        elif amt > balance:
            print("Can't withdraw more than you have!")
        else:
            balance -= amt
    elif func != "quit":
        print("Invalid operation!")

print(f"Final balance: ${balance:.2f}")