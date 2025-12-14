import csv

with open('students.csv', newline='') as ficheiro_estudantes:
    estudantes = csv.reader(ficheiro_estudantes)
    estudantes_sobresaintes = []
    for estudante in estudantes:
        print(estudante)
        if float(estudante[4]) > 7:
            estudantes_sobresaintes.append(estudante)
            
print(estudantes_sobresaintes)
with open('outstanding_students.csv', 'w', newline='') as ficheiro_sobresaintes:
    escritor = csv.writer(ficheiro_sobresaintes)
    escritor.writerows(estudantes_sobresaintes)