# Crea un programa que pregunte al usuario 
# las notas de 10 alumnos y los guarde en una lista.

notas = []

for i in range(5):
    nota = float(input("Dime una nota: "))
    notas.append(nota)
    # notas.insert(0, nota) # Si queremos que se añada al principio

print(notas)