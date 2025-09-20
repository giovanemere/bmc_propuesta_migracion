#!/usr/bin/env python3
"""
Script para organizar archivos CP en outputs/mcp
Evita confusión con otras salidas del sistema
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

def organize_cp_outputs():
    """Organiza archivos CP en estructura outputs/mcp"""
    
    # Directorios base
    base_dir = Path(__file__).parent
    outputs_dir = base_dir / "outputs"
    mcp_dir = outputs_dir / "mcp"
    
    # Crear estructura MCP si no existe
    mcp_dir.mkdir(parents=True, exist_ok=True)
    
    # Subdirectorios para organización
    subdirs = {
        "diagrams": mcp_dir / "diagrams",
        "configs": mcp_dir / "configs", 
        "reports": mcp_dir / "reports",
        "documentation": mcp_dir / "documentation"
    }
    
    for subdir in subdirs.values():
        subdir.mkdir(parents=True, exist_ok=True)
    
    print("🗂️ Organizando archivos CP en outputs/mcp/")
    print("=" * 50)
    
    # Buscar archivos BMC input generados
    bmc_input_dir = outputs_dir / "bmc_input"
    
    if bmc_input_dir.exists():
        # Copiar diagramas
        diagrams_src = bmc_input_dir / "diagrams"
        if diagrams_src.exists():
            diagrams_dest = subdirs["diagrams"] / "bmc_input"
            if diagrams_dest.exists():
                shutil.rmtree(diagrams_dest)
            shutil.copytree(diagrams_src, diagrams_dest)
            print(f"✓ Diagramas copiados a: {diagrams_dest}")
        
        # Copiar reportes
        reports_src = bmc_input_dir / "reports"
        if reports_src.exists():
            reports_dest = subdirs["reports"] / "bmc_input"
            if reports_dest.exists():
                shutil.rmtree(reports_dest)
            shutil.copytree(reports_src, reports_dest)
            print(f"✓ Reportes copiados a: {reports_dest}")
        
        # Copiar configuración
        config_src = bmc_input_dir / "config"
        if config_src.exists():
            config_dest = subdirs["configs"] / "bmc_input"
            if config_dest.exists():
                shutil.rmtree(config_dest)
            shutil.copytree(config_src, config_dest)
            print(f"✓ Configuración copiada a: {config_dest}")
    
    # Crear archivo índice
    create_mcp_index(mcp_dir)
    
    print(f"\n🎉 Archivos CP organizados en: {mcp_dir}")
    return True

def create_mcp_index(mcp_dir: Path):
    """Crea archivo índice de archivos MCP"""
    
    index_file = mcp_dir / "README.md"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    content = f"""# Archivos CP (Código de Prueba) - MCP
Generado: {timestamp}

## Estructura de Archivos CP

### 📊 Diagramas
- **Ubicación:** `diagrams/`
- **Formatos:** PNG, DrawIO, SVG
- **Propósito:** Diagramas de arquitectura generados desde especificaciones BMC

### 📋 Reportes
- **Ubicación:** `reports/`
- **Formato:** Markdown
- **Contenido:** Reportes de generación y métricas

### ⚙️ Configuraciones
- **Ubicación:** `configs/`
- **Formato:** JSON, YAML
- **Propósito:** Configuraciones MCP extraídas de especificaciones

### 📚 Documentación
- **Ubicación:** `documentation/`
- **Formato:** Markdown, PDF
- **Contenido:** Documentación técnica generada

## Casos Procesados

### BMC Input Case
- **Especificación:** `docs/specifications/bmc-input-specification.md`
- **Microservicios:** 5 servicios mapeados
- **AWS Services:** 4 servicios configurados
- **KPIs:** 10,000 facturas/hora, 60M productos

## Uso

Para generar nuevos archivos CP:
```bash
python3 main.py --case bmc-input
python3 organize_cp_outputs.py
```

## Separación de Outputs

Los archivos CP se mantienen separados de otras salidas del sistema:
- `outputs/mcp/` - Archivos CP específicos
- `outputs/bmc_input/` - Salidas originales BMC
- `outputs/generic/` - Otras salidas del sistema
"""
    
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Índice creado: {index_file}")

if __name__ == "__main__":
    organize_cp_outputs()
