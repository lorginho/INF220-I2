codigo 01

Definicion de el metodo adicionar numero, en el que se muestra el empleo de PEP8. En este se muestra como documentar un metodo y como nombrar tambien. Empleando una llamada para probar que el codigo esta funcionando


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


codigo 02

Docstrings Docstrings are strings that appear at the beginning of a module, class, or function definition. They provide documentation for the code that follows. Here's an example of a docstring for the add_numbers() function:


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

codigo 03

""" Liberia time forma de importar una liberia """
import time


class Timer:
    #
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        print(f"Time taken: {end_time - self.start_time} seconds")

with Timer():
    # Code to be timed goes here
    pass

codigo 04

Mostrar mensaje aplicando style code pep8 en python empleando metodo greet.


def greet(name):
    """Greets the user with a personalized message.

    Args:
        name: The name of the user to greet.

    Returns:
        A string containing the greeting message.
    """

    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, world!"


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greeting = greet(user_name)
    print(greeting)
