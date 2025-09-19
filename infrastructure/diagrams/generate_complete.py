#!/usr/bin/env python3
"""
Generador Completo BMC - PNG + Draw.io
Versión definitiva que genera ambos formatos correctamente
"""

import os
from diagrams import Diagram, Cluster
from diagrams.aws.compute import Fargate, Lambda
from diagrams.aws.database import RDS, Redshift, Elasticache
from diagrams.aws.storage import S3
from diagrams.aws.network import APIGateway, CloudFront, ELB
from diagrams.aws.security import Cognito, WAF
from diagrams.aws.integration import SQS, SNS
from diagrams.aws.ml import Textract
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.client import Users
from diagrams.onprem.network import Internet

def generate_png_diagrams():
    """Genera diagramas PNG con iconos AWS"""
    
    print("📊 Generando diagramas PNG...")
    
    # Diagrama 1: Arquitectura Principal
    with Diagram("BMC AWS Architecture - 60M Products", 
                 filename="bmc_complete_architecture", 
                 show=False, 
                 direction="TB"):
        
        users = Users("BMC Users")
        
        with Cluster("AWS Cloud"):
            # Edge Security
            with Cluster("Edge Security"):
                cloudfront = CloudFront("CloudFront")
                waf = WAF("WAF")
                api_gateway = APIGateway("API Gateway")
                cognito = Cognito("Cognito")
            
            # Compute
            with Cluster("ECS Fargate"):
                alb = ELB("ALB")
                invoice_service = Fargate("Invoice\n2vCPU/4GB")
                product_service = Fargate("Product\n4vCPU/8GB\n60M Records")
                ocr_service = Fargate("OCR\n2vCPU/4GB")
                lambda_func = Lambda("Lambda\nOCR Processor")
            
            # Data
            with Cluster("Data Layer"):
                rds = RDS("RDS PostgreSQL\n60M Products")
                redis = Elasticache("Redis Cache\n24h TTL")
                s3 = S3("S3 Documents")
            
            # AI/ML
            textract = Textract("Textract\nOCR >95%")
            
            # Integration
            with Cluster("Integration"):
                sqs = SQS("SQS FIFO")
                sns = SNS("SNS")
            
            # Monitoring
            cloudwatch = Cloudwatch("CloudWatch")
        
        # External
        dian_api = Internet("DIAN API")
        
        # Connections
        users >> cloudfront >> waf >> api_gateway >> cognito
        api_gateway >> alb >> [invoice_service, product_service, ocr_service]
        product_service >> redis >> rds
        ocr_service >> lambda_func >> textract
        ocr_service >> s3
        invoice_service >> sqs >> sns
        product_service >> dian_api
        [invoice_service, product_service, ocr_service] >> cloudwatch
    
    print("✓ bmc_complete_architecture.png generado")
    
    # Diagrama 2: Microservicios
    with Diagram("BMC Microservices Detail", 
                 filename="bmc_microservices_complete", 
                 show=False, 
                 direction="TB"):
        
        api_gateway = APIGateway("API Gateway")
        
        with Cluster("ECS Fargate Cluster"):
            # Invoice Service
            invoice_alb = ELB("Invoice ALB")
            invoice_tasks = [
                Fargate("Task 1\n2vCPU"),
                Fargate("Task 2\n2vCPU")
            ]
            
            # Product Service
            product_alb = ELB("Product ALB")
            product_tasks = [
                Fargate("Task 1\n4vCPU"),
                Fargate("Task 2\n4vCPU"),
                Fargate("Task 3\n4vCPU")
            ]
        
        with Cluster("Data Services"):
            rds = RDS("PostgreSQL\n60M Products")
            redis = Elasticache("Redis Cache")
            s3 = S3("S3 Storage")
        
        # Connections
        api_gateway >> [invoice_alb, product_alb]
        invoice_alb >> invoice_tasks[0]
        invoice_alb >> invoice_tasks[1]
        product_alb >> product_tasks[0]
        product_alb >> product_tasks[1]
        product_alb >> product_tasks[2]
        
        invoice_tasks[0] >> rds
        product_tasks[0] >> redis
        product_tasks[1] >> rds
    
    print("✓ bmc_microservices_complete.png generado")

