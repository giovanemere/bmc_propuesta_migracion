#!/usr/bin/env python3
"""
BMC AWS Architecture Diagram Generator - Draw.io + PNG
Generates both PNG and Draw.io (.drawio) files
"""

import json
import xml.etree.ElementTree as ET
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

class DrawIOGenerator:
    def __init__(self):
        self.shapes = []
        self.connections = []
        self.shape_id = 1
        
    def add_shape(self, name, shape_type="aws", x=100, y=100, width=120, height=80):
        shape = {
            "id": self.shape_id,
            "name": name,
            "type": shape_type,
            "x": x,
            "y": y,
            "width": width,
            "height": height
        }
        self.shapes.append(shape)
        self.shape_id += 1
        return shape["id"]
    
    def add_connection(self, source_id, target_id, label=""):
        connection = {
            "source": source_id,
            "target": target_id,
            "label": label
        }
        self.connections.append(connection)
    
    def generate_drawio_xml(self, title="BMC Architecture"):
        # Create basic Draw.io XML structure
        mxfile = ET.Element("mxfile", host="app.diagrams.net", modified="2024-01-01T00:00:00.000Z", agent="BMC Generator", version="22.1.11")
        diagram = ET.SubElement(mxfile, "diagram", name=title, id="diagram1")
        mxGraphModel = ET.SubElement(diagram, "mxGraphModel", dx="1422", dy="794", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="827", pageHeight="1169", math="0", shadow="0")
        root = ET.SubElement(mxGraphModel, "root")
        
        # Add default cells
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        
        # Add shapes
        for shape in self.shapes:
            cell = ET.SubElement(root, "mxCell", 
                id=str(shape["id"]), 
                value=shape["name"], 
                style=f"rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;",
                vertex="1", 
                parent="1"
            )
            geometry = ET.SubElement(cell, "mxGeometry", 
                x=str(shape["x"]), 
                y=str(shape["y"]), 
                width=str(shape["width"]), 
                height=str(shape["height"]), 
                as_="geometry"
            )
        
        # Add connections
        for conn in self.connections:
            cell = ET.SubElement(root, "mxCell", 
                id=f"edge_{conn['source']}_{conn['target']}", 
                value=conn["label"], 
                style="endArrow=classic;html=1;rounded=0;",
                edge="1", 
                parent="1", 
                source=str(conn["source"]), 
                target=str(conn["target"])
            )
            geometry = ET.SubElement(cell, "mxGeometry", relative="1", as_="geometry")
        
        return ET.tostring(mxfile, encoding='unicode')

def generate_main_architecture_png():
    """Generate main BMC architecture PNG"""
    
    with Diagram("BMC AWS Architecture - 60M Products Platform", 
                 filename="bmc_main_architecture", 
                 show=False, 
                 direction="TB"):
        
        users = Users("BMC Users")
        
        with Cluster("AWS Cloud"):
            with Cluster("Edge & Security"):
                cloudfront = CloudFront("CloudFront CDN")
                waf = WAF("AWS WAF")
                
            with Cluster("API Gateway"):
                api_gateway = APIGateway("API Gateway")
                cognito = Cognito("User Auth")
                
            alb = ELB("Application LB")
                
            with Cluster("Microservices (ECS Fargate)"):
                invoice_service = Fargate("Invoice Service\n2 vCPU, 4GB")
                product_service = Fargate("Product Service\n4 vCPU, 8GB\n60M Products")
                ocr_service = Fargate("OCR Service\n2 vCPU, 4GB")
            
            with Cluster("Lambda Functions"):
                ocr_processor = Lambda("OCR Processor")
                
            textract = Textract("Amazon Textract\nOCR >95%")
                
            with Cluster("Data Layer"):
                rds_primary = RDS("RDS PostgreSQL\n60M Products\nMulti-AZ")
                redis = Elasticache("ElastiCache Redis\nProduct Cache\n24h TTL")
                s3_docs = S3("S3 Documents\nIntelligent Tiering")
                    
            with Cluster("Event-Driven Integration"):
                sqs_fifo = SQS("SQS FIFO\nInvoice Queue")
                sns = SNS("SNS\nNotifications")
                
            cloudwatch = Cloudwatch("CloudWatch\nMetrics & Logs")
        
        dian_api = Internet("DIAN API\nTax Authority")
        
        # Connections
        users >> cloudfront >> waf >> api_gateway >> cognito
        api_gateway >> alb >> [invoice_service, product_service, ocr_service]
        invoice_service >> ocr_processor >> textract
        product_service >> redis >> rds_primary
        ocr_service >> s3_docs
        invoice_service >> sqs_fifo >> sns
        product_service >> dian_api
        [invoice_service, product_service, ocr_service] >> cloudwatch

