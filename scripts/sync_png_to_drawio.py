#!/usr/bin/env python3
"""
Sync PNG to Draw.io - Crea archivos Draw.io para todos los PNG existentes
"""

import os
import glob
from pathlib import Path

def create_basic_drawio(png_file: str, title: str) -> str:
    """Crea un archivo Draw.io básico basado en el PNG"""
    
    xml_template = f'''<mxfile host="app.diagrams.net">
  <diagram name="{title}" id="diagram">
    <mxGraphModel dx="1800" dy="1000" grid="1" gridSize="10">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Title -->
        <mxCell id="title" value="{title}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=none;fontColor=#FFFFFF;fontSize=18;fontStyle=1;align=center;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1500" height="50" as="geometry"/>
        </mxCell>
        
        <!-- Note -->
        <mxCell id="note" value="This Draw.io file corresponds to: {png_file}&#10;&#10;Edit this diagram at: https://app.diagrams.net&#10;&#10;Generated automatically from PNG file." style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1F5FE;strokeColor=#0277BD;fontSize=12;align=left;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="50" y="100" width="400" height="120" as="geometry"/>
        </mxCell>
        
        <!-- AWS Cloud Placeholder -->
        <mxCell id="aws" value="AWS Cloud Architecture&#10;&#10;Components from {png_file}:&#10;• Microservices&#10;• Databases&#10;• Security Layers&#10;• Network Topology" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;strokeWidth=3;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=20;" vertex="1" parent="1">
          <mxGeometry x="500" y="100" width="800" height="400" as="geometry"/>
        </mxCell>
        
        <!-- Placeholder Services -->
        <mxCell id="service1" value="Service 1" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="600" y="200" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="service2" value="Service 2" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;shape=mxgraph.aws4.rds;" vertex="1" parent="1">
          <mxGeometry x="800" y="200" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="service3" value="Service 3" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;shape=mxgraph.aws4.s3;" vertex="1" parent="1">
          <mxGeometry x="1000" y="200" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Connection -->
        <mxCell id="c1" style="endArrow=classic;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="service1" target="service2"/>
        <mxCell id="c2" style="endArrow=classic;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="service2" target="service3"/>
        
        <!-- Instructions -->
        <mxCell id="instructions" value="Instructions:&#10;1. Open this file in https://app.diagrams.net&#10;2. Replace placeholder components with actual AWS services&#10;3. Add detailed configuration and connections&#10;4. Use official AWS icons from the library&#10;5. Save and export as needed" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF8E1;strokeColor=#FFC107;fontSize=11;align=left;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="50" y="300" width="400" height="150" as="geometry"/>
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    return xml_template

def sync_png_to_drawio():
    """Sincroniza PNG a Draw.io"""
    
    print("🔄 Syncing PNG files to Draw.io...")
    
    png_dir = Path("output/png")
    drawio_dir = Path("output/drawio")
    
    if not png_dir.exists():
        print("❌ PNG directory not found")
        return
    
    drawio_dir.mkdir(exist_ok=True)
    
    # Buscar archivos PNG
    png_files = list(png_dir.glob("*.png"))
    
    print(f"📁 Found {len(png_files)} PNG files")
    
    created_count = 0
    
    for png_file in png_files:
        # Generar nombre del Draw.io
        drawio_name = png_file.stem + ".drawio"
        drawio_path = drawio_dir / drawio_name
        
        # Solo crear si no existe
        if not drawio_path.exists():
            # Generar título
            title = png_file.stem.replace("_", " ").title()
            title = title.replace("Bmc", "BMC").replace("Aws", "AWS")
            
            # Crear contenido Draw.io
            xml_content = create_basic_drawio(png_file.name, title)
            
            # Guardar archivo
            with open(drawio_path, 'w', encoding='utf-8') as f:
                f.write(xml_content)
            
            print(f"✓ Created: {drawio_name}")
            created_count += 1
        else:
            print(f"⚠️ Exists: {drawio_name}")
    
    print(f"\n📊 Summary:")
    print(f"  - PNG files found: {len(png_files)}")
    print(f"  - Draw.io files created: {created_count}")
    print(f"  - Total Draw.io files: {len(list(drawio_dir.glob('*.drawio')))}")
    
    print(f"\n📁 Final Draw.io files:")
    for drawio_file in sorted(drawio_dir.glob("*.drawio")):
        size = drawio_file.stat().st_size
        print(f"  - {drawio_file.name} ({size:,} bytes)")

if __name__ == "__main__":
    sync_png_to_drawio()
