#Fairness von Craps
from random import randint, seed
seed()

def wuerfelSumme():
    wuerfel1=randint(1,6)
    wuerfel2=randint(1,6)
    return wuerfel1+wuerfel2
    
def spielgewonnen():
    gewonnen=False
    spielende=False
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
    return gewonnen       
            
#Hauptprogramm            
anzahl = int(input('Wie viele Durchgänge simulieren? '))
gewinne = 0
for i in range(anzahl):
    if spielgewonnen():
        gewinne +=1
              
print('Du hast von ',anzahl,' Spielen ',gewinne,' Spiele gewonnen!')


