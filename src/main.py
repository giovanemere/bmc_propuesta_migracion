#!/usr/bin/env python3
"""
MCP Diagram Generator - Punto de entrada principal
Generador unificado de diagramas, prompts y documentación
"""

import argparse
import sys
from pathlib import Path

# Agregar src al path
sys.path.insert(0, str(Path(__file__).parent))

def run_bmc_input_case():
    """Ejecuta caso BMC Input"""
    from cases.bmc_input_case import run_bmc_input_case
    return run_bmc_input_case()

def main():
    """Función principal"""
    parser = argparse.ArgumentParser(description='MCP Diagram Generator')
    parser.add_argument('--case', choices=['bmc-input'], required=True,
                       help='Caso de uso a ejecutar')
    
    args = parser.parse_args()
    
    print("🚀 MCP Diagram Generator")
    print("=" * 50)
    
    if args.case == 'bmc-input':
        print("🏛️ Running BMC Input Case...")
        success = run_bmc_input_case()
        return 0 if success else 1
    
    return 1

if __name__ == "__main__":
    sys.exit(main())
