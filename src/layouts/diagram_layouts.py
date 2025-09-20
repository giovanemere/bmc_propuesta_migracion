#!/usr/bin/env python3
"""
Diagram Layouts - Sistema de layouts automáticos
"""

from typing import List, Tuple, Dict
from models.diagram_model import DiagramModel, Component, Position, LayoutType
import math

class LayoutEngine:
    """Motor de layouts para diagramas"""
    
    @staticmethod
    def apply_layout(model: DiagramModel) -> None:
        """Aplica layout según el tipo especificado"""
        
        if model.layout == LayoutType.HIERARCHICAL:
            HierarchicalLayout.apply(model)
        elif model.layout == LayoutType.GRID:
            GridLayout.apply(model)
        elif model.layout == LayoutType.CIRCULAR:
            CircularLayout.apply(model)
        elif model.layout == LayoutType.FORCE_DIRECTED:
            ForceDirectedLayout.apply(model)

class HierarchicalLayout:
    """Layout jerárquico por capas"""
    
    @staticmethod
    def apply(model: DiagramModel) -> None:
        """Aplica layout jerárquico"""
        
        # Agrupar componentes por tipo
        layers = HierarchicalLayout._group_by_layers(model.components)
        
        # Posicionar por capas
        y_start = 100
        layer_height = 200
        
        for i, (layer_name, components) in enumerate(layers.items()):
            y_pos = y_start + (i * layer_height)
            HierarchicalLayout._position_layer(components, y_pos, model.canvas_size[0])

    @staticmethod
    def _group_by_layers(components: List[Component]) -> Dict[str, List[Component]]:
        """Agrupa componentes en capas lógicas"""
        
        layers = {
            "edge": [],
            "api": [],
            "microservices": [],
            "data": []
        }
        
        for component in components:
            if any(keyword in component.name.lower() for keyword in ["cloudfront", "waf"]):
                layers["edge"].append(component)
            elif any(keyword in component.name.lower() for keyword in ["api", "gateway"]):
                layers["api"].append(component)
            elif component.id.startswith("ms_"):
                layers["microservices"].append(component)
            elif any(keyword in component.name.lower() for keyword in ["rds", "redis", "s3"]):
                layers["data"].append(component)
        
        return {k: v for k, v in layers.items() if v}  # Solo capas no vacías
    
    @staticmethod
    def _position_layer(components: List[Component], y_pos: int, canvas_width: int) -> None:
        """Posiciona componentes en una capa horizontal"""
        
        if not components:
            return
        
        # Calcular espaciado
        component_width = 120
        spacing = max(50, (canvas_width - len(components) * component_width) // (len(components) + 1))
        
        for i, component in enumerate(components):
            x_pos = spacing + (i * (component_width + spacing))
            component.position = Position(x_pos, y_pos, component_width, 80)

class GridLayout:
    """Layout en grilla regular"""
    
    @staticmethod
    def apply(model: DiagramModel) -> None:
        """Aplica layout en grilla"""
        
        components = [c for c in model.components if c.component_type.value != "title"]
        
        # Calcular dimensiones de grilla
        cols = math.ceil(math.sqrt(len(components)))
        rows = math.ceil(len(components) / cols)
        
        # Espaciado
        cell_width = model.canvas_size[0] // cols
        cell_height = model.canvas_size[1] // rows
        
        for i, component in enumerate(components):
            row = i // cols
            col = i % cols
            
            x = col * cell_width + cell_width // 2 - 60
            y = row * cell_height + cell_height // 2 - 40
            
            component.position = Position(x, y)

class CircularLayout:
    """Layout circular"""
    
    @staticmethod
    def apply(model: DiagramModel) -> None:
        """Aplica layout circular"""
        
        components = [c for c in model.components if c.component_type.value != "title"]
        
        if not components:
            return
        
        # Centro del círculo
        center_x = model.canvas_size[0] // 2
        center_y = model.canvas_size[1] // 2
        radius = min(center_x, center_y) - 100
        
        # Ángulo entre componentes
        angle_step = 2 * math.pi / len(components)
        
        for i, component in enumerate(components):
            angle = i * angle_step
            x = center_x + radius * math.cos(angle) - 60
            y = center_y + radius * math.sin(angle) - 40
            
            component.position = Position(int(x), int(y))

class ForceDirectedLayout:
    """Layout dirigido por fuerzas (simplificado)"""
    
    @staticmethod
    def apply(model: DiagramModel) -> None:
        """Aplica layout dirigido por fuerzas"""
        
        # Implementación simplificada - usar grid como base
        GridLayout.apply(model)
        
        # Ajustar posiciones basado en conexiones
        ForceDirectedLayout._adjust_connected_components(model)
    
    @staticmethod
    def _adjust_connected_components(model: DiagramModel) -> None:
        """Ajusta posiciones de componentes conectados"""
        
        for connection in model.connections:
            source = model.get_component_by_id(connection.source)
            target = model.get_component_by_id(connection.target)
            
            if source and target:
                # Acercar componentes conectados
                dx = target.position.x - source.position.x
                dy = target.position.y - source.position.y
                
                # Reducir distancia en 20%
                adjustment = 0.2
                source.position.x += int(dx * adjustment)
                source.position.y += int(dy * adjustment)
                target.position.x -= int(dx * adjustment)
                target.position.y -= int(dy * adjustment)
