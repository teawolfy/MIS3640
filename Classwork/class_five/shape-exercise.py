#Collaborated with Hunter, Duncan, Rose, Wendy, and Amna
#@Professor: For ease of use, copy the code into a new python window. In my debugging tessting, I had this file set as a repository, but tested all code in a separate VS Code Window
import turtle
import math
import *
tpen = turtle.Turtle()
tpen.pensize(4)
tpen.hideturtle()

print(tpen)

#shape one
def twotris(t):
    t.lt(30)
    t.fd(200)
    t.rt(120)
    t.fd(200)
    t.rt(120)
    t.fd(400)
    t.lt(120)
    t.fd(200)
    t.lt(120)
    t.fd(200)

twotris(tpen)

tpen.lt(60)
twotris(tpen)

tpen.fd(200)
tpen.lt(91)
tpen.circle(200)
tpen.lt(90)
tpen.fd(100)
tpen.circle(55)

tpen.fd(100)
tpen.lt(30)

tpen.fd(100)
tpen.circle(55)

tpen.lt(180)
tpen.fd(100)

tpen.rt(270)
tpen.fd(100)
tpen.circle(55)

tpen.lt(180)
tpen.fd(100)

tpen.rt(270)
tpen.fd(100)
tpen.circle(55)

#shape two
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 100
    length = circumference / n
    polygon(t, n, length)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def petal(t, r, angle):
    for i in range(0,2):
        arc(t, r, angle)
        t.lt(180-angle)

for i in range(0,6):
    petal(tpen, 200, 360/6)
    tpen.lt(360/6)
arc(tpen, 200, 360/6)
tpen.lt(61)
circle(tpen,200)

#shape three
def yin(radius, color1, color2):
    width(3)
    color("black", color1)
    circle(radius/2., 180)
    circle(radius, 180)
    left(180)
    circle(-radius/2., 180)
    left(90)
    up()
    forward(radius*0.35)
    right(90)
    down()
    circle(radius*0.15)
    left(90)
    up()
    backward(radius*0.35)
    down()
    left(90)

def main():
    reset()
    yin(200, "black", "white")
    yin(200, "white", "black")
    ht()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()



turtle.mainloop()