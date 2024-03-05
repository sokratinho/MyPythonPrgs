#Fraktaler Baum
from turtle import *
sc = Screen()
sc.setup(400,400, startx=800, starty=200)
speed(1) # 1: slow - 10: fast - (0:fastest)

def zeichne_baum(laenge):
    if(laenge>=20):
        forward(laenge)
        right(45)
        zeichne_baum(laenge/2)
        left(90)
        zeichne_baum(laenge/2)
        right(45)
        left(180)
        forward(laenge)
        left(180)

goto(0,-100)
left(90)
zeichne_baum(100)