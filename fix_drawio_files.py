#!/usr/bin/env python3
"""
Script para corregir archivos DrawIO con errores mxCell
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from core.fixed_drawio_generator import FixedDrawIOGenerator
from core.config_manager import ConfigManager

def fix_drawio_files():
    """Corrige archivos DrawIO existentes"""
    
    print("🔧 Corrigiendo archivos DrawIO...")
    print("=" * 40)
    
    try:
        # Cargar configuración
        config_manager = ConfigManager()
        config = config_manager.load_config()
        
        # Crear generador corregido
        generator = FixedDrawIOGenerator(config)
        
        # Generar archivo DrawIO corregido
        fixed_file = generator.generate_fixed_drawio("BMC_Input")
        
        # Validar archivo generado
        is_valid = generator.validate_drawio_file(fixed_file)
        
        if is_valid:
            print(f"\n🎉 Archivo DrawIO corregido exitosamente")
            print(f"📁 Ubicación: {fixed_file}")
            
            # Buscar y validar archivos existentes
            print(f"\n🔍 Validando archivos existentes...")
            
            drawio_dir = Path("outputs/mcp/diagrams/bmc_input/drawio")
            if drawio_dir.exists():
                drawio_files = list(drawio_dir.glob("*.drawio"))
                
                for file_path in drawio_files:
                    if "fixed" not in file_path.name:
                        is_valid_existing = generator.validate_drawio_file(str(file_path))
                        status = "✅" if is_valid_existing else "❌"
                        print(f"  {status} {file_path.name}")
            
            return True
        else:
            print(f"\n❌ Error: Archivo generado no es válido")
            return False
            
    except Exception as e:
        print(f"❌ Error corrigiendo DrawIO: {e}")
        return False

if __name__ == "__main__":
    success = fix_drawio_files()
    sys.exit(0 if success else 1)
