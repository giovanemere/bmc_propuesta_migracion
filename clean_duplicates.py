#!/usr/bin/env python3
"""
Script para limpiar archivos duplicados antiguos
"""

import os
from pathlib import Path

def clean_old_duplicates():
    """Limpia archivos duplicados antiguos"""
    
    print("🧹 Limpiando archivos duplicados antiguos...")
    
    base_dir = Path("outputs/mcp/diagrams/bmc_input")
    
    # Archivos antiguos a eliminar (con timestamps viejos)
    old_patterns = [
        "*_20250919_203330.*",
        "*_20250919_203548.*", 
        "*_20250919_203621.*",
        "*_20250919_204313.*",
        "*_20250919_204659.*",
        "*_20250919_205111.*",
        "*_20250919_205616.*"
    ]
    
    removed_count = 0
    
    for pattern in old_patterns:
        for old_file in base_dir.rglob(pattern):
            if old_file.is_file():
                print(f"  🗑️ {old_file.relative_to(base_dir)}")
                old_file.unlink()
                removed_count += 1
    
    print(f"✅ Eliminados {removed_count} archivos duplicados antiguos")
    
    # Mostrar estructura limpia
    print(f"\n📁 Estructura final limpia:")
    for item in sorted(base_dir.rglob("*")):
        if item.is_file():
            size = item.stat().st_size
            rel_path = item.relative_to(base_dir)
            print(f"  📄 {rel_path} ({size:,} bytes)")

if __name__ == "__main__":
    clean_old_duplicates()
