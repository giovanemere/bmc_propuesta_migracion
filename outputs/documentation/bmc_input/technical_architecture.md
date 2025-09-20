# Arquitectura Técnica - BMC Bolsa Comisionista

## Resumen Ejecutivo
Sistema regulatorio para procesamiento de facturas y cálculo de comisiones DIAN.

**Capacidad:** 60M productos, 10,000 facturas/hora
**Compliance:** DIAN Colombia
**Patrón:** Microservicios en AWS

## Arquitectura de Microservicios

### Servicios Core

## Infraestructura AWS

### Servicios Principales

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

Generado: 2025-09-19 23:10:58
