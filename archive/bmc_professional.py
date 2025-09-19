#!/usr/bin/env python3
"""
BMC Professional Draw.io - Small icons, compact text, grouped layout
"""

def generate_professional_drawio():
    """Generate professional Draw.io with small icons and groups"""
    xml_content = '''<mxfile host="app.diagrams.net">
  <diagram name="BMC AWS Architecture" id="diagram1">
    <mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="900">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Title -->
        <mxCell id="title" value="BMC AWS Architecture - 60M Products Platform" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;fontSize=14;fontStyle=1;fontColor=#232F3E;" vertex="1" parent="1">
          <mxGeometry x="500" y="20" width="400" height="25" as="geometry"/>
        </mxCell>
        
        <!-- Edge Security Group -->
        <mxCell id="edgeGroup" value="Edge Security" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F4FD;strokeColor=#1976D2;strokeWidth=2;fontSize=10;fontStyle=1;verticalAlign=top;spacingTop=5;" vertex="1" parent="1">
          <mxGeometry x="50" y="80" width="320" height="80" as="geometry"/>
        </mxCell>
        
        <!-- Users -->
        <mxCell id="users" value="Users" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.users;" vertex="1" parent="1">
          <mxGeometry x="70" y="105" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- CloudFront -->
        <mxCell id="cloudfront" value="CloudFront" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudfront;" vertex="1" parent="1">
          <mxGeometry x="140" y="105" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- WAF -->
        <mxCell id="waf" value="WAF" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.waf;" vertex="1" parent="1">
          <mxGeometry x="210" y="105" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- API Gateway -->
        <mxCell id="api" value="API Gateway" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.api_gateway;" vertex="1" parent="1">
          <mxGeometry x="280" y="105" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Cognito -->
        <mxCell id="cognito" value="Cognito" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cognito;" vertex="1" parent="1">
          <mxGeometry x="330" y="105" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Compute Group -->
        <mxCell id="computeGroup" value="ECS Fargate Microservices" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#FF9800;strokeWidth=2;fontSize=10;fontStyle=1;verticalAlign=top;spacingTop=5;" vertex="1" parent="1">
          <mxGeometry x="50" y="200" width="500" height="120" as="geometry"/>
        </mxCell>
        
        <!-- ALB -->
        <mxCell id="alb" value="ALB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#8C4FFF;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.application_load_balancer;" vertex="1" parent="1">
          <mxGeometry x="280" y="225" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Invoice Service -->
        <mxCell id="invoice" value="Invoice&#xa;2vCPU" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="150" y="270" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Product Service -->
        <mxCell id="product" value="Product&#xa;4vCPU&#xa;60M" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="280" y="270" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- OCR Service -->
        <mxCell id="ocr" value="OCR&#xa;2vCPU" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="410" y="270" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Lambda -->
        <mxCell id="lambda" value="Lambda" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lambda;" vertex="1" parent="1">
          <mxGeometry x="480" y="270" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Data Layer Group -->
        <mxCell id="dataGroup" value="Data Layer" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#4CAF50;strokeWidth=2;fontSize=10;fontStyle=1;verticalAlign=top;spacingTop=5;" vertex="1" parent="1">
          <mxGeometry x="50" y="360" width="350" height="100" as="geometry"/>
        </mxCell>
        
        <!-- RDS -->
        <mxCell id="rds" value="RDS&#xa;60M" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.rds;" vertex="1" parent="1">
          <mxGeometry x="100" y="400" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Redis -->
        <mxCell id="redis" value="Redis&#xa;24h" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elasticache;" vertex="1" parent="1">
          <mxGeometry x="200" y="400" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- S3 -->
        <mxCell id="s3" value="S3&#xa;Docs" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;" vertex="1" parent="1">
          <mxGeometry x="300" y="400" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- AI/ML Group -->
        <mxCell id="aiGroup" value="AI/ML Services" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4EC;strokeColor=#E91E63;strokeWidth=2;fontSize=10;fontStyle=1;verticalAlign=top;spacingTop=5;" vertex="1" parent="1">
          <mxGeometry x="450" y="360" width="120" height="100" as="geometry"/>
        </mxCell>
        
        <!-- Textract -->
        <mxCell id="textract" value="Textract&#xa;>95%" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.textract;" vertex="1" parent="1">
          <mxGeometry x="495" y="400" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Integration Group -->
        <mxCell id="integrationGroup" value="Event-Driven Integration" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F3E5F5;strokeColor=#9C27B0;strokeWidth=2;fontSize=10;fontStyle=1;verticalAlign=top;spacingTop=5;" vertex="1" parent="1">
          <mxGeometry x="600" y="200" width="200" height="120" as="geometry"/>
        </mxCell>
        
        <!-- SQS -->
        <mxCell id="sqs" value="SQS" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sqs;" vertex="1" parent="1">
          <mxGeometry x="630" y="240" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- SNS -->
        <mxCell id="sns" value="SNS" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sns;" vertex="1" parent="1">
          <mxGeometry x="730" y="240" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Monitoring Group -->
        <mxCell id="monitoringGroup" value="Monitoring" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF8E1;strokeColor=#FFC107;strokeWidth=2;fontSize=10;fontStyle=1;verticalAlign=top;spacingTop=5;" vertex="1" parent="1">
          <mxGeometry x="600" y="360" width="120" height="100" as="geometry"/>
        </mxCell>
        
        <!-- CloudWatch -->
        <mxCell id="cloudwatch" value="CloudWatch" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F34482;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudwatch;" vertex="1" parent="1">
          <mxGeometry x="645" y="400" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- External -->
        <mxCell id="dian" value="DIAN API" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.internet_gateway;" vertex="1" parent="1">
          <mxGeometry x="280" y="500" width="30" height="30" as="geometry"/>
        </mxCell>'''
    
    return xml_content

