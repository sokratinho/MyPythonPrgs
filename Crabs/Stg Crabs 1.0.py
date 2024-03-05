#Spielsimulation Craps
from random import randint, seed
seed()
gewonnen=False
spielende=False

def wuerfelSumme():
    wuerfel1=randint(1,6)
    wuerfel2=randint(1,6)
    return wuerfel1+wuerfel2

ersteSumme = wuerfelSumme()
    #Erste Runde
if ersteSumme in [7,11]:
    gewonnen=True
    spielende=True
elif ersteSumme in [2,3,12]:
    spielende=True
else:
    while not spielende:
        naechsteSumme = wuerfelSumme()  
        if naechsteSumme == 7:
            gewonnen = False
            spielende =True
        elif naechsteSumme == ersteSumme:
            gewonnen = True
            spielende = True

if gewonnen:              
    print('Du hast gewonnen!')
else:
    print('Du hast verloren!')

