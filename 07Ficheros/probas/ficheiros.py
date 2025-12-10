import csv

with open("datos.txt", "r", encoding="utf-8") as ficheiro:
    instituto = ficheiro.readline().strip()
    curso = ficheiro.readline().strip()
    ciclo = ficheiro.readline().strip()
    aula = ficheiro.readline().strip()

print(f"Curso {curso} de {ciclo} do {instituto}, na aula {aula}")


with open("nomes.txt", "r", encoding="utf-8") as ficheiro:
    # for linea in ficheiro:
    #     linea = linea.strip()
    #     partes = linea.split(", ")
    #     print(partes[-1])
    nomes = ficheiro.readlines()
    #mostrar o último nome
    print(nomes[-3].strip().split(", ")[-1])
    #print(nomes)

nomes = ["Ana", "Pedro", "María"]

with open("nome.txt", "w", encoding="utf-8") as ficheiro:
    #ficheiro.write("1º DAW")
    ficheiro.writelines("\n".join(nomes))

with open("proba.csv", "r", newline="") as ficheiro:
    lector = csv.reader(ficheiro)
    for linea in lector:
        print(linea[0])