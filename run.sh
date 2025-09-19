#!/bin/bash

# MCP Diagram Generator - Runner Script
# Maneja el entorno virtual y ejecuta la aplicación

echo "🚀 MCP Diagram Generator Runner"
echo "==============================="

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "🐍 Creating virtual environment..."
    python3 -m venv venv
fi

# Activar entorno virtual
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Instalar dependencias
echo "📚 Installing dependencies..."
pip install -q -r requirements.txt

# Ejecutar aplicación con argumentos pasados
echo "🎨 Running MCP Diagram Generator..."
echo ""
python3 main.py "$@"

# Capturar código de salida
exit_code=$?

# Desactivar entorno virtual
deactivate

# Mostrar resultado
if [ $exit_code -eq 0 ]; then
    echo ""
    echo "✅ MCP Diagram Generator completed successfully!"
else
    echo ""
    echo "❌ MCP Diagram Generator failed with exit code: $exit_code"
fi

exit $exit_code
