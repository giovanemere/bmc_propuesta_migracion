#!/usr/bin/env python3
"""
BMC Input Case - Caso que usa la especificación BMC como entrada
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.bmc_input_parser import BMCInputParser
from core.refined_diagram_generator import RefinedDiagramGenerator

def run_bmc_input_case():
    """Ejecuta el caso BMC desde especificación de entrada"""
    
    print("🏛️ BMC Input Case - From Business Specification")
    print("=" * 55)
    
    # Archivo de especificación BMC
    bmc_input_file = "docs/specifications/bmc-input-specification.md"
    
    if not os.path.exists(bmc_input_file):
        print(f"❌ BMC input file not found: {bmc_input_file}")
        return False
    
    # Parser específico BMC
    parser = BMCInputParser(bmc_input_file)
    config = parser.parse_to_mcp_config()
    
    if not config:
        print("❌ Failed to parse BMC specification")
        return False
    
    print("✅ BMC specification parsed successfully")
    
    # Mostrar configuración extraída
    print(f"\n📊 Extracted Configuration:")
    print(f"  - Project: {config['project']['name']}")
    print(f"  - Microservices: {len(config.get('microservices', {}))}")
    print(f"  - AWS Services: {len(config.get('aws_services', {}))}")
    print(f"  - Integrations: {len(config.get('integrations', {}))}")
    
    # Generar diagramas - Solo en estructura MCP
    generator = RefinedDiagramGenerator(config, output_dir="outputs/mcp")
    results = generator.generate_all_refined("BMC_Input")
    
    if results:
        print(f"\n🎉 BMC Input diagrams generated successfully!")
        print(f"\n📁 Generated files:")
        for diagram_type, file_path in results.items():
            print(f"  - {diagram_type}: {file_path}")
        
        print(f"\n🏛️ BMC Business Features Mapped:")
        
        # Mostrar mapeo de funcionalidades
        microservices = config.get('microservices', {})
        for service_name, service_config in microservices.items():
            business_function = service_config.get('business_function', 'N/A')
            print(f"  - {service_name}: {business_function}")
        
        print(f"\n📈 Performance KPIs:")
        kpis = config.get('performance_kpis', {})
        if 'throughput' in kpis:
            throughput = kpis['throughput']
            print(f"  - Products Database: {throughput.get('products_database', 'N/A')}")
            print(f"  - Categories: {throughput.get('categories', 'N/A')}")
            print(f"  - Processing: {throughput.get('invoices_per_hour', 'N/A')} invoices/hour")
        
        return True
    else:
        print(f"\n❌ Failed to generate BMC Input diagrams")
        return False

if __name__ == "__main__":
    success = run_bmc_input_case()
    sys.exit(0 if success else 1)
