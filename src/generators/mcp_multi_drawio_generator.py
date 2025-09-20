#!/usr/bin/env python3
"""
MCP Multi DrawIO Generator - Genera 4 DrawIO equivalentes a PNG
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List

class MCPMultiDrawIOGenerator:
    """Generador de múltiples DrawIO equivalentes a PNG"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str):
        self.config = config
        self.output_dir = Path(output_dir)
        self.schemas = self._load_schemas()
        
        # Estilos de conexión equivalentes a PNG
        self.edge_styles = {
            "primary": {"color": "#232F3E", "width": 3},
            "secondary": {"color": "#FF9900", "width": 2}, 
            "data": {"color": "#2196F3", "width": 2},
            "security": {"color": "#F44336", "width": 2},
            "monitoring": {"color": "#FF9800", "width": 2}
        }
    
    def _load_schemas(self) -> Dict[str, Any]:
        """Carga todos los esquemas MCP"""
        schemas = {}
        schema_files = [
            "network-architecture-schema.json",
            "microservices-architecture-schema.json", 
            "security-architecture-schema.json",
            "dataflow-architecture-schema.json"
        ]
        
        for schema_file in schema_files:
            schema_path = Path("config") / schema_file
            if schema_path.exists():
                with open(schema_path, 'r', encoding='utf-8') as f:
                    schema_data = json.load(f)
                    schema_name = schema_file.replace("-schema.json", "").replace("-", "_")
                    schemas[schema_name] = schema_data
        
        return schemas
    
    def generate_all_drawio_diagrams(self, project_name: str = "bmc_input") -> Dict[str, str]:
        """Genera todos los diagramas DrawIO equivalentes a PNG"""
        
        results = {}
        
        # Generar Network Architecture (equivalente a PNG network)
        if "network_architecture" in self.schemas:
            network_drawio = self._generate_network_drawio(project_name)
            results["network_architecture"] = network_drawio
        
        # Generar Microservices (equivalente a PNG microservices)
        microservices_drawio = self._generate_microservices_drawio(project_name)
        results["microservices_detailed"] = microservices_drawio
        
        # Generar Security (equivalente a PNG security)
        security_drawio = self._generate_security_drawio(project_name)
        results["security_architecture"] = security_drawio
        
        # Generar Data Flow (equivalente a PNG data_flow)
        dataflow_drawio = self._generate_dataflow_drawio(project_name)
        results["data_flow"] = dataflow_drawio
        
        return results
    
    def _generate_network_drawio(self, project_name: str) -> str:
        """Genera DrawIO de Network Architecture equivalente a PNG"""
        
        schema = self.schemas["network_architecture"]["network_architecture"]
        
        # Crear XML DrawIO
        mxfile = ET.Element("mxfile", host="app.diagrams.net")
        diagram = ET.SubElement(mxfile, "diagram", name="Network Architecture", id="network")
        model = ET.SubElement(diagram, "mxGraphModel", dx="2500", dy="1600", grid="1", gridSize="10")
        root = ET.SubElement(model, "root")
        
        # Celdas base
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        
        cell_id = 2
        
        # Título
        title = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value=schema["metadata"]["title"],
            style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;fontColor=#FFFFFF;fontSize=18;fontStyle=1;",
            vertex="1", parent="1"
        )
        ET.SubElement(title, "mxGeometry", x="50", y="20", width="2400", height="50", **{"as": "geometry"})
        cell_id += 1
        
        # Usar layout automático para posicionar componentes
        positioned_components = self._auto_layout_components(schema["components"])
        
        # Generar componentes con posiciones automáticas
        component_ids = {}
        for component in positioned_components:
            comp_id = self._create_component(root, component, cell_id, "1")
            component_ids[component["id"]] = comp_id
            cell_id = comp_id + 1
        
        # Generar conexiones
        self._create_connections(root, schema["connections"], component_ids, cell_id)
        
        # Guardar archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{project_name}_network_architecture_{timestamp}.drawio"
        output_path = self.output_dir / "drawio" / filename
        
        ET.indent(mxfile, space="  ")
        xml_str = ET.tostring(mxfile, encoding='unicode', xml_declaration=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_str)
        
        return str(output_path)
    
    def _generate_microservices_drawio(self, project_name: str) -> str:
        """Genera DrawIO de Microservices equivalente a PNG"""
        
        # Crear DrawIO enfocado en microservicios
        mxfile = ET.Element("mxfile", host="app.diagrams.net")
        diagram = ET.SubElement(mxfile, "diagram", name="Microservices Architecture", id="microservices")
        model = ET.SubElement(diagram, "mxGraphModel", dx="2000", dy="1400", grid="1", gridSize="10")
        root = ET.SubElement(model, "root")
        
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        
        cell_id = 2
        
        # Título
        title = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value=f"{project_name.upper()} - Microservices Architecture",
            style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;fontColor=#FFFFFF;fontSize=18;fontStyle=1;",
            vertex="1", parent="1"
        )
        ET.SubElement(title, "mxGeometry", x="50", y="20", width="1800", height="50", **{"as": "geometry"})
        cell_id += 1
        
        # Microservicios del config
        microservices = self.config.get("microservices", {})
        x_pos = 200
        
        for service_name, service_config in microservices.items():
            # Crear microservicio
            service_cell = ET.SubElement(root, "mxCell",
                id=str(cell_id),
                value=f"{service_name.replace('_', ' ').title()}\\nECS Fargate\\n{service_config.get('business_function', '')}\\nCPU: 2 vCPU\\nRAM: 4 GB",
                style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;",
                vertex="1", parent="1"
            )
            ET.SubElement(service_cell, "mxGeometry", x=str(x_pos), y="200", width="120", height="120", **{"as": "geometry"})
            cell_id += 1
            x_pos += 200
        
        # Guardar archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{project_name}_microservices_detailed_{timestamp}.drawio"
        output_path = self.output_dir / "drawio" / filename
        
        ET.indent(mxfile, space="  ")
        xml_str = ET.tostring(mxfile, encoding='unicode', xml_declaration=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_str)
        
        return str(output_path)
    
    def _generate_security_drawio(self, project_name: str) -> str:
        """Genera DrawIO de Security equivalente a PNG"""
        
        # Crear DrawIO enfocado en seguridad
        mxfile = ET.Element("mxfile", host="app.diagrams.net")
        diagram = ET.SubElement(mxfile, "diagram", name="Security Architecture", id="security")
        model = ET.SubElement(diagram, "mxGraphModel", dx="2000", dy="1400", grid="1", gridSize="10")
        root = ET.SubElement(model, "root")
        
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        
        # Título y componentes de seguridad
        title = ET.SubElement(root, "mxCell",
            id="2",
            value=f"{project_name.upper()} - Security Architecture",
            style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;fontColor=#FFFFFF;fontSize=18;fontStyle=1;",
            vertex="1", parent="1"
        )
        ET.SubElement(title, "mxGeometry", x="50", y="20", width="1800", height="50", **{"as": "geometry"})
        
        # Componentes de seguridad
        security_components = [
            {"id": "waf", "type": "aws4.waf", "label": "AWS WAF\\nDDoS Protection", "x": 200, "y": 150},
            {"id": "cognito", "type": "aws4.cognito", "label": "Cognito\\nUser Pool", "x": 400, "y": 150},
            {"id": "kms", "type": "aws4.kms", "label": "AWS KMS\\nEncryption", "x": 600, "y": 150}
        ]
        
        for comp in security_components:
            comp_cell = ET.SubElement(root, "mxCell",
                id=comp["id"],
                value=comp["label"],
                style=self._get_aws_style(comp["type"]),
                vertex="1", parent="1"
            )
            ET.SubElement(comp_cell, "mxGeometry", x=str(comp["x"]), y=str(comp["y"]), width="100", height="100", **{"as": "geometry"})
        
        # Guardar archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{project_name}_security_architecture_{timestamp}.drawio"
        output_path = self.output_dir / "drawio" / filename
        
        ET.indent(mxfile, space="  ")
        xml_str = ET.tostring(mxfile, encoding='unicode', xml_declaration=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_str)
        
        return str(output_path)
    
    def _generate_dataflow_drawio(self, project_name: str) -> str:
        """Genera DrawIO de Data Flow equivalente a PNG"""
        
        # Crear DrawIO enfocado en flujo de datos
        mxfile = ET.Element("mxfile", host="app.diagrams.net")
        diagram = ET.SubElement(mxfile, "diagram", name="Data Flow Architecture", id="dataflow")
        model = ET.SubElement(diagram, "mxGraphModel", dx="2000", dy="1400", grid="1", gridSize="10")
        root = ET.SubElement(model, "root")
        
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        
        # Título
        title = ET.SubElement(root, "mxCell",
            id="2",
            value=f"{project_name.upper()} - Data Flow Architecture",
            style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;fontColor=#FFFFFF;fontSize=18;fontStyle=1;",
            vertex="1", parent="1"
        )
        ET.SubElement(title, "mxGeometry", x="50", y="20", width="1800", height="50", **{"as": "geometry"})
        
        # Componentes de datos
        data_components = [
            {"id": "api", "type": "aws4.api_gateway", "label": "API Gateway\\nData Entry", "x": 200, "y": 150},
            {"id": "processing", "type": "aws4.fargate", "label": "Data Processing\\nFargate", "x": 500, "y": 150},
            {"id": "database", "type": "aws4.rds", "label": "RDS\\n60M Products", "x": 800, "y": 150},
            {"id": "storage", "type": "aws4.s3", "label": "S3\\nFile Storage", "x": 1100, "y": 150}
        ]
        
        for comp in data_components:
            comp_cell = ET.SubElement(root, "mxCell",
                id=comp["id"],
                value=comp["label"],
                style=self._get_aws_style(comp["type"]),
                vertex="1", parent="1"
            )
            ET.SubElement(comp_cell, "mxGeometry", x=str(comp["x"]), y=str(comp["y"]), width="100", height="100", **{"as": "geometry"})
        
        # Conexiones de flujo de datos
        connections = [
            {"from": "api", "to": "processing"},
            {"from": "processing", "to": "database"},
            {"from": "processing", "to": "storage"}
        ]
        
        cell_id = 10
        for conn in connections:
            edge = ET.SubElement(root, "mxCell",
                id=str(cell_id),
                value="",
                style="endArrow=classic;html=1;rounded=0;strokeColor=#2196F3;strokeWidth=2;",
                edge="1", parent="1", source=conn["from"], target=conn["to"]
            )
            ET.SubElement(edge, "mxGeometry", width="50", height="50", relative="1", **{"as": "geometry"})
            cell_id += 1
        
        # Guardar archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{project_name}_data_flow_{timestamp}.drawio"
        output_path = self.output_dir / "drawio" / filename
        
        ET.indent(mxfile, space="  ")
        xml_str = ET.tostring(mxfile, encoding='unicode', xml_declaration=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_str)
        
        return str(output_path)
    
    def _auto_layout_components(self, components: List[Dict]) -> List[Dict]:
        """Aplica layout automático a componentes"""
        
        # Layout simple: distribución en grid
        positioned = []
        x, y = 100, 100
        
        for component in components:
            component["position"] = {"x": x, "y": y}
            component["size"] = {"width": 100, "height": 100}
            positioned.append(component)
            
            x += 200
            if x > 1800:
                x = 100
                y += 150
        
        return positioned
    
    def _create_component(self, root, component, cell_id, parent_id):
        """Crea componente en DrawIO"""
        
        comp = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value=component["label"],
            style=self._get_aws_style(component["type"]),
            vertex="1", parent=parent_id
        )
        
        pos = component.get("position", {"x": 100, "y": 100})
        size = component.get("size", {"width": 100, "height": 100})
        
        ET.SubElement(comp, "mxGeometry", 
                     x=str(pos["x"]), y=str(pos["y"]), 
                     width=str(size["width"]), height=str(size["height"]), 
                     **{"as": "geometry"})
        
        return cell_id
    
    def _create_connections(self, root, connections, component_ids, cell_id):
        """Crea conexiones entre componentes"""
        
        for conn in connections:
            from_id = component_ids.get(conn["from"])
            to_id = component_ids.get(conn["to"])
            
            if from_id and to_id:
                style_name = conn.get("style", "primary")
                style = self.edge_styles.get(style_name, self.edge_styles["primary"])
                
                edge = ET.SubElement(root, "mxCell",
                    id=str(cell_id),
                    value="",
                    style=f"endArrow=classic;html=1;rounded=0;strokeColor={style['color']};strokeWidth={style['width']};",
                    edge="1", parent="1", 
                    source=str(from_id), target=str(to_id)
                )
                ET.SubElement(edge, "mxGeometry", width="50", height="50", relative="1", **{"as": "geometry"})
                cell_id += 1
    
    def _get_aws_style(self, component_type):
        """Obtiene estilo AWS para componente"""
        
        aws_styles = {
            "aws4.users": "sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#4CAF50;strokeColor=#2E7D32;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=11;fontStyle=1;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.users;",
            "aws4.internet_gateway": "sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#1976D2;gradientDirection=north;fillColor=#0D47A1;strokeColor=#0277BD;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=11;fontStyle=1;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.internet_gateway;",
            "aws4.cloudfront": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudfront;",
            "aws4.waf": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.waf;",
            "aws4.api_gateway": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.api_gateway;",
            "aws4.fargate": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;",
            "aws4.rds": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.rds;",
            "aws4.s3": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;",
            "aws4.cognito": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cognito;",
            "aws4.elastic_load_balancing": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#8C4FFF;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elastic_load_balancing;",
            "aws4.kms": "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.kms;"
        }
        
        return aws_styles.get(component_type, "rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;")
