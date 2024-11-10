from typing import Tuple, Union


def imprime_menu():
    """Imprime el menú de opciones."""
    print('''MENÚ
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir
Elija una opción:
          ''')


def escoger_opcion() -> int:
    """Permite escoger la opción del menú.

    Returns:
        int: La opción escogida.
    """
    correcta = False
    while not correcta:
        imprime_menu()
        opcion = int(input())
        if opcion >= 1 and opcion <= 5:  # Correcta
            correcta = True
    return opcion


def pedir_operandos() -> Tuple[float, float]:
    """Pide los operandos al usuario.

    Returns:
        tuple: Los operandos introducidos por el usuario.
    """
    op1 = float(input("Escribe el primer operando: "))
    op2 = float(input("Escribe el segundo operando: "))
    return op1, op2


def sumar(op1: float, op2: float) -> float:
    """Suma dos números.

    Args:

        op1 (float): El primer operando.
        op2 (float): El segundo operando.

    Returns:
        float: La suma de los operandos.

    >>> sumar(2, 3)
    5
    >>> sumar(-2, 3)
    1
    """
    return op1 + op2


def restar(op1: float, op2: float) -> float:
    """Resta dos números.

    Args:

        op1 (float): El primer operando.
        op2 (float): El segundo operando.

    Returns:
        float: La resta de los operandos.

    >>> restar(2, 3)
    -1
    >>> restar(-2, 3)
    -5
    >>> restar(8, 2)
    6
    """
    return op1 - op2


def multiplicar(op1: float, op2: float) -> float:
    """Multiplica dos números.

    Args:
        op1 (float): El primer operando.
        op2 (float): El segundo operando.

    Returns:
        float: La multiplicación de los operandos.

    >>> multiplicar(2, 3)
    6
    >>> multiplicar(-2, 3)
    -6
    >>> multiplicar(8, 0)
    0
    """
    return op1 * op2


def dividir(op1: float, op2: float) -> Union[float, None]:
    """Divide dos números.

    Args:
        op1 (float): El primer operando.
        op2 (float): El segundo operando.

    Returns:
        float: La división de los operandos.

    >>> dividir(2, 3)
    0.6666666666666666
    >>> dividir(-2, 3)
    -0.6666666666666666
    >>> dividir(8, 2)
    4.0
    >>> dividir(8, 0)
    No se puede dividir entre 0
    """
    if op2 != 0:
        return op1 / op2
    else:
        print("No se puede dividir entre 0")

# Programa principal


opcion = 1
while opcion != 5:
    opcion = escoger_opcion()
    if opcion >= 1 and opcion <= 4:
        op1, op2 = pedir_operandos()
        if opcion == 1:
            resultado = sumar(op1, op2)
        elif opcion == 2:
            resultado = restar(op1, op2)
        elif opcion == 3:
            resultado = multiplicar(op1, op2)
        elif opcion == 4:
            resultado = dividir(op1, op2)

    if (resultado is not None):
        print(round(resultado, 2))