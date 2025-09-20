#!/usr/bin/env python3
"""
Main Entry Point - Punto de entrada principal usando nueva arquitectura
"""

import sys
from pathlib import Path

# Agregar src al path
sys.path.append(str(Path(__file__).parent))

def main():
    """Punto de entrada principal"""
    
    print("🚀 MCP Diagram Generator v4.1.0")
    print("=" * 40)
    
    # Usar nueva arquitectura con WorkflowOrchestrator
    from core.workflow_orchestrator import run_complete_workflow
    
    try:
        # Ejecutar flujo completo
        results = run_complete_workflow("bmc_input")
        
        print(f"\n🎉 Generación completada exitosamente!")
        print(f"📊 Archivos generados: {results['summary']['total_files']}")
        print(f"⏱️ Tiempo: {results['duration_seconds']:.1f}s")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
