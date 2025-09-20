#!/usr/bin/env python3
"""
Automated Quality Tests - Tests automatizados para asegurar calidad de diagramas
"""

import unittest
import json
import tempfile
import os
from pathlib import Path
from typing import Dict, Any, List
import xml.etree.ElementTree as ET

# Imports del sistema
from src.validators.xml_validator import DrawIOXMLValidator, MCPIntegrator, validate_drawio_file
from templates.drawio_templates import DrawIOTemplates
from src.components.aws_components import ComponentFactory, ComponentType

class StandardModelTests(unittest.TestCase):
    """Tests para el modelo estándar de entrada"""
    
    def setUp(self):
        """Configuración inicial"""
        self.temp_dir = Path(tempfile.mkdtemp())
        
        # Modelo de prueba válido
        self.valid_model = {
            "metadata": {
                "title": "Test Architecture",
                "project_name": "test_project",
                "diagram_type": "network",
                "version": "1.0.0"
            },
            "canvas": {
                "width": 2500,
                "height": 1600,
                "grid_size": 10,
                "background": "white"
            },
            "architecture": {
                "components": [
                    {
                        "id": "api_gw",
                        "type": "api_gateway",
                        "label": "API Gateway",
                        "position": {"x": 200, "y": 200},
                        "size": {"width": 100, "height": 80}
                    },
                    {
                        "id": "fargate_app",
                        "type": "fargate",
                        "label": "App Service",
                        "position": {"x": 400, "y": 200},
                        "size": {"width": 100, "height": 80}
                    }
                ],
                "connections": [
                    {
                        "id": "conn_api_app",
                        "from": "api_gw",
                        "to": "fargate_app",
                        "label": "HTTP",
                        "type": "http"
                    }
                ]
            }
        }
    
    def test_model_validation(self):
        """Test validación del modelo estándar"""
        
        # Modelo válido
        errors = DrawIOTemplates.validate_template_data(self.valid_model)
        self.assertEqual(len(errors), 0, f"Modelo válido no debe tener errores: {errors}")
        
        # Modelo inválido - sin metadata
        invalid_model = {"architecture": {}}
        errors = DrawIOTemplates.validate_template_data(invalid_model)
        self.assertGreater(len(errors), 0, "Modelo sin metadata debe tener errores")
        
        # Modelo inválido - sin components ni containers
        invalid_model2 = {
            "metadata": {"title": "Test", "project_name": "test", "diagram_type": "network"},
            "architecture": {}
        }
        errors = DrawIOTemplates.validate_template_data(invalid_model2)
        self.assertGreater(len(errors), 0, "Modelo sin componentes debe tener errores")
    
    def test_component_factory(self):
        """Test factory de componentes"""
        
        # Crear componente válido
        component = ComponentFactory.create_component(
            "api_gateway", "test_api", "Test API Gateway"
        )
        
        self.assertEqual(component.id, "test_api")
        self.assertEqual(component.component_type, ComponentType.API_GATEWAY)
        self.assertEqual(component.aws_service_name, "Amazon API Gateway")
        
        # Tipo no soportado
        with self.assertRaises(ValueError):
            ComponentFactory.create_component("invalid_type", "test", "Test")
    
    def test_component_validation(self):
        """Test validación de componentes"""
        
        component = ComponentFactory.create_component(
            "fargate", "test_fargate", "Test Fargate"
        )
        
        # Componente válido
        errors = component.validate()
        self.assertEqual(len(errors), 0, f"Componente válido no debe tener errores: {errors}")
        
        # ID inválido
        component.id = "123invalid"
        errors = component.validate()
        self.assertGreater(len(errors), 0, "ID inválido debe generar error")
        
        # Tamaño muy pequeño
        component.id = "valid_id"
        component.size.width = 10
        errors = component.validate()
        self.assertGreater(len(errors), 0, "Tamaño muy pequeño debe generar error")

class XMLValidationTests(unittest.TestCase):
    """Tests para validación de XML DrawIO"""
    
    def setUp(self):
        """Configuración inicial"""
        self.validator = DrawIOXMLValidator()
        
        # XML válido básico
        self.valid_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net">
  <diagram name="Test" id="test">
    <mxGraphModel dx="1600" dy="900" grid="1" gridSize="10">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="api_gw" value="API Gateway" style="sketch=0;shape=mxgraph.aws4.api_gateway;" vertex="1" parent="1">
          <mxGeometry x="200" y="200" width="100" height="80" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
        
        # XML inválido
        self.invalid_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<invalid>
  <missing>elements</missing>
