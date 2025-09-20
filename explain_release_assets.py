#!/usr/bin/env python3
"""
Explicación de release_assets
"""

from pathlib import Path

def explain_release_assets():
    """Explica qué son y para qué sirven los release_assets"""
    
    print("📦 ¿Qué son los release_assets?")
    print("=" * 40)
    
    print("\n🎯 PROPÓSITO:")
    print("  📁 Carpeta para almacenar archivos de release")
    print("  🚀 Preparar distribución del proyecto")
    print("  📋 Crear versiones empaquetadas")
    print("  🔄 Facilitar descargas y distribución")
    
    # Analizar archivos existentes
    assets_dir = Path("release_assets")
    if assets_dir.exists():
        assets = list(assets_dir.glob("*.zip"))
        
        print(f"\n📊 Archivos actuales ({len(assets)}):")
        
        for asset in sorted(assets):
            size_mb = asset.stat().st_size / 1024 / 1024
            
            if "bmc_mcp_diagrams" in asset.name:
                print(f"  📐 {asset.name} ({size_mb:.1f}MB)")
                print(f"      🎨 Contiene: Diagramas PNG, DrawIO, Mermaid")
                print(f"      👥 Para: Usuarios finales")
                
            elif "bmc_mcp_clean" in asset.name:
                print(f"  🧹 {asset.name} ({size_mb:.1f}MB)")
                print(f"      🎨 Contiene: Diagramas limpios sin duplicados")
                print(f"      👥 Para: Usuarios finales (v4.0.0)")
                
            elif "mcp_generator_source" in asset.name:
                print(f"  💻 {asset.name} ({size_mb:.1f}MB)")
                print(f"      🎨 Contiene: Código fuente completo")
                print(f"      👥 Para: Desarrolladores")
                
            elif "mcp_generator_restructured" in asset.name:
                print(f"  🏗️ {asset.name} ({size_mb:.1f}MB)")
                print(f"      🎨 Contiene: Código reestructurado")
                print(f"      👥 Para: Desarrolladores (v4.0.0)")
    
    print(f"\n🔄 PROCESO DE RELEASE:")
    print(f"  1️⃣ Desarrollo → Código en src/")
    print(f"  2️⃣ Generación → Diagramas en outputs/")
    print(f"  3️⃣ Empaquetado → ZIPs en release_assets/")
    print(f"  4️⃣ Distribución → GitHub Releases")
    
    print(f"\n📋 TIPOS DE ASSETS:")
    print(f"  🎨 Diagramas: Para usuarios que solo quieren los diagramas")
    print(f"  💻 Código fuente: Para desarrolladores que quieren modificar")
    print(f"  📦 Completo: Código + diagramas + documentación")
    
    print(f"\n🎯 VENTAJAS:")
    print(f"  ✅ Distribución fácil (un solo ZIP)")
    print(f"  ✅ Versionado claro (v3.0.0, v4.0.0)")
    print(f"  ✅ Separación por audiencia (usuarios vs desarrolladores)")
    print(f"  ✅ Historial de releases")
    
    print(f"\n💡 USO RECOMENDADO:")
    print(f"  👤 Usuario final: Descargar bmc_mcp_clean_v4.0.0.zip")
    print(f"  👨‍💻 Desarrollador: Descargar mcp_generator_restructured_v4.0.0.zip")
    print(f"  🏢 Empresa: Usar ambos según necesidad")
    
    print(f"\n🧹 LIMPIEZA:")
    print(f"  ⚠️ Versiones antiguas (v3.x) pueden eliminarse")
    print(f"  ✅ Mantener solo v4.0.0 (más reciente)")
    print(f"  📦 Crear v4.1.0 con DrawIO PlantUML profesional")

if __name__ == "__main__":
    explain_release_assets()
