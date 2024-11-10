def celsius_a_fahrenheit(graos: float) -> float:
    """Convirte graos Celsius a Fahrenheit

    Args:
        graos (float): Os graos Celsius a converter

    Returns:
        float: Os graos Fahrenheit

    >>> celsius_a_fahrenheit(0)
    32.0
    >>> celsius_a_fahrenheit(100)
    212.0
    >>> celsius_a_fahrenheit(-40)
    -40.0
    >>> celsius_a_fahrenheit(37)
    98.6
    >>> celsius_a_fahrenheit(-10)
    14.0
    """
    return (graos * 9 / 5) + 32