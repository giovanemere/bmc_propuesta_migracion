#!/bin/bash
# Script de generación rápida para BMC Diagram Generator

set -e

echo "🚀 BMC DIAGRAM GENERATOR - GENERACIÓN RÁPIDA"
echo "============================================"

# Función para mostrar ayuda
show_help() {
    echo "Uso: ./generate.sh [opción]"
    echo ""
    echo "Opciones:"
    echo "  complete - Flujo completo (default)"
    echo "  config   - Solo configuración"
    echo "  png      - Solo diagramas PNG"
    echo "  drawio   - Solo diagramas DrawIO"
    echo "  prompts  - Solo prompts MCP"
    echo "  docs     - Solo documentación"
    echo "  clean    - Limpiar y regenerar todo"
    echo ""
    echo "Ejemplos:"
    echo "  ./generate.sh           # Flujo completo"
    echo "  ./generate.sh png       # Solo PNG"
    echo "  ./generate.sh clean     # Limpiar y regenerar"
}

# Activar entorno virtual si existe
if [ -d "venv" ]; then
    echo "🔧 Activando entorno virtual..."
    source venv/bin/activate
fi

# Configurar PYTHONPATH
export PYTHONPATH="$(pwd)/src:$(pwd):$PYTHONPATH"

# Función de generación
generate_section() {
    local section=$1
    
    case $section in
        "complete"|"")
            echo "🚀 Ejecutando flujo completo..."
            python run.py --run complete
            ;;
        "config")
            echo "⚙️ Generando configuración..."
            python run.py --run config
            ;;
        "png")
            echo "🎨 Generando diagramas PNG..."
            python run.py --run png
            ;;
        "drawio")
            echo "📐 Generando diagramas DrawIO..."
            python run.py --run drawio
            ;;
        "prompts")
            echo "🎯 Generando prompts MCP..."
            python run.py --run prompts
            ;;
        "docs")
            echo "📚 Generando documentación..."
            python run.py --run docs
            ;;
        "clean")
            echo "🧹 Limpiando y regenerando todo..."
            python run.py --clean all --run complete
            ;;
        "help"|"-h"|"--help")
            show_help
            return
            ;;
        *)
            echo "❌ Opción desconocida: $section"
            echo ""
            show_help
            exit 1
            ;;
    esac
}

# Verificar que existe la especificación
if [ ! -f "config/bmc-input-specification.md" ]; then
    echo "❌ Error: No se encuentra config/bmc-input-specification.md"
    echo "   Este archivo es requerido para la generación"
    exit 1
fi

# Ejecutar generación
echo "📋 Usando especificación: config/bmc-input-specification.md"
echo ""

start_time=$(date +%s)
generate_section "$1"
end_time=$(date +%s)

duration=$((end_time - start_time))

echo ""
echo "✅ GENERACIÓN COMPLETADA"
echo "⏱️ Tiempo total: ${duration}s"
echo ""
echo "📊 Para ver el estado actual:"
echo "   python run.py --status"
echo "   ./clean.sh status"
