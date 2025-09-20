#!/usr/bin/env python3
"""
Script para eliminar carpetas duplicadas y usar solo outputs/mcp
"""

import shutil
from pathlib import Path

def fix_duplicate_outputs():
    """Elimina duplicados y usa solo estructura MCP"""
    
    print("🔧 Corrigiendo salidas duplicadas...")
    
    base_dir = Path("outputs")
    bmc_input_dir = base_dir / "bmc_input"
    mcp_dir = base_dir / "mcp"
    
    # Si existe bmc_input, mover contenido a MCP y eliminar
    if bmc_input_dir.exists():
        print(f"📦 Moviendo contenido de {bmc_input_dir} a {mcp_dir}")
        
        # Asegurar que existe estructura MCP
        mcp_bmc_dir = mcp_dir / "diagrams" / "bmc_input"
        mcp_bmc_dir.mkdir(parents=True, exist_ok=True)
        
        # Mover diagramas si no existen en MCP
        bmc_diagrams = bmc_input_dir / "diagrams"
        if bmc_diagrams.exists():
            for item in bmc_diagrams.rglob("*"):
                if item.is_file():
                    # Crear estructura relativa en MCP
                    rel_path = item.relative_to(bmc_diagrams)
                    dest_path = mcp_bmc_dir / rel_path
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    if not dest_path.exists():
                        shutil.copy2(item, dest_path)
                        print(f"  ✓ {rel_path}")
        
        # Eliminar carpeta duplicada
        shutil.rmtree(bmc_input_dir)
        print(f"🗑️ Eliminada carpeta duplicada: {bmc_input_dir}")
    
    print(f"✅ Solo queda estructura MCP: {mcp_dir}")
    
    # Mostrar estructura final
    print(f"\n📁 Estructura final:")
    for item in mcp_dir.rglob("*"):
        if item.is_dir():
            level = len(item.relative_to(mcp_dir).parts)
            indent = "  " * level
            print(f"{indent}{item.name}/")

if __name__ == "__main__":
    fix_duplicate_outputs()
