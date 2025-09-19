#!/usr/bin/env python3
"""
Complete Draw.io Generator - Genera archivos Draw.io equivalentes a todos los PNG
"""

import os
from typing import Dict, Any

class CompleteDrawioGenerator:
    """Generador completo de archivos Draw.io para todos los diagramas PNG"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str = "output"):
        self.config = config
        self.output_dir = output_dir
        
    def generate_main_architecture_drawio(self, project_name: str) -> str:
        """Genera Draw.io para arquitectura principal"""
        
        xml_content = f'''<mxfile host="app.diagrams.net">
  <diagram name="{project_name} - Main Architecture" id="main_arch">
    <mxGraphModel dx="1800" dy="1000" grid="1" gridSize="10">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Title -->
        <mxCell id="title" value="{project_name} AWS Architecture - Main" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=none;fontColor=#FFFFFF;fontSize=18;fontStyle=1;align=center;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1500" height="50" as="geometry"/>
        </mxCell>
        
        <!-- Users -->
        <mxCell id="users" value="Users&#10;10K concurrent" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;shape=mxgraph.aws4.users;" vertex="1" parent="1">
          <mxGeometry x="100" y="120" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- AWS Cloud -->
        <mxCell id="aws" value="AWS Cloud" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;strokeWidth=3;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=15;" vertex="1" parent="1">
          <mxGeometry x="200" y="100" width="1200" height="600" as="geometry"/>
        </mxCell>
        
        <!-- CloudFront -->
        <mxCell id="cloudfront" value="CloudFront&#10;CDN" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.cloudfront;" vertex="1" parent="1">
          <mxGeometry x="250" y="150" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- API Gateway -->
        <mxCell id="api" value="API Gateway&#10;REST/GraphQL" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;shape=mxgraph.aws4.api_gateway;" vertex="1" parent="1">
          <mxGeometry x="400" y="150" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- ECS Fargate -->
        <mxCell id="ecs" value="ECS Fargate&#10;Microservices" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="600" y="250" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- RDS -->
        <mxCell id="rds" value="RDS&#10;PostgreSQL&#10;60M Products" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;shape=mxgraph.aws4.rds;" vertex="1" parent="1">
          <mxGeometry x="400" y="400" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Redis -->
        <mxCell id="redis" value="Redis&#10;Cache" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;shape=mxgraph.aws4.elasticache;" vertex="1" parent="1">
          <mxGeometry x="600" y="400" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- S3 -->
        <mxCell id="s3" value="S3&#10;Documents" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;shape=mxgraph.aws4.s3;" vertex="1" parent="1">
          <mxGeometry x="800" y="400" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Textract -->
        <mxCell id="textract" value="Textract&#10;OCR >95%" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;shape=mxgraph.aws4.textract;" vertex="1" parent="1">
          <mxGeometry x="1000" y="250" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Connections -->
        <mxCell id="c1" style="endArrow=classic;html=1;strokeColor=#1976D2;strokeWidth=2;" edge="1" parent="1" source="users" target="cloudfront"/>
        <mxCell id="c2" style="endArrow=classic;html=1;strokeColor=#FF9800;strokeWidth=2;" edge="1" parent="1" source="cloudfront" target="api"/>
        <mxCell id="c3" style="endArrow=classic;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="api" target="ecs"/>
        <mxCell id="c4" style="endArrow=classic;html=1;strokeColor=#9C27B0;strokeWidth=2;" edge="1" parent="1" source="ecs" target="redis"/>
        <mxCell id="c5" style="endArrow=classic;html=1;strokeColor=#9C27B0;strokeWidth=2;" edge="1" parent="1" source="redis" target="rds"/>
        <mxCell id="c6" style="endArrow=classic;html=1;strokeColor=#E91E63;strokeWidth=2;" edge="1" parent="1" source="ecs" target="s3"/>
        <mxCell id="c7" style="endArrow=classic;html=1;strokeColor=#E91E63;strokeWidth=2;" edge="1" parent="1" source="s3" target="textract"/>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
        
        output_file = f"{self.output_dir}/drawio/{project_name.lower()}_architecture.drawio"
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        
        return output_file
    
    def generate_microservices_drawio(self, project_name: str) -> str:
        """Genera Draw.io para microservicios detallados"""
        
        xml_content = f'''<mxfile host="app.diagrams.net">
  <diagram name="{project_name} - Microservices Detail" id="microservices">
    <mxGraphModel dx="1800" dy="1000" grid="1" gridSize="10">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Title -->
        <mxCell id="title" value="{project_name} Microservices - ECS Fargate" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=none;fontColor=#FFFFFF;fontSize=18;fontStyle=1;align=center;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1500" height="50" as="geometry"/>
        </mxCell>
        
        <!-- API Gateway -->
        <mxCell id="api" value="API Gateway&#10;Central Router" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;shape=mxgraph.aws4.api_gateway;" vertex="1" parent="1">
          <mxGeometry x="400" y="120" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- ECS Cluster -->
        <mxCell id="cluster" value="ECS Fargate Cluster - Auto Scaling" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#4CAF50;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=15;" vertex="1" parent="1">
          <mxGeometry x="100" y="200" width="1200" height="300" as="geometry"/>
        </mxCell>
        
        <!-- Invoice Service -->
        <mxCell id="invoice_alb" value="Invoice ALB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#8C4FFF;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;shape=mxgraph.aws4.application_load_balancer;" vertex="1" parent="1">
          <mxGeometry x="200" y="250" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="invoice1" value="Invoice Task 1&#10;2vCPU/4GB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="150" y="350" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="invoice2" value="Invoice Task 2&#10;2vCPU/4GB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="250" y="350" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Product Service -->
        <mxCell id="product_alb" value="Product ALB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#8C4FFF;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;shape=mxgraph.aws4.application_load_balancer;" vertex="1" parent="1">
          <mxGeometry x="500" y="250" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="product1" value="Product Task 1&#10;4vCPU/8GB&#10;60M Records" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="400" y="350" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="product2" value="Product Task 2&#10;4vCPU/8GB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="500" y="350" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="product3" value="Product Task 3&#10;4vCPU/8GB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="600" y="350" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- OCR Service -->
        <mxCell id="ocr_alb" value="OCR ALB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#8C4FFF;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;shape=mxgraph.aws4.application_load_balancer;" vertex="1" parent="1">
          <mxGeometry x="800" y="250" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="ocr1" value="OCR Task 1&#10;2vCPU/4GB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="750" y="350" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="ocr2" value="OCR Task 2&#10;2vCPU/4GB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="850" y="350" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Data Services -->
        <mxCell id="data" value="Data Services - Multi-AZ" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4EC;strokeColor=#E91E63;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=15;" vertex="1" parent="1">
          <mxGeometry x="100" y="550" width="800" height="150" as="geometry"/>
        </mxCell>
        
        <mxCell id="rds" value="RDS PostgreSQL&#10;Multi-AZ&#10;60M Products" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;shape=mxgraph.aws4.rds;" vertex="1" parent="1">
          <mxGeometry x="200" y="600" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="redis" value="ElastiCache Redis&#10;Cluster Mode&#10;24h TTL" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;shape=mxgraph.aws4.elasticache;" vertex="1" parent="1">
          <mxGeometry x="400" y="600" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="s3" value="S3 Documents&#10;Intelligent Tiering" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;shape=mxgraph.aws4.s3;" vertex="1" parent="1">
          <mxGeometry x="600" y="600" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Connections -->
        <mxCell id="c1" style="endArrow=classic;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="api" target="invoice_alb"/>
        <mxCell id="c2" style="endArrow=classic;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="api" target="product_alb"/>
        <mxCell id="c3" style="endArrow=classic;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="api" target="ocr_alb"/>
        
        <mxCell id="c4" style="endArrow=classic;html=1;strokeColor=#9C27B0;strokeWidth=2;" edge="1" parent="1" source="invoice_alb" target="invoice1"/>
        <mxCell id="c5" style="endArrow=classic;html=1;strokeColor=#9C27B0;strokeWidth=2;" edge="1" parent="1" source="invoice_alb" target="invoice2"/>
        
        <mxCell id="c6" style="endArrow=classic;html=1;strokeColor=#9C27B0;strokeWidth=2;" edge="1" parent="1" source="product_alb" target="product1"/>
        <mxCell id="c7" style="endArrow=classic;html=1;strokeColor=#9C27B0;strokeWidth=2;" edge="1" parent="1" source="product_alb" target="product2"/>
        <mxCell id="c8" style="endArrow=classic;html=1;strokeColor=#9C27B0;strokeWidth=2;" edge="1" parent="1" source="product_alb" target="product3"/>
        
        <mxCell id="c9" style="endArrow=classic;html=1;strokeColor=#E91E63;strokeWidth=2;" edge="1" parent="1" source="product1" target="redis"/>
        <mxCell id="c10" style="endArrow=classic;html=1;strokeColor=#E91E63;strokeWidth=2;" edge="1" parent="1" source="redis" target="rds"/>
        <mxCell id="c11" style="endArrow=classic;html=1;strokeColor=#E91E63;strokeWidth=2;" edge="1" parent="1" source="ocr1" target="s3"/>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
        
        output_file = f"{self.output_dir}/drawio/{project_name.lower()}_microservices.drawio"
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        
        return output_file
    
    def generate_all_drawio_files(self, project_name: str = "BMC") -> Dict[str, str]:
        """Genera todos los archivos Draw.io equivalentes a los PNG"""
        
        results = {}
        
        print(f"🎨 Generating Draw.io files for {project_name}...")
        
        # Arquitectura principal
        results["architecture"] = self.generate_main_architecture_drawio(project_name)
        print("✓ Main architecture Draw.io generated")
        
        # Microservicios detallados
        results["microservices"] = self.generate_microservices_drawio(project_name)
        print("✓ Microservices Draw.io generated")
        
        return results
    
    def generate_network_drawio(self, project_name: str) -> str:
        """Genera todos los archivos Draw.io equivalentes a los PNG"""
        
        results = {}
        
        print(f"🎨 Generating Draw.io files for {project_name}...")
        
        # Arquitectura principal
        results["architecture"] = self.generate_main_architecture_drawio(project_name)
        print("✓ Main architecture Draw.io generated")
        
        # Microservicios detallados
        results["microservices"] = self.generate_microservices_drawio(project_name)
        print("✓ Microservices Draw.io generated")
        
        # Arquitectura de red
        results["network"] = self.generate_network_drawio(project_name)
        print("✓ Network architecture Draw.io generated")
        
        return results
        """Genera Draw.io para arquitectura de red"""
        
        xml_content = f'''<mxfile host="app.diagrams.net">
  <diagram name="{project_name} - Network Architecture" id="network">
    <mxGraphModel dx="1800" dy="1000" grid="1" gridSize="10">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Title -->
        <mxCell id="title" value="{project_name} Network Architecture &amp; VPC" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=none;fontColor=#FFFFFF;fontSize=18;fontStyle=1;align=center;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1500" height="50" as="geometry"/>
        </mxCell>
        
        <!-- Internet -->
        <mxCell id="internet" value="Internet" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#607D8B;strokeColor=none;shape=mxgraph.aws4.internet_gateway;" vertex="1" parent="1">
          <mxGeometry x="100" y="120" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- AWS Cloud -->
        <mxCell id="aws" value="AWS Cloud - us-east-1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;strokeWidth=3;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=15;" vertex="1" parent="1">
          <mxGeometry x="200" y="100" width="1200" height="700" as="geometry"/>
        </mxCell>
        
        <!-- VPC -->
        <mxCell id="vpc" value="VPC 10.0.0.0/16" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#9E9E9E;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="250" y="150" width="1100" height="600" as="geometry"/>
        </mxCell>
        
        <!-- AZ 1a -->
        <mxCell id="az1a" value="AZ us-east-1a" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#4CAF50;strokeWidth=2;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="300" y="200" width="500" height="250" as="geometry"/>
        </mxCell>
        
        <!-- Public Subnet 1a -->
        <mxCell id="pub1a" value="Public Subnet&#10;10.0.1.0/24" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#FF9800;strokeWidth=1;fontSize=10;fontStyle=1;verticalAlign=top;spacingTop=8;" vertex="1" parent="1">
          <mxGeometry x="320" y="230" width="200" height="80" as="geometry"/>
        </mxCell>
        
        <mxCell id="nat1a" value="NAT Gateway 1A" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#8C4FFF;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;shape=mxgraph.aws4.nat_gateway;" vertex="1" parent="1">
          <mxGeometry x="400" y="250" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Private Subnet 1a -->
        <mxCell id="priv1a" value="Private Subnet&#10;10.0.10.0/24" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1F5FE;strokeColor=#0277BD;strokeWidth=1;fontSize=10;fontStyle=1;verticalAlign=top;spacingTop=8;" vertex="1" parent="1">
          <mxGeometry x="320" y="330" width="200" height="80" as="geometry"/>
        </mxCell>
        
        <mxCell id="app1a" value="App Services 1A" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="400" y="350" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- AZ 1b -->
        <mxCell id="az1b" value="AZ us-east-1b" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#FF9800;strokeWidth=2;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="850" y="200" width="500" height="250" as="geometry"/>
        </mxCell>
        
        <!-- Public Subnet 1b -->
        <mxCell id="pub1b" value="Public Subnet&#10;10.0.2.0/24" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#FF9800;strokeWidth=1;fontSize=10;fontStyle=1;verticalAlign=top;spacingTop=8;" vertex="1" parent="1">
          <mxGeometry x="870" y="230" width="200" height="80" as="geometry"/>
        </mxCell>
        
        <mxCell id="nat1b" value="NAT Gateway 1B" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#8C4FFF;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;shape=mxgraph.aws4.nat_gateway;" vertex="1" parent="1">
          <mxGeometry x="950" y="250" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Private Subnet 1b -->
        <mxCell id="priv1b" value="Private Subnet&#10;10.0.11.0/24" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1F5FE;strokeColor=#0277BD;strokeWidth=1;fontSize=10;fontStyle=1;verticalAlign=top;spacingTop=8;" vertex="1" parent="1">
          <mxGeometry x="870" y="330" width="200" height="80" as="geometry"/>
        </mxCell>
        
        <mxCell id="app1b" value="App Services 1B" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="950" y="350" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Database Subnets -->
        <mxCell id="db_subnet" value="Database Subnets - Isolated" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4EC;strokeColor=#E91E63;strokeWidth=2;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="300" y="500" width="1000" height="150" as="geometry"/>
        </mxCell>
        
        <mxCell id="rds1a" value="RDS Primary&#10;us-east-1a" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;shape=mxgraph.aws4.rds;" vertex="1" parent="1">
          <mxGeometry x="500" y="550" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="rds1b" value="RDS Standby&#10;us-east-1b" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;shape=mxgraph.aws4.rds;" vertex="1" parent="1">
          <mxGeometry x="900" y="550" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Edge Services -->
        <mxCell id="edge" value="Edge Layer" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFEBEE;strokeColor=#F44336;strokeWidth=2;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="600" y="680" width="400" height="100" as="geometry"/>
        </mxCell>
        
        <mxCell id="cloudfront" value="CloudFront&#10;Global Edge" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.cloudfront;" vertex="1" parent="1">
          <mxGeometry x="650" y="720" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="waf" value="AWS WAF&#10;DDoS Protection" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;shape=mxgraph.aws4.waf;" vertex="1" parent="1">
          <mxGeometry x="750" y="720" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="api" value="API Gateway" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;shape=mxgraph.aws4.api_gateway;" vertex="1" parent="1">
          <mxGeometry x="850" y="720" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Connections -->
        <mxCell id="c1" style="endArrow=classic;html=1;strokeColor=#1976D2;strokeWidth=3;" edge="1" parent="1" source="internet" target="cloudfront"/>
        <mxCell id="c2" style="endArrow=classic;html=1;strokeColor=#FF9800;strokeWidth=2;" edge="1" parent="1" source="cloudfront" target="waf"/>
        <mxCell id="c3" style="endArrow=classic;html=1;strokeColor=#FF9800;strokeWidth=2;" edge="1" parent="1" source="waf" target="api"/>
        <mxCell id="c4" style="endArrow=classic;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="api" target="app1a"/>
        <mxCell id="c5" style="endArrow=classic;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="api" target="app1b"/>
        <mxCell id="c6" style="endArrow=classic;html=1;strokeColor=#E91E63;strokeWidth=2;" edge="1" parent="1" source="app1a" target="rds1a"/>
        <mxCell id="c7" style="endArrow=classic;html=1;strokeColor=#E91E63;strokeWidth=2;" edge="1" parent="1" source="app1b" target="rds1b"/>
        <mxCell id="c8" style="endArrow=classic;html=1;strokeColor=#9C27B0;strokeWidth=1;dashed=1;" edge="1" parent="1" source="rds1a" target="rds1b"/>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
        
        output_file = f"{self.output_dir}/drawio/{project_name.lower()}_network_architecture.drawio"
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        
        return output_file
