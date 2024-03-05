# Datenverwaltung
daten = [('2015-06-30', 10944.97),
         ('2015-06-29', 11083.2),
         ('2015-06-26', 11492.43),
         ('2015-06-25', 11473.13),
         ('2015-06-24', 11471.26)]

#Maximaler Listenwert mit Datumsstempel   
def maxListe(Liste):
    max = Liste[0][1]
    maxPos = 0
    for i in range(len(Liste)):
        if Liste[i][1] > max:
            max = Liste[i][1]
            maxpos = i
    return Liste[maxpos]

# Zugriff auf die Daten
print('Das Maximum ist: ',maxListe(daten))
