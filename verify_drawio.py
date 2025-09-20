#!/usr/bin/env python3
"""
Script para verificar contenido del DrawIO profesional
"""

from pathlib import Path
import xml.etree.ElementTree as ET

def verify_drawio_professional():
    """Verifica el contenido del DrawIO profesional"""
    
    print("🔍 Verificación DrawIO Profesional")
    print("=" * 40)
    
    drawio_files = list(Path("outputs/mcp/diagrams/bmc_input/drawio").glob("*professional*.drawio"))
    
    if not drawio_files:
        print("❌ No se encontró archivo DrawIO profesional")
        return
    
    drawio_file = drawio_files[0]
    print(f"📄 Archivo: {drawio_file.name}")
    
    # Parsear XML
    try:
        tree = ET.parse(drawio_file)
        root = tree.getroot()
        
        # Contar elementos
        cells = root.findall(".//mxCell")
        print(f"📊 Total elementos: {len(cells)}")
        
        # Analizar contenido
        components = []
        for cell in cells:
            value = cell.get('value', '')
            if value and value not in ['', '0', '1']:
                components.append(value.split('\\n')[0])  # Primera línea
        
        print(f"\n🏗️ Componentes encontrados ({len(components)}):")
        for i, comp in enumerate(components, 1):
            print(f"  {i:2d}. {comp}")
        
        # Verificar arquitectura AWS
        aws_keywords = [
            'VPC', 'Subnet', 'Availability Zone', 'RDS', 'ElastiCache',
            'CloudFront', 'API Gateway', 'Cognito', 'Fargate', 'S3',
            'NAT Gateway', 'Application LB', 'WAF'
        ]
        
        content = ET.tostring(root, encoding='unicode')
        found_aws = [kw for kw in aws_keywords if kw in content]
        
        print(f"\n☁️ Componentes AWS ({len(found_aws)}/{len(aws_keywords)}):")
        for aws_comp in found_aws:
            print(f"  ✅ {aws_comp}")
        
        missing_aws = [kw for kw in aws_keywords if kw not in found_aws]
        if missing_aws:
            print(f"\n⚠️ Componentes faltantes:")
            for missing in missing_aws:
                print(f"  ❌ {missing}")
        
        # Verificar estructura
        diagrams = root.findall(".//diagram")
        print(f"\n📋 Diagramas: {len(diagrams)}")
        for diagram in diagrams:
            name = diagram.get('name', 'Sin nombre')
            print(f"  📊 {name}")
        
        # Calificación
        score = len(found_aws) / len(aws_keywords) * 100
        print(f"\n🎯 Calificación: {score:.1f}%")
        
        if score >= 80:
            print("  🎉 EXCELENTE - Arquitectura profesional completa")
        elif score >= 60:
            print("  👍 BUENO - Arquitectura sólida")
        elif score >= 40:
            print("  ⚠️ REGULAR - Necesita mejoras")
        else:
            print("  ❌ BÁSICO - Requiere rediseño")
            
    except Exception as e:
        print(f"❌ Error al parsear XML: {e}")

if __name__ == "__main__":
    verify_drawio_professional()