def generate_main_architecture_drawio():
    """Generate main BMC architecture Draw.io file"""
    
    generator = DrawIOGenerator()
    
    # Add shapes with positions
    users_id = generator.add_shape("BMC Users", x=50, y=50)
    cloudfront_id = generator.add_shape("CloudFront CDN", x=200, y=50)
    waf_id = generator.add_shape("AWS WAF", x=350, y=50)
    api_gateway_id = generator.add_shape("API Gateway", x=500, y=50)
    cognito_id = generator.add_shape("User Auth\nCognito", x=650, y=50)
    
    alb_id = generator.add_shape("Application LB", x=400, y=150)
    
    # Microservices
    invoice_id = generator.add_shape("Invoice Service\n2 vCPU, 4GB", x=200, y=250)
    product_id = generator.add_shape("Product Service\n4 vCPU, 8GB\n60M Products", x=400, y=250)
    ocr_id = generator.add_shape("OCR Service\n2 vCPU, 4GB", x=600, y=250)
    
    # Lambda
    ocr_processor_id = generator.add_shape("OCR Processor\nLambda", x=750, y=250)
    textract_id = generator.add_shape("Amazon Textract\nOCR >95%", x=900, y=250)
    
    # Data Layer
    rds_id = generator.add_shape("RDS PostgreSQL\n60M Products\nMulti-AZ", x=200, y=400)
    redis_id = generator.add_shape("ElastiCache Redis\nProduct Cache\n24h TTL", x=400, y=400)
    s3_id = generator.add_shape("S3 Documents\nIntelligent Tiering", x=600, y=400)
    
    # Integration
    sqs_id = generator.add_shape("SQS FIFO\nInvoice Queue", x=100, y=550)
    sns_id = generator.add_shape("SNS\nNotifications", x=300, y=550)
    
    # Monitoring
    cloudwatch_id = generator.add_shape("CloudWatch\nMetrics & Logs", x=500, y=550)
    
    # External
    dian_id = generator.add_shape("DIAN API\nTax Authority", x=800, y=400)
    
    # Add connections
    generator.add_connection(users_id, cloudfront_id)
    generator.add_connection(cloudfront_id, waf_id)
    generator.add_connection(waf_id, api_gateway_id)
    generator.add_connection(api_gateway_id, cognito_id)
    generator.add_connection(api_gateway_id, alb_id)
    
    generator.add_connection(alb_id, invoice_id)
    generator.add_connection(alb_id, product_id)
    generator.add_connection(alb_id, ocr_id)
    
    generator.add_connection(invoice_id, ocr_processor_id)
    generator.add_connection(ocr_processor_id, textract_id)
    generator.add_connection(product_id, redis_id)
    generator.add_connection(redis_id, rds_id)
    generator.add_connection(ocr_id, s3_id)
    
    generator.add_connection(invoice_id, sqs_id)
    generator.add_connection(sqs_id, sns_id)
    generator.add_connection(product_id, dian_id)
    
    generator.add_connection(invoice_id, cloudwatch_id)
    generator.add_connection(product_id, cloudwatch_id)
    generator.add_connection(ocr_id, cloudwatch_id)
    
    # Generate XML
    xml_content = generator.generate_drawio_xml("BMC AWS Architecture - 60M Products Platform")
    
    # Save to file
    with open("bmc_main_architecture.drawio", "w", encoding="utf-8") as f:
        f.write(xml_content)
    
    return "bmc_main_architecture.drawio"

