def clasifica_edad(edad: int) -> str | None:
    """Clasifica una edad en niñx, adolescente, adultx o ancianx.

    Args:
        edad (int): La edad a clasificar.

    Returns:
        str: La clasificación de la edad. 'Edad inválida' si la edad es negativa.
        
    >>> clasifica_edad(-1)
    'Edad inválida'
    
    >>> clasifica_edad(0)
    'niñx'
    
    >>> clasifica_edad(5)
    'niñx'
    
    >>> clasifica_edad(12)
    'adolescente'
    
    >>> clasifica_edad(18)
    'adultx'
    
    >>> clasifica_edad(65)
    'ancianx'
    
    >>> clasifica_edad(100)
    'ancianx'
    """
    if edad < 0:
        return 'Edad inválida'
    elif edad < 12:
        return 'niñx'
    elif edad < 18:
        return 'adolescente'
    elif edad < 65:
        return 'adultx'
    else:
        return 'ancianx'