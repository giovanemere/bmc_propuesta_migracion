#!/usr/bin/env python3
"""
Diagram Model - Modelo de datos para componentes y conexiones
Separa datos de lógica de presentación
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from enum import Enum

class ComponentType(Enum):
    AWS_SERVICE = "aws_service"
    CONTAINER = "container"
    TITLE = "title"
    CONNECTION = "connection"

class LayoutType(Enum):
    HIERARCHICAL = "hierarchical"
    GRID = "grid"
    CIRCULAR = "circular"
    FORCE_DIRECTED = "force_directed"

@dataclass
class Position:
    x: int
    y: int
    width: int = 78
    height: int = 78

@dataclass
class Style:
    fill_color: str = "#E8F5E8"
    stroke_color: str = "#4CAF50"
    font_color: str = "#2E7D32"
    font_size: int = 12
    stroke_width: int = 2

@dataclass
class Component:
    id: str
    name: str
    component_type: ComponentType
    position: Position
    style: Style
    shape: Optional[str] = None
    label: Optional[str] = None
    parent: Optional[str] = None
    specifications: Dict[str, str] = field(default_factory=dict)

@dataclass
class Connection:
    id: str
    source: str
    target: str
    label: str
    style: Style
    connection_type: str = "orthogonal"

@dataclass
class DiagramModel:
    name: str
    components: List[Component] = field(default_factory=list)
    connections: List[Connection] = field(default_factory=list)
    layout: LayoutType = LayoutType.HIERARCHICAL
    canvas_size: Tuple[int, int] = (1400, 1000)
    
    def add_component(self, component: Component) -> None:
        """Agrega componente al modelo"""
        self.components.append(component)
    
    def add_connection(self, connection: Connection) -> None:
        """Agrega conexión al modelo"""
        self.connections.append(connection)
    
    def get_component_by_id(self, component_id: str) -> Optional[Component]:
        """Busca componente por ID"""
        return next((c for c in self.components if c.id == component_id), None)
    
    def validate(self) -> List[str]:
        """Valida el modelo y retorna errores"""
        errors = []
        
        # Validar IDs únicos
        ids = [c.id for c in self.components]
        if len(ids) != len(set(ids)):
            errors.append("IDs de componentes duplicados")
        
        # Validar conexiones
        for conn in self.connections:
            if not self.get_component_by_id(conn.source):
                errors.append(f"Conexión {conn.id}: source {conn.source} no existe")
            if not self.get_component_by_id(conn.target):
                errors.append(f"Conexión {conn.id}: target {conn.target} no existe")
        
        return errors

class DiagramModelBuilder:
    """Builder para crear modelos de diagrama desde configuración"""
    
    @staticmethod
    def from_config(config: Dict) -> DiagramModel:
        """Crea modelo desde configuración MCP"""
        
        model = DiagramModel(name="BMC Architecture")
        
        # Extraer microservicios
        microservices = config.get("microservices", {})
        aws_services = config.get("aws_services", {})
        
        # Crear componentes AWS
        y_offset = 150
        x_offset = 150
        
        for i, (service_name, service_config) in enumerate(microservices.items()):
            component = Component(
                id=f"ms_{service_name}",
                name=service_name,
                component_type=ComponentType.AWS_SERVICE,
                position=Position(x_offset + (i * 200), y_offset + 200),
                style=Style(fill_color="#E8F5E8", stroke_color="#4CAF50"),
                shape="mxgraph.aws4.fargate",
                label=DiagramModelBuilder._build_microservice_label(service_name, service_config),
                specifications=service_config.get("scaling", {})
            )
            model.add_component(component)
        
        # Crear servicios AWS
        for i, (service_name, service_config) in enumerate(aws_services.items()):
            component = Component(
                id=f"aws_{service_name}",
                name=service_name,
                component_type=ComponentType.AWS_SERVICE,
                position=Position(x_offset + (i * 200), y_offset + 400),
                style=Style(fill_color="#E3F2FD", stroke_color="#1976D2"),
                shape=DiagramModelBuilder._get_aws_shape(service_name),
                label=DiagramModelBuilder._build_aws_label(service_name, service_config),
                specifications=service_config
            )
            model.add_component(component)
        
        # Crear conexiones automáticas
        DiagramModelBuilder._create_connections(model, config)
        
        return model
    
    @staticmethod
    def _build_microservice_label(name: str, config: Dict) -> str:
        """Construye label para microservicio"""
        scaling = config.get("scaling", {})
        cpu = scaling.get("cpu", "2vCPU")
        memory = scaling.get("memory", "4GB")
        
        return f"{name.title()} Service\\n{cpu}/{memory}\\nAuto Scaling"
    
    @staticmethod
    def _build_aws_label(name: str, config: Dict) -> str:
        """Construye label para servicio AWS"""
        if "rds" in name.lower():
            instance = config.get("instance_class", "db.r6g.large")
            return f"RDS PostgreSQL\\n{instance}\\nMulti-AZ"
        elif "redis" in name.lower():
            nodes = config.get("cluster", {}).get("num_nodes", 3)
            return f"ElastiCache Redis\\n{nodes} nodes\\nCluster mode"
        elif "s3" in name.lower():
            return f"S3 Storage\\nIntelligent Tiering\\nVersioning"
        else:
            return name.replace("_", " ").title()
    
    @staticmethod
    def _get_aws_shape(service_name: str) -> str:
        """Mapea nombre de servicio a shape AWS"""
        shape_map = {
            "rds": "mxgraph.aws4.rds",
            "redis": "mxgraph.aws4.elasticache",
            "s3": "mxgraph.aws4.s3",
            "api_gateway": "mxgraph.aws4.api_gateway",
            "cloudfront": "mxgraph.aws4.cloudfront",
            "waf": "mxgraph.aws4.waf"
        }
        
        for key, shape in shape_map.items():
            if key in service_name.lower():
                return shape
        
        return "mxgraph.aws4.generic"
    
    @staticmethod
    def _create_connections(model: DiagramModel, config: Dict) -> None:
        """Crea conexiones automáticas basadas en patrones"""
        
        # Buscar componentes
        microservices = [c for c in model.components if c.id.startswith("ms_")]
        aws_services = [c for c in model.components if c.id.startswith("aws_")]
        
        # Conexiones microservicio -> base de datos
        rds_component = next((c for c in aws_services if "rds" in c.id), None)
        if rds_component:
            for ms in microservices:
                if "invoice" in ms.id or "product" in ms.id:
                    connection = Connection(
                        id=f"conn_{ms.id}_to_{rds_component.id}",
                        source=ms.id,
                        target=rds_component.id,
                        label="Database Access",
                        style=Style(stroke_color="#2196F3", font_color="#2196F3")
                    )
                    model.add_connection(connection)
        
        # Conexiones microservicio -> cache
        redis_component = next((c for c in aws_services if "redis" in c.id), None)
        if redis_component:
            for ms in microservices:
                if "product" in ms.id:
                    connection = Connection(
                        id=f"conn_{ms.id}_to_{redis_component.id}",
                        source=ms.id,
                        target=redis_component.id,
                        label="Cache Access",
                        style=Style(stroke_color="#FF9800", font_color="#FF9800")
                    )
                    model.add_connection(connection)
