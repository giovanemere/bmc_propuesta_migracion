#!/usr/bin/env python3
"""
Template DrawIO Generator - Basado en plantillas XML
Enfoque más eficiente usando plantillas predefinidas
"""

from xml.etree import ElementTree as ET
from pathlib import Path
from datetime import datetime
from typing import Dict, Any
import shutil

class TemplateDrawIOGenerator:
    """Generador DrawIO basado en plantillas XML"""
    
    def __init__(self, output_dir: str = "outputs"):
        self.output_dir = Path(output_dir)
        self.templates_dir = Path(__file__).parent.parent.parent / "templates"
        
    def generate_from_template(self, template_name: str, config: Dict[str, Any], project_name: str = "bmc_input") -> str:
        """Genera DrawIO desde plantilla"""
        
        # Cargar plantilla
        template_path = self.templates_dir / f"{template_name}.drawio"
        
        if not template_path.exists():
            # Crear plantilla si no existe
            self._create_template(template_name)
        
        # Cargar XML
        tree = ET.parse(template_path)
        root = tree.getroot()
        
        # Aplicar configuración
        self._apply_config_to_template(root, config)
        
        # Guardar resultado
        output_path = self._save_generated_file(tree, template_name, project_name)
        
        return output_path
    
    def _create_template(self, template_name: str) -> None:
        """Crea plantilla base si no existe"""
        
        self.templates_dir.mkdir(parents=True, exist_ok=True)
        template_path = self.templates_dir / f"{template_name}.drawio"
        
        if template_name == "aws_network":
            xml_content = self._get_network_template()
        elif template_name == "aws_microservices":
            xml_content = self._get_microservices_template()
        else:
            xml_content = self._get_basic_template()
        
        template_path.write_text(xml_content, encoding='utf-8')
        print(f"✅ Plantilla creada: {template_path}")
    
    def _get_network_template(self) -> str:
        """Plantilla de red AWS"""
        
        return '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="2025-09-20T00:00:00.000Z" version="22.1.11">
  <diagram name="AWS Network Architecture" id="network_template">
    <mxGraphModel dx="2500" dy="1600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="1000">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Título -->
        <mxCell id="title" value="{{TITLE}}" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=18;fontStyle=1;fontColor=#1976D2;" vertex="1" parent="1">
          <mxGeometry x="400" y="20" width="600" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Edge Services -->
        <mxCell id="cloudfront" value="{{CLOUDFRONT_LABEL}}" style="shape=mxgraph.aws4.cloudfront;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E3F2FD;strokeColor=#1976D2;fontColor=#0D47A1;" vertex="1" parent="1">
          <mxGeometry x="150" y="150" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <mxCell id="waf" value="{{WAF_LABEL}}" style="shape=mxgraph.aws4.waf;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#FFEBEE;strokeColor=#D32F2F;fontColor=#B71C1C;" vertex="1" parent="1">
          <mxGeometry x="350" y="150" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <mxCell id="api_gateway" value="{{API_GATEWAY_LABEL}}" style="shape=mxgraph.aws4.api_gateway;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E3F2FD;strokeColor=#1976D2;fontColor=#0D47A1;" vertex="1" parent="1">
          <mxGeometry x="550" y="150" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <!-- Microservices -->
        <mxCell id="invoice_service" value="{{INVOICE_SERVICE_LABEL}}" style="shape=mxgraph.aws4.fargate;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#FFF3E0;strokeColor=#FF9800;fontColor=#E65100;" vertex="1" parent="1">
          <mxGeometry x="200" y="400" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <mxCell id="product_service" value="{{PRODUCT_SERVICE_LABEL}}" style="shape=mxgraph.aws4.fargate;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#FFF3E0;strokeColor=#FF9800;fontColor=#E65100;" vertex="1" parent="1">
          <mxGeometry x="400" y="400" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <mxCell id="ocr_service" value="{{OCR_SERVICE_LABEL}}" style="shape=mxgraph.aws4.fargate;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#FFF3E0;strokeColor=#FF9800;fontColor=#E65100;" vertex="1" parent="1">
          <mxGeometry x="600" y="400" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <!-- Data Services -->
        <mxCell id="rds_primary" value="{{RDS_LABEL}}" style="shape=mxgraph.aws4.rds;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E8F5E8;strokeColor=#4CAF50;fontColor=#2E7D32;" vertex="1" parent="1">
          <mxGeometry x="300" y="600" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <mxCell id="redis_cache" value="{{REDIS_LABEL}}" style="shape=mxgraph.aws4.elasticache;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E8F5E8;strokeColor=#4CAF50;fontColor=#2E7D32;" vertex="1" parent="1">
          <mxGeometry x="500" y="600" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <mxCell id="s3_storage" value="{{S3_LABEL}}" style="shape=mxgraph.aws4.s3;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E8F5E8;strokeColor=#4CAF50;fontColor=#2E7D32;" vertex="1" parent="1">
          <mxGeometry x="750" y="150" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <!-- Connections -->
        <mxCell id="conn1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1976D2;strokeWidth=2;" edge="1" parent="1" source="cloudfront" target="waf">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1976D2;strokeWidth=2;" edge="1" parent="1" source="waf" target="api_gateway">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#FF9800;strokeWidth=2;" edge="1" parent="1" source="api_gateway" target="invoice_service">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#FF9800;strokeWidth=2;" edge="1" parent="1" source="api_gateway" target="product_service">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn5" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#FF9800;strokeWidth=2;" edge="1" parent="1" source="api_gateway" target="ocr_service">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn6" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="invoice_service" target="rds_primary">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn7" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="product_service" target="rds_primary">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn8" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="product_service" target="redis_cache">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn9" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="ocr_service" target="s3_storage">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    def _get_microservices_template(self) -> str:
        """Plantilla de microservicios"""
        
        return '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="2025-09-20T00:00:00.000Z" version="22.1.11">
  <diagram name="AWS Microservices Architecture" id="microservices_template">
    <mxGraphModel dx="2500" dy="1600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="1000">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Título -->
        <mxCell id="title" value="{{TITLE}}" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=18;fontStyle=1;fontColor=#1976D2;" vertex="1" parent="1">
          <mxGeometry x="400" y="20" width="600" height="30" as="geometry"/>
        </mxCell>
        
        <!-- API Layer -->
        <mxCell id="api_gateway" value="{{API_GATEWAY_LABEL}}" style="shape=mxgraph.aws4.api_gateway;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E3F2FD;strokeColor=#1976D2;fontColor=#0D47A1;" vertex="1" parent="1">
          <mxGeometry x="150" y="120" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <mxCell id="cognito" value="{{COGNITO_LABEL}}" style="shape=mxgraph.aws4.cognito;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#FFEBEE;strokeColor=#D32F2F;fontColor=#B71C1C;" vertex="1" parent="1">
          <mxGeometry x="400" y="120" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <mxCell id="alb" value="{{ALB_LABEL}}" style="shape=mxgraph.aws4.application_load_balancer;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E3F2FD;strokeColor=#1976D2;fontColor=#0D47A1;" vertex="1" parent="1">
          <mxGeometry x="650" y="120" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <!-- Microservices Tasks -->
        <mxCell id="invoice_task" value="{{INVOICE_TASK_LABEL}}" style="shape=mxgraph.aws4.fargate;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#FFF3E0;strokeColor=#FF9800;fontColor=#E65100;" vertex="1" parent="1">
          <mxGeometry x="120" y="350" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <mxCell id="product_task" value="{{PRODUCT_TASK_LABEL}}" style="shape=mxgraph.aws4.fargate;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#FFF3E0;strokeColor=#FF9800;fontColor=#E65100;" vertex="1" parent="1">
          <mxGeometry x="370" y="350" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <mxCell id="ocr_task" value="{{OCR_TASK_LABEL}}" style="shape=mxgraph.aws4.fargate;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#FFF3E0;strokeColor=#FF9800;fontColor=#E65100;" vertex="1" parent="1">
          <mxGeometry x="620" y="350" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <!-- Data Services -->
        <mxCell id="rds" value="{{RDS_LABEL}}" style="shape=mxgraph.aws4.rds;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E8F5E8;strokeColor=#4CAF50;fontColor=#2E7D32;" vertex="1" parent="1">
          <mxGeometry x="150" y="580" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <mxCell id="redis" value="{{REDIS_LABEL}}" style="shape=mxgraph.aws4.elasticache;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E8F5E8;strokeColor=#4CAF50;fontColor=#2E7D32;" vertex="1" parent="1">
          <mxGeometry x="400" y="580" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <mxCell id="s3" value="{{S3_LABEL}}" style="shape=mxgraph.aws4.s3;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E8F5E8;strokeColor=#4CAF50;fontColor=#2E7D32;" vertex="1" parent="1">
          <mxGeometry x="650" y="580" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <mxCell id="textract" value="{{TEXTRACT_LABEL}}" style="shape=mxgraph.aws4.textract;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#F3E5F5;strokeColor=#9C27B0;fontColor=#4A148C;" vertex="1" parent="1">
          <mxGeometry x="900" y="580" width="78" height="78" as="geometry"/>
        </mxCell>
        
        <!-- Connections -->
        <mxCell id="conn1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1976D2;strokeWidth=2;" edge="1" parent="1" source="api_gateway" target="cognito">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1976D2;strokeWidth=2;" edge="1" parent="1" source="cognito" target="alb">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#FF9800;strokeWidth=2;" edge="1" parent="1" source="alb" target="invoice_task">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#FF9800;strokeWidth=2;" edge="1" parent="1" source="alb" target="product_task">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn5" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#FF9800;strokeWidth=2;" edge="1" parent="1" source="alb" target="ocr_task">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn6" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="invoice_task" target="rds">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn7" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="product_task" target="redis">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn8" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="product_task" target="rds">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn9" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#9C27B0;strokeWidth=2;" edge="1" parent="1" source="ocr_task" target="textract">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn10" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="ocr_task" target="s3">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    def _get_basic_template(self) -> str:
        """Plantilla básica"""
        
        return '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="2025-09-20T00:00:00.000Z" version="22.1.11">
  <diagram name="Basic Template" id="basic_template">
    <mxGraphModel dx="2500" dy="1600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="1000">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <mxCell id="title" value="{{TITLE}}" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=18;fontStyle=1;fontColor=#1976D2;" vertex="1" parent="1">
          <mxGeometry x="400" y="20" width="600" height="30" as="geometry"/>
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    def _apply_config_to_template(self, root: ET.Element, config: Dict[str, Any]) -> None:
        """Aplica configuración a la plantilla"""
        
        # Reemplazos básicos
        replacements = {
            "{{TITLE}}": "BMC Architecture - AWS Senior Level",
            "{{CLOUDFRONT_LABEL}}": "CloudFront CDN\\n200+ edge locations\\nSSL/TLS 1.3",
            "{{WAF_LABEL}}": "AWS WAF\\nDDoS protection\\nRate limiting: 2K/s",
            "{{API_GATEWAY_LABEL}}": "API Gateway\\n10K req/s throttle\\nCaching: 300s TTL",
            "{{INVOICE_SERVICE_LABEL}}": "Invoice Service\\n2vCPU/4GB\\nBlue/Green deploy",
            "{{PRODUCT_SERVICE_LABEL}}": "Product Service\\n4vCPU/8GB\\n60M products",
            "{{OCR_SERVICE_LABEL}}": "OCR Service\\n4vCPU/8GB\\nTextract integration",
            "{{RDS_LABEL}}": "RDS Primary\\nPostgreSQL 14\\ndb.r6g.2xlarge\\n35-day backup",
            "{{REDIS_LABEL}}": "ElastiCache Redis\\n6 nodes (3 shards)\\nMulti-AZ",
            "{{S3_LABEL}}": "S3 Documents\\nIntelligent Tiering\\n90d → Glacier",
            "{{COGNITO_LABEL}}": "Cognito User Pool\\nJWT validation\\nMFA: TOTP + SMS",
            "{{ALB_LABEL}}": "Application LB\\nSticky sessions\\nHealth checks",
            "{{INVOICE_TASK_LABEL}}": "Invoice Task\\n2vCPU/4GB\\nPort: 8000",
            "{{PRODUCT_TASK_LABEL}}": "Product Task\\n4vCPU/8GB\\n<500ms lookup",
            "{{OCR_TASK_LABEL}}": "OCR Task\\n4vCPU/8GB\\nTextract",
            "{{TEXTRACT_LABEL}}": "Amazon Textract\\n>95% accuracy\\nForms + Tables"
        }
        
        # Aplicar reemplazos en todo el XML
        xml_string = ET.tostring(root, encoding='unicode')
        
        for placeholder, value in replacements.items():
            xml_string = xml_string.replace(placeholder, value)
        
        # Parsear XML modificado
        new_root = ET.fromstring(xml_string)
        
        # Reemplazar contenido del root original
        root.clear()
        root.tag = new_root.tag
        root.attrib = new_root.attrib
        root.text = new_root.text
        root.tail = new_root.tail
        root.extend(new_root)
    
    def _save_generated_file(self, tree: ET.ElementTree, template_name: str, project_name: str) -> str:
        """Guarda archivo generado"""
        
        output_dir = self.output_dir / "drawio" / project_name
        output_dir.mkdir(parents=True, exist_ok=True)
        
        filename = f"template_{template_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.drawio"
        file_path = output_dir / filename
        
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
        
        print(f"✅ Template DrawIO generado: {file_path}")
        return str(file_path)
    
    def generate_all_templates(self, config: Dict[str, Any], project_name: str = "bmc_input") -> Dict[str, str]:
        """Genera todos los diagramas desde plantillas"""
        
        results = {}
        
        print("🎨 Generando DrawIO desde plantillas...")
        
        # Generar diagramas principales
        templates = ["aws_network", "aws_microservices"]
        
        for template_name in templates:
            try:
                result_path = self.generate_from_template(template_name, config, project_name)
                results[template_name] = result_path
            except Exception as e:
                print(f"❌ Error generando {template_name}: {e}")
        
        print(f"✅ {len(results)} diagramas generados desde plantillas")
        return results
