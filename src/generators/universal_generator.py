#!/usr/bin/env python3
"""
Universal Generator - PNG y DrawIO desde mismo esquema
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Tuple
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Fargate
from diagrams.aws.database import RDS
from diagrams.aws.network import APIGateway, ELB
from diagrams.aws.security import Cognito, WAF
from diagrams.onprem.client import Users
from diagrams.onprem.network import Internet

from ..core.universal_schema import UniversalDiagramSchema, DiagramType, OutputFormat

class UniversalGenerator:
    """Generador universal para PNG y DrawIO desde mismo esquema"""
    
    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        
        # Mapeo de tipos a componentes
        self.component_mapping = {
            # PNG (diagrams library)
            "png": {
                "users": Users,
                "internet_gateway": Internet,
                "api_gateway": APIGateway,
                "fargate": Fargate,
                "rds": RDS,
                "elastic_load_balancing": ELB,
                "cognito": Cognito,
                "waf": WAF
            },
            # DrawIO (mxgraph shapes)
            "drawio": {
                "users": "mxgraph.aws4.users",
                "internet_gateway": "mxgraph.aws4.internet_gateway",
                "api_gateway": "mxgraph.aws4.api_gateway",
                "fargate": "mxgraph.aws4.fargate",
                "rds": "mxgraph.aws4.rds",
                "elastic_load_balancing": "mxgraph.aws4.elastic_load_balancing",
                "cognito": "mxgraph.aws4.cognito",
                "waf": "mxgraph.aws4.waf"
            }
        }
    
    def generate(self, schema: UniversalDiagramSchema) -> Dict[str, str]:
        """Genera diagramas según esquema universal"""
        
        results = {}
        
        if schema.output_format in [OutputFormat.PNG, OutputFormat.BOTH]:
            png_path = self._generate_png(schema)
            results["png"] = png_path
        
        if schema.output_format in [OutputFormat.DRAWIO, OutputFormat.BOTH]:
            drawio_path = self._generate_drawio(schema)
            results["drawio"] = drawio_path
        
        return results
    
    def _generate_png(self, schema: UniversalDiagramSchema) -> str:
        """Genera PNG usando diagrams library"""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{schema.project_name}_{schema.diagram_type.value}_{timestamp}"
        
        graph_attr = {
            "fontsize": "45",
            "bgcolor": "white"
        }
        
        with Diagram(schema.title, filename=str(self.output_dir / "png" / filename), 
                    show=False, graph_attr=graph_attr):
            
            # Crear componentes PNG
            png_components = {}
            
            # Componentes externos
            for component in schema.components:
                if component.type in self.component_mapping["png"]:
                    ComponentClass = self.component_mapping["png"][component.type]
                    png_components[component.id] = ComponentClass(component.label)
            
            # Contenedores con componentes
            for container in schema.containers:
                with Cluster(container.label):
                    for component in container.components:
                        if component.type in self.component_mapping["png"]:
                            ComponentClass = self.component_mapping["png"][component.type]
                            png_components[component.id] = ComponentClass(component.label)
                    
                    # Contenedores anidados
                    for child_container in container.children:
                        with Cluster(child_container.label):
                            for component in child_container.components:
                                if component.type in self.component_mapping["png"]:
                                    ComponentClass = self.component_mapping["png"][component.type]
                                    png_components[component.id] = ComponentClass(component.label)
            
            # Crear conexiones
            for connection in schema.connections:
                if connection.from_id in png_components and connection.to_id in png_components:
                    from_comp = png_components[connection.from_id]
                    to_comp = png_components[connection.to_id]
                    
                    # Estilo de conexión
                    edge_style = {}
                    if connection.style:
                        edge_style["color"] = connection.style.color
                    
                    from_comp >> Edge(**edge_style) >> to_comp
        
        return str(self.output_dir / "png" / f"{filename}.png")
    
    def _generate_drawio(self, schema: UniversalDiagramSchema) -> str:
        """Genera DrawIO XML desde esquema"""
        
        # Crear XML DrawIO
        mxfile = ET.Element("mxfile", host="app.diagrams.net")
        diagram = ET.SubElement(mxfile, "diagram", name=schema.title, id="universal")
        model = ET.SubElement(diagram, "mxGraphModel", 
                             dx=str(schema.canvas.width), 
                             dy=str(schema.canvas.height), 
                             grid="1", gridSize=str(schema.canvas.grid))
        root = ET.SubElement(model, "root")
        
        # Celdas base
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        
        cell_id = 2
        component_ids = {}
        
        # Título
        title = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value=schema.title,
            style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;fontColor=#FFFFFF;fontSize=18;fontStyle=1;",
            vertex="1", parent="1"
        )
        ET.SubElement(title, "mxGeometry", x="50", y="20", width="2000", height="50", **{"as": "geometry"})
        cell_id += 1
        
        # Componentes externos
        for component in schema.components:
            comp_id = self._create_drawio_component(root, component, cell_id, "1")
            component_ids[component.id] = comp_id
            cell_id += 1
        
        # Contenedores
        for container in schema.containers:
            container_id = self._create_drawio_container(root, container, cell_id, "1")
            cell_id += 1
            
            # Componentes del contenedor
            for component in container.components:
                comp_id = self._create_drawio_component(root, component, cell_id, str(container_id))
                component_ids[component.id] = comp_id
                cell_id += 1
            
            # Contenedores anidados
            for child_container in container.children:
                child_id = self._create_drawio_container(root, child_container, cell_id, str(container_id))
                cell_id += 1
                
                for component in child_container.components:
                    comp_id = self._create_drawio_component(root, component, cell_id, str(child_id))
                    component_ids[component.id] = comp_id
                    cell_id += 1
        
        # Conexiones
        for connection in schema.connections:
            if connection.from_id in component_ids and connection.to_id in component_ids:
                self._create_drawio_connection(root, connection, component_ids, cell_id)
                cell_id += 1
        
        # Guardar archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{schema.project_name}_{schema.diagram_type.value}_{timestamp}.drawio"
        output_path = self.output_dir / "drawio" / filename
        
        ET.indent(mxfile, space="  ")
        xml_str = ET.tostring(mxfile, encoding='unicode', xml_declaration=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_str)
        
        return str(output_path)
    
    def _create_drawio_component(self, root, component, cell_id: int, parent_id: str) -> int:
        """Crea componente DrawIO"""
        
        drawio_shape = self.component_mapping["drawio"].get(component.type, "rounded=1;whiteSpace=wrap;html=1;")
        style = self._get_drawio_style(drawio_shape)
        
        comp = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value=component.label,
            style=style,
            vertex="1", parent=parent_id
        )
        
        # Posición y tamaño
        pos = component.position or Position(100, 100)
        size = component.size or Size(100, 100)
        
        ET.SubElement(comp, "mxGeometry", 
                     x=str(pos.x), y=str(pos.y), 
                     width=str(size.width), height=str(size.height), 
                     **{"as": "geometry"})
        
        return cell_id
    
    def _create_drawio_container(self, root, container, cell_id: int, parent_id: str) -> int:
        """Crea contenedor DrawIO"""
        
        style = container.style
        container_style = f"fillColor={style.fill_color};strokeColor={style.stroke_color};dashed=1;verticalAlign=top;fontStyle=1;fontColor={style.stroke_color};whiteSpace=wrap;html=1;fontSize=12;" if style else "fillColor=#E3F2FD;strokeColor=#1976D2;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#1976D2;whiteSpace=wrap;html=1;fontSize=12;"
        
        cont = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value=container.label,
            style=container_style,
            vertex="1", parent=parent_id
        )
        
        ET.SubElement(cont, "mxGeometry", 
                     x=str(container.position.x), y=str(container.position.y), 
                     width=str(container.size.width), height=str(container.size.height), 
                     **{"as": "geometry"})
        
        return cell_id
    
    def _create_drawio_connection(self, root, connection, component_ids: Dict[str, int], cell_id: int):
        """Crea conexión DrawIO"""
        
        from_id = component_ids[connection.from_id]
        to_id = component_ids[connection.to_id]
        
        style = connection.style
        edge_style = f"endArrow=classic;html=1;rounded=0;strokeColor={style.color};strokeWidth={style.width};" if style else "endArrow=classic;html=1;rounded=0;strokeColor=#232F3E;strokeWidth=2;"
        
        edge = ET.SubElement(root, "mxCell",
            id=str(cell_id),
            value=connection.label,
            style=edge_style,
            edge="1", parent="1", 
            source=str(from_id), target=str(to_id)
        )
        ET.SubElement(edge, "mxGeometry", width="50", height="50", relative="1", **{"as": "geometry"})
    
    def _get_drawio_style(self, shape: str) -> str:
        """Obtiene estilo DrawIO para shape"""
        
        if shape.startswith("mxgraph.aws4"):
            return f"sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape={shape};"
        else:
            return "rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;"
