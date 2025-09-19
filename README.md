# BMC AWS Architecture - Diagram Generator

Generador automatizado de diagramas de arquitectura AWS para el proyecto BMC (Bolsa Mercantil de Colombia).

## 🚀 Generación Rápida

```bash
# Generar todos los diagramas
./scripts/generate_diagrams.sh
```

## 📁 Estructura del Proyecto

```
├── docs/                           # Documentación
│   ├── mcp-diagrams-architecture.md   # MCP principal
│   ├── diagramas-aws-mermaid.md       # Diagramas Mermaid
│   └── README-DIAGRAMAS-BMC.md        # Guía de uso
├── infrastructure/
│   ├── diagrams/                   # Generadores Python
│   │   ├── generate_complete.py       # Generador principal
│   │   ├── generate_final_version.sh  # Script de generación
│   │   └── requirements.txt           # Dependencias
│   └── terraform/                  # Infrastructure as Code (futuro)
├── output/
│   ├── png/                        # Diagramas PNG generados
│   └── drawio/                     # Archivos Draw.io generados
├── scripts/
│   └── generate_diagrams.sh           # Script principal
└── archive/                        # Archivos obsoletos

```

## 🎯 Características

- **60M productos** en base de datos PostgreSQL
- **OCR >95% precisión** con Amazon Textract
- **10K facturas/hora** de throughput
- **99.9% disponibilidad** con Multi-AZ
- **Auto-scaling** 2-15 instancias por servicio

## 📊 Diagramas Generados

### PNG (para presentaciones)
- `bmc_complete_architecture.png` - Arquitectura completa
- `bmc_microservices_complete.png` - Detalle microservicios

### Draw.io (para edición)
- `bmc_complete_architecture.drawio` - Editable en https://app.diagrams.net

## 🔧 Desarrollo

### Requisitos
- Python 3.9+
- Graphviz
- Virtual environment

### Instalación
```bash
cd infrastructure/diagrams
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Generar Diagramas
```bash
# Método 1: Script principal
./scripts/generate_diagrams.sh

# Método 2: Manual
cd infrastructure/diagrams
source venv/bin/activate
python3 generate_complete.py
```

## 📋 MCP (Model Context Protocol)

El proyecto utiliza MCP para definir la arquitectura:
- **Archivo principal**: `docs/mcp-diagrams-architecture.md`
- **Servicios AWS**: 16 servicios implementados
- **Microservicios**: 5 servicios en ECS Fargate
- **Métricas**: KPIs y targets de rendimiento

## 🏗️ Servicios AWS

### Compute
- ECS Fargate (microservicios)
- Lambda (procesamiento)

### Storage  
- RDS PostgreSQL (60M productos)
- ElastiCache Redis (cache)
- S3 (documentos)

### Network
- API Gateway
- CloudFront CDN
- Application Load Balancer

### Security
- Cognito (auth)
- WAF (firewall)
- KMS (encryption)

### AI/ML
- Textract (OCR >95%)

### Integration
- EventBridge (eventos)
- SQS/SNS (mensajería)

### Monitoring
- CloudWatch (métricas)
- X-Ray (tracing)

## 📈 Métricas

- **OCR Processing**: <5s
- **Product Lookup**: <500ms (60M records)
- **Throughput**: 10K invoices/hour
- **Availability**: >99.9%
- **Cost**: $8,650/month

## 🔄 Versionado

- **v2.0.0**: Actual - MCP + generación automatizada
- **v1.0.0**: Inicial - Diagramas Mermaid básicos

## 📞 Soporte

Para modificar diagramas:
1. Editar `docs/mcp-diagrams-architecture.md`
2. Actualizar `infrastructure/diagrams/generate_complete.py`
3. Ejecutar `./scripts/generate_diagrams.sh`
