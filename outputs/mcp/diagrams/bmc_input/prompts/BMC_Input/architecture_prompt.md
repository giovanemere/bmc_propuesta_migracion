# Prompt de Arquitectura MCP - BMC Bolsa Comisionista

## Contexto del Sistema
**Proyecto:** BMC Bolsa Comisionista
**Tipo:** Sistema Regulatorio
**Función:** Procesamiento de facturas

## Microservicios Identificados

### Invoice Service
- **Función de negocio:** Procesamiento de facturas individuales y por lotes
- **CPU:** 2048 
- **Memoria:** 4096MB
- **Escalamiento:** 2-10 instancias

### Product Service
- **Función de negocio:** Gestión de 60M productos migrados desde Google Cloud
- **CPU:** 4096 
- **Memoria:** 8192MB
- **Escalamiento:** 3-15 instancias

### Ocr Service
- **Función de negocio:** Análisis de facturas y matching con base de datos
- **CPU:** 2048 
- **Memoria:** 4096MB
- **Escalamiento:** 1-5 instancias

### Commission Service
- **Función de negocio:** Cálculos de comisión regulatoria (lote e individual)
- **CPU:** 1024 
- **Memoria:** 2048MB
- **Escalamiento:** 1-5 instancias

### Certificate Service
- **Función de negocio:** Generación de certificados PDF DIAN compliance
- **CPU:** 1024 
- **Memoria:** 2048MB
- **Escalamiento:** 1-5 instancias

## Servicios AWS Requeridos

### Rds Primary
- **Tipo:** rds
- **Propósito:** Base de datos transaccional - 60M productos

### Redshift Analytics
- **Tipo:** redshift
- **Propósito:** Data warehouse para reportería regulatoria

### Redis Cache
- **Tipo:** elasticache
- **Propósito:** Cache de productos frecuentes y sesiones

### S3 Documents
- **Tipo:** s3
- **Propósito:** Almacenamiento de facturas PDF/imágenes

## Prompt para Arquitecto

Basado en esta información, diseña una arquitectura AWS que:

1. **Cumpla con regulaciones DIAN** para el procesamiento de facturas
2. **Soporte 60M productos** con alta disponibilidad
3. **Procese 10,000 facturas/hora** con escalamiento automático
4. **Integre OCR** para procesamiento de imágenes/PDFs
5. **Mantenga compliance** regulatorio y auditabilidad

### Consideraciones Técnicas
- Usar patrones de microservicios
- Implementar cache distribuido
- Configurar monitoreo y alertas
- Diseñar para multi-AZ
- Incluir backup y disaster recovery

Generado: 2025-09-19 20:43:13
