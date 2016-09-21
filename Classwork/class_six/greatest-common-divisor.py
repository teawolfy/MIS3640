def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

print(gcd(2,12))
print(gcd(6,12))
print(gcd(9,12))
print(gcd(17,12))

