#!/usr/bin/env python3
"""
BMC Final Professional Draw.io - With dates, comments, and better layout
"""

def generate_final_professional_drawio():
    """Generate final professional Draw.io with dates and comments"""
    xml_content = '''<mxfile host="app.diagrams.net">
  <diagram name="BMC AWS Architecture" id="diagram1">
    <mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="900">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Header with dates and info -->
        <mxCell id="header" value="BMC AWS Architecture - 60M Products Platform" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=none;fontColor=#FFFFFF;fontSize=16;fontStyle=1;align=center;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1300" height="40" as="geometry"/>
        </mxCell>
        
        <mxCell id="dateInfo" value="Implementation: Q1 2024 | Go-Live: Q2 2024 | Cost: $8,650/month | SLA: 99.9%" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;fontSize=10;fontColor=#666666;" vertex="1" parent="1">
          <mxGeometry x="50" y="65" width="1300" height="20" as="geometry"/>
        </mxCell>
        
        <!-- Users with comment -->
        <mxCell id="users" value="BMC Users" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.users;" vertex="1" parent="1">
          <mxGeometry x="80" y="120" width="35" height="35" as="geometry"/>
        </mxCell>
        <mxCell id="usersComment" value="• Web, Mobile, Admin&#xa;• 10,000 concurrent users&#xa;• Multi-tenant access" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF9C4;strokeColor=#F57F17;fontSize=8;align=left;verticalAlign=top;" vertex="1" parent="1">
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
        
        <mxCell id="edgeComment" value="• DDoS Protection&#xa;• SSL Termination&#xa;• Rate Limiting: 1000 req/s" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;fontSize=8;align=left;verticalAlign=top;" vertex="1" parent="1">
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
        <mxCell id="invoice" value="Invoice&#xa;2vCPU/4GB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="200" y="320" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Product Service -->
        <mxCell id="product" value="Product&#xa;4vCPU/8GB&#xa;60M Records" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="370" y="320" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- OCR Service -->
        <mxCell id="ocr" value="OCR&#xa;2vCPU/4GB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;" vertex="1" parent="1">
          <mxGeometry x="540" y="320" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Lambda -->
        <mxCell id="lambda" value="Lambda&#xa;OCR Proc" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lambda;" vertex="1" parent="1">
          <mxGeometry x="620" y="320" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="computeComment" value="• Health Checks: /health&#xa;• Auto Scaling: CPU >70%&#xa;• Blue/Green Deployment&#xa;• Container Insights enabled" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#FF9800;fontSize=8;align=left;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="750" y="260" width="150" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Data Layer Group -->
        <mxCell id="dataGroup" value="Data Layer - Multi-AZ with 35-day backup retention" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#4CAF50;strokeWidth=2;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=8;" vertex="1" parent="1">
          <mxGeometry x="80" y="420" width="450" height="120" as="geometry"/>
        </mxCell>
        
        <!-- RDS -->
        <mxCell id="rds" value="RDS&#xa;PostgreSQL&#xa;60M Products" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.rds;" vertex="1" parent="1">
          <mxGeometry x="150" y="460" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Redis -->
        <mxCell id="redis" value="Redis&#xa;Cache&#xa;24h TTL" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elasticache;" vertex="1" parent="1">
          <mxGeometry x="280" y="460" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- S3 -->
        <mxCell id="s3" value="S3&#xa;Documents&#xa;Intelligent" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;" vertex="1" parent="1">
          <mxGeometry x="410" y="460" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="dataComment" value="• RTO: 4 hours | RPO: 1 hour&#xa;• Cross-region replication&#xa;• Encryption at rest (KMS)&#xa;• Performance Insights enabled" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#4CAF50;fontSize=8;align=left;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="550" y="440" width="150" height="60" as="geometry"/>
        </mxCell>
        
        <!-- AI/ML Group -->
        <mxCell id="aiGroup" value="AI/ML Services - >95% OCR Accuracy" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4EC;strokeColor=#E91E63;strokeWidth=2;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=8;" vertex="1" parent="1">
          <mxGeometry x="750" y="420" width="200" height="120" as="geometry"/>
        </mxCell>
        
        <!-- Textract -->
        <mxCell id="textract" value="Textract&#xa;OCR >95%&#xa;Forms Analysis" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.textract;" vertex="1" parent="1">
          <mxGeometry x="820" y="460" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="aiComment" value="• Async processing&#xa;• Confidence threshold: 95%&#xa;• Manual review queue&#xa;• Multi-language support" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4EC;strokeColor=#E91E63;fontSize=8;align=left;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="970" y="440" width="130" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Integration Group -->
        <mxCell id="integrationGroup" value="Event-Driven Integration - 10,000 invoices/hour" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F3E5F5;strokeColor=#9C27B0;strokeWidth=2;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=8;" vertex="1" parent="1">
          <mxGeometry x="80" y="580" width="400" height="100" as="geometry"/>
        </mxCell>
        
        <!-- SQS -->
        <mxCell id="sqs" value="SQS&#xa;FIFO Queue" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sqs;" vertex="1" parent="1">
          <mxGeometry x="150" y="620" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- SNS -->
        <mxCell id="sns" value="SNS&#xa;Notifications" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sns;" vertex="1" parent="1">
          <mxGeometry x="280" y="620" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- EventBridge -->
        <mxCell id="eventbridge" value="EventBridge&#xa;Event Bus" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.eventbridge;" vertex="1" parent="1">
          <mxGeometry x="410" y="620" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- Monitoring Group -->
        <mxCell id="monitoringGroup" value="Monitoring & Observability - 99.9% SLA" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF8E1;strokeColor=#FFC107;strokeWidth=2;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=8;" vertex="1" parent="1">
          <mxGeometry x="520" y="580" width="300" height="100" as="geometry"/>
        </mxCell>
        
        <!-- CloudWatch -->
        <mxCell id="cloudwatch" value="CloudWatch&#xa;Metrics/Logs" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F34482;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudwatch;" vertex="1" parent="1">
          <mxGeometry x="580" y="620" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- X-Ray -->
        <mxCell id="xray" value="X-Ray&#xa;Tracing" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F34482;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.x_ray;" vertex="1" parent="1">
          <mxGeometry x="720" y="620" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <!-- External Systems -->
        <mxCell id="dian" value="DIAN API&#xa;Tax Authority" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#607D8B;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=8;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.internet_gateway;" vertex="1" parent="1">
          <mxGeometry x="1000" y="320" width="35" height="35" as="geometry"/>
        </mxCell>
        
        <mxCell id="externalComment" value="• DIAN API: 1000 req/hour&#xa;• OAuth 2.0 authentication&#xa;• Circuit breaker pattern&#xa;• Fallback to cached data" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ECEFF1;strokeColor=#607D8B;fontSize=8;align=left;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="1050" y="300" width="140" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Performance Metrics -->
        <mxCell id="metrics" value="Performance KPIs" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1F5FE;strokeColor=#0277BD;fontSize=10;fontStyle=1;verticalAlign=top;spacingTop=5;" vertex="1" parent="1">
          <mxGeometry x="850" y="580" width="200" height="100" as="geometry"/>
        </mxCell>
        
        <mxCell id="metricsText" value="• OCR Processing: <5s&#xa;• Product Lookup: <500ms&#xa;• Invoice Processing: <3s&#xa;• System Availability: >99.9%&#xa;• Throughput: 10K invoices/hour" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;fontSize=8;" vertex="1" parent="1">
          <mxGeometry x="860" y="605" width="180" height="70" as="geometry"/>
        </mxCell>
        
        <!-- Implementation Timeline -->
        <mxCell id="timeline" value="Implementation Timeline" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFEBEE;strokeColor=#C62828;fontSize=10;fontStyle=1;verticalAlign=top;spacingTop=5;" vertex="1" parent="1">
          <mxGeometry x="1070" y="580" width="280" height="100" as="geometry"/>
        </mxCell>
        
        <mxCell id="timelineText" value="Phase 1 (Weeks 1-8): Foundation & 60M Products Migration&#xa;Phase 2 (Weeks 9-16): OCR & Document Processing&#xa;Phase 3 (Weeks 17-22): Business Logic & Commission Calc&#xa;Phase 4 (Weeks 23-26): Frontend & SFTP Integration&#xa;Phase 5 (Weeks 27-30): Go-Live & Optimization" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;fontSize=8;" vertex="1" parent="1">
          <mxGeometry x="1080" y="605" width="260" height="70" as="geometry"/>
        </mxCell>'''
    
    return xml_content

