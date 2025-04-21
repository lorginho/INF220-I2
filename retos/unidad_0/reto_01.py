"""
Módulo para realizar operaciones matemáticas básicas.

Este módulo contiene una función que suma dos números y devuelve el resultado.
"""

def add_numbers(a, b):
    """
    Suma dos números y devuelve el resultado.

    Parameters:
        a (int or float): El primer número a sumar.
        b (int or float): El segundo número a sumar.

    Returns:
        int or float: El resultado de la suma de `a` y `b`.
    """

    result = a + b

    return result

if __name__ == "__main__":
    # Llamada a la función add_numbers()
    resultado_suma = add_numbers(100, 223)
    print(resultado_suma)
