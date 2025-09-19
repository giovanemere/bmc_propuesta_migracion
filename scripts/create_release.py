#!/usr/bin/env python3
"""
GitHub Release Creator - Crea release en GitHub con archivos adjuntos
"""

import os
import subprocess
import zipfile
from pathlib import Path

def create_release_assets():
    """Crea archivos para adjuntar al release"""
    
    print("📦 Creating release assets...")
    
    # Crear directorio de release
    release_dir = Path("release_assets")
    release_dir.mkdir(exist_ok=True)
    
    # Crear ZIP con diagramas de ejemplo
    diagrams_zip = release_dir / "bmc_diagrams_examples_v2.0.0.zip"
    
    with zipfile.ZipFile(diagrams_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Agregar PNG files
        png_dir = Path("output/png")
        if png_dir.exists():
            for png_file in png_dir.glob("*.png"):
                zf.write(png_file, f"png/{png_file.name}")
        
        # Agregar Draw.io files
        drawio_dir = Path("output/drawio")
        if drawio_dir.exists():
            for drawio_file in drawio_dir.glob("*.drawio"):
                zf.write(drawio_file, f"drawio/{drawio_file.name}")
        
        # Agregar documentación
        docs_files = [
            "README.md",
            "CHANGELOG.md", 
            "RELEASE_NOTES.md",
            "docs/mcp-diagrams-architecture.md",
            "docs/mcp-aws-model.md"
        ]
        
        for doc_file in docs_files:
            if Path(doc_file).exists():
                zf.write(doc_file, f"docs/{Path(doc_file).name}")
    
    print(f"✓ Created: {diagrams_zip} ({diagrams_zip.stat().st_size:,} bytes)")
    
    # Crear ZIP con código fuente
    source_zip = release_dir / "mcp_diagram_generator_v2.0.0.zip"
    
    with zipfile.ZipFile(source_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Core modules
        core_dir = Path("core")
        if core_dir.exists():
            for py_file in core_dir.glob("*.py"):
                zf.write(py_file, f"core/{py_file.name}")
        
        # Cases
        cases_dir = Path("cases")
        if cases_dir.exists():
            for py_file in cases_dir.glob("*.py"):
                zf.write(py_file, f"cases/{py_file.name}")
        
        # Scripts
        scripts_dir = Path("scripts")
        if scripts_dir.exists():
            for py_file in scripts_dir.glob("*.py"):
                zf.write(py_file, f"scripts/{py_file.name}")
        
        # Main files
        main_files = [
            "main.py",
            "run.sh",
            "requirements.txt"
        ]
        
        for main_file in main_files:
            if Path(main_file).exists():
                zf.write(main_file, main_file)
    
    print(f"✓ Created: {source_zip} ({source_zip.stat().st_size:,} bytes)")
    
    return [diagrams_zip, source_zip]

def get_release_info():
    """Obtiene información del release"""
    
    # Obtener último commit
    result = subprocess.run(
        ["git", "log", "-1", "--pretty=format:%H %s"],
        capture_output=True, text=True
    )
    
    if result.returncode == 0:
        commit_hash, commit_msg = result.stdout.split(" ", 1)
        short_hash = commit_hash[:7]
    else:
        short_hash = "unknown"
        commit_msg = "Latest commit"
    
    # Contar archivos generados
    png_count = len(list(Path("output/png").glob("*.png"))) if Path("output/png").exists() else 0
    drawio_count = len(list(Path("output/drawio").glob("*.drawio"))) if Path("output/drawio").exists() else 0
    
    return {
        "commit_hash": short_hash,
        "commit_msg": commit_msg,
        "png_count": png_count,
        "drawio_count": drawio_count
    }

def main():
    """Función principal"""
    
    print("🚀 GitHub Release Creator v2.0.0")
    print("=" * 40)
    
    # Crear assets
    assets = create_release_assets()
    
    # Obtener información
    info = get_release_info()
    
    print(f"\n📊 Release Summary:")
    print(f"  - Version: v2.0.0")
    print(f"  - Commit: {info['commit_hash']}")
    print(f"  - PNG Diagrams: {info['png_count']}")
    print(f"  - Draw.io Files: {info['drawio_count']}")
    print(f"  - Assets Created: {len(assets)}")
    
    print(f"\n📦 Release Assets:")
    for asset in assets:
        size = asset.stat().st_size
        print(f"  - {asset.name} ({size:,} bytes)")
    
    print(f"\n🎯 Next Steps:")
    print(f"1. Go to: https://github.com/giovanemere/bmc_propuesta_migracion/releases")
    print(f"2. Click 'Create a new release'")
    print(f"3. Select tag: v2.0.0")
    print(f"4. Title: 'v2.0.0 - MCP Diagram Generator'")
    print(f"5. Copy description from RELEASE_NOTES.md")
    print(f"6. Attach files from release_assets/")
    print(f"7. Publish release")
    
    print(f"\n✅ Release preparation completed!")

if __name__ == "__main__":
    main()
