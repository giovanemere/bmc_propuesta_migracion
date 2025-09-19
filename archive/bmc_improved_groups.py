#!/usr/bin/env python3
"""
BMC Improved Draw.io - Better groups and arrows
"""

def generate_improved_drawio():
    """Generate improved Draw.io with On-Premise/Cloud groups and better arrows"""
    xml_content = '''<mxfile host="app.diagrams.net">
  <diagram name="BMC AWS Architecture" id="diagram1">
    <mxGraphModel dx="1800" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1600" pageHeight="1000">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Title -->
        <mxCell id="title" value="BMC AWS Architecture - 60M Products Platform" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=none;fontColor=#FFFFFF;fontSize=18;fontStyle=1;align=center;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1500" height="50" as="geometry"/>
        </mxCell>
        
        <!-- On-Premise Group -->
        <mxCell id="onPremiseGroup" value="On-Premise / External" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFEBEE;strokeColor=#D32F2F;strokeWidth=3;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=15;dashed=1;dashPattern=5 5;" vertex="1" parent="1">
          <mxGeometry x="50" y="100" width="300" height="200" as="geometry"/>
        </mxCell>
        
        <!-- Users -->
        <mxCell id="users" value="BMC Users&#10;Web/Mobile/Admin" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.users;" vertex="1" parent="1">
          <mxGeometry x="100" y="140" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- DIAN API -->
        <mxCell id="dian" value="DIAN API&#10;Tax Authority" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#607D8B;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.internet_gateway;" vertex="1" parent="1">
          <mxGeometry x="250" y="140" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- SFTP Systems -->
        <mxCell id="sftp" value="SFTP Systems&#10;File Transfer" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#795548;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.storage_gateway;" vertex="1" parent="1">
          <mxGeometry x="175" y="220" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- AWS Cloud Group -->
        <mxCell id="awsCloudGroup" value="AWS Cloud - us-east-1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;strokeWidth=4;fontSize=16;fontStyle=1;verticalAlign=top;spacingTop=20;dashed=0;" vertex="1" parent="1">
          <mxGeometry x="400" y="100" width="1150" height="850" as="geometry"/>
        </mxCell>
        
        <!-- Edge Security Zone -->
        <mxCell id="edgeZone" value="Edge Security Zone" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#FF9800;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="450" y="150" width="500" height="100" as="geometry"/>
        </mxCell>
        
        <!-- CloudFront -->
        <mxCell id="cloudfront" value="CloudFront&#10;CDN" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudfront;" vertex="1" parent="1">
          <mxGeometry x="480" y="180" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- WAF -->
        <mxCell id="waf" value="WAF&#10;Firewall" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.waf;" vertex="1" parent="1">
          <mxGeometry x="580" y="180" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- API Gateway -->
        <mxCell id="api" value="API Gateway&#10;REST/GraphQL" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.api_gateway;" vertex="1" parent="1">
          <mxGeometry x="680" y="180" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Cognito -->
        <mxCell id="cognito" value="Cognito&#10;Auth" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cognito;" vertex="1" parent="1">
          <mxGeometry x="780" y="180" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Application Zone -->
        <mxCell id="appZone" value="Application Zone - ECS Fargate" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#4CAF50;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="450" y="280" width="700" height="200" as="geometry"/>
        </mxCell>
        
        <!-- ALB -->
        <mxCell id="alb" value="ALB&#10;Load Balancer" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#8C4FFF;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.application_load_balancer;" vertex="1" parent="1">
          <mxGeometry x="680" y="320" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Microservices -->
        <mxCell id="invoice" value="Invoice&#10;2vCPU/4GB&#10;Scale: 2-10" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="500" y="380" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="product" value="Product&#10;4vCPU/8GB&#10;60M Records&#10;Scale: 3-15" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="680" y="380" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="ocr" value="OCR&#10;2vCPU/4GB&#10;Scale: 2-8" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="860" y="380" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="lambda" value="Lambda&#10;OCR Processor" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lambda;" vertex="1" parent="1">
          <mxGeometry x="1040" y="380" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Data Zone -->
        <mxCell id="dataZone" value="Data Zone - Multi-AZ" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4EC;strokeColor=#E91E63;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="450" y="520" width="500" height="150" as="geometry"/>
        </mxCell>
        
        <!-- RDS -->
        <mxCell id="rds" value="RDS&#10;PostgreSQL&#10;60M Products&#10;Multi-AZ" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.rds;" vertex="1" parent="1">
          <mxGeometry x="500" y="570" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Redis -->
        <mxCell id="redis" value="Redis&#10;Cache&#10;24h TTL&#10;Cluster Mode" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elasticache;" vertex="1" parent="1">
          <mxGeometry x="680" y="570" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- S3 -->
        <mxCell id="s3" value="S3&#10;Documents&#10;Intelligent&#10;Tiering" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;" vertex="1" parent="1">
          <mxGeometry x="860" y="570" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- AI/ML Zone -->
        <mxCell id="aiZone" value="AI/ML Zone" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F3E5F5;strokeColor=#9C27B0;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="1000" y="520" width="200" height="150" as="geometry"/>
        </mxCell>
        
        <!-- Textract -->
        <mxCell id="textract" value="Textract&#10;OCR Service&#10;Accuracy: 95%&#10;Forms Analysis" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.textract;" vertex="1" parent="1">
          <mxGeometry x="1080" y="570" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Integration Zone -->
        <mxCell id="integrationZone" value="Integration Zone - Event-Driven" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF8E1;strokeColor=#FFC107;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="450" y="720" width="500" height="150" as="geometry"/>
        </mxCell>
        
        <!-- SQS -->
        <mxCell id="sqs" value="SQS&#10;FIFO Queue&#10;Invoice Processing" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sqs;" vertex="1" parent="1">
          <mxGeometry x="500" y="770" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- SNS -->
        <mxCell id="sns" value="SNS&#10;Notifications&#10;Multi-channel" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sns;" vertex="1" parent="1">
          <mxGeometry x="680" y="770" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- EventBridge -->
        <mxCell id="eventbridge" value="EventBridge&#10;Event Bus&#10;10K events/hour" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.eventbridge;" vertex="1" parent="1">
          <mxGeometry x="860" y="770" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Monitoring Zone -->
        <mxCell id="monitoringZone" value="Monitoring Zone - Observability" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ECEFF1;strokeColor=#607D8B;strokeWidth=2;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="1000" y="720" width="300" height="150" as="geometry"/>
        </mxCell>
        
        <!-- CloudWatch -->
        <mxCell id="cloudwatch" value="CloudWatch&#10;Metrics/Logs&#10;99.9% SLA" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F34482;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudwatch;" vertex="1" parent="1">
          <mxGeometry x="1050" y="770" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- X-Ray -->
        <mxCell id="xray" value="X-Ray&#10;Distributed&#10;Tracing" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F34482;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.x_ray;" vertex="1" parent="1">
          <mxGeometry x="1200" y="770" width="35" height="35" as="geometry"/>
        </mxCell>'''
    
    return xml_content

