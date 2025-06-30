import os
import json
from models.lista import ListaDobleEnlazada
from models.tarea import Tarea


class TaskController:
    """
    Controlador principal que gestiona múltiples listas de tareas.
    Permite cargar, guardar, modificar y eliminar tareas y listas.
    """

    def __init__(self, data_dir='data'):
        """
        Inicializa el controlador de tareas.

        Args:
            data_dir (str): Ruta al directorio 
            donde se guardan los archivos JSON.
        """
        self.data_dir = data_dir
        self.listas = {}
        self.lista_activa = None
        os.makedirs(data_dir, exist_ok=True)

    def _archivo_lista(self, nombre_lista):
        """
        Devuelve la ruta al archivo JSON de una lista.

        Args:
            nombre_lista (str): Nombre de la lista.

        Returns:
            str: Ruta del archivo correspondiente.
        """
        return os.path.join(self.data_dir, f"{nombre_lista}.json")

    def obtener_nombres_listas(self):
        """
        Lista todos los nombres de listas almacenadas.

        Returns:
            list[str]: Lista de nombres sin extensión `.json`.
        """
        archivos = os.listdir(self.data_dir)
        return [archivo.replace('.json', '')
                for archivo in archivos if archivo.endswith('.json')]

    def cargar_lista(self, nombre_lista):
        """
        Carga una lista desde archivo, si no está en memoria.

        Args:
            nombre_lista (str): Nombre de la lista a cargar.
        """
        if nombre_lista in self.listas:
            return

        lista = ListaDobleEnlazada()
        archivo = self._archivo_lista(nombre_lista)

        if os.path.exists(archivo):
            with open(archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                for tarea_data in datos:
                    tarea = Tarea.from_dict(tarea_data)
                    lista.agregar_tarea(tarea)

        self.listas[nombre_lista] = lista

    def _guardar_lista(self, nombre_lista):
        """
        Guarda una lista en un archivo JSON.

        Args:
            nombre_lista (str): Nombre de la lista a guardar.
        """
        if nombre_lista not in self.listas:
            return
        lista = self.listas[nombre_lista]
        tareas_dict = [t.to_dict() for t in lista.obtener_tareas()]
        archivo = self._archivo_lista(nombre_lista)
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(tareas_dict, f, ensure_ascii=False, indent=4)

    def obtener_tareas(self, nombre_lista):
        """
        Devuelve la lista de tareas de una lista específica.

        Args:
            nombre_lista (str): Nombre de la lista.

        Returns:
            list[Tarea]: Tareas contenidas en la lista.
        """
        self.cargar_lista(nombre_lista)
        return self.listas[nombre_lista].obtener_tareas()

    def agregar(self, nombre_lista, descripcion, al_inicio=False):
        """
        Agrega una nueva tarea a una lista, al inicio o final.

        Args:
            nombre_lista (str): Lista donde agregar.
            descripcion (str): Descripción de la tarea.
            al_inicio (bool): Si se debe insertar al principio.

        Returns:
            bool: True si se agregó, False si ya existía.
        """
        self.cargar_lista(nombre_lista)
        lista = self.listas[nombre_lista]
        if lista.buscar(descripcion):
            return False
        tarea = Tarea(descripcion)
        lista.agregar_tarea(tarea, al_inicio=al_inicio)
        self._guardar_lista(nombre_lista)
        return True

    def eliminar(self, nombre_lista, descripcion):
        """
        Elimina una tarea por su descripción.

        Args:
            nombre_lista (str): Lista objetivo.
            descripcion (str): Descripción de la tarea.

        Returns:
            bool: True si se eliminó, False si no se encontró.
        """
        self.cargar_lista(nombre_lista)
        lista = self.listas[nombre_lista]
        if lista.eliminar(descripcion):
            self._guardar_lista(nombre_lista)
            return True
        return False

    def completar(self, nombre_lista, descripcion):
        """
        Marca una tarea como completada o pendiente (toggle).

        Args:
            nombre_lista (str): Lista que contiene la tarea.
            descripcion (str): Descripción de la tarea.

        Returns:
            bool: True si se completó, False si no se encontró.
        """
        self.cargar_lista(nombre_lista)
        lista = self.listas[nombre_lista]
        if lista.completar_tarea(descripcion):
            self._guardar_lista(nombre_lista)
            return True
        return False

    def eliminar_lista(self, nombre_lista):
        """
        Elimina completamente una lista (memoria y archivo).

        Args:
            nombre_lista (str): Lista a eliminar.

        Returns:
            bool: True si se eliminó, False si no existía.
        """
        if nombre_lista in self.listas:
            del self.listas[nombre_lista]
        archivo = self._archivo_lista(nombre_lista)
        if os.path.exists(archivo):
            os.remove(archivo)
            return True
        return False

    def obtener_nombre_lista_activa(self):
        """
        Devuelve el nombre de la lista actualmente activa.

        Returns:
            str: Nombre de la lista activa.
        """
        return self.lista_activa

    def set_lista_activa(self, nombre):
        """
        Establece la lista activa.

        Args:
            nombre (str): Nombre de la lista.
        """
        if nombre in self.listas:
            self.lista_activa = nombre

    def listar_listas(self):
        """
        Devuelve los nombres de todas las listas almacenadas.

        Returns:
            list[str]: Nombres de listas.
        """
        return self.obtener_nombres_listas()
