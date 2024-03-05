def verdoppeln_rek(text):
    if (len(text) == 1):
        return text[0]+text[0]
    else:
        return text[0]+text[0]+verdoppeln_rek(text[1:])
    
print(verdoppeln_rek('abcd'))