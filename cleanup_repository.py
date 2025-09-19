#!/usr/bin/env python3
"""
Limpieza y Estructuración del Repositorio BMC
Organiza archivos, elimina obsoletos y crea estructura estable
"""

import os
import shutil
from pathlib import Path

def create_directory_structure():
    """Crea la estructura de directorios organizada"""
    
    print("📁 Creando estructura de directorios...")
    
    directories = [
        "docs",
        "infrastructure/diagrams",
        "infrastructure/terraform", 
        "output/png",
        "output/drawio",
        "scripts",
        "archive"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ {directory}")

def move_active_files():
    """Mueve archivos activos a su ubicación correcta"""
    
    print("\n📋 Organizando archivos activos...")
    
    # Archivos de documentación
    docs_files = [
        "diagramas-aws-mermaid.md",
        "flujos-proceso-mermaid.md", 
        "README-DIAGRAMAS-BMC.md",
        "PROPUESTA-ARQUITECTURA-BMC.md",
        "mcp-arquitectura-bmc.md",
        "mcp-diagrams-architecture.md"
    ]
    
    for file in docs_files:
        if os.path.exists(file):
            shutil.move(file, f"docs/{file}")
            print(f"✓ {file} → docs/")
    
    # Archivos PNG generados
    png_files = [f for f in os.listdir('.') if f.endswith('.png') and 'bmc' in f]
    for file in png_files:
        if os.path.exists(f"infrastructure/diagrams/{file}"):
            shutil.move(f"infrastructure/diagrams/{file}", f"output/png/{file}")
            print(f"✓ {file} → output/png/")
    
    # Archivos Draw.io generados
    drawio_files = [f for f in os.listdir('.') if f.endswith('.drawio') and 'bmc' in f]
    for file in drawio_files:
        if os.path.exists(f"infrastructure/diagrams/{file}"):
            shutil.move(f"infrastructure/diagrams/{file}", f"output/drawio/{file}")
            print(f"✓ {file} → output/drawio/")

def archive_obsolete_files():
    """Archiva archivos obsoletos"""
    
    print("\n🗄️ Archivando archivos obsoletos...")
    
    obsolete_files = [
        # Versiones antiguas de generadores
        "infrastructure/diagrams/bmc_architecture.py",
        "infrastructure/diagrams/bmc_drawio_generator.py",
        "infrastructure/diagrams/bmc_final_professional.py",
        "infrastructure/diagrams/mermaid_converter_fixed.py",
        "infrastructure/diagrams/generate_enhanced.sh",
        "infrastructure/diagrams/bmc_architecture_fixed.py",
        "infrastructure/diagrams/bmc_drawio_aws_icons.py",
        "infrastructure/diagrams/bmc_drawio_fixed.py",
        "infrastructure/diagrams/bmc_drawio_simple.py",
        "infrastructure/diagrams/bmc_final.py",
        "infrastructure/diagrams/bmc_fixed_xml.py",
        "infrastructure/diagrams/bmc_improved_groups.py",
        "infrastructure/diagrams/bmc_professional.py",
        "infrastructure/diagrams/bmc_simple.py",
        "infrastructure/diagrams/mermaid_final.py",
        "infrastructure/diagrams/mermaid_to_python.py",
        
        # MCP files no utilizados
        "mcp-catalogo.py",
        "mcp-estructuracion.py", 
        "mcp-lineamientos.py",
        "mcp-precaracterizacion.py",
        "mcp-server.py",
        "mcp-workflow.py",
        
        # Documentación obsoleta
        "DIAGRAMAS-GENERADOS.md",
        "DIAGRAMAS-MERMAID-BMC.md",
        "GUIA-IMPLEMENTACION-TECNICA.md",
        "INSTRUCCIONES-PNG.md",
        "RESULTADO-ACTUALIZADO.md",
        "RESULTADO-MODELO.md",
        "USAGE.md",
        "metodologia-mcp.md"
    ]
    
    for file in obsolete_files:
        if os.path.exists(file):
            # Crear directorio de archivo si no existe
            archive_dir = f"archive/{os.path.dirname(file)}" if os.path.dirname(file) else "archive"
            Path(archive_dir).mkdir(parents=True, exist_ok=True)
            
            shutil.move(file, f"archive/{os.path.basename(file)}")
            print(f"✓ {file} → archive/")

def create_main_scripts():
    """Crea scripts principales en el directorio scripts/"""
    
    print("\n🔧 Creando scripts principales...")
    
    # Script principal de generación
    generate_script = """#!/bin/bash

# BMC Diagram Generator - Main Script
# Generates architecture diagrams from MCP model

echo "🚀 BMC Architecture Diagram Generator"
echo "====================================="

cd "$(dirname "$0")/../infrastructure/diagrams"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "🐍 Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

# Generate diagrams
echo "🎨 Generating diagrams..."
python3 generate_complete.py

# Move outputs
echo "📁 Moving outputs..."
mv *.png ../../output/png/ 2>/dev/null || true
mv *.drawio ../../output/drawio/ 2>/dev/null || true

echo "✅ Generation complete!"
echo "📊 PNG files: output/png/"
echo "🎨 Draw.io files: output/drawio/"
"""
    
    with open("scripts/generate_diagrams.sh", "w") as f:
        f.write(generate_script)
    
    os.chmod("scripts/generate_diagrams.sh", 0o755)
    print("✓ scripts/generate_diagrams.sh")

def create_readme():
    """Crea README principal actualizado"""
    
    print("\n📝 Creando README principal...")
    
    readme_content = """# BMC AWS Architecture - Diagram Generator

Generador automatizado de diagramas de arquitectura AWS para el proyecto BMC (Bolsa Mercantil de Colombia).

## 🚀 Generación Rápida

```bash
# Generar todos los diagramas
./scripts/generate_diagrams.sh
```

## 📁 Estructura del Proyecto

```
├── docs/                           # Documentación
│   ├── mcp-diagrams-architecture.md   # MCP principal
│   ├── diagramas-aws-mermaid.md       # Diagramas Mermaid
│   └── README-DIAGRAMAS-BMC.md        # Guía de uso
├── infrastructure/
│   ├── diagrams/                   # Generadores Python
│   │   ├── generate_complete.py       # Generador principal
│   │   ├── generate_final_version.sh  # Script de generación
│   │   └── requirements.txt           # Dependencias
│   └── terraform/                  # Infrastructure as Code (futuro)
├── output/
│   ├── png/                        # Diagramas PNG generados
│   └── drawio/                     # Archivos Draw.io generados
├── scripts/
│   └── generate_diagrams.sh           # Script principal
└── archive/                        # Archivos obsoletos

```

## 🎯 Características

- **60M productos** en base de datos PostgreSQL
- **OCR >95% precisión** con Amazon Textract
- **10K facturas/hora** de throughput
- **99.9% disponibilidad** con Multi-AZ
- **Auto-scaling** 2-15 instancias por servicio

## 📊 Diagramas Generados

### PNG (para presentaciones)
- `bmc_complete_architecture.png` - Arquitectura completa
- `bmc_microservices_complete.png` - Detalle microservicios

### Draw.io (para edición)
- `bmc_complete_architecture.drawio` - Editable en https://app.diagrams.net

## 🔧 Desarrollo

### Requisitos
- Python 3.9+
- Graphviz
- Virtual environment

### Instalación
```bash
cd infrastructure/diagrams
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Generar Diagramas
```bash
# Método 1: Script principal
./scripts/generate_diagrams.sh

# Método 2: Manual
cd infrastructure/diagrams
source venv/bin/activate
python3 generate_complete.py
```

## 📋 MCP (Model Context Protocol)

El proyecto utiliza MCP para definir la arquitectura:
- **Archivo principal**: `docs/mcp-diagrams-architecture.md`
- **Servicios AWS**: 16 servicios implementados
- **Microservicios**: 5 servicios en ECS Fargate
- **Métricas**: KPIs y targets de rendimiento

## 🏗️ Servicios AWS

### Compute
- ECS Fargate (microservicios)
- Lambda (procesamiento)

### Storage  
- RDS PostgreSQL (60M productos)
- ElastiCache Redis (cache)
- S3 (documentos)

### Network
- API Gateway
- CloudFront CDN
- Application Load Balancer

### Security
- Cognito (auth)
- WAF (firewall)
- KMS (encryption)

### AI/ML
- Textract (OCR >95%)

### Integration
- EventBridge (eventos)
- SQS/SNS (mensajería)

### Monitoring
- CloudWatch (métricas)
- X-Ray (tracing)

## 📈 Métricas

- **OCR Processing**: <5s
- **Product Lookup**: <500ms (60M records)
- **Throughput**: 10K invoices/hour
- **Availability**: >99.9%
- **Cost**: $8,650/month

## 🔄 Versionado

- **v2.0.0**: Actual - MCP + generación automatizada
- **v1.0.0**: Inicial - Diagramas Mermaid básicos

## 📞 Soporte

Para modificar diagramas:
1. Editar `docs/mcp-diagrams-architecture.md`
2. Actualizar `infrastructure/diagrams/generate_complete.py`
3. Ejecutar `./scripts/generate_diagrams.sh`
"""
    
    with open("README.md", "w") as f:
        f.write(readme_content)
    
    print("✓ README.md actualizado")

def main():
    print("🧹 Limpieza y Estructuración del Repositorio BMC")
    print("=" * 55)
    
    # Crear estructura de directorios
    create_directory_structure()
    
    # Mover archivos activos
    move_active_files()
    
    # Archivar archivos obsoletos
    archive_obsolete_files()
    
    # Crear scripts principales
    create_main_scripts()
    
    # Crear README actualizado
    create_readme()
    
    print("\n✅ Limpieza y estructuración completada!")
    print("\n📊 Resumen:")
    print("- Estructura de directorios organizada")
    print("- Archivos activos movidos a ubicaciones correctas")
    print("- Archivos obsoletos archivados")
    print("- Scripts principales creados")
    print("- README actualizado")
    
    print("\n🚀 Para generar diagramas:")
    print("./scripts/generate_diagrams.sh")
    
    print("\n📁 Estructura final:")
    print("docs/ - Documentación y MCP")
    print("infrastructure/ - Generadores y Terraform")
    print("output/ - Diagramas generados")
    print("scripts/ - Scripts principales")
    print("archive/ - Archivos obsoletos")

if __name__ == "__main__":
    main()
