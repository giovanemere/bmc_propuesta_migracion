#!/usr/bin/env python3
"""
MCP Service para Diagramas BMC
Servicio que lee el MCP y genera diagramas automáticamente
"""

import json
import os
from pathlib import Path

class MCPDiagramService:
    def __init__(self, mcp_file=None):
        if mcp_file is None:
            # Buscar el archivo MCP desde el directorio actual
            import os
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.mcp_file = os.path.join(base_dir, "docs/mcp-diagrams-architecture.md")
        else:
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
