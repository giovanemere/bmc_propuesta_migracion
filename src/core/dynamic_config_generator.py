#!/usr/bin/env python3
"""
Dynamic Config Generator - Genera configuración dinámicamente desde especificación
"""

import re
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any
from .app_config import save_config, get_paths

class DynamicConfigGenerator:
    """Generador dinámico de configuración desde especificación Markdown"""
    
    def __init__(self):
        self.paths = get_paths()
    
    def generate_config_from_specification(self, spec_file: str = None) -> Dict[str, Any]:
        """Genera configuración dinámicamente desde especificación"""
        
        if spec_file is None:
            spec_file = self.paths.config_dir / "bmc-input-specification.md"
        
        spec_path = Path(spec_file)
        
        if not spec_path.exists():
            raise FileNotFoundError(f"Especificación no encontrada: {spec_file}")
        
        print(f"📋 Generando configuración desde: {spec_path.name}")
        
        # Leer especificación
        with open(spec_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extraer información
        config = self._parse_specification(content)
        
        # Guardar configuración generada
        config_path = save_config("bmc", config)
        print(f"✅ Configuración generada: {Path(config_path).name}")
        
        return config
    
    def _parse_specification(self, content: str) -> Dict[str, Any]:
        """Parsea especificación Markdown y extrae configuración"""
        
        config = {
            "project_name": "bmc_input",
            "microservices": {},
            "aws_services": {},
            "metadata": {
                "generated_from": "bmc-input-specification.md",
                "generated_at": datetime.now().isoformat(),
                "version": "dynamic-1.0.0"
            }
        }
        
        # Extraer microservicios
        microservices = self._extract_microservices(content)
        config["microservices"].update(microservices)
        
        # Extraer servicios AWS (inferidos)
        aws_services = self._infer_aws_services(content)
        config["aws_services"].update(aws_services)
        
        return config
    
    def _extract_microservices(self, content: str) -> Dict[str, Any]:
        """Extrae microservicios desde especificación"""
        
        microservices = {}
        
        # Buscar secciones de servicios
        service_patterns = [
            (r'####\s*Invoice Service\s*\n(.*?)(?=####|\n##|\Z)', "invoice_service"),
            (r'####\s*Product Service\s*\n(.*?)(?=####|\n##|\Z)', "product_service"),
            (r'####\s*OCR Service\s*\n(.*?)(?=####|\n##|\Z)', "ocr_service"),
            (r'####\s*Commission Service\s*\n(.*?)(?=####|\n##|\Z)', "commission_service"),
            (r'####\s*Certificate Service\s*\n(.*?)(?=####|\n##|\Z)', "certificate_service")
        ]
        
        for pattern, service_id in service_patterns:
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            if match:
                service_content = match.group(1).strip()
                lines = service_content.split('\n')
                business_function = lines[0].strip('- ').strip() if lines else f"{service_id.replace('_', ' ').title()}"
                
                microservices[service_id] = {
                    "business_function": business_function
                }
        
        return microservices
    
    def _infer_aws_services(self, content: str) -> Dict[str, Any]:
        """Infiere servicios AWS necesarios"""
        
        aws_services = {}
        
        # RDS - si hay base de datos mencionada
        if re.search(r'productos|facturas|base.*datos', content, re.IGNORECASE):
            aws_services["rds"] = {
                "engine": "postgresql",
                "instance_class": "db.r5.2xlarge"
            }
        
        # S3 - para almacenamiento
        if re.search(r'certificados|pdf|documentos', content, re.IGNORECASE):
            aws_services["s3"] = {
                "storage_class": "STANDARD",
                "versioning": True
            }
        
        return aws_services
    
    def is_specification_newer(self, spec_file: str = None) -> bool:
        """Verifica si la especificación es más nueva que la configuración"""
        
        if spec_file is None:
            spec_file = self.paths.config_dir / "bmc-input-specification.md"
        
        spec_path = Path(spec_file)
        # Configuración siempre en outputs/generated
        config_path = self.paths.outputs_generated_dir / "bmc.json"
        
        if not spec_path.exists():
            return False
        
        if not config_path.exists():
            return True  # No hay config, generar
        
        # Comparar fechas de modificación
        spec_mtime = spec_path.stat().st_mtime
        config_mtime = config_path.stat().st_mtime
        
        return spec_mtime > config_mtime

def generate_dynamic_config(force_regenerate: bool = False) -> Dict[str, Any]:
    """Función de conveniencia para generar configuración dinámica"""
    
    generator = DynamicConfigGenerator()
    
    # Verificar si necesita regenerar
    if not force_regenerate and not generator.is_specification_newer():
        print("⚠️ Especificación no ha cambiado, usando configuración existente")
        from .app_config import get_config
        return get_config("bmc")
    
    # Generar nueva configuración
    print("🔄 Especificación actualizada, regenerando configuración...")
    return generator.generate_config_from_specification()
