#!/bin/bash

# Configuración
PROJECT_DIR="/home/lorgio/Documentos/codigo/python/inf220/proyectos/fraction_calculator_web"
PORT=8000

# Función para limpieza al terminar
cleanup() {
    echo "🛑 Deteniendo el servidor (PID $SERVER_PID)..."
    kill -SIGTERM "$SERVER_PID" 2>/dev/null  # Envía señal de terminación
    wait "$SERVER_PID" 2>/dev/null  # Espera a que el proceso termine
    echo "✅ Servidor detenido correctamente."
    exit 0
}

# Registrar la función cleanup para ejecutarse al recibir Ctrl+C o SIGTERM
trap cleanup SIGINT SIGTERM

# 1. Ir al directorio del proyecto
echo "📂 Accediendo al proyecto..."
cd "$PROJECT_DIR" || {
    echo "❌ Error: Directorio no encontrado." >&2
    exit 1
}

# 2. Activar entorno virtual
echo "🐍 Activando entorno virtual..."
source ./venv_fcalc_web/bin/activate || {
    echo "❌ Error: Entorno virtual no encontrado." >&2
    exit 1
}

# 3. Liberar puerto si está ocupado
echo "🔌 Liberando puerto $PORT..."
fuser -k $PORT/tcp 2>/dev/null || true

# 4. Iniciar servidor Django
echo "🚀 Iniciando servidor en http://127.0.0.1:$PORT/"
python manage.py runserver 127.0.0.1:$PORT &
SERVER_PID=$!  # Guarda el PID del proceso

# 5. Abrir navegador (opcional)
sleep 2
xdg-open "http://127.0.0.1:$PORT/" 2>/dev/null || echo "⚠️  No se pudo abrir el navegador." >&2

# 6. Esperar indefinidamente (hasta Ctrl+C)
echo "🛑 Presiona Ctrl+C para detener el servidor."
wait "$SERVER_PID"
