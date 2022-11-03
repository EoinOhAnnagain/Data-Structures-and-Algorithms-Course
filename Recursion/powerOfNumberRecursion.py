def powOfNumber(x, n):
    #Prevent unintended cases
    assert int(n) == n, "Exponent must be an integer"
    #Base case
    if n == 0:
        return 1
    elif n < 0:
        return 1/x * powOfNumber(x, n+1)
    else:
        return x * powOfNumber(x, n-1)

print(powOfNumber(2,8))
print(powOfNumber(8,2))
print(powOfNumber(4,-1))
print("\n\nNext line is expected to cause an assert error\n")
print(powOfNumber(3,2.5))
