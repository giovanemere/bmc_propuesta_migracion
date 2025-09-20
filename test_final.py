#!/usr/bin/env python3
"""
Prueba final de todos los ajustes
"""

from pathlib import Path

def test_final():
    """Prueba final de todos los componentes"""
    
    print("🧪 PRUEBA FINAL - Todos los Ajustes")
    print("=" * 50)
    
    base_dir = Path("outputs/mcp/diagrams/bmc_input")
    
    # Test 1: PNG Profesionales
    png_files = list(base_dir.glob("png/*.png"))
    print(f"\n✅ Test 1 - PNG Profesionales:")
    print(f"  📊 Generados: {len(png_files)}/4 esperados")
    for png in sorted(png_files):
        size_mb = png.stat().st_size / 1024 / 1024
        print(f"    📄 {png.name} ({size_mb:.1f}MB)")
    
    # Test 2: DrawIO con Iconos AWS
    aws_drawio = list(base_dir.glob("drawio/*aws_icons*.drawio"))
    print(f"\n✅ Test 2 - DrawIO con Iconos AWS:")
    print(f"  📊 Generados: {len(aws_drawio)}/1 esperado")
    if aws_drawio:
        file = aws_drawio[0]
        size_kb = file.stat().st_size / 1024
        
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            aws_icons = content.count('mxgraph.aws4')
            
        print(f"    📄 {file.name} ({size_kb:.1f}KB)")
        print(f"    🎨 Iconos AWS: {aws_icons}")
        print(f"    ✅ Calidad: {'PROFESIONAL' if aws_icons >= 10 else 'BÁSICA'}")
    
    # Test 3: Mermaid
    mermaid_files = list(base_dir.glob("mermaid/*.md"))
    print(f"\n✅ Test 3 - Diagramas Mermaid:")
    print(f"  📊 Generados: {len(mermaid_files)}/3 esperados")
    for mermaid in sorted(mermaid_files):
        print(f"    📄 {mermaid.name}")
    
    # Test 4: Prompts MCP
    prompt_files = list(base_dir.glob("prompts/**/*.md"))
    print(f"\n✅ Test 4 - Prompts MCP:")
    print(f"  📊 Generados: {len(prompt_files)}/3 esperados")
    for prompt in sorted(prompt_files):
        print(f"    📄 {prompt.name}")
    
    # Test 5: Documentación
    doc_files = list(base_dir.glob("documentation/**/*.md"))
    print(f"\n✅ Test 5 - Documentación:")
    print(f"  📊 Generados: {len(doc_files)}/4 esperados")
    for doc in sorted(doc_files):
        print(f"    📄 {doc.name}")
    
    # Resumen final
    total_files = len(png_files) + len(aws_drawio) + len(mermaid_files) + len(prompt_files) + len(doc_files)
    expected_files = 4 + 1 + 3 + 3 + 4  # 15 archivos principales
    
    print(f"\n🎯 RESUMEN FINAL:")
    print(f"  📊 Archivos generados: {total_files}/{expected_files}")
    print(f"  🖼️ PNG profesionales: {'✅' if len(png_files) == 4 else '❌'}")
    print(f"  📐 DrawIO con iconos AWS: {'✅' if len(aws_drawio) >= 1 else '❌'}")
    print(f"  🔷 Mermaid: {'✅' if len(mermaid_files) == 3 else '❌'}")
    print(f"  📝 Prompts MCP: {'✅' if len(prompt_files) == 3 else '❌'}")
    print(f"  📚 Documentación: {'✅' if len(doc_files) == 4 else '❌'}")
    
    # Calificación final
    score = (len(png_files)/4 + len(aws_drawio)/1 + len(mermaid_files)/3 + len(prompt_files)/3 + len(doc_files)/4) / 5 * 100
    
    print(f"\n🏆 CALIFICACIÓN FINAL: {score:.1f}%")
    
    if score >= 95:
        print("  🎉 EXCELENTE - Todos los ajustes funcionando perfectamente")
    elif score >= 80:
        print("  👍 BUENO - La mayoría de ajustes funcionando")
    elif score >= 60:
        print("  ⚠️ REGULAR - Algunos ajustes necesitan revisión")
    else:
        print("  ❌ NECESITA TRABAJO - Varios ajustes fallando")
    
    # Archivo recomendado
    if aws_drawio:
        print(f"\n🎯 ARCHIVO DRAWIO RECOMENDADO:")
        print(f"  📄 {aws_drawio[0].name}")
        print(f"  🎨 Iconos AWS reales (equivalente a PNG)")
        print(f"  📐 Abrir en: https://app.diagrams.net/")

if __name__ == "__main__":
    test_final()
