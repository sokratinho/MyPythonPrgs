#Vigenere-Verschlüsselung
#Leerzeichen werden toleriert, Kleinbuchstaben werden gewandelt

def shiftzahl(zeichen):
    return ord(zeichen.upper()) - ord('A')

def Vigenere(wort,shift):
    #Verschlüsselung
    Geheimtext = ''
    wort=wort.upper()
    schluesselpos = 0
    schluessellaenge = len(schluessel)
    for b in wort:
        if schluesselpos == schluessellaenge:
            schluesselpos -= schluessellaenge
        if ord(b) != 32:
            zeichenpos= ord(b) + shiftzahl(schluessel[schluesselpos])
            if zeichenpos > ord('Z'):
                zeichenpos = zeichenpos - 26
            schluesselpos += 1    
        else:
            zeichenpos = 32    
        Geheimtext = Geheimtext + chr(zeichenpos)
    return Geheimtext
    
#Hauptprogramm    
wort = input("Gib das zu verschlüsselnde Wort ein: ")
schluessel = input("Gib das Schlüsselwort ein: ")   
print("Aus dem Wort ",wort," wird ",Vigenere(wort,schluessel))
    
