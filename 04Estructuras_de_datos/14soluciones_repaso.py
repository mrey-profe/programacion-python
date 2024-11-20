def sumar_elementos(lista: list) -> float:
    """
    Suma los elementos de una lista y devuelve el resultado.
    Args:
        lista (list): Lista de números.
    Returns:
        float: Suma de los elementos de la lista.
    >>> sumar_elementos([1, 2, 3, 4])
    10
    >>> sumar_elementos([1, 2, 3, 4, 5])
    15
    >>> sumar_elementos([])
    0
    """
    suma = 0
    for valor in lista:
        suma += valor
    return suma


def encontrar_extremos(lista: list) -> tuple:
    """
    Encuentra el valor mínimo y máximo de una lista.
    Args:
        lista (list): Lista de números.
    Returns:
        tuple: Tupla con el valor mínimo y máximo de la lista.
    >>> encontrar_extremos([1, 2, 3, 4])
    (1, 4)
    >>> encontrar_extremos([1, 2, 3, 4, 5])
    (1, 5)
    >>> encontrar_extremos([1])
    (1, 1)
    >>> encontrar_extremos([])
    (None, None)
    """
    if len(lista) == 0:
        return None, None
    minimo = lista[0]
    maximo = lista[0]
    for valor in lista:
        if valor < minimo:
            minimo = valor
        if valor > maximo:
            maximo = valor
    return minimo, maximo


def contar_ocurrencias(lista: list, elemento: int) -> int:
    """
    Cuenta las ocurrencias de un elemento en una lista.
    Args:
        lista (list): Lista de números.
        elemento (int): Elemento a contar.
    Returns:
        int: Número de ocurrencias del elemento en la lista.
    >>> contar_ocurrencias([1, 2, 3, 4], 1)
    1
    >>> contar_ocurrencias([1, 2, 3, 4, 1], 1)
    2
    >>> contar_ocurrencias([1, 2, 3, 4], 5)
    0
    """
    contador = 0
    for valor in lista:
        if valor == elemento:
            contador += 1
    return contador


def multiplicar_por_factor(lista: list[float], factor: float) -> list[float]:
    """
    Multiplica los elementos de una lista por un factor.
    Args:
        lista (list): Lista de números.
        factor (float): Factor por el que multiplicar los elementos.
    Returns:
        list: Lista con los elementos multiplicados por el factor.
    >>> multiplicar_por_factor([1, 2, 3, 4], 2)
    [2, 4, 6, 8]
    >>> multiplicar_por_factor([1, 2, 3, 4], 0)
    [0, 0, 0, 0]
    >>> multiplicar_por_factor([], 2)
    []
    """
    resultado = []
    for valor in lista:
        resultado.append(valor * factor)
    return resultado

def multiplicar_por_factor_bis(lista: list[float], factor: float) -> list[float]:
    """
    Multiplica los elementos de una lista por un factor.
    Args:
        lista (list): Lista de números.
        factor (float): Factor por el que multiplicar los elementos.
    Returns:
        list: Lista con los elementos multiplicados por el factor.
    >>> multiplicar_por_factor_bis([1, 2, 3, 4], 2)
    [2, 4, 6, 8]
    >>> multiplicar_por_factor_bis([1, 2, 3, 4], 0)
    [0, 0, 0, 0]
    >>> multiplicar_por_factor_bis([], 2)
    []
    """
    return [valor*factor for valor in lista]

def concatenar_listas(lista1: list, lista2: list) -> list:
    """
    Concatena dos listas.
    Args:
        lista1 (list): Primera lista.
        lista2 (list): Segunda lista.
    Returns:
        list: Lista concatenada.
    >>> concatenar_listas([1, 2, 3], [4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    >>> concatenar_listas([1, 2, 3], [])
    [1, 2, 3]
    >>> concatenar_listas([], [4, 5, 6])
    [4, 5, 6]
    >>> concatenar_listas([], [])
    []
    """
    resultado = []
    for valor in lista1:
        resultado.append(valor)
    for valor in lista2:
        resultado.append(valor)
    return resultado


def concatenar_listas_bis(lista1: list, lista2: list) -> list:
    """
    Concatena dos listas.
    Args:
        lista1 (list): Primera lista.
        lista2 (list): Segunda lista.
    Returns:
        list: Lista concatenada.
    >>> concatenar_listas_bis([1, 2, 3], [4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    >>> concatenar_listas_bis([1, 2, 3], [])
    [1, 2, 3]
    >>> concatenar_listas_bis([], [4, 5, 6])
    [4, 5, 6]
    >>> concatenar_listas_bis([], [])
    []
    """
    return lista1 + lista2


def eliminar_negativos(lista: list) -> list:
    """
    Elimina los números negativos de una lista.
    Args:
        lista (list): Lista de números.
    Returns:
        list: Lista sin números negativos.
    >>> eliminar_negativos([1, -2, 3, -4])
    [1, 3]
    >>> eliminar_negativos([1, 2, 3, 4])
    [1, 2, 3, 4]
    >>> eliminar_negativos([])
    []
    """
    resultado = []
    for valor in lista:
        if valor >= 0:
            resultado.append(valor)
    return resultado


def esta_ordenada(lista: list) -> bool:
    """
    Comprueba si una lista está ordenada de forma ascendente.
    Args:
        lista (list): Lista de números.
    Returns:
        bool: True si la lista está ordenada, False en caso contrario.
    >>> esta_ordenada([1, 2, 3, 4])
    True
    >>> esta_ordenada([1, 2, 3, 4, 1])
    False
    >>> esta_ordenada([1])
    True
    >>> esta_ordenada([])
    True
    """
    for i in range(len(lista)):
        if i != len(lista)-1:  # No es el último
            if lista[i] > lista[i+1]:
                return False
    return True


def intercalar_listas(lista1: list, lista2: list) -> list:
    """
    Intercala los elementos de dos listas.
    Args:
        lista1 (list): Primera lista.
        lista2 (list): Segunda lista.
    Returns:
        list: Lista con los elementos intercalados.
    >>> intercalar_listas([1, 2, 3], [4, 5, 6])
    [1, 4, 2, 5, 3, 6]
    >>> intercalar_listas([1, 2, 3], [])
    [1, 2, 3]
    >>> intercalar_listas([], [4, 5, 6])
    [4, 5, 6]
    >>> intercalar_listas([], [])
    []
    >>> intercalar_listas([1, 2, 3], [4, 5, 6, 7, 8, 9])
    [1, 4, 2, 5, 3, 6, 7, 8, 9]
    """
    mayor = max(len(lista1), len(lista2))
    resultado = []
    for i in range(mayor):
        if i < len(lista1):
            resultado.append(lista1[i])
        if i < len(lista2):
            resultado.append(lista2[i])
    return resultado


def rotar_lista(lista: list, n: int) -> list:
    """
    Rota una lista n posiciones a la izquierda.
    Args:
        lista (list): Lista de números.
        n (int): Número de posiciones a rotar.
    Returns:
        list: Lista rotada.
    >>> rotar_lista([1, 2, 3, 4], 1)
    [2, 3, 4, 1]
    >>> rotar_lista([1, 2, 3, 4], 2)
    [3, 4, 1, 2]
    >>> rotar_lista([1, 2, 3, 4], 3)
    [4, 1, 2, 3]
    """
    resultado = []
    for i in range(n, len(lista)):
        resultado.append(lista[i])
    for i in range(n):
        resultado.append(lista[i])
    return resultado
