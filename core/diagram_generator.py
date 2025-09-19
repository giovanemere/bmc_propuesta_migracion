#!/usr/bin/env python3
"""
Diagram Generator - Módulo transversal para generar diagramas
Genera diagramas desde configuración MCP parseada
"""

from diagrams import Diagram, Cluster
from diagrams.aws.compute import Fargate, Lambda
from diagrams.aws.database import RDS, Elasticache
from diagrams.aws.storage import S3
from diagrams.aws.network import APIGateway, CloudFront, ELB
from diagrams.aws.security import Cognito, WAF
from diagrams.aws.integration import SQS, SNS
from diagrams.aws.ml import Textract
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.client import Users
from diagrams.onprem.network import Internet
from typing import Dict, Any, List
import os

class DiagramGenerator:
    """Generador genérico de diagramas desde configuración MCP"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str = "output"):
        self.config = config
        self.output_dir = output_dir
        self.aws_services = self._init_aws_services()
        
    def _init_aws_services(self) -> Dict[str, Any]:
        """Inicializa mapeo de servicios AWS"""
        return {
            "fargate": Fargate,
            "lambda": Lambda,
            "rds": RDS,
            "elasticache": Elasticache,
            "s3": S3,
            "api_gateway": APIGateway,
            "cloudfront": CloudFront,
            "elb": ELB,
            "cognito": Cognito,
            "waf": WAF,
            "sqs": SQS,
            "sns": SNS,
            "textract": Textract,
            "cloudwatch": Cloudwatch,
            "users": Users,
            "internet": Internet
        }
    
    def create_service(self, service_type: str, name: str, **kwargs) -> Any:
        """Crea un servicio AWS dinámicamente"""
        service_class = self.aws_services.get(service_type.lower())
        if service_class:
            return service_class(name)
        else:
            print(f"⚠️ Unknown service type: {service_type}")
            return None
    
    def generate_architecture_diagram(self, title: str, filename: str) -> str:
        """Genera diagrama de arquitectura principal"""
        
        with Diagram(title, filename=f"{self.output_dir}/png/{filename}", show=False, direction="TB"):
            
            # Crear usuarios
            users = self.create_service("users", "BMC Users")
            
            with Cluster("AWS Cloud"):
                # Edge Security
                with Cluster("Edge Security"):
                    cloudfront = self.create_service("cloudfront", "CloudFront")
                    waf = self.create_service("waf", "WAF")
                    api_gateway = self.create_service("api_gateway", "API Gateway")
                    cognito = self.create_service("cognito", "Cognito")
                
                # Compute Layer
                with Cluster("Compute Layer"):
                    alb = self.create_service("elb", "ALB")
                    
                    # Microservicios dinámicos desde config
                    microservices = []
                    if "microservices" in self.config:
                        for service_name, service_config in self.config["microservices"].items():
                            if isinstance(service_config, dict):
                                cpu = service_config.get("cpu", "2vCPU")
                                memory = service_config.get("memory", "4GB")
                                service = self.create_service("fargate", f"{service_name}\n{cpu}/{memory}")
                                microservices.append(service)
                    
                    # Servicios por defecto si no hay config
                    if not microservices:
                        invoice_service = self.create_service("fargate", "Invoice Service\n2vCPU/4GB")
                        product_service = self.create_service("fargate", "Product Service\n4vCPU/8GB")
                        microservices = [invoice_service, product_service]
                
                # Data Layer
                with Cluster("Data Layer"):
                    rds = self.create_service("rds", "RDS PostgreSQL")
                    redis = self.create_service("elasticache", "Redis Cache")
                    s3 = self.create_service("s3", "S3 Documents")
                
                # AI/ML
                textract = self.create_service("textract", "Textract OCR")
                
                # Integration
                with Cluster("Integration"):
                    sqs = self.create_service("sqs", "SQS")
                    sns = self.create_service("sns", "SNS")
                
                # Monitoring
                cloudwatch = self.create_service("cloudwatch", "CloudWatch")
            
            # External
            dian_api = self.create_service("internet", "DIAN API")
            
            # Conexiones
            if all([users, cloudfront, waf, api_gateway, cognito]):
                users >> cloudfront >> waf >> api_gateway >> cognito
            
            if alb and microservices:
                api_gateway >> alb
                for service in microservices:
                    if service:
                        alb >> service
            
            if microservices and rds and redis:
                for service in microservices:
                    if service:
                        service >> redis >> rds
            
            if microservices and cloudwatch:
                for service in microservices:
                    if service:
                        service >> cloudwatch
        
        return f"{self.output_dir}/png/{filename}.png"
    
    def generate_microservices_diagram(self, title: str, filename: str) -> str:
        """Genera diagrama detallado de microservicios"""
        
        with Diagram(title, filename=f"{self.output_dir}/png/{filename}", show=False, direction="TB"):
            
            api_gateway = self.create_service("api_gateway", "API Gateway")
            
            with Cluster("ECS Fargate Cluster"):
                # Generar microservicios desde config
                services = []
                if "microservices" in self.config:
                    for service_name, service_config in self.config["microservices"].items():
                        if isinstance(service_config, dict):
                            with Cluster(f"{service_name.title()} Service"):
                                alb = self.create_service("elb", f"{service_name} ALB")
                                
                                # Crear tasks basados en configuración
                                min_cap = service_config.get("min_capacity", 2)
                                cpu = service_config.get("cpu", 2048)
                                memory = service_config.get("memory", 4096)
                                
                                tasks = []
                                for i in range(min_cap):
                                    task = self.create_service("fargate", f"Task {i+1}\n{cpu//1024}vCPU")
                                    tasks.append(task)
                                
                                services.append({"alb": alb, "tasks": tasks})
                
                # Conexiones
                for service in services:
                    if service["alb"]:
                        api_gateway >> service["alb"]
                        for task in service["tasks"]:
                            if task:
                                service["alb"] >> task
        
        return f"{self.output_dir}/png/{filename}.png"
    
    def generate_drawio(self, title: str, filename: str) -> str:
        """Genera archivo Draw.io"""
        
        drawio_template = f'''<mxfile host="app.diagrams.net">
  <diagram name="{title}" id="diagram1">
    <mxGraphModel dx="1600" dy="900" grid="1" gridSize="10">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Generated from MCP Config -->
        <mxCell id="title" value="{title}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=none;fontColor=#FFFFFF;fontSize=16;fontStyle=1;align=center;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="800" height="40" as="geometry"/>
        </mxCell>
        
        <!-- AWS Cloud -->
        <mxCell id="aws" value="AWS Cloud" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="100" y="100" width="700" height="500" as="geometry"/>
        </mxCell>
        
        <!-- Services from MCP Config -->
        <!-- This would be dynamically generated based on config -->
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
        
        output_file = f"{self.output_dir}/drawio/{filename}.drawio"
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(drawio_template)
        
        return output_file
    
    def generate_all(self, project_name: str = "Architecture") -> Dict[str, str]:
        """Genera todos los diagramas"""
        
        # Crear directorios de salida
        os.makedirs(f"{self.output_dir}/png", exist_ok=True)
        os.makedirs(f"{self.output_dir}/drawio", exist_ok=True)
        
        results = {}
        
        # Diagrama principal
        results["architecture"] = self.generate_architecture_diagram(
            f"{project_name} - AWS Architecture",
            f"{project_name.lower()}_architecture"
        )
        
        # Diagrama de microservicios
        results["microservices"] = self.generate_microservices_diagram(
            f"{project_name} - Microservices Detail", 
            f"{project_name.lower()}_microservices"
        )
        
        # Archivo Draw.io
        results["drawio"] = self.generate_drawio(
            f"{project_name} - AWS Architecture",
            f"{project_name.lower()}_architecture"
        )
        
        return results
