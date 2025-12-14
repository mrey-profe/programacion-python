import json

def escolle_departamento(lista_departamentos):
    eleccion = -1
    while eleccion < 0 or eleccion >= len(lista_departamentos):
        print("Departamentos dispoñibles:")
        for i in range(len(lista_departamentos)):
            print(f"{i + 1}. {lista_departamentos[i].strip()}")
        eleccion = int(input("Elixe un departamento: ")) - 1
    return lista_departamentos[eleccion].strip()


with open("departments.txt", "r", encoding="utf-8") as ficheiro:
    lista_departamentos = ficheiro.readlines()

with open("profesores.json", "r", encoding="utf-8") as ficheiro_json:
    profes = json.load(ficheiro_json)

opcion = 0

while opcion != 3:
    print(profes)
    print(lista_departamentos)
    print("1. Engadir profe")
    print("2. Engadir departamento")
    print("3. Saír")
    opcion = int(input("Elixe unha opción: "))


    match opcion:
        case 1:
            datos_profe = {}
            datos_profe["nome"] = input("Nome: ")
            datos_profe["apellidos"] = input("Apelidos: ")
            departamento = escolle_departamento(lista_departamentos)
            print(datos_profe)
            if departamento not in profes:
                profes[departamento] = []
            profes[departamento].append(datos_profe)
        case 2:
            departamento_novo = input("Di un novo departamento: ")
            lista_departamentos.append(departamento_novo + "\n")
            with open("departments.txt", "a", encoding="utf-8") as ficheiro:
                ficheiro.write("\n" + departamento_novo)
                
            
with open("profesores.json", "w", encoding="utf-8") as ficheiro_json:
    json.dump(profes, ficheiro_json)            
