# Fakultät rekursiv
def fak_rek(n):
    if n == 1:
        return 1
    else:
        return n*fak_rek(n-1)

n = int(input('Gib n ein! '))
print('Die Fakultät ist: ',fak_rek(10))