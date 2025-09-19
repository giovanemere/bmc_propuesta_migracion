#!/usr/bin/env python3
"""
MCP Engine - Motor principal para generar diagramas desde MCP
Orquesta el proceso completo: Parse MCP → Generate Diagrams
"""

from .mcp_parser import MCPParser
from .diagram_generator import DiagramGenerator
from pathlib import Path
import json
from typing import Dict, Any, List

class MCPEngine:
    """Motor principal para generar diagramas desde archivos MCP"""
    
    def __init__(self, output_dir: str = "output"):
        self.output_dir = output_dir
        self.parser = None
        self.generator = None
        self.config = {}
        
    def load_mcp(self, mcp_file: str) -> bool:
        """Carga y parsea un archivo MCP"""
        self.parser = MCPParser(mcp_file)
        self.config = self.parser.parse()
        
        if not self.config:
            print(f"❌ Failed to parse MCP: {mcp_file}")
            return False
            
        print(f"✓ MCP parsed successfully: {mcp_file}")
        return True
    
    def load_config(self, config_file: str) -> bool:
        """Carga configuración desde archivo JSON/YAML"""
        config_path = Path(config_file)
        
        if not config_path.exists():
            print(f"❌ Config file not found: {config_file}")
            return False
            
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                if config_path.suffix.lower() == '.json':
                    self.config = json.load(f)
                else:
                    import yaml
                    self.config = yaml.safe_load(f)
                    
            print(f"✓ Config loaded: {config_file}")
            return True
            
        except Exception as e:
            print(f"❌ Error loading config: {e}")
            return False
    
    def generate_diagrams(self, project_name: str = "Project") -> Dict[str, str]:
        """Genera todos los diagramas"""
        
        if not self.config:
            print("❌ No configuration loaded")
            return {}
            
        self.generator = DiagramGenerator(self.config, self.output_dir)
        results = self.generator.generate_all(project_name)
        
        print(f"✅ Diagrams generated for {project_name}")
        for diagram_type, file_path in results.items():
            print(f"  - {diagram_type}: {file_path}")
            
        return results
    
    def validate_config(self) -> bool:
        """Valida que la configuración tenga los elementos mínimos"""
        
        if not self.config:
            print("❌ No configuration to validate")
            return False
            
        required_sections = ["services", "microservices"]
        missing = []
        
        for section in required_sections:
            if section not in self.config or not self.config[section]:
                missing.append(section)
        
        if missing:
            print(f"⚠️ Missing or empty sections: {missing}")
            print("💡 Will use default configuration")
            
        print("✅ Configuration validation passed")
        return True
    
    def get_supported_formats(self) -> List[str]:
        """Retorna formatos soportados"""
        return ["png", "drawio", "svg"]
    
    def get_config_summary(self) -> Dict[str, Any]:
        """Retorna resumen de la configuración cargada"""
        if not self.config:
            return {}
            
        summary = {
            "services_count": len(self.config.get("services", {})),
            "microservices_count": len(self.config.get("microservices", {})),
            "metrics_count": len(self.config.get("metrics", {})),
            "yaml_blocks_count": len(self.config.get("yaml_blocks", {}))
        }
        
        return summary
    
    def run(self, input_file: str, project_name: str = "Architecture") -> bool:
        """Ejecuta el proceso completo"""
        
        print(f"🚀 MCP Engine Starting - {project_name}")
        print("=" * 50)
        
        # Determinar tipo de archivo de entrada
        input_path = Path(input_file)
        
        if not input_path.exists():
            print(f"❌ Input file not found: {input_file}")
            return False
        
        # Cargar según extensión
        if input_path.suffix.lower() == '.md':
            success = self.load_mcp(input_file)
        elif input_path.suffix.lower() in ['.json', '.yaml', '.yml']:
            success = self.load_config(input_file)
        else:
            print(f"❌ Unsupported file format: {input_path.suffix}")
            return False
            
        if not success:
            return False
        
        # Validar configuración
        if not self.validate_config():
            return False
        
        # Mostrar resumen
        summary = self.get_config_summary()
        print(f"📊 Configuration Summary:")
        for key, value in summary.items():
            print(f"  - {key}: {value}")
        
        # Generar diagramas
        results = self.generate_diagrams(project_name)
        
        if results:
            print(f"\n🎉 {project_name} diagrams generated successfully!")
            return True
        else:
            print(f"\n❌ Failed to generate {project_name} diagrams")
            return False
