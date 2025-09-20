#!/usr/bin/env python3
"""
Simple DrawIO Generator - Versión corregida sin errores mxCell
"""

from pathlib import Path
from datetime import datetime

class SimpleDrawioGenerator:
    """Generador DrawIO simple sin errores"""
    
    def __init__(self, config: dict, output_dir: str = "outputs"):
        self.config = config
        self.output_dir = Path(output_dir)
        
    def generate_simple_drawio(self, project_name: str) -> str:
        """Genera DrawIO simple válido"""
        
        microservices = self.config.get("microservices", {})
        
        # XML válido sin errores mxCell
        xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net">
  <diagram name="{project_name} Architecture" id="1">
    <mxGraphModel dx="1600" dy="900" grid="1" gridSize="10">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="title" value="{project_name} AWS Architecture" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;fontColor=#FFFFFF;fontSize=16;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="800" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="aws" value="AWS Cloud" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;" vertex="1" parent="1">
          <mxGeometry x="100" y="100" width="700" height="500" as="geometry"/>
        </mxCell>'''
        
        # Agregar microservicios
        y_pos = 200
        for i, service_name in enumerate(list(microservices.keys())[:4]):
            xml += f'''
        <mxCell id="svc{i}" value="{service_name.replace('_', ' ').title()}" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D05C17;fontColor=#FFFFFF;" vertex="1" parent="1">
          <mxGeometry x="200" y="{y_pos}" width="120" height="60" as="geometry"/>
        </mxCell>'''
            y_pos += 80
        
        xml += '''
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
        
        # Guardar archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{project_name.lower()}_simple_{timestamp}.drawio"
        output_path = self.output_dir / "mcp" / "diagrams" / "bmc_input" / "drawio" / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml)
        
        return str(output_path)
    
    def generate_simple_architecture(self, project_name: str) -> str:
        """Alias para compatibilidad"""
        return self.generate_simple_drawio(project_name)
