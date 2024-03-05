def ersetze(wort,b,c):
    if len(wort)==0:
        return ''
    else:
        if wort[0]==b:
            return c+ersetze(wort[1:],b,c)
        else:
            return wort[0]+ersetze(wort[1:],b,c)

MeinWort=input('Gib das Wort ein:')
b=input('Welchen Buchstaben ersetzen:')
c=input('Durch welchen Buchstaben ersetzen:')
print('Der Buchstabe '+b+' wurde durch '+c+'ersetzt: '+ersetze(MeinWort,b,c))