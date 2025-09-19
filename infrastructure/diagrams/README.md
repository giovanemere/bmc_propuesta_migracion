# BMC AWS Architecture Diagrams Generator

Este directorio contiene scripts para generar diagramas de arquitectura AWS con iconos oficiales usando la librería `diagrams` de Python.

## 🎯 Diagramas Generados

### Arquitectura Principal
- **`bmc_main_architecture.png`** - Arquitectura completa de BMC en AWS
- **`bmc_microservices_detail.png`** - Detalle de microservicios en ECS Fargate
- **`bmc_data_architecture.png`** - Arquitectura de datos multi-tier
- **`bmc_security_architecture.png`** - Seguridad y compliance
- **`bmc_monitoring_architecture.png`** - Monitoreo y observabilidad

### Flujos de Proceso
- **`bmc_invoice_processing_flow.png`** - Flujo de procesamiento de facturas
- **`bmc_product_lookup_flow.png`** - Búsqueda en 60M productos
- **`bmc_ocr_processing_flow.png`** - Procesamiento OCR con >95% precisión
- **`bmc_error_handling_flow.png`** - Manejo de errores y recuperación
- **`bmc_monitoring_flow.png`** - Flujo de monitoreo y alertas

## 🚀 Generación Rápida

### Opción 1: Script Automático
```bash
./generate_all.sh
```

### Opción 2: Manual
```bash
# Instalar dependencias del sistema
sudo apt-get install graphviz  # Ubuntu/Debian
# o
brew install graphviz          # macOS

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias Python
pip install -r requirements.txt

# Generar diagramas de arquitectura
python3 bmc_architecture.py

# Generar diagramas de flujos
python3 bmc_process_flows.py
```

## 📋 Requisitos

### Sistema
- Python 3.7+
- Graphviz
- pip3

### Python Packages
- diagrams==0.23.4
- graphviz==0.20.1
- Pillow==10.0.1

## 🏗️ Arquitectura Representada

### Servicios AWS Incluidos
- **Compute**: ECS Fargate, Lambda, Step Functions
- **Storage**: RDS PostgreSQL, Redshift, S3, ElastiCache Redis
- **AI/ML**: Amazon Textract, Amazon Comprehend
- **Integration**: API Gateway, EventBridge, SQS, SNS
- **Security**: Cognito, IAM, KMS, WAF, Secrets Manager
- **Monitoring**: CloudWatch, X-Ray, CloudTrail

### Características Técnicas
- **60 millones de productos** en PostgreSQL
- **OCR con >95% precisión** usando Textract
- **Procesamiento de 10,000 facturas/hora**
- **Disponibilidad >99.9%** con Multi-AZ
- **Event-driven architecture** con EventBridge
- **Auto-scaling** basado en métricas

## 📊 Métricas Visualizadas

### Performance KPIs
- OCR Processing: <5s (imágenes), <3s (PDFs)
- Product Lookup: <500ms (60M records)
- Invoice Processing: <3s individual
- System Availability: >99.9%

### Business KPIs
- OCR Accuracy: >95%
- Processing Throughput: 10,000 invoices/hour
- Compliance Rate: 100% DIAN validation

## 🔧 Personalización

### Modificar Diagramas
1. Editar `bmc_architecture.py` para arquitectura principal
2. Editar `bmc_process_flows.py` para flujos de proceso
3. Ejecutar el script correspondiente
4. Los PNG se generan automáticamente

### Agregar Nuevos Diagramas
```python
def generate_new_diagram():
    with Diagram("New Diagram Title", 
                 filename="new_diagram", 
                 show=False, 
                 direction="TB"):
        # Agregar componentes AWS
        service = AWSService("Service Name")
        # Definir conexiones
        service >> other_service
```

## 📤 Uso de los Diagramas

### Documentación
- Incluir en documentación técnica
- Presentaciones de arquitectura
- Propuestas de migración
- Revisiones de diseño

### Formatos Soportados
- PNG (por defecto)
- SVG (vectorial)
- PDF (documentos)
- DOT (Graphviz)

### Cambiar Formato
```python
with Diagram("Title", filename="diagram", format="svg"):
    # Contenido del diagrama
```

## 🎨 Iconos AWS

Los diagramas utilizan iconos oficiales de AWS proporcionados por la librería `diagrams`:
- Iconos actualizados y oficiales
- Colores corporativos de AWS
- Escalado automático
- Compatibilidad con todos los servicios

## 📝 Notas Técnicas

### Rendimiento
- Generación rápida (<30 segundos todos los diagramas)
- Archivos PNG optimizados
- Resolución alta para presentaciones

### Compatibilidad
- Linux, macOS, Windows
- Python 3.7+
- Graphviz 2.40+

### Troubleshooting
- Si falla Graphviz: instalar manualmente
- Si falla Python: verificar versión 3.7+
- Si falla pip: usar `python3 -m pip install`

## 🔄 Actualización

Para actualizar los diagramas:
1. Modificar los scripts Python
2. Ejecutar `./generate_all.sh`
3. Verificar los PNG generados
4. Commit y push al repositorio

## 📞 Soporte

Para problemas con la generación de diagramas:
1. Verificar requisitos del sistema
2. Revisar logs de error
3. Consultar documentación de `diagrams`
4. Crear issue en el repositorio