def generate_microservices_drawio():
    """Generate microservices Draw.io file"""
    
    generator = DrawIOGenerator()
    
    # API Gateway
    api_id = generator.add_shape("API Gateway\nCentral Router", x=400, y=50)
    
    # Load Balancers
    invoice_alb_id = generator.add_shape("Invoice ALB", x=200, y=150)
    product_alb_id = generator.add_shape("Product ALB", x=400, y=150)
    ocr_alb_id = generator.add_shape("OCR ALB", x=600, y=150)
    
    # Tasks
    invoice_task1_id = generator.add_shape("Invoice Task 1\n2 vCPU, 4GB", x=100, y=250)
    invoice_task2_id = generator.add_shape("Invoice Task 2\n2 vCPU, 4GB", x=300, y=250)
    
    product_task1_id = generator.add_shape("Product Task 1\n4 vCPU, 8GB", x=350, y=250)
    product_task2_id = generator.add_shape("Product Task 2\n4 vCPU, 8GB", x=450, y=250)
    
    ocr_task1_id = generator.add_shape("OCR Task 1\n2 vCPU, 4GB", x=550, y=250)
    ocr_task2_id = generator.add_shape("OCR Task 2\n2 vCPU, 4GB", x=650, y=250)
    
    # Data Services
    rds_id = generator.add_shape("RDS PostgreSQL\nMulti-AZ\n60M Products", x=200, y=400)
    redis_id = generator.add_shape("ElastiCache Redis\nCluster Mode", x=400, y=400)
    s3_id = generator.add_shape("S3 Buckets\nDocuments", x=600, y=400)
    
    textract_id = generator.add_shape("Amazon Textract\nOCR Processing", x=800, y=300)
    sqs_id = generator.add_shape("SQS Queues\nFIFO & Standard", x=100, y=500)
    
    # Connections
    generator.add_connection(api_id, invoice_alb_id)
    generator.add_connection(api_id, product_alb_id)
    generator.add_connection(api_id, ocr_alb_id)
    
    generator.add_connection(invoice_alb_id, invoice_task1_id)
    generator.add_connection(invoice_alb_id, invoice_task2_id)
    generator.add_connection(product_alb_id, product_task1_id)
    generator.add_connection(product_alb_id, product_task2_id)
    generator.add_connection(ocr_alb_id, ocr_task1_id)
    generator.add_connection(ocr_alb_id, ocr_task2_id)
    
    generator.add_connection(invoice_task1_id, rds_id)
    generator.add_connection(product_task1_id, redis_id)
    generator.add_connection(ocr_task1_id, s3_id)
    generator.add_connection(ocr_task1_id, textract_id)
    
    generator.add_connection(invoice_task1_id, sqs_id)
    
    # Generate XML
    xml_content = generator.generate_drawio_xml("BMC Microservices Architecture - ECS Fargate")
    
    with open("bmc_microservices_detail.drawio", "w", encoding="utf-8") as f:
        f.write(xml_content)
    
    return "bmc_microservices_detail.drawio"

def main():
    print("🚀 BMC AWS Architecture Generator - PNG + Draw.io")
    print("=" * 55)
    
    # Generate PNG diagrams
    print("\n📊 Generating PNG diagrams...")
    generate_main_architecture_png()
    print("✓ Main architecture PNG generated")
    
    # Generate Draw.io diagrams
    print("\n🎨 Generating Draw.io diagrams...")
    drawio_main = generate_main_architecture_drawio()
    print(f"✓ Main architecture Draw.io generated: {drawio_main}")
    
    drawio_micro = generate_microservices_drawio()
    print(f"✓ Microservices Draw.io generated: {drawio_micro}")
    
    print("\n✅ All diagrams generated successfully!")
    print("\n📁 Files created:")
    print("PNG Files:")
    print("- bmc_main_architecture.png")
    print("\nDraw.io Files:")
    print("- bmc_main_architecture.drawio")
    print("- bmc_microservices_detail.drawio")
    
    print("\n💡 Usage:")
    print("- PNG files: Use in presentations and documents")
    print("- Draw.io files: Open in draw.io for editing")

if __name__ == "__main__":
    main()
