#Funktionen auf der Daxliste
daxListe = [10944.97,
            11083.20,
            11492.43,
            11473.13,
            11471.26,
            11542.54,
            11460.50,
            11040.10,
            11100.30,
            10978.01]

#Maximaler Listenwert
def maxListe(Liste):
    max = Liste[0]
    for i in range(len(Liste)):
        if Liste[i] > max:
            max = Liste[i]
    return max
        
def indexMaxListe(Liste):
    max = Liste[0]
    maxPos = 0
    for i in range(len(Liste)):
        if Liste[i] > max:
            max = Liste[i]
            maxpos = i
    return maxpos
        
# Datenverarbeitung
print(daxListe[0:2])
print(daxListe[3:6])
print(daxListe[3:3])
print(daxListe[0:len(daxListe)])
print(daxListe[4:])
print(daxListe[:4])
print(daxListe[:])
print(maxListe(daxListe))
print(indexMaxListe(daxListe))
        