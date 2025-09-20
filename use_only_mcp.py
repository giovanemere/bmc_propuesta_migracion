#!/usr/bin/env python3
"""
Script para usar solo estructura MCP y eliminar duplicados
"""

import shutil
from pathlib import Path

def use_only_mcp():
    """Configura para usar solo outputs/mcp"""
    
    print("🔧 Configurando para usar solo MCP...")
    
    # Eliminar cualquier carpeta bmc_input
    bmc_dirs = list(Path("outputs").glob("**/bmc_input"))
    for bmc_dir in bmc_dirs:
        if bmc_dir.exists() and "mcp" not in str(bmc_dir):
            print(f"🗑️ Eliminando: {bmc_dir}")
            shutil.rmtree(bmc_dir)
    
    # Asegurar estructura MCP limpia
    mcp_dir = Path("outputs/mcp")
    mcp_dir.mkdir(parents=True, exist_ok=True)
    
    print("✅ Solo estructura MCP activa")
    
    # Mostrar estructura final
    print("\n📁 Estructura MCP:")
    if mcp_dir.exists():
        for item in sorted(mcp_dir.rglob("*")):
            if item.is_dir():
                level = len(item.relative_to(mcp_dir).parts)
                indent = "  " * level
                print(f"{indent}{item.name}/")

if __name__ == "__main__":
    use_only_mcp()
