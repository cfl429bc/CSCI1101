# this is the code before I figured out a function to do the same thing

import sys

def posinput(string):
    num = int(input(f"Enter a value for {string}: "))
    if num <= 0:
        print(f"{string} must be positive!")
        sys.exit()
    return num

N = posinput("N")

sum = 0
for i in range(1, N):
    remain = N % i
    if remain == 0:
        sum += i

if N == sum:
    print(f"{N} is a perfect number!")
else:
    print(f"{N} is not a perfect number.")