from math import sqrt

number = float(input('Enter an integer: '))

def factor(x):
    """
    factor takes an integer and returns a list containing the factors of the integer
    1. the function only needs to check the numbers up through the square root of the integer, because any factor
        larger than the square root will have the corresponding factor that is less than the square root 
        (i.e. 25 and 5 for 100)
    2.if the integer can be evenly divided by the number that's being checked, add that number
        as well as the integer divided by that number
    """
    list_of_factor = []
    x = int(x)
    for num in range(1, int(sqrt(x)+1)):
        if x % num == 0:
            list_of_factor.append(num)
            list_of_factor.append(int(x / num))
    return list_of_factor

print(factor(number))