def add_professional_connections():
    """Add clean professional connections"""
    connections = '''
        <!-- Clean professional connections -->
        <mxCell id="edge1" style="endArrow=classic;html=1;rounded=0;strokeColor=#1976D2;strokeWidth=1.5;" edge="1" parent="1" source="users" target="cloudfront"/>
        <mxCell id="edge2" style="endArrow=classic;html=1;rounded=0;strokeColor=#1976D2;strokeWidth=1.5;" edge="1" parent="1" source="cloudfront" target="waf"/>
        <mxCell id="edge3" style="endArrow=classic;html=1;rounded=0;strokeColor=#1976D2;strokeWidth=1.5;" edge="1" parent="1" source="waf" target="api"/>
        <mxCell id="edge4" style="endArrow=classic;html=1;rounded=0;strokeColor=#FF9800;strokeWidth=1.5;" edge="1" parent="1" source="api" target="cognito"/>
        <mxCell id="edge5" style="endArrow=classic;html=1;rounded=0;strokeColor=#FF9800;strokeWidth=1.5;" edge="1" parent="1" source="api" target="alb"/>
        <mxCell id="edge6" style="endArrow=classic;html=1;rounded=0;strokeColor=#4CAF50;strokeWidth=1.5;" edge="1" parent="1" source="alb" target="invoice"/>
        <mxCell id="edge7" style="endArrow=classic;html=1;rounded=0;strokeColor=#4CAF50;strokeWidth=1.5;" edge="1" parent="1" source="alb" target="product"/>
        <mxCell id="edge8" style="endArrow=classic;html=1;rounded=0;strokeColor=#4CAF50;strokeWidth=1.5;" edge="1" parent="1" source="alb" target="ocr"/>
        <mxCell id="edge9" style="endArrow=classic;html=1;rounded=0;strokeColor=#9C27B0;strokeWidth=1.5;" edge="1" parent="1" source="product" target="redis"/>
        <mxCell id="edge10" style="endArrow=classic;html=1;rounded=0;strokeColor=#9C27B0;strokeWidth=1.5;" edge="1" parent="1" source="redis" target="rds"/>
        <mxCell id="edge11" style="endArrow=classic;html=1;rounded=0;strokeColor=#E91E63;strokeWidth=1.5;" edge="1" parent="1" source="ocr" target="s3"/>
        <mxCell id="edge12" style="endArrow=classic;html=1;rounded=0;strokeColor=#E91E63;strokeWidth=1.5;" edge="1" parent="1" source="lambda" target="textract"/>
        <mxCell id="edge13" style="endArrow=classic;html=1;rounded=0;strokeColor=#607D8B;strokeWidth=1.5;" edge="1" parent="1" source="product" target="dian"/>
        <mxCell id="edge14" style="endArrow=classic;html=1;rounded=0;strokeColor=#FFC107;strokeWidth=1.5;" edge="1" parent="1" source="invoice" target="sqs"/>
        <mxCell id="edge15" style="endArrow=classic;html=1;rounded=0;strokeColor=#FFC107;strokeWidth=1.5;" edge="1" parent="1" source="sqs" target="sns"/>
        <mxCell id="edge16" style="endArrow=classic;html=1;rounded=0;strokeColor=#795548;strokeWidth=1.5;" edge="1" parent="1" source="product" target="cloudwatch"/>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    return connections

def main():
    print("🚀 BMC Professional Draw.io - Compact & Grouped")
    print("=" * 50)
    
    # Generate complete professional XML
    xml_content = generate_professional_drawio() + add_professional_connections()
    
    with open("bmc_professional_architecture.drawio", "w", encoding="utf-8") as f:
        f.write(xml_content)
    
    print("✓ Professional architecture generated: bmc_professional_architecture.drawio")
    print("🎨 Professional features:")
    print("  - Small icons (30x30px)")
    print("  - Compact text (8-10px)")
    print("  - Organized groups by function")
    print("  - Clean color coding")
    print("  - Minimal labels")
    print("🔗 Open at: https://app.diagrams.net")

if __name__ == "__main__":
    main()
