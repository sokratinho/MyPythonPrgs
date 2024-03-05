#Funktionen auf der Daxliste by STG
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
        
#Index des Maximums        
def indexMaxListe(Liste):
    max = Liste[0]
    maxPos = 0
    for i in range(len(Liste)):
        if Liste[i] > max:
            max = Liste[i]
            maxpos = i
    return maxpos

#Durchschnittswert
def average(Liste):
    summe=0
    for i in range(len(Liste)):
        summe += Liste[i]
    return summe/len(Liste)

#Über dem Schwellenwert
def aboveThreshold(Liste, Wert):
    anz = 0
    for i in range(len(Liste)):
        if Liste[i] > Wert:
            anz += 1
    return anz
        
# Datenverarbeitung
print('Die Liste: ', daxListe[:])
print('Das Maximum: ', maxListe(daxListe))
print('Position:', indexMaxListe(daxListe))
print('Durchschnitt: ', average(daxListe))
print('Über 11400: ', aboveThreshold(daxListe,11400))
        