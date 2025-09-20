#!/usr/bin/env python3
"""
Script para consolidar múltiples archivos de configuración en uno solo
"""

import json
import os
from pathlib import Path
from datetime import datetime

def consolidate_configs():
    """Consolida archivos de configuración en uno solo"""
    
    config_dir = Path("docs/specifications/config")
    
    # Leer archivo más completo (bmc-analysis-updated.json)
    main_config_file = config_dir / "bmc-analysis-updated.json"
    
    if not main_config_file.exists():
        print(f"❌ Archivo principal no encontrado: {main_config_file}")
        return False
    
    # Cargar configuración principal
    with open(main_config_file, 'r', encoding='utf-8') as f:
        main_config = json.load(f)
    
    # Crear configuración consolidada
    consolidated = {
        "metadata": {
            "version": "2.0.0",
            "consolidated_date": datetime.now().isoformat(),
            "source_files": [
                "bmc-analysis-updated.json",
                "bmc-analysis-complete.json", 
                "mcp-config.json"
            ],
            "description": "Configuración consolidada BMC - Archivo único"
        },
        "project": {
            "name": "BMC Bolsa Comisionista",
            "type": "Sistema Regulatorio",
            "entity": "Ente Regulador",
            "main_function": "Procesamiento de facturas y cálculo de comisiones"
        },
        "workflow": main_config,
        "mcp_server": {
            "command": "python3",
            "args": ["/home/giovanemere/Migracion/mcp-server.py"],
            "description": "BMC System Context Provider"
        }
    }
    
    # Archivo consolidado
    output_file = config_dir / "bmc-consolidated-config.json"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(consolidated, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Configuración consolidada creada: {output_file}")
    
    # Crear backup de archivos antiguos
    backup_dir = config_dir / "backup"
    backup_dir.mkdir(exist_ok=True)
    
    old_files = [
        "bmc-analysis-complete.json",
        "bmc-analysis-updated.json", 
        "mcp-config.json",
        "bmc-workflow-complete-with-diagrams.json"
    ]
    
    for old_file in old_files:
        old_path = config_dir / old_file
        if old_path.exists():
            backup_path = backup_dir / old_file
            old_path.rename(backup_path)
            print(f"📦 Backup creado: {backup_path}")
    
    return True

if __name__ == "__main__":
    success = consolidate_configs()
    if success:
        print("\n🎉 Consolidación completada - Solo un archivo de configuración")
    else:
        print("\n❌ Error en consolidación")
