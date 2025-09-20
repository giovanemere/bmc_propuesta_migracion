#!/usr/bin/env python3
"""
Fixed DrawIO Generator - Corrige errores de mxCell
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

class FixedDrawIOGenerator:
    """Generador DrawIO corregido sin errores mxCell"""
    
    def __init__(self, config: dict, output_dir: str = "outputs"):
        self.config = config
        self.output_dir = Path(output_dir)
        
    def generate_fixed_drawio(self, project_name: str) -> str:
        """Genera archivo DrawIO válido sin errores mxCell"""
        
        # Crear estructura XML válida
        mxfile = ET.Element("mxfile", host="app.diagrams.net")
        diagram = ET.SubElement(mxfile, "diagram", name=f"{project_name} Architecture", id="arch")
        model = ET.SubElement(diagram, "mxGraphModel", dx="1600", dy="900", grid="1", gridSize="10")
        root = ET.SubElement(model, "root")
        
        # Celdas base requeridas
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        
        # Título
        title_cell = ET.SubElement(root, "mxCell", 
            id="title",
            value=f"{project_name} AWS Architecture",
            style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=none;fontColor=#FFFFFF;fontSize=18;fontStyle=1;align=center;",
            vertex="1",
            parent="1"
        )
        ET.SubElement(title_cell, "mxGeometry", x="50", y="20", width="1500", height="50", **{"as": "geometry"})
        
        # AWS Cloud container
        aws_cell = ET.SubElement(root, "mxCell",
            id="aws_cloud",
            value="AWS Cloud",
            style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;strokeWidth=2;fontSize=14;fontStyle=1;verticalAlign=top;",
            vertex="1",
            parent="1"
        )
        ET.SubElement(aws_cell, "mxGeometry", x="100", y="100", width="1400", height="700", **{"as": "geometry"})
        
        # Application Layer
        app_cell = ET.SubElement(root, "mxCell",
            id="app_layer",
            value="Application Layer - ECS Fargate",
            style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#4CAF50;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;",
            vertex="1",
            parent="1"
        )
        ET.SubElement(app_cell, "mxGeometry", x="200", y="200", width="800", height="200", **{"as": "geometry"})
        
        # Microservicios
        microservices = self.config.get("microservices", {})
        x_pos = 300
        
        for i, (service_name, service_config) in enumerate(list(microservices.items())[:5]):
            service_cell = ET.SubElement(root, "mxCell",
                id=f"service_{i}",
                value=service_name.replace("_", " ").title(),
                style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.fargate;",
                vertex="1",
                parent="1"
            )
            ET.SubElement(service_cell, "mxGeometry", x=str(x_pos), y="280", width="40", height="40", **{"as": "geometry"})
            x_pos += 120
        
        # Data Layer
        data_cell = ET.SubElement(root, "mxCell",
            id="data_layer",
            value="Data Layer",
            style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4EC;strokeColor=#E91E63;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;",
            vertex="1",
            parent="1"
        )
        ET.SubElement(data_cell, "mxGeometry", x="200", y="500", width="600", height="150", **{"as": "geometry"})
        
        # RDS
        rds_cell = ET.SubElement(root, "mxCell",
            id="rds_db",
            value="RDS PostgreSQL",
            style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#116D5B;strokeColor=#ffffff;shape=mxgraph.aws4.rds;",
            vertex="1",
            parent="1"
        )
        ET.SubElement(rds_cell, "mxGeometry", x="300", y="580", width="40", height="40", **{"as": "geometry"})
        
        # S3
        s3_cell = ET.SubElement(root, "mxCell",
            id="s3_storage",
            value="S3 Storage",
            style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#277116;strokeColor=#ffffff;shape=mxgraph.aws4.s3;",
            vertex="1",
            parent="1"
        )
        ET.SubElement(s3_cell, "mxGeometry", x="500", y="580", width="40", height="40", **{"as": "geometry"})
        
        # Generar XML válido
        ET.indent(mxfile, space="  ")
        xml_str = ET.tostring(mxfile, encoding='unicode', xml_declaration=True)
        
        # Guardar archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{project_name.lower()}_fixed_{timestamp}.drawio"
        output_path = self.output_dir / "mcp" / "diagrams" / "bmc_input" / "drawio" / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_str)
        
        print(f"✅ DrawIO corregido generado: {output_path}")
        return str(output_path)
    
    def validate_drawio_file(self, file_path: str) -> bool:
        """Valida que el archivo DrawIO sea válido"""
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            # Verificar estructura básica
            if root.tag != "mxfile":
                return False
            
            diagram = root.find("diagram")
            if diagram is None:
                return False
            
            model = diagram.find("mxGraphModel")
            if model is None:
                return False
            
            graph_root = model.find("root")
            if graph_root is None:
                return False
            
            # Verificar celdas base
            cells = graph_root.findall("mxCell")
            if len(cells) < 2:
                return False
            
            # Verificar que existe celda 0 y 1
            cell_ids = [cell.get("id") for cell in cells]
            if "0" not in cell_ids or "1" not in cell_ids:
                return False
            
            print(f"✅ Archivo DrawIO válido: {file_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error validando DrawIO: {e}")
            return False
