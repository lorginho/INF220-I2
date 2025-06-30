"""
Módulo para medir el tiempo de ejecución de un bloque de código.

Este módulo utiliza la librería `time` y una clase `Timer` que actúa como un
context manager para medir el tiempo transcurrido.
"""

import os
import sys
import time

if sys.stdout.isatty():  # Solo si es una terminal real
    os.system("clear")


class Timer:
    """
    Context manager para medir el tiempo de ejecución de un bloque de código.

    Ejemplo de uso:
        with Timer():
            # Código a medir
            pass
    """

    def __enter__(self):
        """
        Inicia el temporizador al entrar en el bloque `with`.

        Returns:
            self: La instancia de Timer.
        """
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Detiene el temporizador y muestra el tiempo transcurrido
        al salir del bloque `with`.

        Args:
            exc_type: Tipo de excepción (si ocurre).
            exc_val: Valor de la excepción (si ocurre).
            exc_tb: Traceback de la excepción (si ocurre).
        """
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"Tiempo transcurrido: {elapsed_time:.4f} segundos")


if __name__ == "__main__":
    # Ejemplo de uso
    with Timer():
        # Código a medir
        time.sleep(2)  # Simula una operación que toma 2 segundos
