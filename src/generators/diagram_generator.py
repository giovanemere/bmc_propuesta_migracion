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
        """Genera diagrama de flujo de datos nivel AWS Senior Architect"""
        
        filename = os.path.join(self.output_dir, "data_flow")
        
        with Diagram("BMC Data Flow Architecture - Senior Level", 
                    show=False, 
                    filename=filename,
                    direction="TB"):
            
            # External Data Sources - Detailed
            with Cluster("External Data Sources"):
                with Cluster("User Channels"):
                    web_upload = Users("Web Portal\n10K users/day\nMax 50MB/file")
                    mobile_app = Users("Mobile App\nReal-time upload\nImage compression")
                    api_clients = APIGateway("API Clients\n1K req/s\nRate limited")
                
                with Cluster("B2B Integration"):
                    sftp_server = Internet("SFTP Server\nScheduled: 02:00 UTC\n100K records/batch")
                    partner_apis = Internet("Partner APIs\nWebhooks\nOAuth 2.0")
                    erp_systems = Internet("ERP Systems\nSAP/Oracle\nReal-time CDC")
            
            # Ingestion Layer - Enterprise Grade
            with Cluster("Ingestion Layer - Multi-AZ"):
                with Cluster("API Gateway Tier"):
                    api_gw_main = APIGateway("API Gateway\n10K req/s throttle\nCaching: 300s TTL")
                    api_gw_auth = Cognito("Cognito\nJWT validation\nMFA enabled")
                
                with Cluster("Load Balancing"):
                    alb_ingestion = ELB("ALB Ingestion\nSticky sessions\nHealth checks")
                    nlb_sftp = ELB("NLB SFTP\nTCP load balancing\nCross-zone enabled")
                
                with Cluster("Initial Storage"):
                    s3_raw_landing = S3("S3 Raw Landing\nMultipart upload\nEvent notifications\nLifecycle: 30d")
                    s3_quarantine = S3("S3 Quarantine\nFailed uploads\nManual review")
            
            # Processing Pipeline - Microservices
            with Cluster("Processing Pipeline - Event-Driven"):
                with Cluster("Validation Layer"):
                    lambda_validator = Lambda("File Validator\n1GB memory\n15min timeout\nDLQ enabled")
                    lambda_virus_scan = Lambda("Virus Scanner\nClamAV integration\nQuarantine on detect")
                    sqs_validation = SQS("Validation Queue\nFIFO\n5min visibility\n3 retries")
                
                with Cluster("OCR Processing"):
                    fargate_ocr = Fargate("OCR Service\n4vCPU/8GB\nAuto scaling 2-20\nSpot instances")
                    textract_async = Textract("Textract Async\n>95% accuracy\nForms + Tables\nHandwriting")
                    comprehend_nlp = Comprehend("Comprehend\nEntity extraction\nSentiment analysis")
                
                with Cluster("Business Logic"):
                    fargate_invoice = Fargate("Invoice Service\n2vCPU/4GB\nBlue/Green deploy\nCircuit breaker")
                    fargate_product = Fargate("Product Service\n4vCPU/8GB\n60M products\nElastic search")
                    fargate_commission = Fargate("Commission Service\n2vCPU/4GB\nDIAN compliance\nAudit trail")
            
            # Data Storage - Multi-Tier
            with Cluster("Data Storage - Multi-Tier Architecture"):
                with Cluster("Hot Data (< 1 day)"):
                    redis_cluster = Elasticache("Redis Cluster\n6 nodes\nMulti-AZ\n99.9% availability")
                    rds_primary = RDS("RDS Primary\nPostgreSQL 14\ndb.r6g.2xlarge\n35-day backup")
                
                with Cluster("Warm Data (1-90 days)"):
                    rds_replica_1 = RDS("Read Replica AZ-1\nCross-AZ\nRead scaling")
                    rds_replica_2 = RDS("Read Replica AZ-2\nDisaster recovery\nPromotion ready")
                    s3_processed = S3("S3 Processed\nParquet format\nPartitioned by date\nCompression: GZIP")
                
                with Cluster("Cold Data (> 90 days)"):
                    s3_glacier = S3("S3 Glacier\n7-year retention\nCompliance archive\nRestore: 12h")
                    redshift_dw = Redshift("Redshift DW\ndc2.large x3\nColumnar storage\nBI analytics")
            
            # Output & Integration
            with Cluster("Output & Integration Layer"):
                with Cluster("Real-time APIs"):
                    api_gw_output = APIGateway("Output API\nCached responses\nRate limiting\nAPI keys")
                    lambda_formatter = Lambda("Response Formatter\nJSON/XML/CSV\nSchema validation")
                
                with Cluster("Batch Processing"):
                    fargate_reports = Fargate("Report Generator\n2vCPU/4GB\nScheduled jobs\nPDF/Excel output")
                    s3_reports = S3("S3 Reports\nGenerated files\nPre-signed URLs\n7-day expiry")
                
                with Cluster("Notifications"):
                    sns_topics = SNS("SNS Topics\nMulti-protocol\nDLQ enabled\nRetry policy")
                    sqs_notifications = SQS("Notification Queue\nEmail/SMS/Webhook\nBatch processing")
            
            # External Integrations
            with Cluster("External Integrations"):
                dian_api = Internet("DIAN API\nTax validation\n1K req/hour\nCircuit breaker")
                email_service = SNS("SES Email\n50K emails/day\nBounce handling\nReputation monitoring")
                webhook_clients = Internet("Webhook Clients\nAsync delivery\nRetry logic\nSecurity headers")
            
            # Data Flow Connections - Detailed
            # Ingestion flows
            [web_upload, mobile_app] >> api_gw_main >> api_gw_auth >> alb_ingestion
            api_clients >> api_gw_main
            [sftp_server, partner_apis] >> nlb_sftp
            erp_systems >> api_gw_main
            
            # Storage flows
            alb_ingestion >> s3_raw_landing
            nlb_sftp >> s3_raw_landing
            
            # Processing flows
            s3_raw_landing >> lambda_validator >> sqs_validation
            lambda_validator >> lambda_virus_scan
            lambda_virus_scan >> s3_quarantine  # On virus detection
            
            sqs_validation >> fargate_ocr >> textract_async
            textract_async >> comprehend_nlp
            comprehend_nlp >> fargate_invoice
            
            fargate_invoice >> fargate_product >> fargate_commission
            
            # Data persistence flows
            [fargate_invoice, fargate_product, fargate_commission] >> redis_cluster
            redis_cluster >> rds_primary
            rds_primary >> [rds_replica_1, rds_replica_2]
            
            # Analytics flows
            rds_primary >> s3_processed
            s3_processed >> s3_glacier
            s3_processed >> redshift_dw
            
            # Output flows
            redis_cluster >> api_gw_output >> lambda_formatter
            redshift_dw >> fargate_reports >> s3_reports
            
            # Notification flows
            [fargate_invoice, fargate_commission] >> sns_topics >> sqs_notifications
            sqs_notifications >> email_service
            sqs_notifications >> webhook_clients
            
            # External integration flows
            fargate_product >> dian_api
            fargate_commission >> dian_api
        
        png_path = f"{filename}.png"
        print(f"✅ Senior-Level Data Flow PNG generado: {png_path}")
        return png_path

# Alias para compatibilidad
DiagramGenerator = RefinedDiagramGenerator
