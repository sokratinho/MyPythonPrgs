#PGM-Pixelgrafik
kennzeichnung = "P2"
kommentar ="# haus.pgm"
spalten = 5
zeilen = 8
graustufen = 15
bilddaten = [15, 15, 8, 15, 15,
15, 8, 8, 8, 15,
8, 8, 8, 8, 8,
12, 12, 12, 12, 12,
12, 5, 12, 5, 12,
12, 12, 12, 12, 12,
12, 5, 12, 5, 12,
12, 12, 12, 12, 12]

PGMDemoGrafik = (kennzeichnung, kommentar,spalten,zeilen,graustufen,bilddaten)

def invertiereBilddaten(pPixelliste,pGraustufen):
    for i in pPixelliste:
        pPixeliste[i] = pGraustufen - pPixelliste[i]
    return pPixelliste

def invertierePGM(pPGMGrafik):
    #Entpacken der Grafikdatei
    Graustufen = pPGMGrafik[4]
    Pixelliste = pPGMGrafik[5]
    PixellisteNeu = invertiereBilddaten(Pixelliste[:],Graustufen)
    #Neues Objekt erzeugen
    return  (pPGMGrafik[0], pPGMGrafik[1], pPGMGrafik[2], pPGMGrafik[3],
              pPGMGrafik[4], PixellisteNeu)

#Umwandeln des Objekts in einen String
#def PGMtoString(pPGMGrafik,pString):
    
    
#Abspeichern PGM
def speicherePGM(pPGMGrafik,pdateiName):
    pQuelltext =''
    datei = open(pdateiname+'.pgm','w',encoding='iso-8859-1')
    #Entpacken der Grafikdatei
    kennzeichnung = pPGMGrafik[0]
    kommentar = pPGMGrafik[1]
    Spalten = pPGMGrafik[2]
    Zeilen = pPGMGrafik[3]
    Graustufen = pPGMGrafik[4]
    Pixelliste = pPGMGrafik[5]
    #Den zu speichernden String erzeugen

    pQuelltext = kennzeichnung + ' ' + kommentar + ' '
    + Spalten + ' ' + Zeilen + ' 'Spalten + ' ' + Graustufen
    for i in Pixelliste:
        pQuelltext = pQuelltext + ' ' + Pixelliste[i]
    #Objekt in die Datei schreiben
    datei.write(pQelltext)
    datei.close()
    
