print("Introduce tu fecha de nacimiento:")
dia = int(input("Día: "))
mes = int(input("Mes: "))
anho = int(input("Año: "))

suma = dia + mes + anho
num_suerte = 0

while suma != 0:
    cifra = suma % 10
    suma = suma // 10
    num_suerte += cifra # num_suerte = num_suerte + cifra

print(num_suerte)