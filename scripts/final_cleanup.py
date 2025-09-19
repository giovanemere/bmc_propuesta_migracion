#!/usr/bin/env python3
"""
Limpieza Final del Repositorio BMC
Reorganiza archivos restantes y elimina componentes no utilizados
"""

import os
import shutil
from pathlib import Path

def move_root_files():
    """Mueve archivos de la raíz a ubicaciones apropiadas"""
    
    print("📁 Reorganizando archivos de la raíz...")
    
    # Archivos JSON - mover a docs/config/
    Path("docs/config").mkdir(exist_ok=True)
    
    json_files = [
        "bmc-analysis-complete.json",
        "bmc-analysis-updated.json", 
        "bmc-workflow-complete-with-diagrams.json",
        "mcp-config.json"
    ]
    
    for file in json_files:
        if os.path.exists(file):
            shutil.move(file, f"docs/config/{file}")
            print(f"✓ {file} → docs/config/")
    
    # Scripts - mover a scripts/ o archivar
    if os.path.exists("generate-png-diagrams.sh"):
        shutil.move("generate-png-diagrams.sh", "archive/generate-png-diagrams.sh")
        print("✓ generate-png-diagrams.sh → archive/ (obsoleto)")
    
    if os.path.exists("mcp-parser.py"):
        shutil.move("mcp-parser.py", "scripts/mcp-parser.py")
        print("✓ mcp-parser.py → scripts/")
    
    if os.path.exists("cleanup_repository.py"):
        shutil.move("cleanup_repository.py", "scripts/cleanup_repository.py")
        print("✓ cleanup_repository.py → scripts/")

def remove_unused_infrastructure():
    """Elimina Docker y Terraform que no son parte de esta solución"""
    
    print("\n🗑️ Eliminando infraestructura no utilizada...")
    
    # Eliminar Docker
    if os.path.exists("infrastructure/docker"):
        shutil.rmtree("infrastructure/docker")
        print("✓ infrastructure/docker/ eliminado")
    
    # Mover Terraform a archive (no es parte de la solución de diagramas)
    if os.path.exists("infrastructure/terraform"):
        shutil.move("infrastructure/terraform", "archive/terraform")
        print("✓ infrastructure/terraform/ → archive/terraform/")

def create_mcp_service():
    """Crea servicio MCP mejorado para diagramas"""
    
    print("\n🔧 Creando servicio MCP mejorado...")
    
    mcp_service = '''#!/usr/bin/env python3
"""
MCP Service para Diagramas BMC
Servicio que lee el MCP y genera diagramas automáticamente
"""

import json
import os
from pathlib import Path

class MCPDiagramService:
    def __init__(self, mcp_file="docs/mcp-diagrams-architecture.md"):
        self.mcp_file = mcp_file
        self.config = self.load_config()
    
    def load_config(self):
        """Carga configuración desde archivos JSON"""
        config_files = [
            "docs/config/mcp-config.json",
            "docs/config/bmc-workflow-complete-with-diagrams.json"
        ]
        
        config = {}
        for file in config_files:
            if os.path.exists(file):
                with open(file, 'r') as f:
                    config.update(json.load(f))
        
        return config
    
    def read_mcp(self):
        """Lee el archivo MCP y extrae configuración de servicios"""
        if not os.path.exists(self.mcp_file):
            print(f"❌ MCP file not found: {self.mcp_file}")
            return None
        
        with open(self.mcp_file, 'r') as f:
            content = f.read()
        
        print(f"✓ MCP loaded from {self.mcp_file}")
        return content
    
    def generate_diagrams(self):
        """Genera diagramas basados en el MCP"""
        print("🎨 Generating diagrams from MCP...")
        
        # Ejecutar el generador principal
        os.system("./scripts/generate_diagrams.sh")
        
        print("✅ Diagrams generated from MCP")
    
    def validate_mcp(self):
        """Valida que el MCP tenga toda la información necesaria"""
        content = self.read_mcp()
        if not content:
            return False
        
        required_sections = [
            "Servicios AWS Utilizados",
            "Configuración de Servicios", 
            "Métricas y KPIs",
            "Comandos de Generación"
        ]
        
        missing = []
        for section in required_sections:
            if section not in content:
                missing.append(section)
        
        if missing:
            print(f"⚠️ Missing MCP sections: {missing}")
            return False
        
        print("✅ MCP validation passed")
        return True
    
    def run(self):
        """Ejecuta el servicio MCP"""
        print("🚀 MCP Diagram Service Starting...")
        
        if self.validate_mcp():
            self.generate_diagrams()
            print("🎉 MCP Service completed successfully!")
        else:
            print("❌ MCP Service failed validation")

if __name__ == "__main__":
    service = MCPDiagramService()
    service.run()
'''
    
    with open("scripts/mcp_service.py", "w") as f:
        f.write(mcp_service)
    
    os.chmod("scripts/mcp_service.py", 0o755)
    print("✓ scripts/mcp_service.py creado")

