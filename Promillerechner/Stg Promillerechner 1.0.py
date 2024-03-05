#Promillerechner Stg
geschlecht='x'
antwort='x'
antwort2='x'
print('Krasser Promillerechner by Stg')
while not geschlecht in ['m','w','d']:
    geschlecht = input('Moin Digger, bist du männlich/weiblich/divers (m/w/d)?')
while not antwort in ['j','n']:  
    antwort = input('Und schon erwachsen? (j/n)')
    if antwort == 'j':
        erwachsen = True
    else:
        erwachsen = False
while not antwort2 in ['j','n']:
    antwort2 = input('Probezeit schon vorbei? (j/n)')
    if antwort2 == 'j':
        probezeitvorbei = True
    else:
        probezeitvorbei = False    
    geschlecht = input('Moin Digger, bist du männlich/weiblich/divers (m/w/d)?')
liter = float(input('Wie viel Liter hast du weggekippt?'))
print('Echt jetzt!?')
alkanteil = float(input('Wie hochprozentig war das Getränk?'))
gewicht = float(input('Alder, was wiegst du ohne Klamotten (in kg)?'))
if geschlecht == 'm' and erwachsen:
    faktor = 0.7
else:
    faktor == 0.6 # noch genauer
alkoholmenge = 10 * liter * alkanteil * 0.8
konzentration = alkoholmenge / (gewicht *faktor)
konzentration = round(100*konzentration)/100
print('Du hast ',konzentration,' Promille Alk im Blut!')
#Überprüfen
if konzentration = 0 or (konzentration <= 0.5 and probezeitvorbei):
    print('Du kannst noch fahren!')    
else:
    print('Auf keinen Fall mehr fahren!')
 
