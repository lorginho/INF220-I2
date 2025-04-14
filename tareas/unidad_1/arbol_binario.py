class Nodo:
    """
    Clase que representa un nodo dentro del árbol binario.

    Attributes:
        valor: El valor almacenado en el nodo.
        izquierdo: Referencia al hijo izquierdo del nodo.
        derecho: Referencia al hijo derecho del nodo.
    """

    def __init__(self, valor):
        """
        Inicializa un nuevo nodo con el valor especificado.

        Args:
            valor: El valor a almacenar en el nodo.
        """
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    """
    Clase que implementa un árbol binario.

    Attributes:
        raiz: El nodo raíz del árbol.
    """

    def __init__(self):
        """Inicializa un árbol binario vacío."""
        self.raiz = None

    def get_raiz(self):
        """
        Obtiene el nodo raíz del árbol.

        Returns:
            El nodo raíz del árbol o None si el árbol está vacío.
        """
        return self.raiz

    def set_raiz(self, valor):
        """
        Establece el valor del nodo raíz del árbol.

        Args:
            valor: El valor a establecer como raíz.
        """
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self.raiz.valor = valor

    def insertar(self, valor):
        """
        Inserta un nuevo valor en el árbol.

        Args:
            valor: El valor a insertar en el árbol.
        """
        if self.raiz is None:
            # Si el árbol está vacío, el nuevo valor se convierte en la raíz
            self.raiz = Nodo(valor)
        else:
            # Si el árbol no está vacío, usamos un método
            # auxiliar para la inserción
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        """
        Método auxiliar para insertar un valor de forma recursiva.

        Args:
            nodo_actual: El nodo actual en el recorrido recursivo.
            valor: El valor a insertar.
        """
        # Si el valor es menor que el valor del nodo actual
        if valor < nodo_actual.valor:
            # Si no tiene hijo izquierdo, insertamos ahí
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                # Si ya tiene hijo izquierdo, continuamos por ese subárbol
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        # Si el valor es mayor o igual que el valor del nodo actual
        else:
            # Si no tiene hijo derecho, insertamos ahí
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                # Si ya tiene hijo derecho, continuamos por ese subárbol
                self._insertar_recursivo(nodo_actual.derecho, valor)

    def buscar(self, valor):
        """
        Busca un valor en el árbol.

        Args:
            valor: El valor a buscar.

        Returns:
            True si el valor se encuentra en el árbol, False en caso contrario.
        """
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo_actual, valor):
        """
        Método auxiliar para buscar un valor de forma recursiva.

        Args:
            nodo_actual: El nodo actual en el recorrido recursivo.
            valor: El valor a buscar.

        Returns:
            True si el valor se encuentra en el subárbol,
            False en caso contrario.
        """
        # Si el nodo actual es None, el valor no está en esta rama
        if nodo_actual is None:
            return False

        # Si el valor coincide con el valor del nodo actual
        if nodo_actual.valor == valor:
            return True

        # Si el valor es menor, buscamos en el subárbol izquierdo
        if valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierdo, valor)

        # Si el valor es mayor, buscamos en el subárbol derecho
        return self._buscar_recursivo(nodo_actual.derecho, valor)

    def es_hoja(self, nodo):
        """
        Verifica si un nodo es una hoja (no tiene hijos).

        Args:
            nodo: El nodo a verificar.

        Returns:
            True si el nodo es una hoja, False en caso contrario.
        """
        if nodo is None:
            return False

        return nodo.izquierdo is None and nodo.derecho is None

    def altura(self):
        """
        Calcula la altura del árbol.

        Returns:
            La altura del árbol. Si el árbol está vacío, retorna 0.
        """
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo):
        """
        Método auxiliar para calcular la altura de forma recursiva.

        Args:
            nodo: El nodo actual en el recorrido recursivo.

        Returns:
            La altura del subárbol con raíz en nodo.
        """
        # Si el nodo es None, la altura es 0
        if nodo is None:
            return 0

        # Calculamos la altura de los subárboles izquierdo y derecho
        altura_izquierda = self._altura_recursiva(nodo.izquierdo)
        altura_derecha = self._altura_recursiva(nodo.derecho)

        # La altura es el máximo de las alturas de los subárboles más 1
        return max(altura_izquierda, altura_derecha) + 1

    def cantidad(self):
        """
        Calcula la cantidad de nodos en el árbol.

        Returns:
            El número de nodos en el árbol.
        """
        return self._cantidad_recursiva(self.raiz)

    def _cantidad_recursiva(self, nodo):
        """
        Método auxiliar para calcular la cantidad de nodos de forma recursiva.

        Args:
            nodo: El nodo actual en el recorrido recursivo.

        Returns:
            El número de nodos en el subárbol con raíz en nodo.
        """
        # Si el nodo es None, la cantidad es 0
        if nodo is None:
            return 0

        # La cantidad es 1 (el nodo actual) más la cantidad en los subárboles
        return (
            1
            + self._cantidad_recursiva(nodo.izquierdo)
            + self._cantidad_recursiva(nodo.derecho)
        )

    def amplitud(self):
        """
        Realiza un recorrido por amplitud (BFS) del árbol.

        Returns:
            Una lista con los valores de los nodos en orden de amplitud.
        """
        if self.raiz is None:
            return []

        # Utilizamos una cola para el recorrido BFS
        resultado = []
        cola = [self.raiz]

        while cola:
            # Sacamos el primer nodo de la cola
            nodo_actual = cola.pop(0)
            resultado.append(nodo_actual.valor)

            # Agregamos los hijos a la cola (primero izquierdo, luego derecho)
            if nodo_actual.izquierdo is not None:
                cola.append(nodo_actual.izquierdo)

            if nodo_actual.derecho is not None:
                cola.append(nodo_actual.derecho)

        return resultado


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un árbol binario
    arbol = ArbolBinario()

    # Insertar valores

    #valores = [50, 30, 70, 20, 40, 60, 80]
    valores = [50, 30, 70, 120, 40, 60, 20, 28, 41, 37, 11]
    
    for valor in valores:
        arbol.insertar(valor)

    # Imprimir información del árbol
    print(f"Raíz: {arbol.get_raiz().valor}")
    print(f"Altura: {arbol.altura()}")
    print(f"Cantidad de nodos: {arbol.cantidad()}")
    print(f"Recorrido por amplitud: {arbol.amplitud()}")

    # Buscar valores
    print(f"¿El valor 40 está en el árbol? {arbol.buscar(40)}")
    print(f"¿El valor 90 está en el árbol? {arbol.buscar(90)}")

    # Verificar si un nodo es hoja
    print(f"¿El nodo raíz es hoja? {arbol.es_hoja(arbol.get_raiz())}")
    print(f"¿El nodo 20 es hoja? {arbol.es_hoja(arbol.get_raiz().izquierdo.izquierdo)}")
