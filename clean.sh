#!/bin/bash
# Script de limpieza rápida para BMC Diagram Generator

set -e

echo "🧹 BMC DIAGRAM GENERATOR - LIMPIEZA RÁPIDA"
echo "=========================================="

# Función para mostrar ayuda
show_help() {
    echo "Uso: ./clean.sh [opción]"
    echo ""
    echo "Opciones:"
    echo "  all      - Limpiar todo (default)"
    echo "  png      - Solo diagramas PNG"
    echo "  drawio   - Solo diagramas DrawIO"
    echo "  docs     - Solo documentación"
    echo "  prompts  - Solo prompts MCP"
    echo "  config   - Solo configuración generada"
    echo "  status   - Mostrar estado actual"
    echo ""
    echo "Ejemplos:"
    echo "  ./clean.sh           # Limpiar todo"
    echo "  ./clean.sh png       # Solo PNG"
    echo "  ./clean.sh status    # Ver estado"
}

# Función para mostrar estado
show_status() {
    echo "📊 ESTADO ACTUAL:"
    
    if [ ! -d "outputs" ]; then
        echo "📁 No hay archivos generados"
        return
    fi
    
    echo "📂 Archivos por tipo:"
    echo "  🎨 PNG: $(find outputs -name "*.png" 2>/dev/null | wc -l)"
    echo "  📐 DrawIO: $(find outputs -name "*.drawio" 2>/dev/null | wc -l)"
    echo "  📄 MD: $(find outputs -name "*.md" 2>/dev/null | wc -l)"
    echo "  ⚙️ JSON: $(find outputs -name "*.json" 2>/dev/null | wc -l)"
    echo "  📁 Total: $(find outputs -type f 2>/dev/null | wc -l)"
    
    if [ -d "outputs" ]; then
        echo ""
        echo "📁 Estructura:"
        tree outputs 2>/dev/null || find outputs -type d | sort
    fi
}

# Función de limpieza
clean_section() {
    local section=$1
    
    case $section in
        "all"|"")
            echo "🧹 Limpiando todos los archivos generados..."
            if [ -d "outputs" ]; then
                rm -rf outputs
                echo "✅ Todos los archivos eliminados"
            else
                echo "ℹ️ No hay archivos para limpiar"
            fi
            ;;
        "png")
            echo "🧹 Limpiando diagramas PNG..."
            if [ -d "outputs/png" ]; then
                rm -rf outputs/png
                echo "✅ PNG eliminados"
            else
                echo "ℹ️ No hay PNG para limpiar"
            fi
            ;;
        "drawio")
            echo "🧹 Limpiando diagramas DrawIO..."
            if [ -d "outputs/drawio" ]; then
                rm -rf outputs/drawio
                echo "✅ DrawIO eliminados"
            else
                echo "ℹ️ No hay DrawIO para limpiar"
            fi
            ;;
        "docs")
            echo "🧹 Limpiando documentación..."
            if [ -d "outputs/documentation" ]; then
                rm -rf outputs/documentation
                echo "✅ Documentación eliminada"
            else
                echo "ℹ️ No hay documentación para limpiar"
            fi
            ;;
        "prompts")
            echo "🧹 Limpiando prompts MCP..."
            if [ -d "outputs/prompts" ]; then
                rm -rf outputs/prompts
                echo "✅ Prompts eliminados"
            else
                echo "ℹ️ No hay prompts para limpiar"
            fi
            ;;
        "config")
            echo "🧹 Limpiando configuración generada..."
            if [ -d "outputs/generated" ]; then
                rm -rf outputs/generated
                echo "✅ Configuración eliminada"
            else
                echo "ℹ️ No hay configuración para limpiar"
            fi
            ;;
        "status")
            show_status
            return
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

# Ejecutar limpieza
clean_section "$1"

echo ""
echo "🎯 Para regenerar archivos usa:"
echo "   python run.py --run complete    # Flujo completo"
echo "   python run.py --run png         # Solo PNG"
echo "   python run.py --status          # Ver estado"
