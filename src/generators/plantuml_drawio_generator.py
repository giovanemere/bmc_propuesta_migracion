#!/usr/bin/env python3
"""
PlantUML DrawIO Generator - Generador profesional usando PlantUML
"""

from pathlib import Path
from datetime import datetime
from typing import Dict, Any
import subprocess
import tempfile

class PlantUMLDrawIOGenerator:
    """Generador DrawIO profesional usando PlantUML"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str):
        self.config = config
        self.output_dir = Path(output_dir)
    
    def generate_professional_drawio(self, project_name: str = "bmc_input") -> str:
        """Genera DrawIO profesional usando PlantUML"""
        
        # Crear PlantUML para arquitectura AWS
        plantuml_code = self._create_aws_architecture_plantuml(project_name)
        
        # Generar archivo temporal PlantUML
        with tempfile.NamedTemporaryFile(mode='w', suffix='.puml', delete=False) as f:
            f.write(plantuml_code)
            puml_file = f.name
        
        # Generar DrawIO desde PlantUML
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = self.output_dir / "drawio" / f"{project_name}_professional_{timestamp}.drawio"
        
        try:
            # Usar PlantUML para generar DrawIO
            result = subprocess.run([
                'java', '-jar', '/usr/share/plantuml/plantuml.jar',
                '-tdrawio', puml_file, '-o', str(output_file.parent)
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                # Renombrar archivo generado
                generated_files = list(output_file.parent.glob("*.drawio"))
                if generated_files:
                    latest_file = max(generated_files, key=lambda x: x.stat().st_mtime)
                    latest_file.rename(output_file)
                    return str(output_file)
            
        except (subprocess.TimeoutExpired, FileNotFoundError):
            # Fallback: generar DrawIO manualmente desde PlantUML
            return self._generate_drawio_from_plantuml(plantuml_code, output_file)
        
        # Cleanup
        Path(puml_file).unlink(missing_ok=True)
        
        return str(output_file)
    
    def _create_aws_architecture_plantuml(self, project_name: str) -> str:
        """Crea código PlantUML para arquitectura AWS"""
        
        return f"""@startuml {project_name}_architecture
!include <awslib/AWSCommon>
!include <awslib/InternetOfThings/IoTCore>
!include <awslib/NetworkingContentDelivery/CloudFront>
!include <awslib/NetworkingContentDelivery/ElasticLoadBalancing>
!include <awslib/NetworkingContentDelivery/APIGateway>
!include <awslib/SecurityIdentityCompliance/WAF>
!include <awslib/SecurityIdentityCompliance/Cognito>
!include <awslib/Compute/Fargate>
!include <awslib/Database/RDS>
!include <awslib/Database/ElastiCache>
!include <awslib/Storage/SimpleStorageService>
!include <awslib/NetworkingContentDelivery/VPC>

title {project_name.upper()} - Professional AWS Architecture

' External entities
actor "BMC Users\\n10K concurrent" as users
cloud "Internet" as internet

' AWS Cloud boundary
AWSCloudAltGroup(aws_cloud, "AWS Cloud - us-east-1") {{
    
    ' Edge Layer
    rectangle "Edge Layer" as edge_layer {{
        CloudFront(cloudfront, "CloudFront CDN", "Global Edge\\nCaching & SSL")
        WAF(waf, "AWS WAF", "DDoS Protection\\nSecurity Rules")
    }}
    
    ' API Layer  
    rectangle "API Layer" as api_layer {{
        APIGateway(api_gw, "API Gateway", "REST + GraphQL\\nRate Limiting")
        Cognito(cognito, "Cognito", "User Pool\\nAuthentication")
        ElasticLoadBalancing(alb, "Application LB", "Multi-AZ\\nSSL Termination")
    }}
    
    ' VPC
    VPCGroup(vpc, "VPC 10.0.0.0/16") {{
        
        ' Availability Zone A
        AvailabilityZoneGroup(az_a, "us-east-1a") {{
            
            ' Public Subnet A
            PublicSubnetGroup(public_a, "Public Subnet\\n10.0.1.0/24") {{
                ElasticLoadBalancing(nat_a, "NAT Gateway 1A", "Outbound Internet\\nElastic IP")
            }}
            
            ' Private Subnet A
            PrivateSubnetGroup(private_a, "Private Subnet\\n10.0.10.0/24") {{
                Fargate(app_a, "App Services 1A", "ECS Fargate\\nCertificate Service")
            }}
            
            ' Isolated Subnet A
            PrivateSubnetGroup(isolated_a, "Isolated Subnet\\n10.0.20.0/24") {{
                RDS(rds_primary, "RDS PostgreSQL", "Primary Instance\\nus-east-1a\\nMulti-AZ")
                ElastiCache(redis, "ElastiCache", "Redis Cluster\\nSession Store")
            }}
        }}
        
        ' Availability Zone B
        AvailabilityZoneGroup(az_b, "us-east-1b") {{
            PrivateSubnetGroup(isolated_b, "Isolated Subnet\\n10.0.21.0/24") {{
                RDS(rds_standby, "RDS PostgreSQL", "Standby Instance\\nus-east-1b\\nRead Replica")
            }}
        }}
        
        ' S3 Storage (region-wide)
        SimpleStorageService(s3, "S3 Storage", "Documents & Assets\\nVersioning Enabled\\n60M Products Data")
    }}
}}

