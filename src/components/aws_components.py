#!/usr/bin/env python3
"""
AWS Components - Clases para cada tipo de componente AWS
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List
from enum import Enum

class ComponentType(Enum):
    # Network
    VPC = "vpc"
    SUBNET = "subnet"
    AVAILABILITY_ZONE = "availability_zone"
    INTERNET_GATEWAY = "internet_gateway"
    NAT_GATEWAY = "nat_gateway"
    
    # Compute
    FARGATE = "fargate"
    LAMBDA = "lambda"
    EC2 = "ec2"
    ECS = "ecs"
    
    # Database
    RDS = "rds"
    DYNAMODB = "dynamodb"
    ELASTICACHE = "elasticache"
    
    # Storage
    S3 = "s3"
    EFS = "efs"
    EBS = "ebs"
    
    # API & Load Balancing
    API_GATEWAY = "api_gateway"
    ELB = "elb"
    CLOUDFRONT = "cloudfront"
    
    # Security
    WAF = "waf"
    COGNITO = "cognito"
    KMS = "kms"
    
    # Integration
    SQS = "sqs"
    SNS = "sns"
    
    # Generic
    USERS = "users"
    CLIENT = "client"

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
    fill_color: str = "#E3F2FD"
    stroke_color: str = "#1976D2"
    stroke_width: int = 2
    font_size: int = 10

class AWSComponent(ABC):
    """Clase base para todos los componentes AWS"""
    
    def __init__(self, id: str, label: str, position: Optional[Position] = None, 
                 size: Optional[Size] = None, style: Optional[Style] = None):
        self.id = id
        self.label = label
        self.position = position or Position(100, 100)
        self.size = size or Size(100, 100)
        self.style = style or Style()
        self.properties: Dict[str, Any] = {}
        self.metadata: Dict[str, Any] = {}
    
    @property
    @abstractmethod
    def component_type(self) -> ComponentType:
        """Tipo de componente"""
        pass
    
    @property
    @abstractmethod
    def aws_service_name(self) -> str:
        """Nombre del servicio AWS"""
        pass
    
    @property
    @abstractmethod
    def drawio_shape(self) -> str:
        """Shape de DrawIO para este componente"""
        pass
    
    @property
    @abstractmethod
    def png_class(self) -> str:
        """Clase de diagrams library para PNG"""
        pass
    
    def to_dict(self) -> Dict[str, Any]:
        """Convierte a diccionario"""
        return {
            "id": self.id,
            "type": self.component_type.value,
            "label": self.label,
            "position": {"x": self.position.x, "y": self.position.y},
            "size": {"width": self.size.width, "height": self.size.height},
            "properties": self.properties,
            "metadata": self.metadata
        }
    
    def validate(self) -> List[str]:
        """Valida el componente y retorna lista de errores"""
        errors = []
        
        if not self.id:
            errors.append("ID es requerido")
        elif not self.id[0].isalpha():
            errors.append(f"ID debe comenzar con letra: {self.id}")
        elif not all(c.isalnum() or c in '_-' for c in self.id):
            errors.append(f"ID contiene caracteres inválidos: {self.id}")
        
        if not self.label:
            errors.append("Label es requerido")
        
        if self.size.width < 50 or self.size.height < 50:
            errors.append("Tamaño mínimo es 50x50")
        
        return errors

# Network Components
class VPC(AWSComponent):
    component_type = ComponentType.VPC
    aws_service_name = "Amazon VPC"
    drawio_shape = "mxgraph.aws4.vpc"
    png_class = "diagrams.aws.network.VPC"
    
    def __init__(self, id: str, label: str, cidr: str = "10.0.0.0/16", **kwargs):
        super().__init__(id, label, **kwargs)
        self.properties.update({
            "cidr": cidr,
            "dns_hostnames": True,
            "dns_resolution": True
        })

class Subnet(AWSComponent):
    component_type = ComponentType.SUBNET
    aws_service_name = "VPC Subnet"
    drawio_shape = "mxgraph.aws4.vpc_subnet"
    png_class = "diagrams.aws.network.PrivateSubnet"
    
    def __init__(self, id: str, label: str, cidr: str, subnet_type: str = "private", **kwargs):
        super().__init__(id, label, **kwargs)
        self.properties.update({
            "cidr": cidr,
            "type": subnet_type,  # public, private, isolated
            "auto_assign_public_ip": subnet_type == "public"
        })

class InternetGateway(AWSComponent):
    component_type = ComponentType.INTERNET_GATEWAY
    aws_service_name = "Internet Gateway"
    drawio_shape = "mxgraph.aws4.internet_gateway"
    png_class = "diagrams.onprem.network.Internet"

class NATGateway(AWSComponent):
    component_type = ComponentType.NAT_GATEWAY
    aws_service_name = "NAT Gateway"
    drawio_shape = "mxgraph.aws4.nat_gateway"
    png_class = "diagrams.aws.network.NATGateway"
    
    def __init__(self, id: str, label: str, bandwidth: str = "45 Gbps", **kwargs):
        super().__init__(id, label, **kwargs)
        self.properties.update({
            "bandwidth": bandwidth,
            "elastic_ip": True
        })

# Compute Components
class Fargate(AWSComponent):
    component_type = ComponentType.FARGATE
    aws_service_name = "AWS Fargate"
    drawio_shape = "mxgraph.aws4.fargate"
    png_class = "diagrams.aws.compute.Fargate"
    
    def __init__(self, id: str, label: str, cpu: str = "2 vCPU", memory: str = "4 GB", **kwargs):
        super().__init__(id, label, **kwargs)
        self.properties.update({
            "cpu": cpu,
            "memory": memory,
            "platform_version": "LATEST"
        })

class Lambda(AWSComponent):
    component_type = ComponentType.LAMBDA
    aws_service_name = "AWS Lambda"
    drawio_shape = "mxgraph.aws4.lambda"
    png_class = "diagrams.aws.compute.Lambda"
    
    def __init__(self, id: str, label: str, runtime: str = "python3.9", **kwargs):
        super().__init__(id, label, **kwargs)
        self.properties.update({
            "runtime": runtime,
            "timeout": "30s",
            "memory": "128 MB"
        })

# Database Components
class RDS(AWSComponent):
    component_type = ComponentType.RDS
    aws_service_name = "Amazon RDS"
    drawio_shape = "mxgraph.aws4.rds"
    png_class = "diagrams.aws.database.RDS"
    
    def __init__(self, id: str, label: str, engine: str = "postgresql", 
                 instance_class: str = "db.t3.micro", **kwargs):
        super().__init__(id, label, **kwargs)
        self.properties.update({
            "engine": engine,
            "instance_class": instance_class,
            "multi_az": False,
            "storage_encrypted": True
        })

class DynamoDB(AWSComponent):
    component_type = ComponentType.DYNAMODB
    aws_service_name = "Amazon DynamoDB"
    drawio_shape = "mxgraph.aws4.dynamodb"
    png_class = "diagrams.aws.database.Dynamodb"

# Storage Components
class S3(AWSComponent):
    component_type = ComponentType.S3
    aws_service_name = "Amazon S3"
    drawio_shape = "mxgraph.aws4.s3"
    png_class = "diagrams.aws.storage.S3"
    
    def __init__(self, id: str, label: str, storage_class: str = "STANDARD", **kwargs):
        super().__init__(id, label, **kwargs)
        self.properties.update({
            "storage_class": storage_class,
            "versioning": True,
            "encryption": "AES256"
        })

# API & Load Balancing
class APIGateway(AWSComponent):
    component_type = ComponentType.API_GATEWAY
    aws_service_name = "Amazon API Gateway"
    drawio_shape = "mxgraph.aws4.api_gateway"
    png_class = "diagrams.aws.network.APIGateway"
    
    def __init__(self, id: str, label: str, api_type: str = "REST", **kwargs):
        super().__init__(id, label, **kwargs)
        self.properties.update({
            "type": api_type,  # REST, HTTP, WebSocket
            "throttle_rate": "10000/sec",
            "burst_limit": "5000"
        })

class ELB(AWSComponent):
    component_type = ComponentType.ELB
    aws_service_name = "Elastic Load Balancing"
    drawio_shape = "mxgraph.aws4.elastic_load_balancing"
    png_class = "diagrams.aws.network.ELB"
    
    def __init__(self, id: str, label: str, lb_type: str = "application", **kwargs):
        super().__init__(id, label, **kwargs)
        self.properties.update({
            "type": lb_type,  # application, network, gateway
            "scheme": "internet-facing",
            "ip_address_type": "ipv4"
        })

class CloudFront(AWSComponent):
    component_type = ComponentType.CLOUDFRONT
    aws_service_name = "Amazon CloudFront"
    drawio_shape = "mxgraph.aws4.cloudfront"
    png_class = "diagrams.aws.network.CloudFront"

# Security Components
class WAF(AWSComponent):
    component_type = ComponentType.WAF
    aws_service_name = "AWS WAF"
    drawio_shape = "mxgraph.aws4.waf"
    png_class = "diagrams.aws.security.WAF"

class Cognito(AWSComponent):
    component_type = ComponentType.COGNITO
    aws_service_name = "Amazon Cognito"
    drawio_shape = "mxgraph.aws4.cognito"
    png_class = "diagrams.aws.security.Cognito"

# Generic Components
class Users(AWSComponent):
    component_type = ComponentType.USERS
    aws_service_name = "Users"
    drawio_shape = "mxgraph.aws4.users"
    png_class = "diagrams.onprem.client.Users"

# Container Classes
class AWSContainer(ABC):
    """Clase base para contenedores AWS"""
    
    def __init__(self, id: str, label: str, bounds: Dict[str, int], 
                 style: Optional[Style] = None):
        self.id = id
        self.label = label
        self.bounds = bounds  # {x, y, width, height}
        self.style = style or Style()
        self.components: List[AWSComponent] = []
        self.children: List['AWSContainer'] = []
        self.properties: Dict[str, Any] = {}
    
    def add_component(self, component: AWSComponent):
        """Agrega componente al contenedor"""
        self.components.append(component)
    
    def add_child(self, child: 'AWSContainer'):
        """Agrega contenedor hijo"""
        self.children.append(child)
    
    def validate(self) -> List[str]:
        """Valida el contenedor"""
        errors = []
        
        if not self.id:
            errors.append("Container ID es requerido")
        
        if self.bounds["width"] < 200 or self.bounds["height"] < 150:
            errors.append("Container muy pequeño (mínimo 200x150)")
        
        # Validar componentes
        for component in self.components:
            errors.extend(component.validate())
        
        # Validar hijos
        for child in self.children:
            errors.extend(child.validate())
        
        return errors

class VPCContainer(AWSContainer):
    """Contenedor VPC"""
    
    def __init__(self, id: str, label: str, bounds: Dict[str, int], 
                 cidr: str = "10.0.0.0/16", **kwargs):
        super().__init__(id, label, bounds, **kwargs)
        self.properties.update({
            "cidr": cidr,
            "dns_hostnames": True,
            "dns_resolution": True
        })

class AvailabilityZoneContainer(AWSContainer):
    """Contenedor Availability Zone"""
    
    def __init__(self, id: str, label: str, bounds: Dict[str, int], 
                 zone_name: str, **kwargs):
        super().__init__(id, label, bounds, **kwargs)
        self.properties.update({
            "zone_name": zone_name,
            "region": zone_name[:-1]  # us-east-1a -> us-east-1
        })

# Factory para crear componentes
class ComponentFactory:
    """Factory para crear componentes AWS"""
    
    _component_classes = {
        ComponentType.VPC: VPC,
        ComponentType.SUBNET: Subnet,
        ComponentType.INTERNET_GATEWAY: InternetGateway,
        ComponentType.NAT_GATEWAY: NATGateway,
        ComponentType.FARGATE: Fargate,
        ComponentType.LAMBDA: Lambda,
        ComponentType.RDS: RDS,
        ComponentType.DYNAMODB: DynamoDB,
        ComponentType.S3: S3,
        ComponentType.API_GATEWAY: APIGateway,
        ComponentType.ELB: ELB,
        ComponentType.CLOUDFRONT: CloudFront,
        ComponentType.WAF: WAF,
        ComponentType.COGNITO: Cognito,
        ComponentType.USERS: Users
    }
    
    @classmethod
    def create_component(cls, component_type: str, id: str, label: str, 
                        **kwargs) -> AWSComponent:
        """Crea componente por tipo"""
        
        comp_type = ComponentType(component_type)
        component_class = cls._component_classes.get(comp_type)
        
        if not component_class:
            raise ValueError(f"Tipo de componente no soportado: {component_type}")
        
        return component_class(id, label, **kwargs)
    
    @classmethod
    def get_supported_types(cls) -> List[str]:
        """Retorna tipos de componentes soportados"""
        return [ct.value for ct in cls._component_classes.keys()]
