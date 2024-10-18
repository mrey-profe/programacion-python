numero_max = int(input("Escribe un número y te diré cuántos primos menores que él existen: "))
contador = 0

for numero in range(1, numero_max + 1):
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0: #É divisible
            es_primo = False
            break
    if es_primo:
        contador += 1