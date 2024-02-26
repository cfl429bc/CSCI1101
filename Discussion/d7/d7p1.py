import sys

def postest(num):
    if num <= 0:
        print("Value must be positive!")
        sys.exit()

num_1 = float(input("Enter a: "))
postest(num_1)
num_2 = float(input("Enter b: "))
postest(num_2)