#!/usr/bin/env python3
"""
BMC Use Case - Caso específico para BMC
Configuración específica para el proyecto BMC
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.mcp_engine import MCPEngine

def run_bmc_case():
    """Ejecuta el caso BMC"""
    
    print("🏢 BMC Use Case - Bolsa Mercantil de Colombia")
    print("=" * 50)
    
    # Configurar engine
    engine = MCPEngine(output_dir="output")
    
    # Archivo MCP específico de BMC
    mcp_file = "docs/specifications/mcp-diagrams-architecture.md"
    
    # Ejecutar generación
    success = engine.run(mcp_file, "BMC")
    
    if success:
        print("\n✅ BMC diagrams generated successfully!")
        print("📁 Check output/png/ and output/drawio/")
    else:
        print("\n❌ BMC diagram generation failed")
    
    return success

if __name__ == "__main__":
    run_bmc_case()
