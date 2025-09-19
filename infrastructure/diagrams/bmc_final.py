#!/usr/bin/env python3
"""
BMC AWS Architecture Diagram Generator - Final Version
Generates PNG diagrams with available AWS icons
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Fargate, Lambda
from diagrams.aws.database import RDS, Redshift, Elasticache
from diagrams.aws.storage import S3
from diagrams.aws.network import APIGateway, CloudFront, ELB
from diagrams.aws.security import Cognito, WAF
from diagrams.aws.integration import SQS, SNS
from diagrams.aws.ml import Textract
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.client import Users
from diagrams.onprem.network import Internet

def generate_main_architecture():
    """Generate main BMC architecture diagram"""
    
    with Diagram("BMC AWS Architecture - 60M Products Platform", 
                 filename="bmc_main_architecture", 
                 show=False, 
                 direction="TB"):
        
        # Users
        users = Users("BMC Users")
        external = Users("External Systems")
        
        with Cluster("AWS Cloud"):
            # Edge Layer
            with Cluster("Edge & Security"):
                cloudfront = CloudFront("CloudFront CDN")
                waf = WAF("AWS WAF")
                
            # API Layer
            with Cluster("API Gateway"):
                api_gateway = APIGateway("API Gateway")
                cognito = Cognito("User Auth")
                
            # Load Balancing
            alb = ELB("Application LB")
                
            # Compute Layer
            with Cluster("Microservices (ECS Fargate)"):
                invoice_service = Fargate("Invoice Service\n2 vCPU, 4GB")
                product_service = Fargate("Product Service\n4 vCPU, 8GB\n60M Products")
                ocr_service = Fargate("OCR Service\n2 vCPU, 4GB")
                commission_service = Fargate("Commission Service\n1 vCPU, 2GB")
                certificate_service = Fargate("Certificate Service\n1 vCPU, 2GB")
            
            # Serverless Functions
            with Cluster("Lambda Functions"):
                ocr_processor = Lambda("OCR Processor")
                data_validator = Lambda("Data Validator")
                pdf_generator = Lambda("PDF Generator")
                
            # AI/ML Services
            textract = Textract("Amazon Textract\nOCR >95%")
                
            # Data Layer
            with Cluster("Data Layer"):
                rds_primary = RDS("RDS PostgreSQL\n60M Products\nMulti-AZ")
                rds_replica = RDS("Read Replica\nQuery Optimization")
                redis = Elasticache("ElastiCache Redis\nProduct Cache\n24h TTL")
                redshift = Redshift("Redshift\nData Warehouse")
                s3_docs = S3("S3 Documents\nIntelligent Tiering")
                s3_backup = S3("S3 Backup\nCross-Region")
                    
            # Integration Layer
            with Cluster("Event-Driven Integration"):
                sqs_fifo = SQS("SQS FIFO\nInvoice Queue")
                sqs_standard = SQS("SQS Standard\nOCR Queue")
                sns = SNS("SNS\nNotifications")
                
            # Monitoring
            cloudwatch = Cloudwatch("CloudWatch\nMetrics & Logs")
        
        # External Services
        dian_api = Internet("DIAN API\nTax Authority")
        email_service = Internet("Email Service\nSES/SMTP")
        
        # User flows
        users >> cloudfront >> waf >> api_gateway
        external >> s3_docs
        
        # API Gateway flows
        api_gateway >> cognito
        api_gateway >> alb
        
        # Load balancer to services
        alb >> invoice_service
        alb >> product_service
        alb >> ocr_service
        alb >> commission_service
        alb >> certificate_service
        
        # Service interactions
        invoice_service >> ocr_processor >> textract
        product_service >> redis >> rds_primary
        ocr_service >> s3_docs
        commission_service >> pdf_generator
        
        # Event flows
        invoice_service >> sqs_fifo
        invoice_service >> sqs_standard
        invoice_service >> sns
        
        # Data flows
        rds_primary >> rds_replica
        product_service >> redshift
        s3_docs >> s3_backup
        
        # External integrations
        product_service >> dian_api
        sns >> email_service
        
        # Monitoring
        invoice_service >> cloudwatch
        product_service >> cloudwatch
        ocr_service >> cloudwatch

def generate_microservices_detail():
    """Generate detailed microservices architecture"""
    
    with Diagram("BMC Microservices Architecture - ECS Fargate", 
                 filename="bmc_microservices_detail", 
                 show=False, 
                 direction="TB"):
        
        api_gateway = APIGateway("API Gateway\nCentral Router")
            
        with Cluster("ECS Fargate Cluster"):
            with Cluster("Invoice Service Pod"):
                invoice_alb = ELB("Invoice ALB")
                invoice_task1 = Fargate("Invoice Task 1\n2 vCPU, 4GB")
                invoice_task2 = Fargate("Invoice Task 2\n2 vCPU, 4GB")
                
            with Cluster("Product Service Pod (60M Records)"):
                product_alb = ELB("Product ALB")
                product_task1 = Fargate("Product Task 1\n4 vCPU, 8GB")
                product_task2 = Fargate("Product Task 2\n4 vCPU, 8GB")
                product_task3 = Fargate("Product Task 3\n4 vCPU, 8GB")
                
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
        
        # API Gateway routing
        api_gateway >> invoice_alb
        api_gateway >> product_alb
        api_gateway >> ocr_alb
        
        # Load balancer to tasks
        invoice_alb >> invoice_task1
        invoice_alb >> invoice_task2
        product_alb >> product_task1
        product_alb >> product_task2
        product_alb >> product_task3
        ocr_alb >> ocr_task1
        ocr_alb >> ocr_task2
        
        # Data connections
        invoice_task1 >> rds
        invoice_task2 >> rds
        product_task1 >> rds
        product_task1 >> redis
        product_task2 >> rds
        product_task2 >> redis
        product_task3 >> rds
        product_task3 >> redis
        ocr_task1 >> s3
        ocr_task1 >> textract
        ocr_task2 >> s3
        ocr_task2 >> textract
        
        # Event flows
        invoice_task1 >> sqs
        invoice_task2 >> sqs

def generate_data_flow():
    """Generate data flow diagram"""
    
    with Diagram("BMC Data Flow - 60M Products Processing", 
                 filename="bmc_data_flow", 
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
        email = Internet("Email\nDelivery")
        
        # Flow
        user_upload >> api_gateway >> invoice_service
        invoice_service >> s3_raw >> ocr_processor >> textract
        textract >> product_service >> redis
        product_service >> rds >> dian_api
        invoice_service >> sqs >> sns >> email
        textract >> s3_processed

def generate_security_architecture():
    """Generate security architecture"""
    
    with Diagram("BMC Security Architecture", 
                 filename="bmc_security_architecture", 
                 show=False, 
                 direction="TB"):
        
        users = Users("Users")
        
        with Cluster("Security Layers"):
            with Cluster("Edge Security"):
                cloudfront = CloudFront("CloudFront")
                waf = WAF("AWS WAF")
                
            with Cluster("Identity & Access"):
                cognito = Cognito("Cognito")
                
            with Cluster("Application Security"):
                api_gateway = APIGateway("API Gateway")
                fargate = Fargate("ECS Fargate\nSecure Containers")
                
            with Cluster("Data Security"):
                rds = RDS("RDS Encrypted")
                s3 = S3("S3 Encrypted")
                
            with Cluster("Monitoring"):
                cloudwatch = Cloudwatch("CloudWatch\nSecurity Logs")
        
        # Security flow
        users >> cloudfront >> waf >> api_gateway >> cognito
        api_gateway >> fargate
        fargate >> rds
        fargate >> s3
        fargate >> cloudwatch

if __name__ == "__main__":
    print("Generating BMC AWS Architecture Diagrams...")
    
    # Generate all diagrams
    generate_main_architecture()
    print("✓ Main architecture diagram generated")
    
    generate_microservices_detail()
    print("✓ Microservices detail diagram generated")
    
    generate_data_flow()
    print("✓ Data flow diagram generated")
    
    generate_security_architecture()
    print("✓ Security architecture diagram generated")
    
    print("\nAll diagrams generated successfully!")
    print("Files created:")
    print("- bmc_main_architecture.png")
    print("- bmc_microservices_detail.png")
    print("- bmc_data_flow.png")
    print("- bmc_security_architecture.png")
