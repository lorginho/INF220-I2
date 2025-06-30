from flask import Flask, render_template, request, redirect, url_for
from controllers.task_controller import TaskController

app = Flask(__name__)
controller = TaskController()


@app.route('/')
def index():
    """
    Ruta principal de la aplicación.
    Muestra el selector de listas si no hay ninguna seleccionada,
    o la lista de tareas si se ha pasado como parámetro.
    """
    nombre_lista = request.args.get(
        'lista')  # Solo del query string, sin lista activa por defecto
    if not nombre_lista:
        listas = controller.listar_listas()
        return render_template('selector.html',
                               listas_existentes=listas,
                               lista_actual=None)

    tareas = controller.obtener_tareas(nombre_lista)
    listas = controller.listar_listas()
    return render_template('lista.html', tareas=tareas,
                           listas_existentes=listas,
                           lista_actual=nombre_lista)


@app.route('/seleccionar_lista', methods=['POST'])
def seleccionar_lista():
    """
    Selecciona una lista existente y redirige a la página principal.
    """
    nombre = request.form.get('nombre_lista')
    controller.set_lista_activa(nombre)
    return redirect(url_for('index', lista=nombre))


@app.route('/crear_lista', methods=['POST'])
def crear_lista():
    """
    Crea una nueva lista con el nombre ingresado y redirige a su vista.
    """
    nueva = request.form.get('nueva_lista')
    if nueva:
        controller.cargar_lista(nueva)
        return redirect(url_for('ver_lista', nombre_lista=nueva))
    return redirect(url_for('index'))


@app.route('/lista/<nombre_lista>')
def ver_lista(nombre_lista):
    """
    Muestra las tareas asociadas a una lista específica.
    """
    controller.cargar_lista(nombre_lista)
    tareas = controller.obtener_tareas(nombre_lista)
    listas = controller.obtener_nombres_listas()
    return render_template('lista.html', tareas=tareas,
                           lista_actual=nombre_lista,
                           listas_existentes=listas)


@app.route('/lista/<nombre_lista>/agregar', methods=['POST'])
def agregar_tarea(nombre_lista):
    """
    Agrega una nueva tarea a la lista, ya sea al inicio 
    o al final según el checkbox.
    """
    descripcion = request.form['descripcion']
    al_inicio = request.form.get('inicio') == '1'  # True si checkbox marcado
    controller.agregar(nombre_lista, descripcion, al_inicio=al_inicio)
    return redirect(url_for('ver_lista', nombre_lista=nombre_lista))


@app.route('/lista/<nombre_lista>/completar', methods=['POST'])
def completar_tarea(nombre_lista):
    """
    Marca como completada una tarea en la lista dada.
    """
    descripcion = request.form.get('descripcion')
    controller.completar(nombre_lista, descripcion)
    return redirect(url_for('ver_lista', nombre_lista=nombre_lista))


@app.route('/lista/<nombre_lista>/eliminar', methods=['POST'])
def eliminar_tarea(nombre_lista):
    """
    Elimina una tarea de la lista especificada.
    """
    descripcion = request.form.get('descripcion')
    controller.eliminar(nombre_lista, descripcion)
    return redirect(url_for('ver_lista', nombre_lista=nombre_lista))


@app.route('/eliminar_lista/<nombre_lista>', methods=['POST'])
def eliminar_lista(nombre_lista):
    """
    Elimina completamente una lista (archivo JSON y memoria).
    """
    controller.eliminar_lista(nombre_lista)
    return redirect(url_for('index'))


def listar_listas(self):
    """
    (No utilizada directamente como endpoint)
    Devuelve los nombres de todas las listas guardadas.
    """
    return self.obtener_nombres_listas()


if __name__ == '__main__':
    app.run(debug=True)
