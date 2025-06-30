#!/bin/bash
# Activar el entorno virtual (ajustá el nombre si es distinto)
source venv_to_do_list/bin/activate

# Exportar la variable FLASK para que sepa qué archivo ejecutar
export FLASK_APP=app.py

# Activar modo debug (opcional en desarrollo)
export FLASK_ENV=development

# Ejecutar la aplicación
flask run
