"""
Definicion de el metodo add_numbers(a,b):
En el que se muestra el empleo de PEP8.
En este se muestra como documentar un metodo y como nombrar tambien.
Empleando una llamada para probar que el codigo esta funcionando
"""

import os
import sys

if sys.stdout.isatty():  # Solo si es una terminal real
    os.system("clear")


def add_numbers(a, b):
    """Add two numbers together.
    result devuelve el valor concatenado
    Parameters:
      a (int or float)
    """

    result = a + b

    return result


if __name__ == "__main__":
    # Llamada al metodo add_numbers()
    NUMBER = add_numbers(500, 151)
    print(NUMBER)
