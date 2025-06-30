"""
Módulo que utiliza el metodo greet, al cual se pasa como arguemento
un nombre, luego se saluda por consola utilizando el argumento
"""

import os
import sys

if sys.stdout.isatty():  # Solo si es una terminal real
    os.system("clear")


def greet(name):
    """
    Greets the user with a personalized message.

    Args:
        name (str): The name of the user to greet.

    Returns:
        str: A string containing the greeting message.
    """
    if name.strip():  # Elimina espacios en blanco
        return f"Hello, {name}!"


if __name__ == "__main__":
    # Elimina espacios en blanco al principio y al final
    user_name = input("Enter your name: ").strip()
    GREETING = greet(user_name)
    print(GREETING)
