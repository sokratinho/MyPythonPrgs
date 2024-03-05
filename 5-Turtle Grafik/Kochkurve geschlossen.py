#Koch-Kurve gerade Linie
from turtle import *

def seg(laenge):
    if laenge>=30:
        seg(laenge/3)
        left(60)
        seg(laenge/3)
        right(120)
        seg(laenge/3)
        left(60)
        seg(laenge/3)
    else:
        fd(laenge)
 
pu()
goto(-150,100)
pd()
speed(0)
for _ in range(3):
    seg(300)
    right(120)