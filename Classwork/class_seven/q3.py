def sum_squares(n):
    result = 0
    for i in range(1,n+1):
        result += i * i
    return result
    pass

    
print(sum_squares(1))
print(sum_squares(100))