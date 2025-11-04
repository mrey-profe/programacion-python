def contar_opcions(escollas: list[str]) -> dict[str,int]:
    """Conta o número de veces que se escolle cada opción.

    Args:
        escollas (list[str]): As escollas dos asistentes

    Returns:
        dict[str,int]: Un diccionario no que as claves son as escollas e o valor o número de veces que se escollen
    >>> contar_opcions(["marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura"])
    {'marisco': 9, 'carne': 9, 'pescado': 9, 'pavo': 9, 'verdura': 9}
    >>> contar_opcions(["marisco", "carne", "carne", "pescado"])
    {'marisco': 1, 'carne': 2, 'pescado': 1}
    >>> contar_opcions(['marisco', 'carne', 'pescado'])
    {'marisco': 1, 'carne': 1, 'pescado': 1}
    """
    resultado = {}
    for opcion in escollas:
        if opcion not in resultado:
            resultado[opcion] = 1
        else:
            resultado[opcion] += 1
    return resultado

def determinar_maioría(opcions: tuple[str, ...], escollas: list[str]) -> str:
    """
    Determina a opción máis escollida dunha lista de escollas.
    
    Args:
        opcions (list[str]): Lista de opcións posibles.
        escollas (list[str]): Lista de escollas realizadas.
        
    Returns:
        str: A opción máis escollida.
        
    >>> determinar_maioría(("marisco", "carne", "pescado", "pavo", "verdura"), ["marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura"])
    'marisco'
    >>> determinar_maioría(("marisco", "carne", "pescado", "pavo", "verdura"), ["marisco", "carne", "carne", "pescado"])
    'carne'
    >>> determinar_maioría(("marisco", "carne", "pescado", "pavo", "verdura"), ["marisco", "carne", "pescado"])
    'marisco'
    """
    ganadora = opcions[0]
    for opcion in opcions:
        if escollas.count(opcion) > escollas.count(ganadora):
            ganadora = opcion
    return ganadora

    # contador = [0 for i in range(len(opcions))]
    # for escolla in escollas:
    #     posicion = opcions.index(escolla)
    #     contador[posicion] += 1
    # return opcions[contador.index(max(contador))]
    #
    # contador = []
    # for escolla in escollas:
    #     contador.append(escollas.count(escolla))
    # mas_popular = contador.index(max(contador))
    # return escollas[mas_popular]

determinar_maioría(("marisco", "carne", "pescado", "pavo", "verdura"), ["marisco", "carne", "carne", "pescado"])

opcions = ("marisco", "carne", "pescado", "pavo", "verdura")

escollas = []
resposta = "s"
while resposta == "s":
    print("Benvido á aplicación para seleccionar a cea de fin de ano, faga a súa escolla:")
    for i in range(len(opcions)):
        print(i, ". ", opcions[i], sep="")
    valor = int(input("Escolla unha opción: "))
    escollas.append(opcions[valor])
    resposta = input("Quere seguir escollendo? (s/n): ")
print(escollas)