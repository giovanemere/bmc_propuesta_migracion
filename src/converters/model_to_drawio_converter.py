#!/usr/bin/env python3
"""
Model to DrawIO Converter - Convierte JSON/YAML a DrawIO XML
"""

import json
import yaml
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Union

class ModelToDrawIOConverter:
    """Conversor de modelos a DrawIO XML"""
    
    def __init__(self):
        self.aws_shapes = {
            "compute": {
                "fargate": "mxgraph.aws4.fargate",
                "lambda": "mxgraph.aws4.lambda",
                "ec2": "mxgraph.aws4.ec2"
            },
            "database": {
                "rds": "mxgraph.aws4.rds",
                "dynamodb": "mxgraph.aws4.dynamodb",
                "elasticache": "mxgraph.aws4.elasticache"
            },
            "storage": {
                "s3": "mxgraph.aws4.s3",
                "efs": "mxgraph.aws4.efs"
            },
            "network": {
                "api_gateway": "mxgraph.aws4.api_gateway",
                "cloudfront": "mxgraph.aws4.cloudfront",
                "elb": "mxgraph.aws4.elastic_load_balancing"
            },
            "security": {
                "cognito": "mxgraph.aws4.cognito",
                "waf": "mxgraph.aws4.waf",
                "kms": "mxgraph.aws4.kms"
            }
        }
    
    def convert_json_to_drawio(self, json_file: str, output_file: str = None) -> str:
        """Convierte JSON a DrawIO XML"""
        
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return self._convert_model_to_drawio(data, output_file or f"{Path(json_file).stem}.drawio")
    
    def convert_yaml_to_drawio(self, yaml_file: str, output_file: str = None) -> str:
        """Convierte YAML a DrawIO XML"""
        
        with open(yaml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        return self._convert_model_to_drawio(data, output_file or f"{Path(yaml_file).stem}.drawio")
    
    def convert_dict_to_drawio(self, data: Dict[str, Any], output_file: str) -> str:
        """Convierte diccionario Python a DrawIO XML"""
        
        return self._convert_model_to_drawio(data, output_file)
    
    def _convert_model_to_drawio(self, data: Dict[str, Any], output_file: str) -> str:
        """Convierte modelo a DrawIO XML"""
        
        # Crear estructura XML DrawIO
        mxfile = ET.Element("mxfile", host="app.diagrams.net")
        diagram = ET.SubElement(mxfile, "diagram", 
                               name=data.get("title", "Architecture"), 
                               id="model")
        
        canvas = data.get("canvas", {"width": 1600, "height": 900})
        model = ET.SubElement(diagram, "mxGraphModel", 
                             dx=str(canvas["width"]), 
                             dy=str(canvas["height"]), 
                             grid="1", gridSize="10")
        root = ET.SubElement(model, "root")
        
        # Celdas base
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        
        cell_id = 2
        
        # Título
        if "title" in data:
            title = ET.SubElement(root, "mxCell",
                id=str(cell_id),
                value=data["title"],
                style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;fontColor=#FFFFFF;fontSize=18;fontStyle=1;",
                vertex="1", parent="1"
            )
            ET.SubElement(title, "mxGeometry", x="50", y="20", width="1500", height="50", **{"as": "geometry"})
            cell_id += 1
        
        # Procesar componentes
        component_ids = {}
        if "components" in data:
            for component in data["components"]:
                comp_id = self._create_component_from_model(root, component, cell_id, "1")
                component_ids[component.get("id", f"comp_{cell_id}")] = comp_id
                cell_id = comp_id + 1
        
        # Procesar contenedores/clusters
        if "containers" in data:
            for container in data["containers"]:
                container_id = self._create_container_from_model(root, container, cell_id, "1")
                
                # Procesar componentes dentro del contenedor
                if "components" in container:
                    for component in container["components"]:
                        comp_id = self._create_component_from_model(root, component, cell_id + 1, str(container_id))
                        component_ids[component.get("id", f"comp_{cell_id + 1}")] = comp_id
                        cell_id = comp_id + 1
                
                cell_id = container_id + 1
        
        # Procesar conexiones
        if "connections" in data:
            for connection in data["connections"]:
                self._create_connection_from_model(root, connection, component_ids, cell_id)
                cell_id += 1
        
        # Guardar archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if not output_file.endswith('.drawio'):
            output_file += '.drawio'
        
        output_path = Path("outputs/mcp/diagrams") / "converted" / f"{output_file}_{timestamp}"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        ET.indent(mxfile, space="  ")
        xml_str = ET.tostring(mxfile, encoding='unicode', xml_declaration=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_str)
        
        return str(output_path)
    
    def _create_component_from_model(self, root, component: Dict[str, Any], cell_id: int, parent_id: str) -> int:
        """Crea componente desde modelo"""
        
        # Determinar tipo AWS
        comp_type = component.get("type", "generic")
        aws_shape = self._get_aws_shape(comp_type)
        
        # Crear componente
        comp = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value=component.get("label", component.get("name", "Component")),
            style=self._get_component_style(aws_shape),
            vertex="1", parent=parent_id
        )
        
        # Posición y tamaño
        position = component.get("position", {"x": 100, "y": 100})
        size = component.get("size", {"width": 100, "height": 100})
        
        ET.SubElement(comp, "mxGeometry", 
                     x=str(position["x"]), y=str(position["y"]), 
                     width=str(size["width"]), height=str(size["height"]), 
                     **{"as": "geometry"})
        
        return cell_id
    
    def _create_container_from_model(self, root, container: Dict[str, Any], cell_id: int, parent_id: str) -> int:
        """Crea contenedor desde modelo"""
        
        cont = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value=container.get("label", container.get("name", "Container")),
            style="fillColor=#E3F2FD;strokeColor=#1976D2;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#1976D2;whiteSpace=wrap;html=1;fontSize=12;",
            vertex="1", parent=parent_id
        )
        
        # Geometría del contenedor
        geometry = container.get("geometry", {"x": 100, "y": 100, "width": 400, "height": 300})
        ET.SubElement(cont, "mxGeometry", 
                     x=str(geometry["x"]), y=str(geometry["y"]), 
                     width=str(geometry["width"]), height=str(geometry["height"]), 
                     **{"as": "geometry"})
        
        return cell_id
    
    def _create_connection_from_model(self, root, connection: Dict[str, Any], component_ids: Dict[str, int], cell_id: int):
        """Crea conexión desde modelo"""
        
        from_id = component_ids.get(connection.get("from"))
        to_id = component_ids.get(connection.get("to"))
        
        if from_id and to_id:
            style = connection.get("style", {})
            color = style.get("color", "#232F3E")
            width = style.get("width", 2)
            
            edge = ET.SubElement(root, "mxCell",
                id=str(cell_id),
                value=connection.get("label", ""),
                style=f"endArrow=classic;html=1;rounded=0;strokeColor={color};strokeWidth={width};",
                edge="1", parent="1", 
                source=str(from_id), target=str(to_id)
            )
            ET.SubElement(edge, "mxGeometry", width="50", height="50", relative="1", **{"as": "geometry"})
    
    def _get_aws_shape(self, comp_type: str) -> str:
        """Obtiene shape AWS para tipo de componente"""
        
        comp_type_lower = comp_type.lower()
        
        for category, shapes in self.aws_shapes.items():
            if comp_type_lower in shapes:
                return shapes[comp_type_lower]
        
        # Buscar por coincidencia parcial
        for category, shapes in self.aws_shapes.items():
            for shape_name, shape_value in shapes.items():
                if comp_type_lower in shape_name or shape_name in comp_type_lower:
                    return shape_value
        
        return "generic"
    
    def _get_component_style(self, aws_shape: str) -> str:
        """Obtiene estilo para componente"""
        
        if aws_shape.startswith("mxgraph.aws4"):
            return f"sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape={aws_shape};"
        else:
            return "rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;"

