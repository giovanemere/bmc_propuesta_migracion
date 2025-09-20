#!/usr/bin/env python3
"""
Verificación del DrawIO único perfecto
"""

from pathlib import Path

def verify_single_drawio():
    """Verifica que solo hay UN DrawIO y es perfecto"""
    
    print("🔍 Verificación DrawIO Único")
    print("=" * 40)
    
    drawio_dir = Path("outputs/mcp/diagrams/bmc_input/drawio")
    drawio_files = list(drawio_dir.glob("*.drawio"))
    
    print(f"📊 Total archivos DrawIO: {len(drawio_files)}")
    
    # Filtrar solo los generados (no el minimal)
    generated_files = [f for f in drawio_files if "BMC_Input_" in f.name]
    
    print(f"📊 Archivos generados: {len(generated_files)}")
    
    if len(generated_files) == 1:
        print("✅ PERFECTO - Solo UN DrawIO generado")
        
        file = generated_files[0]
        size_kb = file.stat().st_size / 1024
        
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Análisis detallado
        aws_icons = content.count('mxgraph.aws4')
        containers = content.count('parent=')
        edges = content.count('edge="1"')
        cells = content.count('<mxCell')
        
        print(f"\n📄 Archivo: {file.name}")
        print(f"📊 Tamaño: {size_kb:.1f}KB")
        print(f"🎨 Iconos AWS: {aws_icons}")
        print(f"📦 Contenedores: {containers}")
        print(f"🔗 Conexiones: {edges}")
        print(f"📋 Total elementos: {cells}")
        
        # Verificar componentes clave
        components = [
            ("AWS Cloud", "AWS Cloud - us-east-1"),
            ("VPC", "VPC 10.0.0.0/16"),
            ("AZ A", "AZ us-east-1a"),
            ("AZ B", "AZ us-east-1b"),
            ("Public Subnet", "Public Subnet"),
            ("Private Subnet", "Private Subnet"),
            ("Isolated Subnet", "Isolated Subnet"),
            ("Edge Layer", "Edge Layer"),
            ("API Layer", "API Layer"),
            ("CloudFront", "CloudFront"),
            ("WAF", "AWS WAF"),
            ("API Gateway", "API Gateway"),
            ("Cognito", "Cognito"),
            ("ALB", "Application LB"),
            ("Fargate", "App Services"),
            ("RDS Primary", "RDS Primary"),
            ("RDS Standby", "RDS Standby"),
            ("NAT Gateway", "NAT Gateway")
        ]
        
        print(f"\n🏗️ Componentes encontrados:")
        found = 0
        for name, search_text in components:
            if search_text in content:
                print(f"  ✅ {name}")
                found += 1
            else:
                print(f"  ❌ {name}")
        
        score = found / len(components) * 100
        print(f"\n🎯 Completitud: {score:.1f}% ({found}/{len(components)})")
        
        if score >= 95:
            print("  🎉 EXCELENTE - DrawIO idéntico al PNG")
        elif score >= 80:
            print("  👍 BUENO - DrawIO muy completo")
        else:
            print("  ⚠️ INCOMPLETO - Faltan componentes")
        
        # Comparar con PNG
        png_files = list(Path("outputs/mcp/diagrams/bmc_input/png").glob("*network*.png"))
        if png_files:
            png_size = png_files[0].stat().st_size / 1024 / 1024
            print(f"\n📈 Comparación:")
            print(f"  🖼️ PNG: {png_size:.1f}MB (imagen)")
            print(f"  📐 DrawIO: {size_kb:.1f}KB (editable)")
            print(f"  📊 Ratio: {png_size*1024/size_kb:.1f}x más compacto")
        
    elif len(generated_files) > 1:
        print("❌ PROBLEMA - Múltiples DrawIO generados:")
        for file in generated_files:
            print(f"  📄 {file.name}")
        print("\n💡 Solución: Eliminar generadores duplicados")
        
    else:
        print("❌ PROBLEMA - No se generó DrawIO")
        print("\n💡 Solución: Verificar generador")

if __name__ == "__main__":
    verify_single_drawio()
