def lösche(wort,b):
    if len(wort)==0:
        return ''
    else:
        if wort[0]==b:
            return lösche(wort[1:],b)
        else:
            return wort[0]+lösche(wort[1:],b)

MeinWort=input('Gib das Wort ein:')
b=input('Welchen Buchstaben löschen:')
print('Der Buchstabe '+b+' wurde gelöscht: '+lösche(MeinWort,b))