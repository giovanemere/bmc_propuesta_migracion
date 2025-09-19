#!/usr/bin/env python3
"""
Generic AWS Case - Caso genérico para arquitecturas AWS
Configuración genérica reutilizable
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.mcp_engine import MCPEngine

def create_generic_config():
    """Crea configuración genérica AWS"""
    
    config = {
        "microservices": {
            "api_service": {
                "cpu": 2048,
                "memory": 4096,
                "port": 8000,
                "min_capacity": 2,
                "max_capacity": 10
            },
            "data_service": {
                "cpu": 4096,
                "memory": 8192,
                "port": 8001,
                "min_capacity": 3,
                "max_capacity": 15
            },
            "worker_service": {
                "cpu": 1024,
                "memory": 2048,
                "port": 8002,
                "min_capacity": 1,
                "max_capacity": 5
            }
        },
        "services": {
            "database": {
                "type": "rds",
                "engine": "postgresql",
                "instance_class": "db.r6g.large"
            },
            "cache": {
                "type": "elasticache",
                "engine": "redis",
                "node_type": "cache.r6g.large"
            },
            "storage": {
                "type": "s3",
                "storage_class": "standard"
            }
        },
        "metrics": {
            "response_time": {"value": "500", "unit": "ms"},
            "throughput": {"value": "1000", "unit": "req/s"},
            "availability": {"value": "99.9", "unit": "%"}
        }
    }
    
    return config

def run_generic_aws_case():
    """Ejecuta el caso genérico AWS"""
    
    print("☁️ Generic AWS Case - Reusable Architecture")
    print("=" * 50)
    
    # Crear configuración genérica
    config = create_generic_config()
    
    # Guardar configuración temporal
    import json
    config_file = "temp_generic_config.json"
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)
    
    # Configurar engine
    engine = MCPEngine(output_dir="output")
    
    # Ejecutar generación
    success = engine.run(config_file, "Generic_AWS")
    
    # Limpiar archivo temporal
    os.remove(config_file)
    
    if success:
        print("\n✅ Generic AWS diagrams generated successfully!")
        print("📁 Check output/png/ and output/drawio/")
    else:
        print("\n❌ Generic AWS diagram generation failed")
    
    return success

if __name__ == "__main__":
    run_generic_aws_case()
