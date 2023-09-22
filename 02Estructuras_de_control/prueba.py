def longest(a1, a2):
    resultado = a2
    for letra in a1:
        print(letra)
        if letra not in resultado:
            resultado += letra
    
    print(resultado)
    array = resultado.split()
    
    print(resultado)

    resultado_ord = "".join(array.sort())
    return resultado_ord

print(longest("aretheyhere", "yestheyarehere"))