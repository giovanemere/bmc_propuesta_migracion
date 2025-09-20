#!/usr/bin/env python3
"""
Advanced DrawIO Generator - Replica exactamente la estructura PNG
"""

from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Tuple
import json

class AdvancedDrawIOGenerator:
    """Generador DrawIO avanzado que replica estructura PNG"""
    
    def __init__(self, output_dir: str = "outputs"):
        self.output_dir = Path(output_dir)
        self.component_id = 3000
        
    def generate_network_like_png(self, config: Dict[str, Any], project_name: str = "bmc_input") -> str:
        """Genera DrawIO que replica exactamente el PNG de network"""
        
        xml_parts = []
        
        # Header
        xml_parts.append(self._get_xml_header("BMC Network Architecture - PNG Level"))
        
        # AWS Cloud Container (como Cluster en PNG)
        xml_parts.append(self._create_aws_cloud_container())
        
        # Edge Services Layer (top level como PNG)
        edge_components = self._create_edge_layer()
        xml_parts.extend(edge_components)
        
        # VPC Container (como Cluster VPC en PNG)
        xml_parts.append(self._create_vpc_container())
        
        # AZ Containers (como Clusters AZ en PNG)
        az_components = self._create_az_containers()
        xml_parts.extend(az_components)
        
        # Microservices en AZ (posiciones exactas PNG)
        microservices = self._create_microservices_in_az()
        xml_parts.extend(microservices)
        
        # Data Layer (bottom como PNG)
        data_components = self._create_data_layer()
        xml_parts.extend(data_components)
        
        # Conexiones con etiquetas (como PNG >> operator)
        connections = self._create_png_style_connections()
        xml_parts.extend(connections)
        
        # Footer
        xml_parts.append(self._get_xml_footer())
        
        # Guardar archivo
        xml_content = ''.join(xml_parts)
        return self._save_advanced_file(xml_content, "advanced_network", project_name)
    
    def _get_xml_header(self, title: str) -> str:
        """Header XML con configuración profesional"""
        return f'''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="{datetime.now().isoformat()}" version="22.1.11">
  <diagram name="{title}" id="advanced_network">
    <mxGraphModel dx="2500" dy="1600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1600" pageHeight="1200">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Título Principal -->
        <mxCell id="main_title" value="{title}" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=20;fontStyle=1;fontColor=#1976D2;" vertex="1" parent="1">
          <mxGeometry x="500" y="10" width="600" height="40" as="geometry"/>
        </mxCell>'''
    
    def _create_aws_cloud_container(self) -> str:
        """Crea contenedor AWS Cloud como Cluster PNG"""
        return f'''
        <!-- AWS Cloud Container (como Cluster en PNG) -->
        <mxCell id="aws_cloud_{self._next_id()}" value="AWS Cloud - us-east-1" style="fillColor=#E3F2FD;strokeColor=#1976D2;dashed=1;verticalAlign=top;fontStyle=1;fontSize=16;fontColor=#1976D2;labelPosition=center;verticalLabelPosition=top;align=center;" vertex="1" parent="1">
          <mxGeometry x="50" y="70" width="1500" height="1000" as="geometry"/>
        </mxCell>'''
    
    def _create_edge_layer(self) -> List[str]:
        """Crea capa edge como en PNG (top level)"""
        components = []
        
        # Internet (como en PNG)
        components.append(f'''
        <mxCell id="internet_{self._next_id()}" value="Internet\\nGlobal Access" style="shape=mxgraph.aws4.internet;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#FFFFFF;strokeColor=#1976D2;fontColor=#1976D2;" vertex="1" parent="1">
          <mxGeometry x="100" y="120" width="78" height="78" as="geometry"/>
        </mxCell>''')
        
        # Users (como en PNG)
        components.append(f'''
        <mxCell id="users_{self._next_id()}" value="BMC Users\\n10K Concurrent\\nMulti-device" style="shape=mxgraph.aws4.users;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E3F2FD;strokeColor=#1976D2;fontColor=#0D47A1;" vertex="1" parent="aws_cloud_{self.component_id-1}">
          <mxGeometry x="50" y="80" width="78" height="78" as="geometry"/>
        </mxCell>''')
        
        # CloudFront (posición exacta PNG)
        components.append(f'''
        <mxCell id="cloudfront_{self._next_id()}" value="CloudFront CDN\\n200+ edge locations\\nSSL/TLS 1.3\\nGzip compression" style="shape=mxgraph.aws4.cloudfront;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E3F2FD;strokeColor=#1976D2;fontColor=#0D47A1;" vertex="1" parent="aws_cloud_{self.component_id-2}">
          <mxGeometry x="250" y="80" width="78" height="78" as="geometry"/>
        </mxCell>''')
        
        # WAF (después de CloudFront como PNG)
        components.append(f'''
        <mxCell id="waf_{self._next_id()}" value="AWS WAF\\nDDoS protection\\nGeo blocking\\nRate limiting: 2K/s" style="shape=mxgraph.aws4.waf;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#FFEBEE;strokeColor=#D32F2F;fontColor=#B71C1C;" vertex="1" parent="aws_cloud_{self.component_id-3}">
          <mxGeometry x="450" y="80" width="78" height="78" as="geometry"/>
        </mxCell>''')
        
        # API Gateway (después de WAF como PNG)
        components.append(f'''
        <mxCell id="api_gateway_{self._next_id()}" value="API Gateway\\n10K req/s throttle\\nCaching: 300s TTL\\nCustom authorizers" style="shape=mxgraph.aws4.api_gateway;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E3F2FD;strokeColor=#1976D2;fontColor=#0D47A1;" vertex="1" parent="aws_cloud_{self.component_id-4}">
          <mxGeometry x="650" y="80" width="78" height="78" as="geometry"/>
        </mxCell>''')
        
        return components
    
    def _create_vpc_container(self) -> str:
        """Crea contenedor VPC como Cluster PNG"""
        return f'''
        <!-- VPC Container (como Cluster VPC en PNG) -->
        <mxCell id="vpc_{self._next_id()}" value="VPC 10.0.0.0/16 - Multi-AZ" style="fillColor=#F5F5F5;strokeColor=#666666;dashed=1;verticalAlign=top;fontStyle=1;fontSize=14;fontColor=#666666;" vertex="1" parent="aws_cloud_{self.component_id-6}">
          <mxGeometry x="100" y="250" width="1200" height="650" as="geometry"/>
        </mxCell>'''
    
    def _create_az_containers(self) -> List[str]:
        """Crea contenedores AZ como Clusters PNG"""
        containers = []
        
        # AZ us-east-1a (como Cluster en PNG)
        containers.append(f'''
        <!-- AZ us-east-1a Container -->
        <mxCell id="az_1a_{self._next_id()}" value="Availability Zone us-east-1a" style="fillColor=#E8F5E8;strokeColor=#4CAF50;dashed=1;verticalAlign=top;fontStyle=1;fontSize=12;fontColor=#2E7D32;" vertex="1" parent="vpc_{self.component_id-1}">
          <mxGeometry x="50" y="50" width="500" height="250" as="geometry"/>
        </mxCell>''')
        
        # Public Subnet en AZ-1a
        containers.append(f'''
        <mxCell id="public_1a_{self._next_id()}" value="Public Subnet\\n10.0.1.0/24" style="fillColor=#E8F5E8;strokeColor=#4CAF50;dashed=2;verticalAlign=top;fontSize=10;fontColor=#2E7D32;" vertex="1" parent="az_1a_{self.component_id-1}">
          <mxGeometry x="20" y="30" width="200" height="80" as="geometry"/>
        </mxCell>''')
        
        # Private Subnet en AZ-1a
        containers.append(f'''
        <mxCell id="private_1a_{self._next_id()}" value="Private Subnet\\n10.0.10.0/24" style="fillColor=#FFF3E0;strokeColor=#FF9800;dashed=2;verticalAlign=top;fontSize=10;fontColor=#E65100;" vertex="1" parent="az_1a_{self.component_id-2}">
          <mxGeometry x="20" y="130" width="200" height="80" as="geometry"/>
        </mxCell>''')
        
        # AZ us-east-1b (como Cluster en PNG)
        containers.append(f'''
        <!-- AZ us-east-1b Container -->
        <mxCell id="az_1b_{self._next_id()}" value="Availability Zone us-east-1b" style="fillColor=#FFF3E0;strokeColor=#FF9800;dashed=1;verticalAlign=top;fontStyle=1;fontSize=12;fontColor=#E65100;" vertex="1" parent="vpc_{self.component_id-4}">
          <mxGeometry x="600" y="50" width="500" height="250" as="geometry"/>
        </mxCell>''')
        
        # Public Subnet en AZ-1b
        containers.append(f'''
        <mxCell id="public_1b_{self._next_id()}" value="Public Subnet\\n10.0.2.0/24" style="fillColor=#FFF3E0;strokeColor=#FF9800;dashed=2;verticalAlign=top;fontSize=10;fontColor=#E65100;" vertex="1" parent="az_1b_{self.component_id-1}">
          <mxGeometry x="20" y="30" width="200" height="80" as="geometry"/>
        </mxCell>''')
        
        # Private Subnet en AZ-1b
        containers.append(f'''
        <mxCell id="private_1b_{self._next_id()}" value="Private Subnet\\n10.0.11.0/24" style="fillColor=#E8F5E8;strokeColor=#4CAF50;dashed=2;verticalAlign=top;fontSize=10;fontColor=#2E7D32;" vertex="1" parent="az_1b_{self.component_id-2}">
          <mxGeometry x="20" y="130" width="200" height="80" as="geometry"/>
        </mxCell>''')
        
        return containers
    
    def _create_microservices_in_az(self) -> List[str]:
        """Crea microservicios en AZ como PNG"""
        services = []
        
        # Invoice Service en AZ-1a Private Subnet
        services.append(f'''
        <mxCell id="invoice_service_{self._next_id()}" value="Invoice Service\\n2vCPU/4GB\\nBlue/Green deploy\\nHealth checks" style="shape=mxgraph.aws4.fargate;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#FFF3E0;strokeColor=#FF9800;fontColor=#E65100;" vertex="1" parent="private_1a_{self.component_id-4}">
          <mxGeometry x="50" y="20" width="60" height="60" as="geometry"/>
        </mxCell>''')
        
        # Product Service en AZ-1a Private Subnet
        services.append(f'''
        <mxCell id="product_service_{self._next_id()}" value="Product Service\\n4vCPU/8GB\\n60M products\\nElasticsearch" style="shape=mxgraph.aws4.fargate;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#FFF3E0;strokeColor=#FF9800;fontColor=#E65100;" vertex="1" parent="private_1a_{self.component_id-5}">
          <mxGeometry x="130" y="20" width="60" height="60" as="geometry"/>
        </mxCell>''')
        
        # OCR Service en AZ-1b Private Subnet
        services.append(f'''
        <mxCell id="ocr_service_{self._next_id()}" value="OCR Service\\n4vCPU/8GB\\nTextract integration\\n>95% accuracy" style="shape=mxgraph.aws4.fargate;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#FFF3E0;strokeColor=#FF9800;fontColor=#E65100;" vertex="1" parent="private_1b_{self.component_id-1}">
          <mxGeometry x="50" y="20" width="60" height="60" as="geometry"/>
        </mxCell>''')
        
        # Commission Service en AZ-1b Private Subnet
        services.append(f'''
        <mxCell id="commission_service_{self._next_id()}" value="Commission Service\\n2vCPU/4GB\\nDIAN compliance\\nAudit trail" style="shape=mxgraph.aws4.fargate;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#FFF3E0;strokeColor=#FF9800;fontColor=#E65100;" vertex="1" parent="private_1b_{self.component_id-2}">
          <mxGeometry x="130" y="20" width="60" height="60" as="geometry"/>
        </mxCell>''')
        
        return services
    
    def _create_data_layer(self) -> List[str]:
        """Crea capa de datos como PNG (bottom)"""
        data_components = []
        
        # Isolated Subnets para datos
        data_components.append(f'''
        <!-- Isolated Subnet para datos -->
        <mxCell id="isolated_subnet_{self._next_id()}" value="Isolated Subnet - Database Tier\\n10.0.20.0/24 & 10.0.21.0/24" style="fillColor=#E8F5E8;strokeColor=#4CAF50;dashed=1;verticalAlign=top;fontSize=12;fontColor=#2E7D32;" vertex="1" parent="vpc_{self.component_id-10}">
          <mxGeometry x="200" y="400" width="800" height="200" as="geometry"/>
        </mxCell>''')
        
        # RDS Primary (como en PNG)
        data_components.append(f'''
        <mxCell id="rds_primary_{self._next_id()}" value="RDS Primary\\nPostgreSQL 14\\ndb.r6g.2xlarge\\n35-day backup\\nPerformance Insights" style="shape=mxgraph.aws4.rds;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E8F5E8;strokeColor=#4CAF50;fontColor=#2E7D32;" vertex="1" parent="isolated_subnet_{self.component_id-1}">
          <mxGeometry x="100" y="80" width="78" height="78" as="geometry"/>
        </mxCell>''')
        
        # RDS Replica (Multi-AZ como PNG)
        data_components.append(f'''
        <mxCell id="rds_replica_{self._next_id()}" value="RDS Standby\\nus-east-1b\\nCross-AZ replication\\nPromotion ready" style="shape=mxgraph.aws4.rds;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E8F5E8;strokeColor=#4CAF50;fontColor=#2E7D32;" vertex="1" parent="isolated_subnet_{self.component_id-2}">
          <mxGeometry x="300" y="80" width="78" height="78" as="geometry"/>
        </mxCell>''')
        
        # ElastiCache Redis (como PNG)
        data_components.append(f'''
        <mxCell id="redis_cache_{self._next_id()}" value="ElastiCache Redis\\n6 nodes (3 shards)\\nMulti-AZ\\n99.9% availability" style="shape=mxgraph.aws4.elasticache;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E8F5E8;strokeColor=#4CAF50;fontColor=#2E7D32;" vertex="1" parent="isolated_subnet_{self.component_id-3}">
          <mxGeometry x="500" y="80" width="78" height="78" as="geometry"/>
        </mxCell>''')
        
        # S3 Storage (fuera de VPC como PNG)
        data_components.append(f'''
        <mxCell id="s3_storage_{self._next_id()}" value="S3 Documents\\nIntelligent Tiering\\n90d → Glacier\\nVersioning enabled" style="shape=mxgraph.aws4.s3;labelPosition=bottom;verticalLabelPosition=top;align=center;verticalAlign=bottom;fillColor=#E8F5E8;strokeColor=#4CAF50;fontColor=#2E7D32;" vertex="1" parent="aws_cloud_{self.component_id-14}">
          <mxGeometry x="1350" y="200" width="78" height="78" as="geometry"/>
        </mxCell>''')
        
        return data_components
    
    def _create_png_style_connections(self) -> List[str]:
        """Crea conexiones con etiquetas como PNG (>> operator)"""
        connections = []
        
        # Internet → Users (como PNG)
        connections.append(f'''
        <mxCell id="conn_internet_users" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1976D2;strokeWidth=2;" edge="1" parent="1" source="internet_{self.component_id-15}" target="users_{self.component_id-14}">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="label_internet_users" value="HTTPS\\nGlobal Access" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10;fontColor=#1976D2;fontStyle=1;" vertex="1" connectable="0" parent="conn_internet_users">
          <mxGeometry x="-0.1" y="1" relative="1" as="geometry"><mxPoint as="offset"/></mxGeometry>
        </mxCell>''')
        
        # Users → CloudFront (como PNG)
        connections.append(f'''
        <mxCell id="conn_users_cf" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1976D2;strokeWidth=2;" edge="1" parent="1" source="users_{self.component_id-14}" target="cloudfront_{self.component_id-13}">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="label_users_cf" value="Web Traffic\\n200+ Locations" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10;fontColor=#1976D2;fontStyle=1;" vertex="1" connectable="0" parent="conn_users_cf">
          <mxGeometry x="-0.1" y="1" relative="1" as="geometry"><mxPoint as="offset"/></mxGeometry>
        </mxCell>''')
        
        # CloudFront → WAF (como PNG)
        connections.append(f'''
        <mxCell id="conn_cf_waf" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#D32F2F;strokeWidth=3;" edge="1" parent="1" source="cloudfront_{self.component_id-13}" target="waf_{self.component_id-12}">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="label_cf_waf" value="Security Filter\\nDDoS Protection" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10;fontColor=#D32F2F;fontStyle=1;" vertex="1" connectable="0" parent="conn_cf_waf">
          <mxGeometry x="-0.1" y="1" relative="1" as="geometry"><mxPoint as="offset"/></mxGeometry>
        </mxCell>''')
        
        # WAF → API Gateway (como PNG)
        connections.append(f'''
        <mxCell id="conn_waf_api" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1976D2;strokeWidth=2;" edge="1" parent="1" source="waf_{self.component_id-12}" target="api_gateway_{self.component_id-11}">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="label_waf_api" value="Clean Traffic\\n10K req/s" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10;fontColor=#1976D2;fontStyle=1;" vertex="1" connectable="0" parent="conn_waf_api">
          <mxGeometry x="-0.1" y="1" relative="1" as="geometry"><mxPoint as="offset"/></mxGeometry>
        </mxCell>''')
        
        # API Gateway → Microservices (como PNG)
        connections.append(f'''
        <mxCell id="conn_api_invoice" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#FF9800;strokeWidth=2;" edge="1" parent="1" source="api_gateway_{self.component_id-11}" target="invoice_service_{self.component_id-7}">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="label_api_invoice" value="Route\\n/invoices" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10;fontColor=#FF9800;fontStyle=1;" vertex="1" connectable="0" parent="conn_api_invoice">
          <mxGeometry x="-0.1" y="1" relative="1" as="geometry"><mxPoint as="offset"/></mxGeometry>
        </mxCell>''')
        
        # Microservices → Database (como PNG)
        connections.append(f'''
        <mxCell id="conn_invoice_rds" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="invoice_service_{self.component_id-7}" target="rds_primary_{self.component_id-4}">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="label_invoice_rds" value="Database\\nWrite Ops" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10;fontColor=#4CAF50;fontStyle=1;" vertex="1" connectable="0" parent="conn_invoice_rds">
          <mxGeometry x="-0.1" y="1" relative="1" as="geometry"><mxPoint as="offset"/></mxGeometry>
        </mxCell>''')
        
        return connections
    
    def _get_xml_footer(self) -> str:
        """Footer XML"""
        return '''
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    def _save_advanced_file(self, xml_content: str, diagram_type: str, project_name: str) -> str:
        """Guarda archivo DrawIO avanzado"""
        
        output_dir = self.output_dir / "drawio" / project_name
        output_dir.mkdir(parents=True, exist_ok=True)
        
        filename = f"{diagram_type}_png_level_{datetime.now().strftime('%Y%m%d_%H%M%S')}.drawio"
        file_path = output_dir / filename
        
        file_path.write_text(xml_content, encoding='utf-8')
        
        print(f"✅ Advanced DrawIO (PNG Level) generado: {file_path}")
        return str(file_path)
    
    def _next_id(self) -> int:
        """Genera ID único"""
        self.component_id += 1
        return self.component_id
