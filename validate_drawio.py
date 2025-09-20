#!/usr/bin/env python3
"""
Validador automático de archivos DrawIO
Detecta y reporta errores mxCell
"""

import xml.etree.ElementTree as ET
from pathlib import Path

def validate_all_drawio():
    """Valida todos los archivos DrawIO en el proyecto"""
    
    print("🔍 Validando archivos DrawIO...")
    print("=" * 40)
    
    # Buscar todos los archivos DrawIO
    drawio_files = []
    for pattern in ["outputs/**/*.drawio", "**/*.drawio"]:
        drawio_files.extend(Path(".").glob(pattern))
    
    if not drawio_files:
        print("❌ No se encontraron archivos DrawIO")
        return False
    
    valid_count = 0
    invalid_count = 0
    
    for file_path in drawio_files:
        try:
            # Parsear XML
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            errors = []
            
            # Validar estructura básica
            if root.tag != "mxfile":
                errors.append("Root tag no es 'mxfile'")
            
            diagram = root.find("diagram")
            if diagram is None:
                errors.append("No se encontró elemento 'diagram'")
            else:
                model = diagram.find("mxGraphModel")
                if model is None:
                    errors.append("No se encontró 'mxGraphModel'")
                else:
                    graph_root = model.find("root")
                    if graph_root is None:
                        errors.append("No se encontró elemento 'root'")
                    else:
                        # Validar celdas
                        cells = graph_root.findall("mxCell")
                        if len(cells) < 2:
                            errors.append("Menos de 2 celdas mxCell")
                        
                        cell_ids = [cell.get("id") for cell in cells]
                        if "0" not in cell_ids:
                            errors.append("Falta celda con id='0'")
                        if "1" not in cell_ids:
                            errors.append("Falta celda con id='1'")
                        
                        # Validar geometrías
                        for cell in cells:
                            geometry = cell.find("mxGeometry")
                            if geometry is not None:
                                if not geometry.get("as"):
                                    errors.append(f"Celda {cell.get('id')} sin atributo 'as' en geometría")
            
            # Reportar resultado
            if errors:
                print(f"❌ {file_path.name}")
                for error in errors:
                    print(f"   - {error}")
                invalid_count += 1
            else:
                print(f"✅ {file_path.name}")
                valid_count += 1
                
        except ET.ParseError as e:
            print(f"❌ {file_path.name} - Error XML: {e}")
            invalid_count += 1
        except Exception as e:
            print(f"❌ {file_path.name} - Error: {e}")
            invalid_count += 1
    
    print(f"\n📊 Resumen:")
    print(f"  ✅ Válidos: {valid_count}")
    print(f"  ❌ Inválidos: {invalid_count}")
    print(f"  📁 Total: {len(drawio_files)}")
    
    return invalid_count == 0

if __name__ == "__main__":
    success = validate_all_drawio()
    if success:
        print(f"\n🎉 Todos los archivos DrawIO son válidos")
    else:
        print(f"\n⚠️ Se encontraron archivos DrawIO con errores")
        print(f"Ejecuta: python3 fix_drawio_files.py")
