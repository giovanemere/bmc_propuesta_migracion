# 📋 Guía Completa del Flujo de Diagramas

## 🎯 Descripción General

Sistema completo para generación automática de diagramas PNG y DrawIO desde modelo estándar, con integración MCP, validación XML y tests automatizados.

## 🏗️ Arquitectura del Sistema

```
📦 Sistema Completo de Diagramas
├── 📋 Modelo Estándar JSON/YAML
├── 🏭 Clases por Componente AWS
├── 📄 Plantillas XML DrawIO
├── ✅ Validador XML + MCP Integration
├── 🧪 Tests Automatizados
└── 📚 Documentación Completa
```

## 📋 1. Modelo de Entrada Estándar

### Esquema JSON Completo

**Archivo:** `schemas/standard_input_model.json`

```json
{
  "metadata": {
    "title": "BMC Network Architecture",
    "project_name": "bmc_input",
    "diagram_type": "network",
    "version": "1.0.0",
    "description": "Arquitectura de red para BMC",
    "tags": ["aws", "vpc", "multi-az"]
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
        "id": "api_gateway",
        "type": "api_gateway",
        "label": "API Gateway\nREST + GraphQL",
        "position": {"x": 200, "y": 200},
        "size": {"width": 100, "height": 80},
        "properties": {
          "throttle_rate": "10000/sec",
          "burst_limit": "5000"
        },
        "metadata": {
          "capacity": "10K requests/sec",
          "sla": "99.9%"
        }
      }
    ],
    "containers": [
      {
        "id": "vpc_main",
        "type": "vpc",
        "label": "VPC 10.0.0.0/16",
        "bounds": {"x": 50, "y": 300, "width": 2000, "height": 1000},
        "properties": {
          "cidr": "10.0.0.0/16",
          "dns_hostnames": true
        },
        "components": [...]
      }
    ],
    "connections": [
      {
        "id": "conn_api_app",
        "from": "api_gateway",
        "to": "fargate_app",
        "label": "HTTP",
        "type": "http",
        "properties": {
          "protocol": "HTTPS",
          "port": 443,
          "encryption": true
        }
      }
    ]
  },
  "output": {
    "formats": ["png", "drawio"],
    "auto_layout": true,
    "theme": "aws"
  }
}
```

### Tipos de Componentes Soportados

| Categoría | Tipos | DrawIO Shape | PNG Class |
|-----------|-------|--------------|-----------|
| **Compute** | `fargate`, `lambda`, `ec2` | `mxgraph.aws4.fargate` | `diagrams.aws.compute.Fargate` |
| **Database** | `rds`, `dynamodb`, `elasticache` | `mxgraph.aws4.rds` | `diagrams.aws.database.RDS` |
| **Storage** | `s3`, `efs`, `ebs` | `mxgraph.aws4.s3` | `diagrams.aws.storage.S3` |
| **Network** | `api_gateway`, `elb`, `cloudfront` | `mxgraph.aws4.api_gateway` | `diagrams.aws.network.APIGateway` |
| **Security** | `waf`, `cognito`, `kms` | `mxgraph.aws4.waf` | `diagrams.aws.security.WAF` |

## 🏭 2. Clases por Componente

### Ejemplo de Uso

```python
from src.components.aws_components import ComponentFactory, VPC, Fargate

# Crear componente usando factory
api_gateway = ComponentFactory.create_component(
    "api_gateway", 
    "main_api", 
    "API Gateway\nREST + GraphQL",
    throttle_rate="10000/sec"
)

# Crear componente directamente
fargate_app = Fargate(
    "app_service",
    "Certificate Service\nPDF Generation", 
    cpu="2 vCPU",
    memory="4 GB"
)

# Validar componente
errors = fargate_app.validate()
if errors:
    print(f"Errores: {errors}")

# Convertir a diccionario
component_dict = fargate_app.to_dict()
```

### Componentes con Propiedades Específicas

```python
# RDS con configuración específica
rds_db = ComponentFactory.create_component(
    "rds",
    "main_database",
    "RDS PostgreSQL\nPrimary Instance",
    engine="postgresql",
    instance_class="db.r5.2xlarge",
    multi_az=True,
    storage_encrypted=True
)

# S3 con configuración de storage
s3_bucket = ComponentFactory.create_component(
    "s3",
    "document_storage", 
    "S3 Storage\nDocuments & Assets",
    storage_class="STANDARD",
    versioning=True,
    encryption="AES256"
)
```

## 📄 3. Plantillas XML DrawIO

### Generación Automática

```python
from templates.drawio_templates import DrawIOTemplates

# Obtener template predefinido
template = DrawIOTemplates.get_network_template("bmc_project")

# Generar XML DrawIO
xml_content = DrawIOTemplates.generate_drawio_xml(template)

# Guardar archivo
with open("architecture.drawio", "w") as f:
    f.write(xml_content)
```

### Personalización de Estilos

