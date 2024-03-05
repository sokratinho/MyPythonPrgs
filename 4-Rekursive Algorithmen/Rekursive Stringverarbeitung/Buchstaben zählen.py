def zaehle(wort,b):
    if len(wort)==0:
        return 0
    else:
        if wort[0]==b:
            return zaehle(wort[1:],b)+1
        else:
            return zaehle(wort[1:],b)

MeinWort=input('Gib das Wort ein:')
b=input('Welchen Buchstaben suchen:')
print('Der Buchstabe '+b+' kommt '+str(zaehle(MeinWort,b))+' vor!')