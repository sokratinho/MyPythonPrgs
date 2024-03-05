# Aufpassen! Fallstricke!
daxListe = [11058.39, 11099.35, 10944.97, 11083.2, 11492.43]
neueWerte = [11473.13, 11471.26]

# 
daxListeA = daxListe
daxListeB= daxListe[:]
daxListeA.extend()
daxListeB = daxListeB + [11473.13, 11471.26]
print(daxListe)
print(daxListeA)
print(daxListeB)