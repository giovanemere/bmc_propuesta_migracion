#!/usr/bin/env python3
"""
Universal Schema - Esquema único para PNG y DrawIO
"""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from enum import Enum

class DiagramType(Enum):
    NETWORK = "network"
    MICROSERVICES = "microservices"
    SECURITY = "security"
    DATA_FLOW = "data_flow"

class OutputFormat(Enum):
    PNG = "png"
    DRAWIO = "drawio"
    BOTH = "both"

@dataclass
class Position:
    x: int
    y: int

@dataclass
class Size:
    width: int
    height: int

@dataclass
class Style:
    color: str = "#232F3E"
    width: int = 2
    fill_color: str = "#E3F2FD"
    stroke_color: str = "#1976D2"

@dataclass
class Component:
    id: str
    type: str
    label: str
    position: Optional[Position] = None
    size: Optional[Size] = None
    style: Optional[Style] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Container:
    id: str
    label: str
    position: Position
    size: Size
    style: Optional[Style] = None
    components: List[Component] = field(default_factory=list)
    children: List['Container'] = field(default_factory=list)

@dataclass
class Connection:
    from_id: str
    to_id: str
    label: str = ""
    style: Optional[Style] = None

@dataclass
class Canvas:
    width: int = 2500
    height: int = 1600
    grid: int = 10
    background: str = "white"

