def factorial(n: int) -> int:
    """Calcula el factorial de un número entero positivo.

    Args:
        n (int): El número entero positivo del que se quiere calcular el factorial.

    Returns:
        int: El factorial de n.
        
    >>> factorial(5)
    120
    
    >>> factorial(0)
    1
    
    >>> factorial(1)
    1
    
    >>> factorial(2)
    2
    
    >>> factorial(20)
    2432902008176640000
    """
    factorial = 1
    for i in range(2, n+1):
        factorial *= i
    return factorial
