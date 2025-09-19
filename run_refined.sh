#!/bin/bash

# BMC Refined Diagram Generator
# Ejecuta casos refinados con entorno virtual

echo "🎨 BMC Refined Diagram Generator"
echo "================================"

# Activar entorno virtual
if [ ! -d "venv" ]; then
    echo "🐍 Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

# Instalar dependencias
echo "📚 Installing dependencies..."
pip install -q -r requirements.txt

# Ejecutar caso refinado
echo "🚀 Running refined BMC case..."
python3 cases/refined_bmc_case.py

exit_code=$?
deactivate

if [ $exit_code -eq 0 ]; then
    echo ""
    echo "✅ Refined diagrams generated successfully!"
    echo "📁 Check output/png/ for professional diagrams"
else
    echo ""
    echo "❌ Refined diagram generation failed"
fi

exit $exit_code
