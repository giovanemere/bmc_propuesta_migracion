#!/bin/bash

# Script para generar diagramas PNG desde archivos Draw.io
# Requiere: draw.io desktop app o drawio CLI

echo "🎨 Generando diagramas PNG para arquitectura BMC..."

# Crear directorio para PNGs
mkdir -p drawio/png

# Función para convertir drawio a PNG
convert_to_png() {
    local input_file=$1
    local output_file=$2
    local diagram_name=$3
    
    echo "📊 Convirtiendo: $diagram_name"
    
    # Usando drawio CLI (si está instalado)
    if command -v drawio &> /dev/null; then
        drawio -x -f png -o "$output_file" "$input_file"
    # Usando draw.io desktop (si está instalado)
    elif command -v draw.io &> /dev/null; then
        draw.io -x -f png -o "$output_file" "$input_file"
    # Usando Docker con draw.io
    elif command -v docker &> /dev/null; then
        docker run --rm -v "$(pwd)":/data minlag/drawio-cli -f png -o "/data/$output_file" "/data/$input_file"
    else
        echo "❌ Error: No se encontró draw.io CLI, desktop app o Docker"
        echo "📋 Instrucciones de instalación:"
        echo "   1. Instalar draw.io desktop: https://github.com/jgraph/drawio-desktop/releases"
        echo "   2. O usar Docker: docker pull minlag/drawio-cli"
        echo "   3. O instalar drawio CLI: npm install -g @mermaid-js/mermaid-cli"
        return 1
    fi
}

# Convertir diagramas
echo "🔄 Iniciando conversión de diagramas..."

# 1. Diagrama de Contexto
convert_to_png "drawio/bmc-context-diagram.drawio" "drawio/png/bmc-context-diagram.png" "Diagrama de Contexto"

# 2. Diagrama de Contenedores
convert_to_png "drawio/bmc-container-diagram.drawio" "drawio/png/bmc-container-diagram.png" "Diagrama de Contenedores"

# 3. Infraestructura AWS
convert_to_png "drawio/bmc-aws-infrastructure.drawio" "drawio/png/bmc-aws-infrastructure.png" "Infraestructura AWS"

echo "✅ Conversión completada!"
echo "📁 Archivos PNG generados en: drawio/png/"

# Listar archivos generados
if [ -d "drawio/png" ]; then
    echo "📋 Archivos generados:"
    ls -la drawio/png/*.png 2>/dev/null || echo "⚠️  No se generaron archivos PNG"
fi

echo ""
echo "🎯 Instrucciones para usar los diagramas:"
echo "   • Los archivos .drawio se pueden abrir en draw.io (app.diagrams.net)"
echo "   • Los archivos PNG están listos para presentaciones"
echo "   • Para editar: abrir .drawio files en draw.io desktop o web"
echo "   • Para exportar manualmente: File > Export as > PNG en draw.io"
