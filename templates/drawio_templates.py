#!/usr/bin/env python3
"""
DrawIO Templates - Plantillas XML base para diferentes tipos de diagramas
"""

from string import Template
from typing import Dict, Any, List
from datetime import datetime

class DrawIOTemplates:
    """Plantillas XML para DrawIO"""
    
    # Template base para archivo DrawIO
    BASE_TEMPLATE = Template('''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="${timestamp}" agent="MCP-Generator" version="1.0.0">
  <diagram name="${diagram_name}" id="${diagram_id}">
    <mxGraphModel dx="${canvas_width}" dy="${canvas_height}" grid="1" gridSize="${grid_size}" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="${canvas_width}" pageHeight="${canvas_height}" background="${background}">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        ${title_cell}
        ${content}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>''')
    
    # Template para título
    TITLE_TEMPLATE = Template('''<mxCell id="title" value="${title}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;fontColor=#FFFFFF;fontSize=18;fontStyle=1;align=center;verticalAlign=middle;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="${title_width}" height="60" as="geometry"/>
        </mxCell>''')
    
    # Template para componente AWS
    AWS_COMPONENT_TEMPLATE = Template('''<mxCell id="${id}" value="${label}" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=${gradient_color};gradientDirection=north;fillColor=${fill_color};strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=${font_size};fontStyle=0;aspect=fixed;shape=${shape};" vertex="1" parent="${parent}">
          <mxGeometry x="${x}" y="${y}" width="${width}" height="${height}" as="geometry"/>
        </mxCell>''')
    
    # Template para contenedor
    CONTAINER_TEMPLATE = Template('''<mxCell id="${id}" value="${label}" style="fillColor=${fill_color};strokeColor=${stroke_color};strokeWidth=${stroke_width};dashed=1;verticalAlign=top;fontStyle=1;fontColor=${font_color};whiteSpace=wrap;html=1;fontSize=${font_size};" vertex="1" parent="${parent}">
          <mxGeometry x="${x}" y="${y}" width="${width}" height="${height}" as="geometry"/>
        </mxCell>''')
    
    # Template para conexión
    CONNECTION_TEMPLATE = Template('''<mxCell id="${id}" value="${label}" style="endArrow=classic;html=1;rounded=0;strokeColor=${color};strokeWidth=${width};fontColor=#232F3E;fontSize=10;" edge="1" parent="1" source="${source}" target="${target}">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="${source_x}" y="${source_y}" as="sourcePoint"/>
            <mxPoint x="${target_x}" y="${target_y}" as="targetPoint"/>
          </mxGeometry>
        </mxCell>''')
    
    # Estilos predefinidos por tipo de componente
    COMPONENT_STYLES = {
        # Compute
        "fargate": {
            "gradient_color": "#F78E04",
            "fill_color": "#D05C17",
            "shape": "mxgraph.aws4.fargate"
        },
        "lambda": {
            "gradient_color": "#F78E04", 
            "fill_color": "#D05C17",
            "shape": "mxgraph.aws4.lambda"
        },
        "ec2": {
            "gradient_color": "#F78E04",
            "fill_color": "#D05C17", 
            "shape": "mxgraph.aws4.ec2"
        },
        
        # Database
        "rds": {
            "gradient_color": "#4AB29A",
            "fill_color": "#116D5B",
            "shape": "mxgraph.aws4.rds"
        },
        "dynamodb": {
            "gradient_color": "#4AB29A",
            "fill_color": "#116D5B",
            "shape": "mxgraph.aws4.dynamodb"
        },
        
        # Storage
        "s3": {
            "gradient_color": "#60A337",
            "fill_color": "#277116",
            "shape": "mxgraph.aws4.s3"
        },
        
        # Network
        "api_gateway": {
            "gradient_color": "#945DF2",
            "fill_color": "#5A30B5",
            "shape": "mxgraph.aws4.api_gateway"
        },
        "elb": {
            "gradient_color": "#8C4FFF",
            "fill_color": "#5A30B5",
            "shape": "mxgraph.aws4.elastic_load_balancing"
        },
        "cloudfront": {
            "gradient_color": "#945DF2",
            "fill_color": "#5A30B5",
            "shape": "mxgraph.aws4.cloudfront"
        },
        "internet_gateway": {
            "gradient_color": "#1976D2",
            "fill_color": "#0D47A1",
            "shape": "mxgraph.aws4.internet_gateway"
        },
        
        # Security
        "waf": {
            "gradient_color": "#F54749",
            "fill_color": "#C7131F",
            "shape": "mxgraph.aws4.waf"
        },
        "cognito": {
            "gradient_color": "#F54749",
            "fill_color": "#C7131F",
            "shape": "mxgraph.aws4.cognito"
        },
        
        # Generic
        "users": {
            "gradient_color": "#4CAF50",
            "fill_color": "#2E7D32",
            "shape": "mxgraph.aws4.users"
        }
    }
    
    # Estilos para contenedores
    CONTAINER_STYLES = {
        "vpc": {
            "fill_color": "#E3F2FD",
            "stroke_color": "#1976D2",
            "font_color": "#1976D2",
            "stroke_width": "3"
        },
        "availability_zone": {
            "fill_color": "#E8F5E8", 
            "stroke_color": "#4CAF50",
            "font_color": "#2E7D32",
            "stroke_width": "2"
        },
        "subnet": {
            "fill_color": "#FFF3E0",
            "stroke_color": "#FF9800", 
            "font_color": "#E65100",
            "stroke_width": "2"
        },
        "security_group": {
            "fill_color": "#FFEBEE",
            "stroke_color": "#F44336",
            "font_color": "#C62828", 
            "stroke_width": "2"
        }
    }
    
    # Estilos para conexiones
    CONNECTION_STYLES = {
        "http": {"color": "#2196F3", "width": "2"},
        "https": {"color": "#4CAF50", "width": "2"},
        "sql": {"color": "#9C27B0", "width": "2"},
        "api": {"color": "#FF9800", "width": "2"},
        "data_flow": {"color": "#607D8B", "width": "2"},
        "primary": {"color": "#232F3E", "width": "3"},
        "secondary": {"color": "#FF9900", "width": "2"}
    }
    
    @classmethod
    def generate_drawio_xml(cls, diagram_data: Dict[str, Any]) -> str:
        """Genera XML DrawIO completo desde datos del diagrama"""
        
        # Metadata
        metadata = diagram_data.get("metadata", {})
        canvas = diagram_data.get("canvas", {})
        architecture = diagram_data.get("architecture", {})
        
        # Configuración del canvas
        canvas_width = canvas.get("width", 2500)
        canvas_height = canvas.get("height", 1600)
        grid_size = canvas.get("grid_size", 10)
        background = canvas.get("background", "white")
        
        # Título
        title = metadata.get("title", "AWS Architecture")
        title_cell = cls.TITLE_TEMPLATE.substitute(
            title=title,
            title_width=canvas_width - 100
        )
        
        # Generar contenido
        content_parts = []
        
        # Componentes
        for component in architecture.get("components", []):
            content_parts.append(cls._generate_component_xml(component))
        
        # Contenedores
        for container in architecture.get("containers", []):
            content_parts.append(cls._generate_container_xml(container))
        
        # Conexiones
        for connection in architecture.get("connections", []):
            content_parts.append(cls._generate_connection_xml(connection))
        
        content = "\n        ".join(content_parts)
        
        # Generar XML final
        timestamp = datetime.now().isoformat()
        diagram_id = f"diagram_{int(datetime.now().timestamp())}"
        
        return cls.BASE_TEMPLATE.substitute(
            timestamp=timestamp,
            diagram_name=title,
            diagram_id=diagram_id,
            canvas_width=canvas_width,
            canvas_height=canvas_height,
            grid_size=grid_size,
            background=background,
            title_cell=title_cell,
            content=content
        )
    
    @classmethod
    def _generate_component_xml(cls, component: Dict[str, Any]) -> str:
        """Genera XML para un componente"""
        
        comp_type = component.get("type", "generic")
        style = cls.COMPONENT_STYLES.get(comp_type, {
            "gradient_color": "#E0E0E0",
            "fill_color": "#BDBDBD", 
            "shape": "rounded=1;whiteSpace=wrap;html=1;"
        })
        
        position = component.get("position", {"x": 100, "y": 100})
        size = component.get("size", {"width": 100, "height": 100})
        
        # Escapar caracteres especiales en label
        label = component.get("label", "Component")
        label = label.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&apos;")
        
        return cls.AWS_COMPONENT_TEMPLATE.substitute(
            id=component["id"],
            label=label,
            gradient_color=style["gradient_color"],
            fill_color=style["fill_color"],
            shape=style["shape"],
            font_size=10,
            parent="1",
            x=position["x"],
            y=position["y"],
            width=size["width"],
            height=size["height"]
        )
    
    @classmethod
    def _generate_container_xml(cls, container: Dict[str, Any]) -> str:
        """Genera XML para un contenedor"""
        
        container_type = container.get("type", "vpc")
        style = cls.CONTAINER_STYLES.get(container_type, cls.CONTAINER_STYLES["vpc"])
        
        bounds = container.get("bounds", {"x": 100, "y": 100, "width": 400, "height": 300})
        
        # Escapar caracteres especiales en label
        label = container.get("label", "Container")
        label = label.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&apos;")
        
        container_xml = cls.CONTAINER_TEMPLATE.substitute(
            id=container["id"],
            label=label,
            fill_color=style["fill_color"],
            stroke_color=style["stroke_color"],
            stroke_width=style["stroke_width"],
            font_color=style["font_color"],
            font_size=12,
            parent="1",
            x=bounds["x"],
            y=bounds["y"],
            width=bounds["width"],
            height=bounds["height"]
        )
        
        # Agregar componentes del contenedor
        components_xml = []
        for component in container.get("components", []):
            comp_xml = cls._generate_component_xml(component)
            # Cambiar parent al contenedor
            comp_xml = comp_xml.replace('parent="1"', f'parent="{container["id"]}"')
            components_xml.append(comp_xml)
        
        # Agregar contenedores hijos
        for child in container.get("children", []):
            child_xml = cls._generate_container_xml(child)
            # Cambiar parent al contenedor padre
            child_xml = child_xml.replace('parent="1"', f'parent="{container["id"]}"')
            components_xml.append(child_xml)
        
        if components_xml:
            return container_xml + "\n        " + "\n        ".join(components_xml)
        
        return container_xml
    
    @classmethod
    def _generate_connection_xml(cls, connection: Dict[str, Any]) -> str:
        """Genera XML para una conexión"""
        
        conn_type = connection.get("type", "http")
        style = cls.CONNECTION_STYLES.get(conn_type, cls.CONNECTION_STYLES["http"])
        
        return cls.CONNECTION_TEMPLATE.substitute(
            id=connection["id"],
            label=connection.get("label", ""),
            color=style["color"],
            width=style["width"],
            source=connection["from"],
            target=connection["to"],
            source_x=0,  # DrawIO calculará automáticamente
            source_y=0,
            target_x=0,
            target_y=0
        )
    
    @classmethod
    def get_network_template(cls, project_name: str) -> Dict[str, Any]:
        """Retorna template para diagrama de red"""
        
        return {
            "metadata": {
                "title": f"{project_name.upper()} - Network Architecture",
                "project_name": project_name,
                "diagram_type": "network",
                "version": "1.0.0"
            },
            "canvas": {
                "width": 2500,
                "height": 1600,
                "grid_size": 10,
                "background": "white"
            },
            "architecture": {
                "components": [
                    {
                        "id": "internet",
                        "type": "internet_gateway",
                        "label": "Internet",
                        "position": {"x": 100, "y": 150},
                        "size": {"width": 80, "height": 80}
                    },
                    {
                        "id": "users",
                        "type": "users", 
                        "label": "Users\\n10K concurrent",
                        "position": {"x": 300, "y": 150},
                        "size": {"width": 80, "height": 80}
                    }
                ],
                "containers": [
                    {
                        "id": "aws_cloud",
                        "type": "vpc",
                        "label": "AWS Cloud - us-east-1",
                        "bounds": {"x": 50, "y": 300, "width": 2300, "height": 1200},
                        "children": [
                            {
                                "id": "vpc_main",
                                "type": "vpc",
                                "label": "VPC 10.0.0.0/16",
                                "bounds": {"x": 50, "y": 100, "width": 2100, "height": 1000},
                                "components": [
                                    {
                                        "id": "api_gateway",
                                        "type": "api_gateway",
                                        "label": "API Gateway",
                                        "position": {"x": 200, "y": 200},
                                        "size": {"width": 80, "height": 80}
                                    },
                                    {
                                        "id": "fargate_app",
                                        "type": "fargate",
                                        "label": "App Services",
                                        "position": {"x": 500, "y": 200},
                                        "size": {"width": 80, "height": 80}
                                    },
                                    {
                                        "id": "rds_db",
                                        "type": "rds",
                                        "label": "RDS PostgreSQL",
                                        "position": {"x": 800, "y": 200},
                                        "size": {"width": 80, "height": 80}
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "connections": [
                    {
                        "id": "conn_users_internet",
                        "from": "users",
                        "to": "internet",
                        "label": "HTTPS",
                        "type": "https"
                    },
                    {
                        "id": "conn_api_app",
                        "from": "api_gateway",
                        "to": "fargate_app",
                        "label": "HTTP",
                        "type": "http"
                    },
                    {
                        "id": "conn_app_db",
                        "from": "fargate_app",
                        "to": "rds_db",
                        "label": "SQL",
                        "type": "sql"
                    }
                ]
            }
        }
    
    @classmethod
    def validate_template_data(cls, data: Dict[str, Any]) -> List[str]:
        """Valida datos del template"""
        
        errors = []
        
        # Validar metadata
        if "metadata" not in data:
            errors.append("metadata es requerido")
        else:
            metadata = data["metadata"]
            required_fields = ["title", "project_name", "diagram_type"]
            for field in required_fields:
                if field not in metadata:
                    errors.append(f"metadata.{field} es requerido")
        
        # Validar architecture
        if "architecture" not in data:
            errors.append("architecture es requerido")
        else:
            arch = data["architecture"]
            if not arch.get("components") and not arch.get("containers"):
                errors.append("Debe tener al menos components o containers")
        
        return errors
