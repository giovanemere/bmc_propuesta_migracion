# 🔧 Frameworks para Generar DrawIO

## 🎯 Frameworks y Herramientas Disponibles

### 1. **drawio-batch** (Oficial)
```bash
# Herramienta oficial de Draw.io para batch processing
npm install -g @drawio/drawio-batch

# Uso
drawio-batch --input template.drawio --output result.drawio --replace "{{SERVICE}}" "Invoice Service"
```

**Pros:**
- ✅ Oficial de Draw.io
- ✅ Soporte para plantillas
- ✅ Reemplazo de variables

**Contras:**
- ❌ Requiere Node.js
- ❌ Limitado a reemplazo de texto

### 2. **drawio-export** (CLI)
```bash
# Exportar y manipular archivos DrawIO
npm install -g @drawio/drawio-export

# Generar desde plantilla
drawio-export --template aws_template.drawio --data config.json --output diagram.drawio
```

**Pros:**
- ✅ CLI potente
- ✅ Soporte JSON para datos
- ✅ Múltiples formatos de salida

**Contras:**
- ❌ Requiere Node.js
- ❌ Curva de aprendizaje

### 3. **mxgraph** (JavaScript Library)
```javascript
// Librería base de Draw.io
const mxGraph = require('mxgraph');

// Crear diagrama programáticamente
const graph = new mxGraph(container);
const parent = graph.getDefaultParent();

graph.getModel().beginUpdate();
try {
    const v1 = graph.insertVertex(parent, null, 'Invoice Service', 20, 20, 80, 30);
    const v2 = graph.insertVertex(parent, null, 'Database', 200, 150, 80, 30);
    const e1 = graph.insertEdge(parent, null, '', v1, v2);
} finally {
    graph.getModel().endUpdate();
}
```

**Pros:**
- ✅ Control total
- ✅ Librería oficial
- ✅ Muy potente

**Contras:**
- ❌ JavaScript/Node.js
- ❌ Complejo de usar
- ❌ Requiere conocimiento profundo

### 4. **drawio-python** (Wrapper Python)
```python
# Wrapper Python no oficial
from drawio import DrawIO

diagram = DrawIO()
diagram.add_shape('aws.fargate', 'Invoice Service', x=100, y=100)
diagram.add_shape('aws.rds', 'Database', x=300, y=200)
diagram.add_connection('Invoice Service', 'Database', 'SQL')
diagram.save('output.drawio')
```

**Pros:**
- ✅ Python nativo
- ✅ API simple
- ✅ Integración fácil

**Contras:**
- ❌ No oficial
- ❌ Limitado en funcionalidades
- ❌ Puede no estar actualizado

### 5. **PlantUML → DrawIO**
```python
# Generar PlantUML y convertir
plantuml_code = """
@startuml
!define AWSPuml https://raw.githubusercontent.com/awslabs/aws-icons-for-plantuml/v15.0/dist
!includeurl AWSPuml/AWSCommon.puml
!includeurl AWSPuml/Compute/all.puml
!includeurl AWSPuml/Database/all.puml

Fargate(invoice, "Invoice Service", "")
RDS(database, "PostgreSQL", "")
invoice --> database
@enduml
"""

# Convertir a DrawIO
convert_plantuml_to_drawio(plantuml_code, 'output.drawio')
```

**Pros:**
- ✅ Sintaxis simple
- ✅ Soporte AWS
- ✅ Herramientas de conversión disponibles

**Contras:**
- ❌ Paso adicional de conversión
- ❌ Menos control visual

### 6. **Mermaid → DrawIO**
```python
# Generar Mermaid y convertir
mermaid_code = """
graph TB
    A[Invoice Service<br/>2vCPU/4GB] --> B[RDS Database<br/>PostgreSQL 14]
    C[Product Service<br/>4vCPU/8GB] --> B
    D[OCR Service<br/>Textract] --> E[S3 Storage]
"""

# Convertir usando herramientas
convert_mermaid_to_drawio(mermaid_code, 'output.drawio')
```

**Pros:**
- ✅ Sintaxis muy simple
- ✅ Amplio soporte
- ✅ Herramientas de conversión

**Contras:**
- ❌ Limitado en shapes AWS específicos
- ❌ Menos control de layout

## 🎯 Recomendación: Enfoque Híbrido

### **Opción 1: drawio-batch + Plantillas**
```python
# Crear plantilla DrawIO con placeholders
template_content = """
<?xml version="1.0" encoding="UTF-8"?>
<mxfile>
  <diagram name="AWS Architecture">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="service1" value="{{SERVICE_1}}" style="shape=mxgraph.aws4.fargate" vertex="1" parent="1">
          <mxGeometry x="100" y="100" width="78" height="78" as="geometry"/>
        </mxCell>
        <mxCell id="service2" value="{{SERVICE_2}}" style="shape=mxgraph.aws4.rds" vertex="1" parent="1">
          <mxGeometry x="300" y="200" width="78" height="78" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""

# Usar drawio-batch para reemplazar
def generate_drawio_with_batch(services):
    # Guardar plantilla
    with open('template.drawio', 'w') as f:
        f.write(template_content)
    
    # Preparar reemplazos
    replacements = []
    for i, service in enumerate(services):
        replacements.extend([
            '--replace', f'{{{{SERVICE_{i+1}}}}}', service['name']
        ])
    
    # Ejecutar drawio-batch
    subprocess.run([
        'drawio-batch',
        '--input', 'template.drawio',
        '--output', 'result.drawio'
    ] + replacements)
```

