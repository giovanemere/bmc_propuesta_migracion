#!/usr/bin/env python3
"""
Professional DrawIO Generator - Genera diagramas DrawIO profesionales
Equivalente a la calidad de los PNG con arquitectura AWS completa
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

class ProfessionalDrawIOGenerator:
    """Generador DrawIO profesional con arquitectura AWS completa"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str):
        self.config = config
        self.output_dir = Path(output_dir)
        
        # Estilos AWS profesionales
        self.aws_styles = {
            "vpc": "rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;fontSize=14;fontStyle=1;verticalAlign=top;",
            "subnet_public": "rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#4CAF50;fontSize=12;verticalAlign=top;",
            "subnet_private": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#FF9800;fontSize=12;verticalAlign=top;",
            "subnet_isolated": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFEBEE;strokeColor=#F44336;fontSize=12;verticalAlign=top;",
            "fargate": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FF9900;fontColor=#FFFFFF;fontSize=10;",
            "rds": "rounded=1;whiteSpace=wrap;html=1;fillColor=#3F48CC;fontColor=#FFFFFF;fontSize=10;",
            "elasticache": "rounded=1;whiteSpace=wrap;html=1;fillColor=#C925D1;fontColor=#FFFFFF;fontSize=10;",
            "s3": "rounded=1;whiteSpace=wrap;html=1;fillColor=#569A31;fontColor=#FFFFFF;fontSize=10;",
            "api_gateway": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FF4B4B;fontColor=#FFFFFF;fontSize=10;",
            "cloudfront": "rounded=1;whiteSpace=wrap;html=1;fillColor=#8C4FFF;fontColor=#FFFFFF;fontSize=10;",
            "cognito": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DD344C;fontColor=#FFFFFF;fontSize=10;",
            "elb": "rounded=1;whiteSpace=wrap;html=1;fillColor=#8C4FFF;fontColor=#FFFFFF;fontSize=10;",
            "internet": "ellipse;whiteSpace=wrap;html=1;fillColor=#232F3E;fontColor=#FFFFFF;fontSize=12;",
            "users": "shape=actor;whiteSpace=wrap;html=1;fillColor=#4CAF50;fontColor=#FFFFFF;fontSize=10;"
        }
        
    def generate_professional_architecture(self, project_name: str = "bmc_input") -> str:
        """Genera diagrama de arquitectura profesional"""
        
        # Crear XML DrawIO
        mxfile = ET.Element("mxfile", host="app.diagrams.net")
        diagram = ET.SubElement(mxfile, "diagram", name=f"{project_name} Professional Architecture", id="professional")
        model = ET.SubElement(diagram, "mxGraphModel", dx="2000", dy="1200", grid="1", gridSize="10")
        root = ET.SubElement(model, "root")
        
        # Celdas base
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        
        cell_id = 2
        
        # Título
        title_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value=f"{project_name.upper()} - Professional AWS Architecture",
            style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;fontColor=#FFFFFF;fontSize=18;fontStyle=1;",
            vertex="1", parent="1"
        )
        ET.SubElement(title_cell, "mxGeometry", x="50", y="20", width="1800", height="50", **{"as": "geometry"})
        cell_id += 1
        
        # Internet y usuarios
        internet_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Internet\\nGlobal Access",
            style=self.aws_styles["internet"],
            vertex="1", parent="1"
        )
        ET.SubElement(internet_cell, "mxGeometry", x="100", y="100", width="120", height="80", **{"as": "geometry"})
        cell_id += 1
        
        users_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="BMC Users\\n10K concurrent",
            style=self.aws_styles["users"],
            vertex="1", parent="1"
        )
        ET.SubElement(users_cell, "mxGeometry", x="300", y="100", width="100", height="80", **{"as": "geometry"})
        cell_id += 1
        
        # AWS Cloud
        aws_cloud_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="AWS Cloud - us-east-1",
            style=self.aws_styles["vpc"],
            vertex="1", parent="1"
        )
        ET.SubElement(aws_cloud_cell, "mxGeometry", x="50", y="220", width="1750", height="900", **{"as": "geometry"})
        aws_cloud_id = cell_id
        cell_id += 1
        
        # Edge Services
        edge_group = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Edge Layer",
            style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFEBEE;strokeColor=#F44336;fontSize=12;fontStyle=1;verticalAlign=top;",
            vertex="1", parent=str(aws_cloud_id)
        )
        ET.SubElement(edge_group, "mxGeometry", x="100", y="50", width="400", height="120", **{"as": "geometry"})
        edge_group_id = cell_id
        cell_id += 1
        
        # CloudFront
        cloudfront_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="CloudFront CDN\\nGlobal Edge\\nCaching & SSL",
            style=self.aws_styles["cloudfront"],
            vertex="1", parent=str(edge_group_id)
        )
        ET.SubElement(cloudfront_cell, "mxGeometry", x="20", y="40", width="120", height="60", **{"as": "geometry"})
        cell_id += 1
        
        # WAF
        waf_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="AWS WAF\\nDDoS Protection\\nSecurity Rules",
            style=self.aws_styles["api_gateway"],
            vertex="1", parent=str(edge_group_id)
        )
        ET.SubElement(waf_cell, "mxGeometry", x="200", y="40", width="120", height="60", **{"as": "geometry"})
        cell_id += 1
        
        # VPC Principal
        vpc_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="VPC 10.0.0.0/16\\nBMC Production Environment",
            style=self.aws_styles["vpc"],
            vertex="1", parent=str(aws_cloud_id)
        )
        ET.SubElement(vpc_cell, "mxGeometry", x="100", y="200", width="1500", height="650", **{"as": "geometry"})
        vpc_id = cell_id
        cell_id += 1
        
        # Availability Zone A
        az_a_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Availability Zone us-east-1a",
            style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#4CAF50;fontSize=12;fontStyle=1;verticalAlign=top;",
            vertex="1", parent=str(vpc_id)
        )
        ET.SubElement(az_a_cell, "mxGeometry", x="50", y="50", width="650", height="550", **{"as": "geometry"})
        az_a_id = cell_id
        cell_id += 1
        
        # Public Subnet A
        public_a_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Public Subnet 10.0.1.0/24\\nInternet Gateway Access",
            style=self.aws_styles["subnet_public"],
            vertex="1", parent=str(az_a_id)
        )
        ET.SubElement(public_a_cell, "mxGeometry", x="20", y="40", width="280", height="120", **{"as": "geometry"})
        public_a_id = cell_id
        cell_id += 1
        
        # NAT Gateway A
        nat_a_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="NAT Gateway 1A\\nOutbound Internet\\nElastic IP",
            style=self.aws_styles["elb"],
            vertex="1", parent=str(public_a_id)
        )
        ET.SubElement(nat_a_cell, "mxGeometry", x="20", y="50", width="120", height="50", **{"as": "geometry"})
        cell_id += 1
        
        # ALB A
        alb_a_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Application LB\\nMulti-AZ\\nSSL Termination",
            style=self.aws_styles["elb"],
            vertex="1", parent=str(public_a_id)
        )
        ET.SubElement(alb_a_cell, "mxGeometry", x="150", y="50", width="120", height="50", **{"as": "geometry"})
        cell_id += 1
        
        # Private Subnet A
        private_a_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Private Subnet 10.0.10.0/24\\nApplication Layer",
            style=self.aws_styles["subnet_private"],
            vertex="1", parent=str(az_a_id)
        )
        ET.SubElement(private_a_cell, "mxGeometry", x="20", y="180", width="280", height="180", **{"as": "geometry"})
        private_a_id = cell_id
        cell_id += 1
        
        # Microservicios en Private A
        microservices = self.config.get("microservices", {})
        y_offset = 30
        for i, (service_name, service_config) in enumerate(microservices.items()):
            if i >= 3:  # Máximo 3 servicios por AZ
                break
                
            service_cell = ET.SubElement(root, "mxCell",
                id=str(cell_id),
                value=f"{service_name.replace('_', ' ').title()}\\nECS Fargate\\n{service_config.get('business_function', '')[:20]}...",
                style=self.aws_styles["fargate"],
                vertex="1", parent=str(private_a_id)
            )
            ET.SubElement(service_cell, "mxGeometry", x="20", y=str(y_offset), width="120", height="60", **{"as": "geometry"})
            cell_id += 1
            y_offset += 80
        
        # API Gateway
        api_gw_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="API Gateway\\nREST + GraphQL\\nRate Limiting",
            style=self.aws_styles["api_gateway"],
            vertex="1", parent=str(private_a_id)
        )
        ET.SubElement(api_gw_cell, "mxGeometry", x="150", y="30", width="120", height="60", **{"as": "geometry"})
        cell_id += 1
        
        # Cognito
        cognito_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Cognito\\nUser Pool\\nAuthentication",
            style=self.aws_styles["cognito"],
            vertex="1", parent=str(private_a_id)
        )
        ET.SubElement(cognito_cell, "mxGeometry", x="150", y="100", width="120", height="60", **{"as": "geometry"})
        cell_id += 1
        
        # Isolated Subnet A
        isolated_a_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Isolated Subnet 10.0.20.0/24\\nDatabase Layer",
            style=self.aws_styles["subnet_isolated"],
            vertex="1", parent=str(az_a_id)
        )
        ET.SubElement(isolated_a_cell, "mxGeometry", x="20", y="380", width="280", height="150", **{"as": "geometry"})
        isolated_a_id = cell_id
        cell_id += 1
        
        # RDS Primary
        rds_primary_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="RDS PostgreSQL\\nPrimary Instance\\nus-east-1a\\nMulti-AZ",
            style=self.aws_styles["rds"],
            vertex="1", parent=str(isolated_a_id)
        )
        ET.SubElement(rds_primary_cell, "mxGeometry", x="20", y="40", width="120", height="80", **{"as": "geometry"})
        cell_id += 1
        
        # ElastiCache
        redis_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="ElastiCache\\nRedis Cluster\\nSession Store",
            style=self.aws_styles["elasticache"],
            vertex="1", parent=str(isolated_a_id)
        )
        ET.SubElement(redis_cell, "mxGeometry", x="150", y="40", width="120", height="80", **{"as": "geometry"})
        cell_id += 1
        
        # Availability Zone B (similar structure)
        az_b_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Availability Zone us-east-1b",
            style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#FF9800;fontSize=12;fontStyle=1;verticalAlign=top;",
            vertex="1", parent=str(vpc_id)
        )
        ET.SubElement(az_b_cell, "mxGeometry", x="750", y="50", width="650", height="550", **{"as": "geometry"})
        az_b_id = cell_id
        cell_id += 1
        
        # RDS Standby en AZ B
        rds_standby_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="RDS PostgreSQL\\nStandby Instance\\nus-east-1b\\nRead Replica",
            style=self.aws_styles["rds"],
            vertex="1", parent=str(az_b_id)
        )
        ET.SubElement(rds_standby_cell, "mxGeometry", x="50", y="450", width="120", height="80", **{"as": "geometry"})
        cell_id += 1
        
        # S3 Storage
        s3_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="S3 Storage\\nDocuments & Assets\\nVersioning Enabled\\n60M Products Data",
            style=self.aws_styles["s3"],
            vertex="1", parent=str(vpc_id)
        )
        ET.SubElement(s3_cell, "mxGeometry", x="1200", y="300", width="150", height="100", **{"as": "geometry"})
        cell_id += 1
        
        # Generar XML
        ET.indent(mxfile, space="  ")
        xml_str = ET.tostring(mxfile, encoding='unicode', xml_declaration=True)
        
        # Guardar archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{project_name}_professional_aws_{timestamp}.drawio"
        output_path = self.output_dir / "drawio" / filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_str)
        
        return str(output_path)
