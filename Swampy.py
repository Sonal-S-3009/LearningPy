from swampy.TurtleWorld import *
import math
'''def poly(t,length,n):
    angle = 360/n
    for _ in range(n):
        fd(t,length)
        lt(t,angle)

def circle(t,r):
    circum = 2*math.pi*r
    n = int(circum/3) +1
    length = circum/n
    poly(t,length,n)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
circle(bob,200)'''

def arc(t,r,angle):
    arc_length = 2*math.pi*r*angle/360
    n = int(arc_length/3)+1
    step_length = arc_length/n
    step_angle = angle/n
    for _ in range(n):
        fd(t,step_length)
        lt(t,step_angle)

def petal(t, r, angle):
    for _ in range(2):
        arc(t, r, angle)
        lt(t, 180 - angle)

def flower(t, n, r, angle):
    for _ in range(n):
        petal(t, r, angle)
        lt(t, 360 / n)
world = TurtleWorld()
bob = Turtle()
bob.delay =0.01
flower(bob,24,30,30)
