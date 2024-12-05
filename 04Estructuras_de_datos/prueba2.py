def validar_ean(codigo: str) -> bool:
    """
    Verifica si un código de barras EAN-8 o EAN-13 tiene un dígito de control válido.

    Parámetros:
    codigo (str): Cadena que representa el código de barras EAN (8 o 13 dígitos).

    Devuelve:
    bool: True si el código de barras tiene un dígito de control válido; False en caso contrario.

    Ejemplos:
    >>> validar_ean("65839522")
    True
    >>> validar_ean("8414533043847")
    True
    >>> validar_ean("12345678")
    False
    >>> validar_ean("4006381333931")
    True
    >>> validar_ean("00000000")
    True
    """
    suma = 0
    for i in codigo[-2::-2]:
        suma += int(i)*3

    for i in codigo[-3::-2]:
        suma += int(i)

    unidades = int(str(suma)[-1])
    unidades = suma % 10
    cod_control = 10 - unidades else 0

    # if suma > round(suma, -1):
    #     redondeo = round(suma, -1) + 10
    # else:
    #     redondeo = round(suma, -1)

    # cod_control = redondeo - suma
    return codigo[-1::] == str(cod_control)

validar_ean("65839522")