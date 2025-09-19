#!/usr/bin/env python3
"""
BMC Process Flow Diagrams Generator
Generates detailed process flow diagrams with AWS icons
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda, Fargate
from diagrams.aws.database import RDS, ElastiCache
from diagrams.aws.storage import S3
from diagrams.aws.integration import EventBridge, SQS, SNS, StepFunctions
from diagrams.aws.analytics import Textract
from diagrams.aws.management import CloudWatch
from diagrams.aws.network import APIGateway
from diagrams.onprem.client import Users
from diagrams.onprem.network import Internet

def generate_invoice_processing_flow():
    """Generate invoice processing flow diagram"""
    
    with Diagram("BMC Invoice Processing Flow - OCR & Validation", 
                 filename="bmc_invoice_processing_flow", 
                 show=False, 
                 direction="LR"):
        
        # Input
        user = Users("User Upload\nPDF/Image")
        
        with Cluster("Document Processing Pipeline"):
            # Step Functions Workflow
            step_functions = StepFunctions("Step Functions\nWorkflow Orchestration")
            
            # Processing Steps
            with Cluster("Processing Steps"):
                validate_doc = Lambda("Validate Document\nFormat & Size")
                preprocess = Lambda("Preprocess Image\nQuality Enhancement")
                ocr_extract = Textract("OCR Extraction\nTextract >95%")
                parse_data = Lambda("Parse Data\nStructured Extraction")
                validate_business = Lambda("Validate Rules\nBusiness Logic")
                match_products = Fargate("Match Products\n60M Lookup")
                calc_commission = Fargate("Calculate Commission\nBusiness Rules")
                gen_certificate = Lambda("Generate Certificate\nPDF Creation")
            
            # Storage
            s3_raw = S3("S3 Raw\nOriginal Documents")
            s3_processed = S3("S3 Processed\nResults & Certificates")
            rds = RDS("RDS PostgreSQL\nTransaction Data")
            redis = ElastiCache("Redis Cache\nProduct Lookup")
            
            # Events & Notifications
            eventbridge = EventBridge("EventBridge\nEvent Coordination")
            sns = SNS("SNS\nUser Notifications")
            
            # Monitoring
            cloudwatch = CloudWatch("CloudWatch\nProcess Monitoring")
        
        # External
        dian_api = Internet("DIAN API\nProduct Classification")
        email = Internet("Email Service\nCertificate Delivery")
        
        # Flow connections
        user >> s3_raw >> step_functions
        
        step_functions >> validate_doc >> preprocess >> ocr_extract
        ocr_extract >> parse_data >> validate_business
        validate_business >> match_products >> calc_commission >> gen_certificate
        
        # Data flows
        ocr_extract >> s3_processed
        parse_data >> rds
        match_products >> [redis, dian_api]
        gen_certificate >> s3_processed
        
        # Event flows
        step_functions >> eventbridge >> sns >> email
        
        # Monitoring
        [validate_doc, ocr_extract, match_products] >> cloudwatch

def generate_product_lookup_flow():
    """Generate product lookup flow for 60M records"""
    
    with Diagram("BMC Product Lookup Flow - 60M Records Optimization", 
                 filename="bmc_product_lookup_flow", 
                 show=False, 
                 direction="TB"):
        
        # API Entry
        api_gateway = APIGateway("API Gateway\nProduct Search")
        
        with Cluster("Product Service (60M Records)"):
            product_service = Fargate("Product Service\n4 vCPU, 8GB RAM")
            
            with Cluster("Lookup Strategy"):
                cache_check = ElastiCache("Redis Cache Check\n24h TTL")
                db_query = RDS("PostgreSQL Query\nOptimized Indexes")
                search_engine = Lambda("Search Engine\nFull-Text Search")
                
            with Cluster("External Validation"):
                dian_cache = ElastiCache("DIAN Cache\n7-day TTL")
                dian_api = Internet("DIAN API\nClassification Validation")
                
            with Cluster("Response Optimization"):
                result_cache = ElastiCache("Cache Results\nUpdate TTL")
                response_format = Lambda("Format Response\nPagination & Metadata")
        
        with Cluster("Monitoring & Analytics"):
            cloudwatch = CloudWatch("Performance Metrics\nQuery Analytics")
            
        # Flow paths
        api_gateway >> product_service
        
        # Cache-first strategy
        product_service >> cache_check
        cache_check >> Edge(label="Cache Miss") >> db_query
        cache_check >> Edge(label="Cache Hit") >> response_format
        
        # Search flow
        product_service >> search_engine >> db_query
        
        # DIAN validation
        product_service >> dian_cache
        dian_cache >> Edge(label="Cache Miss") >> dian_api
        
        # Result caching
        db_query >> result_cache >> response_format
        dian_api >> dian_cache
        
        # Monitoring
        [product_service, db_query, cache_check] >> cloudwatch

def generate_ocr_processing_flow():
    """Generate OCR processing flow with quality checks"""
    
    with Diagram("BMC OCR Processing Flow - >95% Accuracy Pipeline", 
                 filename="bmc_ocr_processing_flow", 
                 show=False, 
                 direction="TB"):
        
        # Input
        document_upload = S3("Document Upload\nPDF/Image Files")
        
        with Cluster("OCR Processing Pipeline"):
            # Document Analysis
            with Cluster("Document Analysis"):
                doc_classifier = Lambda("Document Classifier\nPDF vs Image")
                pdf_extractor = Lambda("PDF Text Extractor\nDirect Text")
                image_preprocessor = Lambda("Image Preprocessor\nQuality Enhancement")
                
            # OCR Processing
            with Cluster("OCR Engine"):
                textract = Textract("Amazon Textract\nOCR Processing")
                confidence_analyzer = Lambda("Confidence Analyzer\n>95% Threshold")
                
            # Quality Assurance
            with Cluster("Quality Assurance"):
                accuracy_validator = Lambda("Accuracy Validator\nConfidence Check")
                manual_review = SQS("Manual Review Queue\n<95% Confidence")
                enhanced_processing = Lambda("Enhanced Processing\nForms Analysis")
                
            # Data Processing
            with Cluster("Data Processing"):
                field_extractor = Lambda("Field Extractor\nStructured Data")
                data_validator = Lambda("Data Validator\nBusiness Rules")
                format_converter = Lambda("Format Converter\nStandardization")
                
            # Storage & Events
            s3_results = S3("S3 Results\nProcessed Data")
            eventbridge = EventBridge("EventBridge\nCompletion Events")
            
            # Monitoring
            cloudwatch = CloudWatch("OCR Metrics\nAccuracy Tracking")
        
        # Flow connections
        document_upload >> doc_classifier
        
        # Document type routing
        doc_classifier >> Edge(label="PDF") >> pdf_extractor
        doc_classifier >> Edge(label="Image") >> image_preprocessor
        
        # OCR processing
        [pdf_extractor, image_preprocessor] >> textract >> confidence_analyzer
        
        # Quality routing
        confidence_analyzer >> Edge(label=">95%") >> accuracy_validator
        confidence_analyzer >> Edge(label="<95%") >> manual_review
        confidence_analyzer >> Edge(label="90-95%") >> enhanced_processing
        
        # Data processing
        [accuracy_validator, enhanced_processing] >> field_extractor
        field_extractor >> data_validator >> format_converter
        
        # Output
        format_converter >> s3_results >> eventbridge
        
        # Monitoring
        [textract, confidence_analyzer, accuracy_validator] >> cloudwatch

def generate_error_handling_flow():
    """Generate error handling and recovery flow"""
    
    with Diagram("BMC Error Handling & Recovery Flow", 
                 filename="bmc_error_handling_flow", 
                 show=False, 
                 direction="TB"):
        
        # Error Detection
        with Cluster("Error Detection"):
            service_error = Fargate("Service Error\nMicroservice Failure")
            lambda_error = Lambda("Lambda Error\nFunction Failure")
            external_error = Internet("External API Error\nDIAN/SFTP Failure")
            
        with Cluster("Error Classification"):
            error_classifier = Lambda("Error Classifier\nTransient vs Permanent")
            
        with Cluster("Recovery Strategies"):
            # Retry Logic
            with Cluster("Retry Logic"):
                exponential_backoff = Lambda("Exponential Backoff\nRetry Strategy")
                circuit_breaker = Lambda("Circuit Breaker\nFailure Protection")
                
            # Fallback Mechanisms
            with Cluster("Fallback Mechanisms"):
                cache_fallback = ElastiCache("Cache Fallback\nStale Data")
                degraded_service = Lambda("Degraded Service\nLimited Functionality")
                
            # Dead Letter Processing
            with Cluster("Dead Letter Processing"):
                dlq = SQS("Dead Letter Queue\nFailed Messages")
                manual_review = Lambda("Manual Review\nHuman Intervention")
                
        with Cluster("Alerting & Monitoring"):
            cloudwatch_alarms = CloudWatch("CloudWatch Alarms\nError Thresholds")
            sns_alerts = SNS("SNS Alerts\nImmediate Notification")
            
        with Cluster("Recovery Actions"):
            auto_scaling = Lambda("Auto Scaling\nResource Adjustment")
            failover = Lambda("Failover\nDR Activation")
            
        # Error flow
        [service_error, lambda_error, external_error] >> error_classifier
        
        # Classification routing
        error_classifier >> Edge(label="Transient") >> exponential_backoff
        error_classifier >> Edge(label="Rate Limited") >> circuit_breaker
        error_classifier >> Edge(label="Service Down") >> cache_fallback
        error_classifier >> Edge(label="Permanent") >> dlq
        
        # Recovery paths
        exponential_backoff >> Edge(label="Max Retries") >> dlq
        circuit_breaker >> degraded_service
        cache_fallback >> Edge(label="No Cache") >> degraded_service
        dlq >> manual_review
        
        # Alerting
        [error_classifier, dlq] >> cloudwatch_alarms >> sns_alerts
        
        # Auto-recovery
        cloudwatch_alarms >> [auto_scaling, failover]

def generate_monitoring_flow():
    """Generate monitoring and alerting flow"""
    
    with Diagram("BMC Monitoring & Alerting Flow", 
                 filename="bmc_monitoring_flow", 
                 show=False, 
                 direction="LR"):
        
        # Data Sources
        with Cluster("Metric Sources"):
            ecs_metrics = Fargate("ECS Metrics\nCPU, Memory, Network")
            rds_metrics = RDS("RDS Metrics\nConnections, Performance")
            lambda_metrics = Lambda("Lambda Metrics\nDuration, Errors")
            api_metrics = APIGateway("API Metrics\nLatency, Errors")
            
        with Cluster("Log Sources"):
            application_logs = Fargate("Application Logs\nService Logs")
            access_logs = APIGateway("Access Logs\nAPI Gateway")
            
        with Cluster("Monitoring Platform"):
            cloudwatch = CloudWatch("CloudWatch\nMetrics Aggregation")
            log_insights = CloudWatch("CloudWatch Insights\nLog Analysis")
            
        with Cluster("Alerting Engine"):
            alarms = CloudWatch("CloudWatch Alarms\nThreshold Monitoring")
            anomaly_detection = CloudWatch("Anomaly Detection\nML-based Alerts")
            
        with Cluster("Notification Channels"):
            sns_email = SNS("SNS Email\nTeam Notifications")
            sns_sms = SNS("SNS SMS\nCritical Alerts")
            sns_slack = SNS("SNS Slack\nTeam Channel")
            
        with Cluster("Response Actions"):
            auto_scaling = Lambda("Auto Scaling\nResource Adjustment")
            incident_response = Lambda("Incident Response\nAutomated Remediation")
            
        # Metric flows
        [ecs_metrics, rds_metrics, lambda_metrics, api_metrics] >> cloudwatch
        [application_logs, access_logs] >> log_insights
        
        # Alert generation
        cloudwatch >> [alarms, anomaly_detection]
        log_insights >> alarms
        
        # Notification routing
        alarms >> Edge(label="Warning") >> sns_email
        alarms >> Edge(label="Critical") >> [sns_sms, sns_slack]
        anomaly_detection >> sns_slack
        
        # Automated response
        alarms >> [auto_scaling, incident_response]

if __name__ == "__main__":
    print("Generating BMC Process Flow Diagrams...")
    
    # Generate all process flow diagrams
    generate_invoice_processing_flow()
    print("✓ Invoice processing flow diagram generated")
    
    generate_product_lookup_flow()
    print("✓ Product lookup flow diagram generated")
    
    generate_ocr_processing_flow()
    print("✓ OCR processing flow diagram generated")
    
    generate_error_handling_flow()
    print("✓ Error handling flow diagram generated")
    
    generate_monitoring_flow()
    print("✓ Monitoring flow diagram generated")
    
    print("\nAll process flow diagrams generated successfully!")
    print("Files created:")
    print("- bmc_invoice_processing_flow.png")
    print("- bmc_product_lookup_flow.png")
    print("- bmc_ocr_processing_flow.png")
    print("- bmc_error_handling_flow.png")
    print("- bmc_monitoring_flow.png")
