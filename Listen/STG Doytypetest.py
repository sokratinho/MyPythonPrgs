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

#Wie viele über dem Schwellenwert
def above(list, grenze):
    anz = 0
    for i in range(len(list)):
        if list[i] > grenze:
            anz += 1
    return anz

#Welche Elemente über dem Schwellenwert
def ueberSchwellenwert(list, grenze):
    trefferList = []
    for i in range(len(list)):
        if list[i] > grenze:
            trefferList = trefferList + [list[i]]
            #Besser: trefferList.append(list[i])
    return trefferList

#Index der Elemente über dem Schwellenwert
def indexUeberSchwellenwert(list, grenze):
    trefferList = []
    for i in range(len(list)):
        if list[i] > grenze:
            trefferList = trefferList + [i]
    return trefferList

#Kursschwankungen als Liste
def listeDifferenzen(list):
    difList = []
    for i in range(len(list)-1):
        difList = difList + [list[i+1] - list[i]]
    return difList

#Test der Funktionen
print('Werte über 11400:',ueberSchwellenwert(daxListe, 11400))
print('Indizes über 11400:',indexUeberSchwellenwert(daxListe, 11400))
difListe=listeDifferenzen(daxListe)
print('Liste der Differenzen:')
for i in range(len(difListe)):
    print(f" {difListe[i]:.2f}",end=" ")
