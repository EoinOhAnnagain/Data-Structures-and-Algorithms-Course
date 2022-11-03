def sumOfDigits(n):
    assert n >= 0 and int(n) == n, "Number must be a positive integer"
    if n < 10:
        return n
    else:
        return n%10 + sumOfDigits(n//10)

print(sumOfDigits(54))
print(sumOfDigits(112))
print(sumOfDigits(75926747289645))