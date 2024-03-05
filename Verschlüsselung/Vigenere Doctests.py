import doctest



def verschiebezahl(zeichen):
    """ 
    Das Zeichen wird in eine Dezimalzahl umgewandelt,
    wobei A der Zahl 0 und Z der Zahl 25 entsprechen soll.

    >>> verschiebezahl('A')
    1
    >>> verschiebezahl('B')
    1
    >>> verschiebezahl('Y')
    24
    >>> verschiebezahl('Z')
    25
    >>> 

    """
    return ord(zeichen) - 65

def verschieben(zeichen, schluessel):
    zahl = ord(zeichen) + verschiebezahl(schluessel)
    if zahl > ord('Z'):
        zahl = zahl - 26
    return chr(zahl)

def vigenereText(text,schluesseltext):
    while len(text)>len(schluesseltext):
        schluesseltext=2*schluesseltext
    geheimtext=""
    for i in range(len(text)):
        klarzeichen = text[i]
        schluesselzeichen = schluesseltext[i]
        geheimzeichen = verschieben(klarzeichen,schluesselzeichen)
        geheimtext = geheimtext + geheimzeichen
    return geheimtext

if __name__ == "__main__": 
    doctest.testmod(verbose=False)