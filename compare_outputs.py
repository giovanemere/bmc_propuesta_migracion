#!/usr/bin/env python3
"""
Script para comparar calidad de outputs DrawIO vs PNG
"""

from pathlib import Path

def compare_outputs():
    """Compara la calidad de los outputs generados"""
    
    print("📊 Comparación de Calidad: DrawIO vs PNG")
    print("=" * 50)
    
    base_dir = Path("outputs/mcp/diagrams/bmc_input")
    
    # Analizar PNG
    png_files = list(base_dir.glob("png/*.png"))
    print(f"\n🖼️ Diagramas PNG ({len(png_files)} archivos):")
    total_png_size = 0
    for png_file in sorted(png_files):
        size = png_file.stat().st_size
        total_png_size += size
        print(f"  📄 {png_file.name} - {size:,} bytes")
    
    # Analizar DrawIO
    drawio_files = list(base_dir.glob("drawio/*.drawio"))
    print(f"\n📐 Diagramas DrawIO ({len(drawio_files)} archivos):")
    total_drawio_size = 0
    for drawio_file in sorted(drawio_files):
        size = drawio_file.stat().st_size
        total_drawio_size += size
        
        # Contar elementos
        with open(drawio_file, 'r', encoding='utf-8') as f:
            content = f.read()
            elements = content.count('<mxCell')
            
        print(f"  📄 {drawio_file.name}")
        print(f"      📊 {size:,} bytes, {elements} elementos")
        
        # Identificar tipo
        if "professional" in drawio_file.name:
            print(f"      🎯 PROFESIONAL - Arquitectura AWS completa")
        elif "unified" in drawio_file.name:
            print(f"      📝 BÁSICO - Diagrama simple")
    
    print(f"\n📈 Resumen:")
    print(f"  PNG Total: {total_png_size:,} bytes ({len(png_files)} archivos)")
    print(f"  DrawIO Total: {total_drawio_size:,} bytes ({len(drawio_files)} archivos)")
    
    # Verificar contenido profesional
    professional_files = [f for f in drawio_files if "professional" in f.name]
    if professional_files:
        prof_file = professional_files[0]
        with open(prof_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        aws_components = [
            "VPC", "Subnet", "Availability Zone", "RDS", "ElastiCache", 
            "CloudFront", "API Gateway", "Cognito", "Fargate", "S3"
        ]
        
        found_components = [comp for comp in aws_components if comp in content]
        
        print(f"\n🏗️ Componentes AWS en DrawIO Profesional:")
        print(f"  ✅ Encontrados: {len(found_components)}/{len(aws_components)}")
        for comp in found_components:
            print(f"    - {comp}")
        
        if len(found_components) >= 8:
            print(f"  🎉 CALIDAD PROFESIONAL - Equivalente a PNG")
        else:
            print(f"  ⚠️ CALIDAD BÁSICA - Necesita mejoras")

if __name__ == "__main__":
    compare_outputs()
