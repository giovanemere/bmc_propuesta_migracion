#!/usr/bin/env python3
"""
MCP Parser - Módulo transversal para parsear archivos MCP
Extrae configuración de arquitectura desde archivos MCP
"""

import re
import yaml
import json
from pathlib import Path
from typing import Dict, List, Any

class MCPParser:
    """Parser genérico para archivos MCP"""
    
    def __init__(self, mcp_file: str):
        self.mcp_file = Path(mcp_file)
        self.content = ""
        self.config = {}
        
    def load(self) -> bool:
        """Carga el archivo MCP"""
        if not self.mcp_file.exists():
            print(f"❌ MCP file not found: {self.mcp_file}")
            return False
            
        with open(self.mcp_file, 'r', encoding='utf-8') as f:
            self.content = f.read()
            
        print(f"✓ MCP loaded: {self.mcp_file}")
        return True
    
    def extract_yaml_blocks(self) -> Dict[str, Any]:
        """Extrae bloques YAML del MCP"""
        yaml_blocks = {}
        
        # Buscar bloques ```yaml
        pattern = r'```yaml\n(.*?)\n```'
        matches = re.findall(pattern, self.content, re.DOTALL)
        
        for i, match in enumerate(matches):
            try:
                yaml_data = yaml.safe_load(match)
                yaml_blocks[f"block_{i}"] = yaml_data
            except yaml.YAMLError as e:
                print(f"⚠️ YAML parse error in block {i}: {e}")
                
        return yaml_blocks
    
    def extract_services(self) -> Dict[str, Any]:
        """Extrae configuración de servicios AWS"""
        yaml_blocks = self.extract_yaml_blocks()
        services = {}
        
        for block_name, block_data in yaml_blocks.items():
            if isinstance(block_data, dict):
                # Buscar servicios AWS
                for key, value in block_data.items():
                    if any(aws_service in key.lower() for aws_service in 
                          ['ecs', 'rds', 'lambda', 's3', 'api', 'cognito', 'textract']):
                        services[key] = value
                        
        return services
    
    def extract_microservices(self) -> Dict[str, Any]:
        """Extrae configuración de microservicios"""
        yaml_blocks = self.extract_yaml_blocks()
        
        for block_data in yaml_blocks.values():
            if isinstance(block_data, dict) and 'microservices' in str(block_data).lower():
                return block_data
                
        return {}
    
    def extract_metrics(self) -> Dict[str, Any]:
        """Extrae métricas y KPIs"""
        metrics = {}
        
        # Buscar secciones de métricas
        patterns = [
            r'Performance Targets[:\n](.*?)(?=\n##|\n###|\Z)',
            r'Métricas y KPIs[:\n](.*?)(?=\n##|\n###|\Z)',
            r'KPIs[:\n](.*?)(?=\n##|\n###|\Z)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, self.content, re.DOTALL | re.IGNORECASE)
            for match in matches:
                # Extraer valores numéricos
                numbers = re.findall(r'(\d+(?:\.\d+)?)\s*([a-zA-Z/%]+)', match)
                for value, unit in numbers:
                    metrics[f"metric_{len(metrics)}"] = {"value": value, "unit": unit}
                    
        return metrics
    
    def parse(self) -> Dict[str, Any]:
        """Parsea completamente el MCP"""
        if not self.load():
            return {}
            
        self.config = {
            "services": self.extract_services(),
            "microservices": self.extract_microservices(),
            "metrics": self.extract_metrics(),
            "yaml_blocks": self.extract_yaml_blocks()
        }
        
        return self.config
    
    def get_config(self) -> Dict[str, Any]:
        """Retorna la configuración parseada"""
        return self.config
