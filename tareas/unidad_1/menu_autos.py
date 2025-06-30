import json
import os


class Automovil:
    def __init__(
        self, marca, modelo, color, velocidad=0, combustible=100
    ):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad
        self.combustible = combustible

    def to_dict(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "color": self.color,
            "velocidad": self.velocidad,
            "combustible": self.combustible,
        }

    @staticmethod
    def from_dict(data):
        return Automovil(
            data["marca"],
            data["modelo"],
            data["color"],
            data.get("velocidad", 0),
            data.get("combustible", 100),
        )

    def mostrar(self):
        print(f"{self.marca} {self.modelo} ({self.color})")
        print(
            f"Velocidad: {self.velocidad} km/h - Combustible: {self.combustible} L\n"
        )


# ---------- FUNCIONES DE PERSISTENCIA ----------

ARCHIVO = "autos.json"


def cargar_autos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as archivo:
            datos = json.load(archivo)
            return [
                Automovil.from_dict(auto_dict) for auto_dict in datos
            ]
    return []


def guardar_autos(lista_autos):
    with open(ARCHIVO, "w") as archivo:
        json.dump([auto.to_dict() for auto in lista_autos], archivo)


# ---------- MENÚ INTERACTIVO ----------


def menu():
    autos = cargar_autos()

    while True:
        print("\n--- MENÚ DE AUTOMÓVILES ---")
        print("1. Agregar nuevo automóvil")
        print("2. Ver todos los automóviles")
        print("3. Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            color = input("Color: ")
            velocidad = int(input("Velocidad (km/h): "))
            combustible = int(input("Combustible (L): "))

            nuevo_auto = Automovil(
                marca, modelo, color, velocidad, combustible
            )
            autos.append(nuevo_auto)
            print("🚗 Automóvil agregado.")

        elif opcion == "2":
            if not autos:
                print("No hay automóviles cargados.")
            else:
                print("\n📋 Lista de automóviles:")
                for auto in autos:
                    auto.mostrar()

        elif opcion == "3":
            guardar_autos(autos)
            print("✅ Autos guardados. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# ---------- EJECUCIÓN ----------

if __name__ == "__main__":
    menu()
