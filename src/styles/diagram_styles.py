#!/usr/bin/env python3
"""
Diagram Styles - Estilos y colores consistentes por tipo
"""

from dataclasses import dataclass
from typing import Dict, List
from enum import Enum

class ComponentCategory(Enum):
    SECURITY = "security"
    DATA = "data"
    NETWORK = "network"
    COMPUTE = "compute"
    INTEGRATION = "integration"
    MONITORING = "monitoring"

@dataclass
class StyleTheme:
    fill_color: str
    stroke_color: str
    font_color: str
    stroke_width: int = 2
    font_size: int = 12

class StyleManager:
    """Gestor de estilos consistentes"""
    
    # Paleta de colores por categoría
    CATEGORY_STYLES = {
        ComponentCategory.SECURITY: StyleTheme(
            fill_color="#FFEBEE",
            stroke_color="#D32F2F", 
            font_color="#B71C1C"
        ),
        ComponentCategory.DATA: StyleTheme(
            fill_color="#E8F5E8",
            stroke_color="#4CAF50",
            font_color="#2E7D32"
        ),
        ComponentCategory.NETWORK: StyleTheme(
            fill_color="#E3F2FD",
            stroke_color="#1976D2",
            font_color="#0D47A1"
        ),
        ComponentCategory.COMPUTE: StyleTheme(
            fill_color="#FFF3E0",
            stroke_color="#FF9800",
            font_color="#E65100"
        ),
        ComponentCategory.INTEGRATION: StyleTheme(
            fill_color="#F3E5F5",
            stroke_color="#9C27B0",
            font_color="#4A148C"
        ),
        ComponentCategory.MONITORING: StyleTheme(
            fill_color="#FFF8E1",
            stroke_color="#FFC107",
            font_color="#FF8F00"
        )
    }
    
    # Mapeo de servicios AWS a categorías
    SERVICE_CATEGORIES = {
        # Security
        "waf": ComponentCategory.SECURITY,
        "cognito": ComponentCategory.SECURITY,
        "kms": ComponentCategory.SECURITY,
        "secrets_manager": ComponentCategory.SECURITY,
        "shield": ComponentCategory.SECURITY,
        
        # Data
        "rds": ComponentCategory.DATA,
        "dynamodb": ComponentCategory.DATA,
        "elasticache": ComponentCategory.DATA,
        "redis": ComponentCategory.DATA,
        "s3": ComponentCategory.DATA,
        
        # Network
        "cloudfront": ComponentCategory.NETWORK,
        "api_gateway": ComponentCategory.NETWORK,
        "elb": ComponentCategory.NETWORK,
        "vpc": ComponentCategory.NETWORK,
        "route53": ComponentCategory.NETWORK,
        
        # Compute
        "fargate": ComponentCategory.COMPUTE,
        "lambda": ComponentCategory.COMPUTE,
        "ec2": ComponentCategory.COMPUTE,
        "ecs": ComponentCategory.COMPUTE,
        
        # Integration
        "sqs": ComponentCategory.INTEGRATION,
        "sns": ComponentCategory.INTEGRATION,
        "eventbridge": ComponentCategory.INTEGRATION,
        "step_functions": ComponentCategory.INTEGRATION,
        
        # Monitoring
        "cloudwatch": ComponentCategory.MONITORING,
        "xray": ComponentCategory.MONITORING,
        "cloudtrail": ComponentCategory.MONITORING
    }
    
    @staticmethod
    def get_style_for_service(service_name: str) -> StyleTheme:
        """Obtiene estilo basado en nombre de servicio"""
        
        # Buscar categoría por nombre
        for service_key, category in StyleManager.SERVICE_CATEGORIES.items():
            if service_key in service_name.lower():
                return StyleManager.CATEGORY_STYLES[category]
        
        # Estilo por defecto
        return StyleTheme(
            fill_color="#F5F5F5",
            stroke_color="#666666",
            font_color="#333333"
        )
    
    @staticmethod
    def get_connection_style(connection_type: str) -> StyleTheme:
        """Obtiene estilo para conexiones por tipo"""
        
        connection_styles = {
            "data": StyleTheme("", "#2196F3", "#2196F3", 2),
            "security": StyleTheme("", "#D32F2F", "#D32F2F", 3),
            "api": StyleTheme("", "#4CAF50", "#4CAF50", 2),
            "cache": StyleTheme("", "#FF9800", "#FF9800", 2),
            "monitoring": StyleTheme("", "#9C27B0", "#9C27B0", 1),
            "default": StyleTheme("", "#666666", "#666666", 2)
        }
        
        return connection_styles.get(connection_type, connection_styles["default"])

