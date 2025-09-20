# Prompt de Implementación MCP

## Especificaciones Técnicas

### Performance KPIs
- **Throughput:** 10000 facturas/hora
- **Base de datos:** 60M productos
- **Categorías:** 16000 tipos

### Tiempos de Respuesta Objetivo
- **Lookup de productos:** < 300ms
- **Procesamiento de facturas:** < 3000ms  
- **Generación de certificados:** < 2000ms

### Precisión Requerida
- **OCR:** > 95% precisión
- **Matching de productos:** > 99% precisión
- **Compliance regulatorio:** > 99.8% precisión

## Prompt para Desarrollador

Implementa el sistema con estas especificaciones:

### 1. Servicios Core
```
invoice_service:
  - Procesamiento de facturas individuales y por lotes
  - Integración con OCR (Textract)
  - Validación DIAN

product_service:
  - Gestión de 60M productos
  - Cache distribuido (Redis)
  - API de búsqueda optimizada

ocr_service:
  - Análisis de facturas PDF/imagen
  - Matching con base de datos
  - Precisión > 95%

commission_service:
  - Cálculos regulatorios
  - Compliance DIAN
  - Auditabilidad completa

certificate_service:
  - Generación PDF
  - Envío por email
  - Almacenamiento seguro
```

### 2. Infraestructura AWS
- **ECS Fargate** para microservicios
- **RDS PostgreSQL Multi-AZ** para datos transaccionales
- **Redshift** para analytics
- **S3** para documentos
- **ElastiCache Redis** para cache
- **Textract** para OCR

### 3. Monitoreo y Alertas
- CloudWatch métricas custom
- Alertas por SLA breach
- Dashboard de compliance
- Logs centralizados

### 4. Seguridad
- Encriptación AES-256 en reposo
- TLS 1.3 en tránsito
- RBAC con MFA
- Audit trail completo

Generado: 2025-09-19 22:11:02