```python
# Estilos personalizados por componente
custom_styles = {
    "fargate": {
        "gradient_color": "#F78E04",
        "fill_color": "#D05C17",
        "shape": "mxgraph.aws4.fargate"
    },
    "rds": {
        "gradient_color": "#4AB29A", 
        "fill_color": "#116D5B",
        "shape": "mxgraph.aws4.rds"
    }
}

# Aplicar estilos personalizados
DrawIOTemplates.COMPONENT_STYLES.update(custom_styles)
```

## ✅ 4. Validación XML y MCP Integration

### Validación Completa

```python
from src.validators.xml_validator import validate_drawio_file, MCPIntegrator

# Validar archivo DrawIO
result = validate_drawio_file(
    "architecture.drawio",
    mcp_config_path="config/bmc-config.json"
)

if result["valid"]:
    print("✅ DrawIO válido")
    print(f"Componentes AWS: {result['analysis']['aws_components']}")
    print(f"Conexiones: {result['analysis']['connections']}")
else:
    print(f"❌ Errores: {result['errors']}")
```

### Integración MCP

```python
# Convertir configuración MCP a modelo estándar
integrator = MCPIntegrator("config/bmc-config.json")
mcp_config = integrator.load_mcp_config()
standard_model = integrator.convert_mcp_to_standard_model(mcp_config)

# Generar y validar XML desde MCP
xml_content = DrawIOTemplates.generate_drawio_xml(standard_model)
validation = integrator.validate_mcp_generated_xml(xml_content, mcp_config)

print(f"Válido: {validation['overall_valid']}")
print(f"Microservicios esperados: {validation['mcp_integration']['expected_microservices']}")
```

## 🧪 5. Tests Automatizados

### Ejecutar Tests

```bash
# Ejecutar todos los tests
cd /path/to/project
python -m tests.automated_quality_tests

# Ejecutar tests específicos
python -m unittest tests.automated_quality_tests.StandardModelTests
python -m unittest tests.automated_quality_tests.XMLValidationTests
python -m unittest tests.automated_quality_tests.MCPIntegrationTests
```

### Tipos de Tests

| Categoría | Tests | Descripción |
|-----------|-------|-------------|
| **StandardModelTests** | 4 tests | Validación del modelo estándar |
| **XMLValidationTests** | 3 tests | Validación de estructura XML |
| **TemplateGenerationTests** | 3 tests | Generación de templates |
| **MCPIntegrationTests** | 2 tests | Integración con MCP |
| **EndToEndTests** | 2 tests | Flujo completo |

### Ejemplo de Test Personalizado

```python
import unittest
from src.validators.xml_validator import DrawIOXMLValidator

class CustomValidationTests(unittest.TestCase):
    
    def test_custom_component_validation(self):
        """Test validación de componente personalizado"""
        
        xml_content = """<?xml version="1.0"?>
        <mxfile>
          <diagram>
            <mxGraphModel>
              <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="custom" value="Custom Component" 
                       style="shape=mxgraph.aws4.fargate;" 
                       vertex="1" parent="1"/>
              </root>
            </mxGraphModel>
          </diagram>
        </mxfile>"""
        
        validator = DrawIOXMLValidator()
        is_valid, analysis = validator.validate_aws_components(xml_content)
        
        self.assertTrue(is_valid)
        self.assertEqual(analysis["aws_components"], 1)
```

## 🔄 6. Flujo Completo End-to-End

### Opción A: Desde Configuración MCP

```python
# 1. Cargar configuración MCP existente
integrator = MCPIntegrator("config/bmc-config.json")
mcp_config = integrator.load_mcp_config()

# 2. Convertir a modelo estándar
standard_model = integrator.convert_mcp_to_standard_model(mcp_config)

# 3. Generar diagramas
xml_content = DrawIOTemplates.generate_drawio_xml(standard_model)

# 4. Validar resultado
validation = integrator.validate_mcp_generated_xml(xml_content, mcp_config)

# 5. Guardar archivos
with open("outputs/bmc_architecture.drawio", "w") as f:
    f.write(xml_content)

print(f"✅ Generación completa - Válido: {validation['overall_valid']}")
```

### Opción B: Desde Modelo Estándar

```python
# 1. Definir modelo estándar
model = {
    "metadata": {
        "title": "Custom Architecture",
        "project_name": "custom_project",
        "diagram_type": "network"
    },
    "architecture": {
        "components": [
            {
                "id": "api",
                "type": "api_gateway",
                "label": "API Gateway",
                "position": {"x": 200, "y": 200}
            },
            {
                "id": "app", 
                "type": "fargate",
                "label": "App Service",
                "position": {"x": 400, "y": 200}
            }
        ],
        "connections": [
            {
                "id": "api_to_app",
                "from": "api",
                "to": "app",
                "type": "http"
            }
        ]
    }
}

# 2. Validar modelo
errors = DrawIOTemplates.validate_template_data(model)
if errors:
    print(f"❌ Errores en modelo: {errors}")
    exit(1)

# 3. Generar XML
xml_content = DrawIOTemplates.generate_drawio_xml(model)

# 4. Validar XML
validator = DrawIOXMLValidator()
is_valid, validation_errors = validator.validate_xml_structure(xml_content)

if is_valid:
    print("✅ XML válido generado")
else:
    print(f"❌ XML inválido: {validation_errors}")
```

