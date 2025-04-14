#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nombre del archivo: auto_static_atd.py
Descripción: Este módulo contiene la definición de la clase Automovil que simula 
             un vehículo con atributos y comportamientos comunes como arrancar, acelerar,
             frenar, llenar el tanque y más.
Autor: Lorgio Añez J.
Fecha de Creación: 2025-04-07
Versión: 1.0.0
Materia: INF220-I2
Asignatura: Estructura de Datos I
Docente:  Ing. J.C. Peinado
"""


class Automovil:
    """
    Clase Automovil que representa un automóvil con atributos y métodos para
    simular su funcionamiento.
    Atributos:
        - marca: Marca del automóvil.
        - modelo: Modelo del automóvil.
        - year: Año de fabricación.
        - color: Color del automóvil.
        - combustible_maximo: Capacidad máxima del tanque de combustible.
        - combustible_actual: Cantidad actual de combustible en el tanque.
        - kilometraje: Kilometraje recorrido por el automóvil.
        - aceite_cambio: Contador para el cambio de aceite.
        - arrancado: Estado del automóvil (arrancado o detenido).
    Métodos:
        - get_marca: Devuelve la marca del automóvil.
        - set_marca: Establece la marca del automóvil.
        - get_modelo: Devuelve el modelo del automóvil.
        - set_modelo: Establece el modelo del automóvil.
        - get_year: Devuelve el año de fabricación del automóvil.
        - set_year: Establece el año de fabricación del automóvil.
        - get_color: Devuelve el color del automóvil.
        - set_color: Establece el color del automóvil.
        - mostrar_info: Muestra la información del automóvil.
        - arrancar: Arranca el automóvil.
        - detener: Detiene el automóvil.
        - acelerar: Acelera el automóvil.
        - frenar: Frena el automóvil.
        - verificar_combustible: Verifica el nivel de combustible.
        - llenar_tanque: Llena el tanque de combustible.
        - mantenimiento: Realiza un mantenimiento al automóvil (cambio de aceite).
        - cambiar_aceite: Cambia el aceite del automóvil.
    """

    def __init__(self, marca, modelo, year, color, combustible_maximo):
        """Método Constructor"""
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.color = color
        self.combustible_maximo = combustible_maximo
        self.combustible_actual = (
            combustible_maximo  # Inicializamos con el tanque lleno
        )
        self.kilometraje = 0
        self.aceite_cambio = 0
        self.arrancado = False

    # Getter y Setter para la marca
    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    # Getter y Setter para el modelo
    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    # Getter y Setter para el year
    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    # Getter y Setter para el color
    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    # Método para mostrar la información del automóvil
    def mostrar_info(self):
        return f"{self.marca} {self.modelo} ({self.year}), Color: {self.color}, Kilometraje: {self.kilometraje} km, Combustible: {self.combustible_actual}/{self.combustible_maximo} litros"

    # Método para arrancar el automóvil
    def arrancar(self):
        if self.combustible_actual > 0:
            self.arrancado = True
            print(f"{self.marca} {self.modelo} ha arrancado.")
        else:
            print(
                f"No hay suficiente combustible para arrancar {self.marca} {self.modelo}."
            )

    # Método para detener el automóvil
    def detener(self):
        self.arrancado = False
        print(f"{self.marca} {self.modelo} se ha detenido.")

    # Método para acelerar el automóvil
    def acelerar(self):
        if self.arrancado:
            if self.combustible_actual > 0:
                self.combustible_actual -= (
                    0.1  # Reducimos el combustible por cada aceleración
                )
                self.kilometraje += 1  # Aumentamos el kilometraje
                print(
                    f"{self.marca} {self.modelo} está acelerando. Combustible restante: {self.combustible_actual} litros."
                )
            else:
                print("No hay suficiente combustible para acelerar.")
        else:
            print(
                f"{self.marca} {self.modelo} no está arrancado. No se puede acelerar."
            )

    # Método para frenar el automóvil
    def frenar(self):
        if self.arrancado:
            print(f"{self.marca} {self.modelo} está frenando.")
        else:
            print(f"{self.marca} {self.modelo} no está arrancado. No se puede frenar.")

    # Método para verificar el nivel de combustible
    def verificar_combustible(self):
        print(
            f"El nivel de combustible en {self.marca} {self.modelo} es {self.combustible_actual} litros."
        )

    # Método para llenar el tanque
    def llenar_tanque(self):
        self.combustible_actual = self.combustible_maximo
        print(
            f"El tanque de {self.marca} {self.modelo} ha sido llenado a {self.combustible_maximo} litros."
        )

    # Método para realizar un mantenimiento (cambio de aceite)
    def mantenimiento(self):
        print(f"Se ha realizado un mantenimiento en {self.marca} {self.modelo}.")
        self.aceite_cambio = 0  # Resetear el contador de cambios de aceite
        self.kilometraje = 0  # Reseteamos el kilometraje después del mantenimiento

    # Método para cambiar el aceite
    def cambiar_aceite(self):
        print(f"Se ha cambiado el aceite de {self.marca} {self.modelo}.")
        self.aceite_cambio = 0

    # Método para simular el uso del automóvil, incrementando el contador de aceite
    def usar(self, distancia):
        if self.arrancado:
            self.kilometraje += distancia
            self.aceite_cambio += distancia
            if self.aceite_cambio >= 5000:  # Cada 5000 km cambiamos el aceite
                print(f"Es hora de cambiar el aceite de {self.marca} {self.modelo}.")
                self.cambiar_aceite()
            print(f"{self.marca} {self.modelo} ha recorrido {distancia} km.")
        else:
            print(f"{self.marca} {self.modelo} no está arrancado. No se puede usar.")


# Ejemplo de uso
auto1 = Automovil("Suzuki", "Swift", 2015, "Rojo", 42)

# Mostrar la información inicial
print(auto1.mostrar_info())

# Arrancar, acelerar y frenar
auto1.arrancar()
auto1.acelerar()
auto1.acelerar()
auto1.frenar()

# Verificar el nivel de combustible y llenar el tanque
auto1.verificar_combustible()
auto1.llenar_tanque()

# Hacer uso del automóvil
auto1.usar(150)
auto1.mantenimiento()

# Cambiar el aceite
auto1.cambiar_aceite()

# Mostrar la información final
print(auto1.mostrar_info())
