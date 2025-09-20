#!/usr/bin/env python3
"""
Refined Diagram Generator - Generador refinado para diagramas profesionales
Crea diagramas detallados y profesionales usando configuración MCP refinada
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Fargate, Lambda, ECS
from diagrams.aws.database import RDS, Elasticache, Redshift
from diagrams.aws.storage import S3, EBS
from diagrams.aws.network import APIGateway, CloudFront, ELB, VPC, PrivateSubnet, PublicSubnet
from diagrams.aws.security import Cognito, WAF, KMS, SecretsManager
from diagrams.aws.integration import SQS, SNS, Eventbridge
from diagrams.aws.ml import Textract, Comprehend
from diagrams.aws.management import Cloudwatch, SystemsManager
from diagrams.aws.analytics import Kinesis
from diagrams.onprem.client import Users, Client
from diagrams.onprem.network import Internet
from diagrams.generic.blank import Blank
from typing import Dict, Any, List
import os

class RefinedDiagramGenerator:
    """Generador refinado de diagramas AWS profesionales"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str = "output"):
        self.config = config
        self.output_dir = output_dir
        self.diagram_config = config.get("diagram_config", {})
        self.colors = self.diagram_config.get("colors", {})
    
    def generate_diagram(self, diagram_type: str, output_path: str = None) -> str:
        """Genera diagrama según el tipo especificado"""
        
        if output_path:
            self.output_dir = output_path
        
        os.makedirs(self.output_dir, exist_ok=True)
        
        if diagram_type == "network":
            return self._generate_network_png()
        elif diagram_type == "microservices":
            return self._generate_microservices_png()
        elif diagram_type == "security":
            return self._generate_security_png()
        elif diagram_type == "data_flow":
            return self._generate_data_flow_png()
        else:
            raise ValueError(f"Tipo de diagrama no soportado: {diagram_type}")
    
    def _generate_network_png(self) -> str:
        """Genera diagrama de red completo"""
        
        filename = os.path.join(self.output_dir, "network_architecture")
        
        with Diagram("BMC Network Architecture", 
                    show=False, 
                    filename=filename,
                    direction="TB"):
            
            # Usuarios externos
            users = Users("BMC Users\n10K Concurrent")
            
            # Edge services
            with Cluster("Edge & Security"):
                cloudfront = CloudFront("CloudFront CDN")
                waf = WAF("AWS WAF")
                api_gw = APIGateway("API Gateway")
            
            # VPC y microservicios
            with Cluster("VPC 10.0.0.0/16"):
                with Cluster("AZ us-east-1a"):
                    alb = ELB("Application LB")
                    
                    # Microservicios
                    invoice = Fargate("Invoice Service")
                    product = Fargate("Product Service")
                    ocr = Fargate("OCR Service")
                    commission = Fargate("Commission Service")
                    certificate = Fargate("Certificate Service")
                    
                    rds_primary = RDS("PostgreSQL Primary")
                
                with Cluster("Storage"):
                    s3_docs = S3("S3 Documents")
                    s3_data = S3("S3 Data Lake")
            
            # Conexiones
            users >> cloudfront >> waf >> api_gw >> alb
            alb >> [invoice, product, ocr, commission, certificate]
            [invoice, product, commission] >> rds_primary
            certificate >> s3_docs
            product >> s3_data
        
        png_path = f"{filename}.png"
        print(f"✅ Network PNG generado: {png_path}")
        return png_path
    
    def _generate_microservices_png(self) -> str:
        """Genera diagrama de microservicios detallado"""
        
        filename = os.path.join(self.output_dir, "microservices_detailed")
        
        with Diagram("BMC Microservices Architecture", 
                    show=False, 
                    filename=filename,
                    direction="LR"):
            
            # API Gateway
            api_gw = APIGateway("API Gateway")
            
            # Microservicios con detalles
            with Cluster("Microservices Layer"):
                invoice = Fargate("Invoice Service\nProcessing & Batch")
                product = Fargate("Product Service\n60M Products")
                ocr = Fargate("OCR Service\n95% Accuracy")
                commission = Fargate("Commission Service\nDIAN Compliance")
                certificate = Fargate("Certificate Service\nPDF Generation")
            
            # Base de datos
            with Cluster("Data Layer"):
                rds = RDS("PostgreSQL\nPrimary DB")
                cache = Elasticache("Redis Cache")
            
            # Storage
            with Cluster("Storage Layer"):
                s3_docs = S3("Documents\nPDFs & Files")
                s3_data = S3("Data Lake\nAnalytics")
            
            # Conexiones
            api_gw >> [invoice, product, ocr, commission, certificate]
            [invoice, product, ocr, commission] >> rds
            [invoice, product] >> cache
            certificate >> s3_docs
            [product, invoice] >> s3_data
        
        png_path = f"{filename}.png"
        print(f"✅ Microservices PNG generado: {png_path}")
        return png_path
    
    def _generate_security_png(self) -> str:
        """Genera diagrama de seguridad"""
        
        filename = os.path.join(self.output_dir, "security_architecture")
        
        with Diagram("BMC Security Architecture", 
                    show=False, 
                    filename=filename,
                    direction="TB"):
            
            # Internet y usuarios
            internet = Internet("Internet")
            users = Users("BMC Users")
            
            # Capa de seguridad
            with Cluster("Security Layer"):
                waf = WAF("AWS WAF\nDDoS Protection")
                cloudfront = CloudFront("CloudFront\nSSL/TLS")
                cognito = Cognito("Cognito\nAuthentication")
            
            # API y aplicación
            with Cluster("Application Layer"):
                api_gw = APIGateway("API Gateway\nRate Limiting")
                
                with Cluster("VPC Security"):
                    fargate = Fargate("Microservices\nPrivate Subnets")
                    rds = RDS("Database\nEncrypted")
            
            # Servicios de seguridad
            with Cluster("Security Services"):
                kms = KMS("KMS\nEncryption Keys")
                secrets = SecretsManager("Secrets Manager\nCredentials")
                cloudwatch = Cloudwatch("CloudWatch\nSecurity Logs")
            
            # Conexiones de seguridad
            users >> internet >> waf >> cloudfront >> api_gw
            api_gw >> cognito
            cognito >> fargate
            fargate >> rds
            [fargate, rds] >> kms
            fargate >> secrets
            [waf, api_gw, fargate] >> cloudwatch
        
        png_path = f"{filename}.png"
        print(f"✅ Security PNG generado: {png_path}")
        return png_path
    
    def _generate_data_flow_png(self) -> str:
        """Genera diagrama de flujo de datos"""
        
        filename = os.path.join(self.output_dir, "data_flow")
        
        with Diagram("BMC Data Flow Architecture", 
                    show=False, 
                    filename=filename,
                    direction="LR"):
            
            # Entrada de datos
            with Cluster("Data Input"):
                upload = Blank("Invoice Upload")
                batch = Blank("Batch Processing")
            
            # Procesamiento
            with Cluster("Processing"):
                ocr = Fargate("OCR Service\nPDF Analysis")
                invoice = Fargate("Invoice Service\nValidation")
                product = Fargate("Product Service\nMatching")
                commission = Fargate("Commission Service\nCalculation")
            
            # Almacenamiento
            with Cluster("Storage & Output"):
                rds = RDS("PostgreSQL\nTransactional")
                s3_data = S3("Data Lake\nAnalytics")
                certificate = Fargate("Certificate Service\nPDF Generation")
                s3_docs = S3("Documents\nGenerated PDFs")
            
            # Notificaciones
            with Cluster("Notifications"):
                sqs = SQS("SQS Queue\nAsync Processing")
                sns = SNS("SNS\nEmail Delivery")
            
            # Flujo de datos
            upload >> ocr >> invoice >> product >> commission
            [upload, batch] >> invoice
            [invoice, commission] >> rds
            commission >> certificate >> s3_docs
            [invoice, product] >> s3_data
            certificate >> sqs >> sns
        
        png_path = f"{filename}.png"
        print(f"✅ Data Flow PNG generado: {png_path}")
        return png_path

# Alias para compatibilidad
DiagramGenerator = RefinedDiagramGenerator
