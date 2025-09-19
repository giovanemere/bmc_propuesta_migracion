#!/usr/bin/env python3
"""
Draw.io Cleanup Script - Limpia archivos Draw.io duplicados
Mantiene solo un archivo Draw.io unificado por proyecto
"""

import os
import glob
from pathlib import Path

def cleanup_drawio_files():
    """Limpia archivos Draw.io duplicados"""
    
    print("🧹 Cleaning up Draw.io files...")
    
    drawio_dir = Path("output/drawio")
    if not drawio_dir.exists():
        print("❌ Draw.io directory not found")
        return
    
    # Buscar archivos duplicados
    all_files = list(drawio_dir.glob("*.drawio"))
    
    print(f"📁 Found {len(all_files)} Draw.io files:")
    for file in all_files:
        size = file.stat().st_size
        print(f"  - {file.name} ({size:,} bytes)")
    
    # Identificar duplicados por proyecto
    projects = {}
    for file in all_files:
        # Extraer nombre del proyecto
        name = file.stem
        if "_unified_architecture" in name:
            project = name.replace("_unified_architecture", "")
        elif "_complete_architecture" in name:
            project = name.replace("_complete_architecture", "")
        elif "_architecture" in name:
            project = name.replace("_architecture", "")
        else:
            project = name
        
        if project not in projects:
            projects[project] = []
        projects[project].append(file)
    
    # Mantener solo el archivo más completo por proyecto
    kept_files = []
    removed_files = []
    
    for project, files in projects.items():
        if len(files) == 1:
            kept_files.append(files[0])
            continue
        
        # Ordenar por tamaño (más grande = más completo)
        files.sort(key=lambda f: f.stat().st_size, reverse=True)
        
        # Mantener el más grande
        best_file = files[0]
        target_name = f"{project}_architecture.drawio"
        target_path = drawio_dir / target_name
        
        # Renombrar si es necesario
        if best_file.name != target_name:
            best_file.rename(target_path)
            print(f"✓ Renamed {best_file.name} → {target_name}")
            kept_files.append(target_path)
        else:
            kept_files.append(best_file)
        
        # Eliminar duplicados
        for file in files[1:]:
            file.unlink()
            removed_files.append(file.name)
            print(f"🗑️ Removed duplicate: {file.name}")
    
    print(f"\n📊 Cleanup Summary:")
    print(f"  - Files kept: {len(kept_files)}")
    print(f"  - Files removed: {len(removed_files)}")
    
    print(f"\n📁 Final Draw.io files:")
    for file in sorted(kept_files):
        size = file.stat().st_size
        print(f"  - {file.name} ({size:,} bytes)")

if __name__ == "__main__":
    cleanup_drawio_files()
