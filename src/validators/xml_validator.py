#!/usr/bin/env python3
"""
XML Validator - Validación de XML DrawIO y integración con MCP
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
import json
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional
import re

class DrawIOXMLValidator:
    """Validador de XML DrawIO"""
    
    def __init__(self):
        self.required_elements = ["mxfile", "diagram", "mxGraphModel", "root"]
        self.aws_shape_pattern = re.compile(r'mxgraph\.aws4\.[a-zA-Z_]+')
        
    def validate_xml_structure(self, xml_content: str) -> Tuple[bool, List[str]]:
        """Valida estructura básica del XML DrawIO"""
        
        errors = []
        
        try:
            # Parsear XML
            root = ET.fromstring(xml_content)
            
            # Verificar elemento raíz
            if root.tag != "mxfile":
                errors.append("Elemento raíz debe ser 'mxfile'")
            
            # Verificar elementos requeridos
            diagram = root.find("diagram")
            if diagram is None:
                errors.append("Elemento 'diagram' no encontrado")
                return False, errors
            
            model = diagram.find("mxGraphModel")
            if model is None:
                errors.append("Elemento 'mxGraphModel' no encontrado")
                return False, errors
            
            model_root = model.find("root")
            if model_root is None:
                errors.append("Elemento 'root' no encontrado")
                return False, errors
            
            # Verificar celdas base
            cells = model_root.findall("mxCell")
            if len(cells) < 2:
                errors.append("Debe tener al menos 2 celdas base (id='0' y id='1')")
            
            # Verificar IDs únicos
            ids = set()
            for cell in cells:
                cell_id = cell.get("id")
                if cell_id in ids:
                    errors.append(f"ID duplicado: {cell_id}")
                ids.add(cell_id)
            
        except ET.ParseError as e:
            errors.append(f"XML malformado: {str(e)}")
            return False, errors
        except Exception as e:
            errors.append(f"Error inesperado: {str(e)}")
            return False, errors
        
        return len(errors) == 0, errors
    
    def validate_aws_components(self, xml_content: str) -> Tuple[bool, Dict[str, Any]]:
        """Valida componentes AWS en el XML"""
        
        try:
            root = ET.fromstring(xml_content)
            
            # Buscar componentes AWS
            aws_components = []
            generic_components = []
            connections = []
            
            for cell in root.findall(".//mxCell"):
                style = cell.get("style", "")
                
                # Componente AWS
                if "mxgraph.aws4" in style:
                    aws_match = self.aws_shape_pattern.search(style)
                    if aws_match:
                        aws_components.append({
                            "id": cell.get("id"),
                            "shape": aws_match.group(),
                            "label": cell.get("value", "")
                        })
                
                # Componente genérico
                elif cell.get("vertex") == "1":
                    generic_components.append({
                        "id": cell.get("id"),
                        "label": cell.get("value", ""),
                        "style": style
                    })
                
                # Conexión
                elif cell.get("edge") == "1":
                    connections.append({
                        "id": cell.get("id"),
                        "source": cell.get("source"),
                        "target": cell.get("target"),
                        "label": cell.get("value", "")
                    })
            
            analysis = {
                "aws_components": len(aws_components),
                "generic_components": len(generic_components),
                "connections": len(connections),
                "total_elements": len(aws_components) + len(generic_components),
                "aws_shapes": [comp["shape"] for comp in aws_components],
                "component_details": aws_components,
                "connection_details": connections
            }
            
            # Validaciones
            is_valid = True
            if len(aws_components) == 0:
                is_valid = False
                analysis["warning"] = "No se encontraron componentes AWS"
            
            return is_valid, analysis
            
        except Exception as e:
            return False, {"error": str(e)}
    
    def validate_diagram_completeness(self, xml_content: str, expected_components: List[str]) -> Tuple[bool, Dict[str, Any]]:
        """Valida completitud del diagrama vs componentes esperados"""
        
        try:
            _, analysis = self.validate_aws_components(xml_content)
            
            if "error" in analysis:
                return False, analysis
            
            # Extraer tipos de componentes encontrados
            found_shapes = set()
            for comp in analysis["component_details"]:
                shape_name = comp["shape"].replace("mxgraph.aws4.", "")
                found_shapes.add(shape_name)
            
            # Comparar con esperados
            expected_set = set(expected_components)
            missing = expected_set - found_shapes
            extra = found_shapes - expected_set
            
            completeness = {
                "expected": len(expected_components),
                "found": len(found_shapes),
                "missing": list(missing),
                "extra": list(extra),
                "completeness_percentage": (len(found_shapes & expected_set) / len(expected_set)) * 100 if expected_components else 100
            }
            
            analysis["completeness"] = completeness
            
            return len(missing) == 0, analysis
            
        except Exception as e:
            return False, {"error": str(e)}
    
    def format_xml(self, xml_content: str) -> str:
        """Formatea XML para mejor legibilidad"""
        
        try:
            # Parsear y reformatear
            dom = minidom.parseString(xml_content)
            formatted = dom.toprettyxml(indent="  ")
            
            # Limpiar líneas vacías extra
            lines = [line for line in formatted.split('\n') if line.strip()]
            return '\n'.join(lines)
            
        except Exception:
            return xml_content  # Retornar original si falla el formateo

class MCPIntegrator:
    """Integrador con el modelo MCP existente"""
    
    def __init__(self, mcp_config_path: str = None):
        if mcp_config_path is None:
            from core.app_config import get_config
            self.mcp_config = get_config("bmc")
            self.mcp_config_path = None
        else:
            self.mcp_config_path = Path(mcp_config_path)
            self.mcp_config = None
        self.validator = DrawIOXMLValidator()
    
    def load_mcp_config(self) -> Dict[str, Any]:
        """Carga configuración MCP existente"""
        
        if self.mcp_config is not None:
            return self.mcp_config
        
        try:
            if self.mcp_config_path and self.mcp_config_path.exists():
                with open(self.mcp_config_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return self._get_default_mcp_config()
        except json.JSONDecodeError as e:
            raise ValueError(f"Error en configuración MCP: {e}")
    
    def convert_mcp_to_standard_model(self, mcp_config: Dict[str, Any]) -> Dict[str, Any]:
        """Convierte configuración MCP al modelo estándar"""
        
        # Extraer información del MCP
        project_name = mcp_config.get("project_name", "mcp_project")
        microservices = mcp_config.get("microservices", {})
        aws_services = mcp_config.get("aws_services", {})
        
        # Crear modelo estándar
        standard_model = {
            "metadata": {
                "title": f"{project_name.upper()} - Architecture",
                "project_name": project_name,
                "diagram_type": "network",
                "version": "1.0.0",
                "description": f"Arquitectura generada desde MCP para {project_name}",
                "tags": ["mcp", "aws", "auto-generated"]
            },
            "canvas": {
                "width": 2500,
                "height": 1600,
                "grid_size": 10,
                "background": "white"
            },
            "architecture": {
                "components": [],
                "containers": [],
                "connections": []
            },
            "output": {
                "formats": ["png", "drawio"],
                "auto_layout": True,
                "theme": "aws"
            }
        }
        
        # Convertir microservicios a componentes
        x_pos = 200
        for service_name, service_config in microservices.items():
            component = {
                "id": service_name,
                "type": "fargate",
                "label": f"{service_name.replace('_', ' ').title()}\\n{service_config.get('business_function', 'Microservice')}",
                "position": {"x": x_pos, "y": 300},
                "size": {"width": 120, "height": 100},
                "properties": {
                    "business_function": service_config.get("business_function", ""),
                    "technology": service_config.get("technology", ""),
                    "replicas": service_config.get("replicas", 1)
                }
            }
            standard_model["architecture"]["components"].append(component)
            x_pos += 200
        
        # Convertir servicios AWS a componentes
        y_pos = 500
        for service_name, service_config in aws_services.items():
            component = {
                "id": service_name,
                "type": service_name.lower(),
                "label": f"{service_name.upper()}\\n{service_config.get('description', '')}",
                "position": {"x": 200, "y": y_pos},
                "size": {"width": 100, "height": 80},
                "properties": service_config
            }
            standard_model["architecture"]["components"].append(component)
            y_pos += 120
        
        # Crear conexiones básicas entre microservicios y servicios
        connections = []
        microservice_ids = list(microservices.keys())
        service_ids = list(aws_services.keys())
        
        # Conectar microservicios con bases de datos
        for i, ms_id in enumerate(microservice_ids):
            if "rds" in service_ids:
                connections.append({
                    "id": f"conn_{ms_id}_rds",
                    "from": ms_id,
                    "to": "rds",
                    "label": "Database Access",
                    "type": "sql"
                })
        
        standard_model["architecture"]["connections"] = connections
        
        return standard_model
    
    def validate_mcp_generated_xml(self, xml_content: str, mcp_config: Dict[str, Any]) -> Dict[str, Any]:
        """Valida XML generado desde MCP"""
        
        # Validación estructural
        is_valid_structure, structure_errors = self.validator.validate_xml_structure(xml_content)
        
        # Validación de componentes AWS
        is_valid_aws, aws_analysis = self.validator.validate_aws_components(xml_content)
        
        # Extraer componentes esperados del MCP
        expected_components = []
        microservices = mcp_config.get("microservices", {})
        aws_services = mcp_config.get("aws_services", {})
        
        # Agregar tipos esperados
        if microservices:
            expected_components.append("fargate")  # Microservicios como Fargate
        
        for service_name in aws_services.keys():
            expected_components.append(service_name.lower())
        
        # Validación de completitud
        is_complete, completeness_analysis = self.validator.validate_diagram_completeness(
            xml_content, expected_components
        )
        
        return {
            "overall_valid": is_valid_structure and is_valid_aws,
            "structure": {
                "valid": is_valid_structure,
                "errors": structure_errors
            },
            "aws_components": aws_analysis,
            "completeness": completeness_analysis.get("completeness", {}),
            "mcp_integration": {
                "expected_microservices": len(microservices),
                "expected_aws_services": len(aws_services),
                "total_expected": len(expected_components)
            }
        }
    
    def _get_default_mcp_config(self) -> Dict[str, Any]:
        """Configuración MCP por defecto"""
        
        return {
            "project_name": "default_project",
            "microservices": {
                "api_service": {
                    "business_function": "API Gateway Service",
                    "technology": "Node.js"
                }
            },
            "aws_services": {
                "rds": {
                    "engine": "postgresql",
                    "instance_class": "db.t3.micro"
                },
                "s3": {
                    "storage_class": "STANDARD"
                }
            }
        }

# Funciones de utilidad
def validate_drawio_file(file_path: str, mcp_config_path: str = None) -> Dict[str, Any]:
    """Valida archivo DrawIO completo"""
    
    validator = DrawIOXMLValidator()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        # Validación básica
        is_valid, errors = validator.validate_xml_structure(xml_content)
        
        if not is_valid:
            return {
                "valid": False,
                "errors": errors,
                "file": file_path
            }
        
        # Validación AWS
        _, aws_analysis = validator.validate_aws_components(xml_content)
        
        result = {
            "valid": True,
            "file": file_path,
            "analysis": aws_analysis
        }
        
        # Integración MCP si se proporciona config
        if mcp_config_path:
            integrator = MCPIntegrator(mcp_config_path)
            mcp_config = integrator.load_mcp_config()
            mcp_validation = integrator.validate_mcp_generated_xml(xml_content, mcp_config)
            result["mcp_integration"] = mcp_validation
        
        return result
        
    except Exception as e:
        return {
            "valid": False,
            "errors": [str(e)],
            "file": file_path
        }

def format_drawio_file(input_path: str, output_path: str = None) -> str:
    """Formatea archivo DrawIO para mejor legibilidad"""
    
    validator = DrawIOXMLValidator()
    
    with open(input_path, 'r', encoding='utf-8') as f:
        xml_content = f.read()
    
    formatted_xml = validator.format_xml(xml_content)
    
    if output_path is None:
        output_path = input_path.replace('.drawio', '_formatted.drawio')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(formatted_xml)
    
    return output_path
