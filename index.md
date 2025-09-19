# BMC - Bolsa Comisionista | Sistema Regulatorio AWS

## 🏛️ Contexto del Negocio

**Entidad:** Bolsa Comisionista (Ente Regulador)  
**Función Principal:** Procesamiento de facturas y cálculo de comisiones regulatorias

### 📊 Características del Sistema

#### Volumen de Datos Masivo
- **60M productos** migrados desde Google Cloud a AWS
- **16,000 categorías** de productos clasificados
- **Procesamiento dual:** Facturas individuales y por lotes
- **Clasificación DIAN:** Alimentos (leche, carne, huevos) con cantidad/unidad

#### 🔄 Flujo de Negocio Regulatorio
1. **Carga de facturas** → Tabla de facturas (PostgreSQL)
2. **Análisis automático** → Matching con base de datos de productos
3. **Aplicación de reglas** → Cálculo de comisiones regulatorias
4. **Generación de certificado** → PDF descargable/envío por correo
5. **Integración SFTP** → Transmisión con otros sistemas regulatorios

## 🏗️ Arquitectura AWS para BMC

### Funcionalidades Backend
- **APIs REST/GraphQL** para procesamiento de facturas
- **Base de datos de productos** (60M registros en PostgreSQL)
- **Desagregación automática** por producto con OCR
- **Análisis inteligente** de facturas vs base de datos
- **Cálculos de comisión** (lote e individual)
- **Procesamiento en background** con colas SQS

### Funcionalidades Frontend
- **Formularios web** para carga de datos
- **Servicio de carga** de facturas (imágenes/PDF)
- **Sistema de archivos:** Individuales, ZIP, repeticiones permitidas
- **Opciones de exportación:** PDF y Excel
- **Dashboard regulatorio** con métricas en tiempo real

### Validaciones del Sistema Regulatorio

#### Primera Validación (Básica)
- ✅ Producto existe en base de datos
- ✅ Cantidad es válida y numérica
- ✅ Unidad corresponde al producto

#### Segunda Validación (Regulatoria)
- ✅ Producto tiene clasificación DIAN válida
- ✅ Clasificación corresponde a categoría regulatoria
- ✅ Unidad cumple normativas específicas

### Arquitectura de Datos

#### Transaccional (Operacional)
- **PostgreSQL Multi-AZ** - 60M productos, facturas, transacciones
- **ElastiCache Redis** - Cache de productos frecuentes (>95% hit ratio)
- **S3 Intelligent Tiering** - Documentos, imágenes, archivos ZIP

#### Analítica (Reportería Regulatoria)
- **Amazon Redshift** - Data warehouse para reportes DIAN
- **Amazon Textract** - OCR para procesamiento de facturas (>95% precisión)
- **Amazon Comprehend** - Clasificación automática de productos

#### Procesamiento Inteligente
- **Text processing** para clasificación automática
- **Búsqueda semántica** y matching de productos
- **Machine Learning** para mejorar precisión de matching
- **Campos vacíos** cuando no hay coincidencia (requiere revisión manual)

## 🔗 Integraciones Externas

### SFTP Integration Regulatoria
- **Transmisión automática** de archivos con otros sistemas regulatorios
- **Intercambio de datos** con DIAN y entidades supervisoras
- **Sincronización** de clasificaciones y normativas actualizadas
- **Backup y auditoría** de todas las transmisiones

### APIs Externas
- **DIAN API** - Validación de clasificaciones y normativas
- **Bancos Centrales** - Tipos de cambio y regulaciones financieras
- **Sistemas ERP** - Integración con sistemas contables existentes

## 🎯 Arquitectura AWS Implementada

### Microservicios en ECS Fargate
- **Invoice Service** (2vCPU/4GB) - Procesamiento de facturas, escala 2-10 instancias
- **Product Service** (4vCPU/8GB) - Gestión de 60M productos, escala 3-15 instancias  
- **OCR Service** (2vCPU/4GB) - Textract integration, >95% precisión
- **Commission Service** (1vCPU/2GB) - Cálculos regulatorios en tiempo real
- **Certificate Service** (1vCPU/2GB) - Generación de PDFs certificados DIAN

### Servicios de Datos
- **RDS PostgreSQL Multi-AZ** - 60M productos, transacciones, auditoría
- **ElastiCache Redis Cluster** - Cache de productos y sesiones
- **S3 + Lifecycle** - Documentos con retención regulatoria (7 años)
- **Redshift** - Analytics y reportería para entes reguladores

### Seguridad y Compliance
- **Cognito + MFA** - Autenticación de usuarios regulatorios
- **WAF + DDoS Protection** - Protección de APIs críticas
- **KMS Encryption** - Cifrado de datos sensibles regulatorios
- **CloudTrail** - Auditoría completa para compliance

### Monitoreo Regulatorio
- **CloudWatch Custom Metrics** - KPIs específicos de regulación
- **Alarms** - Alertas por incumplimiento de SLAs regulatorios
- **Dashboards** - Métricas en tiempo real para supervisores

## 📊 Métricas de Rendimiento Regulatorio

### Performance Targets
- **Procesamiento:** 10,000 facturas/hora sostenido
- **Respuesta API:** <500ms (p95) para consultas de productos
- **OCR Accuracy:** >95% en facturas estándar
- **Disponibilidad:** >99.9% (SLA regulatorio)
- **Matching Products:** <300ms con cache, <2s sin cache

### Business Metrics
- **Costo por factura:** $0.0009 USD
- **Precisión regulatoria:** >99.8% en clasificaciones DIAN
- **Tiempo de certificación:** <3 segundos por documento
- **Capacidad pico:** 30,000 facturas/hora (3x normal)

## 🚀 Generación de Diagramas MCP

### Comandos Disponibles
```bash
# Arquitectura BMC completa
./run.sh --case bmc

# Diagramas profesionales refinados  
./run.sh --case refined

# Patrones AWS genéricos
./run.sh --case generic

# Desde archivo MCP personalizado
./run.sh --file docs/mcp-diagrams-architecture.md --name BMC
```

### Diagramas Generados
- **Arquitectura Principal** - Vista completa del sistema regulatorio
- **Microservicios Detallados** - ECS Fargate con auto-scaling
- **Arquitectura de Red** - VPC Multi-AZ con subnets privadas
- **Seguridad y Compliance** - Capas de protección regulatoria
- **Flujo de Datos** - Pipeline completo de procesamiento

### Formatos de Salida
- **PNG** - Para presentaciones a entes reguladores
- **Draw.io** - Para colaboración técnica (editable en app.diagrams.net)
- **Documentación** - MCP como fuente de verdad técnica

## 🎯 Evolución del Sistema

### Implementado (v2.0.0)
- ✅ Migración completa de 60M productos a AWS
- ✅ OCR con >95% precisión usando Textract
- ✅ Procesamiento de 10K facturas/hora
- ✅ Integración SFTP con sistemas regulatorios
- ✅ Generación automática de certificados DIAN

### Roadmap Regulatorio
- 🔄 **v2.1** - Integración con blockchain para trazabilidad
- 🔄 **v2.2** - ML avanzado para detección de anomalías
- 🔄 **v2.3** - API real-time para consultas regulatorias
- 🔄 **v3.0** - Expansión a otros países latinoamericanos

---

**BMC - Transformando la regulación financiera con AWS Cloud** 🏛️☁️
