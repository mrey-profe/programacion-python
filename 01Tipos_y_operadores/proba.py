año = int(input("Dime un año: "))
resto = año % 4
resto_bisiesto = resto % 400
if resto == 0:
    if resto_bisiesto == 0:
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
else:
    print("El año no es bisiesto")