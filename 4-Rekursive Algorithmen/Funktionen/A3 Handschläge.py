#Handschläge
def handschlag(n):
    if n == 2:
        return 1
    else:
        return (n-1) + handschlag(n-1)
    
n = int(input('Gib die Anzahl der Personen ein:'))    
print(handschlag(n))