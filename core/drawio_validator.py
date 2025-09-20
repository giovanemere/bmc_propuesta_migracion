#!/usr/bin/env python3
"""
Draw.io Validator - Valida y corrige archivos Draw.io
"""

import xml.etree.ElementTree as ET
import re
from pathlib import Path

class DrawioValidator:
    """Validador y corrector de archivos Draw.io"""
    
    def __init__(self):
        self.errors = []
        
    def validate_and_fix(self, file_path: str) -> bool:
        """Valida y corrige un archivo Draw.io"""
        
        try:
            # Leer archivo
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Verificar estructura básica
            if not content.strip().startswith('<mxfile'):
                self.errors.append("Invalid mxfile header")
                return False
            
            # Limpiar contenido
            fixed_content = self._fix_common_issues(content)
            
            # Validar XML
            try:
                ET.fromstring(fixed_content)
            except ET.ParseError as e:
                self.errors.append(f"XML Parse Error: {e}")
                return False
            
            # Escribir archivo corregido si hay cambios
            if fixed_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                print(f"✓ Fixed Draw.io file: {file_path}")
            
            return True
            
        except Exception as e:
            self.errors.append(f"Validation error: {e}")
            return False
    
    def _fix_common_issues(self, content: str) -> str:
        """Corrige problemas comunes en archivos Draw.io"""
        
        # Eliminar líneas vacías extra
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # Corregir caracteres especiales en valores
        content = re.sub(r'value="([^"]*)"', self._fix_value_attribute, content)
        
        # Asegurar cierre correcto de tags
        content = re.sub(r'<mxCell([^>]*)/>', r'<mxCell\1></mxCell>', content)
        
        # Corregir encoding de caracteres especiales
        content = content.replace('&', '&amp;')
        content = content.replace('<', '&lt;').replace('>', '&gt;')
        
        # Restaurar tags XML válidos
        content = re.sub(r'&lt;mxfile', '<mxfile', content)
        content = re.sub(r'&lt;/mxfile&gt;', '</mxfile>', content)
        content = re.sub(r'&lt;diagram', '<diagram', content)
        content = re.sub(r'&lt;/diagram&gt;', '</diagram>', content)
        content = re.sub(r'&lt;mxGraphModel', '<mxGraphModel', content)
        content = re.sub(r'&lt;/mxGraphModel&gt;', '</mxGraphModel>', content)
        content = re.sub(r'&lt;root&gt;', '<root>', content)
        content = re.sub(r'&lt;/root&gt;', '</root>', content)
        content = re.sub(r'&lt;mxCell', '<mxCell', content)
        content = re.sub(r'&lt;/mxCell&gt;', '</mxCell>', content)
        content = re.sub(r'&lt;mxGeometry', '<mxGeometry', content)
        content = re.sub(r'/&gt;', '/>', content)
        
        return content
    
    def _fix_value_attribute(self, match):
        """Corrige atributos value con caracteres especiales"""
        value = match.group(1)
        
        # Escapar caracteres especiales en valores
        value = value.replace('&', '&amp;')
        value = value.replace('<', '&lt;')
        value = value.replace('>', '&gt;')
        value = value.replace('"', '&quot;')
        
        return f'value="{value}"'
    
    def create_minimal_valid_drawio(self, project_name: str, output_path: str) -> str:
        """Crea un archivo Draw.io mínimo válido"""
        
        minimal_content = f'''<mxfile host="app.diagrams.net" modified="2025-09-19T20:00:00.000Z" agent="BMC Generator" version="22.1.11">
  <diagram name="{project_name} - Architecture" id="arch">
    <mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1600" pageHeight="900">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Title -->
        <mxCell id="title" value="{project_name} AWS Architecture" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=none;fontColor=#FFFFFF;fontSize=18;fontStyle=1;align=center;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1500" height="50" as="geometry"/>
        </mxCell>
        
        <!-- AWS Cloud -->
        <mxCell id="aws" value="AWS Cloud" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;strokeWidth=2;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=15;" vertex="1" parent="1">
          <mxGeometry x="100" y="100" width="1400" height="700" as="geometry"/>
        </mxCell>
        
        <!-- Microservices -->
        <mxCell id="services" value="ECS Fargate Services" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#4CAF50;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="200" y="200" width="600" height="200" as="geometry"/>
        </mxCell>
        
        <!-- Service 1 -->
        <mxCell id="service1" value="Invoice Service" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="300" y="250" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Service 2 -->
        <mxCell id="service2" value="Product Service" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="500" y="250" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Database -->
        <mxCell id="database" value="RDS PostgreSQL" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;shape=mxgraph.aws4.rds;" vertex="1" parent="1">
          <mxGeometry x="300" y="500" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Storage -->
        <mxCell id="storage" value="S3 Storage" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;shape=mxgraph.aws4.s3;" vertex="1" parent="1">
          <mxGeometry x="500" y="500" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Connections -->
        <mxCell id="c1" style="endArrow=classic;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="service1" target="database"/>
        <mxCell id="c2" style="endArrow=classic;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="service2" target="storage"/>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
        
        # Guardar archivo
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(minimal_content)
        
        return output_path
