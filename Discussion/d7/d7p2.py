import sys

def posinput(string):
    num = int(input(f"Enter a value for {string}: "))
    if num <= 0:
        print(f"{string} must be positive!")
        sys.exit()
    return num

def factortest(num, n): # outputs the factors, or 0 if not a factor
    zero = 0
    remain = num % n
    if remain == 0:
        return n
    else:
        return zero

N = posinput("N")

sum = 0
for i in range(1, N):
    sum += factortest(N, i)

if N == sum:
    print(f"{N} is a perfect number!")
else:
    print(f"{N} is not a perfect number.")