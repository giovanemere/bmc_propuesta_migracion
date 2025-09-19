#!/usr/bin/env python3
"""
Convertidor de Diagramas Mermaid a Python - Versión Corregida
"""

from diagrams import Diagram, Cluster
from diagrams.aws.compute import Fargate, Lambda
from diagrams.aws.database import RDS, Redshift, Elasticache
from diagrams.aws.storage import S3
from diagrams.aws.network import APIGateway, CloudFront, ELB
from diagrams.aws.security import Cognito, WAF
from diagrams.aws.integration import SQS, SNS
from diagrams.aws.ml import Textract, Comprehend
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.client import Users
from diagrams.onprem.network import Internet

def generate_main_architecture():
    """Diagrama 1: Arquitectura General AWS (del Mermaid)"""
    
    with Diagram("BMC Arquitectura General AWS", 
                 filename="bmc_arquitectura_general", 
                 show=False, 
                 direction="TB"):
        
        # Internet (equivalente al subgraph Internet del Mermaid)
        with Cluster("Internet"):
            users = Users("Usuarios BMC")
            external = Users("Sistemas Externos")
        
        # AWS Cloud (equivalente al subgraph AWS Cloud del Mermaid)
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
                sqs = SQS("SQS\nMessage Queue")
                sns = SNS("SNS\nNotifications")
            
            # AI/ML Services
            with Cluster("AI/ML Services"):
                textract = Textract("Textract\nOCR Service")
                comprehend = Comprehend("Comprehend\nNLP Analysis")
            
            # Monitoring
            cloudwatch = Cloudwatch("CloudWatch\nMonitoring")
        
        # External Services
        dian_api = Internet("DIAN API\nTax Authority")
        
        # Flujo principal (similar al Mermaid)
        users >> cloudfront >> waf >> api_gateway
        api_gateway >> cognito
        api_gateway >> alb >> ecs
        
        ecs >> lambda_func >> textract
        ecs >> elasticache >> rds
        ecs >> s3
        ecs >> sqs >> sns
        ecs >> dian_api
        
        [ecs, lambda_func] >> cloudwatch
        rds >> redshift

def generate_microservices_detail():
    """Diagrama 2: Microservicios ECS Fargate (del Mermaid)"""
    
    with Diagram("BMC Microservicios ECS Fargate", 
                 filename="bmc_microservicios_detalle", 
                 show=False, 
                 direction="TB"):
        
        api_gateway = APIGateway("API Gateway\nCentral Router")
        
        with Cluster("ECS Fargate Cluster"):
            # Invoice Service Pod
            with Cluster("Invoice Service Pod"):
                invoice_alb = ELB("Invoice ALB")
                invoice_task1 = Fargate("Invoice Task 1\n2 vCPU, 4GB")
                invoice_task2 = Fargate("Invoice Task 2\n2 vCPU, 4GB")
            
            # Product Service Pod (60M Records)
            with Cluster("Product Service Pod (60M Records)"):
                product_alb = ELB("Product ALB")
                product_task1 = Fargate("Product Task 1\n4 vCPU, 8GB")
                product_task2 = Fargate("Product Task 2\n4 vCPU, 8GB")
                product_task3 = Fargate("Product Task 3\n4 vCPU, 8GB")
            
            # OCR Service Pod
            with Cluster("OCR Service Pod"):
                ocr_alb = ELB("OCR ALB")
                ocr_task1 = Fargate("OCR Task 1\n2 vCPU, 4GB")
                ocr_task2 = Fargate("OCR Task 2\n2 vCPU, 4GB")
        
        with Cluster("Data Services"):
            rds = RDS("RDS PostgreSQL\nMulti-AZ\n60M Products")
            redis = Elasticache("ElastiCache Redis\nCluster Mode")
            s3 = S3("S3 Buckets\nDocuments")
        
        textract = Textract("Amazon Textract\nOCR Processing")
        sqs = SQS("SQS Queues\nFIFO & Standard")
        
        # Conexiones (similar al flujo del Mermaid)
        api_gateway >> [invoice_alb, product_alb, ocr_alb]
        
        invoice_alb >> [invoice_task1, invoice_task2]
        product_alb >> [product_task1, product_task2, product_task3]
        ocr_alb >> [ocr_task1, ocr_task2]
        
        [invoice_task1, invoice_task2] >> rds
        [product_task1, product_task2, product_task3] >> redis
        product_task1 >> rds
        [ocr_task1, ocr_task2] >> [s3, textract]
        
        invoice_task1 >> sqs

def generate_data_flow():
    """Diagrama 3: Flujo de Datos (basado en el Mermaid)"""
    
    with Diagram("BMC Flujo de Datos - 60M Productos", 
                 filename="bmc_flujo_datos", 
                 show=False, 
                 direction="LR"):
        
        # Input
        user_upload = Users("User Upload\nPDF/Image")
        
        # Processing Pipeline
        with Cluster("Processing Pipeline"):
            api_gateway = APIGateway("API Gateway")
            invoice_service = Fargate("Invoice Service")
            ocr_processor = Lambda("OCR Processor")
            textract = Textract("Textract\n>95% Accuracy")
            product_service = Fargate("Product Service\n60M Lookup")
        
        # Data Storage
        with Cluster("Data Storage"):
            s3_raw = S3("S3 Raw\nDocuments")
            s3_processed = S3("S3 Processed\nResults")
            rds = RDS("PostgreSQL\n60M Products")
            redis = Elasticache("Redis Cache\n24h TTL")
        
        # Events & Notifications
        sqs = SQS("SQS Queue\nProcessing")
        sns = SNS("SNS\nNotifications")
        
        # External
        dian_api = Internet("DIAN API\nClassification")
        
        # Flow (similar al sequence del Mermaid)
        user_upload >> api_gateway >> invoice_service
        invoice_service >> s3_raw >> ocr_processor >> textract
        textract >> product_service >> redis
        product_service >> rds >> dian_api
        invoice_service >> sqs >> sns
        textract >> s3_processed

def main():
    print("🚀 Convertidor Mermaid a Python Diagrams")
    print("=" * 45)
    print("📄 Basado en: /home/giovanemere/Migracion/diagramas-aws-mermaid.md")
    print()
    
    print("📊 Generando diagramas...")
    
    # Generar cada diagrama
    generate_main_architecture()
    print("✓ Arquitectura General AWS generada")
    
    generate_microservices_detail()
    print("✓ Microservicios ECS Fargate generado")
    
    generate_data_flow()
    print("✓ Flujo de Datos generado")
    
    print("\n✅ Conversión completada!")
    print("\n📁 Archivos PNG generados:")
    print("- bmc_arquitectura_general.png")
    print("- bmc_microservicios_detalle.png")
    print("- bmc_flujo_datos.png")
    
    print("\n💡 Cómo se hizo la conversión:")
    print("1. Leí los diagramas Mermaid del archivo .md")
    print("2. Convertí cada 'subgraph' a 'Cluster' de Python")
    print("3. Convertí cada nodo a su equivalente AWS icon")
    print("4. Mantuve las conexiones y flujos originales")
    print("5. Generé PNG con iconos oficiales de AWS")
    
    print("\n🔄 Para actualizar:")
    print("1. Modifica este script según cambios en el Mermaid")
    print("2. Ejecuta: python3 mermaid_converter_fixed.py")
    print("3. Los PNG se actualizan automáticamente")

if __name__ == "__main__":
    main()
