def fib(n):
    fibs = [-1]*(n+1)
    fibs[0] = 0
    fibs[1] = 1
    return fib_work(n, fibs)
def fib_work(n, fibs):
    if fibs[n] == -1:
        fibs[n] = fib_work(n-1, fibs) + fib_work(n-2, fibs)
        print(fibs)
    return fibs[n]

n = 5
f = fib(n)
print(f"F_{n} = {f}")