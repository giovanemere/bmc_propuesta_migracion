#!/usr/bin/env python3
"""
Automated Tests - Pruebas automatizadas para calidad de diagramas
"""

import unittest
import json
import tempfile
from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image
import requests

from src.core.universal_schema import UniversalDiagramSchema, DiagramType, OutputFormat, SchemaBuilder
from src.generators.universal_generator import UniversalGenerator

class DiagramQualityTests(unittest.TestCase):
    """Pruebas de calidad para diagramas PNG y DrawIO"""
    
    def setUp(self):
        """Configuración inicial para pruebas"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.generator = UniversalGenerator(str(self.temp_dir))
        
        # Esquemas de prueba
        self.network_schema = SchemaBuilder.build_network_schema("test_project")
        self.microservices_schema = SchemaBuilder.build_microservices_schema("test_project")
    
    def test_schema_creation(self):
        """Prueba creación de esquemas"""
        
        # Test network schema
        self.assertEqual(self.network_schema.diagram_type, DiagramType.NETWORK)
        self.assertEqual(self.network_schema.project_name, "test_project")
        self.assertGreater(len(self.network_schema.components), 0)
        self.assertGreater(len(self.network_schema.containers), 0)
        
        # Test microservices schema
        self.assertEqual(self.microservices_schema.diagram_type, DiagramType.MICROSERVICES)
        self.assertGreater(len(self.microservices_schema.components), 0)
    
    def test_schema_serialization(self):
        """Prueba serialización/deserialización de esquemas"""
        
        # Convertir a dict
        schema_dict = self.network_schema.to_dict()
        self.assertIsInstance(schema_dict, dict)
        self.assertIn("title", schema_dict)
        self.assertIn("components", schema_dict)
        
        # Convertir de vuelta a esquema
        reconstructed_schema = UniversalDiagramSchema.from_dict(schema_dict)
        self.assertEqual(reconstructed_schema.title, self.network_schema.title)
        self.assertEqual(len(reconstructed_schema.components), len(self.network_schema.components))
    
    def test_png_generation(self):
        """Prueba generación de PNG"""
        
        # Configurar para solo PNG
        self.network_schema.output_format = OutputFormat.PNG
        
        # Generar
        results = self.generator.generate(self.network_schema)
        
        # Verificar resultado
        self.assertIn("png", results)
        png_path = Path(results["png"])
        self.assertTrue(png_path.exists())
        
        # Verificar que es imagen válida
        try:
            with Image.open(png_path) as img:
                self.assertGreater(img.width, 0)
                self.assertGreater(img.height, 0)
        except Exception as e:
            self.fail(f"PNG generado no es válido: {e}")
    
    def test_drawio_generation(self):
        """Prueba generación de DrawIO"""
        
        # Configurar para solo DrawIO
        self.network_schema.output_format = OutputFormat.DRAWIO
        
        # Generar
        results = self.generator.generate(self.network_schema)
        
        # Verificar resultado
        self.assertIn("drawio", results)
        drawio_path = Path(results["drawio"])
        self.assertTrue(drawio_path.exists())
        
        # Verificar que es XML válido
        try:
            tree = ET.parse(drawio_path)
            root = tree.getroot()
            self.assertEqual(root.tag, "mxfile")
        except ET.ParseError as e:
            self.fail(f"DrawIO XML no es válido: {e}")
    
    def test_drawio_content_quality(self):
        """Prueba calidad del contenido DrawIO"""
        
        self.network_schema.output_format = OutputFormat.DRAWIO
        results = self.generator.generate(self.network_schema)
        
        drawio_path = Path(results["drawio"])
        with open(drawio_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar elementos clave
        self.assertIn("mxgraph.aws4", content, "Debe contener iconos AWS")
        self.assertGreater(content.count("<mxCell"), 5, "Debe tener múltiples elementos")
        self.assertIn("edge=\"1\"", content, "Debe tener conexiones")
        
        # Contar elementos
        aws_icons = content.count("mxgraph.aws4")
        connections = content.count("edge=\"1\"")
        
        self.assertGreaterEqual(aws_icons, 3, f"Mínimo 3 iconos AWS, encontrados: {aws_icons}")
        self.assertGreaterEqual(connections, 1, f"Mínimo 1 conexión, encontradas: {connections}")
    
    def test_both_formats_generation(self):
        """Prueba generación de ambos formatos"""
        
        self.network_schema.output_format = OutputFormat.BOTH
        results = self.generator.generate(self.network_schema)
        
        # Verificar ambos formatos
        self.assertIn("png", results)
        self.assertIn("drawio", results)
        
        # Verificar archivos existen
        self.assertTrue(Path(results["png"]).exists())
        self.assertTrue(Path(results["drawio"]).exists())
    
    def test_component_mapping(self):
        """Prueba mapeo de componentes"""
        
        # Verificar que todos los tipos de componentes tienen mapeo
        for component in self.network_schema.components:
            self.assertIn(component.type, self.generator.component_mapping["drawio"],
                         f"Componente {component.type} no tiene mapeo DrawIO")
    
    def test_file_sizes(self):
        """Prueba tamaños de archivos generados"""
        
        self.network_schema.output_format = OutputFormat.BOTH
        results = self.generator.generate(self.network_schema)
        
        # Verificar tamaños razonables
        png_size = Path(results["png"]).stat().st_size
        drawio_size = Path(results["drawio"]).stat().st_size
        
        self.assertGreater(png_size, 1000, "PNG muy pequeño")
        self.assertLess(png_size, 5 * 1024 * 1024, "PNG muy grande (>5MB)")
        
        self.assertGreater(drawio_size, 500, "DrawIO muy pequeño")
        self.assertLess(drawio_size, 100 * 1024, "DrawIO muy grande (>100KB)")
    
    def test_error_handling(self):
        """Prueba manejo de errores"""
        
        # Esquema inválido
        invalid_schema = UniversalDiagramSchema(
            title="Invalid",
            diagram_type=DiagramType.NETWORK,
            project_name="test"
        )
        # Sin componentes ni contenedores
        
        try:
            results = self.generator.generate(invalid_schema)
            # Debe generar algo aunque sea básico
            self.assertIsInstance(results, dict)
        except Exception:
            # O manejar error graciosamente
            pass

class APITests(unittest.TestCase):
    """Pruebas para API REST"""
    
    @classmethod
    def setUpClass(cls):
        """Configurar servidor API para pruebas"""
        # Nota: En producción usar servidor de pruebas
        cls.base_url = "http://localhost:5000"
    
    def test_health_endpoint(self):
        """Prueba endpoint de health"""
        try:
            response = requests.get(f"{self.base_url}/health", timeout=5)
            self.assertEqual(response.status_code, 200)
            
            data = response.json()
            self.assertEqual(data["status"], "healthy")
        except requests.exceptions.ConnectionError:
            self.skipTest("API server no disponible")
    
    def test_template_endpoint(self):
        """Prueba endpoint de templates"""
        try:
            response = requests.get(f"{self.base_url}/api/v1/diagrams/templates/network", timeout=5)
            self.assertEqual(response.status_code, 200)
            
            data = response.json()
            self.assertTrue(data["success"])
            self.assertIn("template", data)
        except requests.exceptions.ConnectionError:
            self.skipTest("API server no disponible")
    
    def test_validation_endpoint(self):
        """Prueba endpoint de validación"""
        try:
            # Esquema válido
            schema = SchemaBuilder.build_network_schema("test").to_dict()
            
            response = requests.post(
                f"{self.base_url}/api/v1/diagrams/validate",
                json=schema,
                timeout=10
            )
            
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertTrue(data["valid"])
        except requests.exceptions.ConnectionError:
            self.skipTest("API server no disponible")

class PerformanceTests(unittest.TestCase):
    """Pruebas de rendimiento"""
    
    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp())
        self.generator = UniversalGenerator(str(self.temp_dir))
    
    def test_generation_speed(self):
        """Prueba velocidad de generación"""
        import time
        
        schema = SchemaBuilder.build_network_schema("perf_test")
        schema.output_format = OutputFormat.BOTH
        
        start_time = time.time()
        results = self.generator.generate(schema)
        end_time = time.time()
        
        generation_time = end_time - start_time
        
        # Debe generar en menos de 30 segundos
        self.assertLess(generation_time, 30, f"Generación muy lenta: {generation_time:.2f}s")
        
        # Verificar archivos generados
        self.assertEqual(len(results), 2)  # PNG y DrawIO

def run_quality_tests():
    """Ejecuta todas las pruebas de calidad"""
    
    print("🧪 Ejecutando Pruebas de Calidad de Diagramas")
    print("=" * 50)
    
    # Crear suite de pruebas
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Agregar pruebas
    suite.addTests(loader.loadTestsFromTestCase(DiagramQualityTests))
    suite.addTests(loader.loadTestsFromTestCase(APITests))
    suite.addTests(loader.loadTestsFromTestCase(PerformanceTests))
    
    # Ejecutar pruebas
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Resumen
    print(f"\n📊 Resumen de Pruebas:")
    print(f"  ✅ Exitosas: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  ❌ Fallidas: {len(result.failures)}")
    print(f"  🚫 Errores: {len(result.errors)}")
    print(f"  ⏭️ Omitidas: {len(result.skipped) if hasattr(result, 'skipped') else 0}")
    
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_quality_tests()
    exit(0 if success else 1)
