#!/usr/bin/env python3
"""
Convertidor de Diagramas Mermaid a Python Diagrams
Convierte los diagramas del archivo diagramas-aws-mermaid.md a PNG usando Python
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import ECS, Lambda, Fargate
from diagrams.aws.database import RDS, Redshift, Elasticache
from diagrams.aws.storage import S3
from diagrams.aws.network import APIGateway, CloudFront, ELB
from diagrams.aws.security import Cognito, WAF
from diagrams.aws.integration import SQS, SNS
from diagrams.aws.ml import Textract, Comprehend
from diagrams.aws.management import Cloudwatch
from diagrams.aws.migration import TransferFamily
from diagrams.onprem.client import Users
from diagrams.onprem.network import Internet

def generate_main_architecture():
    """Genera el diagrama principal de arquitectura AWS"""
    
    with Diagram("BMC Arquitectura General AWS", 
                 filename="bmc_arquitectura_general", 
                 show=False, 
                 direction="TB"):
        
        # Internet
        with Cluster("Internet"):
            users = Users("Usuarios BMC")
            external = Users("Sistemas Externos")
        
        # AWS Cloud
        with Cluster("AWS Cloud"):
            # Security & Access
            with Cluster("Security & Access"):
                cloudfront = CloudFront("CloudFront\nCDN")
                waf = WAF("AWS WAF\nWeb Firewall")
                cognito = Cognito("Cognito\nAuthentication")
            
            # API Layer
            with Cluster("API Layer"):
                alb = ELB("Application\nLoad Balancer")
                api_gateway = APIGateway("API Gateway\nREST/GraphQL")
            
            # Compute Layer
            with Cluster("Compute Layer"):
                ecs = Fargate("ECS Fargate\nMicroservices")
                lambda_func = Lambda("Lambda\nServerless Functions")
            
            # Data Layer
            with Cluster("Data Layer"):
                rds = RDS("RDS PostgreSQL\n60M Products")
                redshift = Redshift("Redshift\nAnalytics")
                elasticache = Elasticache("ElastiCache\nRedis Cache")
                s3 = S3("S3\nDocument Storage")
            
            # Integration Layer
            with Cluster("Integration Layer"):
                eventbridge = Lambda("EventBridge\nEvent Bus")  # No hay EventBridge específico
                sqs = SQS("SQS\nMessage Queue")
                sns = SNS("SNS\nNotifications")
                transfer_family = TransferFamily("Transfer Family\nSFTP Gateway")
            
            # AI/ML Services
            with Cluster("AI/ML Services"):
                textract = Textract("Textract\nOCR Service")
                comprehend = Comprehend("Comprehend\nNLP Analysis")
            
            # Monitoring
            cloudwatch = Cloudwatch("CloudWatch\nMonitoring")
        
        # External Services
        dian_api = Internet("DIAN API\nTax Authority")
        email_service = Internet("Email Service\nSES/SMTP")
        
        # Conexiones principales
        users >> cloudfront >> waf >> api_gateway
        external >> transfer_family
        
        api_gateway >> cognito
        api_gateway >> alb >> ecs
        
        ecs >> lambda_func >> textract
        ecs >> elasticache >> rds
        ecs >> s3
        
        ecs >> eventbridge >> [sqs, sns]
        ecs >> dian_api
        sns >> email_service
        
        [ecs, lambda_func] >> cloudwatch
        rds >> redshift

def generate_microservices_detail():
    """Genera el diagrama detallado de microservicios"""
    
    with Diagram("BMC Microservicios ECS Fargate", 
                 filename="bmc_microservicios_detalle", 
                 show=False, 
                 direction="TB"):
        
        api_gateway = APIGateway("API Gateway\nCentral Router")
        
        with Cluster("ECS Fargate Cluster"):
            # Invoice Service
            with Cluster("Invoice Service"):
                invoice_alb = ELB("Invoice ALB")
                invoice_tasks = [
                    Fargate("Invoice Task 1\n2 vCPU, 4GB"),
                    Fargate("Invoice Task 2\n2 vCPU, 4GB")
                ]
            
            # Product Service
            with Cluster("Product Service (60M)"):
                product_alb = ELB("Product ALB")
                product_tasks = [
                    Fargate("Product Task 1\n4 vCPU, 8GB"),
                    Fargate("Product Task 2\n4 vCPU, 8GB"),
                    Fargate("Product Task 3\n4 vCPU, 8GB")
                ]
            
            # OCR Service
            with Cluster("OCR Service"):
                ocr_alb = ELB("OCR ALB")
                ocr_tasks = [
                    Fargate("OCR Task 1\n2 vCPU, 4GB"),
                    Fargate("OCR Task 2\n2 vCPU, 4GB")
                ]
        
        with Cluster("Data Services"):
            rds = RDS("RDS PostgreSQL\nMulti-AZ\n60M Products")
            redis = Elasticache("ElastiCache Redis\nCluster Mode")
            s3 = S3("S3 Buckets\nDocuments")
        
        textract = Textract("Amazon Textract\nOCR Processing")
        sqs = SQS("SQS Queues\nFIFO & Standard")
        
        # Conexiones
        api_gateway >> [invoice_alb, product_alb, ocr_alb]
        
        invoice_alb >> invoice_tasks
        product_alb >> product_tasks
        ocr_alb >> ocr_tasks
        
        invoice_tasks >> rds
        product_tasks >> [rds, redis]
        ocr_tasks >> [s3, textract]
        
        invoice_tasks >> sqs

def generate_data_architecture():
    """Genera el diagrama de arquitectura de datos"""
    
    with Diagram("BMC Arquitectura de Datos Multi-Tier", 
                 filename="bmc_arquitectura_datos", 
                 show=False, 
                 direction="TB"):
        
        # Application Layer
        with Cluster("Application Layer"):
            web_app = Users("Web App\nReact SPA")
            mobile_app = Users("Mobile App\nReact Native")
            admin_portal = Users("Admin Portal\nManagement UI")
        
        # API Layer
        api_gateway = APIGateway("API Gateway\nREST Endpoints")
        
        # Business Logic
        with Cluster("Business Logic"):
            product_service = Fargate("Product Service\n60M Records Lookup")
            invoice_service = Fargate("Invoice Service\nDocument Processing")
            commission_service = Fargate("Commission Service\nBusiness Rules")
        
        # Hot Data (Real-time)
        with Cluster("Hot Data (Real-time)"):
            redis = Elasticache("ElastiCache Redis\nProduct Cache\nTTL: 24h")
            rds_primary = RDS("RDS Primary\nPostgreSQL 14\nMulti-AZ")
        
        # Warm Data (Operational)
        with Cluster("Warm Data (Operational)"):
            rds_replica = RDS("RDS Read Replica\nQuery Optimization\nCross-AZ")
            s3_intelligent = S3("S3 Intelligent Tiering\nDocument Storage\nAuto-archiving")
        
        # Cold Data (Analytics)
        with Cluster("Cold Data (Analytics)"):
            redshift = Redshift("Redshift Cluster\nData Warehouse\nColumnar Storage")
            s3_glacier = S3("S3 Glacier\nLong-term Archive\n7-year retention")
        
        # Conexiones
        [web_app, mobile_app, admin_portal] >> api_gateway
        api_gateway >> [product_service, invoice_service, commission_service]
        
        product_service >> redis >> rds_primary
        invoice_service >> rds_primary
        commission_service >> rds_replica
        
        rds_primary >> rds_replica
        invoice_service >> s3_intelligent
        s3_intelligent >> s3_glacier
        rds_primary >> redshift

def generate_security_architecture():
    """Genera el diagrama de arquitectura de seguridad"""
    
    with Diagram("BMC Seguridad y Compliance", 
                 filename="bmc_seguridad_arquitectura", 
                 show=False, 
                 direction="TB"):
        
        users = Users("Users")
        
        with Cluster("Security Layers"):
            # Edge Security
            with Cluster("Edge Security"):
                cloudfront = CloudFront("CloudFront")
                waf = WAF("AWS WAF")
            
            # Identity & Access
            with Cluster("Identity & Access"):
                cognito = Cognito("Cognito")
            
            # Application Security
            with Cluster("Application Security"):
                api_gateway = APIGateway("API Gateway")
                fargate = Fargate("ECS Fargate\nSecure Containers")
            
            # Data Security
            with Cluster("Data Security"):
                rds = RDS("RDS Encrypted")
                s3 = S3("S3 Encrypted")
            
            # Monitoring
            cloudwatch = Cloudwatch("CloudWatch\nSecurity Logs")
        
        # Security flow
        users >> cloudfront >> waf >> api_gateway >> cognito
        api_gateway >> fargate
        fargate >> [rds, s3]
        fargate >> cloudwatch

def main():
    print("🚀 Generando Diagramas BMC desde Mermaid a Python")
    print("=" * 55)
    
    print("📊 Generando diagrama de arquitectura general...")
    generate_main_architecture()
    print("✓ bmc_arquitectura_general.png generado")
    
    print("📊 Generando diagrama de microservicios...")
    generate_microservices_detail()
    print("✓ bmc_microservicios_detalle.png generado")
    
    print("📊 Generando diagrama de arquitectura de datos...")
    generate_data_architecture()
    print("✓ bmc_arquitectura_datos.png generado")
    
    print("📊 Generando diagrama de seguridad...")
    generate_security_architecture()
    print("✓ bmc_seguridad_arquitectura.png generado")
    
    print("\n✅ Todos los diagramas generados exitosamente!")
    print("\n📁 Archivos PNG creados:")
    print("- bmc_arquitectura_general.png")
    print("- bmc_microservicios_detalle.png") 
    print("- bmc_arquitectura_datos.png")
    print("- bmc_seguridad_arquitectura.png")
    
    print("\n💡 Cómo usar:")
    print("1. Los diagramas están basados en diagramas-aws-mermaid.md")
    print("2. Usa iconos oficiales de AWS")
    print("3. Formato PNG listo para presentaciones")
    print("4. Estructura similar a los diagramas Mermaid originales")

if __name__ == "__main__":
    main()
