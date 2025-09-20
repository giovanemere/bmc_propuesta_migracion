#!/usr/bin/env python3
"""
Perfect DrawIO Generator - UN SOLO DrawIO idéntico al PNG
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

class PerfectDrawIOGenerator:
    """Genera UN SOLO DrawIO idéntico al PNG network diagram"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str):
        self.config = config
        self.output_dir = Path(output_dir)
    
    def generate_network_drawio(self, project_name: str = "bmc_input") -> str:
        """Genera DrawIO idéntico al PNG network architecture"""
        
        # Crear XML DrawIO
        mxfile = ET.Element("mxfile", host="app.diagrams.net")
        diagram = ET.SubElement(mxfile, "diagram", name=f"{project_name} Network Architecture", id="network")
        model = ET.SubElement(diagram, "mxGraphModel", dx="3000", dy="2000", grid="1", gridSize="10")
        root = ET.SubElement(model, "root")
        
        # Celdas base
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        
        cell_id = 2
        
        # Título (igual al PNG)
        title = ET.SubElement(root, "mxCell",
            id=str(cell_id), value=f"{project_name.upper()} - Network Architecture & VPC",
            style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;fontColor=#FFFFFF;fontSize=18;fontStyle=1;",
            vertex="1", parent="1"
        )
        ET.SubElement(title, "mxGeometry", x="50", y="20", width="2500", height="50", **{"as": "geometry"})
        cell_id += 1
        
        # Internet (fuera del cloud, igual al PNG)
        internet = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="Internet",
            style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.internet_gateway;",
            vertex="1", parent="1"
        )
        ET.SubElement(internet, "mxGeometry", x="100", y="100", width="78", height="78", **{"as": "geometry"})
        internet_id = cell_id
        cell_id += 1
        
        # Users (fuera del cloud, igual al PNG)
        users = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="BMC Users\\n10K concurrent",
            style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.users;",
            vertex="1", parent="1"
        )
        ET.SubElement(users, "mxGeometry", x="300", y="100", width="78", height="78", **{"as": "geometry"})
        users_id = cell_id
        cell_id += 1
        
        # AWS Cloud (contenedor principal, igual al PNG)
        aws_cloud = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="AWS Cloud - us-east-1",
            style="fillColor=#E3F2FD;strokeColor=#1976D2;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#1976D2;whiteSpace=wrap;html=1;fontSize=14;",
            vertex="1", parent="1"
        )
        ET.SubElement(aws_cloud, "mxGeometry", x="50", y="220", width="2400", height="1600", **{"as": "geometry"})
        aws_cloud_id = cell_id
        cell_id += 1
        
        # VPC (dentro de AWS Cloud, igual al PNG)
        vpc = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="VPC 10.0.0.0/16",
            style="fillColor=#F5F5F5;strokeColor=#666666;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#666666;whiteSpace=wrap;html=1;fontSize=12;",
            vertex="1", parent=str(aws_cloud_id)
        )
        ET.SubElement(vpc, "mxGeometry", x="50", y="250", width="2200", height="1200", **{"as": "geometry"})
        vpc_id = cell_id
        cell_id += 1
        
        # AZ us-east-1a (dentro de VPC, igual al PNG)
        az_a = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="AZ us-east-1a",
            style="fillColor=#E8F5E8;strokeColor=#4CAF50;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#4CAF50;whiteSpace=wrap;html=1;fontSize=11;",
            vertex="1", parent=str(vpc_id)
        )
        ET.SubElement(az_a, "mxGeometry", x="50", y="50", width="1000", height="1000", **{"as": "geometry"})
        az_a_id = cell_id
        cell_id += 1
        
        # Public Subnet (dentro de AZ A, igual al PNG)
        public_subnet = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="Public Subnet\\n10.0.1.0/24",
            style="fillColor=#E8F5E8;strokeColor=#4CAF50;dashed=2;verticalAlign=top;fontStyle=0;fontColor=#4CAF50;whiteSpace=wrap;html=1;fontSize=10;",
            vertex="1", parent=str(az_a_id)
        )
        ET.SubElement(public_subnet, "mxGeometry", x="50", y="50", width="400", height="200", **{"as": "geometry"})
        public_subnet_id = cell_id
        cell_id += 1
        
        # NAT Gateway (dentro de Public Subnet, igual al PNG)
        nat_gateway = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="NAT Gateway 1A",
            style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#8C4FFF;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elastic_load_balancing;",
            vertex="1", parent=str(public_subnet_id)
        )
        ET.SubElement(nat_gateway, "mxGeometry", x="50", y="80", width="78", height="78", **{"as": "geometry"})
        nat_gateway_id = cell_id
        cell_id += 1
        
        # Private Subnet (dentro de AZ A, igual al PNG)
        private_subnet = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="Private Subnet\\n10.0.10.0/24",
            style="fillColor=#FFF3E0;strokeColor=#FF9800;dashed=2;verticalAlign=top;fontStyle=0;fontColor=#FF9800;whiteSpace=wrap;html=1;fontSize=10;",
            vertex="1", parent=str(az_a_id)
        )
        ET.SubElement(private_subnet, "mxGeometry", x="50", y="300", width="400", height="300", **{"as": "geometry"})
        private_subnet_id = cell_id
        cell_id += 1
        
        # App Services (dentro de Private Subnet, igual al PNG)
        app_services = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="App Services 1A",
            style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;",
            vertex="1", parent=str(private_subnet_id)
        )
        ET.SubElement(app_services, "mxGeometry", x="50", y="100", width="78", height="78", **{"as": "geometry"})
        app_services_id = cell_id
        cell_id += 1
        
        # Isolated Subnet (dentro de AZ A, igual al PNG)
        isolated_subnet = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="Isolated Subnet\\n10.0.20.0/24",
            style="fillColor=#FFEBEE;strokeColor=#F44336;dashed=2;verticalAlign=top;fontStyle=0;fontColor=#F44336;whiteSpace=wrap;html=1;fontSize=10;",
            vertex="1", parent=str(az_a_id)
        )
        ET.SubElement(isolated_subnet, "mxGeometry", x="50", y="650", width="400", height="200", **{"as": "geometry"})
        isolated_subnet_id = cell_id
        cell_id += 1
        
        # RDS Primary (dentro de Isolated Subnet, igual al PNG)
        rds_primary = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="RDS Primary\\nus-east-1a",
            style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.rds;",
            vertex="1", parent=str(isolated_subnet_id)
        )
        ET.SubElement(rds_primary, "mxGeometry", x="50", y="80", width="78", height="78", **{"as": "geometry"})
        rds_primary_id = cell_id
        cell_id += 1
        
        # AZ us-east-1b (dentro de VPC, igual al PNG)
        az_b = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="AZ us-east-1b",
            style="fillColor=#FFF3E0;strokeColor=#FF9800;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#FF9800;whiteSpace=wrap;html=1;fontSize=11;",
            vertex="1", parent=str(vpc_id)
        )
        ET.SubElement(az_b, "mxGeometry", x="1100", y="50", width="1000", height="1000", **{"as": "geometry"})
        az_b_id = cell_id
        cell_id += 1
        
        # RDS Standby (dentro de AZ B, igual al PNG)
        rds_standby = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="RDS Standby\\nus-east-1b",
            style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.rds;",
            vertex="1", parent=str(az_b_id)
        )
        ET.SubElement(rds_standby, "mxGeometry", x="100", y="750", width="78", height="78", **{"as": "geometry"})
        rds_standby_id = cell_id
        cell_id += 1
        
        # Edge Layer (dentro de AWS Cloud, igual al PNG)
        edge_layer = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="Edge Layer",
            style="fillColor=#FFEBEE;strokeColor=#F44336;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#F44336;whiteSpace=wrap;html=1;fontSize=11;",
            vertex="1", parent=str(aws_cloud_id)
        )
        ET.SubElement(edge_layer, "mxGeometry", x="50", y="50", width="600", height="150", **{"as": "geometry"})
        edge_layer_id = cell_id
        cell_id += 1
        
        # CloudFront (dentro de Edge Layer, igual al PNG)
        cloudfront = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="CloudFront CDN\\nGlobal Edge",
            style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudfront;",
            vertex="1", parent=str(edge_layer_id)
        )
        ET.SubElement(cloudfront, "mxGeometry", x="50", y="60", width="78", height="78", **{"as": "geometry"})
        cloudfront_id = cell_id
        cell_id += 1
        
        # WAF (dentro de Edge Layer, igual al PNG)
        waf = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="AWS WAF\\nDDoS Protection",
            style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.waf;",
            vertex="1", parent=str(edge_layer_id)
        )
        ET.SubElement(waf, "mxGeometry", x="200", y="60", width="78", height="78", **{"as": "geometry"})
        waf_id = cell_id
        cell_id += 1
        
        # API Layer (dentro de AWS Cloud, igual al PNG)
        api_layer = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="API Layer",
            style="fillColor=#F3E5F5;strokeColor=#9C27B0;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#9C27B0;whiteSpace=wrap;html=1;fontSize=11;",
            vertex="1", parent=str(aws_cloud_id)
        )
        ET.SubElement(api_layer, "mxGeometry", x="700", y="50", width="600", height="150", **{"as": "geometry"})
        api_layer_id = cell_id
        cell_id += 1
        
        # API Gateway (dentro de API Layer, igual al PNG)
        api_gateway = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="API Gateway\\nREST + GraphQL",
            style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.api_gateway;",
            vertex="1", parent=str(api_layer_id)
        )
        ET.SubElement(api_gateway, "mxGeometry", x="50", y="60", width="78", height="78", **{"as": "geometry"})
        api_gateway_id = cell_id
        cell_id += 1
        
        # Cognito (dentro de API Layer, igual al PNG)
        cognito = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="Cognito\\nUser Pool",
            style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cognito;",
            vertex="1", parent=str(api_layer_id)
        )
        ET.SubElement(cognito, "mxGeometry", x="200", y="60", width="78", height="78", **{"as": "geometry"})
        cognito_id = cell_id
        cell_id += 1
        
        # ALB (dentro de API Layer, igual al PNG)
        alb = ET.SubElement(root, "mxCell",
            id=str(cell_id), value="Application LB\\nMulti-AZ",
            style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#8C4FFF;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elastic_load_balancing;",
            vertex="1", parent=str(api_layer_id)
        )
        ET.SubElement(alb, "mxGeometry", x="350", y="60", width="78", height="78", **{"as": "geometry"})
        alb_id = cell_id
        cell_id += 1
        
        # Conexiones (igual al PNG)
        connections = [
            (users_id, internet_id, "#232F3E"),
            (internet_id, cloudfront_id, "#232F3E"),
            (cloudfront_id, waf_id, "#F44336"),
            (waf_id, api_gateway_id, "#232F3E"),
            (api_gateway_id, cognito_id, "#FF9900"),
            (api_gateway_id, alb_id, "#232F3E"),
            (alb_id, app_services_id, "#2196F3"),
            (app_services_id, rds_primary_id, "#2196F3"),
            (rds_primary_id, rds_standby_id, "#FF9800")
        ]
        
        for source, target, color in connections:
            edge = ET.SubElement(root, "mxCell",
                id=str(cell_id), value="",
                style=f"endArrow=classic;html=1;rounded=0;strokeColor={color};strokeWidth=2;",
                edge="1", parent="1", source=str(source), target=str(target)
            )
            ET.SubElement(edge, "mxGeometry", width="50", height="50", relative="1", **{"as": "geometry"})
            cell_id += 1
        
        # Generar XML
        ET.indent(mxfile, space="  ")
        xml_str = ET.tostring(mxfile, encoding='unicode', xml_declaration=True)
        
        # Guardar archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{project_name}_network_architecture_{timestamp}.drawio"
        output_path = self.output_dir / "drawio" / filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_str)
        
        return str(output_path)
