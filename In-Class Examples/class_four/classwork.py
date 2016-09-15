def my_abs(n):
    if n >= 0:
        print(n)
    else:
        print(-n)

my_abs(100)

my_abs(0)

my_abs(-4)

def give_me_a_break():
    str1 = 'break'
    return str1

print(give_me_a_break())

def nop():
    pass

age= int(input())
if age >= 18:
    pass

import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

#Homework for tonight
def quadratic(a, b, c):

    pass
