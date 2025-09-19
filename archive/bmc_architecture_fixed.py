#!/usr/bin/env python3
"""
BMC AWS Architecture Diagram Generator - Fixed Version
Generates PNG diagrams with AWS icons using diagrams library
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import ECS, Lambda, Fargate
from diagrams.aws.database import RDS, Redshift, Elasticache
from diagrams.aws.storage import S3
from diagrams.aws.network import APIGateway, CloudFront, ELB, VPC
from diagrams.aws.security import Cognito, IAM, WAF, KMS
from diagrams.aws.integration import Eventbridge, SQS, SNS
from diagrams.aws.ml import Textract, Comprehend
from diagrams.aws.management import Cloudwatch, XRay, Cloudtrail
from diagrams.aws.migration import TransferFamily
from diagrams.onprem.client import Users

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
            with Cluster("Load Balancing"):
                alb = ELB("Application LB")
                
            # Compute Layer
            with Cluster("Microservices (ECS Fargate)"):
                with Cluster("Invoice Service"):
                    invoice_service = Fargate("Invoice\n2 vCPU, 4GB")
                    
                with Cluster("Product Service (60M)"):
                    product_service = Fargate("Product\n4 vCPU, 8GB")
                    
                with Cluster("OCR Service"):
                    ocr_service = Fargate("OCR\n2 vCPU, 4GB")
                    
                with Cluster("Commission Service"):
                    commission_service = Fargate("Commission\n1 vCPU, 2GB")
                    
                with Cluster("Certificate Service"):
                    certificate_service = Fargate("Certificate\n1 vCPU, 2GB")
            
            # Serverless Functions
            with Cluster("Lambda Functions"):
                ocr_processor = Lambda("OCR Processor")
                data_validator = Lambda("Data Validator")
                pdf_generator = Lambda("PDF Generator")
                
            # AI/ML Services
            with Cluster("AI/ML Services"):
                textract = Textract("Amazon Textract\nOCR >95%")
                comprehend = Comprehend("Amazon Comprehend\nNLP Analysis")
                
            # Data Layer
            with Cluster("Data Layer"):
                with Cluster("Transactional"):
                    rds_primary = RDS("RDS PostgreSQL\n60M Products\nMulti-AZ")
                    rds_replica = RDS("Read Replica\nQuery Optimization")
                    
                with Cluster("Caching"):
                    redis = Elasticache("ElastiCache Redis\nProduct Cache\n24h TTL")
                    
                with Cluster("Analytics"):
                    redshift = Redshift("Redshift\nData Warehouse\nOLAP")
                    
                with Cluster("Document Storage"):
                    s3_docs = S3("S3 Documents\nIntelligent Tiering")
                    s3_backup = S3("S3 Backup\nCross-Region")
                    
            # Integration Layer
            with Cluster("Event-Driven Integration"):
                eventbridge = Eventbridge("EventBridge\nEvent Bus")
                sqs_fifo = SQS("SQS FIFO\nInvoice Queue")
                sqs_standard = SQS("SQS Standard\nOCR Queue")
                sns = SNS("SNS\nNotifications")
                
            # External Integration
            with Cluster("External Integration"):
                sftp = TransferFamily("Transfer Family\nSFTP Gateway")
                
            # Monitoring
            with Cluster("Monitoring & Observability"):
                cloudwatch = Cloudwatch("CloudWatch\nMetrics & Logs")
                xray = XRay("X-Ray\nDistributed Tracing")
                cloudtrail = Cloudtrail("CloudTrail\nAudit Logs")
        
        # User flows
        users >> cloudfront >> waf >> api_gateway
        external >> sftp
        
        # API Gateway flows
        api_gateway >> cognito
        api_gateway >> alb
        
        # Load balancer to services
        alb >> [invoice_service, product_service, ocr_service, commission_service, certificate_service]
        
        # Service interactions
        invoice_service >> ocr_processor >> textract
        product_service >> redis >> rds_primary
        ocr_service >> s3_docs
        commission_service >> pdf_generator
        
        # Event flows
        invoice_service >> eventbridge >> [sqs_fifo, sqs_standard, sns]
        eventbridge >> [ocr_processor, data_validator, pdf_generator]
        
        # Data flows
        rds_primary >> rds_replica
        product_service >> redshift
        s3_docs >> s3_backup
        
        # Monitoring
        [invoice_service, product_service, ocr_service] >> cloudwatch
        [invoice_service, product_service] >> xray

def generate_microservices_detail():
    """Generate detailed microservices architecture"""
    
    with Diagram("BMC Microservices Architecture - ECS Fargate", 
                 filename="bmc_microservices_detail", 
                 show=False, 
                 direction="TB"):
        
        with Cluster("API Gateway Layer"):
            api_gateway = APIGateway("API Gateway\nCentral Router")
            
        with Cluster("ECS Fargate Cluster"):
            with Cluster("Invoice Service Pod"):
                invoice_alb = ELB("Invoice ALB")
                invoice_tasks = [
                    Fargate("Invoice Task 1\n2 vCPU, 4GB"),
                    Fargate("Invoice Task 2\n2 vCPU, 4GB"),
                    Fargate("Invoice Task N\nAuto Scaling 2-10")
                ]
                
            with Cluster("Product Service Pod (60M Records)"):
                product_alb = ELB("Product ALB")
                product_tasks = [
                    Fargate("Product Task 1\n4 vCPU, 8GB"),
                    Fargate("Product Task 2\n4 vCPU, 8GB"),
                    Fargate("Product Task N\nAuto Scaling 3-15")
                ]
                
            with Cluster("OCR Service Pod"):
                ocr_alb = ELB("OCR ALB")
                ocr_tasks = [
                    Fargate("OCR Task 1\n2 vCPU, 4GB"),
                    Fargate("OCR Task 2\n2 vCPU, 4GB")
                ]
        
        with Cluster("Data Services"):
            rds = RDS("RDS PostgreSQL\nMulti-AZ\n60M Products")
            redis = Elasticache("ElastiCache Redis\nCluster Mode")
            s3 = S3("S3 Buckets\nDocuments")
            
        with Cluster("AI Services"):
            textract = Textract("Amazon Textract\nOCR Processing")
            
        with Cluster("Event Processing"):
            eventbridge = Eventbridge("EventBridge\nEvent Router")
            sqs = SQS("SQS Queues\nFIFO & Standard")
        
        # API Gateway routing
        api_gateway >> [invoice_alb, product_alb, ocr_alb]
        
        # Load balancer to tasks
        invoice_alb >> invoice_tasks
        product_alb >> product_tasks
        ocr_alb >> ocr_tasks
        
        # Data connections
        invoice_tasks >> rds
        product_tasks >> [rds, redis]
        ocr_tasks >> [s3, textract]
        
        # Event flows
        invoice_tasks >> eventbridge >> sqs

def generate_data_architecture():
    """Generate data architecture diagram"""
    
    with Diagram("BMC Data Architecture - Multi-Tier Storage", 
                 filename="bmc_data_architecture", 
                 show=False, 
                 direction="TB"):
        
        with Cluster("Application Layer"):
            web_app = Users("Web App\nReact SPA")
            mobile_app = Users("Mobile App\nReact Native")
            admin_portal = Users("Admin Portal\nManagement UI")
            
        with Cluster("API Layer"):
            api_gateway = APIGateway("API Gateway\nREST Endpoints")
            
        with Cluster("Business Logic"):
            product_service = Fargate("Product Service\n60M Records Lookup")
            invoice_service = Fargate("Invoice Service\nDocument Processing")
            commission_service = Fargate("Commission Service\nBusiness Rules")
            
        with Cluster("Hot Data (Real-time)"):
            redis = Elasticache("ElastiCache Redis\nProduct Cache\nTTL: 24h")
            rds_primary = RDS("RDS Primary\nPostgreSQL 14\nMulti-AZ")
            
        with Cluster("Warm Data (Operational)"):
            rds_replica = RDS("RDS Read Replica\nQuery Optimization\nCross-AZ")
            s3_intelligent = S3("S3 Intelligent Tiering\nDocument Storage\nAuto-archiving")
            
        with Cluster("Cold Data (Analytics)"):
            redshift = Redshift("Redshift Cluster\nData Warehouse\nColumnar Storage")
            s3_glacier = S3("S3 Glacier\nLong-term Archive\n7-year retention")
        
        # Application flows
        [web_app, mobile_app, admin_portal] >> api_gateway
        api_gateway >> [product_service, invoice_service, commission_service]
        
        # Data access patterns
        product_service >> redis >> rds_primary
        invoice_service >> rds_primary
        commission_service >> rds_replica
        
        # Data replication
        rds_primary >> rds_replica
        invoice_service >> s3_intelligent
        
        # Archiving
        s3_intelligent >> s3_glacier
        
        # Analytics
        rds_primary >> redshift

if __name__ == "__main__":
    print("Generating BMC AWS Architecture Diagrams...")
    
    # Generate all diagrams
    generate_main_architecture()
    print("✓ Main architecture diagram generated")
    
    generate_microservices_detail()
    print("✓ Microservices detail diagram generated")
    
    generate_data_architecture()
    print("✓ Data architecture diagram generated")
    
    print("\nAll diagrams generated successfully!")
    print("Files created:")
    print("- bmc_main_architecture.png")
    print("- bmc_microservices_detail.png")
    print("- bmc_data_architecture.png")
