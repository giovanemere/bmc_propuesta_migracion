# BMC Input Specification

## Sistema BMC - Bolsa Comisionista

### Información General
- **Nombre:** BMC Bolsa Comisionista
- **Tipo:** Sistema Regulatorio
- **Entidad:** Ente Regulador
- **Función Principal:** Procesamiento de facturas y cálculo de comisiones

### Capacidades del Sistema
- **Productos:** 60M registros migrados desde Google Cloud
- **Categorías:** 16,000 tipos de productos
- **Throughput:** 10,000 facturas/hora
- **Procesamiento:** Individual y por lotes

### Servicios Principales

#### Invoice Service
- Procesamiento de facturas individuales y por lotes
- Carga de facturas → Tabla de facturas
- Botón calcular → Aplicación de reglas de negocio
- Generación de certificado → PDF descargable o envío por correo

#### Product Service  
- Gestión de 60M productos migrados desde Google Cloud
- Base de datos de productos con clasificación DIAN
- Análisis y matching de facturas con base de datos
- API para entregar listados al frontend

#### OCR Service
- Servicio de carga de facturas en imagen o PDF
- Análisis de factura con base de datos de productos
- Matching con precisión > 95%

#### Commission Service
- Cálculos de comisión regulatoria (lote e individual)
- Compliance DIAN Colombia
- Auditabilidad completa

#### Certificate Service
- Generación de certificados PDF DIAN compliance
- Envío por correo electrónico
- Almacenamiento seguro

### Integraciones
- **SFTP:** Transmisión de archivos con otros sistemas
- **Email:** Envío de certificados
- **APIs:** Intercambio de datos regulatorios

### Compliance Regulatorio
- Cumplimiento DIAN Colombia
- Retención de datos 7 años mínimo
- Audit trail completo
- Clasificación de productos regulatoria
