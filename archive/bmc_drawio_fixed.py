#!/usr/bin/env python3
"""
BMC AWS Architecture Diagram Generator - Draw.io Fixed
Generates PNG and Draw.io files with unique IDs
"""

import json
import xml.etree.ElementTree as ET
from diagrams import Diagram, Cluster
from diagrams.aws.compute import Fargate, Lambda
from diagrams.aws.database import RDS, Elasticache
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
        self.shape_id = 10  # Start from 10 to avoid conflicts
        
    def add_shape(self, name, shape_type="aws", x=100, y=100, width=120, height=80):
        shape = {
            "id": f"shape_{self.shape_id}",
            "name": name,
            "type": shape_type,
            "x": x,
            "y": y,
            "width": width,
            "height": height
        }
        self.shapes.append(shape)
        current_id = shape["id"]
        self.shape_id += 1
        return current_id
    
    def add_connection(self, source_id, target_id, label=""):
        connection = {
            "id": f"edge_{self.shape_id}",
            "source": source_id,
            "target": target_id,
            "label": label
        }
        self.connections.append(connection)
        self.shape_id += 1
    
    def generate_drawio_xml(self, title="BMC Architecture"):
        mxfile = ET.Element("mxfile", host="app.diagrams.net")
        diagram = ET.SubElement(mxfile, "diagram", name=title, id="diagram1")
        mxGraphModel = ET.SubElement(diagram, "mxGraphModel", dx="1422", dy="794", grid="1", gridSize="10")
        root = ET.SubElement(mxGraphModel, "root")
        
        # Default cells with unique IDs
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        
        # Add shapes
        for shape in self.shapes:
            cell = ET.SubElement(root, "mxCell", 
                id=shape["id"], 
                value=shape["name"], 
                style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;",
                vertex="1", 
                parent="1"
            )
            ET.SubElement(cell, "mxGeometry", 
                x=str(shape["x"]), 
                y=str(shape["y"]), 
                width=str(shape["width"]), 
                height=str(shape["height"]), 
                as_="geometry"
            )
        
        # Add connections
        for conn in self.connections:
            cell = ET.SubElement(root, "mxCell", 
                id=conn["id"], 
                value=conn["label"], 
                style="endArrow=classic;html=1;rounded=0;",
                edge="1", 
                parent="1", 
                source=conn["source"], 
                target=conn["target"]
            )
            ET.SubElement(cell, "mxGeometry", relative="1", as_="geometry")
        
        return ET.tostring(mxfile, encoding='unicode')

def generate_main_architecture_png():
    """Generate PNG"""
    with Diagram("BMC AWS Architecture", filename="bmc_main_architecture", show=False):
        users = Users("BMC Users")
        with Cluster("AWS Cloud"):
            api_gateway = APIGateway("API Gateway")
            alb = ELB("Application LB")
            invoice_service = Fargate("Invoice Service")
            product_service = Fargate("Product Service\n60M Products")
            rds = RDS("RDS PostgreSQL")
            redis = Elasticache("Redis Cache")
            s3 = S3("S3 Documents")
            
        users >> api_gateway >> alb >> [invoice_service, product_service]
        product_service >> redis >> rds
        invoice_service >> s3

def generate_main_architecture_drawio():
    """Generate Draw.io with unique IDs"""
    generator = DrawIOGenerator()
    
    # Add shapes with unique positions
    users_id = generator.add_shape("BMC Users", x=50, y=50)
    api_id = generator.add_shape("API Gateway", x=200, y=50)
    alb_id = generator.add_shape("Application LB", x=350, y=50)
    
    invoice_id = generator.add_shape("Invoice Service\n2 vCPU, 4GB", x=200, y=150)
    product_id = generator.add_shape("Product Service\n60M Products", x=400, y=150)
    
    rds_id = generator.add_shape("RDS PostgreSQL\n60M Products", x=200, y=250)
    redis_id = generator.add_shape("Redis Cache\n24h TTL", x=400, y=250)
    s3_id = generator.add_shape("S3 Documents", x=600, y=250)
    
    # Add connections
    generator.add_connection(users_id, api_id)
    generator.add_connection(api_id, alb_id)
    generator.add_connection(alb_id, invoice_id)
    generator.add_connection(alb_id, product_id)
    generator.add_connection(product_id, redis_id)
    generator.add_connection(redis_id, rds_id)
    generator.add_connection(invoice_id, s3_id)
    
    # Generate and save
    xml_content = generator.generate_drawio_xml("BMC AWS Architecture")
    with open("bmc_main_architecture.drawio", "w", encoding="utf-8") as f:
        f.write(xml_content)
    
    return "bmc_main_architecture.drawio"

def main():
    print("🚀 BMC Diagram Generator - Fixed IDs")
    print("=" * 40)
    
    # Generate PNG
    print("📊 Generating PNG...")
    generate_main_architecture_png()
    print("✓ PNG generated")
    
    # Generate Draw.io
    print("🎨 Generating Draw.io...")
    drawio_file = generate_main_architecture_drawio()
    print(f"✓ Draw.io generated: {drawio_file}")
    
    print("\n✅ All diagrams generated successfully!")

if __name__ == "__main__":
    main()
