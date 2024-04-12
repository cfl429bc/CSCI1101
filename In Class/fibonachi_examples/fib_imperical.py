def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    last2 = 0
    last1 = 1
    i = 2
    while i <= n:
        current = last2 + last1
        last2 = last1
        last1 = current
        i += 1
    return current

n = 5
f = fib(n)
print(f"F_{n} = {f}")