def add_improved_connections():
    """Add improved connections with clear flow"""
    connections = '''
        <!-- Improved connections with clear data flow -->
        
        <!-- User to Edge -->
        <mxCell id="edge1" value="HTTPS&#10;10K users" style="endArrow=classic;html=1;rounded=0;strokeColor=#1976D2;strokeWidth=3;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="users" target="cloudfront">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="400" y="400" as="sourcePoint"/>
            <mxPoint x="450" y="350" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <!-- Edge Security Flow -->
        <mxCell id="edge2" value="CDN&#10;Global" style="endArrow=classic;html=1;rounded=0;strokeColor=#FF9800;strokeWidth=3;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="cloudfront" target="waf"/>
        <mxCell id="edge3" value="Filter&#10;DDoS" style="endArrow=classic;html=1;rounded=0;strokeColor=#FF9800;strokeWidth=3;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="waf" target="api"/>
        <mxCell id="edge4" value="Auth&#10;JWT" style="endArrow=classic;html=1;rounded=0;strokeColor=#FF9800;strokeWidth=2;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="api" target="cognito"/>
        
        <!-- API to Load Balancer -->
        <mxCell id="edge5" value="Route&#10;REST/GraphQL" style="endArrow=classic;html=1;rounded=0;strokeColor=#4CAF50;strokeWidth=3;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="api" target="alb"/>
        
        <!-- Load Balancer to Services -->
        <mxCell id="edge6" value="Scale&#10;2-10 inst" style="endArrow=classic;html=1;rounded=0;strokeColor=#4CAF50;strokeWidth=2;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="alb" target="invoice"/>
        <mxCell id="edge7" value="Scale&#10;3-15 inst" style="endArrow=classic;html=1;rounded=0;strokeColor=#4CAF50;strokeWidth=3;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="alb" target="product"/>
        <mxCell id="edge8" value="Scale&#10;2-8 inst" style="endArrow=classic;html=1;rounded=0;strokeColor=#4CAF50;strokeWidth=2;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="alb" target="ocr"/>
        
        <!-- Data Flow -->
        <mxCell id="edge9" value="Lookup&#10;60M Products&#10;500ms" style="endArrow=classic;html=1;rounded=0;strokeColor=#9C27B0;strokeWidth=3;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="product" target="redis"/>
        <mxCell id="edge10" value="Cache Miss&#10;Query DB" style="endArrow=classic;html=1;rounded=0;strokeColor=#9C27B0;strokeWidth=2;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="redis" target="rds"/>
        
        <!-- Document Processing -->
        <mxCell id="edge11" value="Store&#10;Documents" style="endArrow=classic;html=1;rounded=0;strokeColor=#E91E63;strokeWidth=2;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="ocr" target="s3"/>
        <mxCell id="edge12" value="Process&#10;OCR 95%" style="endArrow=classic;html=1;rounded=0;strokeColor=#E91E63;strokeWidth=3;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="lambda" target="textract"/>
        <mxCell id="edge13" value="Trigger&#10;Lambda" style="endArrow=classic;html=1;rounded=0;strokeColor=#E91E63;strokeWidth=2;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="ocr" target="lambda"/>
        
        <!-- External Integration -->
        <mxCell id="edge14" value="Classify&#10;1000 req/h" style="endArrow=classic;html=1;rounded=0;strokeColor=#607D8B;strokeWidth=2;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="product" target="dian"/>
        
        <!-- Event Flow -->
        <mxCell id="edge15" value="Events&#10;Invoice Process" style="endArrow=classic;html=1;rounded=0;strokeColor=#FFC107;strokeWidth=2;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="invoice" target="eventbridge"/>
        <mxCell id="edge16" value="Queue&#10;FIFO" style="endArrow=classic;html=1;rounded=0;strokeColor=#FFC107;strokeWidth=2;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="eventbridge" target="sqs"/>
        <mxCell id="edge17" value="Notify&#10;Multi-channel" style="endArrow=classic;html=1;rounded=0;strokeColor=#FFC107;strokeWidth=2;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="sqs" target="sns"/>
        
        <!-- Monitoring -->
        <mxCell id="edge18" value="Metrics&#10;Real-time" style="endArrow=classic;html=1;rounded=0;strokeColor=#795548;strokeWidth=2;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="product" target="cloudwatch"/>
        <mxCell id="edge19" value="Trace&#10;Distributed" style="endArrow=classic;html=1;rounded=0;strokeColor=#795548;strokeWidth=2;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="invoice" target="xray"/>
        
        <!-- SFTP Integration -->
        <mxCell id="edge20" value="File Transfer&#10;Batch Process" style="endArrow=classic;html=1;rounded=0;strokeColor=#795548;strokeWidth=2;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="sftp" target="s3"/>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    return connections

def main():
    print("🚀 BMC Improved Draw.io - Better Groups & Arrows")
    print("=" * 55)
    
    # Generate improved XML with better groups and arrows
    xml_content = generate_improved_drawio() + add_improved_connections()
    
    with open("bmc_improved_architecture.drawio", "w", encoding="utf-8") as f:
        f.write(xml_content)
    
    print("✓ Improved architecture generated: bmc_improved_architecture.drawio")
    print("🎨 Improvements:")
    print("  - Clear On-Premise vs AWS Cloud separation")
    print("  - Organized zones: Edge, Application, Data, AI/ML, Integration, Monitoring")
    print("  - Detailed arrows with data flow labels")
    print("  - Performance metrics on connections")
    print("  - Color-coded zones by function")
    print("  - Professional grouping and layout")
    print("🔗 Open at: https://app.diagrams.net")

if __name__ == "__main__":
    main()
