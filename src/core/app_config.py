#!/usr/bin/env python3
"""
App Config - Configuración transversal de la aplicación
"""

import os
import json
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class AppPaths:
    """Rutas de la aplicación"""
    
    # Directorio raíz del proyecto
    root_dir: Path
    
    # Directorios principales
    src_dir: Path
    config_dir: Path
    outputs_dir: Path
    schemas_dir: Path
    templates_dir: Path
    docs_dir: Path
    tests_dir: Path
    
    # Subdirectorios de outputs
    outputs_png_dir: Path
    outputs_drawio_dir: Path
    outputs_mermaid_dir: Path
    outputs_prompts_dir: Path
    outputs_docs_dir: Path
    outputs_generated_dir: Path
    
    @classmethod
    def from_root(cls, root_path: str = None) -> 'AppPaths':
        """Crea paths desde directorio raíz"""
        
        if root_path is None:
            # Detectar automáticamente el directorio raíz
            current = Path(__file__).parent
            while current.parent != current:
                if (current / "src").exists() and (current / "config").exists():
                    root_path = current
                    break
                current = current.parent
            else:
                root_path = Path.cwd()
        
        root = Path(root_path)
        
        # Crear directorios si no existen
        outputs_dir = root / "outputs"
        outputs_dir.mkdir(exist_ok=True)
        
        # Subdirectorios de outputs
        outputs_png = outputs_dir / "png"
        outputs_drawio = outputs_dir / "drawio"
        outputs_mermaid = outputs_dir / "mermaid"
        outputs_prompts = outputs_dir / "prompts"
        outputs_docs = outputs_dir / "documentation"
        outputs_generated = outputs_dir / "generated"
        
        # Crear subdirectorios
        for subdir in [outputs_png, outputs_drawio, outputs_mermaid, outputs_prompts, outputs_docs, outputs_generated]:
            subdir.mkdir(exist_ok=True)
        
        return cls(
            root_dir=root,
            src_dir=root / "src",
            config_dir=root / "config",
            outputs_dir=outputs_dir,
            schemas_dir=root / "schemas",
            templates_dir=root / "templates",
            docs_dir=root / "docs",
            tests_dir=root / "tests",
            outputs_png_dir=outputs_png,
            outputs_drawio_dir=outputs_drawio,
            outputs_mermaid_dir=outputs_mermaid,
            outputs_prompts_dir=outputs_prompts,
            outputs_docs_dir=outputs_docs,
            outputs_generated_dir=outputs_generated
        )

