#!/usr/bin/env python3
"""
MCP Diagram Generator - Main Entry Point
Punto de entrada principal para la generación de diagramas desde MCP
"""

import sys
import argparse
from pathlib import Path

# Agregar el directorio actual al path
sys.path.append(str(Path(__file__).parent))

from core.mcp_engine import MCPEngine
from cases.bmc_case import run_bmc_case
from cases.generic_aws_case import run_generic_aws_case

def main():
    """Función principal"""
    
    parser = argparse.ArgumentParser(
        description="MCP Diagram Generator - Generate AWS architecture diagrams from MCP files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 main.py --case bmc                           # Run BMC specific case
  python3 main.py --case generic                      # Run generic AWS case
  python3 main.py --file docs/mcp-aws-model.md        # Generate from MCP file
  python3 main.py --file config.json --name MyProject # Generate from JSON config
        """
    )
    
    # Argumentos principales
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--case', choices=['bmc', 'generic'], 
                      help='Run predefined use case')
    group.add_argument('--file', type=str,
                      help='Input file (MCP .md, JSON, or YAML)')
    
    # Argumentos opcionales
    parser.add_argument('--name', type=str, default='Architecture',
                       help='Project name for generated diagrams')
    parser.add_argument('--output', type=str, default='output',
                       help='Output directory for generated files')
    parser.add_argument('--validate', action='store_true',
                       help='Only validate configuration without generating')
    parser.add_argument('--summary', action='store_true',
                       help='Show configuration summary')
    
    args = parser.parse_args()
    
    print("🚀 MCP Diagram Generator")
    print("=" * 50)
    
    success = False
    
    try:
        if args.case:
            # Ejecutar caso predefinido
            if args.case == 'bmc':
                print("🏢 Running BMC Case...")
                success = run_bmc_case()
            elif args.case == 'generic':
                print("☁️ Running Generic AWS Case...")
                success = run_generic_aws_case()
                
        elif args.file:
            # Procesar archivo específico
            print(f"📄 Processing file: {args.file}")
            
            # Verificar que el archivo existe
            if not Path(args.file).exists():
                print(f"❌ File not found: {args.file}")
                return 1
            
            # Crear engine
            engine = MCPEngine(output_dir=args.output)
            
            # Solo validar si se solicita
            if args.validate:
                if args.file.endswith('.md'):
                    engine.load_mcp(args.file)
                else:
                    engine.load_config(args.file)
                
                success = engine.validate_config()
                
                if args.summary:
                    summary = engine.get_config_summary()
                    print("\n📊 Configuration Summary:")
                    for key, value in summary.items():
                        print(f"  - {key}: {value}")
                
            else:
                # Generar diagramas
                success = engine.run(args.file, args.name)
        
        # Resultado final
        if success:
            print(f"\n🎉 Success! Check {args.output}/ for generated files")
            return 0
        else:
            print(f"\n❌ Generation failed")
            return 1
            
    except KeyboardInterrupt:
        print(f"\n⚠️ Operation cancelled by user")
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
