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
    diagrams_zip = release_dir / "bmc_mcp_diagrams_v3.0.0.zip"
    
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
    source_zip = release_dir / "mcp_generator_source_v3.0.0.zip"
    
    with zipfile.ZipFile(source_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Core files
        for py_file in Path("core").glob("*.py"):
            zf.write(py_file, f"core/{py_file.name}")
        
        # Cases
        for py_file in Path("cases").glob("*.py"):
            zf.write(py_file, f"cases/{py_file.name}")
        
        # Scripts principales
        main_files = ["main.py", "requirements.txt", "README.md"]
        for file_name in main_files:
            if Path(file_name).exists():
                zf.write(file_name, file_name)
        
        # Scripts de utilidad
        util_scripts = [
            "consolidate_config.py",
            "validate_single_config.py", 
            "fix_drawio_files.py",
            "organize_cp_outputs.py"
        ]
        for script in util_scripts:
            if Path(script).exists():
                zf.write(script, f"scripts/{script}")
    
    print(f"✅ Assets creados:")
    print(f"  - {diagrams_zip}")
    print(f"  - {source_zip}")
    
    return [str(diagrams_zip), str(source_zip)]

def create_github_release():
    """Crea release en GitHub"""
    
    version = "v3.0.0"
    
    # Crear assets
    assets = create_release_assets()
    
    # Crear tag
    print(f"🏷️ Creando tag {version}...")
    subprocess.run(["git", "tag", "-a", version, "-m", f"Release {version}"], check=True)
    subprocess.run(["git", "push", "origin", version], check=True)
    
    # Release notes
    release_notes = f"""# MCP Diagram Generator v3.0.0

## 🎉 Nuevas Características

### ✅ Configuración Consolidada
- **Archivo único**: `bmc-consolidated-config.json`
- **Backup automático** de configuraciones anteriores
- **Validación** de configuración única

### 🔧 Corrección DrawIO
- **Errores mxCell solucionados**
- **XML válido** compatible con draw.io
- **Validador automático** de archivos DrawIO

### 📁 Estructura MCP Unificada
- **Solo `outputs/mcp/`** - Sin duplicados
- **Organización CP** separada de otras salidas
- **Scripts de limpieza** automática

## 🛠️ Herramientas Incluidas

### Scripts de Validación
```bash
python3 validate_single_config.py  # Validar configuración única
python3 validate_drawio.py         # Validar archivos DrawIO
```

### Scripts de Organización
```bash
python3 organize_cp_outputs.py     # Organizar archivos CP
python3 fix_duplicate_outputs.py   # Eliminar duplicados
```

## 📊 Métricas del Proyecto BMC

- **Microservicios**: 5 servicios mapeados
- **AWS Services**: 4 servicios configurados  
- **Throughput**: 10,000 facturas/hora
- **Base de datos**: 60M productos

## 🔄 Migración desde v2.x

1. Ejecutar `python3 consolidate_config.py`
2. Ejecutar `python3 use_only_mcp.py`
3. Validar con `python3 validate_single_config.py`

## 📁 Archivos Incluidos

- `bmc_mcp_diagrams_v3.0.0.zip` - Diagramas y configuración MCP
- `mcp_generator_source_v3.0.0.zip` - Código fuente completo

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
