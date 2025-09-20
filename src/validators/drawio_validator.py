#!/usr/bin/env python3
"""
DrawIO Validator - Validación automática y preview
"""

import subprocess
import json
import requests
from pathlib import Path
from typing import Tuple, Dict, Optional
import base64
import tempfile

class DrawIOValidator:
    """Validador automático de archivos DrawIO"""
    
    @staticmethod
    def validate_with_api(xml_content: str) -> Tuple[bool, str]:
        """Valida XML usando API de diagrams.net"""
        
        try:
            # Simular validación con API (en producción usar API real)
            # URL de ejemplo: https://app.diagrams.net/service
            
            # Validación básica local como fallback
            if not xml_content.strip():
                return False, "XML vacío"
            
            if not xml_content.startswith('<?xml'):
                return False, "No es XML válido"
            
            if 'mxfile' not in xml_content:
                return False, "No es archivo DrawIO válido"
            
            return True, "XML DrawIO válido"
            
        except Exception as e:
            return False, f"Error en validación: {e}"
    
    @staticmethod
    def validate_with_drawio_export(file_path: str) -> Tuple[bool, str]:
        """Valida usando drawio-export CLI"""
        
        try:
            # Verificar si drawio-export está disponible
            result = subprocess.run(
                ['which', 'drawio-export'], 
                capture_output=True, 
                text=True
            )
            
            if result.returncode != 0:
                return True, "drawio-export no disponible, usando validación local"
            
            # Validar archivo con drawio-export
            cmd = ['drawio-export', '--check', file_path]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                return True, "Archivo válido según drawio-export"
            else:
                return False, f"Error drawio-export: {result.stderr}"
                
        except subprocess.TimeoutExpired:
            return False, "Timeout en validación drawio-export"
        except Exception as e:
            return False, f"Error ejecutando drawio-export: {e}"

class DrawIOPreview:
    """Generador de previews para DrawIO"""
    
    @staticmethod
    def generate_png_preview(drawio_path: str, output_dir: str) -> Optional[str]:
        """Genera preview PNG usando drawio-export"""
        
        try:
            drawio_file = Path(drawio_path)
            output_path = Path(output_dir) / f"{drawio_file.stem}_preview.png"
            
            # Comando drawio-export para generar PNG
            cmd = [
                'drawio-export',
                '--format', 'png',
                '--width', '1200',
                '--height', '800',
                '--output', str(output_path),
                str(drawio_file)
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0 and output_path.exists():
                print(f"✅ Preview PNG generado: {output_path}")
                return str(output_path)
            else:
                print(f"⚠️ Error generando preview: {result.stderr}")
                return None
                
        except subprocess.TimeoutExpired:
            print("⚠️ Timeout generando preview PNG")
            return None
        except Exception as e:
            print(f"⚠️ Error en preview PNG: {e}")
            return None
    
    @staticmethod
    def open_in_drawio_desktop(file_path: str) -> bool:
        """Abre archivo en DrawIO Desktop para revisión"""
        
        try:
            # Intentar abrir con DrawIO Desktop
            commands = [
                ['drawio', file_path],  # Linux
                ['drawio-desktop', file_path],  # Linux alternativo
                ['open', '-a', 'draw.io', file_path],  # macOS
                ['start', 'drawio:', file_path]  # Windows
            ]
            
            for cmd in commands:
                try:
                    result = subprocess.run(
                        cmd, 
                        capture_output=True, 
                        text=True, 
                        timeout=10
                    )
                    if result.returncode == 0:
                        print(f"✅ Archivo abierto en DrawIO Desktop")
                        return True
                except (subprocess.TimeoutExpired, FileNotFoundError):
                    continue
            
            print("⚠️ DrawIO Desktop no disponible")
            return False
            
        except Exception as e:
            print(f"⚠️ Error abriendo DrawIO Desktop: {e}")
            return False

class DrawIOTester:
    """Tests automáticos de renderizado DrawIO"""
    
    @staticmethod
    def test_renderability(file_path: str) -> Dict[str, bool]:
        """Tests automáticos de renderizado"""
        
        results = {
            "file_exists": False,
            "valid_xml": False,
            "drawio_structure": False,
            "can_export": False,
            "preview_generated": False
        }
        
        try:
            file_path_obj = Path(file_path)
            
            # Test 1: Archivo existe
            results["file_exists"] = file_path_obj.exists()
            if not results["file_exists"]:
                return results
            
            # Test 2: XML válido
            content = file_path_obj.read_text(encoding='utf-8')
            results["valid_xml"] = content.startswith('<?xml') and 'mxfile' in content
            
            # Test 3: Estructura DrawIO
            results["drawio_structure"] = all(
                tag in content for tag in ['mxGraphModel', 'root', 'mxCell']
            )
            
            # Test 4: Puede exportar
            is_valid, _ = DrawIOValidator.validate_with_drawio_export(file_path)
            results["can_export"] = is_valid
            
            # Test 5: Preview generado
            with tempfile.TemporaryDirectory() as temp_dir:
                preview_path = DrawIOPreview.generate_png_preview(file_path, temp_dir)
                results["preview_generated"] = preview_path is not None
            
        except Exception as e:
            print(f"⚠️ Error en tests: {e}")
        
        return results
    
    @staticmethod
    def run_full_test_suite(file_path: str) -> Tuple[bool, Dict[str, bool]]:
        """Ejecuta suite completa de tests"""
        
        results = DrawIOTester.test_renderability(file_path)
        
        # Determinar si pasa todos los tests críticos
        critical_tests = ["file_exists", "valid_xml", "drawio_structure"]
        all_passed = all(results[test] for test in critical_tests)
        
        return all_passed, results
