def umdrehen(wort):
    if len(wort)==1:
        return wort[0]
    else:
        return umdrehen(wort[1:])+wort[0]
    
print(umdrehen('Leben'))