@dataclass
class UniversalDiagramSchema:
    """Esquema universal para PNG y DrawIO"""
    
    # Metadata
    title: str
    diagram_type: DiagramType
    project_name: str
    
    # Canvas
    canvas: Canvas = field(default_factory=Canvas)
    
    # Componentes
    components: List[Component] = field(default_factory=list)
    containers: List[Container] = field(default_factory=list)
    connections: List[Connection] = field(default_factory=list)
    
    # Configuración
    auto_layout: bool = True
    output_format: OutputFormat = OutputFormat.BOTH
    
    def to_dict(self) -> Dict[str, Any]:
        """Convierte a diccionario para JSON"""
        return {
            "title": self.title,
            "diagram_type": self.diagram_type.value,
            "project_name": self.project_name,
            "canvas": {
                "width": self.canvas.width,
                "height": self.canvas.height,
                "grid": self.canvas.grid,
                "background": self.canvas.background
            },
            "components": [
                {
                    "id": c.id,
                    "type": c.type,
                    "label": c.label,
                    "position": {"x": c.position.x, "y": c.position.y} if c.position else None,
                    "size": {"width": c.size.width, "height": c.size.height} if c.size else None,
                    "metadata": c.metadata
                }
                for c in self.components
            ],
            "containers": [
                {
                    "id": cont.id,
                    "label": cont.label,
                    "position": {"x": cont.position.x, "y": cont.position.y},
                    "size": {"width": cont.size.width, "height": cont.size.height},
                    "components": [
                        {
                            "id": c.id,
                            "type": c.type,
                            "label": c.label,
                            "position": {"x": c.position.x, "y": c.position.y} if c.position else None
                        }
                        for c in cont.components
                    ]
                }
                for cont in self.containers
            ],
            "connections": [
                {
                    "from": c.from_id,
                    "to": c.to_id,
                    "label": c.label,
                    "style": {
                        "color": c.style.color,
                        "width": c.style.width
                    } if c.style else None
                }
                for c in self.connections
            ],
            "auto_layout": self.auto_layout,
            "output_format": self.output_format.value
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UniversalDiagramSchema':
        """Crea desde diccionario JSON"""
        
        # Canvas
        canvas_data = data.get("canvas", {})
        canvas = Canvas(
            width=canvas_data.get("width", 2500),
            height=canvas_data.get("height", 1600),
            grid=canvas_data.get("grid", 10),
            background=canvas_data.get("background", "white")
        )
        
        # Componentes
        components = []
        for comp_data in data.get("components", []):
            pos_data = comp_data.get("position")
            size_data = comp_data.get("size")
            
            component = Component(
                id=comp_data["id"],
                type=comp_data["type"],
                label=comp_data["label"],
                position=Position(pos_data["x"], pos_data["y"]) if pos_data else None,
                size=Size(size_data["width"], size_data["height"]) if size_data else None,
                metadata=comp_data.get("metadata", {})
            )
            components.append(component)
        
        # Contenedores
        containers = []
        for cont_data in data.get("containers", []):
            container_components = []
            for comp_data in cont_data.get("components", []):
                pos_data = comp_data.get("position")
                comp = Component(
                    id=comp_data["id"],
                    type=comp_data["type"],
                    label=comp_data["label"],
                    position=Position(pos_data["x"], pos_data["y"]) if pos_data else None
                )
                container_components.append(comp)
            
            container = Container(
                id=cont_data["id"],
                label=cont_data["label"],
                position=Position(cont_data["position"]["x"], cont_data["position"]["y"]),
                size=Size(cont_data["size"]["width"], cont_data["size"]["height"]),
                components=container_components
            )
            containers.append(container)
        
        # Conexiones
        connections = []
        for conn_data in data.get("connections", []):
            style_data = conn_data.get("style")
            style = Style(
                color=style_data.get("color", "#232F3E"),
                width=style_data.get("width", 2)
            ) if style_data else None
            
            connection = Connection(
                from_id=conn_data["from"],
                to_id=conn_data["to"],
                label=conn_data.get("label", ""),
                style=style
            )
            connections.append(connection)
        
        return cls(
            title=data["title"],
            diagram_type=DiagramType(data["diagram_type"]),
            project_name=data["project_name"],
            canvas=canvas,
            components=components,
            containers=containers,
            connections=connections,
            auto_layout=data.get("auto_layout", True),
            output_format=OutputFormat(data.get("output_format", "both"))
        )

class SchemaBuilder:
    """Constructor de esquemas para diferentes tipos de diagramas"""
    
    @staticmethod
    def build_network_schema(project_name: str) -> UniversalDiagramSchema:
        """Construye esquema para diagrama de red"""
        
        schema = UniversalDiagramSchema(
            title=f"{project_name.upper()} - Network Architecture",
            diagram_type=DiagramType.NETWORK,
            project_name=project_name
        )
        
        # Componentes externos
        schema.components.extend([
            Component("internet", "internet_gateway", "Internet", Position(100, 100)),
            Component("users", "users", "BMC Users\\n10K concurrent", Position(300, 100))
        ])
        
        # AWS Cloud container
        aws_cloud = Container(
            "aws_cloud", "AWS Cloud - us-east-1",
            Position(50, 220), Size(2300, 1300)
        )
        
        # VPC container
        vpc = Container(
            "vpc", "VPC 10.0.0.0/16",
            Position(50, 200), Size(2100, 1000)
        )
        
        # AZ containers con componentes
        az_a = Container(
            "az_a", "AZ us-east-1a",
            Position(50, 50), Size(900, 900)
        )
        
        az_a.components.extend([
            Component("nat_1a", "elastic_load_balancing", "NAT Gateway 1A", Position(100, 100)),
            Component("app_1a", "fargate", "App Services 1A", Position(100, 300)),
            Component("db_1a", "rds", "RDS Primary\\nus-east-1a", Position(100, 500))
        ])
        
        vpc.children.append(az_a)
        aws_cloud.children.append(vpc)
        schema.containers.append(aws_cloud)
        
        # Conexiones
        schema.connections.extend([
            Connection("users", "internet", "HTTPS", Style("#232F3E", 3)),
            Connection("internet", "cloudfront", "CDN", Style("#1976D2", 3)),
            Connection("app_1a", "db_1a", "SQL", Style("#2196F3", 2))
        ])
        
        return schema
    
    @staticmethod
    def build_microservices_schema(project_name: str) -> UniversalDiagramSchema:
        """Construye esquema para microservicios"""
        
        schema = UniversalDiagramSchema(
            title=f"{project_name.upper()} - Microservices Architecture",
            diagram_type=DiagramType.MICROSERVICES,
            project_name=project_name
        )
        
        # Microservicios
        schema.components.extend([
            Component("api_gateway", "api_gateway", "API Gateway\\nREST + GraphQL", Position(200, 200)),
            Component("cert_service", "fargate", "Certificate Service\\nPDF Generation", Position(500, 200)),
            Component("database", "rds", "PostgreSQL\\n60M Products", Position(800, 200))
        ])
        
        # Conexiones
        schema.connections.extend([
            Connection("api_gateway", "cert_service", "HTTP", Style("#2196F3", 2)),
            Connection("cert_service", "database", "SQL", Style("#4CAF50", 2))
        ])
        
        return schema