</invalid>'''
    
    def test_xml_structure_validation(self):
        """Test validación de estructura XML"""
        
        # XML válido
        is_valid, errors = self.validator.validate_xml_structure(self.valid_xml)
        self.assertTrue(is_valid, f"XML válido debe pasar validación: {errors}")
        
        # XML inválido
        is_valid, errors = self.validator.validate_xml_structure(self.invalid_xml)
        self.assertFalse(is_valid, "XML inválido debe fallar validación")
        self.assertGreater(len(errors), 0, "XML inválido debe tener errores")
    
    def test_aws_components_validation(self):
        """Test validación de componentes AWS"""
        
        is_valid, analysis = self.validator.validate_aws_components(self.valid_xml)
        
        self.assertIsInstance(analysis, dict)
        self.assertIn("aws_components", analysis)
        self.assertGreater(analysis["aws_components"], 0, "Debe encontrar componentes AWS")
        self.assertIn("component_details", analysis)
    
    def test_diagram_completeness(self):
        """Test validación de completitud"""
        
        expected_components = ["api_gateway"]
        is_complete, analysis = self.validator.validate_diagram_completeness(
            self.valid_xml, expected_components
        )
        
        self.assertIsInstance(analysis, dict)
        self.assertIn("completeness", analysis)
        
        completeness = analysis["completeness"]
        self.assertEqual(completeness["expected"], 1)
        self.assertEqual(completeness["found"], 1)
        self.assertEqual(len(completeness["missing"]), 0)

class TemplateGenerationTests(unittest.TestCase):
    """Tests para generación de templates DrawIO"""
    
    def setUp(self):
        """Configuración inicial"""
        self.temp_dir = Path(tempfile.mkdtemp())
    
    def test_network_template_generation(self):
        """Test generación de template de red"""
        
        template = DrawIOTemplates.get_network_template("test_project")
        
        # Verificar estructura
        self.assertIn("metadata", template)
        self.assertIn("architecture", template)
        
        # Verificar contenido
        self.assertEqual(template["metadata"]["project_name"], "test_project")
        self.assertEqual(template["metadata"]["diagram_type"], "network")
        
        # Verificar componentes
        components = template["architecture"]["components"]
        self.assertGreater(len(components), 0, "Template debe tener componentes")
        
        # Verificar conexiones
        connections = template["architecture"]["connections"]
        self.assertGreater(len(connections), 0, "Template debe tener conexiones")
    
    def test_xml_generation_from_template(self):
        """Test generación de XML desde template"""
        
        template = DrawIOTemplates.get_network_template("test_project")
        xml_content = DrawIOTemplates.generate_drawio_xml(template)
        
        # Verificar que es XML válido
        try:
            ET.fromstring(xml_content)
        except ET.ParseError:
            self.fail("XML generado no es válido")
        
        # Verificar contenido
        self.assertIn("mxfile", xml_content)
        self.assertIn("diagram", xml_content)
        self.assertIn("mxgraph.aws4", xml_content)
    
    def test_component_style_mapping(self):
        """Test mapeo de estilos de componentes"""
        
        # Verificar que todos los tipos tienen estilo
        for comp_type in ["fargate", "rds", "api_gateway", "s3"]:
            self.assertIn(comp_type, DrawIOTemplates.COMPONENT_STYLES,
                         f"Tipo {comp_type} debe tener estilo definido")
        
        # Verificar estructura de estilos
        for style in DrawIOTemplates.COMPONENT_STYLES.values():
            self.assertIn("gradient_color", style)
            self.assertIn("fill_color", style)
            self.assertIn("shape", style)

class MCPIntegrationTests(unittest.TestCase):
    """Tests para integración con MCP"""
    
    def setUp(self):
        """Configuración inicial"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.integrator = MCPIntegrator()
        
        # Configuración MCP de prueba
        self.test_mcp_config = {
            "project_name": "test_mcp_project",
            "microservices": {
                "certificate_service": {
                    "business_function": "PDF Certificate Generation",
                    "technology": "Python"
                },
                "api_service": {
                    "business_function": "REST API",
                    "technology": "Node.js"
                }
            },
            "aws_services": {
                "rds": {
                    "engine": "postgresql",
                    "instance_class": "db.r5.2xlarge"
                },
                "s3": {
                    "storage_class": "STANDARD",
                    "versioning": True
                }
            }
        }
    
    def test_mcp_to_standard_conversion(self):
        """Test conversión de MCP a modelo estándar"""
        
        standard_model = self.integrator.convert_mcp_to_standard_model(self.test_mcp_config)
        
        # Verificar estructura
        self.assertIn("metadata", standard_model)
        self.assertIn("architecture", standard_model)
        
        # Verificar metadata
        metadata = standard_model["metadata"]
        self.assertEqual(metadata["project_name"], "test_mcp_project")
        self.assertIn("mcp", metadata["tags"])
        
        # Verificar componentes
        components = standard_model["architecture"]["components"]
        self.assertEqual(len(components), 4)  # 2 microservicios + 2 servicios AWS
        
        # Verificar tipos de componentes
        component_types = [comp["type"] for comp in components]
        self.assertIn("fargate", component_types)  # Microservicios
        self.assertIn("rds", component_types)      # Servicios AWS
        self.assertIn("s3", component_types)
    
    def test_mcp_xml_validation(self):
        """Test validación de XML generado desde MCP"""
        
        # Generar modelo estándar desde MCP
        standard_model = self.integrator.convert_mcp_to_standard_model(self.test_mcp_config)
        
        # Generar XML
        xml_content = DrawIOTemplates.generate_drawio_xml(standard_model)
        
        # Validar XML con contexto MCP
        validation_result = self.integrator.validate_mcp_generated_xml(
            xml_content, self.test_mcp_config
        )
        
        # Verificar resultado
        self.assertIn("overall_valid", validation_result)
        self.assertIn("mcp_integration", validation_result)
        
        mcp_integration = validation_result["mcp_integration"]
        self.assertEqual(mcp_integration["expected_microservices"], 2)
        self.assertEqual(mcp_integration["expected_aws_services"], 2)

class EndToEndTests(unittest.TestCase):
    """Tests end-to-end del sistema completo"""
    
    def setUp(self):
        """Configuración inicial"""
        self.temp_dir = Path(tempfile.mkdtemp())
    
    def test_complete_workflow(self):
        """Test flujo completo: MCP -> Modelo Estándar -> XML -> Validación"""
        
        # 1. Configuración MCP
        mcp_config = {
            "project_name": "e2e_test",
            "microservices": {
                "web_service": {
                    "business_function": "Web Interface"
                }
            },
            "aws_services": {
                "rds": {"engine": "postgresql"}
            }
        }
        
        # 2. Conversión a modelo estándar
        integrator = MCPIntegrator()
        standard_model = integrator.convert_mcp_to_standard_model(mcp_config)
        
        # 3. Generación de XML
        xml_content = DrawIOTemplates.generate_drawio_xml(standard_model)
        
        # 4. Validación completa
        validator = DrawIOXMLValidator()
        
        # Validación estructural
        is_valid_structure, structure_errors = validator.validate_xml_structure(xml_content)
        self.assertTrue(is_valid_structure, f"Estructura XML inválida: {structure_errors}")
        
        # Validación de componentes
        is_valid_aws, aws_analysis = validator.validate_aws_components(xml_content)
        self.assertGreater(aws_analysis["aws_components"], 0, "Debe tener componentes AWS")
        
        # Validación MCP
        mcp_validation = integrator.validate_mcp_generated_xml(xml_content, mcp_config)
        self.assertTrue(mcp_validation["overall_valid"], "Validación MCP debe pasar")
    
    def test_file_operations(self):
        """Test operaciones con archivos"""
        
        # Crear archivo de prueba
        test_xml = DrawIOTemplates.generate_drawio_xml(
            DrawIOTemplates.get_network_template("file_test")
        )
        
        test_file = self.temp_dir / "test_diagram.drawio"
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(test_xml)
        
        # Validar archivo
        result = validate_drawio_file(str(test_file))
        
        self.assertTrue(result["valid"], f"Archivo debe ser válido: {result}")
        self.assertIn("analysis", result)

def run_all_tests():
    """Ejecuta todos los tests automatizados"""
    
    print("🧪 Ejecutando Tests Automatizados de Calidad")
    print("=" * 60)
    
    # Crear suite de tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Agregar todas las clases de test
    test_classes = [
        StandardModelTests,
        XMLValidationTests,
        TemplateGenerationTests,
        MCPIntegrationTests,
        EndToEndTests
    ]
    
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Ejecutar tests
    runner = unittest.TextTestRunner(verbosity=2, buffer=True)
    result = runner.run(suite)
    
    # Resumen detallado
    print(f"\n📊 RESUMEN DE TESTS:")
    print(f"  ✅ Exitosos: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  ❌ Fallidos: {len(result.failures)}")
    print(f"  🚫 Errores: {len(result.errors)}")
    
    if hasattr(result, 'skipped'):
        print(f"  ⏭️ Omitidos: {len(result.skipped)}")
    
    # Detalles de fallos
    if result.failures:
        print(f"\n❌ TESTS FALLIDOS:")
        for test, traceback in result.failures:
            print(f"  - {test}: {traceback.split('AssertionError: ')[-1].split('\\n')[0]}")
    
    if result.errors:
        print(f"\n🚫 TESTS CON ERRORES:")
        for test, traceback in result.errors:
            print(f"  - {test}: {traceback.split('\\n')[-2]}")
    
    # Calificación final
    success_rate = (result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100
    print(f"\n🎯 CALIFICACIÓN: {success_rate:.1f}%")
    
    if success_rate >= 95:
        print("  🎉 EXCELENTE - Sistema de alta calidad")
    elif success_rate >= 80:
        print("  👍 BUENO - Sistema estable")
    elif success_rate >= 60:
        print("  ⚠️ REGULAR - Necesita mejoras")
    else:
        print("  ❌ CRÍTICO - Requiere atención inmediata")
    
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_all_tests()
    exit(0 if success else 1)
