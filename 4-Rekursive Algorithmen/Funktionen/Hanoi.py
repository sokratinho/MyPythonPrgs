#Türme von Hanoi
def hanoi(n):
    if n == 1:
        return 1
    else:
        return 1 + 2*hanoi(n-1)
    
n = int(input('Gib n ein! '))
print('Man braucht ',hanoi(n),' Züge!')