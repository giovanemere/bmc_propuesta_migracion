#!/usr/bin/env python3
"""
BMC AWS Architecture Diagram Generator
Generates PNG diagrams with AWS icons using diagrams library
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import ECS, Lambda, Fargate
from diagrams.aws.database import RDS, Redshift, ElastiCache
from diagrams.aws.storage import S3
from diagrams.aws.network import APIGateway, CloudFront, ELB, VPC
from diagrams.aws.security import Cognito, IAM, WAF, KMS
from diagrams.aws.integration import EventBridge, SQS, SNS
from diagrams.aws.analytics import Textract, Comprehend
from diagrams.aws.management import CloudWatch, XRay, CloudTrail
from diagrams.aws.migration import TransferFamily
from diagrams.aws.general import Users, Internet
from diagrams.onprem.client import Users as OnPremUsers

def generate_main_architecture():
    """Generate main BMC architecture diagram"""
    
    with Diagram("BMC AWS Architecture - 60M Products Platform", 
                 filename="bmc_main_architecture", 
                 show=False, 
                 direction="TB"):
        
        # Users
        users = OnPremUsers("BMC Users")
        external = OnPremUsers("External Systems")
        
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
                    redis = ElastiCache("ElastiCache Redis\nProduct Cache\n24h TTL")
                    
                with Cluster("Analytics"):
                    redshift = Redshift("Redshift\nData Warehouse\nOLAP")
                    
                with Cluster("Document Storage"):
                    s3_docs = S3("S3 Documents\nIntelligent Tiering")
                    s3_backup = S3("S3 Backup\nCross-Region")
                    
            # Integration Layer
            with Cluster("Event-Driven Integration"):
                eventbridge = EventBridge("EventBridge\nEvent Bus")
                sqs_fifo = SQS("SQS FIFO\nInvoice Queue")
                sqs_standard = SQS("SQS Standard\nOCR Queue")
                sns = SNS("SNS\nNotifications")
                
            # External Integration
            with Cluster("External Integration"):
                sftp = TransferFamily("Transfer Family\nSFTP Gateway")
                
            # Monitoring
            with Cluster("Monitoring & Observability"):
                cloudwatch = CloudWatch("CloudWatch\nMetrics & Logs")
                xray = XRay("X-Ray\nDistributed Tracing")
                cloudtrail = CloudTrail("CloudTrail\nAudit Logs")
        
        # External Services
        with Cluster("External Services"):
            dian_api = Internet("DIAN API\nTax Authority")
            email_service = Internet("Email Service\nSES/SMTP")
        
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
        
        # External integrations
        product_service >> dian_api
        sns >> email_service
        
        # Monitoring
        [invoice_service, product_service, ocr_service] >> cloudwatch
        [invoice_service, product_service] >> xray
        cloudwatch >> sns

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
                
            with Cluster("Commission Service Pod"):
                commission_alb = ELB("Commission ALB")
                commission_tasks = [
                    Fargate("Commission Task 1\n1 vCPU, 2GB"),
                    Fargate("Commission Task 2\n1 vCPU, 2GB")
                ]
                
            with Cluster("Certificate Service Pod"):
                cert_alb = ELB("Certificate ALB")
                cert_tasks = [
                    Fargate("Certificate Task 1\n1 vCPU, 2GB"),
                    Fargate("Certificate Task 2\n1 vCPU, 2GB")
                ]
        
        with Cluster("Data Services"):
            rds = RDS("RDS PostgreSQL\nMulti-AZ\n60M Products")
            redis = ElastiCache("ElastiCache Redis\nCluster Mode")
            s3 = S3("S3 Buckets\nDocuments")
            
        with Cluster("AI Services"):
            textract = Textract("Amazon Textract\nOCR Processing")
            
        with Cluster("Event Processing"):
            eventbridge = EventBridge("EventBridge\nEvent Router")
            sqs = SQS("SQS Queues\nFIFO & Standard")
        
        # API Gateway routing
        api_gateway >> [invoice_alb, product_alb, ocr_alb, commission_alb, cert_alb]
        
        # Load balancer to tasks
        invoice_alb >> invoice_tasks
        product_alb >> product_tasks
        ocr_alb >> ocr_tasks
        commission_alb >> commission_tasks
        cert_alb >> cert_tasks
        
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
            web_app = OnPremUsers("Web App\nReact SPA")
            mobile_app = OnPremUsers("Mobile App\nReact Native")
            admin_portal = OnPremUsers("Admin Portal\nManagement UI")
            
        with Cluster("API Layer"):
            api_gateway = APIGateway("API Gateway\nREST Endpoints")
            
        with Cluster("Business Logic"):
            product_service = Fargate("Product Service\n60M Records Lookup")
            invoice_service = Fargate("Invoice Service\nDocument Processing")
            commission_service = Fargate("Commission Service\nBusiness Rules")
            
        with Cluster("Hot Data (Real-time)"):
            redis = ElastiCache("ElastiCache Redis\nProduct Cache\nTTL: 24h")
            rds_primary = RDS("RDS Primary\nPostgreSQL 14\nMulti-AZ")
            
        with Cluster("Warm Data (Operational)"):
            rds_replica = RDS("RDS Read Replica\nQuery Optimization\nCross-AZ")
            s3_intelligent = S3("S3 Intelligent Tiering\nDocument Storage\nAuto-archiving")
            
        with Cluster("Cold Data (Analytics)"):
            redshift = Redshift("Redshift Cluster\nData Warehouse\nColumnar Storage")
            s3_glacier = S3("S3 Glacier\nLong-term Archive\n7-year retention")
            
        with Cluster("Data Pipeline"):
            glue = Lambda("AWS Glue\nETL Jobs\nData Catalog")
            kinesis = EventBridge("Kinesis Data Streams\nReal-time Analytics")
            
        with Cluster("Analytics & BI"):
            quicksight = CloudWatch("QuickSight\nBusiness Intelligence\nDashboards")
            athena = Lambda("Amazon Athena\nServerless Queries\nS3 Data Lake")
        
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
        
        # ETL Pipeline
        rds_primary >> glue >> redshift
        s3_intelligent >> glue
        product_service >> kinesis >> s3_intelligent
        
        # Archiving
        s3_intelligent >> s3_glacier
        
        # Analytics
        redshift >> quicksight
        s3_intelligent >> athena >> quicksight

def generate_security_architecture():
    """Generate security and compliance architecture"""
    
    with Diagram("BMC Security & Compliance Architecture", 
                 filename="bmc_security_architecture", 
                 show=False, 
                 direction="TB"):
        
        with Cluster("Edge Security"):
            cloudfront = CloudFront("CloudFront\nGlobal CDN")
            waf = WAF("AWS WAF\nWeb Application Firewall")
            shield = WAF("AWS Shield\nDDoS Protection")
            
        with Cluster("Identity & Access"):
            cognito = Cognito("Amazon Cognito\nUser Authentication")
            iam = IAM("AWS IAM\nRole-based Access")
            secrets = KMS("Secrets Manager\nAPI Keys & Passwords")
            
        with Cluster("Network Security"):
            vpc = VPC("VPC\nIsolated Network")
            private_subnets = VPC("Private Subnets\nApplication Tier")
            public_subnets = VPC("Public Subnets\nLoad Balancers")
            nat_gateway = VPC("NAT Gateway\nOutbound Internet")
            
        with Cluster("Data Encryption"):
            kms = KMS("AWS KMS\nKey Management\nCustomer Managed Keys")
            s3_encryption = S3("S3 Encryption\nAES-256 at Rest")
            rds_encryption = RDS("RDS Encryption\nTDE + Backup Encryption")
            
        with Cluster("Monitoring & Compliance"):
            cloudtrail = CloudTrail("CloudTrail\nAPI Audit Logs\n7-year retention")
            config = CloudWatch("AWS Config\nCompliance Rules\nResource Tracking")
            guardduty = CloudWatch("GuardDuty\nThreat Detection\nML-based Security")
            security_hub = CloudWatch("Security Hub\nCentralized Security\nCompliance Dashboard")
            
        with Cluster("Incident Response"):
            cloudwatch = CloudWatch("CloudWatch\nSecurity Metrics\nReal-time Alerts")
            sns = SNS("SNS\nAlert Notifications\nMulti-channel")
            lambda_response = Lambda("Lambda\nAutomated Response\nSecurity Remediation")
        
        # Security flow
        cloudfront >> waf >> shield >> public_subnets
        public_subnets >> private_subnets >> nat_gateway
        
        # Identity flow
        cognito >> iam >> secrets
        
        # Encryption flow
        kms >> [s3_encryption, rds_encryption]
        
        # Monitoring flow
        [cloudtrail, config, guardduty] >> security_hub >> cloudwatch
        cloudwatch >> sns >> lambda_response

def generate_monitoring_architecture():
    """Generate monitoring and observability architecture"""
    
    with Diagram("BMC Monitoring & Observability", 
                 filename="bmc_monitoring_architecture", 
                 show=False, 
                 direction="TB"):
        
        with Cluster("Metrics Collection"):
            cloudwatch = CloudWatch("CloudWatch\nSystem Metrics\nCustom Metrics")
            xray = XRay("X-Ray\nDistributed Tracing\nService Map")
            container_insights = CloudWatch("Container Insights\nECS/Fargate Metrics\nPerformance Monitoring")
            
        with Cluster("Logging"):
            cloudwatch_logs = CloudWatch("CloudWatch Logs\nCentralized Logging\nLog Groups")
            log_insights = CloudWatch("CloudWatch Insights\nLog Analysis\nQuery Engine")
            s3_archive = S3("S3 Log Archive\nLong-term Storage\nCost Optimization")
            
        with Cluster("Alerting & Notifications"):
            alarms = CloudWatch("CloudWatch Alarms\nThreshold Monitoring\nAnomaly Detection")
            sns = SNS("SNS Topics\nMulti-channel Alerts\nEmail, SMS, Slack")
            
        with Cluster("Dashboards & Visualization"):
            dashboards = CloudWatch("CloudWatch Dashboards\nReal-time Metrics\nCustom Widgets")
            quicksight = CloudWatch("QuickSight\nBusiness Intelligence\nExecutive Reports")
            
        with Cluster("Application Performance"):
            apm = XRay("APM Agent\nApplication Monitoring\nPerformance Insights")
            rum = CloudWatch("RUM Agent\nReal User Monitoring\nFrontend Performance")
            synthetic = Lambda("Synthetic Monitoring\nProactive Testing\nAvailability Checks")
        
        # Monitoring flows
        [cloudwatch, xray, container_insights] >> alarms
        cloudwatch_logs >> log_insights >> s3_archive
        alarms >> sns
        
        # Dashboard flows
        cloudwatch >> [dashboards, quicksight]
        
        # APM flows
        apm >> xray
        [rum, synthetic] >> cloudwatch

if __name__ == "__main__":
    print("Generating BMC AWS Architecture Diagrams...")
    
    # Generate all diagrams
    generate_main_architecture()
    print("✓ Main architecture diagram generated")
    
    generate_microservices_detail()
    print("✓ Microservices detail diagram generated")
    
    generate_data_architecture()
    print("✓ Data architecture diagram generated")
    
    generate_security_architecture()
    print("✓ Security architecture diagram generated")
    
    generate_monitoring_architecture()
    print("✓ Monitoring architecture diagram generated")
    
    print("\nAll diagrams generated successfully!")
    print("Files created:")
    print("- bmc_main_architecture.png")
    print("- bmc_microservices_detail.png")
    print("- bmc_data_architecture.png")
    print("- bmc_security_architecture.png")
    print("- bmc_monitoring_architecture.png")
