#Zielscheibe
from turtle import *

def kreis(durchmesser):
    for _ in range(36):
        forward(3.142*durchmesser/36)
        left(10)
        
def zielscheibe(diam,n):
    if n==0:
        pass
    else:
        abstand=diam/(2*n)
        kreis(diam)
        pu()
        lt(90)
        fd(abstand)
        rt(90)
        pd()
        zielscheibe(diam-2*abstand,n-1)

pu()
right(90)
forward(200)
pd()
left(90)
zielscheibe(400,10)
    