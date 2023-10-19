limite = int(input("Introduce el límite superior para bucar números primos:"))
contador = 0

for numero in range(1, limite + 1):
    primo = True
    for i in range (2, numero):
        if numero % i == 0: # Hemos encontrado un divisor
            primo = False
            break
    if primo:
        contador += 1

print("Hay", contador, "primos.")