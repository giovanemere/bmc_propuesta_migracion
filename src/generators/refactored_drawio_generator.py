#!/usr/bin/env python3
"""
Refactored DrawIO Generator - Arquitectura separada datos/lógica
"""

from pathlib import Path
from datetime import datetime
from typing import Dict, Any
import sys
sys.path.append('/home/giovanemere/Migracion/src')

from models.diagram_model import DiagramModel, DiagramModelBuilder, Component, Connection
from layouts.diagram_layouts import LayoutEngine
from validators.diagram_validator import DiagramValidator, XMLValidator, DiagramsNetAPI

class RefactoredDrawIOGenerator:
    """Generador DrawIO refactorizado con separación datos/lógica"""
    
    def __init__(self, output_dir: str = "outputs"):
        self.output_dir = Path(output_dir)
        self.xml_renderer = XMLRenderer()
    
    def generate_from_config(self, config: Dict[str, Any], project_name: str = "bmc_input") -> str:
        """Genera DrawIO desde configuración usando modelo de datos"""
        
        # 1. Crear modelo desde configuración
        model = DiagramModelBuilder.from_config(config)
        
        # 2. Aplicar layout automático
        LayoutEngine.apply_layout(model)
        
        # 3. Validar modelo
        is_valid, errors = DiagramValidator.validate_model(model)
        if not is_valid:
            print(f"⚠️ Errores en modelo: {errors}")
        
        # 4. Generar XML
        xml_content = self.xml_renderer.render_model(model)
        
        # 5. Validar XML
        xml_valid, xml_errors = XMLValidator.validate_xml(xml_content)
        if not xml_valid:
            print(f"⚠️ Errores en XML: {xml_errors}")
        
        # 6. Validación online (opcional)
        online_valid, online_msg = DiagramsNetAPI.validate_online(xml_content)
        if online_valid:
            print("✅ Validación online exitosa")
        else:
            print(f"⚠️ Validación online: {online_msg}")
        
        # 7. Guardar archivo
        output_path = self._save_file(xml_content, project_name)
        
        return output_path
    
    def _save_file(self, xml_content: str, project_name: str) -> str:
        """Guarda archivo DrawIO"""
        
        output_dir = self.output_dir / "drawio" / project_name
        output_dir.mkdir(parents=True, exist_ok=True)
        
        filename = f"refactored_architecture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.drawio"
        file_path = output_dir / filename
        
        file_path.write_text(xml_content, encoding='utf-8')
        
        print(f"✅ Refactored DrawIO generado: {file_path}")
        return str(file_path)

