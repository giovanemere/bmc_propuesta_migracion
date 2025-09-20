#!/usr/bin/env python3
"""
GitHub Release Creator - Crea release v3.0.0 con estructura MCP
"""

import os
import subprocess
import zipfile
from pathlib import Path
from datetime import datetime

def create_release_assets():
    """Crea archivos para release v3.0.0"""
    
    print("📦 Creando assets para release v3.0.0...")
    
    # Crear directorio de release
    release_dir = Path("release_assets")
    release_dir.mkdir(exist_ok=True)
    
    # Crear ZIP con diagramas MCP
    diagrams_zip = release_dir / "bmc_mcp_clean_v4.0.0.zip"
    
    with zipfile.ZipFile(diagrams_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Agregar archivos MCP
        mcp_dir = Path("outputs/mcp")
        if mcp_dir.exists():
            for file_path in mcp_dir.rglob("*"):
                if file_path.is_file():
                    rel_path = file_path.relative_to(mcp_dir)
                    zf.write(file_path, f"mcp/{rel_path}")
        
        # Agregar configuración consolidada
        config_file = Path("docs/specifications/config/bmc-consolidated-config.json")
        if config_file.exists():
            zf.write(config_file, "config/bmc-consolidated-config.json")
    
    # Crear ZIP con código fuente
    source_zip = release_dir / "mcp_generator_restructured_v4.0.0.zip"
    
    with zipfile.ZipFile(source_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Src files
        for py_file in Path("src").rglob("*.py"):
            zf.write(py_file, str(py_file))
        
        # Config
        for config_file in Path("config").glob("*"):
            if config_file.is_file():
                zf.write(config_file, f"config/{config_file.name}")
        
        # Tools
        for tool_file in Path("tools").rglob("*.py"):
            zf.write(tool_file, str(tool_file))
        
        # Main files
        main_files = ["requirements.txt", "README.md"]
        for file_name in main_files:
            if Path(file_name).exists():
                zf.write(file_name, file_name)
    
    print(f"✅ Assets creados:")
    print(f"  - {diagrams_zip}")
    print(f"  - {source_zip}")
    
    return [str(diagrams_zip), str(source_zip)]

def create_github_release():
    """Crea release en GitHub"""
    
    version = "v4.0.0"
    
    # Crear assets
    assets = create_release_assets()
    
    # Crear tag
    print(f"🏷️ Creando tag {version}...")
    subprocess.run(["git", "tag", "-a", version, "-m", f"Release {version}"], check=True)
    subprocess.run(["git", "push", "origin", version], check=True)
    
    # Release notes
    release_notes = f"""# MCP Diagram Generator v4.0.0 - Major Restructure

## 🎉 Reestructuración Completa del Proyecto

### 🏗️ Nueva Arquitectura Modular
- **`src/`** - Código fuente organizado por responsabilidades
- **`src/generators/`** - Generadores especializados (diagramas, prompts, docs)
- **`src/parsers/`** - Parsers de especificaciones
- **`src/cases/`** - Casos de uso específicos
- **`config/`** - Configuración única consolidada

### 🧹 Limpieza Masiva de Código
- **21 archivos obsoletos eliminados**
- **11 generadores DrawIO duplicados** removidos
- **10 scripts de utilidad obsoletos** eliminados
- **Carpetas duplicadas** corregidas
- **83 archivos modificados** en total

### ✅ Corrección de Duplicación
- **Problema:** `outputs/mcp/diagrams/bmc_input/diagrams/` (carpetas duplicadas)
- **Solución:** Estructura unificada sin duplicación
- **Resultado:** 16 archivos únicos vs 25+ duplicados anteriormente

## 🎯 Beneficios de v4.0.0

### Código Limpio
- Solo módulos activos necesarios
- Imports corregidos sin dependencias rotas
- Separación clara de responsabilidades

### Generación Optimizada
- **4 diagramas PNG** únicos
- **3 diagramas Mermaid** automáticos  
- **2 archivos DrawIO** (1 unificado + 1 minimal)
- **3 prompts MCP** especializados
- **4 documentos** de implementación

### Estructura Final
```
src/
├── generators/    # 4 generadores especializados
├── parsers/       # 1 parser BMC
├── cases/         # 1 caso de uso
├── core/          # 1 config manager
└── main.py        # Punto de entrada único

config/            # Configuración consolidada
tools/             # Scripts de release
outputs/mcp/       # Salidas organizadas (16 archivos únicos)
```

## 🔧 Uso Simplificado

```bash
# Generar todos los artefactos MCP
python src/main.py --case bmc-input

# Estructura generada (sin duplicados)
outputs/mcp/diagrams/bmc_input/
├── mermaid/       # 3 diagramas Mermaid
├── drawio/        # 2 archivos DrawIO
├── png/           # 4 diagramas PNG  
├── prompts/       # 3 prompts especializados
└── documentation/ # 4 docs de implementación
```

## 📊 Métricas de Limpieza

- **Archivos eliminados:** 21 obsoletos
- **Duplicados removidos:** 9 archivos
- **Carpetas duplicadas:** 0 (corregidas)
- **Estructura final:** 16 archivos únicos
- **Reducción de código:** ~4,300 líneas eliminadas

## 🔄 Migración desde v3.x

Los usuarios de versiones anteriores deben:
1. Usar nueva estructura: `python src/main.py --case bmc-input`
2. Configuración en: `config/bmc-config.json`
3. Salidas en: `outputs/mcp/` (estructura limpia)

## 📁 Archivos del Release

- `bmc_mcp_clean_v4.0.0.zip` - Diagramas y configuración limpia
- `mcp_generator_restructured_v4.0.0.zip` - Código fuente reestructurado

## 🎉 Resultado Final

Proyecto completamente reestructurado, optimizado y sin duplicación. 
Código limpio, modular y mantenible para desarrollo futuro.

Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    # Crear release usando GitHub CLI si está disponible
    try:
        cmd = [
            "gh", "release", "create", version,
            "--title", f"MCP Diagram Generator {version}",
            "--notes", release_notes
        ]
        
        # Agregar assets
        for asset in assets:
            cmd.append(asset)
        
        subprocess.run(cmd, check=True)
        print(f"🎉 Release {version} creado exitosamente!")
        
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f"⚠️ GitHub CLI no disponible. Release manual requerido.")
        print(f"📝 Release notes guardadas en release_notes.md")
        
        with open("release_notes.md", "w") as f:
            f.write(release_notes)

if __name__ == "__main__":
    create_github_release()
