#!/usr/bin/env python3
"""
Professional DrawIO Generator - Nivel igual a PNG
Genera DrawIO XML con el mismo nivel de detalle que los PNG
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List
import uuid

class ProfessionalDrawIOGenerator:
    """Generador DrawIO profesional nivel PNG"""
    
    def __init__(self, output_dir: str = "outputs"):
        self.output_dir = Path(output_dir)
        self.component_id = 1000
        
    def generate_professional_drawio(self, config: Dict, project_name: str = "bmc_input") -> str:
        """Genera DrawIO con nivel profesional igual a PNG"""
        
        # Solo generar network diagram por ahora
        diagrams = []
        
        # 1. Network Architecture - Nivel Senior (funcional)
        network_xml = self._generate_network_drawio(config)
        diagrams.append(("Network Architecture", network_xml))
        
        # Combinar en archivo
        combined_xml = self._combine_diagrams(diagrams, project_name)
        
        # Guardar archivo
        output_path = self._save_drawio_file(combined_xml, project_name)
        
        return output_path
    
    def _generate_network_drawio(self, config: Dict) -> str:
        """Genera diagrama de red nivel senior"""
        
        components = []
        component_ids = {}
        
        # Título
        components.append(self._create_title("BMC NETWORK ARCHITECTURE - AWS SENIOR LEVEL", 400, 20))
        
        # AWS Cloud Container
        components.append(self._create_container("aws_cloud", "AWS Cloud - us-east-1", 50, 80, 1200, 800, "#E3F2FD", "#1976D2"))
        
        # Edge Services - capturar IDs
        cloudfront_xml, cloudfront_id = self._create_aws_component("cloudfront", "CloudFront CDN\\n200+ edge locations\\nSSL/TLS 1.3", 150, 150, "mxgraph.aws4.cloudfront")
        waf_xml, waf_id = self._create_aws_component("waf", "AWS WAF\\nDDoS protection\\nRate limiting: 2K/s", 350, 150, "mxgraph.aws4.waf")
        api_gw_xml, api_gw_id = self._create_aws_component("api_gw", "API Gateway\\n10K req/s throttle\\nCaching: 300s TTL", 550, 150, "mxgraph.aws4.api_gateway")
        
        components.extend([cloudfront_xml, waf_xml, api_gw_xml])
        component_ids.update({"cloudfront": cloudfront_id, "waf": waf_id, "api_gw": api_gw_id})
        
        # VPC Container
        components.append(self._create_container("vpc", "VPC 10.0.0.0/16 - Multi-AZ", 100, 300, 1000, 500, "#F5F5F5", "#666666"))
        
        # AZ-1a Container
        components.append(self._create_container("az1a", "AZ us-east-1a", 150, 350, 400, 200, "#E8F5E8", "#4CAF50"))
        
        # Microservices en AZ-1a
        invoice_xml, invoice_id = self._create_aws_component("invoice", "Invoice Service\\n2vCPU/4GB\\nBlue/Green deploy", 200, 400, "mxgraph.aws4.fargate")
        product_xml, product_id = self._create_aws_component("product", "Product Service\\n4vCPU/8GB\\n60M products", 350, 400, "mxgraph.aws4.fargate")
        
        components.extend([invoice_xml, product_xml])
        component_ids.update({"invoice": invoice_id, "product": product_id})
        
        # AZ-1b Container  
        components.append(self._create_container("az1b", "AZ us-east-1b", 600, 350, 400, 200, "#FFF3E0", "#FF9800"))
        
        # Microservices en AZ-1b
        ocr_xml, ocr_id = self._create_aws_component("ocr", "OCR Service\\n4vCPU/8GB\\nTextract integration", 650, 400, "mxgraph.aws4.fargate")
        commission_xml, commission_id = self._create_aws_component("commission", "Commission Service\\n2vCPU/4GB\\nDIAN compliance", 800, 400, "mxgraph.aws4.fargate")
        
        components.extend([ocr_xml, commission_xml])
        component_ids.update({"ocr": ocr_id, "commission": commission_id})
        
        # Database Layer
        rds_primary_xml, rds_primary_id = self._create_aws_component("rds_primary", "RDS Primary\\nPostgreSQL 14\\ndb.r6g.2xlarge\\n35-day backup", 300, 600, "mxgraph.aws4.rds")
        rds_replica_xml, rds_replica_id = self._create_aws_component("rds_replica", "Read Replica\\nCross-AZ\\nPromotion ready", 500, 600, "mxgraph.aws4.rds")
        
        components.extend([rds_primary_xml, rds_replica_xml])
        component_ids.update({"rds_primary": rds_primary_id, "rds_replica": rds_replica_id})
        
        # Storage
        s3_docs_xml, s3_docs_id = self._create_aws_component("s3_docs", "S3 Documents\\nIntelligent Tiering\\n90d → Glacier", 750, 150, "mxgraph.aws4.s3")
        redis_xml, redis_id = self._create_aws_component("redis", "ElastiCache Redis\\n6 nodes (3 shards)\\nMulti-AZ", 700, 600, "mxgraph.aws4.elasticache")
        
        components.extend([s3_docs_xml, redis_xml])
        component_ids.update({"s3_docs": s3_docs_id, "redis": redis_id})
        
        # Conexiones profesionales con IDs correctos
        connections = [
            self._create_connection(component_ids["cloudfront"], component_ids["waf"], "HTTPS Traffic", "#1976D2"),
            self._create_connection(component_ids["waf"], component_ids["api_gw"], "Filtered Requests", "#1976D2"),
            self._create_connection(component_ids["api_gw"], component_ids["invoice"], "Route /invoices", "#4CAF50"),
            self._create_connection(component_ids["api_gw"], component_ids["product"], "Route /products", "#4CAF50"),
            self._create_connection(component_ids["api_gw"], component_ids["ocr"], "Route /ocr", "#4CAF50"),
            self._create_connection(component_ids["api_gw"], component_ids["commission"], "Route /commissions", "#4CAF50"),
            self._create_connection(component_ids["invoice"], component_ids["rds_primary"], "Write Operations", "#2196F3"),
            self._create_connection(component_ids["product"], component_ids["rds_primary"], "Write Operations", "#2196F3"),
            self._create_connection(component_ids["product"], component_ids["redis"], "Cache Lookup", "#FF9800"),
            self._create_connection(component_ids["rds_primary"], component_ids["rds_replica"], "Replication", "#9C27B0")
        ]
        
        return self._build_diagram_xml(components + connections)
    
    def _generate_microservices_drawio(self, config: Dict) -> str:
        """Genera diagrama de microservicios detallado"""
        
        components = []
        component_ids = {}
        
        # Título
        components.append(self._create_title("BMC MICROSERVICES - DETAILED ARCHITECTURE", 400, 20))
        
        # API Layer
        components.append(self._create_container("api_layer", "API Management Layer", 50, 80, 1200, 150, "#E3F2FD", "#1976D2"))
        
        api_gateway_xml, api_gateway_id = self._create_aws_component("api_gateway", "API Gateway\\nThrottling: 10K req/s\\nCustom authorizers", 150, 120, "mxgraph.aws4.api_gateway")
        cognito_xml, cognito_id = self._create_aws_component("cognito", "Cognito User Pool\\nJWT validation\\nMFA: TOTP + SMS", 400, 120, "mxgraph.aws4.cognito")
        alb_xml, alb_id = self._create_aws_component("alb", "Application LB\\nSticky sessions\\nHealth checks", 650, 120, "mxgraph.aws4.application_load_balancer")
        
        components.extend([api_gateway_xml, cognito_xml, alb_xml])
        component_ids.update({"api_gateway": api_gateway_id, "cognito": cognito_id, "alb": alb_id})
        
        # Microservices Layer
        components.append(self._create_container("microservices", "ECS Fargate Cluster - Auto Scaling", 50, 280, 1200, 200, "#E8F5E8", "#4CAF50"))
        
        # Invoice Service Pod
        components.append(self._create_container("invoice_pod", "Invoice Service Pod", 100, 320, 200, 120, "#FFF3E0", "#FF9800"))
        invoice_task1_xml, invoice_task1_id = self._create_aws_component("invoice_task1", "Task 1\\n2vCPU/4GB\\nPort: 8000", 120, 350, "mxgraph.aws4.fargate")
        invoice_task2_xml, invoice_task2_id = self._create_aws_component("invoice_task2", "Task 2\\n2vCPU/4GB\\nPort: 8000", 200, 350, "mxgraph.aws4.fargate")
        
        components.extend([invoice_task1_xml, invoice_task2_xml])
        component_ids.update({"invoice_task1": invoice_task1_id, "invoice_task2": invoice_task2_id})
        
        # RDS
        rds_primary_xml, rds_primary_id = self._create_aws_component("rds_primary", "RDS PostgreSQL\\ndb.r6g.2xlarge\\nMulti-AZ\\n35-day backup", 150, 580, "mxgraph.aws4.rds")
        components.append(rds_primary_xml)
        component_ids["rds_primary"] = rds_primary_id
        
        # Conexiones básicas
        connections = [
            self._create_connection(component_ids["api_gateway"], component_ids["cognito"], "Auth", "#1976D2"),
            self._create_connection(component_ids["cognito"], component_ids["alb"], "Authorized", "#1976D2"),
            self._create_connection(component_ids["alb"], component_ids["invoice_task1"], "Route", "#4CAF50"),
            self._create_connection(component_ids["invoice_task1"], component_ids["rds_primary"], "Write", "#2196F3")
        ]
        
        return self._build_diagram_xml(components + connections)
    
    def _create_title(self, text: str, x: int, y: int) -> str:
        """Crea título profesional"""
        escaped_text = text.replace('<', '&lt;').replace('>', '&gt;').replace('&', '&amp;').replace('"', '&quot;')
        return f'''<mxCell id="title_{self._next_id()}" value="{escaped_text}" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=18;fontStyle=1;fontColor=#1976D2;" vertex="1" parent="1">
          <mxGeometry x="{x}" y="{y}" width="600" height="30" as="geometry"/>
        </mxCell>'''
    
    def _create_container(self, id_name: str, label: str, x: int, y: int, width: int, height: int, fill_color: str, stroke_color: str) -> str:
        """Crea contenedor profesional"""
        escaped_label = label.replace('<', '&lt;').replace('>', '&gt;').replace('&', '&amp;').replace('"', '&quot;')
        return f'''<mxCell id="{id_name}_{self._next_id()}" value="{escaped_label}" style="fillColor={fill_color};strokeColor={stroke_color};dashed=1;verticalAlign=top;fontStyle=1;fontSize=14;fontColor={stroke_color};" vertex="1" parent="1">
          <mxGeometry x="{x}" y="{y}" width="{width}" height="{height}" as="geometry"/>
        </mxCell>'''
    
    def _create_aws_component(self, id_name: str, label: str, x: int, y: int, shape: str) -> tuple[str, str]:
        """Crea componente AWS profesional y devuelve XML e ID"""
        # Escapar caracteres XML
        escaped_label = label.replace('<', '&lt;').replace('>', '&gt;').replace('&', '&amp;').replace('"', '&quot;')
        component_id = f"{id_name}_{self._next_id()}"
        
        xml = f'''<mxCell id="{component_id}" value="{escaped_label}" style="shape={shape};labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E8F5E8;strokeColor=#4CAF50;fontColor=#2E7D32;" vertex="1" parent="1">
          <mxGeometry x="{x}" y="{y}" width="78" height="78" as="geometry"/>
        </mxCell>'''
        
        return xml, component_id
    
    def _create_connection(self, source: str, target: str, label: str, color: str) -> str:
        """Crea conexión profesional"""
        
        # Genera un ID único y lo guarda en una variable local
        conn_id = f"conn_{self._next_id()}"
        escaped_label = label.replace('<', '&lt;').replace('>', '&gt;').replace('&', '&amp;').replace('"', '&quot;')
        
        return f'''<mxCell id="{conn_id}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor={color};strokeWidth=2;fontColor={color};" edge="1" parent="1" source="{source}" target="{target}">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="0" y="-10" as="offset"/>
            <Array as="points"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="label_{self._next_id()}" value="{escaped_label}" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10;fontColor={color};" vertex="1" connectable="0" parent="{conn_id}">
          <mxGeometry x="-0.1" y="1" relative="1" as="geometry">
            <mxPoint as="offset"/>
          </mxGeometry>
        </mxCell>'''
    
    def _next_id(self) -> int:
        """Genera ID único"""
        self.component_id += 1
        return self.component_id
    
    def _build_diagram_xml(self, components: List[str]) -> str:
        """Construye XML del diagrama"""
        return '\n'.join(components)
    
    def _generate_security_drawio(self, config: Dict) -> str:
        """Genera diagrama de seguridad nivel senior"""
        
        components = []
        
        # Título
        components.append(self._create_title("BMC SECURITY ARCHITECTURE - ENTERPRISE GRADE", 400, 20))
        
        # Internet y usuarios
        components.append(self._create_aws_component("internet", "Internet\\nGlobal Access", 100, 100, "mxgraph.aws4.internet"))
        components.append(self._create_aws_component("users", "BMC Users\\n10K concurrent\\nMulti-device", 300, 100, "mxgraph.aws4.users"))
        
        # Edge Security Layer
        components.append(self._create_container("edge_security", "Edge Security Layer", 50, 200, 1200, 150, "#FFEBEE", "#D32F2F"))
        components.append(self._create_aws_component("cloudfront", "CloudFront\\nSSL/TLS 1.3\\nGlobal edge\\nGzip compression", 150, 240, "mxgraph.aws4.cloudfront"))
        components.append(self._create_aws_component("waf", "AWS WAF\\nDDoS protection\\nGeo blocking\\nSQL injection\\nRate limiting: 2K/s", 350, 240, "mxgraph.aws4.waf"))
        components.append(self._create_aws_component("shield", "AWS Shield\\nAdvanced DDoS\\n24/7 DRT support", 550, 240, "mxgraph.aws4.shield"))
        
        # Identity & Access Management
        components.append(self._create_container("iam_layer", "Identity & Access Management", 50, 400, 1200, 150, "#F3E5F5", "#7B1FA2"))
        components.append(self._create_aws_component("cognito", "Cognito User Pool\\nMFA: TOTP + SMS\\nPassword policy\\nSocial login", 150, 440, "mxgraph.aws4.cognito"))
        components.append(self._create_aws_component("api_gateway", "API Gateway\\nJWT validation\\nAPI keys\\nThrottling\\nCustom authorizers", 350, 440, "mxgraph.aws4.api_gateway"))
        components.append(self._create_aws_component("iam", "IAM Roles\\nLeast privilege\\nAssumeRole\\nPolicy conditions", 550, 440, "mxgraph.aws4.iam"))
        
        # Application Security
        components.append(self._create_container("app_security", "Application Security", 50, 600, 1200, 150, "#E8EAF6", "#3F51B5"))
        components.append(self._create_aws_component("fargate", "ECS Fargate\\nTask Role IAM\\nSecrets Manager\\nVPC Endpoints\\nPrivate subnets", 150, 640, "mxgraph.aws4.fargate"))
        components.append(self._create_aws_component("secrets", "Secrets Manager\\nDB credentials\\nAPI keys\\nAuto rotation\\nEncryption", 350, 640, "mxgraph.aws4.secrets_manager"))
        components.append(self._create_aws_component("parameter_store", "Parameter Store\\nConfig values\\nSecure strings\\nHierarchy", 550, 640, "mxgraph.aws4.systems_manager_parameter_store"))
        
        # Data Security
        components.append(self._create_container("data_security", "Data Security", 50, 800, 1200, 150, "#E0F2F1", "#00695C"))
        components.append(self._create_aws_component("kms", "KMS Encryption\\nCustomer managed keys\\nAuto rotation\\nCloudTrail audit\\nGrant permissions", 150, 840, "mxgraph.aws4.kms"))
        components.append(self._create_aws_component("rds", "RDS Encrypted\\nAt rest + in transit\\nSSL certificates\\nTDE enabled", 350, 840, "mxgraph.aws4.rds"))
        components.append(self._create_aws_component("s3", "S3 Encrypted\\nBucket policies\\nAccess logging\\nMFA delete\\nVersioning", 550, 840, "mxgraph.aws4.s3"))
        
        # Network Security
        components.append(self._create_container("network_security", "Network Security", 750, 600, 400, 350, "#FFF3E0", "#E65100"))
        components.append(self._create_aws_component("vpc", "VPC\\nPrivate subnets\\nNACLs\\nFlow logs", 800, 640, "mxgraph.aws4.vpc"))
        components.append(self._create_aws_component("security_groups", "Security Groups\\nLeast privilege\\nPort restrictions\\nSource-based rules", 800, 740, "mxgraph.aws4.security_group"))
        components.append(self._create_aws_component("nat_gateway", "NAT Gateway\\nOutbound internet\\nStatic IP\\nHigh availability", 800, 840, "mxgraph.aws4.nat_gateway"))
        
        # Monitoring & Compliance
        components.append(self._create_aws_component("cloudwatch", "CloudWatch\\nSecurity logs\\nAnomaly detection\\nCustom metrics\\nAlarms", 950, 240, "mxgraph.aws4.cloudwatch"))
        components.append(self._create_aws_component("cloudtrail", "CloudTrail\\nAPI audit logs\\nCompliance reports\\nData events\\nInsight events", 950, 440, "mxgraph.aws4.cloudtrail"))
        
        # Conexiones de seguridad
        connections = [
            self._create_connection("users", "cloudfront", "HTTPS Only", "#D32F2F"),
            self._create_connection("cloudfront", "waf", "Filter Traffic", "#D32F2F"),
            self._create_connection("waf", "shield", "DDoS Protection", "#D32F2F"),
            self._create_connection("shield", "api_gateway", "Clean Traffic", "#7B1FA2"),
            self._create_connection("api_gateway", "cognito", "Authenticate", "#7B1FA2"),
            self._create_connection("cognito", "iam", "Authorize", "#7B1FA2"),
            self._create_connection("iam", "fargate", "Assume Role", "#3F51B5"),
            self._create_connection("fargate", "secrets", "Retrieve Secrets", "#3F51B5"),
            self._create_connection("fargate", "kms", "Encrypt/Decrypt", "#00695C"),
            self._create_connection("kms", "rds", "Protect Data", "#00695C"),
            self._create_connection("kms", "s3", "Protect Files", "#00695C"),
            self._create_connection("fargate", "vpc", "Network Control", "#E65100"),
            self._create_connection("vpc", "security_groups", "Traffic Rules", "#E65100"),
            self._create_connection("fargate", "cloudwatch", "Security Logs", "#FF9800"),
            self._create_connection("api_gateway", "cloudtrail", "API Audit", "#FF9800")
        ]
        
        return self._build_diagram_xml(components + connections)
    
    def _generate_dataflow_drawio(self, config: Dict) -> str:
        """Genera diagrama de flujo de datos nivel senior"""
        
        components = []
        
        # Título
        components.append(self._create_title("BMC DATA FLOW - AWS SENIOR ARCHITECT LEVEL", 400, 20))
        
        # External Data Sources
        components.append(self._create_container("external_sources", "External Data Sources - Multi-Channel", 50, 80, 1200, 150, "#E3F2FD", "#1976D2"))
        components.append(self._create_aws_component("web_portal", "Web Portal\\n10K DAU\\nReact SPA\\nMax 50MB/file\\nProgress tracking", 100, 120, "mxgraph.aws4.users"))
        components.append(self._create_aws_component("mobile_app", "Mobile App\\nReact Native\\nImage compression\\nOffline sync\\nPush notifications", 250, 120, "mxgraph.aws4.mobile_client"))
        components.append(self._create_aws_component("api_clients", "API Clients\\n1K req/s\\nOAuth 2.0\\nRate limited\\nSDK support", 400, 120, "mxgraph.aws4.api_gateway"))
        components.append(self._create_aws_component("sftp_server", "SFTP Server\\nScheduled: 02:00 UTC\\n100K records/batch\\nPGP encrypted\\nChecksum validation", 550, 120, "mxgraph.aws4.storage_gateway"))
        components.append(self._create_aws_component("erp_systems", "ERP Systems\\nSAP/Oracle\\nReal-time CDC\\nKafka streams\\nSchema registry", 700, 120, "mxgraph.aws4.database"))
        
        # Ingestion Layer
        components.append(self._create_container("ingestion_layer", "Ingestion Layer - Event-Driven", 50, 280, 1200, 150, "#E8F5E8", "#4CAF50"))
        components.append(self._create_aws_component("s3_raw", "S3 Raw Landing\\nMultipart upload\\nEvent notifications\\nLifecycle: 30d → IA\\nCross-region replication", 100, 320, "mxgraph.aws4.s3"))
        components.append(self._create_aws_component("lambda_validator", "File Validator\\n1GB memory\\n15min timeout\\nDLQ enabled\\nX-Ray tracing\\nError handling", 250, 320, "mxgraph.aws4.lambda"))
        components.append(self._create_aws_component("sqs_validation", "Validation Queue\\nFIFO\\n5min visibility\\n3 retries\\nDLQ\\nMessage deduplication", 400, 320, "mxgraph.aws4.sqs"))
        components.append(self._create_aws_component("lambda_virus", "Virus Scanner\\nClamAV integration\\nQuarantine on detect\\n512MB memory\\nAsync processing", 550, 320, "mxgraph.aws4.lambda"))
        components.append(self._create_aws_component("s3_quarantine", "S3 Quarantine\\nFailed uploads\\nManual review\\nCompliance logging\\nAccess restricted", 700, 320, "mxgraph.aws4.s3"))
        
        # Processing Pipeline
        components.append(self._create_container("processing_pipeline", "Processing Pipeline - Microservices", 50, 480, 1200, 200, "#FCE4EC", "#E91E63"))
        
        # OCR Processing
        components.append(self._create_container("ocr_processing", "OCR Processing", 100, 520, 250, 120, "#FFF3E0", "#FF9800"))
        components.append(self._create_aws_component("fargate_ocr", "OCR Service\\n4vCPU/8GB\\nAuto scaling 2-20\\nSpot instances 70%\\nCircuit breaker", 120, 550, "mxgraph.aws4.fargate"))
        components.append(self._create_aws_component("textract", "Textract Async\\n>95% accuracy\\nForms + Tables\\nHandwriting\\nCustom models", 200, 550, "mxgraph.aws4.textract"))
        
        # Business Logic
        components.append(self._create_container("business_logic", "Business Logic", 400, 520, 350, 120, "#E8EAF6", "#3F51B5"))
        components.append(self._create_aws_component("fargate_invoice", "Invoice Service\\n2vCPU/4GB\\nBlue/Green deploy\\nHealth checks\\nMetrics", 420, 550, "mxgraph.aws4.fargate"))
        components.append(self._create_aws_component("fargate_product", "Product Service\\n4vCPU/8GB\\n60M products\\nElasticsearch\\nCache-aside", 500, 550, "mxgraph.aws4.fargate"))
        components.append(self._create_aws_component("fargate_commission", "Commission Service\\n2vCPU/4GB\\nDIAN compliance\\nAudit trail\\nRetry logic", 580, 550, "mxgraph.aws4.fargate"))
        
        # Integration
        components.append(self._create_container("integration", "Integration", 800, 520, 200, 120, "#F3E5F5", "#9C27B0"))
        components.append(self._create_aws_component("step_functions", "Step Functions\\nWorkflow orchestration\\nError handling\\nRetry logic\\nState machine", 820, 550, "mxgraph.aws4.step_functions"))
        components.append(self._create_aws_component("eventbridge", "EventBridge\\nCustom event bus\\nSchema registry\\nReplay capability\\nDLQ", 900, 550, "mxgraph.aws4.eventbridge"))
        
        # Data Storage
        components.append(self._create_container("data_storage", "Data Storage - Multi-Tier Architecture", 50, 720, 1200, 200, "#F5F5F5", "#666666"))
        
        # Hot Data
        components.append(self._create_container("hot_data", "Hot Data (< 1 day)", 100, 760, 300, 120, "#FFEBEE", "#D32F2F"))
        components.append(self._create_aws_component("redis_cluster", "Redis Cluster\\n6 nodes (3 shards)\\nMulti-AZ\\n99.9% availability\\nCluster mode", 120, 790, "mxgraph.aws4.elasticache"))
        components.append(self._create_aws_component("rds_primary", "RDS Primary\\nPostgreSQL 14\\ndb.r6g.2xlarge\\n35-day backup\\nPerformance Insights", 220, 790, "mxgraph.aws4.rds"))
        
        # Warm Data
        components.append(self._create_container("warm_data", "Warm Data (1-90 days)", 450, 760, 300, 120, "#E8F5E8", "#4CAF50"))
        components.append(self._create_aws_component("rds_replica", "Read Replica\\nCross-AZ replication\\nRead scaling\\nConnection pooling\\nLag monitoring", 470, 790, "mxgraph.aws4.rds"))
        components.append(self._create_aws_component("s3_processed", "S3 Processed\\nParquet format\\nPartitioned by date\\nCompression: GZIP\\nAthena optimized", 570, 790, "mxgraph.aws4.s3"))
        
        # Cold Data
        components.append(self._create_container("cold_data", "Cold Data (> 90 days)", 800, 760, 300, 120, "#E3F2FD", "#1976D2"))
        components.append(self._create_aws_component("s3_glacier", "S3 Glacier\\n7-year retention\\nCompliance archive\\nRestore: 12h\\nVault lock", 820, 790, "mxgraph.aws4.glacier"))
        components.append(self._create_aws_component("redshift", "Redshift Cluster\\ndc2.large x3\\nColumnar storage\\nBI analytics\\nSpectrum", 920, 790, "mxgraph.aws4.redshift"))
        
        # Conexiones de flujo de datos
        connections = [
            # Ingestion flows
            self._create_connection("web_portal", "s3_raw", "Upload", "#1976D2"),
            self._create_connection("mobile_app", "s3_raw", "Sync", "#1976D2"),
            self._create_connection("api_clients", "s3_raw", "API", "#1976D2"),
            self._create_connection("sftp_server", "s3_raw", "Batch", "#1976D2"),
            self._create_connection("erp_systems", "s3_raw", "CDC", "#1976D2"),
            
            # Processing flows
            self._create_connection("s3_raw", "lambda_validator", "Trigger", "#4CAF50"),
            self._create_connection("lambda_validator", "lambda_virus", "Validate", "#4CAF50"),
            self._create_connection("lambda_virus", "s3_quarantine", "Quarantine", "#FF5722"),
            self._create_connection("lambda_validator", "sqs_validation", "Queue", "#4CAF50"),
            self._create_connection("sqs_validation", "fargate_ocr", "Process", "#FF9800"),
            self._create_connection("fargate_ocr", "textract", "OCR", "#FF9800"),
            self._create_connection("textract", "step_functions", "Orchestrate", "#9C27B0"),
            self._create_connection("step_functions", "fargate_invoice", "Invoice", "#3F51B5"),
            self._create_connection("fargate_invoice", "fargate_product", "Product", "#3F51B5"),
            self._create_connection("fargate_product", "fargate_commission", "Commission", "#3F51B5"),
            self._create_connection("fargate_commission", "eventbridge", "Events", "#9C27B0"),
            
            # Data persistence flows
            self._create_connection("fargate_invoice", "redis_cluster", "Cache", "#D32F2F"),
            self._create_connection("fargate_product", "redis_cluster", "Cache", "#D32F2F"),
            self._create_connection("redis_cluster", "rds_primary", "Persist", "#D32F2F"),
            self._create_connection("rds_primary", "rds_replica", "Replicate", "#4CAF50"),
            self._create_connection("rds_primary", "s3_processed", "ETL", "#4CAF50"),
            self._create_connection("s3_processed", "s3_glacier", "Archive", "#1976D2"),
            self._create_connection("s3_processed", "redshift", "Analytics", "#1976D2")
        ]
        
        return self._build_diagram_xml(components + connections)
    
    def _combine_diagrams(self, diagrams: List, project_name: str) -> str:
        """Combina múltiples diagramas en un archivo"""
        
        xml_parts = [f'''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="{datetime.now().isoformat()}" version="22.1.11">''']
        
        for i, (name, diagram_xml) in enumerate(diagrams):
            xml_parts.append(f'''
  <diagram name="{name}" id="diagram_{i}">
    <mxGraphModel dx="2500" dy="1600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="1000">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        {diagram_xml}
      </root>
    </mxGraphModel>
  </diagram>''')
        
        xml_parts.append('</mxfile>')
        
        return ''.join(xml_parts)
    
    def _save_drawio_file(self, xml_content: str, project_name: str) -> str:
        """Guarda archivo DrawIO profesional"""
        
        output_dir = self.output_dir / "drawio" / project_name
        output_dir.mkdir(parents=True, exist_ok=True)
        
        filename = f"professional_architecture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.drawio"
        file_path = output_dir / filename
        
        file_path.write_text(xml_content, encoding='utf-8')
        
        print(f"✅ Professional DrawIO generado: {file_path}")
        return str(file_path)
