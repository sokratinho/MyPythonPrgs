def verschiebezahl(zeichen): 
    return ord(zeichen) - 65

if __name__ == "__main__":    
    if verschiebezahl('A') == 0 and verschiebezahl('X') == 23:
        print('Test der Funktion "verschiebezahl" erfolgreich!')
    else:
        print('Test der Funktion "verschiebezahl" fehlgeschlagen!')

def verschieben(zeichen, schluessel):
    zahl = ord(zeichen) + verschiebezahl(schluessel)
    if zahl > ord('Z'):
        zahl = zahl - 26
    return chr(zahl)

if __name__ == "__main__":
    if verschieben('A','A') == 'A' and verschieben('Z','C') == 'B':
        print('Test der Funktion "verschieben" erfolgreich!')
    else:
        print('Test der Funktion "verschieben" fehlgeschlagen!')

def vigenereText(text,schluesseltext):
    while len(text)>len(schluesseltext):
        schluesseltext=2*schluesseltext
    geheimtext=""
    for i in range(len(w)):
        klarzeichen = text[i]
        schluesselzeichen = schluesseltext[i]
        geheimzeichen = verschieben(klarzeichen,schluesselzeichen)
        geheimtext = geheimtext + geheimzeichen
    return geheimtext