def is_isogram(string):
    string = string.lower()
    resultado = ""
    for letra in string:
        if letra not in resultado:
            resultado += letra
    if resultado == string:
        return True
    else:
        return False
    
print(is_isogram("Dermatoglyphics"))