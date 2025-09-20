#!/usr/bin/env python3
"""
PNG Equivalent DrawIO Generator - Replica exactamente la estructura del PNG
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

class PNGEquivalentDrawIOGenerator:
    """Genera DrawIO que replica exactamente la estructura del PNG"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str):
        self.config = config
        self.output_dir = Path(output_dir)
        
        # Iconos AWS exactos
        self.aws_icons = {
            "internet": "sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.internet_gateway;",
            "users": "sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.users;",
            "cloudfront": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudfront;",
            "waf": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.waf;",
            "api_gateway": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.api_gateway;",
            "cognito": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cognito;",
            "elb": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#8C4FFF;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elastic_load_balancing;",
            "fargate": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;",
            "rds": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.rds;"
        }
        
        # Estilos de contenedores (clusters)
        self.cluster_styles = {
            "aws_cloud": "fillColor=#E3F2FD;strokeColor=#1976D2;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#1976D2;whiteSpace=wrap;html=1;fontSize=14;",
            "vpc": "fillColor=#F5F5F5;strokeColor=#666666;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#666666;whiteSpace=wrap;html=1;fontSize=12;",
            "az_a": "fillColor=#E8F5E8;strokeColor=#4CAF50;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#4CAF50;whiteSpace=wrap;html=1;fontSize=11;",
            "az_b": "fillColor=#FFF3E0;strokeColor=#FF9800;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#FF9800;whiteSpace=wrap;html=1;fontSize=11;",
            "subnet_public": "fillColor=#E8F5E8;strokeColor=#4CAF50;dashed=2;verticalAlign=top;fontStyle=0;fontColor=#4CAF50;whiteSpace=wrap;html=1;fontSize=10;",
            "subnet_private": "fillColor=#FFF3E0;strokeColor=#FF9800;dashed=2;verticalAlign=top;fontStyle=0;fontColor=#FF9800;whiteSpace=wrap;html=1;fontSize=10;",
            "subnet_isolated": "fillColor=#FFEBEE;strokeColor=#F44336;dashed=2;verticalAlign=top;fontStyle=0;fontColor=#F44336;whiteSpace=wrap;html=1;fontSize=10;",
            "edge_layer": "fillColor=#FFEBEE;strokeColor=#F44336;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#F44336;whiteSpace=wrap;html=1;fontSize=11;",
            "api_layer": "fillColor=#F3E5F5;strokeColor=#9C27B0;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#9C27B0;whiteSpace=wrap;html=1;fontSize=11;"
        }
        
    def generate_png_equivalent_drawio(self, project_name: str = "bmc_input") -> str:
        """Genera DrawIO que replica exactamente la estructura del PNG"""
        
        # Crear XML DrawIO
        mxfile = ET.Element("mxfile", host="app.diagrams.net")
        diagram = ET.SubElement(mxfile, "diagram", name=f"{project_name} Network Architecture", id="network")
        model = ET.SubElement(diagram, "mxGraphModel", dx="3000", dy="2000", grid="1", gridSize="10")
        root = ET.SubElement(model, "root")
        
        # Celdas base
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        
        cell_id = 2
        
        # Título
        title_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value=f"{project_name.upper()} - Network Architecture & VPC",
            style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;fontColor=#FFFFFF;fontSize=18;fontStyle=1;",
            vertex="1", parent="1"
        )
        ET.SubElement(title_cell, "mxGeometry", x="50", y="20", width="2500", height="50", **{"as": "geometry"})
        cell_id += 1
        
        # Internet (fuera del cloud)
        internet_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Internet",
            style=self.aws_icons["internet"],
            vertex="1", parent="1"
        )
        ET.SubElement(internet_cell, "mxGeometry", x="100", y="100", width="78", height="78", **{"as": "geometry"})
        internet_id = cell_id
        cell_id += 1
        
        # Users (fuera del cloud)
        users_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="BMC Users\\n10K concurrent",
            style=self.aws_icons["users"],
            vertex="1", parent="1"
        )
        ET.SubElement(users_cell, "mxGeometry", x="300", y="100", width="78", height="78", **{"as": "geometry"})
        users_id = cell_id
        cell_id += 1
        
        # AWS Cloud (contenedor principal)
        aws_cloud_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="AWS Cloud - us-east-1",
            style=self.cluster_styles["aws_cloud"],
            vertex="1", parent="1"
        )
        ET.SubElement(aws_cloud_cell, "mxGeometry", x="50", y="220", width="2400", height="1600", **{"as": "geometry"})
        aws_cloud_id = cell_id
        cell_id += 1
        
        # Edge Layer (dentro de AWS Cloud)
        edge_layer_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Edge Layer",
            style=self.cluster_styles["edge_layer"],
            vertex="1", parent=str(aws_cloud_id)
        )
        ET.SubElement(edge_layer_cell, "mxGeometry", x="50", y="50", width="600", height="150", **{"as": "geometry"})
        edge_layer_id = cell_id
        cell_id += 1
        
        # CloudFront (dentro de Edge Layer)
        cloudfront_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="CloudFront CDN\\nGlobal Edge",
            style=self.aws_icons["cloudfront"],
            vertex="1", parent=str(edge_layer_id)
        )
        ET.SubElement(cloudfront_cell, "mxGeometry", x="50", y="60", width="78", height="78", **{"as": "geometry"})
        cloudfront_id = cell_id
        cell_id += 1
        
        # WAF (dentro de Edge Layer)
        waf_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="AWS WAF\\nDDoS Protection",
            style=self.aws_icons["waf"],
            vertex="1", parent=str(edge_layer_id)
        )
        ET.SubElement(waf_cell, "mxGeometry", x="200", y="60", width="78", height="78", **{"as": "geometry"})
        waf_id = cell_id
        cell_id += 1
        
        # API Layer (dentro de AWS Cloud)
        api_layer_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="API Layer",
            style=self.cluster_styles["api_layer"],
            vertex="1", parent=str(aws_cloud_id)
        )
        ET.SubElement(api_layer_cell, "mxGeometry", x="700", y="50", width="600", height="150", **{"as": "geometry"})
        api_layer_id = cell_id
        cell_id += 1
        
        # API Gateway (dentro de API Layer)
        api_gw_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="API Gateway\\nREST + GraphQL",
            style=self.aws_icons["api_gateway"],
            vertex="1", parent=str(api_layer_id)
        )
        ET.SubElement(api_gw_cell, "mxGeometry", x="50", y="60", width="78", height="78", **{"as": "geometry"})
        api_gw_id = cell_id
        cell_id += 1
        
        # Cognito (dentro de API Layer)
        cognito_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Cognito\\nUser Pool",
            style=self.aws_icons["cognito"],
            vertex="1", parent=str(api_layer_id)
        )
        ET.SubElement(cognito_cell, "mxGeometry", x="200", y="60", width="78", height="78", **{"as": "geometry"})
        cognito_id = cell_id
        cell_id += 1
        
        # ALB (dentro de API Layer)
        alb_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Application LB\\nMulti-AZ",
            style=self.aws_icons["elb"],
            vertex="1", parent=str(api_layer_id)
        )
        ET.SubElement(alb_cell, "mxGeometry", x="350", y="60", width="78", height="78", **{"as": "geometry"})
        alb_id = cell_id
        cell_id += 1
        
        # VPC Principal (dentro de AWS Cloud)
        vpc_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="VPC 10.0.0.0/16",
            style=self.cluster_styles["vpc"],
            vertex="1", parent=str(aws_cloud_id)
        )
        ET.SubElement(vpc_cell, "mxGeometry", x="50", y="250", width="2200", height="1200", **{"as": "geometry"})
        vpc_id = cell_id
        cell_id += 1
        
        # Availability Zone A (dentro de VPC)
        az_a_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="AZ us-east-1a",
            style=self.cluster_styles["az_a"],
            vertex="1", parent=str(vpc_id)
        )
        ET.SubElement(az_a_cell, "mxGeometry", x="50", y="50", width="1000", height="1000", **{"as": "geometry"})
        az_a_id = cell_id
        cell_id += 1
        
        # Public Subnet A (dentro de AZ A)
        public_a_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Public Subnet\\n10.0.1.0/24",
            style=self.cluster_styles["subnet_public"],
            vertex="1", parent=str(az_a_id)
        )
        ET.SubElement(public_a_cell, "mxGeometry", x="50", y="50", width="400", height="200", **{"as": "geometry"})
        public_a_id = cell_id
        cell_id += 1
        
        # NAT Gateway A (dentro de Public Subnet A)
        nat_a_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="NAT Gateway 1A",
            style=self.aws_icons["elb"],
            vertex="1", parent=str(public_a_id)
        )
        ET.SubElement(nat_a_cell, "mxGeometry", x="50", y="80", width="78", height="78", **{"as": "geometry"})
        cell_id += 1
        
        # Private Subnet A (dentro de AZ A)
        private_a_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Private Subnet\\n10.0.10.0/24",
            style=self.cluster_styles["subnet_private"],
            vertex="1", parent=str(az_a_id)
        )
        ET.SubElement(private_a_cell, "mxGeometry", x="50", y="300", width="400", height="300", **{"as": "geometry"})
        private_a_id = cell_id
        cell_id += 1
        
        # App Services A (dentro de Private Subnet A)
        app_a_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="App Services 1A",
            style=self.aws_icons["fargate"],
            vertex="1", parent=str(private_a_id)
        )
        ET.SubElement(app_a_cell, "mxGeometry", x="50", y="100", width="78", height="78", **{"as": "geometry"})
        app_a_id = cell_id
        cell_id += 1
        
        # Isolated Subnet A (dentro de AZ A)
        isolated_a_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="Isolated Subnet\\n10.0.20.0/24",
            style=self.cluster_styles["subnet_isolated"],
            vertex="1", parent=str(az_a_id)
        )
        ET.SubElement(isolated_a_cell, "mxGeometry", x="50", y="650", width="400", height="200", **{"as": "geometry"})
        isolated_a_id = cell_id
        cell_id += 1
        
        # RDS Primary (dentro de Isolated Subnet A)
        rds_primary_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="RDS Primary\\nus-east-1a",
            style=self.aws_icons["rds"],
            vertex="1", parent=str(isolated_a_id)
        )
        ET.SubElement(rds_primary_cell, "mxGeometry", x="50", y="80", width="78", height="78", **{"as": "geometry"})
        rds_primary_id = cell_id
        cell_id += 1
        
        # Availability Zone B (dentro de VPC)
        az_b_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="AZ us-east-1b",
            style=self.cluster_styles["az_b"],
            vertex="1", parent=str(vpc_id)
        )
        ET.SubElement(az_b_cell, "mxGeometry", x="1100", y="50", width="1000", height="1000", **{"as": "geometry"})
        az_b_id = cell_id
        cell_id += 1
        
        # RDS Standby en AZ B (simplificado)
        rds_standby_cell = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="RDS Standby\\nus-east-1b",
            style=self.aws_icons["rds"],
            vertex="1", parent=str(az_b_id)
        )
        ET.SubElement(rds_standby_cell, "mxGeometry", x="100", y="750", width="78", height="78", **{"as": "geometry"})
        rds_standby_id = cell_id
        cell_id += 1
        
        # Conexiones (edges)
        # Internet -> CloudFront
        edge1 = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="",
            style="endArrow=classic;html=1;rounded=0;strokeColor=#232F3E;strokeWidth=2;",
            edge="1", parent="1", source=str(internet_id), target=str(cloudfront_id)
        )
        ET.SubElement(edge1, "mxGeometry", width="50", height="50", relative="1", **{"as": "geometry"})
        cell_id += 1
        
        # CloudFront -> WAF
        edge2 = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="",
            style="endArrow=classic;html=1;rounded=0;strokeColor=#F44336;strokeWidth=2;",
            edge="1", parent="1", source=str(cloudfront_id), target=str(waf_id)
        )
        ET.SubElement(edge2, "mxGeometry", width="50", height="50", relative="1", **{"as": "geometry"})
        cell_id += 1
        
        # ALB -> App Services
        edge3 = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="",
            style="endArrow=classic;html=1;rounded=0;strokeColor=#2196F3;strokeWidth=2;",
            edge="1", parent="1", source=str(alb_id), target=str(app_a_id)
        )
        ET.SubElement(edge3, "mxGeometry", width="50", height="50", relative="1", **{"as": "geometry"})
        cell_id += 1
        
        # App Services -> RDS
        edge4 = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="",
            style="endArrow=classic;html=1;rounded=0;strokeColor=#2196F3;strokeWidth=2;",
            edge="1", parent="1", source=str(app_a_id), target=str(rds_primary_id)
        )
        ET.SubElement(edge4, "mxGeometry", width="50", height="50", relative="1", **{"as": "geometry"})
        cell_id += 1
        
        # RDS Primary -> RDS Standby
        edge5 = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value="",
            style="endArrow=classic;html=1;rounded=0;strokeColor=#FF9800;strokeWidth=2;",
            edge="1", parent="1", source=str(rds_primary_id), target=str(rds_standby_id)
        )
        ET.SubElement(edge5, "mxGeometry", width="50", height="50", relative="1", **{"as": "geometry"})
        cell_id += 1
        
        # Generar XML
        ET.indent(mxfile, space="  ")
        xml_str = ET.tostring(mxfile, encoding='unicode', xml_declaration=True)
        
        # Guardar archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{project_name}_png_equivalent_{timestamp}.drawio"
        output_path = self.output_dir / "drawio" / filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_str)
        
        return str(output_path)
