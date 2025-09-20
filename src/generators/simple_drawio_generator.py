#!/usr/bin/env python3
"""
Simple DrawIO Generator - Copia exacta de la lógica PNG exitosa
Enfoque minimalista: reutilizar lo que funciona
"""

import os
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

class SimpleDrawIOGenerator:
    """Generador DrawIO simple que copia la lógica PNG exitosa"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str = "outputs"):
        self.config = config
        self.output_dir = output_dir
        self.component_id = 2000
        
        # Mapeo directo PNG → DrawIO (copiado de diagram_generator.py exitoso)
        self.aws_shapes = {
            "fargate": "mxgraph.aws4.fargate",
            "rds": "mxgraph.aws4.rds", 
            "elasticache": "mxgraph.aws4.elasticache",
            "s3": "mxgraph.aws4.s3",
            "api_gateway": "mxgraph.aws4.api_gateway",
            "cloudfront": "mxgraph.aws4.cloudfront",
            "waf": "mxgraph.aws4.waf",
            "cognito": "mxgraph.aws4.cognito",
            "elb": "mxgraph.aws4.application_load_balancer",
            "textract": "mxgraph.aws4.textract",
            "lambda": "mxgraph.aws4.lambda",
            "sqs": "mxgraph.aws4.sqs",
            "sns": "mxgraph.aws4.sns"
        }
    
    def generate_network_drawio(self) -> str:
        """Genera diagrama de red - COPIA EXACTA de PNG exitoso"""
        
        components = []
        
        # Título (igual que PNG)
        components.append(self._create_title("BMC Network Architecture - AWS Senior Level"))
        
        # Componentes exactos del PNG exitoso
        components.append(self._create_aws_service("cloudfront", "CloudFront CDN\\n200+ edge locations\\nSSL/TLS 1.3", 150, 150))
        components.append(self._create_aws_service("waf", "AWS WAF\\nDDoS protection\\nRate limiting: 2K/s", 350, 150))
        components.append(self._create_aws_service("api_gateway", "API Gateway\\n10K req/s throttle\\nCaching: 300s TTL", 550, 150))
        
        # Microservicios (posiciones exactas del PNG)
        components.append(self._create_aws_service("invoice", "Invoice Service\\n2vCPU/4GB\\nBlue/Green deploy", 200, 400))
        components.append(self._create_aws_service("product", "Product Service\\n4vCPU/8GB\\n60M products", 400, 400))
        components.append(self._create_aws_service("ocr", "OCR Service\\n4vCPU/8GB\\nTextract integration", 600, 400))
        
        # Base de datos (posiciones exactas del PNG)
        components.append(self._create_aws_service("rds", "RDS Primary\\nPostgreSQL 14\\ndb.r6g.2xlarge", 300, 600))
        components.append(self._create_aws_service("redis", "ElastiCache Redis\\n6 nodes\\nMulti-AZ", 500, 600))
        
        # Storage
        components.append(self._create_aws_service("s3", "S3 Documents\\nIntelligent Tiering", 750, 150))
        
        # Conexiones exactas del PNG exitoso
        connections = [
            self._create_connection("cloudfront", "waf", "HTTPS Traffic"),
            self._create_connection("waf", "api_gateway", "Filtered Requests"),
            self._create_connection("api_gateway", "invoice", "Route /invoices"),
            self._create_connection("api_gateway", "product", "Route /products"),
            self._create_connection("api_gateway", "ocr", "Route /ocr"),
            self._create_connection("invoice", "rds", "Write Operations"),
            self._create_connection("product", "rds", "Write Operations"),
            self._create_connection("product", "redis", "Cache Lookup"),
            self._create_connection("ocr", "s3", "Store Documents")
        ]
        
        # Generar XML DrawIO
        xml_content = self._build_drawio_xml("Network Architecture", components + connections)
        
        # Guardar archivo
        return self._save_file(xml_content, "simple_network_architecture")
    
    def generate_microservices_drawio(self) -> str:
        """Genera diagrama de microservicios - COPIA EXACTA de PNG exitoso"""
        
        components = []
        
        # Título
        components.append(self._create_title("BMC Microservices - Detailed Architecture"))
        
        # API Layer (posiciones del PNG exitoso)
        components.append(self._create_aws_service("api_gateway", "API Gateway\\nThrottling: 10K req/s", 150, 120))
        components.append(self._create_aws_service("cognito", "Cognito User Pool\\nJWT + MFA", 400, 120))
        components.append(self._create_aws_service("alb", "Application LB\\nHealth checks", 650, 120))
        
        # Microservicios (layout del PNG)
        components.append(self._create_aws_service("invoice_task", "Invoice Task\\n2vCPU/4GB\\nPort: 8000", 120, 350))
        components.append(self._create_aws_service("product_task", "Product Task\\n4vCPU/8GB\\n<500ms lookup", 370, 350))
        components.append(self._create_aws_service("ocr_task", "OCR Task\\n4vCPU/8GB\\nTextract", 620, 350))
        
        # Data Services (posiciones del PNG)
        components.append(self._create_aws_service("rds", "RDS PostgreSQL\\ndb.r6g.2xlarge\\nMulti-AZ", 150, 580))
        components.append(self._create_aws_service("redis", "ElastiCache Redis\\n6 nodes\\nCluster mode", 400, 580))
        components.append(self._create_aws_service("s3", "S3 Documents\\nVersioning enabled", 650, 580))
        components.append(self._create_aws_service("textract", "Amazon Textract\\n>95% accuracy", 900, 580))
        
        # Conexiones del PNG exitoso
        connections = [
            self._create_connection("api_gateway", "cognito", "Auth"),
            self._create_connection("cognito", "alb", "Authorized"),
            self._create_connection("alb", "invoice_task", "Route"),
            self._create_connection("alb", "product_task", "Route"),
            self._create_connection("alb", "ocr_task", "Route"),
            self._create_connection("invoice_task", "rds", "Write"),
            self._create_connection("product_task", "redis", "Cache"),
            self._create_connection("product_task", "rds", "60M lookup"),
            self._create_connection("ocr_task", "textract", "OCR >95%"),
            self._create_connection("ocr_task", "s3", "Documents")
        ]
        
        xml_content = self._build_drawio_xml("Microservices Architecture", components + connections)
        return self._save_file(xml_content, "simple_microservices_detailed")
    
    def _create_title(self, text: str) -> str:
        """Crea título simple"""
        escaped_text = self._escape_xml(text)
        return f'''<mxCell id="title_{self._next_id()}" value="{escaped_text}" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=18;fontStyle=1;fontColor=#1976D2;" vertex="1" parent="1">
          <mxGeometry x="400" y="20" width="600" height="30" as="geometry"/>
        </mxCell>'''
    
    def _create_aws_service(self, service_type: str, label: str, x: int, y: int) -> str:
        """Crea servicio AWS - mapeo directo desde PNG"""
        
        shape = self.aws_shapes.get(service_type, "mxgraph.aws4.generic")
        escaped_label = self._escape_xml(label)
        component_id = f"{service_type}_{self._next_id()}"
        
        return f'''<mxCell id="{component_id}" value="{escaped_label}" style="shape={shape};labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E8F5E8;strokeColor=#4CAF50;fontColor=#2E7D32;" vertex="1" parent="1">
          <mxGeometry x="{x}" y="{y}" width="78" height="78" as="geometry"/>
        </mxCell>'''
    
    def _create_connection(self, source_type: str, target_type: str, label: str) -> str:
        """Crea conexión simple"""
        
        escaped_label = self._escape_xml(label)
        conn_id = f"conn_{self._next_id()}"
        label_id = f"label_{self._next_id()}"
        
        # IDs basados en tipo (simplificado)
        source_id = f"{source_type}_*"  # Usar wildcard para matching
        target_id = f"{target_type}_*"
        
        return f'''<mxCell id="{conn_id}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1976D2;strokeWidth=2;" edge="1" parent="1" source="{source_id}" target="{target_id}">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="{label_id}" value="{escaped_label}" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10;fontColor=#1976D2;" vertex="1" connectable="0" parent="{conn_id}">
          <mxGeometry x="-0.1" y="1" relative="1" as="geometry">
            <mxPoint as="offset"/>
          </mxGeometry>
        </mxCell>'''
    
    def _build_drawio_xml(self, diagram_name: str, components: list) -> str:
        """Construye XML DrawIO mínimo"""
        
        xml_parts = []
        
        # Header mínimo
        xml_parts.append(f'''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="{datetime.now().isoformat()}" version="22.1.11">
  <diagram name="{diagram_name}" id="simple_diagram">
    <mxGraphModel dx="2500" dy="1600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="1000">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>''')
        
        # Componentes
        for component in components:
            xml_parts.append(component)
        
        # Footer
        xml_parts.append('''
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>''')
        
        return ''.join(xml_parts)
    
    def _save_file(self, xml_content: str, filename: str) -> str:
        """Guarda archivo DrawIO"""
        
        output_dir = Path(self.output_dir) / "drawio" / "bmc_input"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        file_path = output_dir / f"{filename}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.drawio"
        file_path.write_text(xml_content, encoding='utf-8')
        
        print(f"✅ Simple DrawIO generado: {file_path}")
        return str(file_path)
    
    def _escape_xml(self, text: str) -> str:
        """Escapa caracteres XML"""
        if not text:
            return ""
        return (text.replace('&', '&amp;')
                   .replace('<', '&lt;')
                   .replace('>', '&gt;')
                   .replace('"', '&quot;'))
    
    def _next_id(self) -> int:
        """Genera ID único"""
        self.component_id += 1
        return self.component_id
    
    def generate_all_simple(self) -> dict:
        """Genera todos los diagramas simples"""
        
        results = {}
        
        print("🎨 Generando DrawIO simple (copiando lógica PNG exitosa)...")
        
        # Solo los diagramas que funcionan en PNG
        results["network"] = self.generate_network_drawio()
        results["microservices"] = self.generate_microservices_drawio()
        
        print(f"✅ {len(results)} diagramas DrawIO simples generados")
        return results
