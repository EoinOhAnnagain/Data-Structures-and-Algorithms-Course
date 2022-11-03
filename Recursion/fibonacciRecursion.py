def fib(n):
    assert n >= 0 and int(n) == n, "Fibonacci number can not be a negative number or non integer"
    if n in [0,1]:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(7))
print(fib(10))
print(fib(17))