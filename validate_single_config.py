#!/usr/bin/env python3
"""
Validador de configuración única
Asegura que solo existe un archivo de configuración activo
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from core.config_manager import ConfigManager

def validate_single_config():
    """Valida configuración única"""
    
    print("🔍 Validando configuración única...")
    print("=" * 40)
    
    try:
        manager = ConfigManager()
        
        # Cargar y validar configuración
        config = manager.load_config()
        summary = manager.get_config_summary()
        
        print(f"📋 Resumen de Configuración:")
        print(f"  - Versión: {summary['version']}")
        print(f"  - Proyecto: {summary['project_name']}")
        print(f"  - Fecha consolidación: {summary['consolidated_date']}")
        print(f"  - Archivos fuente: {summary['source_files_count']}")
        print(f"  - Configuración única: {'✅' if summary['single_config'] else '❌'}")
        
        if summary['single_config']:
            print(f"\n🎉 Validación exitosa - Solo un archivo de configuración activo")
            
            # Mostrar información del proyecto
            project_info = manager.get_project_info()
            print(f"\n📊 Información del Proyecto:")
            print(f"  - Nombre: {project_info.get('name')}")
            print(f"  - Tipo: {project_info.get('type')}")
            print(f"  - Entidad: {project_info.get('entity')}")
            print(f"  - Función: {project_info.get('main_function')}")
            
            return True
        else:
            print(f"\n❌ Error: Múltiples archivos de configuración encontrados")
            print(f"Ejecuta: python3 consolidate_config.py")
            return False
            
    except Exception as e:
        print(f"❌ Error validando configuración: {e}")
        return False

if __name__ == "__main__":
    success = validate_single_config()
    sys.exit(0 if success else 1)