def add_final_connections():
    """Add final professional connections with labels"""
    connections = '''
        <!-- Professional connections with performance labels -->
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
        <mxCell id="edge12" value=">95% OCR" style="endArrow=classic;html=1;rounded=0;strokeColor=#E91E63;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="lambda" target="textract"/>
        <mxCell id="edge13" value="Classify" style="endArrow=classic;html=1;rounded=0;strokeColor=#607D8B;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="product" target="dian"/>
        <mxCell id="edge14" value="Events" style="endArrow=classic;html=1;rounded=0;strokeColor=#9C27B0;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="invoice" target="eventbridge"/>
        <mxCell id="edge15" value="Queue" style="endArrow=classic;html=1;rounded=0;strokeColor=#9C27B0;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="eventbridge" target="sqs"/>
        <mxCell id="edge16" value="Notify" style="endArrow=classic;html=1;rounded=0;strokeColor=#9C27B0;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="sqs" target="sns"/>
        <mxCell id="edge17" value="Metrics" style="endArrow=classic;html=1;rounded=0;strokeColor=#FFC107;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="product" target="cloudwatch"/>
        <mxCell id="edge18" value="Trace" style="endArrow=classic;html=1;rounded=0;strokeColor=#FFC107;strokeWidth=2;fontSize=8;" edge="1" parent="1" source="invoice" target="xray"/>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    return connections

def main():
    print("🚀 BMC Final Professional Draw.io - Complete with Dates & Comments")
    print("=" * 70)
    
    # Generate complete professional XML with dates and comments
    xml_content = generate_final_professional_drawio() + add_final_connections()
    
    with open("bmc_final_professional.drawio", "w", encoding="utf-8") as f:
        f.write(xml_content)
    
    print("✓ Final professional architecture generated: bmc_final_professional.drawio")
    print("🎨 Enhanced features:")
    print("  - Implementation dates and timeline")
    print("  - Performance KPIs and metrics")
    print("  - Detailed comments for each group")
    print("  - Cost information ($8,650/month)")
    print("  - SLA targets (99.9%)")
    print("  - Connection labels with performance data")
    print("  - Professional color-coded groups")
    print("  - Compact 35px icons with detailed info")
    print("🔗 Open at: https://app.diagrams.net")

if __name__ == "__main__":
    main()
