def es_par(num: int) -> bool:
    '''
    Función que determina se un número é ou non par.

    Parámetros:
    num: int
        Número a determinar a paridade.

    Devolve:
    bool
        True se o número é par, False se é impar

    >>> es_par(4)
    True
    >>> es_par(5)
    False
    >>> es_par(0)
    True
    '''
    # Opción 1
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False
    # Opción 2
    #return True if num % 2 == 0 else False
    return num % 2 == 0