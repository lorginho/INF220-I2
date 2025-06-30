# 📝 Gestor de Listas de Tareas

Aplicación web construida con **Flask** que permite 
gestionar múltiples listas de tareas con funcionalidades 
como agregar, eliminar, marcar como completada 
y persistir la información en archivos `.json`.

---

## 🚀 Funcionalidades

- ✅ Crear múltiples listas de tareas.
- ➕ Agregar tareas al **inicio o final** de la lista.
- 📌 Marcar tareas como completadas.
- 🗑 Eliminar tareas individuales o listas completas.
- 💾 Persistencia automática en archivos JSON.
- 🔁 Interfaz amigable desarrollada con HTML (Jinja) + CSS.

---

## ⚙️ Requisitos del Sistema

- Python 3.7 o superior
- Flask

### Instalación

```bash
pip install flask


Ejecución
bash
Copiar
Editar
python app.py
Luego abre tu navegador en http://127.0.0.1:5000.

📂 Estructura del Proyecto
csharp
Copiar
Editar
.
├── app.py
├── controllers/
│   └── task_controller.py
├── models/
│   ├── tarea.py
│   └── lista.py
├── templates/
│   ├── base.html
│   ├── lista.html
│   └── selector.html
├── static/
│   └── style.css
└── data/
    └── *.json  # Archivos de listas guardadas
🧠 Modelado de Datos
Clase Tarea
descripcion: texto

completada: booleano

Métodos:

completar()

to_dict() / from_dict()

Clase Nodo
tarea: una instancia de Tarea

siguiente: puntero al siguiente nodo

anterior: puntero al nodo anterior

Clase ListaDobleEnlazada
Lista doblemente enlazada con operaciones:

agregar_tarea(tarea, al_inicio=False)

buscar(descripcion)

eliminar(descripcion)

completar_tarea(descripcion)

obtener_tareas()

Clase TaskController
Maneja múltiples listas y persistencia.

Operaciones:

cargar_lista()

agregar()

eliminar()

completar()

eliminar_lista()

✅ Requisitos del Proyecto (Cumplidos)
Requisito	Estado
Agregar tarea al inicio o final	✅
Marcar una tarea como completada	✅
Eliminar una tarea	✅
Mostrar todas las tareas con su estado	✅
Nodo con descripción, estado y puntero al siguiente	✅
Persistencia con archivos locales	✅

