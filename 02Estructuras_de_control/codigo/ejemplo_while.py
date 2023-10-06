hay_negativos = False

for i in range(10):
    numero = int(input("Escribe un número: "))
    if (numero < 0):
        hay_negativos = True

if hay_negativos: # if hay_negativos == True
    print("Hay negativos")
else:
    print("No hay negativos")