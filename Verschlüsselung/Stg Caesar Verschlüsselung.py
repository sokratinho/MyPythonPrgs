#Caesar-Verschlüsselung
Quelltext = input("Gib das zu verschlüsselnde Wort in Großbuchstaben ein: ")
shift = int(input("Gib den Shift ein: "))
Geheimtext=''
#Verschlüsselung
for b in Quelltext:
    #Nur für Großbuchstaben
    if ord(b)<=90 and ord(b)>=65:
        Geheimtext = Geheimtext + chr(ord(b)+shift)
        
    else:
        print("Falsche Eingabe!")
print("Aus dem Wort ",Quelltext," wird ",Geheimtext)
    
