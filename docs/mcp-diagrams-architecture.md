# MCP Diagramas de Arquitectura BMC

## Contexto del Sistema

### Información General
- **Proyecto**: BMC (Bolsa Mercantil de Colombia) - Migración AWS
- **Objetivo**: Generar diagramas de arquitectura automatizados desde MCP
- **Tecnologías**: Python Diagrams, Draw.io, Mermaid, Terraform
- **Capacidad**: 60M productos, OCR >95%, 10K facturas/hora

### Arquitectura de Diagramas
```yaml
Formatos Soportados:
  - PNG: Presentaciones ejecutivas (Python Diagrams)
  - Draw.io: Edición colaborativa (XML válido)
  - Mermaid: Documentación como código (Markdown)

Servicios AWS Representados:
  - Compute: ECS Fargate, Lambda, Step Functions
  - Storage: RDS PostgreSQL, S3, ElastiCache Redis
  - Network: API Gateway, CloudFront, ALB
  - Security: Cognito, WAF, KMS
  - AI/ML: Textract, Comprehend
  - Integration: EventBridge, SQS, SNS
  - Monitoring: CloudWatch, X-Ray
```

## Estructura del Repositorio

### Directorio Principal
```
/home/giovanemere/Migracion/
├── mcp-diagrams-architecture.md     # Este archivo MCP
├── infrastructure/
│   ├── diagrams/                    # Generadores de diagramas
│   │   ├── generate_final_version.sh   # Script principal
│   │   ├── generate_complete.py        # Generador Python
│   │   └── requirements.txt            # Dependencias
│   └── terraform/                   # IaC (futuro)
├── docs/                           # Documentación
│   ├── diagramas-aws-mermaid.md    # Diagramas Mermaid
│   ├── flujos-proceso-mermaid.md   # Flujos de proceso
│   └── README-DIAGRAMAS-BMC.md     # Guía de uso
└── output/                         # Archivos generados
    ├── png/                        # Diagramas PNG
    └── drawio/                     # Archivos Draw.io
```

### Archivos Activos (En Uso)
```yaml
Core Files:
  - infrastructure/diagrams/generate_final_version.sh  # Script principal
  - infrastructure/diagrams/generate_complete.py       # Generador Python
  - infrastructure/diagrams/requirements.txt           # Dependencias
  - diagramas-aws-mermaid.md                          # Fuente Mermaid
  - mcp-arquitectura-bmc.md                           # MCP principal

Documentation:
  - README-DIAGRAMAS-BMC.md                           # Guía de uso
  - PROPUESTA-ARQUITECTURA-BMC.md                     # Propuesta técnica
  - flujos-proceso-mermaid.md                         # Flujos detallados
```

### Archivos Obsoletos (Para Limpieza)
```yaml
Deprecated Files:
  - bmc_architecture.py                    # Versión antigua
  - bmc_drawio_generator.py               # Generador obsoleto
  - bmc_final_professional.py             # Versión intermedia
  - mermaid_converter_fixed.py            # Convertidor obsoleto
  - generate_enhanced.sh                  # Script anterior
  - bmc_*.py (múltiples versiones)        # Iteraciones previas

Unused MCP Files:
  - mcp-catalogo.py                       # No utilizado
  - mcp-estructuracion.py                 # No utilizado
  - mcp-lineamientos.py                   # No utilizado
  - mcp-precaracterizacion.py            # No utilizado
  - mcp-server.py                         # No utilizado
  - mcp-workflow.py                       # No utilizado
```

## Servicios AWS Utilizados

### Servicios Implementados en Diagramas
```yaml
Compute Services:
  - ECS Fargate: Microservicios (Invoice, Product, OCR, Commission, Certificate)
  - Lambda: Procesamiento OCR, validaciones, generación PDF
  - Step Functions: Orquestación de workflows (futuro)

Storage Services:
  - RDS PostgreSQL: Base de datos principal (60M productos)
  - ElastiCache Redis: Cache de productos (24h TTL)
  - S3: Almacenamiento de documentos (Intelligent Tiering)
  - Redshift: Data warehouse para analytics (futuro)

Network Services:
  - API Gateway: Punto de entrada REST/GraphQL
  - CloudFront: CDN global
  - Application Load Balancer: Balanceador de microservicios
  - VPC: Red privada virtual

Security Services:
  - Cognito: Autenticación de usuarios
  - WAF: Web Application Firewall
  - KMS: Gestión de claves de cifrado
  - Secrets Manager: Gestión de secretos

AI/ML Services:
  - Textract: OCR con >95% precisión
  - Comprehend: Análisis de texto (futuro)

Integration Services:
  - EventBridge: Bus de eventos
  - SQS: Colas de mensajes (FIFO y Standard)
  - SNS: Notificaciones multi-canal
  - Transfer Family: Gateway SFTP

Monitoring Services:
  - CloudWatch: Métricas, logs, alarmas
  - X-Ray: Trazabilidad distribuida
  - CloudTrail: Auditoría de API calls
```

