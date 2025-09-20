#!/usr/bin/env python3
"""
AWS DrawIO Generator - Genera DrawIO con iconos AWS reales
Usa la misma lógica del PNG pero genera DrawIO con iconos profesionales
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

class AWSDrawIOGenerator:
    """Generador DrawIO con iconos AWS reales"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str):
        self.config = config
        self.output_dir = Path(output_dir)
        
        # Iconos AWS reales (shapes de draw.io)
        self.aws_shapes = {
            # Compute
            "fargate": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;",
            
            # Database
            "rds": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.rds;",
            
            "elasticache": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elasticache;",
            
            # Storage
            "s3": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;",
            
            # Network
            "api_gateway": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.api_gateway;",
            
            "cloudfront": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudfront;",
            
            "elb": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#8C4FFF;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elastic_load_balancing;",
            
            "vpc": "fillColor=none;strokeColor=#147EBA;dashed=1;verticalAlign=top;fontStyle=0;fontColor=#147EBA;whiteSpace=wrap;html=1;",
            
            # Security
            "cognito": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cognito;",
            
            "waf": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.waf;",
            
            # Generic
            "internet": "sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.internet_gateway;",
            
            "users": "sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.users;"
        }
        
    def generate_aws_architecture_drawio(self, project_name: str = "bmc_input") -> str:
        """Genera DrawIO con iconos AWS reales usando la misma lógica del PNG"""
        
        # Crear XML DrawIO
        mxfile = ET.Element("mxfile", host="app.diagrams.net")
        diagram = ET.SubElement(mxfile, "diagram", name=f"{project_name} AWS Architecture", id="aws_arch")
        model = ET.SubElement(diagram, "mxGraphModel", dx="2400", dy="1600", grid="1", gridSize="10")
        root = ET.SubElement(model, "root")
        
        # Celdas base
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        
        cell_id = 2
        
        # Título
        title_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value=f"{project_name.upper()} - AWS Architecture with Real Icons",
            style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;fontColor=#FFFFFF;fontSize=20;fontStyle=1;",
            vertex="1", parent="1"
        )
        ET.SubElement(title_cell, "mxGeometry", x="50", y="20", width="2000", height="60", **{"as": "geometry"})
        cell_id += 1
        
        # Internet (icono AWS real)
        internet_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Internet",
            style=self.aws_shapes["internet"],
            vertex="1", parent="1"
        )
        ET.SubElement(internet_cell, "mxGeometry", x="100", y="120", width="78", height="78", **{"as": "geometry"})
        cell_id += 1
        
        # Users (icono AWS real)
        users_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="BMC Users\\n10K concurrent",
            style=self.aws_shapes["users"],
            vertex="1", parent="1"
        )
        ET.SubElement(users_cell, "mxGeometry", x="300", y="120", width="78", height="78", **{"as": "geometry"})
        cell_id += 1
        
        # AWS Cloud VPC
        vpc_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="AWS Cloud - VPC 10.0.0.0/16",
            style=self.aws_shapes["vpc"],
            vertex="1", parent="1"
        )
        ET.SubElement(vpc_cell, "mxGeometry", x="50", y="250", width="1900", height="1200", **{"as": "geometry"})
        vpc_id = cell_id
        cell_id += 1
        
        # CloudFront (icono AWS real)
        cloudfront_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="CloudFront CDN\\nGlobal Edge",
            style=self.aws_shapes["cloudfront"],
            vertex="1", parent=str(vpc_id)
        )
        ET.SubElement(cloudfront_cell, "mxGeometry", x="100", y="50", width="78", height="78", **{"as": "geometry"})
        cell_id += 1
        
        # WAF (icono AWS real)
        waf_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="AWS WAF\\nDDoS Protection",
            style=self.aws_shapes["waf"],
            vertex="1", parent=str(vpc_id)
        )
        ET.SubElement(waf_cell, "mxGeometry", x="250", y="50", width="78", height="78", **{"as": "geometry"})
        cell_id += 1
        
        # API Gateway (icono AWS real)
        api_gw_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="API Gateway\\nREST + GraphQL",
            style=self.aws_shapes["api_gateway"],
            vertex="1", parent=str(vpc_id)
        )
        ET.SubElement(api_gw_cell, "mxGeometry", x="400", y="50", width="78", height="78", **{"as": "geometry"})
        cell_id += 1
        
        # Application Load Balancer (icono AWS real)
        alb_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Application LB\\nMulti-AZ",
            style=self.aws_shapes["elb"],
            vertex="1", parent=str(vpc_id)
        )
        ET.SubElement(alb_cell, "mxGeometry", x="550", y="50", width="78", height="78", **{"as": "geometry"})
        cell_id += 1
        
        # Cognito (icono AWS real)
        cognito_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Cognito\\nUser Pool",
            style=self.aws_shapes["cognito"],
            vertex="1", parent=str(vpc_id)
        )
        ET.SubElement(cognito_cell, "mxGeometry", x="700", y="50", width="78", height="78", **{"as": "geometry"})
        cell_id += 1
        
        # Microservicios con Fargate (iconos AWS reales)
        microservices = self.config.get("microservices", {})
        x_offset = 100
        for i, (service_name, service_config) in enumerate(microservices.items()):
            fargate_cell = ET.SubElement(root, "mxCell",
                id=str(cell_id),
                value=f"{service_name.replace('_', ' ').title()}\\nECS Fargate\\n{service_config.get('business_function', '')[:30]}...",
                style=self.aws_shapes["fargate"],
                vertex="1", parent=str(vpc_id)
            )
            ET.SubElement(fargate_cell, "mxGeometry", x=str(x_offset), y="200", width="78", height="78", **{"as": "geometry"})
            cell_id += 1
            x_offset += 150
        
        # RDS Primary (icono AWS real)
        rds_primary_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="RDS PostgreSQL\\nPrimary\\nus-east-1a\\nMulti-AZ",
            style=self.aws_shapes["rds"],
            vertex="1", parent=str(vpc_id)
        )
        ET.SubElement(rds_primary_cell, "mxGeometry", x="100", y="350", width="78", height="78", **{"as": "geometry"})
        cell_id += 1
        
        # RDS Standby (icono AWS real)
        rds_standby_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="RDS PostgreSQL\\nStandby\\nus-east-1b\\nRead Replica",
            style=self.aws_shapes["rds"],
            vertex="1", parent=str(vpc_id)
        )
        ET.SubElement(rds_standby_cell, "mxGeometry", x="300", y="350", width="78", height="78", **{"as": "geometry"})
        cell_id += 1
        
        # ElastiCache Redis (icono AWS real)
        redis_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="ElastiCache\\nRedis Cluster\\nSession Store",
            style=self.aws_shapes["elasticache"],
            vertex="1", parent=str(vpc_id)
        )
        ET.SubElement(redis_cell, "mxGeometry", x="500", y="350", width="78", height="78", **{"as": "geometry"})
        cell_id += 1
        
        # S3 Storage (icono AWS real)
        s3_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="S3 Storage\\nDocuments & Assets\\n60M Products Data",
            style=self.aws_shapes["s3"],
            vertex="1", parent=str(vpc_id)
        )
        ET.SubElement(s3_cell, "mxGeometry", x="700", y="350", width="78", height="78", **{"as": "geometry"})
        cell_id += 1
        
        # Generar XML
        ET.indent(mxfile, space="  ")
        xml_str = ET.tostring(mxfile, encoding='unicode', xml_declaration=True)
        
        # Guardar archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{project_name}_aws_icons_{timestamp}.drawio"
        output_path = self.output_dir / "drawio" / filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_str)
        
        return str(output_path)
