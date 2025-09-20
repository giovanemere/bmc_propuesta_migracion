#!/usr/bin/env python3
"""
Draw.io API Client - Integración con diagrams.net API
"""

import requests
import json
import base64
from pathlib import Path
from typing import Dict, Any, Optional

class DrawIOAPIClient:
    """Cliente para API de diagrams.net"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.base_url = "https://app.diagrams.net"
        self.api_key = api_key
        self.session = requests.Session()
        
        if api_key:
            self.session.headers.update({"Authorization": f"Bearer {api_key}"})
    
    def create_diagram_from_xml(self, xml_content: str, title: str = "BMC Architecture") -> Dict[str, Any]:
        """Crea diagrama en Draw.io desde XML"""
        
        try:
            # Codificar XML en base64
            xml_b64 = base64.b64encode(xml_content.encode('utf-8')).decode('utf-8')
            
            # Crear URL de Draw.io con XML embebido
            drawio_url = f"{self.base_url}/#G{xml_b64}"
            
            return {
                "success": True,
                "url": drawio_url,
                "title": title,
                "message": "Diagrama creado exitosamente"
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Error al crear diagrama"
            }
    
    def upload_diagram(self, xml_content: str, filename: str) -> Dict[str, Any]:
        """Sube diagrama a Draw.io (requiere API key)"""
        
        if not self.api_key:
            return {
                "success": False,
                "error": "API key requerida",
                "message": "Configurar API key para subir diagramas"
            }
        
        try:
            # Endpoint para subir diagrama
            upload_url = f"{self.base_url}/api/v1/diagrams"
            
            payload = {
                "title": filename,
                "content": xml_content,
                "format": "xml"
            }
            
            response = self.session.post(upload_url, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                return {
                    "success": True,
                    "diagram_id": result.get("id"),
                    "edit_url": result.get("edit_url"),
                    "view_url": result.get("view_url"),
                    "message": "Diagrama subido exitosamente"
                }
            else:
                return {
                    "success": False,
                    "error": f"HTTP {response.status_code}",
                    "message": "Error al subir diagrama"
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Error de conexión con API"
            }
    
    def share_diagram(self, diagram_id: str, permissions: str = "view") -> Dict[str, Any]:
        """Comparte diagrama (requiere API key)"""
        
        if not self.api_key:
            return {
                "success": False,
                "error": "API key requerida"
            }
        
        try:
            share_url = f"{self.base_url}/api/v1/diagrams/{diagram_id}/share"
            
            payload = {
                "permissions": permissions,  # "view", "edit", "comment"
                "public": True
            }
            
            response = self.session.post(share_url, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                return {
                    "success": True,
                    "share_url": result.get("share_url"),
                    "permissions": permissions,
                    "message": "Diagrama compartido exitosamente"
                }
            else:
                return {
                    "success": False,
                    "error": f"HTTP {response.status_code}"
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def export_diagram(self, xml_content: str, format: str = "png") -> Dict[str, Any]:
        """Exporta diagrama a diferentes formatos"""
        
        try:
            export_url = f"{self.base_url}/export"
            
            payload = {
                "xml": xml_content,
                "format": format,  # "png", "jpg", "svg", "pdf"
                "bg": "white",
                "scale": 1
            }
            
            response = self.session.post(export_url, data=payload)
            
            if response.status_code == 200:
                return {
                    "success": True,
                    "content": response.content,
                    "format": format,
                    "message": f"Diagrama exportado a {format.upper()}"
                }
            else:
                return {
                    "success": False,
                    "error": f"HTTP {response.status_code}"
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def validate_xml(self, xml_content: str) -> Dict[str, Any]:
        """Valida XML de Draw.io"""
        
        try:
            # Verificar estructura básica
            if not xml_content.strip().startswith('<?xml'):
                return {
                    "valid": False,
                    "error": "XML debe comenzar con declaración XML"
                }
            
            if '<mxfile' not in xml_content:
                return {
                    "valid": False,
                    "error": "XML debe contener elemento mxfile"
                }
            
            if '<diagram' not in xml_content:
                return {
                    "valid": False,
                    "error": "XML debe contener al menos un diagrama"
                }
            
            # Contar elementos
            cells = xml_content.count('<mxCell')
            aws_icons = xml_content.count('mxgraph.aws4')
            
            return {
                "valid": True,
                "elements": cells,
                "aws_icons": aws_icons,
                "message": f"XML válido con {cells} elementos y {aws_icons} iconos AWS"
            }
            
        except Exception as e:
            return {
                "valid": False,
                "error": str(e)
            }

# Funciones de utilidad
def create_drawio_url(xml_file_path: str) -> str:
    """Crea URL de Draw.io desde archivo XML local"""
    
    try:
        with open(xml_file_path, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        client = DrawIOAPIClient()
        result = client.create_diagram_from_xml(xml_content)
        
        if result["success"]:
            return result["url"]
        else:
            return f"Error: {result['error']}"
            
    except Exception as e:
        return f"Error: {str(e)}"

def export_drawio_to_png(xml_file_path: str, output_path: str) -> bool:
    """Exporta DrawIO XML a PNG usando API"""
    
    try:
        with open(xml_file_path, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        client = DrawIOAPIClient()
        result = client.export_diagram(xml_content, "png")
        
        if result["success"]:
            with open(output_path, 'wb') as f:
                f.write(result["content"])
            return True
        else:
            print(f"Error: {result['error']}")
            return False
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return False
