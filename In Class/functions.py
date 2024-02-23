def get_int(prompt):
    value = int(input(prompt))
    return value

def factorial(n):
    total = 1
    while n > 0:
        total *= n
        n -= 1
    return total

def factor_sum(n):
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

test = factorial(int(input("factorial of: ")))
print(f"factorial = {test}")

test = factor_sum(int(input("factor sum of: ")))
print(f"factor sum = {test}")