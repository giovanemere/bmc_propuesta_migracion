#!/usr/bin/env python3
"""
BMC Diagram Generator - Script de Gestión Principal
Limpieza, ejecución completa y por secciones
"""

import os
import sys
import shutil
import argparse
from pathlib import Path
import json
import time

# Agregar src al path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def clean_outputs(section=None):
    """Limpia archivos generados"""
    
    outputs_dir = Path("outputs")
    
    if section == "all" or section is None:
        print("🧹 Limpiando todos los archivos generados...")
        if outputs_dir.exists():
            shutil.rmtree(outputs_dir)
        print("✅ Todos los archivos eliminados")
        
    elif section == "png":
        print("🧹 Limpiando diagramas PNG...")
        png_dir = outputs_dir / "png"
        if png_dir.exists():
            shutil.rmtree(png_dir)
        print("✅ PNG eliminados")
        
    elif section == "drawio":
        print("🧹 Limpiando diagramas DrawIO...")
        drawio_dir = outputs_dir / "drawio"
        if drawio_dir.exists():
            shutil.rmtree(drawio_dir)
        print("✅ DrawIO eliminados")
        
    elif section == "docs":
        print("🧹 Limpiando documentación...")
        docs_dir = outputs_dir / "documentation"
        if docs_dir.exists():
            shutil.rmtree(docs_dir)
        print("✅ Documentación eliminada")
        
    elif section == "prompts":
        print("🧹 Limpiando prompts MCP...")
        prompts_dir = outputs_dir / "prompts"
        if prompts_dir.exists():
            shutil.rmtree(prompts_dir)
        print("✅ Prompts eliminados")
        
    elif section == "config":
        print("🧹 Limpiando configuración generada...")
        generated_dir = outputs_dir / "generated"
        if generated_dir.exists():
            shutil.rmtree(generated_dir)
        print("✅ Configuración eliminada")

def run_complete_workflow():
    """Ejecuta el flujo completo"""
    
    print("🚀 EJECUTANDO FLUJO COMPLETO BMC DIAGRAM GENERATOR")
    print("=" * 60)
    
    start_time = time.time()
    
    try:
        from core.workflow_orchestrator import run_complete_workflow
        results = run_complete_workflow('bmc_input')
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"\n🎉 FLUJO COMPLETO EXITOSO")
        print(f"⏱️  Tiempo total: {duration:.1f}s")
        print(f"📂 Archivos generados: {results['summary']['total_files']}")
        
        return results
        
    except Exception as e:
        print(f"❌ Error en flujo completo: {e}")
        return None

def run_section(section):
    """Ejecuta una sección específica"""
    
    print(f"🎯 EJECUTANDO SECCIÓN: {section.upper()}")
    print("=" * 40)
    
    try:
        # Cargar configuración
        config_path = Path("outputs/generated/bmc.json")
        if not config_path.exists():
            print("⚠️  Configuración no encontrada, generando...")
            from core.dynamic_config_generator import generate_dynamic_config
            generate_dynamic_config()
        
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        if section == "config":
            from core.dynamic_config_generator import generate_dynamic_config
            result = generate_dynamic_config(force_regenerate=True)
            print("✅ Configuración regenerada")
            
        elif section == "png":
            from generators.diagram_generator import DiagramGenerator
            gen = DiagramGenerator(config, 'outputs/png/bmc_input')
            
            png_types = ['network', 'microservices', 'security', 'data_flow']
            for png_type in png_types:
                result = gen.generate_diagram(png_type)
                print(f"✅ {png_type}: {Path(result).name}")
                
        elif section == "drawio":
            # DrawIO estático
            from generators.universal_generator import UniversalGenerator
            gen = UniversalGenerator('outputs')
            result = gen.generate_drawio_xml(config)
            print(f"✅ DrawIO estático: {Path(result).name}")
            
            # DrawIO dinámico
            from generators.dynamic_drawio_generator import DynamicDrawIOGenerator
            with open('config/bmc-input-specification.md', 'r') as f:
                spec = f.read()
            
            dynamic_gen = DynamicDrawIOGenerator('outputs')
            result = dynamic_gen.generate_dynamic_drawio(spec, 'bmc_input')
            print(f"✅ DrawIO dinámico: {Path(result).name}")
            
        elif section == "prompts":
            from generators.prompt_generator import MCPPromptGenerator
            gen = MCPPromptGenerator(config, 'outputs/prompts')
            results = gen.generate_prompts('bmc_input')
            print(f"✅ Prompts generados: {len(results)} archivos")
            
        elif section == "docs":
            from generators.doc_generator import ImplementationDocGenerator
            gen = ImplementationDocGenerator(config, 'outputs/documentation')
            results = gen.generate_implementation_docs('bmc_input')
            print(f"✅ Documentos generados: {len(results)} archivos")
            
        else:
            print(f"❌ Sección desconocida: {section}")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Error en sección {section}: {e}")
        return False

def show_status():
    """Muestra el estado actual del sistema"""
    
    print("📊 ESTADO ACTUAL DEL SISTEMA")
    print("=" * 40)
    
    outputs_dir = Path("outputs")
    if not outputs_dir.exists():
        print("📁 No hay archivos generados")
        return
    
    # Contar archivos por tipo
    png_files = list(outputs_dir.glob("**/*.png"))
    drawio_files = list(outputs_dir.glob("**/*.drawio"))
    md_files = list(outputs_dir.glob("**/*.md"))
    json_files = list(outputs_dir.glob("**/*.json"))
    
    total_files = len(png_files) + len(drawio_files) + len(md_files) + len(json_files)
    
    print(f"📂 Total archivos: {total_files}")
    print(f"🎨 PNG: {len(png_files)}")
    print(f"📐 DrawIO: {len(drawio_files)}")
    print(f"📄 Documentos MD: {len(md_files)}")
    print(f"⚙️  JSON: {len(json_files)}")
    
    if png_files:
        print("\n🎨 Diagramas PNG:")
        for png in png_files:
            size_kb = png.stat().st_size / 1024
            print(f"  - {png.name} ({size_kb:.1f} KB)")
    
    if drawio_files:
        print("\n📐 Diagramas DrawIO:")
        for drawio in drawio_files:
            size_kb = drawio.stat().st_size / 1024
            print(f"  - {drawio.name} ({size_kb:.1f} KB)")

def main():
    """Función principal con argumentos"""
    
    parser = argparse.ArgumentParser(
        description="BMC Diagram Generator - Script de Gestión",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python run.py --clean all              # Limpiar todo
  python run.py --run complete           # Ejecutar flujo completo
  python run.py --run png                # Solo generar PNG
  python run.py --clean png --run png    # Limpiar y regenerar PNG
  python run.py --status                 # Ver estado actual
        """
    )
    
    parser.add_argument('--clean', choices=['all', 'png', 'drawio', 'docs', 'prompts', 'config'],
                       help='Limpiar archivos generados')
    
    parser.add_argument('--run', choices=['complete', 'config', 'png', 'drawio', 'prompts', 'docs'],
                       help='Ejecutar generación')
    
    parser.add_argument('--status', action='store_true',
                       help='Mostrar estado actual')
    
    args = parser.parse_args()
    
    # Si no hay argumentos, mostrar ayuda
    if not any(vars(args).values()):
        parser.print_help()
        return
    
    # Ejecutar acciones
    if args.clean:
        clean_outputs(args.clean)
    
    if args.run:
        if args.run == 'complete':
            run_complete_workflow()
        else:
            run_section(args.run)
    
    if args.status:
        show_status()

if __name__ == "__main__":
    main()