### Servicios No Utilizados (Para Futuras Versiones)
```yaml
Potential Services:
  - Step Functions: Orquestación compleja de workflows
  - Kinesis: Streaming de datos en tiempo real
  - Glue: ETL para data warehouse
  - QuickSight: Business Intelligence
  - Redshift: Analytics (planificado)
  - Comprehend: NLP avanzado
  - Rekognition: Análisis de imágenes
  - SageMaker: Machine Learning personalizado
```

## Comandos de Generación

### Comando Principal
```bash
cd /home/giovanemere/Migracion/infrastructure/diagrams
./generate_final_version.sh
```

### Archivos Generados
```yaml
PNG Files:
  - bmc_complete_architecture.png      # Arquitectura completa
  - bmc_microservices_complete.png     # Detalle microservicios

Draw.io Files:
  - bmc_complete_architecture.drawio   # Editable en draw.io

Características:
  - Iconos oficiales AWS
  - Información técnica (vCPU, memoria, escalado)
  - Métricas de rendimiento
  - Conexiones etiquetadas
  - Grupos organizados por función
```

## Configuración de Servicios

### Microservicios ECS Fargate
```yaml
invoice_service:
  cpu: 2048
  memory: 4096
  port: 8000
  min_capacity: 2
  max_capacity: 10
  health_check: "/health"

product_service:
  cpu: 4096
  memory: 8192
  port: 8001
  min_capacity: 3
  max_capacity: 15
  records: 60000000
  cache_ttl: "24h"

ocr_service:
  cpu: 2048
  memory: 4096
  port: 8002
  min_capacity: 2
  max_capacity: 8
  accuracy: ">95%"

commission_service:
  cpu: 1024
  memory: 2048
  port: 8003
  min_capacity: 2
  max_capacity: 6

certificate_service:
  cpu: 1024
  memory: 2048
  port: 8004
  min_capacity: 2
  max_capacity: 5
```

### Base de Datos
```yaml
rds_postgresql:
  instance_class: "db.r6g.2xlarge"
  allocated_storage: 1000
  max_allocated_storage: 5000
  multi_az: true
  backup_retention: 35
  performance_insights: true
  records: 60000000

elasticache_redis:
  node_type: "cache.r6g.xlarge"
  num_nodes: 3
  cluster_mode: true
  ttl: "24h"
```

## Métricas y KPIs

### Performance Targets
```yaml
Response Times:
  - OCR Processing: <5 segundos
  - Product Lookup: <500ms (60M records)
  - Invoice Processing: <3 segundos
  - API Response: <1 segundo (p95)

Throughput:
  - Invoice Processing: 10,000/hour
  - Product Queries: 1,000/second
  - OCR Accuracy: >95%

Availability:
  - System SLA: >99.9%
  - Database RTO: 4 hours
  - Database RPO: 1 hour

Costs:
  - Monthly Estimate: $8,650
  - Cost per Invoice: $0.0009
  - Cost per Product Query: $0.000001
```

## Proceso de Actualización

### Para Actualizar Diagramas
```bash
# 1. Modificar configuración en este MCP
# 2. Actualizar generate_complete.py si es necesario
# 3. Ejecutar generación
cd /home/giovanemere/Migracion/infrastructure/diagrams
./generate_final_version.sh

# 4. Verificar archivos generados
ls -la bmc_*.png bmc_*.drawio

# 5. Commit y push
git add .
git commit -m "Update architecture diagrams"
git push origin main
```

### Para Agregar Nuevos Servicios
```python
# En generate_complete.py, agregar:
new_service = NewAWSService("Service Name\nDescription")

# En el cluster correspondiente:
with Cluster("Service Group"):
    new_service = NewAWSService("Service Name")

# Agregar conexiones:
existing_service >> new_service
```

## Integración con Terraform

### Futura Integración
```yaml
Terraform Integration:
  - Generar diagramas desde terraform.tfstate
  - Sincronizar configuración con IaC
  - Validar arquitectura vs implementación
  - Auto-update en cambios de infraestructura

Files to Create:
  - infrastructure/terraform/main.tf
  - infrastructure/terraform/variables.tf
  - infrastructure/terraform/outputs.tf
  - scripts/sync-terraform-diagrams.py
```

## Versionado

### Versión Actual
- **v2.0.0**: Diagramas automatizados con MCP
- **Última actualización**: 2024-09-19
- **Próxima versión**: v2.1.0 (Integración Terraform)

### Changelog
```yaml
v2.0.0:
  - MCP para diagramas de arquitectura
  - Generación automatizada PNG + Draw.io
  - Limpieza de archivos obsoletos
  - Estructura de repositorio organizada

v1.0.0:
  - Diagramas Mermaid básicos
  - Propuesta de arquitectura inicial
  - Documentación técnica
```
