#Flawed string based method as 0 in binary does not translate
def decToBinStr(n):
    if n == 0:
        return ""
    else:
        if n%2 == 0:
            return decToBinStr(n//2)+"0"
        else:
            return decToBinStr(n//2)+"1"

def decToBinInt(n):
    assert n >= 0 and int(n) == n
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decToBinInt(n//2)

print(decToBinInt(-4))