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
        kreis(diam-n*2*abstand)
        pu()
        rt(90)
        fd(diam/abstand)
        lt(90)
        pd()
        zielscheibe(diam,n-1)
        
zielscheibe(400,10)
    