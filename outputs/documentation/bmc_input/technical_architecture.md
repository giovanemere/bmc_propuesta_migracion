# Arquitectura Técnica - BMC

## Resumen Ejecutivo
Sistema regulatorio para procesamiento de facturas y cálculo de comisiones DIAN.

**Capacidad:** 60M productos, 10,000 facturas/hora
**Compliance:** DIAN Colombia
**Patrón:** Microservicios en AWS

## Arquitectura de Microservicios

### Servicios Core

#### Invoice Service

**Función:** Procesamiento de facturas individuales y por lotes

**Recursos:**
- CPU: N/A vCPU
- Memoria: N/A MB
- Escalamiento: 1-5 instancias

**Tecnologías:**
- Runtime: ECS Fargate
- Base de datos: RDS PostgreSQL
- Cache: ElastiCache Redis

#### Product Service

**Función:** Gestión de 60M productos migrados desde Google Cloud

**Recursos:**
- CPU: N/A vCPU
- Memoria: N/A MB
- Escalamiento: 1-5 instancias

**Tecnologías:**
- Runtime: ECS Fargate
- Base de datos: RDS PostgreSQL
- Cache: ElastiCache Redis

#### Ocr Service

**Función:** Servicio de carga de facturas en imagen o PDF

**Recursos:**
- CPU: N/A vCPU
- Memoria: N/A MB
- Escalamiento: 1-5 instancias

**Tecnologías:**
- Runtime: ECS Fargate
- Base de datos: RDS PostgreSQL
- Cache: ElastiCache Redis

#### Commission Service

**Función:** Cálculos de comisión regulatoria (lote e individual)

**Recursos:**
- CPU: N/A vCPU
- Memoria: N/A MB
- Escalamiento: 1-5 instancias

**Tecnologías:**
- Runtime: ECS Fargate
- Base de datos: RDS PostgreSQL
- Cache: ElastiCache Redis

#### Certificate Service

**Función:** Generación de certificados PDF DIAN compliance

**Recursos:**
- CPU: N/A vCPU
- Memoria: N/A MB
- Escalamiento: 1-5 instancias

**Tecnologías:**
- Runtime: ECS Fargate
- Base de datos: RDS PostgreSQL
- Cache: ElastiCache Redis

## Infraestructura AWS

### Servicios Principales

#### Rds
- **Tipo:** N/A
- **Propósito:** N/A
- **Configuración:** Multi-AZ, alta disponibilidad

#### S3
- **Tipo:** N/A
- **Propósito:** N/A
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

Generado: 2025-09-19 23:47:23
