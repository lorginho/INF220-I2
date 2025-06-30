from models.tarea import Tarea


class Nodo:
    """
    Representa un nodo de una lista doblemente enlazada.

    Atributos:
        tarea (Tarea): La tarea contenida en este nodo.
        anterior (Nodo): Referencia al nodo anterior.
        siguiente (Nodo): Referencia al nodo siguiente.
    """

    def __init__(self, tarea):
        self.tarea = tarea
        self.anterior = None
        self.siguiente = None


class ListaDobleEnlazada:
    """
    Implementa una lista doblemente enlazada para almacenar tareas.

    Métodos:
        agregar_tarea(tarea, al_inicio): Inserta una tarea al inicio 
        o al final.
        buscar(descripcion): Retorna el nodo con la descripción dada.
        eliminar(descripcion): Elimina una tarea de la lista.
        completar_tarea(descripcion): Marca una tarea como completada.
        obtener_tareas(): Devuelve todas las tareas como lista.
    """

    def __init__(self):
        self.primero = None

    def agregar_tarea(self, tarea, al_inicio=False):
        """
        Agrega una nueva tarea a la lista, ya sea al inicio o al final.

        Args:
            tarea (Tarea): La tarea a agregar.
            al_inicio (bool): Si es True, se inserta al inicio.
        """
        nuevo = Nodo(tarea)
        if not self.primero:
            self.primero = nuevo
            return

        if al_inicio:
            # Insertar al inicio
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
        else:
            # Insertar al final
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual

    def buscar(self, descripcion):
        """
        Busca un nodo por su descripción.

        Args:
            descripcion (str): Descripción de la tarea a buscar.

        Returns:
            Nodo o None: El nodo que contiene la tarea, 
            o None si no se encuentra.
        """
        actual = self.primero
        while actual:
            if actual.tarea.descripcion == descripcion:
                return actual
            actual = actual.siguiente
        return None

    def eliminar(self, descripcion):
        """
        Elimina una tarea de la lista por su descripción.

        Args:
            descripcion (str): La descripción de la tarea a eliminar.

        Returns:
            bool: True si se eliminó, False si no se encontró.
        """
        nodo = self.buscar(descripcion)
        if not nodo:
            return False

        if nodo.anterior:
            nodo.anterior.siguiente = nodo.siguiente
        else:
            self.primero = nodo.siguiente

        if nodo.siguiente:
            nodo.siguiente.anterior = nodo.anterior

        return True

    def completar_tarea(self, descripcion):
        """
        Marca una tarea como completada.

        Args:
            descripcion (str): La descripción de la tarea a completar.

        Returns:
            bool: True si se marcó como completada, 
            False si no se encontró.
        """
        nodo = self.buscar(descripcion)
        if nodo:
            nodo.tarea.completar()
            return True
        return False

    def obtener_tareas(self):
        """
        Devuelve todas las tareas de la lista en forma de lista Python.

        Returns:
            list[Tarea]: Lista de objetos Tarea en orden 
            de la lista enlazada.
        """
        tareas = []
        actual = self.primero
        while actual:
            tareas.append(actual.tarea)
            actual = actual.siguiente
        return tareas
