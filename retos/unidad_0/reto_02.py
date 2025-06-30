"""
Docstrings are strings that appear at the beginning
of a module, class, or function definition.
They provide documentation for the code that follows.
Here's an example of a docstring for the add_numbers() function:

Módulo para realizar operaciones matemáticas básicas.
Este módulo contiene una función que suma dos números y devuelve el resultado.
"""

import os
import sys

if sys.stdout.isatty():  # Solo si es una terminal real
    os.system("clear")


def add_numbers(a, b):
    """
    Add two numbers together.

    Parameters:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.

    Returns:
        int or float: The sum of the two input values.
    """

    result = a + b
    return result


if __name__ == "__main__":
    # Llamada al metodo add_numbers()
    NUMBER = add_numbers(20, 51)
    print(NUMBER)
