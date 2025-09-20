#!/usr/bin/env python3
"""
Diagram Validator - Validación de modelos y XML
"""

import xml.etree.ElementTree as ET
from typing import List, Dict, Tuple
from models.diagram_model import DiagramModel
import requests
import json

class DiagramValidator:
    """Validador de diagramas y XML"""
    
    @staticmethod
    def validate_model(model: DiagramModel) -> Tuple[bool, List[str]]:
        """Valida modelo de diagrama"""
        
        errors = []
        
        # Validaciones básicas del modelo
        errors.extend(model.validate())
        
        # Validaciones adicionales
        errors.extend(DiagramValidator._validate_positions(model))
        errors.extend(DiagramValidator._validate_styles(model))
        errors.extend(DiagramValidator._validate_connections(model))
        
        return len(errors) == 0, errors
    
    @staticmethod
    def _validate_positions(model: DiagramModel) -> List[str]:
        """Valida posiciones de componentes"""
        
        errors = []
        canvas_width, canvas_height = model.canvas_size
        
        for component in model.components:
            pos = component.position
            
            # Verificar que esté dentro del canvas
            if pos.x < 0 or pos.y < 0:
                errors.append(f"Componente {component.id}: posición negativa")
            
            if pos.x + pos.width > canvas_width:
                errors.append(f"Componente {component.id}: fuera del canvas (X)")
            
            if pos.y + pos.height > canvas_height:
                errors.append(f"Componente {component.id}: fuera del canvas (Y)")
        
        return errors
    
    @staticmethod
    def _validate_styles(model: DiagramModel) -> List[str]:
        """Valida estilos de componentes"""
        
        errors = []
        
        for component in model.components:
            style = component.style
            
            # Validar colores (formato hex)
            colors = [style.fill_color, style.stroke_color, style.font_color]
            for color in colors:
                if not color.startswith('#') or len(color) != 7:
                    errors.append(f"Componente {component.id}: color inválido {color}")
        
        return errors
    
    @staticmethod
    def _validate_connections(model: DiagramModel) -> List[str]:
        """Valida conexiones entre componentes"""
        
        errors = []
        
        for connection in model.connections:
            # Verificar que source y target existan
            if not model.get_component_by_id(connection.source):
                errors.append(f"Conexión {connection.id}: source {connection.source} no existe")
            
            if not model.get_component_by_id(connection.target):
                errors.append(f"Conexión {connection.id}: target {connection.target} no existe")
            
            # Verificar que no sea auto-conexión
            if connection.source == connection.target:
                errors.append(f"Conexión {connection.id}: auto-conexión no permitida")
        
        return errors

class XMLValidator:
    """Validador de XML DrawIO"""
    
    @staticmethod
    def validate_xml(xml_content: str) -> Tuple[bool, List[str]]:
        """Valida XML DrawIO"""
        
        errors = []
        
        try:
            # Parsear XML
            root = ET.fromstring(xml_content)
            
            # Validar estructura básica
            if root.tag != 'mxfile':
                errors.append("Root element debe ser 'mxfile'")
            
            # Validar diagramas
            diagrams = root.findall('diagram')
            if not diagrams:
                errors.append("No se encontraron diagramas")
            
            for diagram in diagrams:
                errors.extend(XMLValidator._validate_diagram(diagram))
        
        except ET.ParseError as e:
            errors.append(f"Error de parsing XML: {e}")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def _validate_diagram(diagram_element) -> List[str]:
        """Valida elemento diagram"""
        
        errors = []
        
        # Verificar que tenga mxGraphModel
        model = diagram_element.find('mxGraphModel')
        if model is None:
            errors.append("Diagrama sin mxGraphModel")
            return errors
        
        # Verificar root
        root = model.find('root')
        if root is None:
            errors.append("mxGraphModel sin root")
            return errors
        
        # Verificar celdas básicas (0 y 1)
        cells = root.findall('mxCell')
        if len(cells) < 2:
            errors.append("Faltan celdas básicas (0 y 1)")
        
        # Validar IDs únicos
        ids = [cell.get('id') for cell in cells if cell.get('id')]
        if len(ids) != len(set(ids)):
            errors.append("IDs duplicados en celdas")
        
        return errors

class DiagramsNetAPI:
    """Integración con API de diagrams.net"""
    
    BASE_URL = "https://app.diagrams.net"
    
    @staticmethod
    def validate_online(xml_content: str) -> Tuple[bool, str]:
        """Valida XML usando API de diagrams.net"""
        
        try:
            # Simular validación (diagrams.net no tiene API pública de validación)
            # En implementación real, usaríamos su API o biblioteca
            
            # Validación local como fallback
            is_valid, errors = XMLValidator.validate_xml(xml_content)
            
            if is_valid:
                return True, "XML válido"
            else:
                return False, "; ".join(errors)
        
        except Exception as e:
            return False, f"Error en validación: {e}"
    
    @staticmethod
    def render_preview(xml_content: str) -> str:
        """Genera preview del diagrama"""
        
        # En implementación real, usaríamos API de diagrams.net
        # Por ahora, retornamos URL de ejemplo
        
        return f"{DiagramsNetAPI.BASE_URL}/#G{hash(xml_content) % 1000000}"

# Tests unitarios
class DiagramTests:
    """Tests para validación de diagramas"""
    
    @staticmethod
    def run_all_tests() -> Dict[str, bool]:
        """Ejecuta todos los tests"""
        
        results = {}
        
        results["test_model_validation"] = DiagramTests.test_model_validation()
        results["test_xml_validation"] = DiagramTests.test_xml_validation()
        results["test_position_validation"] = DiagramTests.test_position_validation()
        
        return results
    
    @staticmethod
    def test_model_validation() -> bool:
        """Test de validación de modelo"""
        
        try:
            from models.diagram_model import DiagramModel, Component, ComponentType, Position, Style
            
            # Crear modelo de prueba
            model = DiagramModel("Test")
            
            # Agregar componente válido
            component = Component(
                id="test_1",
                name="Test Component",
                component_type=ComponentType.AWS_SERVICE,
                position=Position(100, 100),
                style=Style()
            )
            model.add_component(component)
            
            # Validar
            is_valid, errors = DiagramValidator.validate_model(model)
            
            return is_valid and len(errors) == 0
        
        except Exception:
            return False
    
    @staticmethod
    def test_xml_validation() -> bool:
        """Test de validación XML"""
        
        try:
            # XML válido mínimo
            xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile>
  <diagram name="Test">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
            
            is_valid, errors = XMLValidator.validate_xml(xml_content)
            
            return is_valid
        
        except Exception:
            return False
    
    @staticmethod
    def test_position_validation() -> bool:
        """Test de validación de posiciones"""
        
        try:
            from models.diagram_model import DiagramModel, Component, ComponentType, Position, Style
            
            model = DiagramModel("Test", canvas_size=(800, 600))
            
            # Componente fuera del canvas
            component = Component(
                id="test_1",
                name="Test",
                component_type=ComponentType.AWS_SERVICE,
                position=Position(900, 100),  # Fuera del canvas
                style=Style()
            )
            model.add_component(component)
            
            is_valid, errors = DiagramValidator.validate_model(model)
            
            # Debe fallar la validación
            return not is_valid and len(errors) > 0
        
        except Exception:
            return False
