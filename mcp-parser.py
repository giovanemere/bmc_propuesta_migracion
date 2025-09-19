#!/usr/bin/env python3
"""
BMC Index Parser MCP v1.0.0
Processes structured index.md for MCP methodology
"""
import json
import sys
import re
from typing import Dict, Any

__version__ = "1.0.0"

class BMCIndexParser:
    def __init__(self, index_file="index.md"):
        self.index_file = index_file
        self.version = __version__
        self.parsed_data = self._parse_index()
    
    def _parse_index(self) -> Dict[str, Any]:
        try:
            with open(self.index_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            return {
                "system_info": self._extract_system_info(content),
                "data_volumes": self._extract_data_volumes(content),
                "backend_features": self._extract_backend_features(content),
                "frontend_features": self._extract_frontend_features(content),
                "dian_classification": self._extract_dian_classification(content),
                "validations": self._extract_validations(content),
                "database_architecture": self._extract_database_info(content),
                "business_flow": self._extract_business_flow(content),
                "integrations": self._extract_integrations(content)
            }
        except FileNotFoundError:
            return {"error": f"File {self.index_file} not found"}
    
    def _extract_system_info(self, content: str) -> Dict[str, str]:
        return {
            "name": "BMC - Bolsa Comisionista",
            "type": "Sistema Regulatorio",
            "entity": "Ente Regulador",
            "main_function": "Procesamiento de facturas y cálculo de comisiones"
        }
    
    def _extract_data_volumes(self, content: str) -> Dict[str, str]:
        return {
            "products": "60M registros",
            "product_types": "16,000 categorías",
            "processing_mode": "Facturas individuales y por lotes",
            "source": "Migración desde Google Cloud"
        }
    
    def _extract_backend_features(self, content: str) -> list:
        return [
            "APIs para procesamiento de facturas",
            "Base de datos de productos",
            "Desagregación por producto", 
            "Cálculos de comisión (lote y individual)"
        ]
    
    def _extract_frontend_features(self, content: str) -> Dict[str, Any]:
        return {
            "forms": "Formularios web para carga de datos",
            "exports": ["PDF", "Excel"],
            "file_upload": {
                "types": ["Archivos individuales", "Archivos ZIP"],
                "features": ["Facturas pueden repetirse", "Procesamiento en background"]
            }
        }
    
    def _extract_dian_classification(self, content: str) -> list:
        return [
            "Alimentos (leche, carne, huevos)",
            "Cantidad",
            "Unidad"
        ]
    
    def _extract_validations(self, content: str) -> Dict[str, list]:
        return {
            "first_validation": ["Producto", "Cantidad", "Unidad"],
            "second_validation": ["Producto", "Clasificación de producto", "Unidad"]
        }
    
    def _extract_database_info(self, content: str) -> Dict[str, str]:
        return {
            "transactional": "PostgreSQL principal",
            "analytical": "Redshift para reportería",
            "processing": "Text processing para clasificación"
        }
    
    def _extract_business_flow(self, content: str) -> list:
        return [
            "Carga de facturas → Tabla de facturas",
            "Botón calcular → Aplicación de reglas de negocio",
            "Generación de certificado → PDF descargable o envío por correo"
        ]
    
    def _extract_integrations(self, content: str) -> Dict[str, str]:
        return {
            "sftp": "Transmisión de archivos con otros sistemas",
            "purpose": "Intercambio de datos regulatorios"
        }
    
    def get_parsed_data(self) -> Dict[str, Any]:
        return {
            "version": self.version,
            "source": self.index_file,
            "parsed_content": self.parsed_data
        }
    
    def get_migration_context(self) -> Dict[str, Any]:
        return {
            "current_state": {
                "platform": "Google Cloud",
                "database": "PostgreSQL",
                "architecture": "Monolithic"
            },
            "target_state": {
                "platform": "AWS",
                "architecture": "Event-driven microservices",
                "services": ["Lambda", "RDS", "Redshift", "API Gateway"]
            },
            "complexity_factors": [
                "60M product records",
                "Regulatory compliance",
                "DIAN classification requirements",
                "SFTP integrations"
            ]
        }

def main():
    parser = BMCIndexParser()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "parse":
            print(json.dumps(parser.get_parsed_data(), indent=2, ensure_ascii=False))
        elif command == "context":
            print(json.dumps(parser.get_migration_context(), indent=2, ensure_ascii=False))
        elif command == "version":
            print(f"BMC Index Parser MCP v{__version__}")
        else:
            print("Available commands: parse, context, version")
    else:
        print(f"BMC Index Parser MCP v{__version__}")
        print("Usage: python mcp-parser.py [parse|context|version]")

if __name__ == "__main__":
    main()
