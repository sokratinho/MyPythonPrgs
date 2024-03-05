def geheimbuchstabe(zeichen,schlüssel):
    ascii = ord(zeichen)
    if (ascii>64 and ascii < 91) or (ascii>96 and ascii<123):
        neues_ascii = ascii+schlüssel
        if (neues_ascii>90 and neues_ascii<(91+schlüssel)) or (neues_ascii>122 and neues_ascii<(123+schlüssel)):
            neues_ascii -= 26
    return chr(neues_ascii)

def caesar(text, schlüssel):
    if len(text)==0:
        return ''
    else:
        return geheimbuchstabe(text[0],schlüssel)+caesar(text[1:],schlüssel) 


original_text = input("Geben Sie bitte den Text ein: ")
key=int(input("Geben Sie die Codierung ein (1-20):"))
print('Das Wort lautet verschlüsselt: '+caesar(original_text,key))
