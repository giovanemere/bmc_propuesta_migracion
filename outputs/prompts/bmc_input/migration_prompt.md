# Prompt de Migración MCP

## Estrategia de Migración

### Patrón Recomendado: Strangler Fig
Migración gradual reemplazando componentes del sistema legacy.

### Fases de Migración

#### Fase 1: Precaracterización
- Análisis del sistema actual
- Identificación de dependencias
- Mapeo de datos (60M productos)

#### Fase 2: Estructuración  
- Diseño de microservicios
- Arquitectura de datos (PostgreSQL + Redshift)
- Definición de APIs

#### Fase 3: Catálogo
- Mapeo de aplicaciones
- Priorización de componentes
- Plan de implementación

#### Fase 4: Lineamientos
- Estándares de implementación
- Compliance regulatorio DIAN
- Métricas de rendimiento

## Prompt para Especialista en Migración

Desarrolla un plan detallado que:

1. **Minimice el downtime** durante la migración
2. **Preserve la integridad** de 60M registros de productos
3. **Mantenga compliance** DIAN durante todo el proceso
4. **Implemente rollback** en caso de problemas
5. **Valide la migración** con pruebas exhaustivas

### Riesgos Identificados
- Pérdida de datos durante migración
- Interrupción del servicio regulatorio
- Incompatibilidad con sistemas SFTP existentes
- Degradación de performance con 60M registros

### Mitigaciones Propuestas
- Migración por lotes con validación
- Ambiente de staging idéntico a producción
- Pruebas de carga con datos reales
- Plan de rollback automatizado

Generado: 2025-09-19 23:45:55
