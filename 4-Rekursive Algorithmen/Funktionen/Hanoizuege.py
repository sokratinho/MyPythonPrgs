#Türme von Hanoi
def hanoizuege(n, von, ueber, nach):
    if n == 1:
        print(von + ' '+chr(8594)+' '+ nach)
    else:
        hanoizuege(n-1, von, nach, ueber)
        print(von + ' '+chr(8594)+' '+ nach)
        hanoizuege(n-1, ueber, von, nach)
    
hanoizuege(3, '1','2','3')