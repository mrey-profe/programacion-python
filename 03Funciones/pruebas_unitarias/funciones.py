def es_bisiesto(anho: int) -> bool:
    '''
    Recibe un año y determina si es bisiesto o no.
    
    Parámetros
    ----------
    anho: int
        Año a evaluar.
        
    Devuelve
    -------
    bool
        True si el año es bisiesto, False en caso contrario.
    '''
    if (anho % 4 == 0 and anho % 100 != 0) or anho % 400 == 0:
        return True
    return False