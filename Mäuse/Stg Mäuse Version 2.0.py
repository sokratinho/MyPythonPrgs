#Einlesen der Werte
jung = 6
erwachsen = 9
alt = 12
gesamt = jung+erwachsen+alt
print("Startwerte:")
print("Schritt 0: Jung:",jung," Erwachsen:",erwachsen," Alt:",alt," Gesamt: ",gesamt)
n= int(input("Wie viele Generationen?"))
#Berechnungsschleife
for i in range(1,n):
    erwachsen_neu = jung // 2
    alt_neu = erwachsen // 3
    jung_neu = erwachsen*4 + alt*2
    jung = jung_neu
    erwachsen = erwachsen_neu
    alt = alt_neu
    gesamt = jung+erwachsen+alt
    #Ausgabe
    print("Schritt ",i," Jung:",jung," Erwachsen:",erwachsen," Elt:",alt," Gesamt: ",gesamt)