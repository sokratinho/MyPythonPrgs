#Promillerechner Stg
geschlecht='x'
erwachsen='x'
antwort='x'
print('Krasser Promillerechner by Stg')
while not geschlecht in ['m','w','d']:
    geschlecht = input('Moin Digger, bist du männlich/weiblich/divers (m/w/d)?')
while not antwort in ['j','n']:  
    antwort = input('Und schon erwachsen? (j/n)')
    if antwort == 'j':
        erwachsen = True
    else:
        erwachsen = False
liter = float(input('Wie viel Liter hast du weggekippt?'))
print('Echt jetzt!?')
alkanteil = float(input('Wie hochprozentig war das Getränk?'))
gewicht = float(input('Alder, was wiegst du ohne Klamotten (in kg)?'))
if geschlecht == 'm' and erwachsen:
    faktor = 0.7
else:
    faktor == 0.6 # noch genauer
alkoholmenge = 10 * liter * alkanteil * 0.8
konzentration = alkoholmenge * (gewicht *faktor)
print('Du hast ',konzentration,' Promille Alk im Blut!')
if konzentration > 0.5:
    print('Auf keinen Fall mehr fahren!')
else:
    print('Du kannst noch fahren!')  
