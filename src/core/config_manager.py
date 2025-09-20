#!/usr/bin/env python3
"""
Config Manager - Gestor de configuración única
Evita duplicación de archivos de configuración
"""

import json
from pathlib import Path
from typing import Dict, Any

class ConfigManager:
    """Gestor de configuración única para BMC"""
    
    def __init__(self):
        self.config_file = Path("docs/specifications/config/bmc-consolidated-config.json")
        self.config = None
    
    def load_config(self) -> Dict[str, Any]:
        """Carga la configuración consolidada única"""
        
        if not self.config_file.exists():
            raise FileNotFoundError(f"Configuración no encontrada: {self.config_file}")
        
        with open(self.config_file, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        
        return self.config
    
    def get_project_info(self) -> Dict[str, str]:
        """Obtiene información del proyecto"""
        if not self.config:
            self.load_config()
        
        return self.config.get("project", {})
    
    def get_workflow_config(self) -> Dict[str, Any]:
        """Obtiene configuración de workflow"""
        if not self.config:
            self.load_config()
        
        return self.config.get("workflow", {})
    
    def get_mcp_server_config(self) -> Dict[str, Any]:
        """Obtiene configuración del servidor MCP"""
        if not self.config:
            self.load_config()
        
        return self.config.get("mcp_server", {})
    
    def validate_single_config(self) -> bool:
        """Valida que solo existe un archivo de configuración"""
        
        config_dir = self.config_file.parent
        config_files = list(config_dir.glob("*.json"))
        
        # Filtrar solo el archivo consolidado
        active_configs = [f for f in config_files if f.name != "bmc-consolidated-config.json"]
        
        if active_configs:
            print(f"⚠️ Archivos de configuración adicionales encontrados:")
            for config in active_configs:
                print(f"  - {config}")
            return False
        
        return True
    
    def get_config_summary(self) -> Dict[str, Any]:
        """Obtiene resumen de configuración"""
        if not self.config:
            self.load_config()
        
        metadata = self.config.get("metadata", {})
        project = self.config.get("project", {})
        
        return {
            "version": metadata.get("version", "unknown"),
            "project_name": project.get("name", "unknown"),
            "consolidated_date": metadata.get("consolidated_date", "unknown"),
            "source_files_count": len(metadata.get("source_files", [])),
            "single_config": self.validate_single_config()
        }
