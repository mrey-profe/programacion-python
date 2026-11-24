def horas_paro_totais(dias: int, horas_iniciais: int, incremento: int) -> int:
    """
    Calcula o total de horas de paro dunha folga escalonada: o primeiro día
    párase horas_iniciais e cada día seguinte o paro aumenta en incremento
    horas, sen superar nunca as 8 horas diarias.

    Parámetros:
    - dias (int): número de días que dura a folga. Debe ser polo menos 1.
    - horas_iniciais (int): horas de paro do primeiro día, entre 1 e 8.
    - incremento (int): horas que se engaden ao paro cada día (non negativo).

    Devolve:
    - int: total de horas de paro da folga, ou -1 se os datos non son válidos.

    >>> horas_paro_totais(4, 1, 0)
    4
    >>> horas_paro_totais(3, 2, 1)
    9
    >>> horas_paro_totais(5, 2, 2)
    28
    >>> horas_paro_totais(10, 1, 3)
    68
    >>> horas_paro_totais(0, 2, 2)
    -1
    >>> horas_paro_totais(3, 9, 1)
    -1
    """
    if dias < 1 or horas_iniciais < 1 or horas_iniciais > 8:
        return -1
    horas_paro_dia = horas_iniciais
    horas_totais = 0
    for i in range(dias):
        horas_totais += horas_paro_dia
        horas_paro_dia += incremento
        if horas_paro_dia > 8:
            horas_paro_dia = 8
    return horas_totais

print(horas_paro_totais(5, 2, 3))