# Funciones de utilidad
def convert_file_to_drawio(input_file: str, output_file: str = None) -> str:
    """Convierte archivo JSON/YAML a DrawIO"""
    
    converter = ModelToDrawIOConverter()
    
    if input_file.endswith('.json'):
        return converter.convert_json_to_drawio(input_file, output_file)
    elif input_file.endswith(('.yaml', '.yml')):
        return converter.convert_yaml_to_drawio(input_file, output_file)
    else:
        raise ValueError("Formato de archivo no soportado. Use JSON o YAML.")

def create_sample_model() -> Dict[str, Any]:
    """Crea modelo de ejemplo"""
    
    return {
        "title": "Sample AWS Architecture",
        "canvas": {"width": 1600, "height": 900},
        "containers": [
            {
                "id": "vpc",
                "name": "VPC",
                "label": "VPC 10.0.0.0/16",
                "geometry": {"x": 100, "y": 100, "width": 1200, "height": 600},
                "components": [
                    {
                        "id": "api_gw",
                        "type": "api_gateway",
                        "label": "API Gateway",
                        "position": {"x": 100, "y": 100}
                    },
                    {
                        "id": "fargate",
                        "type": "fargate",
                        "label": "ECS Fargate",
                        "position": {"x": 300, "y": 100}
                    },
                    {
                        "id": "rds",
                        "type": "rds",
                        "label": "RDS PostgreSQL",
                        "position": {"x": 500, "y": 100}
                    }
                ]
            }
        ],
        "connections": [
            {
                "from": "api_gw",
                "to": "fargate",
                "label": "HTTP",
                "style": {"color": "#2196F3", "width": 2}
            },
            {
                "from": "fargate",
                "to": "rds",
                "label": "SQL",
                "style": {"color": "#4CAF50", "width": 2}
            }
        ]
    }
