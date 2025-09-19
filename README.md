# BMC Propuesta de Migración a AWS

Metodología MCP (Model Context Protocol) para la migración del sistema BMC (Bolsa Comisionista) desde Google Cloud a AWS.

## Descripción del Sistema

BMC es un sistema regulatorio que procesa:
- 60M de productos con clasificación DIAN
- Facturas individuales y por lotes
- Cálculo de comisiones por reglas de negocio
- Generación de certificados PDF
- Integración SFTP con sistemas externos

## Metodología MCP

### Fase 1: Precaracterización
```bash
python3 mcp-precaracterizacion.py proposal   # Propuesta inicial
python3 mcp-precaracterizacion.py inventory  # Inventario de aplicaciones  
python3 mcp-precaracterizacion.py baseline   # Baseline técnico
```

### Fase 2: Estructuración
```bash
python3 mcp-estructuracion.py architecture   # Patrones arquitectónicos
python3 mcp-estructuracion.py data          # Arquitectura de datos
python3 mcp-estructuracion.py flows         # Flujos de integración
```

### Fase 3: Catálogo de Aplicaciones
```bash
python3 mcp-catalogo.py catalog       # Catálogo completo
python3 mcp-catalogo.py dependencies  # Matriz de dependencias
python3 mcp-catalogo.py migration     # Plan de migración
```

### Fase 4: Lineamientos
```bash
python3 mcp-lineamientos.py standards    # Estándares de desarrollo
python3 mcp-lineamientos.py security     # Guías de seguridad
python3 mcp-lineamientos.py deployment   # Procedimientos de despliegue
python3 mcp-lineamientos.py monitoring   # Métricas y monitoreo
```

## Arquitectura Objetivo

- **Patrón:** Event-Driven Microservices
- **Compute:** AWS Lambda + ECS Fargate
- **Database:** RDS PostgreSQL + Redshift + ElastiCache
- **Integration:** API Gateway + EventBridge + Transfer Family
- **Frontend:** React SPA + CloudFront

## Servicios Principales

1. **Invoice Service** - Procesamiento de facturas
2. **Product Service** - Gestión de 60M productos
3. **Commission Service** - Cálculo de comisiones
4. **Certificate Service** - Generación de certificados

## Versión

Todos los MCPs están en versión 1.0.0