### Opción C: Usando API REST

```python
import requests

# 1. Obtener template
response = requests.get("http://localhost:5000/api/v1/diagrams/templates/network")
template = response.json()["template"]

# 2. Personalizar template
template["metadata"]["project_name"] = "my_project"
template["architecture"]["components"][0]["label"] = "My API Gateway"

# 3. Generar diagrama
response = requests.post(
    "http://localhost:5000/api/v1/diagrams/generate",
    json=template
)

if response.status_code == 200:
    result = response.json()
    print(f"✅ Diagramas generados: {result['generated_files']}")
else:
    print(f"❌ Error: {response.json()}")
```

## 📊 7. Métricas de Calidad

### Validación Automática

El sistema valida automáticamente:

- ✅ **Estructura XML** - Elementos requeridos, IDs únicos
- ✅ **Componentes AWS** - Iconos oficiales, configuración válida  
- ✅ **Completitud** - Todos los componentes esperados presentes
- ✅ **Integración MCP** - Coherencia con configuración original
- ✅ **Conexiones** - Referencias válidas entre componentes

### Métricas Reportadas

```json
{
  "overall_valid": true,
  "structure": {
    "valid": true,
    "errors": []
  },
  "aws_components": {
    "aws_components": 8,
    "connections": 6,
    "total_elements": 15,
    "aws_shapes": ["mxgraph.aws4.fargate", "mxgraph.aws4.rds"]
  },
  "completeness": {
    "expected": 8,
    "found": 8,
    "missing": [],
    "completeness_percentage": 100.0
  },
  "mcp_integration": {
    "expected_microservices": 2,
    "expected_aws_services": 3,
    "total_expected": 5
  }
}
```

## 🚀 8. Mejores Prácticas

### Diseño de Modelos

1. **IDs Únicos**: Usar nombres descriptivos (`api_gateway_main`, no `comp1`)
2. **Labels Informativos**: Incluir información técnica relevante
3. **Posicionamiento**: Usar grid de 10px para alineación
4. **Agrupación**: Usar containers para organizar componentes relacionados

### Validación Continua

```python
# Validar antes de generar
def safe_generate_diagram(model):
    # 1. Validar modelo
    errors = DrawIOTemplates.validate_template_data(model)
    if errors:
        raise ValueError(f"Modelo inválido: {errors}")
    
    # 2. Generar XML
    xml_content = DrawIOTemplates.generate_drawio_xml(model)
    
    # 3. Validar XML
    validator = DrawIOXMLValidator()
    is_valid, validation_errors = validator.validate_xml_structure(xml_content)
    if not is_valid:
        raise ValueError(f"XML inválido: {validation_errors}")
    
    return xml_content
```

### Tests Personalizados

```python
# Crear tests específicos para tu proyecto
class ProjectSpecificTests(unittest.TestCase):
    
    def test_bmc_architecture_completeness(self):
        """Verifica que arquitectura BMC tenga todos los componentes"""
        
        required_components = [
            "api_gateway", "fargate", "rds", "s3", 
            "cloudfront", "waf", "cognito"
        ]
        
        # Generar desde MCP
        integrator = MCPIntegrator("config/bmc-config.json")
        mcp_config = integrator.load_mcp_config()
        standard_model = integrator.convert_mcp_to_standard_model(mcp_config)
        xml_content = DrawIOTemplates.generate_drawio_xml(standard_model)
        
        # Validar completitud
        validator = DrawIOXMLValidator()
        is_complete, analysis = validator.validate_diagram_completeness(
            xml_content, required_components
        )
        
        self.assertTrue(is_complete, 
                       f"Faltan componentes: {analysis['completeness']['missing']}")
```

## 🎯 9. Próximos Pasos

### Integración en Pipeline

1. **CI/CD**: Agregar tests automatizados al pipeline
2. **API Deployment**: Desplegar API REST para uso en producción
3. **Monitoring**: Agregar métricas de uso y performance
4. **Extensiones**: Agregar soporte para Azure/GCP

### Mejoras Futuras

- **Layout Automático**: Algoritmos de posicionamiento inteligente
- **Temas Visuales**: Múltiples temas (dark, light, corporate)
- **Exportación**: Soporte para más formatos (SVG, PDF, Visio)
- **Colaboración**: Integración con herramientas de equipo

---

**El sistema está completo y listo para generar diagramas de calidad profesional desde cualquier entrada estándar, con validación automática y integración MCP.**
