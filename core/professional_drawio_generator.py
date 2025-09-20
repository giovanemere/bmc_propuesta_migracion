#!/usr/bin/env python3
"""
Professional Draw.io Generator - Versión profesional con plugins y mejores características
"""

import os
from typing import Dict, Any

class ProfessionalDrawioGenerator:
    """Generador profesional de Draw.io con características avanzadas"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str = "output"):
        self.config = config
        self.output_dir = output_dir
        
        # Configuración profesional
        self.aws_colors = {
            "orange": "#FF9900",
            "blue": "#232F3E", 
            "light_blue": "#4B92DB",
            "green": "#7AA116",
            "red": "#D13212",
            "purple": "#9D5AAE"
        }
        
        self.service_categories = {
            "compute": {"color": "#FF9900", "icon_prefix": "compute"},
            "database": {"color": "#3F48CC", "icon_prefix": "database"},
            "storage": {"color": "#7AA116", "icon_prefix": "storage"},
            "network": {"color": "#9D5AAE", "icon_prefix": "network"},
            "security": {"color": "#D13212", "icon_prefix": "security"},
            "ml": {"color": "#01A88D", "icon_prefix": "ml"}
        }
    
    def generate_professional_architecture(self, project_name: str) -> str:
        """Genera arquitectura profesional completa"""
        
        # Extraer configuración
        microservices = self.config.get("microservices", {})
        aws_services = self.config.get("aws_services", {})
        performance_kpis = self.config.get("performance_kpis", {})
        project_info = self.config.get("project", {})
        
        # Generar componentes
        header_xml = self._generate_professional_header(project_name, project_info)
        onprem_xml = self._generate_onpremise_section()
        aws_cloud_xml = self._generate_aws_cloud_container()
        edge_layer_xml = self._generate_edge_security_layer()
        app_layer_xml = self._generate_application_layer(microservices)
        data_layer_xml = self._generate_data_layer(aws_services)
        integration_xml = self._generate_integration_layer()
        monitoring_xml = self._generate_monitoring_layer()
        kpis_xml = self._generate_professional_kpis(performance_kpis)
        connections_xml = self._generate_professional_connections()
        
        # Ensamblar XML completo
        xml_content = f'''<mxfile host="app.diagrams.net" modified="{self._get_timestamp()}" agent="BMC Professional Generator" version="22.1.11" etag="professional-v2.0">
  <diagram name="{project_name} - Professional Architecture" id="professional_arch">
    <mxGraphModel dx="2200" dy="1400" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="2000" pageHeight="1400" background="#FFFFFF">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        {header_xml}
        {onprem_xml}
        {aws_cloud_xml}
        {edge_layer_xml}
        {app_layer_xml}
        {data_layer_xml}
        {integration_xml}
        {monitoring_xml}
        {kpis_xml}
        {connections_xml}
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
        
        # Guardar archivo
        output_file = f"{self.output_dir}/drawio/{project_name.lower()}_professional_architecture.drawio"
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        
        return output_file
    
    def _generate_professional_header(self, project_name: str, project_info: Dict) -> str:
        """Genera header profesional con información del proyecto"""
        
        description = project_info.get("description", "Sistema AWS")
        version = project_info.get("version", "2.0.0")
        
        return f'''
        <!-- Professional Header -->
        <mxCell id="main_header" value="{project_name}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=none;fontColor=#FFFFFF;fontSize=24;fontStyle=1;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1900" height="70" as="geometry"/>
        </mxCell>
        
        <mxCell id="sub_header" value="{description} | Version {version}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FF9900;strokeColor=none;fontColor=#FFFFFF;fontSize=14;fontStyle=0;align=center;" vertex="1" parent="1">
          <mxGeometry x="50" y="90" width="1900" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Legend -->
        <mxCell id="legend" value="🏛️ Regulatorio | 🔒 Seguridad | ⚡ Performance | 📊 Analytics" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#4CAF50;fontSize=12;align=center;" vertex="1" parent="1">
          <mxGeometry x="50" y="130" width="600" height="30" as="geometry"/>
        </mxCell>'''
    
    def _generate_onpremise_section(self) -> str:
        """Genera sección on-premise profesional"""
        
        return '''
        <!-- On-Premise Professional -->
        <mxCell id="onprem_container" value="On-Premise &amp; External Systems" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFEBEE;strokeColor=#D32F2F;strokeWidth=3;fontSize=16;fontStyle=1;verticalAlign=top;spacingTop=20;shadow=1;glass=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="180" width="400" height="300" as="geometry"/>
        </mxCell>
        
        <!-- Professional Users -->
        <mxCell id="bmc_users" value="BMC Users&lt;br&gt;&lt;b&gt;Reguladores&lt;/b&gt;&lt;br&gt;10K concurrent&lt;br&gt;Multi-device" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=11;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.users;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="100" y="230" width="60" height="60" as="geometry"/>
        </mxCell>
        
        <!-- DIAN API Professional -->
        <mxCell id="dian_api" value="DIAN API&lt;br&gt;&lt;b&gt;Tax Authority&lt;/b&gt;&lt;br&gt;Clasificaciones&lt;br&gt;1K req/hour" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=11;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.internet_gateway;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="300" y="230" width="60" height="60" as="geometry"/>
        </mxCell>
        
        <!-- SFTP Professional -->
        <mxCell id="sftp_systems" value="SFTP Systems&lt;br&gt;&lt;b&gt;Regulatory&lt;/b&gt;&lt;br&gt;Batch Transfer&lt;br&gt;Nightly Sync" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=11;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.storage_gateway;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="200" y="350" width="60" height="60" as="geometry"/>
        </mxCell>'''
    
    def _generate_aws_cloud_container(self) -> str:
        """Genera contenedor AWS Cloud profesional"""
        
        return '''
        <!-- AWS Cloud Professional Container -->
        <mxCell id="aws_cloud" value="AWS Cloud - us-east-1 (Multi-AZ Production)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;strokeWidth=4;fontSize=18;fontStyle=1;verticalAlign=top;spacingTop=25;shadow=1;glass=1;" vertex="1" parent="1">
          <mxGeometry x="500" y="180" width="1450" height="1100" as="geometry"/>
        </mxCell>
        
        <!-- AWS Logo -->
        <mxCell id="aws_logo" value="AWS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FF9900;strokeColor=none;fontColor=#FFFFFF;fontSize=20;fontStyle=1;align=center;" vertex="1" parent="1">
          <mxGeometry x="1800" y="200" width="80" height="40" as="geometry"/>
        </mxCell>'''
    
    def _generate_edge_security_layer(self) -> str:
        """Genera capa de seguridad edge profesional"""
        
        return '''
        <!-- Edge Security Professional Layer -->
        <mxCell id="edge_security" value="Edge Security &amp; CDN Layer - Global Protection" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#FF9800;strokeWidth=3;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=20;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="550" y="250" width="800" height="150" as="geometry"/>
        </mxCell>
        
        <!-- CloudFront Professional -->
        <mxCell id="cloudfront_pro" value="CloudFront&lt;br&gt;&lt;b&gt;Global CDN&lt;/b&gt;&lt;br&gt;SSL/TLS&lt;br&gt;Edge Locations&lt;br&gt;Cache Rules" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.cloudfront;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="600" y="300" width="60" height="60" as="geometry"/>
        </mxCell>
        
        <!-- WAF Professional -->
        <mxCell id="waf_pro" value="AWS WAF&lt;br&gt;&lt;b&gt;Web Firewall&lt;/b&gt;&lt;br&gt;DDoS Protection&lt;br&gt;Rate: 2K req/s&lt;br&gt;Geo Blocking" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.waf;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="750" y="300" width="60" height="60" as="geometry"/>
        </mxCell>
        
        <!-- API Gateway Professional -->
        <mxCell id="api_gateway_pro" value="API Gateway&lt;br&gt;&lt;b&gt;REST + GraphQL&lt;/b&gt;&lt;br&gt;JWT Validation&lt;br&gt;1K req/s&lt;br&gt;Caching" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.api_gateway;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="900" y="300" width="60" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Cognito Professional -->
        <mxCell id="cognito_pro" value="Cognito&lt;br&gt;&lt;b&gt;User Pool&lt;/b&gt;&lt;br&gt;MFA: TOTP+SMS&lt;br&gt;Regulatory Auth&lt;br&gt;Session Mgmt" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.cognito;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1050" y="300" width="60" height="60" as="geometry"/>
        </mxCell>'''
    
    def _generate_application_layer(self, microservices: Dict) -> str:
        """Genera capa de aplicación profesional"""
        
        app_layer = '''
        <!-- Application Layer Professional -->
        <mxCell id="app_layer_pro" value="Application Layer - ECS Fargate Auto Scaling (Production Ready)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#4CAF50;strokeWidth=3;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=20;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="550" y="430" width="1200" height="300" as="geometry"/>
        </mxCell>
        
        <!-- ALB Professional -->
        <mxCell id="alb_pro" value="Application LB&lt;br&gt;&lt;b&gt;Multi-AZ&lt;/b&gt;&lt;br&gt;Health Checks&lt;br&gt;Target Groups&lt;br&gt;SSL Termination" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#8C4FFF;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.application_load_balancer;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="800" y="480" width="60" height="60" as="geometry"/>
        </mxCell>'''
        
        # Generar microservicios profesionales
        x_positions = [600, 750, 900, 1050, 1200, 1350]
        y_position = 580
        
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
            
            # Función de negocio corta
            short_function = business_function.split()[0:3]
            short_function = " ".join(short_function) if short_function else "Service"
            
            # Determinar color por tipo de servicio
            color = "#D05C17"  # Default orange
            if "ocr" in service_name.lower():
                color = "#01A88D"  # ML green
            elif "commission" in service_name.lower():
                color = "#9D5AAE"  # Purple
            elif "certificate" in service_name.lower():
                color = "#D13212"  # Red
            
            app_layer += f'''
        <!-- {service_name.title()} Professional -->
        <mxCell id="{service_name}_pro" value="{service_name.title()}&lt;br&gt;&lt;b&gt;{cpu}vCPU/{memory}GB&lt;/b&gt;&lt;br&gt;Scale: {min_cap}-{max_cap}&lt;br&gt;{short_function}&lt;br&gt;Health: /health" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor={color};strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.fargate;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="{x_pos}" y="{y_position}" width="60" height="60" as="geometry"/>
        </mxCell>'''
        
        return app_layer
    
    def _generate_data_layer(self, aws_services: Dict) -> str:
        """Genera capa de datos profesional"""
        
        data_layer = '''
        <!-- Data Layer Professional -->
        <mxCell id="data_layer_pro" value="Data Layer - Multi-AZ with Backup, Encryption &amp; Compliance" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4EC;strokeColor=#E91E63;strokeWidth=3;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=20;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="550" y="760" width="900" height="200" as="geometry"/>
        </mxCell>'''
        
        # Servicios de datos profesionales
        x_positions = [600, 750, 900, 1050, 1200]
        y_position = 820
        
        service_configs = {
            "rds": {
                "name": "RDS PostgreSQL",
                "icon": "rds",
                "details": "Multi-AZ&lt;br&gt;60M Products&lt;br&gt;35-day Backup&lt;br&gt;Encryption"
            },
            "redis": {
                "name": "ElastiCache Redis", 
                "icon": "elasticache",
                "details": "3-node Cluster&lt;br&gt;24h TTL&lt;br&gt;&gt;95% Hit Ratio&lt;br&gt;Failover"
            },
            "s3": {
                "name": "S3 Documents",
                "icon": "s3", 
                "details": "Intelligent Tier&lt;br&gt;Lifecycle Rules&lt;br&gt;7-year Retention&lt;br&gt;Compliance"
            },
            "redshift": {
                "name": "Redshift DW",
                "icon": "redshift",
                "details": "Analytics&lt;br&gt;Regulatory Reports&lt;br&gt;DIAN Compliance&lt;br&gt;ETL Pipeline"
            }
        }
        
        i = 0
        for service_key, service_config in aws_services.items():
            if i >= len(x_positions):
                break
                
            service_type = service_config.get("type", "")
            if service_type in service_configs:
                config = service_configs[service_type]
                x_pos = x_positions[i]
                
                data_layer += f'''
        <!-- {config['name']} Professional -->
        <mxCell id="{service_key}_pro" value="{config['name']}&lt;br&gt;&lt;b&gt;Production&lt;/b&gt;&lt;br&gt;{config['details']}" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.{config['icon']};shadow=1;" vertex="1" parent="1">
          <mxGeometry x="{x_pos}" y="{y_position}" width="60" height="60" as="geometry"/>
        </mxCell>'''
                
                i += 1
        
    def _generate_integration_layer(self) -> str:
        """Genera capa de integración profesional"""
        
        return '''
        <!-- Integration Layer Professional -->
        <mxCell id="integration_pro" value="Event-Driven Integration - 10K events/hour (Regulatory Compliant)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF8E1;strokeColor=#FFC107;strokeWidth=3;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=20;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="550" y="990" width="600" height="150" as="geometry"/>
        </mxCell>
        
        <!-- SQS Professional -->
        <mxCell id="sqs_pro" value="SQS FIFO&lt;br&gt;&lt;b&gt;Processing Queue&lt;/b&gt;&lt;br&gt;5min Visibility&lt;br&gt;DLQ Enabled&lt;br&gt;Batch Processing" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.sqs;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="600" y="1040" width="60" height="60" as="geometry"/>
        </mxCell>
        
        <!-- SNS Professional -->
        <mxCell id="sns_pro" value="SNS Topics&lt;br&gt;&lt;b&gt;Notifications&lt;/b&gt;&lt;br&gt;Multi-channel&lt;br&gt;Email/SMS&lt;br&gt;Webhooks" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.sns;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="750" y="1040" width="60" height="60" as="geometry"/>
        </mxCell>
        
        <!-- EventBridge Professional -->
        <mxCell id="eventbridge_pro" value="EventBridge&lt;br&gt;&lt;b&gt;Custom Bus&lt;/b&gt;&lt;br&gt;Event Rules&lt;br&gt;Regulatory Events&lt;br&gt;Schema Registry" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.eventbridge;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="900" y="1040" width="60" height="60" as="geometry"/>
        </mxCell>'''
    
    def _generate_monitoring_layer(self) -> str:
        """Genera capa de monitoreo profesional"""
        
        return '''
        <!-- Monitoring Layer Professional -->
        <mxCell id="monitoring_pro" value="Monitoring &amp; Observability - 99.9% SLA (Regulatory Compliance)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ECEFF1;strokeColor=#607D8B;strokeWidth=3;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=20;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1200" y="990" width="500" height="150" as="geometry"/>
        </mxCell>
        
        <!-- CloudWatch Professional -->
        <mxCell id="cloudwatch_pro" value="CloudWatch&lt;br&gt;&lt;b&gt;Metrics &amp; Logs&lt;/b&gt;&lt;br&gt;Custom Metrics&lt;br&gt;Regulatory Alarms&lt;br&gt;Dashboards" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F34482;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.cloudwatch;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1250" y="1040" width="60" height="60" as="geometry"/>
        </mxCell>
        
        <!-- X-Ray Professional -->
        <mxCell id="xray_pro" value="X-Ray Tracing&lt;br&gt;&lt;b&gt;Distributed&lt;/b&gt;&lt;br&gt;Service Map&lt;br&gt;Performance&lt;br&gt;Error Analysis" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F34482;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.x_ray;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1400" y="1040" width="60" height="60" as="geometry"/>
        </mxCell>'''
    
    def _generate_professional_kpis(self, performance_kpis: Dict) -> str:
        """Genera KPIs profesionales"""
        
        throughput = performance_kpis.get("throughput", {})
        accuracy = performance_kpis.get("accuracy", {})
        response_times = performance_kpis.get("response_times", {})
        
        kpis_content = "📊 Performance KPIs\\n\\n"
        
        if throughput:
            kpis_content += f"🏛️ REGULATORY:\\n"
            kpis_content += f"• Products: {throughput.get('products_database', 'N/A')}\\n"
            kpis_content += f"• Categories: {throughput.get('categories', 'N/A')}\\n"
            kpis_content += f"• Processing: {throughput.get('invoices_per_hour', 'N/A')}/hour\\n\\n"
        
        if accuracy:
            kpis_content += f"🎯 ACCURACY:\\n"
            kpis_content += f"• OCR: {accuracy.get('ocr_processing', 'N/A')}\\n"
            kpis_content += f"• Matching: {accuracy.get('product_matching', 'N/A')}\\n"
            kpis_content += f"• Compliance: {accuracy.get('regulatory_compliance', 'N/A')}\\n\\n"
        
        if response_times:
            kpis_content += f"⚡ PERFORMANCE:\\n"
            kpis_content += f"• Product Lookup: {response_times.get('product_lookup', 'N/A')}\\n"
            kpis_content += f"• Invoice Process: {response_times.get('invoice_processing', 'N/A')}\\n"
            kpis_content += f"• Certificate Gen: {response_times.get('certificate_generation', 'N/A')}"
        
        return f'''
        <!-- Professional KPIs -->
        <mxCell id="kpis_pro" value="{kpis_content}" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1F5FE;strokeColor=#0277BD;strokeWidth=2;fontSize=10;align=left;verticalAlign=top;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1500" y="430" width="250" height="300" as="geometry"/>
        </mxCell>
        
        <!-- Cost Optimization -->
        <mxCell id="cost_opt" value="💰 COST OPTIMIZATION\\n\\n• Monthly: $8,650\\n• Per Invoice: $0.0009\\n• Reserved Instances: 40%\\n• Spot Instances: 20%\\n• Auto Scaling: Enabled\\n• Cost Alerts: Active" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#4CAF50;strokeWidth=2;fontSize=10;align=left;verticalAlign=top;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1500" y="760" width="250" height="150" as="geometry"/>
        </mxCell>'''
    
    def _generate_professional_connections(self) -> str:
        """Genera conexiones profesionales con etiquetas"""
        
        return '''
        <!-- Professional Connections with Labels -->
        
        <!-- Main User Flow -->
        <mxCell id="conn_user_cf" style="endArrow=classic;html=1;strokeColor=#1976D2;strokeWidth=4;fontSize=10;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="bmc_users" target="cloudfront_pro">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="400" y="400" as="sourcePoint"/>
            <mxPoint x="450" y="350" as="targetPoint"/>
          </mxGeometry>
          <mxCell id="label_user_cf" value="HTTPS\\n10K users" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=9;fontStyle=1;fillColor=#E3F2FD;strokeColor=#1976D2;" vertex="1" connectable="0" parent="conn_user_cf">
            <mxGeometry x="-0.1" y="-1" relative="1" as="geometry">
              <mxPoint as="offset"/>
            </mxGeometry>
          </mxCell>
        </mxCell>
        
        <!-- Security Chain -->
        <mxCell id="conn_cf_waf" style="endArrow=classic;html=1;strokeColor=#FF9800;strokeWidth=3;fontSize=10;" edge="1" parent="1" source="cloudfront_pro" target="waf_pro">
          <mxCell id="label_cf_waf" value="Filter\\nDDoS" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=9;fillColor=#FFF3E0;strokeColor=#FF9800;" vertex="1" connectable="0" parent="conn_cf_waf">
            <mxGeometry x="-0.1" y="-1" relative="1" as="geometry">
              <mxPoint as="offset"/>
            </mxGeometry>
          </mxCell>
        </mxCell>
        
        <mxCell id="conn_waf_api" style="endArrow=classic;html=1;strokeColor=#FF9800;strokeWidth=3;" edge="1" parent="1" source="waf_pro" target="api_gateway_pro">
          <mxCell id="label_waf_api" value="Validate\\nRate Limit" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=9;fillColor=#FFF3E0;strokeColor=#FF9800;" vertex="1" connectable="0" parent="conn_waf_api">
            <mxGeometry x="-0.1" y="-1" relative="1" as="geometry">
              <mxPoint as="offset"/>
            </mxGeometry>
          </mxCell>
        </mxCell>
        
        <mxCell id="conn_api_cognito" style="endArrow=classic;html=1;strokeColor=#D32F2F;strokeWidth=2;dashed=1;" edge="1" parent="1" source="api_gateway_pro" target="cognito_pro">
          <mxCell id="label_api_cognito" value="Auth\\nMFA" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=9;fillColor=#FFEBEE;strokeColor=#D32F2F;" vertex="1" connectable="0" parent="conn_api_cognito">
            <mxGeometry x="-0.1" y="-1" relative="1" as="geometry">
              <mxPoint as="offset"/>
            </mxGeometry>
          </mxCell>
        </mxCell>
        
        <!-- Application Flow -->
        <mxCell id="conn_api_alb" style="endArrow=classic;html=1;strokeColor=#4CAF50;strokeWidth=4;" edge="1" parent="1" source="api_gateway_pro" target="alb_pro">
          <mxCell id="label_api_alb" value="Route\\n1K req/s" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=9;fontStyle=1;fillColor=#E8F5E8;strokeColor=#4CAF50;" vertex="1" connectable="0" parent="conn_api_alb">
            <mxGeometry x="-0.1" y="-1" relative="1" as="geometry">
              <mxPoint as="offset"/>
            </mxGeometry>
          </mxCell>
        </mxCell>
        
        <!-- External Integrations -->
        <mxCell id="conn_dian_api" style="endArrow=classic;html=1;strokeColor=#607D8B;strokeWidth=2;dashed=1;" edge="1" parent="1" source="dian_api" target="api_gateway_pro">
          <mxCell id="label_dian_api" value="Tax\\nValidation" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=9;fillColor=#ECEFF1;strokeColor=#607D8B;" vertex="1" connectable="0" parent="conn_dian_api">
            <mxGeometry x="-0.1" y="-1" relative="1" as="geometry">
              <mxPoint as="offset"/>
            </mxGeometry>
          </mxCell>
        </mxCell>
        
        <!-- Monitoring Connections -->
        <mxCell id="conn_monitor1" style="endArrow=classic;html=1;strokeColor=#795548;strokeWidth=1;dashed=1;" edge="1" parent="1" source="invoice_service_pro" target="cloudwatch_pro"/>
        <mxCell id="conn_monitor2" style="endArrow=classic;html=1;strokeColor=#795548;strokeWidth=1;dashed=1;" edge="1" parent="1" source="product_service_pro" target="cloudwatch_pro"/>
        <mxCell id="conn_monitor3" style="endArrow=classic;html=1;strokeColor=#795548;strokeWidth=1;dashed=1;" edge="1" parent="1" source="rds_primary_pro" target="cloudwatch_pro"/>'''
    
    def _get_timestamp(self) -> str:
        """Genera timestamp para el archivo"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z")