class XMLRenderer:
    """Renderizador de XML DrawIO desde modelo"""
    
    def __init__(self):
        self.id_counter = 1000
    
    def render_model(self, model: DiagramModel) -> str:
        """Renderiza modelo completo a XML"""
        
        xml_parts = []
        
        # Header
        xml_parts.append(self._render_header(model))
        
        # Componentes
        for component in model.components:
            xml_parts.append(self._render_component(component))
        
        # Conexiones
        for connection in model.connections:
            xml_parts.append(self._render_connection(connection))
        
        # Footer
        xml_parts.append(self._render_footer())
        
        return ''.join(xml_parts)
    
    def _render_header(self, model: DiagramModel) -> str:
        """Renderiza header XML"""
        
        canvas_width, canvas_height = model.canvas_size
        
        return f'''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="{datetime.now().isoformat()}" version="22.1.11">
  <diagram name="{model.name}" id="refactored_diagram">
    <mxGraphModel dx="2500" dy="1600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{canvas_width}" pageHeight="{canvas_height}">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>'''
    
    def _render_component(self, component: Component) -> str:
        """Renderiza componente individual"""
        
        # Escapar caracteres XML
        escaped_label = self._escape_xml(component.label or component.name)
        
        # Construir estilo
        style_parts = [
            f"fillColor={component.style.fill_color}",
            f"strokeColor={component.style.stroke_color}",
            f"fontColor={component.style.font_color}",
            f"fontSize={component.style.font_size}"
        ]
        
        if component.shape:
            style_parts.insert(0, f"shape={component.shape}")
            style_parts.extend([
                "labelPosition=bottom",
                "verticalLabelPosition=top",
                "align=center",
                "verticalAlign=bottom"
            ])
        
        style = ";".join(style_parts) + ";"
        
        return f'''
        <mxCell id="{component.id}" value="{escaped_label}" style="{style}" vertex="1" parent="1">
          <mxGeometry x="{component.position.x}" y="{component.position.y}" width="{component.position.width}" height="{component.position.height}" as="geometry"/>
        </mxCell>'''
    
    def _render_connection(self, connection: Connection) -> str:
        """Renderiza conexión individual"""
        
        escaped_label = self._escape_xml(connection.label)
        
        # Estilo de conexión
        style_parts = [
            "edgeStyle=orthogonalEdgeStyle",
            "rounded=0",
            "orthogonalLoop=1",
            "jettySize=auto",
            "html=1",
            f"strokeColor={connection.style.stroke_color}",
            f"strokeWidth={connection.style.stroke_width}",
            f"fontColor={connection.style.font_color}"
        ]
        
        style = ";".join(style_parts) + ";"
        
        label_id = f"label_{self._next_id()}"
        
        return f'''
        <mxCell id="{connection.id}" style="{style}" edge="1" parent="1" source="{connection.source}" target="{connection.target}">
          <mxGeometry relative="1" as="geometry">
            <Array as="points"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="{label_id}" value="{escaped_label}" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize={connection.style.font_size};fontColor={connection.style.font_color};" vertex="1" connectable="0" parent="{connection.id}">
          <mxGeometry x="-0.1" y="1" relative="1" as="geometry">
            <mxPoint as="offset"/>
          </mxGeometry>
        </mxCell>'''
    
    def _render_footer(self) -> str:
        """Renderiza footer XML"""
        
        return '''
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    def _escape_xml(self, text: str) -> str:
        """Escapa caracteres XML"""
        if not text:
            return ""
        
        return (text.replace('&', '&amp;')
                   .replace('<', '&lt;')
                   .replace('>', '&gt;')
                   .replace('"', '&quot;')
                   .replace("'", '&apos;'))
    
    def _next_id(self) -> int:
        """Genera ID único"""
        self.id_counter += 1
        return self.id_counter

# Template system
class DiagramTemplate:
    """Sistema de plantillas para diagramas"""
    
    @staticmethod
    def create_network_template() -> DiagramModel:
        """Crea plantilla de diagrama de red"""
        
        from models.diagram_model import DiagramModel, Component, ComponentType, Position, Style, Connection
        
        model = DiagramModel("Network Architecture Template")
        
        # Componentes de plantilla
        components = [
            Component(
                id="cloudfront",
                name="CloudFront",
                component_type=ComponentType.AWS_SERVICE,
                position=Position(100, 100),
                style=Style(fill_color="#E3F2FD", stroke_color="#1976D2"),
                shape="mxgraph.aws4.cloudfront",
                label="CloudFront CDN\\nGlobal Distribution"
            ),
            Component(
                id="api_gateway",
                name="API Gateway",
                component_type=ComponentType.AWS_SERVICE,
                position=Position(300, 100),
                style=Style(fill_color="#E8F5E8", stroke_color="#4CAF50"),
                shape="mxgraph.aws4.api_gateway",
                label="API Gateway\\nRESTful APIs"
            )
        ]
        
        for component in components:
            model.add_component(component)
        
        # Conexión de plantilla
        connection = Connection(
            id="conn_cf_api",
            source="cloudfront",
            target="api_gateway",
            label="HTTPS Traffic",
            style=Style(stroke_color="#1976D2", font_color="#1976D2")
        )
        model.add_connection(connection)
        
        return model
    
    @staticmethod
    def create_microservices_template() -> DiagramModel:
        """Crea plantilla de microservicios"""
        
        # Implementación similar para microservicios
        model = DiagramModel("Microservices Template")
        # ... agregar componentes y conexiones
        return model
