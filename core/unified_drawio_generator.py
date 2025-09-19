#!/usr/bin/env python3
"""
Unified Draw.io Generator - Generador unificado de archivos Draw.io
Genera un solo archivo Draw.io profesional y completo
"""

import os
from typing import Dict, Any

class UnifiedDrawioGenerator:
    """Generador unificado de archivos Draw.io"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str = "output"):
        self.config = config
        self.output_dir = output_dir
        
    def generate_unified_drawio(self, project_name: str = "Architecture") -> str:
        """Genera un archivo Draw.io unificado y completo"""
        
        # Extraer información del config
        project_info = self.config.get("project", {})
        microservices = self.config.get("microservices", {})
        aws_services = self.config.get("aws_services", {})
        
        title = project_info.get("name", f"{project_name} AWS Architecture")
        description = project_info.get("description", "Cloud Architecture Diagram")
        
        # Generar XML completo
        xml_content = f'''<mxfile host="app.diagrams.net" modified="2024-09-19T21:00:00.000Z" agent="MCP Diagram Generator" version="22.1.11">
  <diagram name="{title}" id="unified_architecture">
    <mxGraphModel dx="1800" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1600" pageHeight="1000">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Header -->
        <mxCell id="header" value="{title}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=none;fontColor=#FFFFFF;fontSize=18;fontStyle=1;align=center;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1500" height="50" as="geometry"/>
        </mxCell>
        
        <mxCell id="subtitle" value="{description}" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;fontSize=12;fontColor=#666666;" vertex="1" parent="1">
          <mxGeometry x="50" y="75" width="1500" height="25" as="geometry"/>
        </mxCell>
        
        <!-- On-Premise Zone -->
        <mxCell id="onpremise" value="On-Premise / External Systems" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFEBEE;strokeColor=#D32F2F;strokeWidth=3;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=15;dashed=1;dashPattern=8 8;" vertex="1" parent="1">
          <mxGeometry x="50" y="120" width="300" height="200" as="geometry"/>
        </mxCell>
        
        <!-- Users -->
        <mxCell id="users" value="BMC Users&#10;Web/Mobile/Admin&#10;10K concurrent" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.users;" vertex="1" parent="1">
          <mxGeometry x="100" y="160" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- DIAN API -->
        <mxCell id="dian" value="DIAN API&#10;Tax Authority&#10;1K req/hour" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#607D8B;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.internet_gateway;" vertex="1" parent="1">
          <mxGeometry x="250" y="160" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- SFTP Systems -->
        <mxCell id="sftp" value="SFTP Systems&#10;Batch Files&#10;Nightly Import" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#795548;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.storage_gateway;" vertex="1" parent="1">
          <mxGeometry x="175" y="240" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- AWS Cloud -->
        <mxCell id="awscloud" value="AWS Cloud - us-east-1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;strokeWidth=4;fontSize=16;fontStyle=1;verticalAlign=top;spacingTop=20;" vertex="1" parent="1">
          <mxGeometry x="400" y="120" width="1150" height="800" as="geometry"/>
        </mxCell>
        
        <!-- Edge Security Zone -->
        <mxCell id="edgezone" value="Edge Security &amp; CDN" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#FF9800;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="450" y="170" width="500" height="100" as="geometry"/>
        </mxCell>
        
        <!-- CloudFront -->
        <mxCell id="cloudfront" value="CloudFront&#10;Global CDN&#10;SSL Termination" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudfront;" vertex="1" parent="1">
          <mxGeometry x="480" y="200" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- WAF -->
        <mxCell id="waf" value="WAF&#10;DDoS Protection&#10;Rate Limiting" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.waf;" vertex="1" parent="1">
          <mxGeometry x="580" y="200" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- API Gateway -->
        <mxCell id="api" value="API Gateway&#10;REST + GraphQL&#10;1K req/s" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.api_gateway;" vertex="1" parent="1">
          <mxGeometry x="680" y="200" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Cognito -->
        <mxCell id="cognito" value="Cognito&#10;User Pool&#10;MFA Enabled" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cognito;" vertex="1" parent="1">
          <mxGeometry x="780" y="200" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Application Zone -->
        <mxCell id="appzone" value="Application Layer - ECS Fargate Auto Scaling" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#4CAF50;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="450" y="300" width="700" height="200" as="geometry"/>
        </mxCell>
        
        <!-- ALB -->
        <mxCell id="alb" value="Application LB&#10;Multi-AZ&#10;Health Checks" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#8C4FFF;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.application_load_balancer;" vertex="1" parent="1">
          <mxGeometry x="680" y="340" width="35" height="35" as="geometry"/>
        </mxCell>'''
        
        # Agregar microservicios dinámicamente
        x_positions = [500, 650, 800, 950, 1100]
        y_position = 420
        
        service_xml = ""
        connection_xml = ""
        
        # Verificar que microservices sea un diccionario
        if isinstance(microservices, dict):
            for i, (service_name, service_config) in enumerate(microservices.items()):
                if i >= len(x_positions):
                    break
                    
                x_pos = x_positions[i]
                
                # Verificar que service_config sea un diccionario
                if not isinstance(service_config, dict):
                    service_config = {}
                
                # Extraer configuración con valores por defecto
                compute = service_config.get("compute", {})
                scaling = service_config.get("scaling", {})
                
                cpu = compute.get("cpu", 2048) // 1024
                memory = compute.get("memory", 4096) // 1024
                min_cap = scaling.get("min_capacity", 2)
                max_cap = scaling.get("max_capacity", 10)
                
                service_xml += f'''
        <!-- {service_name.title()} Service -->
        <mxCell id="{service_name}" value="{service_name.title()}&#10;{cpu}vCPU/{memory}GB&#10;Scale: {min_cap}-{max_cap}" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="{x_pos}" y="{y_position}" width="35" height="35" as="geometry"/>
        </mxCell>'''
                
                # Conexión desde ALB
                connection_xml += f'''
        <mxCell id="alb_to_{service_name}" style="endArrow=classic;html=1;rounded=0;strokeColor=#4CAF50;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="alb" target="{service_name}"/>'''
        
        # Continuar con el resto del XML
        xml_content += service_xml + '''
        
        <!-- Data Layer -->
        <mxCell id="datazone" value="Data Layer - Multi-AZ with Backup &amp; Encryption" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4EC;strokeColor=#E91E63;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="450" y="530" width="500" height="150" as="geometry"/>
        </mxCell>'''
        
        # Agregar servicios de datos dinámicamente
        data_services = {
            "rds": {"name": "RDS PostgreSQL", "x": 500, "icon": "rds"},
            "redis": {"name": "ElastiCache Redis", "x": 650, "icon": "elasticache"}, 
            "s3": {"name": "S3 Documents", "x": 800, "icon": "s3"}
        }
        
        for service_id, service_info in data_services.items():
            service_config = aws_services.get(f"{service_id}_primary", aws_services.get(f"{service_id}_cluster", aws_services.get(f"{service_id}_documents", {})))
            
            # Configuración específica por servicio
            if service_id == "rds":
                instance_class = service_config.get("instance_class", "db.r6g.2xlarge")
                multi_az = "Multi-AZ" if service_config.get("high_availability", {}).get("multi_az", True) else "Single-AZ"
                label = f"{service_info['name']}&#10;{instance_class}&#10;{multi_az}&#10;35-day backup"
            elif service_id == "redis":
                num_nodes = service_config.get("cluster", {}).get("num_nodes", 3)
                label = f"{service_info['name']}&#10;{num_nodes} nodes&#10;Cluster Mode&#10;24h TTL"
            else:  # s3
                storage_class = service_config.get("storage", {}).get("storage_class", "intelligent_tiering")
                label = f"{service_info['name']}&#10;{storage_class.title()}&#10;Lifecycle Rules&#10;Encryption"
            
            xml_content += f'''
        <mxCell id="{service_id}" value="{label}" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.{service_info['icon']};" vertex="1" parent="1">
          <mxGeometry x="{service_info['x']}" y="570" width="35" height="35" as="geometry"/>
        </mxCell>'''
        
        # AI/ML y otros servicios
        xml_content += '''
        
        <!-- AI/ML Zone -->
        <mxCell id="aizone" value="AI/ML Services - OCR &amp; Classification" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F3E5F5;strokeColor=#9C27B0;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="1000" y="530" width="200" height="150" as="geometry"/>
        </mxCell>
        
        <!-- Textract -->
        <mxCell id="textract" value="Textract&#10;OCR Service&#10;&gt;95% Accuracy&#10;Forms + Tables" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.textract;" vertex="1" parent="1">
          <mxGeometry x="1080" y="570" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Integration Zone -->
        <mxCell id="integrationzone" value="Event-Driven Integration - 10K events/hour" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF8E1;strokeColor=#FFC107;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="450" y="720" width="400" height="120" as="geometry"/>
        </mxCell>
        
        <!-- SQS -->
        <mxCell id="sqs" value="SQS&#10;FIFO Queue&#10;5min Visibility&#10;DLQ Enabled" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sqs;" vertex="1" parent="1">
          <mxGeometry x="500" y="760" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- SNS -->
        <mxCell id="sns" value="SNS&#10;Notifications&#10;Multi-channel&#10;Email/SMS" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sns;" vertex="1" parent="1">
          <mxGeometry x="650" y="760" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- EventBridge -->
        <mxCell id="eventbridge" value="EventBridge&#10;Custom Bus&#10;Event Rules&#10;Targets" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.eventbridge;" vertex="1" parent="1">
          <mxGeometry x="800" y="760" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Monitoring Zone -->
        <mxCell id="monitoringzone" value="Monitoring &amp; Observability - 99.9% SLA" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ECEFF1;strokeColor=#607D8B;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="900" y="720" width="300" height="120" as="geometry"/>
        </mxCell>
        
        <!-- CloudWatch -->
        <mxCell id="cloudwatch" value="CloudWatch&#10;Metrics/Logs&#10;Custom Alarms&#10;Dashboards" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F34482;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudwatch;" vertex="1" parent="1">
          <mxGeometry x="950" y="760" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Performance KPIs -->
        <mxCell id="kpis" value="Performance KPIs&#10;• Response Time: &lt;500ms&#10;• Throughput: 10K invoices/hour&#10;• OCR Accuracy: &gt;95%&#10;• Availability: &gt;99.9%&#10;• Cost: $8,650/month" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1F5FE;strokeColor=#0277BD;fontSize=9;align=left;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="1250" y="300" width="250" height="120" as="geometry"/>
        </mxCell>
        
        <!-- Implementation Timeline -->
        <mxCell id="timeline" value="Implementation Phases&#10;Phase 1: Infrastructure (Weeks 1-8)&#10;Phase 2: Microservices (Weeks 9-16)&#10;Phase 3: AI/ML Integration (Weeks 17-22)&#10;Phase 4: Frontend &amp; APIs (Weeks 23-26)&#10;Phase 5: Go-Live &amp; Optimization (Weeks 27-30)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFEBEE;strokeColor=#C62828;fontSize=9;align=left;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="1250" y="450" width="250" height="120" as="geometry"/>
        </mxCell>'''
        
        # Agregar todas las conexiones
        xml_content += connection_xml + '''
        
        <!-- Main Flow Connections -->
        <mxCell id="c1" style="endArrow=classic;html=1;rounded=0;strokeColor=#1976D2;strokeWidth=3;fontSize=8;" edge="1" parent="1" source="users" target="cloudfront">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="400" y="400" as="sourcePoint"/>
            <mxPoint x="450" y="350" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="c2" style="endArrow=classic;html=1;rounded=0;strokeColor=#FF9800;strokeWidth=3;fontSize=8;" edge="1" parent="1" source="cloudfront" target="waf"/>
        <mxCell id="c3" style="endArrow=classic;html=1;rounded=0;strokeColor=#FF9800;strokeWidth=3;fontSize=8;" edge="1" parent="1" source="waf" target="api"/>
        <mxCell id="c4" style="endArrow=classic;html=1;rounded=0;strokeColor=#FF9800;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="api" target="cognito"/>
        <mxCell id="c5" style="endArrow=classic;html=1;rounded=0;strokeColor=#4CAF50;strokeWidth=3;fontSize=8;" edge="1" parent="1" source="api" target="alb"/>
        
        <!-- Data Connections -->
        <mxCell id="d1" style="endArrow=classic;html=1;rounded=0;strokeColor=#9C27B0;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="product_service" target="redis"/>
        <mxCell id="d2" style="endArrow=classic;html=1;rounded=0;strokeColor=#9C27B0;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="redis" target="rds"/>
        <mxCell id="d3" style="endArrow=classic;html=1;rounded=0;strokeColor=#E91E63;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="ocr_service" target="s3"/>
        <mxCell id="d4" style="endArrow=classic;html=1;rounded=0;strokeColor=#E91E63;strokeWidth=2;fontSize=8;" edge="1" source="ocr_service" target="textract" parent="1"/>
        
        <!-- External Connections -->
        <mxCell id="e1" style="endArrow=classic;html=1;rounded=0;strokeColor=#607D8B;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="product_service" target="dian"/>
        <mxCell id="e2" style="endArrow=classic;html=1;rounded=0;strokeColor=#795548;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="sftp" target="s3"/>
        
        <!-- Integration Connections -->
        <mxCell id="i1" style="endArrow=classic;html=1;rounded=0;strokeColor=#FFC107;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="invoice_service" target="eventbridge"/>
        <mxCell id="i2" style="endArrow=classic;html=1;rounded=0;strokeColor=#FFC107;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="eventbridge" target="sqs"/>
        <mxCell id="i3" style="endArrow=classic;html=1;rounded=0;strokeColor=#FFC107;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="sqs" target="sns"/>
        
        <!-- Monitoring Connections -->
        <mxCell id="m1" style="endArrow=classic;html=1;rounded=0;strokeColor=#795548;strokeWidth=1;fontSize=8;dashed=1;" edge="1" parent="1" source="invoice_service" target="cloudwatch"/>
        <mxCell id="m2" style="endArrow=classic;html=1;rounded=0;strokeColor=#795548;strokeWidth=1;fontSize=8;dashed=1;" edge="1" parent="1" source="product_service" target="cloudwatch"/>
        <mxCell id="m3" style="endArrow=classic;html=1;rounded=0;strokeColor=#795548;strokeWidth=1;fontSize=8;dashed=1;" edge="1" parent="1" source="rds" target="cloudwatch"/>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
        
        # Guardar archivo
        output_file = f"{self.output_dir}/drawio/{project_name.lower()}_unified_architecture.drawio"
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        
        return output_file
