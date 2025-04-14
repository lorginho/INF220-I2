## Retos: Ejercicios propuestos Sobre estandares y buenas practicas

Trabajo: 

Realizar una practica basada en estilos de codigos de python y ejecutar las siguientes intrucciones que permita escribir un codigo legible para usuarios y desarrolladores .

Usaremos el Sistema Operativo Fedora Linux para desarrollar el lenguaje de programación Python, las preguntas serán descritas en la plantilla del enlace que esta mas adelante.

Presentación: Presentar el codigo en la siguiente plataforma:  Laboratorio

https://colab.research.google.com/drive/1WNCazsF8YFb4FoYO_lT6fTyhM7MyJWDc?usp=sharing#scrollTo=IkvZ6KPDDOJb

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



Recursos para la tareas: 
---

### **1. Conceptos Clave de PEP 8**

Aquí tienes una lista de las pautas más importantes de PEP 8 que debes tener en cuenta al escribir tu código:

1. **Indentación:**
   - Usa **4 espacios** por nivel de indentación.
   - No mezcles espacios y tabs.

2. **Líneas Largas:**
   - Limita las líneas a un máximo de **79 caracteres**.
   - Si una línea es demasiado larga, puedes dividirla en varias líneas usando paréntesis o el operador de continuación (`\`).

3. **Nombres de Variables y Funciones:**
   - Usa `snake_case` para nombres de variables y funciones (todo en minúsculas, separado por guiones bajos).
   - Ejemplo: `calcular_promedio`, `lista_numeros`.

4. **Nombres de Clases:**
   - Usa `CamelCase` para nombres de clases (la primera letra de cada palabra en mayúscula).
   - Ejemplo: `MiClase`, `CalculadoraAvanzada`.

5. **Espacios en Blanco:**
   - Usa espacios alrededor de operadores (`=`, `+`, `-`, etc.) y después de comas.
   - No uses espacios alrededor de paréntesis, corchetes o llaves.

6. **Comentarios:**
   - Escribe comentarios claros y concisos.
   - Los comentarios deben explicar el **por qué** y no el **qué** (el código en sí ya explica lo que hace).

7. **Docstrings:**
   - Documenta funciones, clases y módulos con **docstrings**.
   - Usa el formato de docstring de triple comilla (`"""`).

8. **Manejo de Errores:**
   - Usa excepciones para manejar errores de manera adecuada.
   - Proporciona mensajes de error claros y útiles.

---

### **2. Pasos para Cumplir con PEP 8 en tu Tarea**

Aquí te dejo una guía paso a paso para que puedas aplicar PEP 8 en tu tarea sin necesidad de que te proporcione código:

1. **Define el Propósito de la Función:**
   - Piensa en qué debe hacer la función (por ejemplo, calcular el área de un rectángulo).
   - Escribe una descripción clara de la función en forma de docstring.

2. **Elige Nombres Descriptivos:**
   - Usa nombres descriptivos para la función y sus parámetros.
   - Asegúrate de que los nombres sigan las convenciones de PEP 8 (`snake_case` para funciones y variables).

3. **Estructura la Función:**
   - Usa una indentación de 4 espacios.
   - Divide el código en bloques lógicos (por ejemplo, validación de entrada, cálculo, retorno del resultado).

4. **Maneja Errores:**
   - Valida los parámetros de entrada (por ejemplo, asegúrate de que los valores sean positivos).
   - Usa excepciones para manejar casos inválidos.

5. **Comenta el Código:**
   - Agrega comentarios para explicar partes del código que puedan no ser obvias.
   - Asegúrate de que los comentarios sean útiles y no redundantes.

6. **Prueba la Función:**
   - Escribe un pequeño bloque de código para probar la función con diferentes valores de entrada.
   - Asegúrate de que la función maneje correctamente casos válidos e inválidos.

---

### **3. Preguntas para Guiarte**

Aquí tienes algunas preguntas que puedes hacerte mientras escribes tu código para asegurarte de que cumple con PEP 8:

1. **Nombres:**
   - ¿Los nombres de las variables y funciones son descriptivos y siguen `snake_case`?
   - ¿Los nombres de las clases (si las hay) siguen `CamelCase`?

2. **Formato:**
   - ¿El código está correctamente indentado (4 espacios por nivel)?
   - ¿Las líneas tienen menos de 79 caracteres?

3. **Espacios en Blanco:**
   - ¿Hay espacios alrededor de operadores y después de comas?
   - ¿No hay espacios innecesarios alrededor de paréntesis, corchetes o llaves?

4. **Documentación:**
   - ¿La función tiene un docstring que explica su propósito, parámetros y valor de retorno?
   - ¿Los comentarios son claros y útiles?

5. **Manejo de Errores:**
   - ¿La función valida los parámetros de entrada?
   - ¿Se manejan adecuadamente los casos inválidos con excepciones?

---

### **4. Recursos Adicionales**

Si quieres profundizar en PEP 8, aquí tienes algunos recursos útiles:

1. **Documentación Oficial de PEP 8:**
   - [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

2. **Herramientas para Verificar PEP 8:**
   - **`pylint`:** Un linter que verifica el estilo y la calidad del código.
   - **`flake8`:** Una herramienta que combina verificaciones de estilo, lógica y complejidad.
   - **`autopep8`:** Una herramienta que formatea automáticamente el código para cumplir con PEP 8.

---
