class Tarea:
    """
    Representa una tarea individual en una lista de tareas.

    Atributos:
        descripcion (str): La descripción de la tarea.
        completada (bool): Indica si la tarea está completada o no.
    """

    def __init__(self, descripcion, completada=False):
        """
        Inicializa una tarea con una descripción y su estado opcional.

        Args:
            descripcion (str): Texto que describe la tarea.
            completada (bool): Estado inicial (por defecto, False).
        """
        self.descripcion = descripcion
        self.completada = completada  # booleano

    def completar(self):
        """
        Alterna el estado de completada de la tarea.
        Si estaba pendiente, se marca como completada y viceversa.
        """
        self.completada = not self.completada

    def to_dict(self):
        """
        Convierte la tarea en un diccionario.

        Returns:
            dict: Contiene la descripción y el estado de completada.
        """
        return {
            'descripcion': self.descripcion,
            'completada': self.completada
        }

    @staticmethod
    def from_dict(data):
        """
        Crea una instancia de Tarea a partir de un diccionario.

        Args:
            data (dict): Diccionario con claves 
            'descripcion' y 'completada'.

        Returns:
            Tarea: Instancia creada a partir del diccionario.
        """
        return Tarea(
            data['descripcion'],
            data.get('completada', False)
        )
