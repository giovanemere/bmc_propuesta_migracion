#!/usr/bin/env python3
"""
MCP DrawIO Generator - Genera DrawIO exacto desde esquema MCP
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

class MCPDrawIOGenerator:
    """Generador DrawIO exacto basado en esquema MCP"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str):
        self.config = config
        self.output_dir = Path(output_dir)
        
        # Cargar esquema de arquitectura
        schema_path = Path("config/drawio-architecture-schema.json")
        if schema_path.exists():
            with open(schema_path, 'r', encoding='utf-8') as f:
                self.architecture_schema = json.load(f)
        else:
            self.architecture_schema = None
    
    def generate_from_mcp_schema(self, project_name: str = "bmc_input") -> str:
        """Genera DrawIO exacto desde esquema MCP"""
        
        if not self.architecture_schema:
            return self._generate_fallback(project_name)
        
        schema = self.architecture_schema["drawio_architecture"]
        
        # Crear XML DrawIO
        mxfile = ET.Element("mxfile", host="app.diagrams.net")
        diagram = ET.SubElement(mxfile, "diagram", 
                               name=schema["metadata"]["title"], 
                               id="mcp_schema")
        
        canvas = schema["metadata"]["canvas"]
        model = ET.SubElement(diagram, "mxGraphModel", 
                             dx=str(canvas["width"]), 
                             dy=str(canvas["height"]), 
                             grid="1", 
                             gridSize=str(canvas["grid"]))
        root = ET.SubElement(model, "root")
        
        # Celdas base
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        
        cell_id = 2
        
        # Título desde metadata
        title = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value=f"{schema['metadata']['title']}\\n{schema['metadata']['subtitle']}",
            style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;fontColor=#FFFFFF;fontSize=16;fontStyle=1;",
            vertex="1", parent="1"
        )
        ET.SubElement(title, "mxGeometry", x="50", y="20", width="2800", height="70", **{"as": "geometry"})
        cell_id += 1
        
        # Procesar layers del esquema
        for layer in schema["layers"]:
            cell_id = self._process_layer(root, layer, cell_id)
        
        # Procesar conexiones
        self._process_connections(root, schema["connections"], cell_id)
        
        # Guardar archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{project_name}_mcp_schema_{timestamp}.drawio"
        output_path = self.output_dir / "drawio" / filename
        
        # Generar XML
        ET.indent(mxfile, space="  ")
        xml_str = ET.tostring(mxfile, encoding='unicode', xml_declaration=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_str)
        
        return str(output_path)
    
    def _process_layer(self, root, layer, cell_id):
        """Procesa una capa del esquema MCP"""
        
        if layer.get("type") == "container":
            # Crear contenedor
            container = ET.SubElement(root, "mxCell",
                id=str(cell_id),
                value=layer["label"],
                style=self._build_style(layer["style"]),
                vertex="1", parent="1"
            )
            pos = layer["position"]
            size = layer["size"]
            ET.SubElement(container, "mxGeometry", 
                         x=str(pos["x"]), y=str(pos["y"]), 
                         width=str(size["width"]), height=str(size["height"]), 
                         **{"as": "geometry"})
            
            container_id = cell_id
            cell_id += 1
            
            # Procesar hijos
            if "children" in layer:
                for child in layer["children"]:
                    cell_id = self._process_component(root, child, container_id, cell_id)
            
            if "components" in layer:
                for component in layer["components"]:
                    cell_id = self._process_component(root, component, container_id, cell_id)
        
        else:
            # Procesar componentes directos
            if "components" in layer:
                for component in layer["components"]:
                    cell_id = self._process_component(root, component, "1", cell_id)
        
        return cell_id
    
    def _process_component(self, root, component, parent_id, cell_id):
        """Procesa un componente individual"""
        
        # Determinar estilo AWS
        aws_style = self._get_aws_style(component["type"])
        
        # Crear componente
        comp = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value=component["label"],
            style=aws_style,
            vertex="1", parent=str(parent_id)
        )
        
        pos = component["position"]
        size = component.get("size", {"width": 100, "height": 100})
        ET.SubElement(comp, "mxGeometry", 
                     x=str(pos["x"]), y=str(pos["y"]), 
                     width=str(size["width"]), height=str(size["height"]), 
                     **{"as": "geometry"})
        
        # Guardar ID para conexiones
        component["_cell_id"] = cell_id
        cell_id += 1
        
        # Procesar componentes anidados
        if "components" in component:
            for nested in component["components"]:
                cell_id = self._process_component(root, nested, str(cell_id-1), cell_id)
        
        # Procesar subnets
        if "subnets" in component:
            for subnet in component["subnets"]:
                cell_id = self._process_subnet(root, subnet, str(cell_id-1), cell_id)
        
        return cell_id
    
    def _process_subnet(self, root, subnet, parent_id, cell_id):
        """Procesa una subnet"""
        
        # Crear subnet container
        subnet_container = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value=subnet["label"],
            style=self._get_subnet_style(subnet["type"]),
            vertex="1", parent=str(parent_id)
        )
        
        pos = subnet["position"]
        size = subnet["size"]
        ET.SubElement(subnet_container, "mxGeometry", 
                     x=str(pos["x"]), y=str(pos["y"]), 
                     width=str(size["width"]), height=str(size["height"]), 
                     **{"as": "geometry"})
        
        subnet_id = cell_id
        cell_id += 1
        
        # Procesar componentes de la subnet
        if "components" in subnet:
            for component in subnet["components"]:
                cell_id = self._process_component(root, component, str(subnet_id), cell_id)
        
        return cell_id
    
    def _process_connections(self, root, connections, cell_id):
        """Procesa las conexiones entre componentes"""
        
        for conn in connections:
            # Buscar IDs de componentes
            from_id = self._find_component_id(conn["from"])
            to_id = self._find_component_id(conn["to"])
            
            if from_id and to_id:
                edge = ET.SubElement(root, "mxCell",
                    id=str(cell_id),
                    value=conn.get("label", ""),
                    style=self._build_connection_style(conn["style"]),
                    edge="1", parent="1", 
                    source=str(from_id), target=str(to_id)
                )
                ET.SubElement(edge, "mxGeometry", width="50", height="50", relative="1", **{"as": "geometry"})
                cell_id += 1
    
    def _get_aws_style(self, component_type):
        """Obtiene estilo AWS para tipo de componente"""
        
        aws_styles = {
            "aws4.users": "sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#4CAF50;strokeColor=#2E7D32;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=11;fontStyle=1;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.users;",
            
            "aws4.internet_gateway": "sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#1976D2;gradientDirection=north;fillColor=#0D47A1;strokeColor=#0277BD;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=11;fontStyle=1;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.internet_gateway;",
            
            "aws4.cloudfront": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#4527A0;strokeWidth=2;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=1;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudfront;",
            
            "aws4.waf": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#B71C1C;strokeWidth=2;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=1;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.waf;",
            
            "aws4.route_53": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#4527A0;strokeWidth=2;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=1;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.route_53;",
            
            "aws4.api_gateway": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.api_gateway;",
            
            "aws4.fargate": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;",
            
            "aws4.rds": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.rds;",
            
            "aws4.elasticache": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elasticache;",
            
            "aws4.s3": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;",
            
            "aws4.cognito": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cognito;",
            
            "aws4.elastic_load_balancing": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#8C4FFF;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elastic_load_balancing;"
        }
        
        return aws_styles.get(component_type, "rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;")
    
    def _get_subnet_style(self, subnet_type):
        """Obtiene estilo para tipo de subnet"""
        
        subnet_styles = {
            "public_subnet": "fillColor=#E8F5E8;strokeColor=#4CAF50;strokeWidth=2;dashed=2;verticalAlign=top;fontStyle=0;fontColor=#2E7D32;whiteSpace=wrap;html=1;fontSize=10;",
            "private_subnet": "fillColor=#FFF3E0;strokeColor=#FF9800;strokeWidth=2;dashed=2;verticalAlign=top;fontStyle=0;fontColor=#E65100;whiteSpace=wrap;html=1;fontSize=10;",
            "isolated_subnet": "fillColor=#FFEBEE;strokeColor=#F44336;strokeWidth=2;dashed=2;verticalAlign=top;fontStyle=0;fontColor=#C62828;whiteSpace=wrap;html=1;fontSize=10;"
        }
        
        return subnet_styles.get(subnet_type, "fillColor=#F5F5F5;strokeColor=#666666;dashed=1;")
    
    def _build_style(self, style_dict):
        """Construye string de estilo desde diccionario"""
        
        style_parts = []
        for key, value in style_dict.items():
            if key == "dashed" and value:
                style_parts.append("dashed=1")
            else:
                style_parts.append(f"{key}={value}")
        
        return ";".join(style_parts) + ";"
    
    def _build_connection_style(self, style_dict):
        """Construye estilo para conexiones"""
        
        base_style = "endArrow=classic;html=1;rounded=0;"
        style_parts = [base_style]
        
        for key, value in style_dict.items():
            style_parts.append(f"{key}={value}")
        
        return ";".join(style_parts) + ";"
    
    def _find_component_id(self, component_name):
        """Busca ID de componente por nombre"""
        # Implementar búsqueda en estructura generada
        return None  # Placeholder
    
    def _generate_fallback(self, project_name):
        """Genera DrawIO básico si no hay esquema"""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{project_name}_fallback_{timestamp}.drawio"
        output_path = self.output_dir / "drawio" / filename
        
        # DrawIO básico
        basic_xml = """<?xml version='1.0' encoding='utf-8'?>
<mxfile host="app.diagrams.net">
  <diagram name="Basic Architecture" id="basic">
    <mxGraphModel dx="1600" dy="900" grid="1" gridSize="10">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="2" value="BMC Architecture - Schema Not Found" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
          <mxGeometry x="50" y="50" width="400" height="50" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(basic_xml)
        
        return str(output_path)
