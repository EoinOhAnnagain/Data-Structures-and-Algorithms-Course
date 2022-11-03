def GCD(n1, n2):
    assert int(n1) == n1 and int(n2) == n2, "Both numbers must be integers"
    if n1 < 0:
        n1 = n1*-1
    if n2 < 0:
        n2 = n2*-1
    if n2 == 0:
        return n1
    else:
        return GCD(n2, n1%n2)

print(GCD(100,-10))
print(GCD(18,48))
print(GCD(48,18))
print(GCD(48,16))
print(GCD(1000,333))