### **Opción 2: mxgraph + Python Wrapper**
```python
# Crear wrapper Python para mxgraph
import subprocess
import json

class MXGraphGenerator:
    def __init__(self):
        self.components = []
        self.connections = []
    
    def add_aws_component(self, service_type, label, x, y):
        shape = f"mxgraph.aws4.{service_type}"
        self.components.append({
            'id': f'{service_type}_{len(self.components)}',
            'label': label,
            'shape': shape,
            'x': x, 'y': y
        })
    
    def add_connection(self, source_id, target_id, label):
        self.connections.append({
            'source': source_id,
            'target': target_id,
            'label': label
        })
    
    def generate(self, output_path):
        # Generar JavaScript para mxgraph
        js_code = self._build_mxgraph_js()
        
        # Ejecutar con Node.js
        with open('temp_generator.js', 'w') as f:
            f.write(js_code)
        
        subprocess.run(['node', 'temp_generator.js', output_path])
```

### **Opción 3: Plantillas + Manipulación XML**
```python
# Enfoque más simple: plantillas XML + manipulación
from xml.etree import ElementTree as ET

class TemplateDrawIOGenerator:
    def __init__(self, template_path):
        self.tree = ET.parse(template_path)
        self.root = self.tree.getroot()
    
    def replace_component(self, component_id, new_label):
        # Buscar componente por ID
        cell = self.root.find(f".//mxCell[@id='{component_id}']")
        if cell is not None:
            cell.set('value', new_label)
    
    def add_component(self, component_id, label, shape, x, y):
        # Crear nuevo componente
        model = self.root.find('.//mxGraphModel/root')
        cell = ET.SubElement(model, 'mxCell')
        cell.set('id', component_id)
        cell.set('value', label)
        cell.set('style', f'shape={shape};fillColor=#E8F5E8;strokeColor=#4CAF50')
        cell.set('vertex', '1')
        cell.set('parent', '1')
        
        geometry = ET.SubElement(cell, 'mxGeometry')
        geometry.set('x', str(x))
        geometry.set('y', str(y))
        geometry.set('width', '78')
        geometry.set('height', '78')
        geometry.set('as', 'geometry')
    
    def save(self, output_path):
        self.tree.write(output_path, encoding='utf-8', xml_declaration=True)
```

## 🚀 Implementación Recomendada

### **Framework Elegido: Plantillas XML + Python**

**Razones:**
1. ✅ **No requiere Node.js** - Solo Python
2. ✅ **Control total** - Manipulación directa XML
3. ✅ **Simple de implementar** - Pocas dependencias
4. ✅ **Fácil de mantener** - Código Python puro
5. ✅ **Plantillas reutilizables** - Una vez creadas, siempre funcionan

### **Arquitectura Propuesta:**
```
templates/
├── aws_network_template.drawio      # Plantilla red
├── aws_microservices_template.drawio # Plantilla microservicios
└── aws_security_template.drawio     # Plantilla seguridad

src/generators/
└── template_drawio_generator.py     # Generador basado en plantillas
```

### **Código de Ejemplo:**
```python
class TemplateDrawIOGenerator:
    def generate_from_template(self, template_name, config):
        # Cargar plantilla
        template_path = f"templates/{template_name}.drawio"
        generator = TemplateDrawIOGenerator(template_path)
        
        # Reemplazar componentes según config
        for service_name, service_config in config['microservices'].items():
            generator.replace_component(
                f'service_{service_name}',
                f"{service_name}\\n{service_config['cpu']}/{service_config['memory']}"
            )
        
        # Guardar resultado
        output_path = f"outputs/{template_name}_generated.drawio"
        generator.save(output_path)
        return output_path
```

## 📊 Comparación Final

| Framework | Complejidad | Dependencias | Control | Recomendado |
|-----------|-------------|--------------|---------|-------------|
| **drawio-batch** | Baja | Node.js | Medio | ⭐⭐⭐ |
| **mxgraph** | Alta | Node.js | Total | ⭐⭐ |
| **Plantillas XML** | Baja | Solo Python | Alto | ⭐⭐⭐⭐⭐ |
| **PlantUML** | Media | Java | Medio | ⭐⭐⭐ |
| **Mermaid** | Baja | Conversores | Bajo | ⭐⭐ |

## 🎯 Próximo Paso

**Implementar generador basado en plantillas XML:**
1. Crear plantillas DrawIO base
2. Implementar TemplateDrawIOGenerator
3. Integrar con workflow existente
4. Probar y validar resultados
