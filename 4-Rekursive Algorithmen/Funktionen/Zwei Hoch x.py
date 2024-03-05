# Rekursive Funktionen
#Im Rollenspiel darstellen
def zwei_hoch(exp):
    print('Berechne 2 hoch ',exp)
    if exp == 0:
        ergebnis = 1 #Pförtner weiß es!
    else:
        ergebnis = 2*zwei_hoch(exp-1)
    print('Ergebnis ist: ',ergebnis)
    return ergebnis
    
print('Jetzt haben wir das Ergebnis: '+ str(zwei_hoch(9)))

#def potenz_rek(basis, exp)