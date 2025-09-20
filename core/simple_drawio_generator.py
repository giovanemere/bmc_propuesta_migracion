#!/usr/bin/env python3
"""
Simple Draw.io Generator - Generador simple y válido
"""

import os
from typing import Dict, Any

class SimpleDrawioGenerator:
    """Generador simple de Draw.io válido"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str = "output"):
        self.config = config
        self.output_dir = output_dir
    
    def generate_simple_architecture(self, project_name: str) -> str:
        """Genera arquitectura simple válida"""
        
        microservices = self.config.get("microservices", {})
        aws_services = self.config.get("aws_services", {})
        
        # XML simple y válido
        xml_content = f'''<mxfile host="app.diagrams.net">
  <diagram name="{project_name} Architecture" id="arch">
    <mxGraphModel dx="1600" dy="900" grid="1" gridSize="10">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <mxCell id="title" value="{project_name} AWS Architecture" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=none;fontColor=#FFFFFF;fontSize=18;fontStyle=1;align=center;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1500" height="50" as="geometry"/>
        </mxCell>
        
        <mxCell id="aws" value="AWS Cloud" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;strokeWidth=2;fontSize=14;fontStyle=1;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="100" y="100" width="1400" height="700" as="geometry"/>
        </mxCell>
        
        <mxCell id="app_layer" value="Application Layer - ECS Fargate" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#4CAF50;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="200" y="200" width="800" height="200" as="geometry"/>
        </mxCell>'''
        
        # Agregar microservicios
        x_pos = 300
        for service_name in list(microservices.keys())[:5]:
            xml_content += f'''
        <mxCell id="{service_name}" value="{service_name.title()}" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="{x_pos}" y="280" width="40" height="40" as="geometry"/>
        </mxCell>'''
            x_pos += 120
        
        # Agregar servicios de datos
        xml_content += '''
        <mxCell id="data_layer" value="Data Layer" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4EC;strokeColor=#E91E63;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="200" y="500" width="600" height="150" as="geometry"/>
        </mxCell>
        
        <mxCell id="rds" value="RDS PostgreSQL" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#116D5B;strokeColor=#ffffff;shape=mxgraph.aws4.rds;" vertex="1" parent="1">
          <mxGeometry x="300" y="580" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <mxCell id="s3" value="S3 Storage" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#277116;strokeColor=#ffffff;shape=mxgraph.aws4.s3;" vertex="1" parent="1">
          <mxGeometry x="500" y="580" width="40" height="40" as="geometry"/>
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
        
        # Guardar archivo
        output_file = f"{self.output_dir}/drawio/{project_name.lower()}_simple_architecture.drawio"
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        
        return output_file
