def fibonacci(i):
    count = 1
    a = 0
    b = 1
    c = 0
    while count < i:
        c = a + b
        a = b
        b = c
        count += 1
    return c

print(fibonacci())