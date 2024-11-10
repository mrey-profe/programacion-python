import random

def aleatorio(min: int, max: int) -> int:
    """Genera un número aleatorio entre min y max (ambos incluidos).

    Args:
        min (int): El valor mínimo del rango.
        max (int): El valor máximo del rango.

    Returns:
        int: El número aleatorio generado.
        
    >>> 0 <= aleatorio(0, 10) <= 10
    True
    
    >>> 0 <= aleatorio(0, 1000) <= 1000
    True
    """
    return random.randint(min, max)