class AppConfig:
    """Configuración transversal de la aplicación"""
    
    def __init__(self, root_path: str = None):
        self.paths = AppPaths.from_root(root_path)
        self._config_cache = {}
        
        # Variables de entorno
        self.env = {
            "DEBUG": os.getenv("DEBUG", "false").lower() == "true",
            "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
            "OUTPUT_FORMAT": os.getenv("OUTPUT_FORMAT", "both"),  # png, drawio, both
            "AWS_REGION": os.getenv("AWS_REGION", "us-east-1"),
            "PROJECT_NAME": os.getenv("PROJECT_NAME", "mcp_diagrams")
        }
    
    def load_config(self, config_name: str) -> Dict[str, Any]:
        """Carga configuración por nombre"""
        
        if config_name in self._config_cache:
            return self._config_cache[config_name]
        
        # Para configuración BMC, usar generador dinámico
        if config_name == "bmc":
            try:
                from .dynamic_config_generator import generate_dynamic_config
                config = generate_dynamic_config()
                self._config_cache[config_name] = config
                return config
            except Exception as e:
                print(f"⚠️ Error generando configuración dinámica: {e}")
                # Fallback a configuración por defecto
                pass
        
        # Buscar archivo de configuración
        config_paths = [
            self.paths.config_dir / f"{config_name}.json",
            self.paths.config_dir / f"{config_name}-config.json",
            self.paths.schemas_dir / f"{config_name}.json",
            self.paths.outputs_generated_dir / f"{config_name}.json"
        ]
        
        for config_path in config_paths:
            if config_path.exists():
                try:
                    with open(config_path, 'r', encoding='utf-8') as f:
                        config = json.load(f)
                    self._config_cache[config_name] = config
                    return config
                except Exception as e:
                    print(f"⚠️ Error cargando {config_path}: {e}")
        
        # Configuración por defecto
        default_config = self._get_default_config(config_name)
        self._config_cache[config_name] = default_config
        return default_config
    
    def save_config(self, config_name: str, config_data: Dict[str, Any], 
                   location: str = "generated") -> str:
        """Guarda configuración en ubicación especificada"""
        
        if location == "generated":
            config_path = self.paths.outputs_generated_dir / f"{config_name}.json"
        elif location == "config":
            config_path = self.paths.config_dir / f"{config_name}.json"
        else:
            config_path = Path(location) / f"{config_name}.json"
        
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config_data, f, indent=2, ensure_ascii=False)
        
        # Actualizar cache
        self._config_cache[config_name] = config_data
        
        return str(config_path)
    
    def get_output_path(self, file_type: str, filename: str, 
                       project_name: str = None) -> Path:
        """Obtiene ruta de salida para tipo de archivo"""
        
        if project_name is None:
            project_name = self.env["PROJECT_NAME"]
        
        # Mapeo de tipos a directorios
        type_mapping = {
            "png": self.paths.outputs_png_dir,
            "drawio": self.paths.outputs_drawio_dir,
            "mermaid": self.paths.outputs_mermaid_dir,
            "prompts": self.paths.outputs_prompts_dir,
            "documentation": self.paths.outputs_docs_dir,
            "generated": self.paths.outputs_generated_dir
        }
        
        base_dir = type_mapping.get(file_type, self.paths.outputs_dir)
        
        # Crear subdirectorio por proyecto
        project_dir = base_dir / project_name
        project_dir.mkdir(exist_ok=True)
        
        return project_dir / filename
    
    def _get_default_config(self, config_name: str) -> Dict[str, Any]:
        """Configuraciones por defecto"""
        
        defaults = {
            "bmc": {
                "project_name": "bmc_input",
                "microservices": {
                    "certificate_service": {
                        "business_function": "Generación de certificados PDF DIAN compliance"
                    },
                    "invoice_service": {
                        "business_function": "Procesamiento de facturas individuales y por lotes"
                    },
                    "product_service": {
                        "business_function": "Gestión de 60M productos migrados desde Google Cloud"
                    },
                    "ocr_service": {
                        "business_function": "Análisis de facturas PDF/imagen con 95% precisión"
                    },
                    "commission_service": {
                        "business_function": "Cálculos de comisión regulatoria DIAN compliance"
                    }
                },
                "aws_services": {
                    "rds": {"engine": "postgresql", "instance_class": "db.r5.2xlarge"},
                    "s3": {"storage_class": "STANDARD", "versioning": True},
                    "elasticache": {"engine": "redis", "node_type": "cache.r6g.large"}
                }
            },
            "standard_model": {
                "metadata": {
                    "version": "1.0.0",
                    "diagram_type": "network"
                },
                "canvas": {
                    "width": 2500,
                    "height": 1600,
                    "grid_size": 10
                }
            },
            "app": {
                "version": "4.1.0",
                "name": "MCP Diagram Generator",
                "supported_formats": ["png", "drawio", "mermaid"],
                "default_theme": "aws"
            }
        }
        
        return defaults.get(config_name, {})

# Instancia global de configuración
app_config = AppConfig()

# Funciones de conveniencia
def get_config(config_name: str) -> Dict[str, Any]:
    """Obtiene configuración por nombre"""
    return app_config.load_config(config_name)

def save_config(config_name: str, config_data: Dict[str, Any]) -> str:
    """Guarda configuración en outputs/generated"""
    return app_config.save_config(config_name, config_data)

def get_output_path(file_type: str, filename: str, project_name: str = None) -> Path:
    """Obtiene ruta de salida"""
    return app_config.get_output_path(file_type, filename, project_name)

def get_paths() -> AppPaths:
    """Obtiene paths de la aplicación"""
    return app_config.paths
