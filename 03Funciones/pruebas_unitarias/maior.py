def e_maior_idade(idade: int) -> bool:
    '''
    Permite comprobar se unha persoa é ou non maior de idade.

    Parámetros:
    idade: int
       A idade da persoa.
    
    Devolve:
    bool
       True se é maior de idade e False en caso contrario.

    >>> e_maior_idade(15)
    False
    >>> e_maior_idade(20)
    True
    >>> e_maior_idade(18)
    True
    '''
    if idade >= 18: #Isto está mal
        return True
    else:
        return False