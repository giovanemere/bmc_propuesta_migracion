#!/usr/bin/env python3
"""
Script de reestructuración y limpieza de la solución MCP
Organiza módulos y elimina archivos no utilizados
"""

import os
import shutil
from pathlib import Path

def analyze_current_structure():
    """Analiza la estructura actual"""
    
    print("🔍 Analizando estructura actual...")
    
    # Archivos core activos
    core_active = [
        "refined_diagram_generator.py",
        "unified_mcp_generator.py", 
        "mcp_prompt_generator.py",
        "implementation_doc_generator.py",
        "config_manager.py",
        "bmc_input_parser.py"
    ]
    
    # Archivos core obsoletos
    core_obsolete = [
        "simple_drawio_generator.py",
        "fixed_drawio_generator.py",
        "enhanced_drawio_generator.py",
        "professional_drawio_generator.py",
        "complete_drawio_generator.py",
        "unified_drawio_generator.py",
        "diagram_generator.py",
        "drawio_validator.py",
        "output_manager.py",
        "mcp_engine.py",
        "mcp_parser.py"
    ]
    
    # Scripts raíz obsoletos
    root_obsolete = [
        "consolidate_config.py",
        "fix_drawio_files.py",
        "fix_duplicate_outputs.py",
        "minimal_drawio_fix.py",
        "organize_cp_outputs.py",
        "use_only_mcp.py",
        "validate_drawio.py",
        "validate_single_config.py",
        "show_mcp_prompts.py",
        "show_mcp_structure.py"
    ]
    
    return {
        "core_active": core_active,
        "core_obsolete": core_obsolete,
        "root_obsolete": root_obsolete
    }

def create_new_structure():
    """Crea nueva estructura organizada"""
    
    print("📁 Creando nueva estructura...")
    
    # Crear directorios organizados
    new_dirs = [
        "src/core",
        "src/generators", 
        "src/parsers",
        "src/cases",
        "tools/scripts",
        "tools/utilities",
        "config",
        "docs/api",
        "tests"
    ]
    
    for dir_path in new_dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"  ✓ {dir_path}/")
    
    return new_dirs

def reorganize_files():
    """Reorganiza archivos en nueva estructura"""
    
    print("🔄 Reorganizando archivos...")
    
    # Mapeo de archivos a nueva ubicación
    file_mapping = {
        # Core activos
        "core/config_manager.py": "src/core/config_manager.py",
        "core/bmc_input_parser.py": "src/parsers/bmc_input_parser.py",
        
        # Generadores
        "core/refined_diagram_generator.py": "src/generators/diagram_generator.py",
        "core/unified_mcp_generator.py": "src/generators/mcp_generator.py",
        "core/mcp_prompt_generator.py": "src/generators/prompt_generator.py", 
        "core/implementation_doc_generator.py": "src/generators/doc_generator.py",
        
        # Cases
        "cases/bmc_input_case.py": "src/cases/bmc_input_case.py",
        "cases/__init__.py": "src/cases/__init__.py",
        
        # Scripts útiles
        "scripts/create_release.py": "tools/scripts/create_release.py",
        
        # Configuración
        "docs/specifications/config/bmc-consolidated-config.json": "config/bmc-config.json",
        "docs/specifications/config/README.md": "config/README.md",
        
        # Main files
        "main.py": "src/main.py",
        "requirements.txt": "requirements.txt"
    }
    
    for old_path, new_path in file_mapping.items():
        if Path(old_path).exists():
            # Crear directorio padre si no existe
            Path(new_path).parent.mkdir(parents=True, exist_ok=True)
            
            # Mover archivo
            shutil.move(old_path, new_path)
            print(f"  📦 {old_path} → {new_path}")

def cleanup_obsolete_files():
    """Elimina archivos obsoletos"""
    
    print("🗑️ Eliminando archivos obsoletos...")
    
    analysis = analyze_current_structure()
    
    # Eliminar archivos core obsoletos
    for file_name in analysis["core_obsolete"]:
        file_path = Path("core") / file_name
        if file_path.exists():
            file_path.unlink()
            print(f"  ❌ core/{file_name}")
    
    # Eliminar scripts raíz obsoletos
    for file_name in analysis["root_obsolete"]:
        file_path = Path(file_name)
        if file_path.exists():
            file_path.unlink()
            print(f"  ❌ {file_name}")
    
    # Eliminar directorios vacíos
    empty_dirs = ["core", "cases", "scripts", "infrastructure", "docs/specifications"]
    for dir_name in empty_dirs:
        dir_path = Path(dir_name)
        if dir_path.exists() and not any(dir_path.iterdir()):
            shutil.rmtree(dir_path)
            print(f"  🗂️ {dir_name}/")