class LegendGenerator:
    """Generador de leyendas para diagramas"""
    
    @staticmethod
    def create_legend_components() -> List[Dict]:
        """Crea componentes de leyenda"""
        
        legend_components = []
        
        # Título de leyenda
        legend_components.append({
            "id": "legend_title",
            "type": "text",
            "label": "LEYENDA - CATEGORÍAS DE COMPONENTES",
            "position": {"x": 50, "y": 50},
            "style": {
                "fontSize": 16,
                "fontStyle": "bold",
                "fontColor": "#333333"
            }
        })
        
        # Elementos de leyenda por categoría
        y_offset = 100
        for i, (category, style) in enumerate(StyleManager.CATEGORY_STYLES.items()):
            
            # Icono de ejemplo
            legend_components.append({
                "id": f"legend_icon_{category.value}",
                "type": "rectangle",
                "label": "",
                "position": {"x": 70, "y": y_offset + (i * 40), "width": 30, "height": 20},
                "style": {
                    "fillColor": style.fill_color,
                    "strokeColor": style.stroke_color,
                    "strokeWidth": style.stroke_width
                }
            })
            
            # Texto explicativo
            legend_components.append({
                "id": f"legend_text_{category.value}",
                "type": "text",
                "label": f"{category.value.title()}: {LegendGenerator._get_category_description(category)}",
                "position": {"x": 120, "y": y_offset + (i * 40)},
                "style": {
                    "fontSize": 12,
                    "fontColor": style.font_color
                }
            })
        
        return legend_components
    
    @staticmethod
    def _get_category_description(category: ComponentCategory) -> str:
        """Obtiene descripción de categoría"""
        
        descriptions = {
            ComponentCategory.SECURITY: "Servicios de seguridad y autenticación",
            ComponentCategory.DATA: "Bases de datos y almacenamiento",
            ComponentCategory.NETWORK: "Servicios de red y distribución",
            ComponentCategory.COMPUTE: "Servicios de cómputo y procesamiento",
            ComponentCategory.INTEGRATION: "Servicios de integración y mensajería",
            ComponentCategory.MONITORING: "Monitoreo y observabilidad"
        }
        
        return descriptions.get(category, "Otros servicios")

class AnnotationManager:
    """Gestor de anotaciones y notas explicativas"""
    
    @staticmethod
    def create_architecture_notes() -> List[Dict]:
        """Crea notas explicativas para arquitectura"""
        
        notes = []
        
        # Nota principal
        notes.append({
            "id": "main_note",
            "type": "note",
            "title": "Arquitectura BMC - Migración GCP → AWS",
            "content": [
                "• 5 microservicios en ECS Fargate",
                "• Base de datos PostgreSQL Multi-AZ", 
                "• Cache Redis para alta performance",
                "• CDN CloudFront para distribución global",
                "• Seguridad WAF + Cognito integrada"
            ],
            "position": {"x": 1100, "y": 100},
            "style": {
                "fillColor": "#FFF9C4",
                "strokeColor": "#F57F17",
                "fontColor": "#333333"
            }
        })
        
        # Notas de performance
        notes.append({
            "id": "performance_note",
            "type": "note", 
            "title": "Métricas de Performance",
            "content": [
                "• API Gateway: 10K req/s throttle",
                "• Product Service: <500ms lookup",
                "• OCR Service: >95% accuracy",
                "• RDS: 35-day backup retention",
                "• Redis: 99.9% availability"
            ],
            "position": {"x": 1100, "y": 300},
            "style": {
                "fillColor": "#E8F5E8",
                "strokeColor": "#4CAF50",
                "fontColor": "#2E7D32"
            }
        })
        
        # Notas de seguridad
        notes.append({
            "id": "security_note",
            "type": "note",
            "title": "Características de Seguridad", 
            "content": [
                "• WAF con protección DDoS",
                "• Cognito MFA habilitado",
                "• KMS encryption at rest",
                "• VPC con subnets privadas",
                "• CloudTrail audit completo"
            ],
            "position": {"x": 1100, "y": 500},
            "style": {
                "fillColor": "#FFEBEE",
                "strokeColor": "#D32F2F",
                "fontColor": "#B71C1C"
            }
        })
        
        return notes
    
    @staticmethod
    def create_migration_timeline() -> Dict:
        """Crea timeline de migración"""
        
        return {
            "id": "migration_timeline",
            "type": "timeline",
            "title": "Timeline de Migración (12 semanas)",
            "phases": [
                {"week": "1-2", "task": "Setup AWS + VPC", "status": "completed"},
                {"week": "3-4", "task": "Migrar Product Service", "status": "in_progress"},
                {"week": "5-6", "task": "Migrar Invoice Service", "status": "pending"},
                {"week": "7-8", "task": "Migrar OCR Service", "status": "pending"},
                {"week": "9-10", "task": "Testing + Optimización", "status": "pending"},
                {"week": "11-12", "task": "Go-live + Monitoreo", "status": "pending"}
            ],
            "position": {"x": 50, "y": 850},
            "style": {
                "fillColor": "#F3E5F5",
                "strokeColor": "#9C27B0",
                "fontColor": "#4A148C"
            }
        }
