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
        
seg(300)