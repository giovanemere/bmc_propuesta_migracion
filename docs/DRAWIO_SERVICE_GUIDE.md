# 📐 Servicio DrawIO - Guía Completa

## 🎯 Descripción General

El **Servicio DrawIO** genera diagramas editables en formato Draw.io usando **exactamente la misma entrada** que los PNG. Incluye integración con API, conversores de modelos y documentación completa.

## 🏗️ Arquitectura del Servicio

```
📦 DrawIO Service
├── 🔧 Universal Generator (misma entrada que PNG)
├── 🌐 API Integration (diagrams.net)
├── 🔄 Model Converters (JSON/YAML → DrawIO)
└── 📚 Documentation & Examples
```

## 🚀 Uso Rápido

### 1. Generar DrawIO desde PNG Input

```python
from src.generators.universal_drawio_generator import UniversalDrawIOGenerator

# Usar misma configuración que PNG
config = {...}  # Misma config que diagram_generator.py
generator = UniversalDrawIOGenerator(config, "outputs/")

# Generar network (usa líneas 60-120 del PNG generator)
drawio_path = generator.generate_from_png_input("network", "bmc_input")
```

### 2. Integración con Draw.io API

```python
from src.integrations.drawio_api_client import DrawIOAPIClient

# Crear cliente
client = DrawIOAPIClient()

# Crear URL de Draw.io desde XML
with open("diagram.drawio", "r") as f:
    xml_content = f.read()

result = client.create_diagram_from_xml(xml_content, "BMC Architecture")
print(f"URL: {result['url']}")

# Exportar a PNG usando API
client.export_diagram(xml_content, "png")
```

### 3. Convertir Modelos a DrawIO

```python
from src.converters.model_to_drawio_converter import ModelToDrawIOConverter

# Desde JSON
converter = ModelToDrawIOConverter()
drawio_path = converter.convert_json_to_drawio("architecture.json")

# Desde YAML
drawio_path = converter.convert_yaml_to_drawio("architecture.yaml")

# Desde diccionario Python
model = {
    "title": "AWS Architecture",
    "components": [...],
    "connections": [...]
}
drawio_path = converter.convert_dict_to_drawio(model, "output.drawio")
```

## 📋 Componentes del Servicio

### 🔧 1. Universal DrawIO Generator

**Archivo:** `src/generators/universal_drawio_generator.py`

**Función:** Genera DrawIO usando **exactamente la misma entrada** que PNG

**Características:**
- ✅ Mapeo directo PNG → DrawIO
- ✅ Replica lógica línea por línea del PNG generator
- ✅ Clusters jerárquicos idénticos
- ✅ Iconos AWS oficiales (mxgraph.aws4)
- ✅ Conexiones con estilos equivalentes

**Tipos soportados:**
- `network` - Arquitectura de red (VPC, subnets, AZ)
- `microservices` - Servicios y APIs
- `security` - Componentes de seguridad
- `data_flow` - Flujo de datos

### 🌐 2. Draw.io API Client

**Archivo:** `src/integrations/drawio_api_client.py`

**Función:** Integración completa con diagrams.net API

**Características:**
- ✅ Crear diagramas desde XML
- ✅ Subir a Draw.io (requiere API key)
- ✅ Compartir diagramas
- ✅ Exportar a PNG/SVG/PDF
- ✅ Validar XML

**Métodos principales:**
```python
# Crear URL de Draw.io
create_diagram_from_xml(xml_content, title)

# Subir diagrama (requiere API key)
upload_diagram(xml_content, filename)

# Compartir diagrama
share_diagram(diagram_id, permissions="view")

# Exportar a diferentes formatos
export_diagram(xml_content, format="png")
```

### 🔄 3. Model Converters

**Archivo:** `src/converters/model_to_drawio_converter.py`

**Función:** Convierte JSON/YAML/Dict a DrawIO XML

**Formatos soportados:**
- ✅ JSON → DrawIO
- ✅ YAML → DrawIO  
- ✅ Python Dict → DrawIO

**Estructura de modelo:**
```json
{
  "title": "Architecture Name",
  "canvas": {"width": 1600, "height": 900},
  "containers": [
    {
      "id": "vpc",
      "label": "VPC 10.0.0.0/16",
      "geometry": {"x": 100, "y": 100, "width": 1200, "height": 600},
      "components": [
        {
          "id": "api_gw",
          "type": "api_gateway",
          "label": "API Gateway",
          "position": {"x": 100, "y": 100}
        }
      ]
    }
  ],
  "connections": [
    {
      "from": "api_gw",
      "to": "fargate",
      "style": {"color": "#2196F3", "width": 2}
    }
  ]
}
```

## 🎨 Mapeo PNG → DrawIO

### Componentes Soportados

| PNG Component | DrawIO Shape | Descripción |
|---------------|--------------|-------------|
| `Fargate` | `mxgraph.aws4.fargate` | ECS Fargate |
| `RDS` | `mxgraph.aws4.rds` | Base de datos |
| `S3` | `mxgraph.aws4.s3` | Almacenamiento |
| `APIGateway` | `mxgraph.aws4.api_gateway` | API Gateway |
| `CloudFront` | `mxgraph.aws4.cloudfront` | CDN |
| `ELB` | `mxgraph.aws4.elastic_load_balancing` | Load Balancer |
| `Cognito` | `mxgraph.aws4.cognito` | Autenticación |
| `WAF` | `mxgraph.aws4.waf` | Firewall |
| `Users` | `mxgraph.aws4.users` | Usuarios |
| `Internet` | `mxgraph.aws4.internet_gateway` | Internet |

