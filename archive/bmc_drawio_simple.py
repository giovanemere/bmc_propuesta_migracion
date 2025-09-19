#!/usr/bin/env python3
"""
BMC Draw.io Generator - Simple Valid XML
"""

def generate_drawio_xml():
    """Generate valid Draw.io XML"""
    xml_content = '''<mxfile host="app.diagrams.net" modified="2024-01-01T00:00:00.000Z" agent="BMC Generator" version="22.1.11" etag="abc123">
  <diagram name="BMC AWS Architecture" id="diagram1">
    <mxGraphModel dx="1422" dy="794" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Users -->
        <mxCell id="users" value="BMC Users" style="shape=actor;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="50" width="80" height="60" as="geometry"/>
        </mxCell>
        
        <!-- API Gateway -->
        <mxCell id="api" value="API Gateway" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="200" y="50" width="120" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Load Balancer -->
        <mxCell id="alb" value="Application LB" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="400" y="50" width="120" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Invoice Service -->
        <mxCell id="invoice" value="Invoice Service&#xa;2 vCPU, 4GB" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="200" y="200" width="120" height="80" as="geometry"/>
        </mxCell>
        
        <!-- Product Service -->
        <mxCell id="product" value="Product Service&#xa;4 vCPU, 8GB&#xa;60M Products" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="400" y="200" width="120" height="80" as="geometry"/>
        </mxCell>
        
        <!-- OCR Service -->
        <mxCell id="ocr" value="OCR Service&#xa;2 vCPU, 4GB" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="600" y="200" width="120" height="80" as="geometry"/>
        </mxCell>
        
        <!-- RDS -->
        <mxCell id="rds" value="RDS PostgreSQL&#xa;60M Products&#xa;Multi-AZ" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
          <mxGeometry x="200" y="350" width="120" height="80" as="geometry"/>
        </mxCell>
        
        <!-- Redis -->
        <mxCell id="redis" value="ElastiCache Redis&#xa;Product Cache&#xa;24h TTL" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="400" y="350" width="120" height="80" as="geometry"/>
        </mxCell>
        
        <!-- S3 -->
        <mxCell id="s3" value="S3 Documents&#xa;Intelligent Tiering" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="600" y="350" width="120" height="80" as="geometry"/>
        </mxCell>
        
        <!-- Textract -->
        <mxCell id="textract" value="Amazon Textract&#xa;OCR &gt;95%" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;" vertex="1" parent="1">
          <mxGeometry x="800" y="200" width="120" height="80" as="geometry"/>
        </mxCell>
        
        <!-- CloudWatch -->
        <mxCell id="cloudwatch" value="CloudWatch&#xa;Metrics &amp; Logs" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="400" y="500" width="120" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Connections -->
        <mxCell id="edge1" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1" source="users" target="api">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="390" y="400" as="sourcePoint"/>
            <mxPoint x="440" y="350" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="edge2" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1" source="api" target="alb">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="390" y="400" as="sourcePoint"/>
            <mxPoint x="440" y="350" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="edge3" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1" source="alb" target="invoice">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="390" y="400" as="sourcePoint"/>
            <mxPoint x="440" y="350" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="edge4" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1" source="alb" target="product">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="390" y="400" as="sourcePoint"/>
            <mxPoint x="440" y="350" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="edge5" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1" source="alb" target="ocr">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="390" y="400" as="sourcePoint"/>
            <mxPoint x="440" y="350" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="edge6" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1" source="product" target="redis">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="390" y="400" as="sourcePoint"/>
            <mxPoint x="440" y="350" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="edge7" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1" source="redis" target="rds">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="390" y="400" as="sourcePoint"/>
            <mxPoint x="440" y="350" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="edge8" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1" source="ocr" target="s3">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="390" y="400" as="sourcePoint"/>
            <mxPoint x="440" y="350" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="edge9" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1" source="ocr" target="textract">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="390" y="400" as="sourcePoint"/>
            <mxPoint x="440" y="350" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="edge10" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1" source="invoice" target="cloudwatch">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="390" y="400" as="sourcePoint"/>
            <mxPoint x="440" y="350" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="edge11" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1" source="product" target="cloudwatch">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="390" y="400" as="sourcePoint"/>
            <mxPoint x="440" y="350" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    return xml_content

def main():
    print("🚀 BMC Draw.io Generator - Valid XML")
    print("=" * 40)
    
    # Generate Draw.io file
    xml_content = generate_drawio_xml()
    
    with open("bmc_architecture.drawio", "w", encoding="utf-8") as f:
        f.write(xml_content)
    
    print("✓ Draw.io file generated: bmc_architecture.drawio")
    print("🔗 Open at: https://app.diagrams.net")

if __name__ == "__main__":
    main()