def create_init_files():
    """Crea archivos __init__.py necesarios"""
    
    print("📝 Creando archivos __init__.py...")
    
    init_files = [
        "src/__init__.py",
        "src/core/__init__.py", 
        "src/generators/__init__.py",
        "src/parsers/__init__.py",
        "src/cases/__init__.py"
    ]
    
    for init_file in init_files:
        with open(init_file, 'w') as f:
            f.write('"""MCP Diagram Generator Module"""\n')
        print(f"  ✓ {init_file}")

def update_imports():
    """Actualiza imports en archivos movidos"""
    
    print("🔧 Actualizando imports...")
    
    # Actualizar main.py
    main_file = Path("src/main.py")
    if main_file.exists():
        content = main_file.read_text()
        
        # Actualizar imports
        content = content.replace("from cases.", "from .cases.")
        content = content.replace("from core.", "from .core.")
        
        main_file.write_text(content)
        print("  ✓ src/main.py imports updated")

def create_new_readme():
    """Crea README actualizado"""
    
    readme_content = """# MCP Diagram Generator

Generador unificado de diagramas, prompts y documentación para arquitecturas AWS.

## 🏗️ Estructura del Proyecto

```
├── src/                    # Código fuente principal
│   ├── core/              # Módulos core (config, utils)
│   ├── generators/        # Generadores (diagramas, prompts, docs)
│   ├── parsers/           # Parsers de especificaciones
│   ├── cases/             # Casos de uso específicos
│   └── main.py            # Punto de entrada principal
├── tools/                 # Herramientas y scripts
│   ├── scripts/           # Scripts de automatización
│   └── utilities/         # Utilidades de desarrollo
├── config/                # Configuraciones del proyecto
├── outputs/               # Archivos generados
├── docs/                  # Documentación
└── tests/                 # Tests unitarios
```

## 🚀 Uso

```bash
# Generar diagramas BMC
python src/main.py --case bmc-input

# Ver estructura generada
ls outputs/mcp/
```

## 📦 Componentes Principales

### Generadores
- **DiagramGenerator** - Diagramas PNG/DrawIO
- **MCPGenerator** - Diagramas Mermaid unificados  
- **PromptGenerator** - Prompts especializados MCP
- **DocGenerator** - Documentación de implementación

### Parsers
- **BMCInputParser** - Parser de especificaciones BMC

### Core
- **ConfigManager** - Gestión de configuración única

## 🎯 Características

- ✅ Generación unificada desde configuración MCP
- ✅ Diagramas Mermaid, PNG y DrawIO
- ✅ Prompts especializados por rol
- ✅ Documentación técnica automática
- ✅ Estructura organizada sin duplicados
"""
    
    with open("README.md", 'w') as f:
        f.write(readme_content)
    
    print("✓ README.md actualizado")

def restructure_solution():
    """Ejecuta reestructuración completa"""
    
    print("🔄 Reestructurando solución MCP...")
    print("=" * 50)
    
    # 1. Analizar estructura actual
    analysis = analyze_current_structure()
    print(f"📊 Archivos activos: {len(analysis['core_active'])}")
    print(f"📊 Archivos obsoletos: {len(analysis['core_obsolete']) + len(analysis['root_obsolete'])}")
    
    # 2. Crear nueva estructura
    create_new_structure()
    
    # 3. Reorganizar archivos
    reorganize_files()
    
    # 4. Limpiar obsoletos
    cleanup_obsolete_files()
    
    # 5. Crear archivos init
    create_init_files()
    
    # 6. Actualizar imports
    update_imports()
    
    # 7. Crear README
    create_new_readme()
    
    print("\n✅ Reestructuración completada")
    print("\n📁 Nueva estructura:")
    print("  src/core/           - Módulos core")
    print("  src/generators/     - Generadores unificados")
    print("  src/parsers/        - Parsers de especificaciones")
    print("  src/cases/          - Casos de uso")
    print("  tools/              - Scripts y utilidades")
    print("  config/             - Configuración única")

if __name__ == "__main__":
    restructure_solution()