### Estilos de Conexión

| PNG Style | DrawIO Style | Color | Ancho |
|-----------|--------------|-------|-------|
| `primary` | Primary | `#232F3E` | 3px |
| `secondary` | Secondary | `#FF9900` | 2px |
| `data` | Data | `#2196F3` | 2px |
| `security` | Security | `#F44336` | 2px |
| `monitoring` | Monitoring | `#FF9800` | 2px |

## 🔧 Configuración

### Variables de Entorno

```bash
# Opcional: API key para Draw.io
export DRAWIO_API_KEY="your_api_key_here"

# Directorio de salida
export DRAWIO_OUTPUT_DIR="outputs/drawio/"
```

### Configuración en código

```python
# Configurar cliente API
client = DrawIOAPIClient(api_key="your_key")

# Configurar generador
generator = UniversalDrawIOGenerator(config, output_dir)
```

## 📚 Ejemplos Prácticos

### Ejemplo 1: Generar Network DrawIO

```python
# Usar misma config que PNG
config = {
    "microservices": {
        "certificate_service": {
            "business_function": "PDF generation"
        }
    }
}

generator = UniversalDrawIOGenerator(config, "outputs/")
drawio_path = generator.generate_from_png_input("network", "bmc_input")

print(f"DrawIO generado: {drawio_path}")
```

### Ejemplo 2: Crear URL de Draw.io

```python
from src.integrations.drawio_api_client import create_drawio_url

# Crear URL desde archivo local
url = create_drawio_url("outputs/diagram.drawio")
print(f"Abrir en: {url}")
```

### Ejemplo 3: Convertir JSON a DrawIO

```python
# Crear modelo
model = {
    "title": "BMC Architecture",
    "components": [
        {
            "id": "api",
            "type": "api_gateway", 
            "label": "API Gateway",
            "position": {"x": 100, "y": 100}
        },
        {
            "id": "app",
            "type": "fargate",
            "label": "App Service", 
            "position": {"x": 300, "y": 100}
        }
    ],
    "connections": [
        {"from": "api", "to": "app"}
    ]
}

# Convertir a DrawIO
converter = ModelToDrawIOConverter()
drawio_path = converter.convert_dict_to_drawio(model, "bmc_architecture")
```

## 🚀 Integración en Proyecto

### 1. Reemplazar generador actual

```python
# En mcp_generator.py
from .universal_drawio_generator import UniversalDrawIOGenerator

def generate_unified_diagrams(self, base_dir, project_name):
    # Usar generador universal
    generator = UniversalDrawIOGenerator(self.config, str(base_dir))
    
    # Generar todos los tipos
    results = {}
    for diagram_type in ["network", "microservices", "security", "data_flow"]:
        drawio_path = generator.generate_from_png_input(diagram_type, project_name)
        results[f"drawio_{diagram_type}"] = drawio_path
    
    return results
```

### 2. Agregar API integration

```python
# Opcional: subir a Draw.io
if api_key:
    client = DrawIOAPIClient(api_key)
    result = client.upload_diagram(xml_content, filename)
    if result["success"]:
        print(f"Diagrama subido: {result['edit_url']}")
```

## 🎯 Ventajas del Servicio

### vs PNG Generator
- ✅ **Misma entrada** - No cambios en configuración
- ✅ **Misma lógica** - Replica línea por línea
- ✅ **Resultado editable** - DrawIO vs PNG estático
- ✅ **Más compacto** - 12KB vs 225KB

### vs Manual DrawIO
- ✅ **Automatizado** - No creación manual
- ✅ **Consistente** - Siempre mismo resultado
- ✅ **Escalable** - Genera múltiples diagramas
- ✅ **Integrado** - Parte del pipeline MCP

### vs Otros Generadores
- ✅ **API Integration** - Sube a Draw.io automáticamente
- ✅ **Model Conversion** - JSON/YAML → DrawIO
- ✅ **Validation** - Verifica XML generado
- ✅ **Export Options** - PNG/SVG/PDF desde API

## 🔍 Troubleshooting

### Problema: XML inválido
```python
# Validar XML antes de usar
client = DrawIOAPIClient()
result = client.validate_xml(xml_content)
if not result["valid"]:
    print(f"Error: {result['error']}")
```

### Problema: API key no funciona
```python
# Verificar API key
client = DrawIOAPIClient(api_key)
result = client.upload_diagram(xml_content, "test")
if not result["success"]:
    print("API key inválida o expirada")
```

### Problema: Componente no mapeado
```python
# Agregar mapeo personalizado
generator.png_to_drawio_mapping["CustomComponent"] = "mxgraph.aws4.custom"
```

## 📞 Soporte

Para problemas o mejoras:
1. Verificar logs en `outputs/logs/`
2. Validar XML con `client.validate_xml()`
3. Probar con modelo simple
4. Revisar documentación de Draw.io API

---

**El Servicio DrawIO está listo para reemplazar completamente la generación PNG con diagramas editables equivalentes.**
