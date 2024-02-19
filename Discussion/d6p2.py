import sys

# ask users for how many numbers they want
len = int(input("How many numbers do you have? "))

# makes sure number is greater than zero and exits if not
# has nice print statements
if len == 0:
    print("Must be at least 1 number.")
    sys.exit()
elif len < 0:
    print("Must be a positive number.")
    sys.exit()

# tells user to input the corect number of numbers that they chose
print(f"Enter the {len} numbers each on their own line:")
      
#creates empty list
list = []

# makes list
for i in range(len):
    list.append(float(input()))

# could also be written as
# i = 0
# while i < len:
#     val = float(input())
#     i += 1

#sets counting variables to zero
pos = 0
zero = 0
neg = 0

# tests in numbes in list are positive, negative, or zero and changes counting variable
for num in list:
    if num > 0:
        pos += 1
    elif num == 0:
        zero += 1
    elif num < 0:
        neg += 1

# percent calculations
p_pos = (pos / len) * 100
p_zero = (zero / len) * 100
p_neg = (neg / len) * 100

# print percentages
print(f"{p_pos:.2f}% positive values.")
print(f"{p_zero:.2f}% zero values.")
print(f"{p_neg:.2f}% negative values.")