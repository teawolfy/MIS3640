import math

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

d = b**2-4*a*c #descriminant 

if d < 0:
    print("This equation has no real solution")
elif d == 0:
    x = (-b + math.sqrt(b**2 - 4*a*c))/2*a
    print("This equation has one solution: "), x
else:
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
    x2 = (-b + math.sqrt(b**2 - 4*a*c))/2*a        
    print("This equation has two solutions: "), x1, print(" and"), x2

#correct solution
def quadratic(a, b, c):
    try:
        x1 = (-b + (sqrt(b**2 - 4*a*c))) / (2*a)
        x2 = (-b - (sqrt(b**2 - 4*a*c))) / (2*a)
        return x1, x2
    except ValueError:
        print('These values will not work')