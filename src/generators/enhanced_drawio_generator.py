#!/usr/bin/env python3
"""
Enhanced DrawIO Generator - DrawIO con detalles profesionales mejorados
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

class EnhancedDrawIOGenerator:
    """Generador DrawIO con detalles profesionales mejorados"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str):
        self.config = config
        self.output_dir = Path(output_dir)
    
    def generate_detailed_drawio(self, project_name: str = "bmc_input") -> str:
        """Genera DrawIO con detalles profesionales mejorados"""
        
        # Crear XML DrawIO con más detalles
        mxfile = ET.Element("mxfile", host="app.diagrams.net")
        diagram = ET.SubElement(mxfile, "diagram", name=f"{project_name} Detailed Architecture", id="detailed")
        model = ET.SubElement(diagram, "mxGraphModel", dx="3200", dy="2400", grid="1", gridSize="10")
        root = ET.SubElement(model, "root")
        
        # Celdas base
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        
        cell_id = 2
        
        # Título con más información
        title = ET.SubElement(root, "mxCell",
            id=str(cell_id), 
            value=f"{project_name.upper()} - Detailed AWS Architecture\\nBMC Bolsa Comisionista - 60M Products, 10K Invoices/hour",
            style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;fontColor=#FFFFFF;fontSize=16;fontStyle=1;",
            vertex="1", parent="1"
        )
        ET.SubElement(title, "mxGeometry", x="50", y="20", width="2800", height="70", **{"as": "geometry"})
        cell_id += 1
        
        # Usuarios con más detalle
        users = ET.SubElement(root, "mxCell",
            id=str(cell_id), 
            value="BMC Users\\n10K Concurrent\\nWeb + Mobile\\nColombia",
            style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#4CAF50;strokeColor=#2E7D32;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=11;fontStyle=1;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.users;",
            vertex="1", parent="1"
        )
        ET.SubElement(users, "mxGeometry", x="100", y="120", width="90", height="90", **{"as": "geometry"})
        users_id = cell_id
        cell_id += 1
        
        # Internet con más detalle
        internet = ET.SubElement(root, "mxCell",
            id=str(cell_id), 
            value="Internet\\nHTTPS/TLS 1.3\\nGlobal CDN\\nLatency < 50ms",
            style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#1976D2;gradientDirection=north;fillColor=#0D47A1;strokeColor=#0277BD;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=11;fontStyle=1;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.internet_gateway;",
            vertex="1", parent="1"
        )
        ET.SubElement(internet, "mxGeometry", x="350", y="120", width="90", height="90", **{"as": "geometry"})
        internet_id = cell_id
        cell_id += 1
        
        # AWS Cloud con región específica
        aws_cloud = ET.SubElement(root, "mxCell",
            id=str(cell_id), 
            value="AWS Cloud - us-east-1 (N. Virginia)\\nProduction Environment - 99.99% SLA",
            style="fillColor=#E3F2FD;strokeColor=#1976D2;strokeWidth=3;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#1976D2;whiteSpace=wrap;html=1;fontSize=14;",
            vertex="1", parent="1"
        )
        ET.SubElement(aws_cloud, "mxGeometry", x="50", y="250", width="2700", height="1800", **{"as": "geometry"})
        aws_cloud_id = cell_id
        cell_id += 1
        
        return self._add_detailed_components(root, aws_cloud_id, cell_id, project_name)
    
    def _add_detailed_components(self, root, aws_cloud_id, cell_id, project_name):
        """Agrega componentes detallados al DrawIO"""
        
        # Edge Layer con más servicios
        edge_layer = ET.SubElement(root, "mxCell",
            id=str(cell_id), 
            value="Edge & CDN Layer\\nGlobal Distribution - 200+ Edge Locations",
            style="fillColor=#FFEBEE;strokeColor=#F44336;strokeWidth=2;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#C62828;whiteSpace=wrap;html=1;fontSize=12;",
            vertex="1", parent=str(aws_cloud_id)
        )
        ET.SubElement(edge_layer, "mxGeometry", x="100", y="80", width="800", height="200", **{"as": "geometry"})
        edge_layer_id = cell_id
        cell_id += 1
        
        # CloudFront detallado
        cloudfront = ET.SubElement(root, "mxCell",
            id=str(cell_id), 
            value="CloudFront CDN\\nGlobal Edge Caching\\nSSL/TLS Termination\\nGZIP Compression\\nCache TTL: 24h",
            style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#4527A0;strokeWidth=2;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=1;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudfront;",
            vertex="1", parent=str(edge_layer_id)
        )
        ET.SubElement(cloudfront, "mxGeometry", x="50", y="80", width="100", height="100", **{"as": "geometry"})
        cloudfront_id = cell_id
        cell_id += 1
        
        # WAF detallado
        waf = ET.SubElement(root, "mxCell",
            id=str(cell_id), 
            value="AWS WAF\\nDDoS Protection\\nSQL Injection Block\\nXSS Prevention\\nRate Limiting: 1000/min",
            style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#B71C1C;strokeWidth=2;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=1;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.waf;",
            vertex="1", parent=str(edge_layer_id)
        )
        ET.SubElement(waf, "mxGeometry", x="200", y="80", width="100", height="100", **{"as": "geometry"})
        waf_id = cell_id
        cell_id += 1
        
        # Route 53 para DNS
        route53 = ET.SubElement(root, "mxCell",
            id=str(cell_id), 
            value="Route 53\\nDNS Management\\nHealth Checks\\nFailover Routing\\nLatency-based",
            style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#4527A0;strokeWidth=2;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=1;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.route_53;",
            vertex="1", parent=str(edge_layer_id)
        )
        ET.SubElement(route53, "mxGeometry", x="350", y="80", width="100", height="100", **{"as": "geometry"})
        cell_id += 1
        
        # Continuar con más componentes detallados...
        return self._add_vpc_details(root, aws_cloud_id, cell_id, project_name)
    
    def _add_vpc_details(self, root, aws_cloud_id, cell_id, project_name):
        """Agrega detalles de VPC y subnets"""
        
        # VPC con más información
        vpc = ET.SubElement(root, "mxCell",
            id=str(cell_id), 
            value="VPC 10.0.0.0/16\\nBMC Production Environment\\nDHCP Options Set\\nFlow Logs Enabled\\nDNS Resolution: Enabled",
            style="fillColor=#F5F5F5;strokeColor=#666666;strokeWidth=2;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#424242;whiteSpace=wrap;html=1;fontSize=12;",
            vertex="1", parent=str(aws_cloud_id)
        )
        ET.SubElement(vpc, "mxGeometry", x="100", y="320", width="2400", height="1400", **{"as": "geometry"})
        vpc_id = cell_id
        cell_id += 1
        
        # Availability Zone A con más detalle
        az_a = ET.SubElement(root, "mxCell",
            id=str(cell_id), 
            value="Availability Zone us-east-1a\\nPrimary AZ - Active\\nLatency: < 1ms intra-AZ",
            style="fillColor=#E8F5E8;strokeColor=#4CAF50;strokeWidth=2;dashed=1;verticalAlign=top;fontStyle=1;fontColor=#2E7D32;whiteSpace=wrap;html=1;fontSize=11;",
            vertex="1", parent=str(vpc_id)
        )
        ET.SubElement(az_a, "mxGeometry", x="50", y="80", width="1100", height="1200", **{"as": "geometry"})
        az_a_id = cell_id
        cell_id += 1
        
        # Guardar archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{project_name}_detailed_architecture_{timestamp}.drawio"
        output_path = self.output_dir / "drawio" / filename
        
        # Generar XML final
        ET.indent(ET.ElementTree(root).getroot(), space="  ")
        xml_str = ET.tostring(ET.ElementTree(root).getroot(), encoding='unicode', xml_declaration=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>\n')
            f.write('<mxfile host="app.diagrams.net">\n')
            f.write('  <diagram name="BMC Detailed Architecture" id="detailed">\n')
            f.write('    <mxGraphModel dx="3200" dy="2400" grid="1" gridSize="10">\n')
            f.write('      <root>\n')
            
            # Escribir celdas generadas
            for cell in root:
                cell_xml = ET.tostring(cell, encoding='unicode')
                f.write(f"        {cell_xml}\n")
            
            f.write('      </root>\n')
            f.write('    </mxGraphModel>\n')
            f.write('  </diagram>\n')
            f.write('</mxfile>\n')
        
        return str(output_path)
