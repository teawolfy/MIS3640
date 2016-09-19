import turtle
shape = turtle.Turtle()
print(shape)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

#square(shape,200)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

#polygon(shape, 100, 5)
import math

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

#circle(shape,100)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

arc(shape, 200, 45)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle) 

#polyline(shape,30,100,45)

turtle.mainloop()