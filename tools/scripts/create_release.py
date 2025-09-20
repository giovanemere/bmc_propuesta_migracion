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
    diagrams_zip = release_dir / "bmc_mcp_diagrams_v3.1.0.zip"
    
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
    source_zip = release_dir / "mcp_generator_source_v3.1.0.zip"
    
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
    
    version = "v3.1.0"
    
    # Crear assets
    assets = create_release_assets()
    
    # Crear tag
    print(f"🏷️ Creando tag {version}...")
    subprocess.run(["git", "tag", "-a", version, "-m", f"Release {version}"], check=True)
    subprocess.run(["git", "push", "origin", version], check=True)
    
    # Release notes
    release_notes = f"""# MCP Diagram Generator v3.1.0

## 🎉 Nueva Característica Principal

### 📝 Generador de Prompts MCP
- **3 tipos de prompts especializados**: Arquitectura, Migración, Implementación
- **Especificaciones técnicas detalladas** extraídas de configuración BMC
- **Prompts contextualizados** para arquitectos, desarrolladores y especialistas
- **Métricas de rendimiento** incluidas (60M productos, 10K facturas/hora)
- **Compliance regulatorio** DIAN integrado

## 🔧 Mejoras Técnicas

### Prompts Generados
- **`architecture_prompt.md`** - Contexto del sistema y diseño AWS
- **`implementation_prompt.md`** - Especificaciones técnicas y código
- **`migration_prompt.md`** - Estrategia Strangler Fig y plan detallado

### Integración Automática
- Generación automática con `python3 main.py --case bmc-input`
- Ubicación organizada en `outputs/mcp/prompts/`
- Script `show_mcp_prompts.py` para visualización

## 📊 Contenido de Prompts

### Arquitectura
- 5 microservicios mapeados con recursos AWS
- Consideraciones de escalamiento y alta disponibilidad
- Patrones de diseño para compliance regulatorio

### Implementación  
- Performance KPIs específicos (< 300ms lookup, > 95% OCR)
- Configuración de infraestructura AWS detallada
- Especificaciones de seguridad y monitoreo

### Migración
- Patrón Strangler Fig con 4 fases definidas
- Análisis de riesgos y mitigaciones
- Plan de rollback y validación

## 🛠️ Herramientas Actualizadas

```bash
# Generar todos los artefactos MCP (diagramas + prompts)
python3 main.py --case bmc-input

# Visualizar prompts generados
python3 show_mcp_prompts.py

# Validar estructura completa
python3 validate_single_config.py
```

## 📁 Archivos del Release

- `bmc_mcp_diagrams_v3.1.0.zip` - Diagramas, prompts y configuración MCP
- `mcp_generator_source_v3.1.0.zip` - Código fuente con generador de prompts

## 🔄 Actualización desde v3.0.0

Los usuarios de v3.0.0 pueden actualizar ejecutando:
```bash
git pull origin main
python3 main.py --case bmc-input
```

Los prompts se generarán automáticamente en la estructura MCP existente.

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
