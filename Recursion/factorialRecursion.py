def factorial(n):
    assert n >= 0 and int(n) == n, "Number must be a positive integer"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(7))
print(factorial(4))
print(factorial(10))
print(factorial(-3))
print(factorial(1.5))