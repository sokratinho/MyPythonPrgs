#Caesar-Verschlüsselung 
wort = input("Gib das zu verschlüsselnde Wort in Großbuchstaben ein: ")
shift = input("Gib den Verschiebungsbuchstaben ein: ")

def shiftzahl(zeichen):
    return ord(zeichen.upper()) - ord('A')

def caesar(wort,shift):
    #Verschlüsselung
    Geheimtext =''
    wort=wort.upper()  
    for b in wort:
        zeichenpos= ord(b) + shiftzahl(shift)
        if zeichenpos > ord('Z'):
            zeichenpos = zeichenpos - 26
        Geheimtext = Geheimtext + chr(zeichenpos)
    return Geheimtext
        
print("Aus dem Wort ",wort," wird ",caesar(wort,shift))
    
