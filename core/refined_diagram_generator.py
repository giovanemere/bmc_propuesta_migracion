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
        self.fonts = self.diagram_config.get("fonts", {})
        
        # Configurar estilos
        self.setup_styles()
        
    def setup_styles(self):
        """Configura estilos para diagramas"""
        self.edge_styles = {
            "primary": {"color": self.colors.get("primary", "#232F3E"), "style": "bold"},
            "secondary": {"color": self.colors.get("secondary", "#FF9900"), "style": "dashed"},
            "data": {"color": self.colors.get("info", "#2196F3"), "style": "dotted"},
            "security": {"color": self.colors.get("danger", "#F44336"), "style": "bold"},
            "monitoring": {"color": self.colors.get("warning", "#FF9800"), "style": "dashed"}
        }
        
    def create_network_diagram(self, title: str, filename: str) -> str:
        """Genera diagrama detallado de red y VPC"""
        
        graph_attr = {
            "fontsize": str(self.fonts.get("title", 16)),
            "bgcolor": "white",
            "pad": "0.5",
            "splines": "ortho"
        }
        
        with Diagram(title, 
                    filename=f"{self.output_dir}/png/{filename}", 
                    show=False, 
                    direction="TB",
                    graph_attr=graph_attr):
            
            # Internet y usuarios
            internet = Internet("Internet")
            users = Users("BMC Users\n10K concurrent")
            
            # AWS Cloud con VPC
            with Cluster("AWS Cloud - us-east-1", graph_attr={"bgcolor": "#E3F2FD"}):
                
                # VPC Principal
                with Cluster("VPC 10.0.0.0/16", graph_attr={"bgcolor": "#F5F5F5"}):
                    
                    # Availability Zone A
                    with Cluster("AZ us-east-1a", graph_attr={"bgcolor": "#E8F5E8"}):
                        with Cluster("Public Subnet\n10.0.1.0/24"):
                            nat_1a = ELB("NAT Gateway 1A")
                            
                        with Cluster("Private Subnet\n10.0.10.0/24"):
                            app_1a = Fargate("App Services 1A")
                            
                        with Cluster("Isolated Subnet\n10.0.20.0/24"):
                            db_1a = RDS("RDS Primary\nus-east-1a")
                    
                    # Availability Zone B  
                    with Cluster("AZ us-east-1b", graph_attr={"bgcolor": "#FFF3E0"}):
                        with Cluster("Public Subnet\n10.0.2.0/24"):
                            nat_1b = ELB("NAT Gateway 1B")
                            
                        with Cluster("Private Subnet\n10.0.11.0/24"):
                            app_1b = Fargate("App Services 1B")
                            
                        with Cluster("Isolated Subnet\n10.0.21.0/24"):
                            db_1b = RDS("RDS Standby\nus-east-1b")
                
                # Edge Services
                with Cluster("Edge Layer", graph_attr={"bgcolor": "#FFEBEE"}):
                    cloudfront = CloudFront("CloudFront CDN\nGlobal Edge")
                    waf = WAF("AWS WAF\nDDoS Protection")
                    
                # API Layer
                with Cluster("API Layer", graph_attr={"bgcolor": "#F3E5F5"}):
                    api_gateway = APIGateway("API Gateway\nREST + GraphQL")
                    cognito = Cognito("Cognito\nUser Pool")
                    alb = ELB("Application LB\nMulti-AZ")
            
            # Conexiones con estilos
            users >> Edge(**self.edge_styles["primary"]) >> internet
            internet >> Edge(**self.edge_styles["primary"]) >> cloudfront
            cloudfront >> Edge(**self.edge_styles["security"]) >> waf
            waf >> Edge(**self.edge_styles["primary"]) >> api_gateway
            api_gateway >> Edge(**self.edge_styles["secondary"]) >> cognito
            api_gateway >> Edge(**self.edge_styles["primary"]) >> alb
            
            alb >> Edge(**self.edge_styles["data"]) >> app_1a
            alb >> Edge(**self.edge_styles["data"]) >> app_1b
            
            app_1a >> Edge(**self.edge_styles["data"]) >> db_1a
            app_1b >> Edge(**self.edge_styles["data"]) >> db_1b
            db_1a >> Edge(**self.edge_styles["monitoring"]) >> db_1b
        
        return f"{self.output_dir}/png/{filename}.png"
    
    def create_microservices_diagram(self, title: str, filename: str) -> str:
        """Genera diagrama detallado de microservicios"""
        
        with Diagram(title, 
                    filename=f"{self.output_dir}/png/{filename}", 
                    show=False, 
                    direction="TB"):
            
            # API Gateway
            api_gateway = APIGateway("API Gateway\nThrottling: 1K req/s")
            
            # Application Load Balancer
            alb = ELB("Application LB\nHealth Checks")
            
            # Microservicios con configuración detallada
            microservices_config = self.config.get("microservices", {})
            
            with Cluster("ECS Fargate Cluster - Auto Scaling", graph_attr={"bgcolor": "#E8F5E8"}):
                
                # Invoice Service
                if "invoice_service" in microservices_config:
                    with Cluster("Invoice Service Pod", graph_attr={"bgcolor": "#FFF3E0"}):
                        invoice_config = microservices_config["invoice_service"]
                        scaling = invoice_config.get("scaling", {})
                        
                        invoice_alb = ELB("Invoice ALB")
                        invoice_tasks = []
                        
                        min_cap = scaling.get("min_capacity", 2)
                        for i in range(min_cap):
                            task = Fargate(f"Task {i+1}\n2vCPU/4GB\nPort: 8000")
                            invoice_tasks.append(task)
                
                # Product Service
                if "product_service" in microservices_config:
                    with Cluster("Product Service Pod - 60M Records", graph_attr={"bgcolor": "#E3F2FD"}):
                        product_config = microservices_config["product_service"]
                        
                        product_alb = ELB("Product ALB")
                        product_tasks = []
                        
                        min_cap = product_config.get("scaling", {}).get("min_capacity", 3)
                        for i in range(min_cap):
                            task = Fargate(f"Task {i+1}\n4vCPU/8GB\n<500ms lookup")
                            product_tasks.append(task)
                
                # OCR Service
                if "ocr_service" in microservices_config:
                    with Cluster("OCR Service Pod", graph_attr={"bgcolor": "#FCE4EC"}):
                        ocr_alb = ELB("OCR ALB")
                        ocr_tasks = [
                            Fargate("Task 1\n2vCPU/4GB\nTextract"),
                            Fargate("Task 2\n2vCPU/4GB\nTextract")
                        ]
            
            # Data Services con configuración
            with Cluster("Data Services - Multi-AZ", graph_attr={"bgcolor": "#F5F5F5"}):
                
                # RDS con detalles
                rds_config = self.config.get("aws_services", {}).get("rds_primary", {})
                rds_instance = rds_config.get("instance_class", "db.r6g.2xlarge")
                rds = RDS(f"RDS PostgreSQL\n{rds_instance}\nMulti-AZ\n35-day backup")
                
                # Redis con configuración
                redis_config = self.config.get("aws_services", {}).get("redis_cluster", {})
                redis_nodes = redis_config.get("cluster", {}).get("num_nodes", 3)
                redis = Elasticache(f"ElastiCache Redis\n{redis_nodes} nodes\nCluster mode")
                
                # S3 con lifecycle
                s3 = S3("S3 Documents\nIntelligent Tiering\n90d → Glacier")
            
            # AI/ML Services
            with Cluster("AI/ML Services", graph_attr={"bgcolor": "#E1F5FE"}):
                textract = Textract("Amazon Textract\n>95% accuracy\nForms + Tables")
                lambda_classifier = Lambda("Classification\nLambda")
            
            # Integration Layer
            with Cluster("Event-Driven Integration", graph_attr={"bgcolor": "#F3E5F5"}):
                eventbridge = Eventbridge("EventBridge\nCustom Bus")
                sqs_fifo = SQS("SQS FIFO\nOCR Queue\n5min visibility")
                sns = SNS("SNS Topics\nMulti-channel")
            
            # Monitoring
            with Cluster("Observability", graph_attr={"bgcolor": "#FFF8E1"}):
                cloudwatch = Cloudwatch("CloudWatch\nCustom Metrics\nAlarms")
                xray = SystemsManager("X-Ray Tracing\nService Map")
            
            # External Services
            dian_api = Internet("DIAN API\nTax Authority\n1K req/hour")
            
            # Conexiones detalladas
            api_gateway >> Edge(label="Auth", **self.edge_styles["security"]) >> alb
            
            # Microservices connections
            if 'invoice_tasks' in locals():
                alb >> Edge(label="Route", **self.edge_styles["primary"]) >> invoice_alb
                for task in invoice_tasks:
                    invoice_alb >> Edge(**self.edge_styles["data"]) >> task
                    task >> Edge(label="Events", **self.edge_styles["monitoring"]) >> eventbridge
            
            if 'product_tasks' in locals():
                alb >> Edge(label="Route", **self.edge_styles["primary"]) >> product_alb
                for task in product_tasks:
                    product_alb >> Edge(**self.edge_styles["data"]) >> task
                    task >> Edge(label="Cache", **self.edge_styles["data"]) >> redis
                
                product_tasks[0] >> Edge(label="60M lookup", **self.edge_styles["data"]) >> rds
                product_tasks[0] >> Edge(label="Classification", **self.edge_styles["secondary"]) >> dian_api
            
            if 'ocr_tasks' in locals():
                alb >> Edge(label="Route", **self.edge_styles["primary"]) >> ocr_alb
                for task in ocr_tasks:
                    ocr_alb >> Edge(**self.edge_styles["data"]) >> task
                    task >> Edge(label="Documents", **self.edge_styles["data"]) >> s3
                    task >> Edge(label="OCR >95%", **self.edge_styles["secondary"]) >> textract
            
            # Integration flows
            eventbridge >> Edge(label="Queue", **self.edge_styles["monitoring"]) >> sqs_fifo
            sqs_fifo >> Edge(label="Process", **self.edge_styles["monitoring"]) >> lambda_classifier
            lambda_classifier >> Edge(label="Notify", **self.edge_styles["monitoring"]) >> sns
            
            # Monitoring connections
            if 'invoice_tasks' in locals():
                invoice_tasks[0] >> Edge(label="Metrics", **self.edge_styles["monitoring"]) >> cloudwatch
            if 'product_tasks' in locals():
                product_tasks[0] >> Edge(label="Traces", **self.edge_styles["monitoring"]) >> cloudwatch
        
        return f"{self.output_dir}/png/{filename}.png"
    
    def create_security_diagram(self, title: str, filename: str) -> str:
        """Genera diagrama de arquitectura de seguridad"""
        
        with Diagram(title, 
                    filename=f"{self.output_dir}/png/{filename}", 
                    show=False, 
                    direction="TB"):
            
            # Usuarios y amenazas externas
            users = Users("Legitimate Users")
            attackers = Client("Potential Attackers")
            
            # Capas de seguridad
            with Cluster("Security Layers", graph_attr={"bgcolor": "#FFEBEE"}):
                
                # Edge Security
                with Cluster("Edge Security", graph_attr={"bgcolor": "#FCE4EC"}):
                    cloudfront = CloudFront("CloudFront\nSSL/TLS Termination")
                    waf = WAF("AWS WAF\nRate Limiting: 2K req/s\nGeo Blocking\nSQL Injection Protection")
                
                # Identity & Access
                with Cluster("Identity & Access Management", graph_attr={"bgcolor": "#F3E5F5"}):
                    cognito = Cognito("Cognito User Pool\nMFA: TOTP + SMS\nPassword Policy")
                    api_gateway = APIGateway("API Gateway\nJWT Validation\nAPI Keys")
                
                # Application Security
                with Cluster("Application Security", graph_attr={"bgcolor": "#E8EAF6"}):
                    fargate = Fargate("ECS Fargate\nTask Role IAM\nSecrets Manager\nVPC Endpoints")
                    secrets = SecretsManager("Secrets Manager\nDB Credentials\nAPI Keys")
                
                # Data Security
                with Cluster("Data Security", graph_attr={"bgcolor": "#E0F2F1"}):
                    kms = KMS("KMS Encryption\nCustomer Managed Keys\nAuto Rotation")
                    rds = RDS("RDS Encrypted\nAt Rest + In Transit\nSSL Certificates")
                    s3 = S3("S3 Encrypted\nBucket Policies\nAccess Logging")
                
                # Network Security
                with Cluster("Network Security", graph_attr={"bgcolor": "#FFF3E0"}):
                    vpc = VPC("VPC\nPrivate Subnets\nNACLs")
                    sg = Blank("Security Groups\nLeast Privilege\nPort Restrictions")
                
                # Monitoring & Compliance
                with Cluster("Security Monitoring", graph_attr={"bgcolor": "#F1F8E9"}):
                    cloudwatch = Cloudwatch("CloudWatch\nSecurity Logs\nAnomaly Detection")
                    cloudtrail = SystemsManager("CloudTrail\nAPI Audit Logs\nCompliance Reports")
            
            # Flujo de seguridad
            users >> Edge(label="HTTPS", **self.edge_styles["security"]) >> cloudfront
            attackers >> Edge(label="Blocked", color="red", style="dashed") >> waf
            
            cloudfront >> Edge(label="Filter", **self.edge_styles["security"]) >> waf
            waf >> Edge(label="Authenticate", **self.edge_styles["security"]) >> api_gateway
            api_gateway >> Edge(label="Authorize", **self.edge_styles["security"]) >> cognito
            api_gateway >> Edge(label="Secure", **self.edge_styles["security"]) >> fargate
            
            fargate >> Edge(label="Secrets", **self.edge_styles["data"]) >> secrets
            fargate >> Edge(label="Encrypt", **self.edge_styles["data"]) >> kms
            
            kms >> Edge(label="Protect", **self.edge_styles["data"]) >> rds
            kms >> Edge(label="Protect", **self.edge_styles["data"]) >> s3
            
            fargate >> Edge(label="Network", **self.edge_styles["monitoring"]) >> vpc
            vpc >> Edge(label="Control", **self.edge_styles["monitoring"]) >> sg
            
            [fargate, rds, s3] >> Edge(label="Audit", **self.edge_styles["monitoring"]) >> cloudwatch
            cloudwatch >> Edge(label="Compliance", **self.edge_styles["monitoring"]) >> cloudtrail
        
        return f"{self.output_dir}/png/{filename}.png"
    
    def create_data_flow_diagram(self, title: str, filename: str) -> str:
        """Genera diagrama de flujo de datos detallado"""
        
        with Diagram(title, 
                    filename=f"{self.output_dir}/png/{filename}", 
                    show=False, 
                    direction="LR"):
            
            # Input Sources
            with Cluster("Data Sources", graph_attr={"bgcolor": "#E3F2FD"}):
                user_upload = Users("User Upload\nPDF/Images\n10K files/day")
                sftp_batch = Internet("SFTP Batch\nNightly Import\n100K records")
                api_realtime = APIGateway("Real-time API\n1K req/s")
            
            # Processing Pipeline
            with Cluster("Processing Pipeline", graph_attr={"bgcolor": "#E8F5E8"}):
                
                # Ingestion Layer
                with Cluster("Ingestion"):
                    s3_raw = S3("S3 Raw Data\nMultipart Upload\nEvent Notifications")
                    sqs_processing = SQS("Processing Queue\nFIFO\n5min visibility")
                
                # Processing Layer
                with Cluster("Processing"):
                    lambda_validator = Lambda("Data Validator\n512MB\n30s timeout")
                    fargate_processor = Fargate("Batch Processor\n4vCPU/8GB\nAuto Scaling")
                    textract_ocr = Textract("Textract OCR\n>95% accuracy\nAsync processing")
                
                # Classification Layer
                with Cluster("Classification"):
                    lambda_classifier = Lambda("ML Classifier\n1GB\nSageMaker endpoint")
                    product_matcher = Fargate("Product Matcher\n60M products\n<500ms")
            
            # Storage Layer
            with Cluster("Storage Layer", graph_attr={"bgcolor": "#FFF3E0"}):
                
                # Hot Data
                with Cluster("Hot Data (Real-time)"):
                    redis_cache = Elasticache("Redis Cache\n24h TTL\n>95% hit ratio")
                    rds_primary = RDS("RDS Primary\nPostgreSQL 14\nRead/Write")
                
                # Warm Data
                with Cluster("Warm Data (Operational)"):
                    rds_replica = RDS("Read Replica\nCross-AZ\nRead-only")
                    s3_processed = S3("S3 Processed\nParquet format\nPartitioned")
                
                # Cold Data
                with Cluster("Cold Data (Archive)"):
                    s3_glacier = S3("S3 Glacier\n7-year retention\nCompliance")
                    redshift = Redshift("Redshift\nData Warehouse\nBI Analytics")
            
            # Output Layer
            with Cluster("Output Layer", graph_attr={"bgcolor": "#FCE4EC"}):
                api_response = APIGateway("API Response\nJSON/XML\nCached")
                report_generator = Lambda("Report Generator\nPDF/Excel\nScheduled")
                notification_system = SNS("Notifications\nEmail/SMS/Webhook")
            
            # External Systems
            with Cluster("External Integration", graph_attr={"bgcolor": "#F3E5F5"}):
                dian_api = Internet("DIAN API\nTax validation\n1K req/hour")
                erp_system = Internet("ERP Systems\nSAP/Oracle\nReal-time sync")
            
            # Data Flow Connections
            user_upload >> Edge(label="Upload", **self.edge_styles["primary"]) >> s3_raw
            sftp_batch >> Edge(label="Batch", **self.edge_styles["data"]) >> s3_raw
            api_realtime >> Edge(label="Stream", **self.edge_styles["primary"]) >> sqs_processing
            
            s3_raw >> Edge(label="Trigger", **self.edge_styles["monitoring"]) >> lambda_validator
            sqs_processing >> Edge(label="Process", **self.edge_styles["data"]) >> fargate_processor
            
            lambda_validator >> Edge(label="OCR", **self.edge_styles["secondary"]) >> textract_ocr
            fargate_processor >> Edge(label="Classify", **self.edge_styles["secondary"]) >> lambda_classifier
            
            lambda_classifier >> Edge(label="Match", **self.edge_styles["data"]) >> product_matcher
            product_matcher >> Edge(label="Cache", **self.edge_styles["data"]) >> redis_cache
            
            redis_cache >> Edge(label="Persist", **self.edge_styles["data"]) >> rds_primary
            rds_primary >> Edge(label="Replicate", **self.edge_styles["monitoring"]) >> rds_replica
            
            textract_ocr >> Edge(label="Store", **self.edge_styles["data"]) >> s3_processed
            s3_processed >> Edge(label="Archive", **self.edge_styles["monitoring"]) >> s3_glacier
            
            rds_replica >> Edge(label="ETL", **self.edge_styles["data"]) >> redshift
            
            # Output flows
            redis_cache >> Edge(label="Serve", **self.edge_styles["primary"]) >> api_response
            redshift >> Edge(label="Reports", **self.edge_styles["secondary"]) >> report_generator
            
            # External integrations
            product_matcher >> Edge(label="Validate", **self.edge_styles["secondary"]) >> dian_api
            rds_primary >> Edge(label="Sync", **self.edge_styles["data"]) >> erp_system
            
            # Notifications
            [lambda_validator, fargate_processor] >> Edge(label="Alert", **self.edge_styles["monitoring"]) >> notification_system
        
        return f"{self.output_dir}/png/{filename}.png"
    
    def generate_all_refined(self, project_name: str = "BMC") -> Dict[str, str]:
        """Genera todos los diagramas refinados PNG y Draw.io"""
        
        # Crear directorios
        os.makedirs(f"{self.output_dir}/png", exist_ok=True)
        os.makedirs(f"{self.output_dir}/drawio", exist_ok=True)
        
        results = {}
        
        print("🎨 Generating refined diagrams...")
        
        # Diagramas PNG
        results["network"] = self.create_network_diagram(
            f"{project_name} - Network Architecture & VPC",
            f"{project_name.lower()}_network_architecture"
        )
        print("✓ Network architecture diagram generated")
        
        results["microservices"] = self.create_microservices_diagram(
            f"{project_name} - Microservices Architecture",
            f"{project_name.lower()}_microservices_detailed"
        )
        print("✓ Microservices detailed diagram generated")
        
        results["security"] = self.create_security_diagram(
            f"{project_name} - Security Architecture",
            f"{project_name.lower()}_security_architecture"
        )
        print("✓ Security architecture diagram generated")
        
        results["data_flow"] = self.create_data_flow_diagram(
            f"{project_name} - Data Flow Architecture",
            f"{project_name.lower()}_data_flow"
        )
        print("✓ Data flow diagram generated")
        
        # Generar archivos Draw.io profesionales
        from .professional_drawio_generator import ProfessionalDrawioGenerator
        drawio_generator = ProfessionalDrawioGenerator(self.config, self.output_dir)
        
        # Generar Draw.io profesional completo
        professional_drawio = drawio_generator.generate_professional_architecture(project_name)
        results["drawio_professional"] = professional_drawio
        
        print("✓ Professional Draw.io generated")
        
        return results
