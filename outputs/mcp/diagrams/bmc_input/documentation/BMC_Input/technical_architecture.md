# Arquitectura Técnica - BMC Bolsa Comisionista

## Resumen Ejecutivo
Sistema regulatorio para procesamiento de facturas y cálculo de comisiones DIAN.

**Capacidad:** 60M productos, 10,000 facturas/hora
**Compliance:** DIAN Colombia
**Patrón:** Microservicios en AWS

## Arquitectura de Microservicios

### Servicios Core

#### Certificate Service

**Función:** Generación de certificados PDF DIAN compliance

**Recursos:**
- CPU: 1024 vCPU
- Memoria: 2048 MB
- Escalamiento: 1-5 instancias

**Tecnologías:**
- Runtime: ECS Fargate
- Base de datos: RDS PostgreSQL
- Cache: ElastiCache Redis

## Infraestructura AWS

### Servicios Principales

#### Redis Cache
- **Tipo:** ELASTICACHE
- **Propósito:** Cache de productos frecuentes y sesiones
- **Configuración:** Multi-AZ, alta disponibilidad

#### S3 Documents
- **Tipo:** S3
- **Propósito:** Almacenamiento de facturas PDF/imágenes
- **Configuración:** Multi-AZ, alta disponibilidad

## Patrones de Diseño

### Microservicios
- **API Gateway** como punto de entrada único
- **Service mesh** para comunicación inter-servicios
- **Circuit breaker** para resiliencia
- **Event sourcing** para auditabilidad

### Datos
- **CQRS** para separar lectura/escritura
- **Database per service** para independencia
- **Event-driven architecture** para consistencia eventual

### Seguridad
- **OAuth 2.0 + JWT** para autenticación
- **RBAC** para autorización
- **Encryption at rest** AES-256
- **TLS 1.3** para datos en tránsito

Generado: 2025-09-19 22:25:09
