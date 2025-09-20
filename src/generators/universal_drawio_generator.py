#!/usr/bin/env python3
"""
Universal DrawIO Generator - Usa misma entrada que PNG
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List
import json

class UniversalDrawIOGenerator:
    """Generador DrawIO que usa exactamente la misma entrada que PNG"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str):
        self.config = config
        self.output_dir = Path(output_dir)
        
        # Mapeo directo de componentes PNG a DrawIO
        self.png_to_drawio_mapping = {
            # Compute
            "Fargate": "mxgraph.aws4.fargate",
            "Lambda": "mxgraph.aws4.lambda",
            "ECS": "mxgraph.aws4.ecs",
            
            # Database  
            "RDS": "mxgraph.aws4.rds",
            "Elasticache": "mxgraph.aws4.elasticache",
            "Redshift": "mxgraph.aws4.redshift",
            
            # Storage
            "S3": "mxgraph.aws4.s3",
            "EBS": "mxgraph.aws4.ebs",
            
            # Network
            "APIGateway": "mxgraph.aws4.api_gateway",
            "CloudFront": "mxgraph.aws4.cloudfront", 
            "ELB": "mxgraph.aws4.elastic_load_balancing",
            "VPC": "container",
            "PrivateSubnet": "private_subnet",
            "PublicSubnet": "public_subnet",
            
            # Security
            "Cognito": "mxgraph.aws4.cognito",
            "WAF": "mxgraph.aws4.waf",
            "KMS": "mxgraph.aws4.kms",
            
            # Integration
            "SQS": "mxgraph.aws4.sqs",
            "SNS": "mxgraph.aws4.sns",
            
            # Generic
            "Users": "mxgraph.aws4.users",
            "Internet": "mxgraph.aws4.internet_gateway",
            "Client": "mxgraph.aws4.client"
        }
    
    def generate_from_png_input(self, diagram_type: str, project_name: str = "bmc_input") -> str:
        """Genera DrawIO usando exactamente la misma entrada que PNG"""
        
        if diagram_type == "network":
            return self._generate_network_from_png_logic(project_name)
        elif diagram_type == "microservices":
            return self._generate_microservices_from_png_logic(project_name)
        elif diagram_type == "security":
            return self._generate_security_from_png_logic(project_name)
        elif diagram_type == "data_flow":
            return self._generate_dataflow_from_png_logic(project_name)
        else:
            return self._generate_generic_from_png_logic(diagram_type, project_name)
    
    def _generate_network_from_png_logic(self, project_name: str) -> str:
        """Replica exactamente la lógica del PNG network"""
        
        # Usar la misma estructura que diagram_generator.py líneas 60-120
        mxfile = ET.Element("mxfile", host="app.diagrams.net")
        diagram = ET.SubElement(mxfile, "diagram", name="Network Architecture", id="network")
        model = ET.SubElement(diagram, "mxGraphModel", dx="2500", dy="1600", grid="1", gridSize="10")
        root = ET.SubElement(model, "root")
        
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        
        cell_id = 2
        
        # Replicar exactamente la estructura PNG
        # Internet y usuarios (líneas 65-66 del PNG)
        internet_id = self._create_component(root, cell_id, "Internet", "Internet", 
                                           {"x": 100, "y": 100}, "1")
        cell_id += 1
        
        users_id = self._create_component(root, cell_id, "Users", "BMC Users\\n10K concurrent",
                                        {"x": 300, "y": 100}, "1")
        cell_id += 1
        
        # AWS Cloud con VPC (líneas 69-70 del PNG)
        aws_cloud_id = self._create_cluster(root, cell_id, "AWS Cloud - us-east-1",
                                          {"x": 50, "y": 220, "width": 2300, "height": 1300}, "1")
        cell_id += 1
        
        # VPC Principal (líneas 72-73 del PNG)
        vpc_id = self._create_cluster(root, cell_id, "VPC 10.0.0.0/16",
                                    {"x": 50, "y": 200, "width": 2100, "height": 1000}, str(aws_cloud_id))
        cell_id += 1
        
        # Availability Zone A (líneas 75-76 del PNG)
        az_a_id = self._create_cluster(root, cell_id, "AZ us-east-1a",
                                     {"x": 50, "y": 50, "width": 900, "height": 900}, str(vpc_id))
        cell_id += 1
        
        # Public Subnet (líneas 77-79 del PNG)
        public_subnet_id = self._create_cluster(root, cell_id, "Public Subnet\\n10.0.1.0/24",
                                              {"x": 50, "y": 50, "width": 350, "height": 150}, str(az_a_id))
        cell_id += 1
        
        nat_1a_id = self._create_component(root, cell_id, "ELB", "NAT Gateway 1A",
                                         {"x": 50, "y": 60}, str(public_subnet_id))
        cell_id += 1
        
        # Private Subnet (líneas 81-83 del PNG)
        private_subnet_id = self._create_cluster(root, cell_id, "Private Subnet\\n10.0.10.0/24",
                                               {"x": 50, "y": 250, "width": 350, "height": 200}, str(az_a_id))
        cell_id += 1
        
        app_1a_id = self._create_component(root, cell_id, "Fargate", "App Services 1A",
                                         {"x": 50, "y": 80}, str(private_subnet_id))
        cell_id += 1
        
        # Isolated Subnet (líneas 85-87 del PNG)
        isolated_subnet_id = self._create_cluster(root, cell_id, "Isolated Subnet\\n10.0.20.0/24",
                                                {"x": 50, "y": 500, "width": 350, "height": 150}, str(az_a_id))
        cell_id += 1
        
        db_1a_id = self._create_component(root, cell_id, "RDS", "RDS Primary\\nus-east-1a",
                                        {"x": 50, "y": 60}, str(isolated_subnet_id))
        cell_id += 1
        
        # Availability Zone B (líneas 89-95 del PNG)
        az_b_id = self._create_cluster(root, cell_id, "AZ us-east-1b",
                                     {"x": 1000, "y": 50, "width": 900, "height": 900}, str(vpc_id))
        cell_id += 1
        
        db_1b_id = self._create_component(root, cell_id, "RDS", "RDS Standby\\nus-east-1b",
                                        {"x": 100, "y": 600}, str(az_b_id))
        cell_id += 1
        
        # Edge Services (líneas 97-100 del PNG)
        edge_layer_id = self._create_cluster(root, cell_id, "Edge Layer",
                                           {"x": 50, "y": 50, "width": 500, "height": 120}, str(aws_cloud_id))
        cell_id += 1
        
        cloudfront_id = self._create_component(root, cell_id, "CloudFront", "CloudFront CDN\\nGlobal Edge",
                                             {"x": 50, "y": 40}, str(edge_layer_id))
        cell_id += 1
        
        waf_id = self._create_component(root, cell_id, "WAF", "AWS WAF\\nDDoS Protection",
                                      {"x": 180, "y": 40}, str(edge_layer_id))
        cell_id += 1
        
        # API Layer (líneas 102-106 del PNG)
        api_layer_id = self._create_cluster(root, cell_id, "API Layer",
                                          {"x": 600, "y": 50, "width": 500, "height": 120}, str(aws_cloud_id))
        cell_id += 1
        
        api_gateway_id = self._create_component(root, cell_id, "APIGateway", "API Gateway\\nREST + GraphQL",
                                              {"x": 50, "y": 40}, str(api_layer_id))
        cell_id += 1
        
        cognito_id = self._create_component(root, cell_id, "Cognito", "Cognito\\nUser Pool",
                                          {"x": 180, "y": 40}, str(api_layer_id))
        cell_id += 1
        
        alb_id = self._create_component(root, cell_id, "ELB", "Application LB\\nMulti-AZ",
                                      {"x": 310, "y": 40}, str(api_layer_id))
        cell_id += 1
        
        # Conexiones con estilos (líneas 108-118 del PNG)
        self._create_connections(root, [
            (users_id, internet_id, "primary"),
            (internet_id, cloudfront_id, "primary"),
            (cloudfront_id, waf_id, "security"),
            (waf_id, api_gateway_id, "primary"),
            (api_gateway_id, cognito_id, "secondary"),
            (api_gateway_id, alb_id, "primary"),
            (alb_id, app_1a_id, "data"),
            (app_1a_id, db_1a_id, "data"),
            (db_1a_id, db_1b_id, "monitoring")
        ], cell_id)
        
        return self._save_drawio(mxfile, f"{project_name}_network_from_png")
    
    def _create_component(self, root, cell_id: int, png_type: str, label: str, 
                         position: Dict, parent_id: str) -> int:
        """Crea componente DrawIO desde tipo PNG"""
        
        drawio_type = self.png_to_drawio_mapping.get(png_type, "rounded=1;whiteSpace=wrap;html=1;")
        style = self._get_aws_style(drawio_type)
        
        component = ET.SubElement(root, "mxCell",
            id=str(cell_id), value=label, style=style,
            vertex="1", parent=parent_id
        )
        
        size = {"width": 78, "height": 78}
        ET.SubElement(component, "mxGeometry", 
                     x=str(position["x"]), y=str(position["y"]),
                     width=str(size["width"]), height=str(size["height"]),
                     **{"as": "geometry"})
        
        return cell_id
    
    def _create_cluster(self, root, cell_id: int, label: str, 
                       geometry: Dict, parent_id: str) -> int:
        """Crea cluster DrawIO"""
        
        cluster = ET.SubElement(root, "mxCell",
            id=str(cell_id), value=label,
            style="fillColor=#E3F2FD;strokeColor=#1976D2;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#1976D2;whiteSpace=wrap;html=1;fontSize=12;",
            vertex="1", parent=parent_id
        )
        
        ET.SubElement(cluster, "mxGeometry",
                     x=str(geometry["x"]), y=str(geometry["y"]),
                     width=str(geometry["width"]), height=str(geometry["height"]),
                     **{"as": "geometry"})
        
        return cell_id
    
    def _create_connections(self, root, connections: List, start_cell_id: int):
        """Crea conexiones con estilos PNG"""
        
        edge_styles = {
            "primary": {"color": "#232F3E", "width": 3},
            "secondary": {"color": "#FF9900", "width": 2},
            "data": {"color": "#2196F3", "width": 2},
            "security": {"color": "#F44336", "width": 2},
            "monitoring": {"color": "#FF9800", "width": 2}
        }
        
        cell_id = start_cell_id
        for source_id, target_id, style_name in connections:
            style = edge_styles.get(style_name, edge_styles["primary"])
            
            edge = ET.SubElement(root, "mxCell",
                id=str(cell_id), value="",
                style=f"endArrow=classic;html=1;rounded=0;strokeColor={style['color']};strokeWidth={style['width']};",
                edge="1", parent="1", source=str(source_id), target=str(target_id)
            )
            ET.SubElement(edge, "mxGeometry", width="50", height="50", relative="1", **{"as": "geometry"})
            cell_id += 1
    
    def _get_aws_style(self, drawio_type: str) -> str:
        """Obtiene estilo AWS para DrawIO"""
        
        if drawio_type.startswith("mxgraph.aws4"):
            return f"sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape={drawio_type};"
        else:
            return "rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;"
    
    def _save_drawio(self, mxfile, filename: str) -> str:
        """Guarda archivo DrawIO"""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = self.output_dir / "drawio" / f"{filename}_{timestamp}.drawio"
        
        ET.indent(mxfile, space="  ")
        xml_str = ET.tostring(mxfile, encoding='unicode', xml_declaration=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_str)
        
        return str(output_path)
    
    def _generate_microservices_from_png_logic(self, project_name: str) -> str:
        """Genera microservices usando lógica PNG"""
        # Implementar lógica específica de microservices
        return self._generate_generic_from_png_logic("microservices", project_name)
    
    def _generate_security_from_png_logic(self, project_name: str) -> str:
        """Genera security usando lógica PNG"""
        # Implementar lógica específica de security
        return self._generate_generic_from_png_logic("security", project_name)
    
    def _generate_dataflow_from_png_logic(self, project_name: str) -> str:
        """Genera data flow usando lógica PNG"""
        # Implementar lógica específica de data flow
        return self._generate_generic_from_png_logic("data_flow", project_name)
    
    def _generate_generic_from_png_logic(self, diagram_type: str, project_name: str) -> str:
        """Genera diagrama genérico desde lógica PNG"""
        
        mxfile = ET.Element("mxfile", host="app.diagrams.net")
        diagram = ET.SubElement(mxfile, "diagram", name=f"{diagram_type.title()} Architecture", id=diagram_type)
        model = ET.SubElement(diagram, "mxGraphModel", dx="1600", dy="900", grid="1", gridSize="10")
        root = ET.SubElement(model, "root")
        
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        
        # Título
        title = ET.SubElement(root, "mxCell",
            id="2", value=f"{project_name.upper()} - {diagram_type.title()} Architecture",
            style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;fontColor=#FFFFFF;fontSize=18;fontStyle=1;",
            vertex="1", parent="1"
        )
        ET.SubElement(title, "mxGeometry", x="50", y="20", width="1500", height="50", **{"as": "geometry"})
        
        return self._save_drawio(mxfile, f"{project_name}_{diagram_type}_from_png")