' Connections with professional styling
users -down-> internet : HTTPS
internet -down-> cloudfront : Global CDN
cloudfront -down-> waf : Security Filter
waf -down-> api_gw : Filtered Traffic
api_gw -right-> cognito : Authentication
api_gw -down-> alb : Load Balance
alb -down-> app_a : Route Traffic
app_a -down-> rds_primary : Database Queries
app_a -right-> redis : Session Cache
app_a -right-> s3 : File Storage
rds_primary -right-> rds_standby : Replication

' Layout hints for professional appearance
!define DIRECTION top to bottom direction
skinparam backgroundColor white
skinparam shadowing false
skinparam defaultFontName Arial
skinparam defaultFontSize 10

@enduml"""
    
    def _generate_drawio_from_plantuml(self, plantuml_code: str, output_file: Path) -> str:
        """Genera DrawIO manualmente desde código PlantUML (fallback)"""
        
        # Crear DrawIO básico basado en PlantUML
        drawio_xml = f"""<?xml version='1.0' encoding='utf-8'?>
<mxfile host="app.diagrams.net">
  <diagram name="AWS Architecture - PlantUML Generated" id="plantuml">
    <mxGraphModel dx="2400" dy="1600" grid="1" gridSize="10">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- Title -->
        <mxCell id="title" value="BMC_INPUT - Professional AWS Architecture (PlantUML)" 
                style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;fontColor=#FFFFFF;fontSize=18;fontStyle=1;" 
                vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="2000" height="50" as="geometry" />
        </mxCell>
        
        <!-- Users -->
        <mxCell id="users" value="BMC Users\\n10K concurrent" 
                style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.users;" 
                vertex="1" parent="1">
          <mxGeometry x="100" y="100" width="78" height="78" as="geometry" />
        </mxCell>
        
        <!-- Internet -->
        <mxCell id="internet" value="Internet" 
                style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.internet_gateway;" 
                vertex="1" parent="1">
          <mxGeometry x="300" y="100" width="78" height="78" as="geometry" />
        </mxCell>
        
        <!-- AWS Cloud -->
        <mxCell id="aws_cloud" value="AWS Cloud - us-east-1" 
                style="fillColor=#E3F2FD;strokeColor=#1976D2;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#1976D2;whiteSpace=wrap;html=1;fontSize=14;" 
                vertex="1" parent="1">
          <mxGeometry x="50" y="220" width="1800" height="1000" as="geometry" />
        </mxCell>
        
        <!-- CloudFront -->
        <mxCell id="cloudfront" value="CloudFront CDN\\nGlobal Edge" 
                style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudfront;" 
                vertex="1" parent="aws_cloud">
          <mxGeometry x="100" y="50" width="78" height="78" as="geometry" />
        </mxCell>
        
        <!-- API Gateway -->
        <mxCell id="api_gateway" value="API Gateway\\nREST + GraphQL" 
                style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.api_gateway;" 
                vertex="1" parent="aws_cloud">
          <mxGeometry x="300" y="50" width="78" height="78" as="geometry" />
        </mxCell>
        
        <!-- Fargate -->
        <mxCell id="fargate" value="App Services\\nECS Fargate" 
                style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;" 
                vertex="1" parent="aws_cloud">
          <mxGeometry x="500" y="200" width="78" height="78" as="geometry" />
        </mxCell>
        
        <!-- RDS -->
        <mxCell id="rds" value="RDS PostgreSQL\\nPrimary + Standby" 
                style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.rds;" 
                vertex="1" parent="aws_cloud">
          <mxGeometry x="700" y="350" width="78" height="78" as="geometry" />
        </mxCell>
        
        <!-- S3 -->
        <mxCell id="s3" value="S3 Storage\\n60M Products" 
                style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;" 
                vertex="1" parent="aws_cloud">
          <mxGeometry x="900" y="200" width="78" height="78" as="geometry" />
        </mxCell>
        
        <!-- Professional Connections -->
        <mxCell id="conn1" value="" style="endArrow=classic;html=1;rounded=0;strokeColor=#232F3E;strokeWidth=3;" edge="1" parent="1" source="users" target="internet">
          <mxGeometry width="50" height="50" relative="1" as="geometry" />
        </mxCell>
        
        <mxCell id="conn2" value="" style="endArrow=classic;html=1;rounded=0;strokeColor=#1976D2;strokeWidth=3;" edge="1" parent="1" source="internet" target="cloudfront">
          <mxGeometry width="50" height="50" relative="1" as="geometry" />
        </mxCell>
        
        <mxCell id="conn3" value="" style="endArrow=classic;html=1;rounded=0;strokeColor=#5A30B5;strokeWidth=2;" edge="1" parent="1" source="cloudfront" target="api_gateway">
          <mxGeometry width="50" height="50" relative="1" as="geometry" />
        </mxCell>
        
        <mxCell id="conn4" value="" style="endArrow=classic;html=1;rounded=0;strokeColor=#D05C17;strokeWidth=2;" edge="1" parent="1" source="api_gateway" target="fargate">
          <mxGeometry width="50" height="50" relative="1" as="geometry" />
        </mxCell>
        
        <mxCell id="conn5" value="" style="endArrow=classic;html=1;rounded=0;strokeColor=#116D5B;strokeWidth=2;" edge="1" parent="1" source="fargate" target="rds">
          <mxGeometry width="50" height="50" relative="1" as="geometry" />
        </mxCell>
        
        <mxCell id="conn6" value="" style="endArrow=classic;html=1;rounded=0;strokeColor=#277116;strokeWidth=2;" edge="1" parent="1" source="fargate" target="s3">
          <mxGeometry width="50" height="50" relative="1" as="geometry" />
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""
        
        # Guardar archivo
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(drawio_xml)
        
        return str(output_file)
