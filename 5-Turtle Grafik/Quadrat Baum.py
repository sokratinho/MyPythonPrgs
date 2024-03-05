#Fraktaler Quadrat Baum
#Ist noch falsch!
from turtle import *
sc = Screen()
sc.setup(400,400, startx=800, starty=200)
speed(1) # 1: slow - 10: fast - (0:fastest)

def zeichne_baum(laenge,tiefe):
    if tiefe>0:
        forward(laenge/2)
        left(90)
        forward(laenge)
        right(135)
        zeichne_baum(laenge/2,tiefe-1) #Rechts oben
        right(135)
        forward(laenge)
        right(135)
        zeichne_baum(laenge/2,tiefe-1) #Links oben
        right(135)
        forward(laenge)
        left(90)
        forward(laenge/2)
    else:
        pass
        

#Anfangsposition einnehmen
speed(0)
pu()
goto(0,-100)
pd()
tiefe=int(input("Anzahl der Iterationen (1-10)):"))
zeichne_baum(100,tiefe)