# Eliminar todos los elementos de una lista que son múltiplos de 5

lista = [1, 2, 16, 15, 34, 25, 10]

i = 0

while i < len(lista):
    if lista[i] % 5 == 0:
        del lista[i] # Cuando borro un elemento no incremento el índice porque el siguiente elemento pasa a ocupar la posición del borrado
    else:
        i += 1 

print(lista)