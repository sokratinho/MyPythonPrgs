# Summe der ersten n Zahlen
def summe_rek(n):
    if n == 1:
        return 1
    else:
        return n + summe_rek(n-1)

n = int(input('Gib n ein! '))
print(summe_rek(n))