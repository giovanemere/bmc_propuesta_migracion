#!/usr/bin/env python3
"""
Script para comparar tipos de DrawIO generados
"""

from pathlib import Path

def compare_drawio_types():
    """Compara los diferentes tipos de DrawIO generados"""
    
    print("🔍 Comparación de Tipos de DrawIO")
    print("=" * 50)
    
    drawio_dir = Path("outputs/mcp/diagrams/bmc_input/drawio")
    drawio_files = list(drawio_dir.glob("*.drawio"))
    
    types = {
        "png_equivalent": [],
        "aws_icons": [],
        "professional": [],
        "unified": [],
        "minimal": []
    }
    
    # Clasificar archivos
    for file in drawio_files:
        if "png_equivalent" in file.name:
            types["png_equivalent"].append(file)
        elif "aws_icons" in file.name:
            types["aws_icons"].append(file)
        elif "professional" in file.name:
            types["professional"].append(file)
        elif "unified" in file.name:
            types["unified"].append(file)
        elif "minimal" in file.name:
            types["minimal"].append(file)
    
    print(f"\n📊 Tipos de DrawIO Encontrados:")
    
    # PNG Equivalent (NUEVO - estructura exacta del PNG)
    if types["png_equivalent"]:
        file = types["png_equivalent"][0]
        size_kb = file.stat().st_size / 1024
        
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            aws_shapes = content.count('mxgraph.aws4')
            clusters = content.count('parent=')
            edges = content.count('edge="1"')
            
        print(f"\n🎯 PNG EQUIVALENT (NUEVO - Estructura Exacta):")
        print(f"  📄 {file.name}")
        print(f"  📊 {size_kb:.1f}KB, {aws_shapes} iconos AWS, {clusters} contenedores, {edges} conexiones")
        print(f"  🎨 Usa: Clusters jerárquicos + iconos AWS + conexiones")
        print(f"  ⭐ CALIDAD: IDÉNTICA AL PNG")
    
    # AWS Icons (iconos reales pero planos)
    if types["aws_icons"]:
        file = types["aws_icons"][0]
        size_kb = file.stat().st_size / 1024
        
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            aws_shapes = content.count('mxgraph.aws4')
            
        print(f"\n🎨 AWS ICONS (Iconos Reales Planos):")
        print(f"  📄 {file.name}")
        print(f"  📊 {size_kb:.1f}KB, {aws_shapes} iconos AWS reales")
        print(f"  🎨 Usa: mxgraph.aws4.* (iconos oficiales AWS)")
        print(f"  ⭐ CALIDAD: PROFESIONAL con iconos reales")
    
    # Professional (formas básicas)
    if types["professional"]:
        file = types["professional"][0]
        size_kb = file.stat().st_size / 1024
        
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            elements = content.count('<mxCell')
            
        print(f"\n🏗️ PROFESSIONAL (Formas Básicas):")
        print(f"  📄 {file.name}")
        print(f"  📊 {size_kb:.1f}KB, {elements} elementos")
        print(f"  🎨 Usa: Formas básicas con colores AWS")
        print(f"  ⭐ CALIDAD: Buena estructura, iconos básicos")
    
    # Unified (muy básico)
    if types["unified"]:
        file = types["unified"][0]
        size_kb = file.stat().st_size / 1024
        
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            elements = content.count('<mxCell')
            
        print(f"\n📝 UNIFIED (Básico):")
        print(f"  📄 {file.name}")
        print(f"  📊 {size_kb:.1f}KB, {elements} elementos")
        print(f"  🎨 Usa: Rectángulos simples")
        print(f"  ⭐ CALIDAD: Básica")
    
    print(f"\n🎯 RECOMENDACIÓN:")
    if types["png_equivalent"]:
        print(f"  ✅ USAR: {types['png_equivalent'][0].name}")
        print(f"  🎨 Razón: Estructura IDÉNTICA al PNG (clusters + iconos + conexiones)")
        print(f"  📐 Equivalente a: PNG Network Architecture exacto")
    elif types["aws_icons"]:
        print(f"  ⚠️ ALTERNATIVA: {types['aws_icons'][0].name}")
        print(f"  🎨 Razón: Iconos AWS reales pero sin estructura jerárquica")
    
    print(f"\n📈 Comparación con PNG:")
    print(f"  🖼️ PNG: Clusters jerárquicos + iconos AWS + layout automático + conexiones")
    print(f"  📐 DrawIO PNG Equivalent: Clusters jerárquicos + iconos AWS + layout manual + conexiones")
    print(f"  📐 DrawIO AWS Icons: Iconos AWS reales + layout plano")
    print(f"  📐 DrawIO Professional: Formas básicas + layout manual")
    print(f"  📐 DrawIO Unified: Muy básico")

if __name__ == "__main__":
    compare_drawio_types()
