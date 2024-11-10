def sumatorio_divisores(n: int) -> int:
    """Calcula la suma de los divisores de un número entero positivo, salvo él mismo.
    
    Args:
        n (int): El número entero positivo del que se quieren calcular los divisores.
        
    Returns:
        int: La suma de los divisores de n.
        
    >>> sumatorio_divisores(6)
    6
    >>> sumatorio_divisores(28)
    28
    >>> sumatorio_divisores(220)
    284
    """
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def son_amigos(a: int, b: int) -> bool:
    """Comprueba si dos números enteros positivos son amigos.
    
    Dos números son amigos si la suma de los divisores de uno es igual al otro y viceversa.
    
    Args:
        a (int): El primer número entero positivo.
        b (int): El segundo número entero positivo.
        
    Returns:
        bool: True si los números son amigos, False en caso contrario.
    
    >>> son_amigos(220, 284)
    True
    >>> son_amigos(1184, 1210)
    True
    >>> son_amigos(2620, 2924)
    True
    >>> son_amigos(5020, 5564)
    True
    >>> son_amigos(6232, 6368)
    True
    >>> son_amigos(10744, 10856)
    True
    >>> son_amigos(17296, 18416)
    True
    >>> son_amigos(220, 1000)
    False
    >>> son_amigos(220, 285)
    False
    >>> son_amigos(3, 28)
    False
    """
    return sumatorio_divisores(a) == b and sumatorio_divisores(b) == a