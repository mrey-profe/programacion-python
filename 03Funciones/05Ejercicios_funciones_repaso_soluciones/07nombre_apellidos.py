def nombre_completo(nombre: str, apellido1: str, apellido2: str = "") -> str:
    """Devuelve el nombre completo de una persona.

    Args:
        nombre (str): El nombre de la persona.
        apellido1 (str): El primer apellido de la persona.
        apellido2 (str): El segundo apellido de la persona.

    Returns:
        str: El nombre completo de la persona.

    >>> nombre_completo('María', 'García', 'Pérez')
    'María García Pérez'
    
    >>> nombre_completo('Juan', 'Gómez', 'Gómez')
    'Juan Gómez Gómez'
    
    >>> nombre_completo('Luis', 'Gómez')
    'Luis Gómez'
    """
    if apellido2: # Si apellido2 no es una cadena vacía, equivale a apellido2 != ""
        return nombre + ' ' + apellido1 + ' ' + apellido2
    else:
        return nombre + ' ' + apellido1