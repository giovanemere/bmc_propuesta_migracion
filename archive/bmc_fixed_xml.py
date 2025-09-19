#!/usr/bin/env python3
"""
BMC Draw.io - Fixed XML with proper escaping
"""

def generate_fixed_drawio():
    """Generate Draw.io with properly escaped XML"""
    xml_content = '''<mxfile host="app.diagrams.net">
  <diagram name="BMC AWS Architecture" id="diagram1">
    <mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="900">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Header -->
        <mxCell id="header" value="BMC AWS Architecture - 60M Products Platform" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=none;fontColor=#FFFFFF;fontSize=16;fontStyle=1;align=center;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1300" height="40" as="geometry"/>
        </mxCell>
        
        <mxCell id="dateInfo" value="Implementation: Q1 2024 | Go-Live: Q2 2024 | Cost: $8,650/month | SLA: 99.9%" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;fontSize=10;fontColor=#666666;" vertex="1" parent="1">
          <mxGeometry x="50" y="65" width="1300" height="20" as="geometry"/>
        </mxCell>
        
        <!-- Users -->
        <mxCell id="users" value="BMC Users" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.users;" vertex="1" parent="1">
          <mxGeometry x="80" y="120" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="usersComment" value="Web, Mobile, Admin&#10;10,000 concurrent users&#10;Multi-tenant access" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF9C4;strokeColor=#F57F17;fontSize=8;align=left;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="20" y="170" width="120" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Edge Security Group -->
        <mxCell id="edgeGroup" value="Edge Security Layer" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;strokeWidth=2;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=8;" vertex="1" parent="1">
          <mxGeometry x="180" y="100" width="400" height="80" as="geometry"/>
        </mxCell>
        
        <!-- CloudFront -->
        <mxCell id="cloudfront" value="CloudFront" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudfront;" vertex="1" parent="1">
          <mxGeometry x="210" y="125" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- WAF -->
        <mxCell id="waf" value="WAF" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.waf;" vertex="1" parent="1">
          <mxGeometry x="290" y="125" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- API Gateway -->
        <mxCell id="api" value="API Gateway" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.api_gateway;" vertex="1" parent="1">
          <mxGeometry x="370" y="125" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Cognito -->
        <mxCell id="cognito" value="Cognito" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cognito;" vertex="1" parent="1">
          <mxGeometry x="450" y="125" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="edgeComment" value="DDoS Protection&#10;SSL Termination&#10;Rate Limiting: 1000 req/s" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;fontSize=8;align=left;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="600" y="110" width="130" height="50" as="geometry"/>
        </mxCell>
        
        <!-- Compute Group -->
        <mxCell id="computeGroup" value="ECS Fargate Microservices - Auto Scaling 2-15 instances" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#FF9800;strokeWidth=2;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=8;" vertex="1" parent="1">
          <mxGeometry x="80" y="240" width="650" height="140" as="geometry"/>
        </mxCell>
        
        <!-- ALB -->
        <mxCell id="alb" value="ALB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#8C4FFF;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.application_load_balancer;" vertex="1" parent="1">
          <mxGeometry x="370" y="270" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Invoice Service -->
        <mxCell id="invoice" value="Invoice&#10;2vCPU/4GB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="200" y="320" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Product Service -->
        <mxCell id="product" value="Product&#10;4vCPU/8GB&#10;60M Records" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="370" y="320" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- OCR Service -->
        <mxCell id="ocr" value="OCR&#10;2vCPU/4GB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="540" y="320" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Lambda -->
        <mxCell id="lambda" value="Lambda&#10;OCR Proc" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lambda;" vertex="1" parent="1">
          <mxGeometry x="620" y="320" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Data Layer Group -->
        <mxCell id="dataGroup" value="Data Layer - Multi-AZ with 35-day backup retention" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#4CAF50;strokeWidth=2;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=8;" vertex="1" parent="1">
          <mxGeometry x="80" y="420" width="450" height="120" as="geometry"/>
        </mxCell>
        
        <!-- RDS -->
        <mxCell id="rds" value="RDS&#10;PostgreSQL&#10;60M Products" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.rds;" vertex="1" parent="1">
          <mxGeometry x="150" y="460" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Redis -->
        <mxCell id="redis" value="Redis&#10;Cache&#10;24h TTL" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elasticache;" vertex="1" parent="1">
          <mxGeometry x="280" y="460" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- S3 -->
        <mxCell id="s3" value="S3&#10;Documents" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;" vertex="1" parent="1">
          <mxGeometry x="410" y="460" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- AI/ML Group -->
        <mxCell id="aiGroup" value="AI/ML Services - OCR Accuracy greater than 95%" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4EC;strokeColor=#E91E63;strokeWidth=2;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=8;" vertex="1" parent="1">
          <mxGeometry x="580" y="420" width="200" height="120" as="geometry"/>
        </mxCell>
        
        <!-- Textract -->
        <mxCell id="textract" value="Textract&#10;OCR 95%&#10;Forms Analysis" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.textract;" vertex="1" parent="1">
          <mxGeometry x="650" y="460" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Integration Group -->
        <mxCell id="integrationGroup" value="Event-Driven Integration - 10,000 invoices/hour" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F3E5F5;strokeColor=#9C27B0;strokeWidth=2;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=8;" vertex="1" parent="1">
          <mxGeometry x="80" y="580" width="400" height="100" as="geometry"/>
        </mxCell>
        
        <!-- SQS -->
        <mxCell id="sqs" value="SQS&#10;FIFO Queue" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sqs;" vertex="1" parent="1">
          <mxGeometry x="150" y="620" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- SNS -->
        <mxCell id="sns" value="SNS&#10;Notifications" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sns;" vertex="1" parent="1">
          <mxGeometry x="280" y="620" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- CloudWatch -->
        <mxCell id="cloudwatch" value="CloudWatch&#10;Metrics/Logs" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F34482;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudwatch;" vertex="1" parent="1">
          <mxGeometry x="580" y="620" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- DIAN API -->
        <mxCell id="dian" value="DIAN API&#10;Tax Authority" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#607D8B;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.internet_gateway;" vertex="1" parent="1">
          <mxGeometry x="800" y="320" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Performance Metrics -->
        <mxCell id="metrics" value="Performance KPIs&#10;OCR Processing: less than 5s&#10;Product Lookup: less than 500ms&#10;Invoice Processing: less than 3s&#10;System Availability: greater than 99.9%&#10;Throughput: 10K invoices/hour" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1F5FE;strokeColor=#0277BD;fontSize=9;align=left;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="850" y="580" width="200" height="100" as="geometry"/>
        </mxCell>
        
        <!-- Implementation Timeline -->
        <mxCell id="timeline" value="Implementation Timeline&#10;Phase 1 (Weeks 1-8): Foundation&#10;Phase 2 (Weeks 9-16): OCR Processing&#10;Phase 3 (Weeks 17-22): Business Logic&#10;Phase 4 (Weeks 23-26): Frontend&#10;Phase 5 (Weeks 27-30): Go-Live" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFEBEE;strokeColor=#C62828;fontSize=9;align=left;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="1070" y="580" width="280" height="100" as="geometry"/>
        </mxCell>
        
        <!-- Connections -->
        <mxCell id="edge1" value="HTTPS" style="endArrow=classic;html=1;rounded=0;strokeColor=#1976D2;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="users" target="cloudfront"/>
        <mxCell id="edge2" value="CDN" style="endArrow=classic;html=1;rounded=0;strokeColor=#1976D2;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="cloudfront" target="waf"/>
        <mxCell id="edge3" value="Filter" style="endArrow=classic;html=1;rounded=0;strokeColor=#1976D2;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="waf" target="api"/>
        <mxCell id="edge4" value="Auth" style="endArrow=classic;html=1;rounded=0;strokeColor=#FF9800;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="api" target="cognito"/>
        <mxCell id="edge5" value="Route" style="endArrow=classic;html=1;rounded=0;strokeColor=#FF9800;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="api" target="alb"/>
        <mxCell id="edge6" value="2-10 inst" style="endArrow=classic;html=1;rounded=0;strokeColor=#4CAF50;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="alb" target="invoice"/>
        <mxCell id="edge7" value="3-15 inst" style="endArrow=classic;html=1;rounded=0;strokeColor=#4CAF50;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="alb" target="product"/>
        <mxCell id="edge8" value="2-8 inst" style="endArrow=classic;html=1;rounded=0;strokeColor=#4CAF50;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="alb" target="ocr"/>
        <mxCell id="edge9" value="60M lookup" style="endArrow=classic;html=1;rounded=0;strokeColor=#9C27B0;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="product" target="redis"/>
        <mxCell id="edge10" value="Cache miss" style="endArrow=classic;html=1;rounded=0;strokeColor=#9C27B0;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="redis" target="rds"/>
        <mxCell id="edge11" value="Store docs" style="endArrow=classic;html=1;rounded=0;strokeColor=#E91E63;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="ocr" target="s3"/>
        <mxCell id="edge12" value="OCR Process" style="endArrow=classic;html=1;rounded=0;strokeColor=#E91E63;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="lambda" target="textract"/>
        <mxCell id="edge13" value="Classify" style="endArrow=classic;html=1;rounded=0;strokeColor=#607D8B;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="product" target="dian"/>
        <mxCell id="edge14" value="Queue" style="endArrow=classic;html=1;rounded=0;strokeColor=#9C27B0;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="invoice" target="sqs"/>
        <mxCell id="edge15" value="Notify" style="endArrow=classic;html=1;rounded=0;strokeColor=#9C27B0;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="sqs" target="sns"/>
        <mxCell id="edge16" value="Metrics" style="endArrow=classic;html=1;rounded=0;strokeColor=#FFC107;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="product" target="cloudwatch"/>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    return xml_content

def main():
    print("🚀 BMC Draw.io - Fixed XML Entities")
    print("=" * 40)
    
    xml_content = generate_fixed_drawio()
    
    with open("bmc_fixed_architecture.drawio", "w", encoding="utf-8") as f:
        f.write(xml_content)
    
    print("✓ Fixed XML architecture generated: bmc_fixed_architecture.drawio")
    print("🔧 XML fixes applied:")
    print("  - Replaced & with proper entities")
    print("  - Used &#10; for line breaks")
    print("  - Escaped special characters")
    print("  - Valid XML structure")
    print("🔗 Open at: https://app.diagrams.net")

if __name__ == "__main__":
    main()
