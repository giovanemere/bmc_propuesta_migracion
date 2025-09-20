#!/usr/bin/env python3
"""
Enhanced Draw.io Generator - Genera Draw.io completos equivalentes a PNG
"""

import os
from typing import Dict, Any

class EnhancedDrawioGenerator:
    """Generador mejorado de Draw.io con contenido completo"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str = "output"):
        self.config = config
        self.output_dir = output_dir
        
    def generate_complete_architecture_drawio(self, project_name: str) -> str:
        """Genera Draw.io completo de arquitectura principal"""
        
        microservices = self.config.get("microservices", {})
        aws_services = self.config.get("aws_services", {})
        performance_kpis = self.config.get("performance_kpis", {})
        
        # Generar servicios dinámicamente
        services_xml = self._generate_microservices_xml(microservices)
        data_services_xml = self._generate_data_services_xml(aws_services)
        connections_xml = self._generate_connections_xml(microservices, aws_services)
        kpis_xml = self._generate_kpis_xml(performance_kpis)
        
        xml_content = f'''<mxfile host="app.diagrams.net">
  <diagram name="{project_name} - Complete Architecture" id="complete_arch">
    <mxGraphModel dx="2000" dy="1200" grid="1" gridSize="10">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Header -->
        <mxCell id="header" value="{project_name} - Sistema Regulatorio AWS" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=none;fontColor=#FFFFFF;fontSize=20;fontStyle=1;align=center;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1800" height="60" as="geometry"/>
        </mxCell>
        
        <!-- On-Premise -->
        <mxCell id="onprem" value="On-Premise / External Systems" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFEBEE;strokeColor=#D32F2F;strokeWidth=3;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=15;dashed=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="100" width="350" height="200" as="geometry"/>
        </mxCell>
        
        <!-- Users -->
        <mxCell id="users" value="BMC Users&#10;Reguladores&#10;10K concurrent" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;shape=mxgraph.aws4.users;" vertex="1" parent="1">
          <mxGeometry x="100" y="150" width="50" height="50" as="geometry"/>
        </mxCell>
        
        <!-- DIAN API -->
        <mxCell id="dian" value="DIAN API&#10;Clasificaciones&#10;Regulatorias" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#607D8B;strokeColor=none;shape=mxgraph.aws4.internet_gateway;" vertex="1" parent="1">
          <mxGeometry x="250" y="150" width="50" height="50" as="geometry"/>
        </mxCell>
        
        <!-- SFTP Systems -->
        <mxCell id="sftp" value="SFTP Systems&#10;Intercambio&#10;Regulatorio" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#795548;strokeColor=none;shape=mxgraph.aws4.storage_gateway;" vertex="1" parent="1">
          <mxGeometry x="175" y="230" width="50" height="50" as="geometry"/>
        </mxCell>
        
        <!-- AWS Cloud -->
        <mxCell id="aws" value="AWS Cloud - us-east-1 (Multi-AZ)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;strokeWidth=4;fontSize=16;fontStyle=1;verticalAlign=top;spacingTop=20;" vertex="1" parent="1">
          <mxGeometry x="450" y="100" width="1400" height="900" as="geometry"/>
        </mxCell>
        
        <!-- Edge Security -->
        <mxCell id="edge" value="Edge Security &amp; CDN Layer" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#FF9800;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="500" y="150" width="600" height="120" as="geometry"/>
        </mxCell>
        
        <!-- CloudFront -->
        <mxCell id="cloudfront" value="CloudFront&#10;Global CDN&#10;SSL Termination&#10;Edge Locations" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.cloudfront;" vertex="1" parent="1">
          <mxGeometry x="550" y="190" width="45" height="45" as="geometry"/>
        </mxCell>
        
        <!-- WAF -->
        <mxCell id="waf" value="AWS WAF&#10;DDoS Protection&#10;Rate Limiting&#10;Geo Blocking" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;shape=mxgraph.aws4.waf;" vertex="1" parent="1">
          <mxGeometry x="700" y="190" width="45" height="45" as="geometry"/>
        </mxCell>
        
        <!-- API Gateway -->
        <mxCell id="api" value="API Gateway&#10;REST + GraphQL&#10;1K req/s&#10;JWT Validation" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;shape=mxgraph.aws4.api_gateway;" vertex="1" parent="1">
          <mxGeometry x="850" y="190" width="45" height="45" as="geometry"/>
        </mxCell>
        
        <!-- Cognito -->
        <mxCell id="cognito" value="Cognito&#10;User Pool&#10;MFA Enabled&#10;Regulatory Auth" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;shape=mxgraph.aws4.cognito;" vertex="1" parent="1">
          <mxGeometry x="1000" y="190" width="45" height="45" as="geometry"/>
        </mxCell>
        
        <!-- Application Layer -->
        <mxCell id="app_layer" value="Application Layer - ECS Fargate Auto Scaling" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#4CAF50;strokeWidth=2;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=15;" vertex="1" parent="1">
          <mxGeometry x="500" y="300" width="1000" height="250" as="geometry"/>
        </mxCell>
        
        <!-- ALB -->
        <mxCell id="alb" value="Application LB&#10;Multi-AZ&#10;Health Checks&#10;Target Groups" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#8C4FFF;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;shape=mxgraph.aws4.application_load_balancer;" vertex="1" parent="1">
          <mxGeometry x="750" y="350" width="45" height="45" as="geometry"/>
        </mxCell>
        
        {services_xml}
        
        <!-- Data Layer -->
        <mxCell id="data_layer" value="Data Layer - Multi-AZ with Backup &amp; Encryption" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4EC;strokeColor=#E91E63;strokeWidth=2;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=15;" vertex="1" parent="1">
          <mxGeometry x="500" y="580" width="800" height="200" as="geometry"/>
        </mxCell>
        
        {data_services_xml}
        
        <!-- AI/ML Layer -->
        <mxCell id="ai_layer" value="AI/ML Services - OCR &amp; Classification" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F3E5F5;strokeColor=#9C27B0;strokeWidth=2;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=15;" vertex="1" parent="1">
          <mxGeometry x="1350" y="580" width="300" height="200" as="geometry"/>
        </mxCell>
        
        <!-- Textract -->
        <mxCell id="textract" value="Amazon Textract&#10;OCR Service&#10;&gt;95% Accuracy&#10;Forms + Tables&#10;Invoice Processing" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;shape=mxgraph.aws4.textract;" vertex="1" parent="1">
          <mxGeometry x="1450" y="630" width="50" height="50" as="geometry"/>
        </mxCell>
        
        <!-- Integration Layer -->
        <mxCell id="integration" value="Event-Driven Integration - 10K events/hour" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF8E1;strokeColor=#FFC107;strokeWidth=2;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=15;" vertex="1" parent="1">
          <mxGeometry x="500" y="810" width="600" height="150" as="geometry"/>
        </mxCell>
        
        <!-- SQS -->
        <mxCell id="sqs" value="SQS FIFO&#10;Processing Queue&#10;5min Visibility&#10;DLQ Enabled" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;shape=mxgraph.aws4.sqs;" vertex="1" parent="1">
          <mxGeometry x="550" y="860" width="45" height="45" as="geometry"/>
        </mxCell>
        
        <!-- SNS -->
        <mxCell id="sns" value="SNS Topics&#10;Notifications&#10;Multi-channel&#10;Email/SMS" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;shape=mxgraph.aws4.sns;" vertex="1" parent="1">
          <mxGeometry x="700" y="860" width="45" height="45" as="geometry"/>
        </mxCell>
        
        <!-- EventBridge -->
        <mxCell id="eventbridge" value="EventBridge&#10;Custom Bus&#10;Event Rules&#10;Regulatory Events" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;shape=mxgraph.aws4.eventbridge;" vertex="1" parent="1">
          <mxGeometry x="850" y="860" width="45" height="45" as="geometry"/>
        </mxCell>
        
        <!-- Monitoring -->
        <mxCell id="monitoring" value="Monitoring &amp; Observability - 99.9% SLA" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ECEFF1;strokeColor=#607D8B;strokeWidth=2;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=15;" vertex="1" parent="1">
          <mxGeometry x="1150" y="810" width="400" height="150" as="geometry"/>
        </mxCell>
        
        <!-- CloudWatch -->
        <mxCell id="cloudwatch" value="CloudWatch&#10;Custom Metrics&#10;Regulatory Alarms&#10;Dashboards" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F34482;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;shape=mxgraph.aws4.cloudwatch;" vertex="1" parent="1">
          <mxGeometry x="1200" y="860" width="45" height="45" as="geometry"/>
        </mxCell>
        
        {kpis_xml}
        
        {connections_xml}
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
        
        output_file = f"{self.output_dir}/drawio/{project_name.lower()}_complete_architecture.drawio"
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        
        return output_file
    
    def _generate_microservices_xml(self, microservices: Dict) -> str:
        """Genera XML para microservicios"""
        
        services_xml = ""
        x_positions = [550, 700, 850, 1000, 1150, 1300]
        y_position = 420
        
        for i, (service_name, service_config) in enumerate(microservices.items()):
            if i >= len(x_positions):
                break
                
            x_pos = x_positions[i]
            
            # Extraer configuración
            compute = service_config.get("compute", {})
            scaling = service_config.get("scaling", {})
            business_function = service_config.get("business_function", "")
            
            cpu = compute.get("cpu", 2048) // 1024
            memory = compute.get("memory", 4096) // 1024
            min_cap = scaling.get("min_capacity", 2)
            max_cap = scaling.get("max_capacity", 10)
            
            # Truncar función de negocio
            short_function = business_function[:30] + "..." if len(business_function) > 30 else business_function
            
            services_xml += f'''
        <!-- {service_name.title()} Service -->
        <mxCell id="{service_name}" value="{service_name.title()}&#10;{cpu}vCPU/{memory}GB&#10;Scale: {min_cap}-{max_cap}&#10;{short_function}" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;shape=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="{x_pos}" y="{y_position}" width="50" height="50" as="geometry"/>
        </mxCell>'''
        
        return services_xml
    
    def _generate_data_services_xml(self, aws_services: Dict) -> str:
        """Genera XML para servicios de datos"""
        
        data_xml = ""
        x_positions = [550, 700, 850, 1000, 1150]
        y_position = 630
        
        service_mapping = {
            "rds": {"icon": "rds", "name": "RDS PostgreSQL"},
            "redis": {"icon": "elasticache", "name": "ElastiCache Redis"},
            "s3": {"icon": "s3", "name": "S3 Documents"},
            "redshift": {"icon": "redshift", "name": "Redshift Analytics"}
        }
        
        i = 0
        for service_key, service_config in aws_services.items():
            if i >= len(x_positions):
                break
                
            # Determinar tipo de servicio
            service_type = service_config.get("type", "")
            if service_type in service_mapping:
                mapping = service_mapping[service_type]
                x_pos = x_positions[i]
                
                business_purpose = service_config.get("business_purpose", "")
                short_purpose = business_purpose[:40] + "..." if len(business_purpose) > 40 else business_purpose
                
                data_xml += f'''
        <!-- {mapping['name']} -->
        <mxCell id="{service_key}" value="{mapping['name']}&#10;{short_purpose}" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;shape=mxgraph.aws4.{mapping['icon']};" vertex="1" parent="1">
          <mxGeometry x="{x_pos}" y="{y_position}" width="50" height="50" as="geometry"/>
        </mxCell>'''
                
                i += 1
        
        return data_xml
    
    def _generate_connections_xml(self, microservices: Dict, aws_services: Dict) -> str:
        """Genera XML para conexiones"""
        
        connections = """
        <!-- Main Flow Connections -->
        <mxCell id="c1" style="endArrow=classic;html=1;strokeColor=#1976D2;strokeWidth=3;fontSize=10;" edge="1" parent="1" source="users" target="cloudfront">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="400" y="400" as="sourcePoint"/>
            <mxPoint x="450" y="350" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="c2" style="endArrow=classic;html=1;strokeColor=#FF9800;strokeWidth=3;" edge="1" parent="1" source="cloudfront" target="waf"/>
        <mxCell id="c3" style="endArrow=classic;html=1;strokeColor=#FF9800;strokeWidth=3;" edge="1" parent="1" source="waf" target="api"/>
        <mxCell id="c4" style="endArrow=classic;html=1;strokeColor=#FF9800;strokeWidth=2;" edge="1" parent="1" source="api" target="cognito"/>
        <mxCell id="c5" style="endArrow=classic;html=1;strokeColor=#4CAF50;strokeWidth=3;" edge="1" parent="1" source="api" target="alb"/>
        
        <!-- External Connections -->
        <mxCell id="e1" style="endArrow=classic;html=1;strokeColor=#607D8B;strokeWidth=2;dashed=1;" edge="1" parent="1" source="dian" target="api"/>
        <mxCell id="e2" style="endArrow=classic;html=1;strokeColor=#795548;strokeWidth=2;dashed=1;" edge="1" parent="1" source="sftp" target="s3_documents"/>
        
        <!-- Integration Connections -->
        <mxCell id="i1" style="endArrow=classic;html=1;strokeColor=#FFC107;strokeWidth=2;" edge="1" parent="1" source="invoice_service" target="eventbridge"/>
        <mxCell id="i2" style="endArrow=classic;html=1;strokeColor=#FFC107;strokeWidth=2;" edge="1" parent="1" source="eventbridge" target="sqs"/>
        <mxCell id="i3" style="endArrow=classic;html=1;strokeColor=#FFC107;strokeWidth=2;" edge="1" parent="1" source="sqs" target="sns"/>
        
        <!-- Monitoring Connections -->
        <mxCell id="m1" style="endArrow=classic;html=1;strokeColor=#795548;strokeWidth=1;dashed=1;" edge="1" parent="1" source="invoice_service" target="cloudwatch"/>
        <mxCell id="m2" style="endArrow=classic;html=1;strokeColor=#795548;strokeWidth=1;dashed=1;" edge="1" parent="1" source="product_service" target="cloudwatch"/>"""
        
        return connections
    
    def _generate_kpis_xml(self, performance_kpis: Dict) -> str:
        """Genera XML para KPIs"""
        
        throughput = performance_kpis.get("throughput", {})
        accuracy = performance_kpis.get("accuracy", {})
        
        kpis_text = "Performance KPIs\\n"
        if throughput:
            kpis_text += f"• Products: {throughput.get('products_database', 'N/A')}\\n"
            kpis_text += f"• Categories: {throughput.get('categories', 'N/A')}\\n"
            kpis_text += f"• Processing: {throughput.get('invoices_per_hour', 'N/A')}/hour\\n"
        
        if accuracy:
            kpis_text += f"• OCR Accuracy: {accuracy.get('ocr_processing', 'N/A')}\\n"
            kpis_text += f"• Matching: {accuracy.get('product_matching', 'N/A')}\\n"
        
        return f'''
        <!-- Performance KPIs -->
        <mxCell id="kpis" value="{kpis_text}" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1F5FE;strokeColor=#0277BD;fontSize=11;align=left;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="1700" y="300" width="200" height="150" as="geometry"/>
        </mxCell>'''