def generate_drawio_file():
    """Genera archivo Draw.io válido"""
    
    print("🎨 Generando archivo Draw.io...")
    
    drawio_content = '''<mxfile host="app.diagrams.net">
  <diagram name="BMC AWS Architecture Complete" id="complete">
    <mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="900">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Title -->
        <mxCell id="title" value="BMC AWS Architecture - 60M Products Platform" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=none;fontColor=#FFFFFF;fontSize=16;fontStyle=1;align=center;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1300" height="40" as="geometry"/>
        </mxCell>
        
        <!-- On-Premise -->
        <mxCell id="onprem" value="On-Premise" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFEBEE;strokeColor=#D32F2F;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=10;dashed=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="80" width="200" height="120" as="geometry"/>
        </mxCell>
        
        <!-- Users -->
        <mxCell id="users" value="BMC Users&#10;Web/Mobile/Admin" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.users;" vertex="1" parent="1">
          <mxGeometry x="130" y="120" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- AWS Cloud -->
        <mxCell id="awscloud" value="AWS Cloud - us-east-1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;strokeWidth=3;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=15;" vertex="1" parent="1">
          <mxGeometry x="300" y="80" width="1050" height="750" as="geometry"/>
        </mxCell>
        
        <!-- Edge Security -->
        <mxCell id="edge" value="Edge Security" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#FF9800;strokeWidth=2;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=8;" vertex="1" parent="1">
          <mxGeometry x="330" y="120" width="400" height="80" as="geometry"/>
        </mxCell>
        
        <!-- CloudFront -->
        <mxCell id="cloudfront" value="CloudFront" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudfront;" vertex="1" parent="1">
          <mxGeometry x="360" y="145" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- WAF -->
        <mxCell id="waf" value="WAF" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.waf;" vertex="1" parent="1">
          <mxGeometry x="450" y="145" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- API Gateway -->
        <mxCell id="api" value="API Gateway" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.api_gateway;" vertex="1" parent="1">
          <mxGeometry x="540" y="145" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Cognito -->
        <mxCell id="cognito" value="Cognito" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cognito;" vertex="1" parent="1">
          <mxGeometry x="630" y="145" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Application Layer -->
        <mxCell id="app" value="Application Layer - ECS Fargate" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#4CAF50;strokeWidth=2;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=8;" vertex="1" parent="1">
          <mxGeometry x="330" y="230" width="600" height="150" as="geometry"/>
        </mxCell>
        
        <!-- ALB -->
        <mxCell id="alb" value="ALB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#8C4FFF;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.application_load_balancer;" vertex="1" parent="1">
          <mxGeometry x="540" y="260" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Invoice Service -->
        <mxCell id="invoice" value="Invoice&#10;2vCPU/4GB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="400" y="320" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Product Service -->
        <mxCell id="product" value="Product&#10;4vCPU/8GB&#10;60M Records" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="540" y="320" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- OCR Service -->
        <mxCell id="ocr" value="OCR&#10;2vCPU/4GB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="680" y="320" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Lambda -->
        <mxCell id="lambda" value="Lambda&#10;OCR Proc" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lambda;" vertex="1" parent="1">
          <mxGeometry x="820" y="320" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Data Layer -->
        <mxCell id="data" value="Data Layer" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4EC;strokeColor=#E91E63;strokeWidth=2;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=8;" vertex="1" parent="1">
          <mxGeometry x="330" y="410" width="400" height="100" as="geometry"/>
        </mxCell>
        
        <!-- RDS -->
        <mxCell id="rds" value="RDS&#10;PostgreSQL&#10;60M Products" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.rds;" vertex="1" parent="1">
          <mxGeometry x="380" y="450" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Redis -->
        <mxCell id="redis" value="Redis&#10;Cache&#10;24h TTL" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elasticache;" vertex="1" parent="1">
          <mxGeometry x="540" y="450" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- S3 -->
        <mxCell id="s3" value="S3&#10;Documents" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;" vertex="1" parent="1">
          <mxGeometry x="680" y="450" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- AI/ML -->
        <mxCell id="textract" value="Textract&#10;OCR >95%" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.textract;" vertex="1" parent="1">
          <mxGeometry x="820" y="450" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Integration -->
        <mxCell id="integration" value="Integration" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F3E5F5;strokeColor=#9C27B0;strokeWidth=2;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=8;" vertex="1" parent="1">
          <mxGeometry x="330" y="540" width="300" height="100" as="geometry"/>
        </mxCell>
        
        <!-- SQS -->
        <mxCell id="sqs" value="SQS&#10;FIFO" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sqs;" vertex="1" parent="1">
          <mxGeometry x="380" y="580" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- SNS -->
        <mxCell id="sns" value="SNS&#10;Notifications" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sns;" vertex="1" parent="1">
          <mxGeometry x="540" y="580" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Monitoring -->
        <mxCell id="cloudwatch" value="CloudWatch&#10;Monitoring" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F34482;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudwatch;" vertex="1" parent="1">
          <mxGeometry x="680" y="580" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- External -->
        <mxCell id="dian" value="DIAN API" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#607D8B;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.internet_gateway;" vertex="1" parent="1">
          <mxGeometry x="1000" y="320" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Performance Info -->
        <mxCell id="perf" value="Performance KPIs&#10;• OCR Processing: &lt;5s&#10;• Product Lookup: &lt;500ms (60M)&#10;• Throughput: 10K invoices/hour&#10;• Availability: &gt;99.9%&#10;• Cost: $8,650/month" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1F5FE;strokeColor=#0277BD;fontSize=9;align=left;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="1000" y="450" width="200" height="100" as="geometry"/>
        </mxCell>
        
        <!-- Connections -->
        <mxCell id="c1" style="endArrow=classic;html=1;rounded=0;strokeColor=#1976D2;strokeWidth=2;" edge="1" parent="1" source="users" target="cloudfront"/>
        <mxCell id="c2" style="endArrow=classic;html=1;rounded=0;strokeColor=#FF9800;strokeWidth=2;" edge="1" parent="1" source="cloudfront" target="waf"/>
        <mxCell id="c3" style="endArrow=classic;html=1;rounded=0;strokeColor=#FF9800;strokeWidth=2;" edge="1" parent="1" source="waf" target="api"/>
        <mxCell id="c4" style="endArrow=classic;html=1;rounded=0;strokeColor=#FF9800;strokeWidth=2;" edge="1" parent="1" source="api" target="cognito"/>
        <mxCell id="c5" style="endArrow=classic;html=1;rounded=0;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="api" target="alb"/>
        <mxCell id="c6" style="endArrow=classic;html=1;rounded=0;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="alb" target="invoice"/>
        <mxCell id="c7" style="endArrow=classic;html=1;rounded=0;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="alb" target="product"/>
        <mxCell id="c8" style="endArrow=classic;html=1;rounded=0;strokeColor=#4CAF50;strokeWidth=2;" edge="1" parent="1" source="alb" target="ocr"/>
        <mxCell id="c9" style="endArrow=classic;html=1;rounded=0;strokeColor=#9C27B0;strokeWidth=2;" edge="1" parent="1" source="product" target="redis"/>
        <mxCell id="c10" style="endArrow=classic;html=1;rounded=0;strokeColor=#9C27B0;strokeWidth=2;" edge="1" parent="1" source="redis" target="rds"/>
        <mxCell id="c11" style="endArrow=classic;html=1;rounded=0;strokeColor=#E91E63;strokeWidth=2;" edge="1" parent="1" source="ocr" target="s3"/>
        <mxCell id="c12" style="endArrow=classic;html=1;rounded=0;strokeColor=#E91E63;strokeWidth=2;" edge="1" parent="1" source="lambda" target="textract"/>
        <mxCell id="c13" style="endArrow=classic;html=1;rounded=0;strokeColor=#607D8B;strokeWidth=2;" edge="1" parent="1" source="product" target="dian"/>
        <mxCell id="c14" style="endArrow=classic;html=1;rounded=0;strokeColor=#9C27B0;strokeWidth=2;" edge="1" parent="1" source="invoice" target="sqs"/>
        <mxCell id="c15" style="endArrow=classic;html=1;rounded=0;strokeColor=#9C27B0;strokeWidth=2;" edge="1" parent="1" source="sqs" target="sns"/>
        <mxCell id="c16" style="endArrow=classic;html=1;rounded=0;strokeColor=#795548;strokeWidth=2;" edge="1" parent="1" source="product" target="cloudwatch"/>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    with open("bmc_complete_architecture.drawio", "w", encoding="utf-8") as f:
        f.write(drawio_content)
    
    print("✓ bmc_complete_architecture.drawio generado")

def main():
    print("🚀 Generador Completo BMC - Versión Definitiva")
    print("=" * 55)
    
    # Verificar directorio
    current_dir = os.getcwd()
    print(f"📁 Directorio actual: {current_dir}")
    
    try:
        # Generar PNG
        generate_png_diagrams()
        
        # Generar Draw.io
        generate_drawio_file()
        
        print("\n✅ Generación completada exitosamente!")
        
        # Verificar archivos generados
        png_files = [f for f in os.listdir('.') if f.endswith('.png') and 'bmc' in f]
        drawio_files = [f for f in os.listdir('.') if f.endswith('.drawio') and 'bmc' in f]
        
        print(f"\n📊 Archivos PNG generados ({len(png_files)}):")
        for f in sorted(png_files):
            size = os.path.getsize(f)
            print(f"  - {f} ({size:,} bytes)")
        
        print(f"\n🎨 Archivos Draw.io generados ({len(drawio_files)}):")
        for f in sorted(drawio_files):
            size = os.path.getsize(f)
            print(f"  - {f} ({size:,} bytes)")
        
        print("\n💡 Archivos listos para usar:")
        print("  - PNG: Para presentaciones y documentos")
        print("  - Draw.io: Para edición en https://app.diagrams.net")
        
    except Exception as e:
        print(f"❌ Error durante la generación: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