def create_terraform_diagram_generator():
    """Crea generador de diagramas desde Terraform (futuro)"""
    
    print("\n📋 Creando generador desde Terraform (placeholder)...")
    
    tf_generator = '''#!/usr/bin/env python3
"""
Terraform to Diagram Generator (Future Feature)
Genera diagramas desde archivos main.tf
"""

import json
import os

def parse_terraform_file(tf_file):
    """Parse Terraform file and extract resources"""
    print(f"📄 Parsing Terraform file: {tf_file}")
    
    # TODO: Implementar parser de Terraform
    # Usar python-hcl2 o terraform-external-data
    
    resources = {
        "aws_ecs_service": [],
        "aws_rds_instance": [],
        "aws_elasticache_cluster": [],
        "aws_s3_bucket": [],
        "aws_api_gateway_rest_api": []
    }
    
    print("⚠️ Terraform parsing not implemented yet")
    return resources

def generate_diagram_from_terraform(tf_file, output_format="png"):
    """Generate diagram from Terraform file"""
    
    if not os.path.exists(tf_file):
        print(f"❌ Terraform file not found: {tf_file}")
        return False
    
    print(f"🏗️ Generating diagram from {tf_file}")
    
    # Parse Terraform
    resources = parse_terraform_file(tf_file)
    
    # Generate diagram code
    # TODO: Convert resources to Python diagrams code
    
    print("⚠️ Feature not implemented yet")
    print("💡 Use MCP-based generation instead: ./scripts/generate_diagrams.sh")
    
    return False

if __name__ == "__main__":
    # Example usage (when implemented)
    tf_file = "archive/terraform/main.tf"
    generate_diagram_from_terraform(tf_file)
'''
    
    with open("scripts/terraform_to_diagram.py", "w") as f:
        f.write(tf_generator)
    
    os.chmod("scripts/terraform_to_diagram.py", 0o755)
    print("✓ scripts/terraform_to_diagram.py creado (placeholder)")

def update_main_script():
    """Actualiza el script principal para usar MCP service"""
    
    print("\n🔄 Actualizando script principal...")
    
    updated_script = '''#!/bin/bash

# BMC Diagram Generator - Main Script with MCP Service
# Generates architecture diagrams from MCP model

echo "🚀 BMC Architecture Diagram Generator with MCP"
echo "=============================================="

# Check if MCP service should be used
if [ "$1" = "--mcp" ]; then
    echo "🔧 Using MCP Service..."
    cd "$(dirname "$0")"
    python3 mcp_service.py
    exit $?
fi

# Standard generation
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
echo ""
echo "💡 Usage options:"
echo "  ./scripts/generate_diagrams.sh        # Standard generation"
echo "  ./scripts/generate_diagrams.sh --mcp  # Use MCP service"
'''
    
    with open("scripts/generate_diagrams.sh", "w") as f:
        f.write(updated_script)
    
    os.chmod("scripts/generate_diagrams.sh", 0o755)
    print("✓ scripts/generate_diagrams.sh actualizado")

def main():
    print("🧹 Limpieza Final del Repositorio BMC")
    print("=" * 40)
    
    # Reorganizar archivos de la raíz
    move_root_files()
    
    # Eliminar infraestructura no utilizada
    remove_unused_infrastructure()
    
    # Crear servicio MCP mejorado
    create_mcp_service()
    
    # Crear generador desde Terraform (placeholder)
    create_terraform_diagram_generator()
    
    # Actualizar script principal
    update_main_script()
    
    print("\n✅ Limpieza final completada!")
    print("\n📊 Resumen:")
    print("- Archivos JSON movidos a docs/config/")
    print("- Scripts reorganizados en scripts/")
    print("- Docker eliminado (no utilizado)")
    print("- Terraform movido a archive/")
    print("- MCP service creado")
    print("- Generador Terraform placeholder creado")
    
    print("\n🚀 Comandos disponibles:")
    print("./scripts/generate_diagrams.sh        # Generación estándar")
    print("./scripts/generate_diagrams.sh --mcp  # Usar servicio MCP")
    print("./scripts/mcp_service.py              # Servicio MCP directo")
    
    print("\n📁 Estructura final limpia:")
    print("docs/ - Documentación, MCP y configuración")
    print("infrastructure/diagrams/ - Solo generadores Python")
    print("output/ - Diagramas generados")
    print("scripts/ - Scripts y servicios")
    print("archive/ - Todo lo obsoleto/no utilizado")

if __name__ == "__main__":
    main()
