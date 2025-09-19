#!/bin/bash

# BMC Final Version Generator - PNG + Draw.io
# Genera la versión más completa y profesional

echo "🚀 BMC Final Version Generator"
echo "=============================="
echo "Generando versión completa: PNG + Draw.io"
echo ""

# Verificar directorio
echo "📁 Directorio: $(pwd)"

# Activar entorno virtual
if [ -d "venv" ]; then
    echo "🐍 Activando entorno virtual..."
    source venv/bin/activate
else
    echo "❌ No se encontró entorno virtual. Creando..."
    python3 -m venv venv
    source venv/bin/activate
    pip install diagrams graphviz
fi

# Limpiar archivos anteriores
echo "🧹 Limpiando archivos anteriores..."
rm -f bmc_*.png bmc_*.drawio

# Generar versión completa
echo "🎨 Generando versión final completa..."
python3 generate_complete.py

# Verificar generación
echo ""
echo "📊 Verificando archivos generados..."

PNG_COUNT=$(ls bmc_*.png 2>/dev/null | wc -l)
DRAWIO_COUNT=$(ls bmc_*.drawio 2>/dev/null | wc -l)

echo "PNG files: $PNG_COUNT"
echo "Draw.io files: $DRAWIO_COUNT"

if [ $PNG_COUNT -gt 0 ] && [ $DRAWIO_COUNT -gt 0 ]; then
    echo ""
    echo "✅ Generación exitosa!"
    echo ""
    echo "📁 Archivos PNG generados:"
    ls -la bmc_*.png | awk '{print "  - " $9 " (" $5 " bytes)"}'
    echo ""
    echo "📁 Archivos Draw.io generados:"
    ls -la bmc_*.drawio | awk '{print "  - " $9 " (" $5 " bytes)"}'
    echo ""
    echo "💡 Uso recomendado:"
    echo "  📊 PNG: Presentaciones ejecutivas, documentos"
    echo "  🎨 Draw.io: Edición en https://app.diagrams.net"
    echo ""
    echo "🎯 Versión final lista para producción!"
else
    echo "❌ Error: No se generaron todos los archivos"
    exit 1
fi

# Desactivar entorno virtual
deactivate

echo ""
echo "🎉 BMC Final Version Generation Complete!"
echo "📍 Location: $(pwd)"
