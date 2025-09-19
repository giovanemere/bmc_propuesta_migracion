# MCP Arquitectura BMC - Definición Completa

## Contexto del Sistema

### Información General
- **Sistema**: BMC (Bolsa Mercantil de Colombia) - Plataforma Regulatoria
- **Objetivo**: Migración a AWS con procesamiento de 60M productos y OCR de documentos
- **Arquitectura**: Event-Driven Microservices con AI/ML Integration
- **Compliance**: DIAN (Dirección de Impuestos y Aduanas Nacionales)

### Métricas Clave
- **Productos**: 60 millones de registros
- **OCR Accuracy**: >95% de confianza
- **Throughput**: 10,000 facturas/hora
- **Availability**: >99.9% SLA
- **Retention**: 7 años para compliance

## Stack Tecnológico Definido

### Backend Services
```yaml
Language: Python 3.9+
Framework: FastAPI
Architecture: Event-Driven Microservices
Containerization: Docker + ECS Fargate
Orchestration: AWS Step Functions
API Documentation: OpenAPI/Swagger
Testing: pytest + coverage >90%
Database: PostgreSQL 14 (RDS Multi-AZ)
Cache: Redis (ElastiCache Cluster Mode)
Message Queue: SQS FIFO + Standard
Event Bus: Amazon EventBridge
```

### Frontend Applications
```yaml
Framework: React 18+ with TypeScript
State Management: Redux Toolkit + RTK Query
UI Library: Material-UI v5
Build Tool: Vite
Testing: Jest + React Testing Library
E2E Testing: Playwright
CDN: CloudFront with WAF
```

### AWS Services Architecture
```yaml
Compute:
  - ECS Fargate (Microservices)
  - Lambda (Event Processing)
  - Step Functions (Workflows)

Storage:
  - RDS PostgreSQL Multi-AZ (Transactional)
  - Redshift (Analytics)
  - S3 (Documents, Intelligent Tiering)
  - ElastiCache Redis (Caching)

AI/ML:
  - Amazon Textract (OCR)
  - Amazon Comprehend (NLP)

Integration:
  - API Gateway (REST/GraphQL)
  - EventBridge (Event Bus)
  - SQS (Message Queues)
  - SNS (Notifications)
  - Transfer Family (SFTP)

Security:
  - Cognito (Authentication)
  - IAM (Authorization)
  - KMS (Encryption)
  - WAF (Web Firewall)
  - Secrets Manager (Credentials)

Monitoring:
  - CloudWatch (Metrics/Logs)
  - X-Ray (Tracing)
  - CloudTrail (Audit)
```

## Microservicios Definidos

### 1. Invoice Service
```yaml
Responsabilidad: Procesamiento de facturas y documentos
Tecnología: FastAPI + Python 3.9
Recursos: 2 vCPU, 4GB RAM
Escalado: Auto Scaling 2-10 instancias
Dependencias:
  - OCR Service (Textract)
  - Product Service (Lookup)
  - Validation Service (Rules)
Endpoints:
  - POST /invoices/upload
  - GET /invoices/{id}/status
  - GET /invoices/{id}/details
```

### 2. Product Service (60M Records)
```yaml
Responsabilidad: Gestión de 60M productos y clasificación DIAN
Tecnología: FastAPI + Python 3.9
Recursos: 4 vCPU, 8GB RAM
Escalado: Auto Scaling 3-15 instancias
Cache Strategy: Redis 24h TTL
Dependencias:
  - RDS PostgreSQL (Primary)
  - ElastiCache Redis (Cache)
  - DIAN API (Classification)
Endpoints:
  - GET /products/search
  - GET /products/{code}
  - GET /products/classification/{dian_code}
```

### 3. OCR Service
```yaml
Responsabilidad: Extracción de texto con >95% precisión
Tecnología: FastAPI + Amazon Textract
Recursos: 2 vCPU, 4GB RAM
Escalado: Auto Scaling 2-8 instancias
Dependencias:
  - Amazon Textract
  - S3 (Document Storage)
  - EventBridge (Status Events)
Endpoints:
  - POST /ocr/process
  - GET /ocr/{job_id}/status
  - GET /ocr/{job_id}/results
```

### 4. Commission Service
```yaml
Responsabilidad: Cálculo de comisiones según reglas de negocio
Tecnología: FastAPI + Business Rules Engine
Recursos: 1 vCPU, 2GB RAM
Escalado: Auto Scaling 2-6 instancias
Dependencias:
  - Invoice Service (Data)
  - Certificate Service (Generation)
Endpoints:
  - POST /commissions/calculate
  - GET /commissions/{invoice_id}
  - GET /commissions/rules/current
```

### 5. Certificate Service
```yaml
Responsabilidad: Generación de certificados PDF
Tecnología: FastAPI + ReportLab
Recursos: 1 vCPU, 2GB RAM
Escalado: Auto Scaling 2-5 instancias
Dependencias:
  - S3 (Certificate Storage)
  - SES (Email Delivery)
Endpoints:
  - POST /certificates/generate
  - GET /certificates/{id}/download
  - POST /certificates/{id}/email
```

## Arquitectura de Datos

### Transactional Layer (RDS PostgreSQL)
```sql
-- Schema principal
CREATE SCHEMA bmc_transactional;

-- Tabla de productos (60M registros)
CREATE TABLE bmc_transactional.products (
    product_id BIGSERIAL PRIMARY KEY,
    product_code VARCHAR(50) UNIQUE NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    dian_classification VARCHAR(20) NOT NULL,
    category_id INTEGER NOT NULL,
    unit_type VARCHAR(20) NOT NULL,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices optimizados para 60M registros
CREATE INDEX CONCURRENTLY idx_products_code ON bmc_transactional.products(product_code);
CREATE INDEX CONCURRENTLY idx_products_dian ON bmc_transactional.products(dian_classification);
CREATE INDEX CONCURRENTLY idx_products_active ON bmc_transactional.products(is_active) WHERE is_active = true;

-- Tabla de facturas (particionada por mes)
CREATE TABLE bmc_transactional.invoices (
    invoice_id BIGSERIAL PRIMARY KEY,
    invoice_number VARCHAR(100) NOT NULL,
    invoice_date DATE NOT NULL,
    document_type VARCHAR(20) NOT NULL,
    document_path VARCHAR(500),
    ocr_confidence DECIMAL(5,2),
    processing_status VARCHAR(20) DEFAULT 'PENDING',
    total_amount DECIMAL(15,4),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) PARTITION BY RANGE (invoice_date);

-- Particiones mensuales (últimos 24 meses + próximos 12)
CREATE TABLE bmc_transactional.invoices_2024_01 PARTITION OF bmc_transactional.invoices
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');
```

### Caching Strategy (ElastiCache Redis)
```yaml
Product Cache:
  Pattern: "product:{product_code}"
  TTL: 24 hours
  Size: ~2GB for metadata
  Eviction: LRU

DIAN Classification Cache:
  Pattern: "dian:{classification_code}"
  TTL: 7 days
  Size: ~100MB
  Eviction: LRU

Session Cache:
  Pattern: "session:{user_id}"
  TTL: 30 minutes
  Size: ~10MB total
  Eviction: TTL-based
```

### Analytics Layer (Redshift)
```sql
-- Data Warehouse Schema
CREATE SCHEMA bmc_analytics;

-- Fact table para comisiones
CREATE TABLE bmc_analytics.fact_commissions (
    commission_key BIGINT IDENTITY(1,1) PRIMARY KEY,
    invoice_key BIGINT NOT NULL,
    product_key BIGINT NOT NULL,
    date_key INTEGER NOT NULL,
    commission_amount DECIMAL(15,4) NOT NULL,
    commission_rate DECIMAL(8,6) NOT NULL,
    quantity DECIMAL(15,4) NOT NULL,
    total_invoice_amount DECIMAL(15,4) NOT NULL
) DISTKEY(date_key) SORTKEY(date_key);
```

## Event-Driven Architecture

### EventBridge Rules
```yaml
invoice.uploaded:
  Source: "bmc.invoice.service"
  DetailType: "Invoice Uploaded"
  Targets:
    - OCR Service (Start Processing)
    - Notification Service (User Alert)

invoice.ocr.completed:
  Source: "bmc.ocr.service"
  DetailType: "OCR Processing Complete"
  Targets:
    - Invoice Service (Continue Processing)
    - Product Service (Match Products)

invoice.validated:
  Source: "bmc.invoice.service"
  DetailType: "Invoice Validated"
  Targets:
    - Commission Service (Calculate)
    - Analytics Service (Update Metrics)

commission.calculated:
  Source: "bmc.commission.service"
  DetailType: "Commission Calculated"
  Targets:
    - Certificate Service (Generate PDF)
    - Notification Service (Email User)
```

### SQS Queue Configuration
```yaml
invoice-processing-queue:
  Type: FIFO
  VisibilityTimeout: 300 seconds
  MessageRetentionPeriod: 14 days
  DeadLetterQueue: invoice-dlq
  MaxReceiveCount: 3

ocr-processing-queue:
  Type: Standard
  VisibilityTimeout: 900 seconds
  MessageRetentionPeriod: 14 days
  DeadLetterQueue: ocr-dlq
  MaxReceiveCount: 3

notification-queue:
  Type: Standard
  VisibilityTimeout: 60 seconds
  MessageRetentionPeriod: 7 days
  DeadLetterQueue: notification-dlq
  MaxReceiveCount: 5
```

## Integraciones Externas

### DIAN API Integration
```yaml
Base URL: https://api.dian.gov.co/v1
Authentication: OAuth 2.0 Client Credentials
Rate Limit: 1000 requests/hour
Timeout: 30 seconds
Retry Strategy: Exponential backoff (3 attempts)

Endpoints:
  - GET /classification/validate/{code}
  - GET /products/lookup
  - POST /compliance/validate

Error Handling:
  - Circuit Breaker Pattern
  - Fallback to cached data
  - Manual review queue for failures
```

### SFTP Integration (AWS Transfer Family)
```yaml
Protocol: SFTP
Identity Provider: Service Managed
Endpoint Type: VPC
Home Directory: S3 Bucket

Directory Structure:
  /incoming/
    - daily-reports/
    - regulatory-filings/
  /outgoing/
    - commission-reports/
    - compliance-documents/
  /archive/
    - processed-files/

Automation:
  - Lambda trigger on file upload
  - Automatic file validation
  - Processing status notifications
  - Archive after 30 days
```

## Seguridad y Compliance

### Encryption Strategy
```yaml
Data at Rest:
  - RDS: TDE with customer-managed KMS keys
  - S3: AES-256 with KMS encryption
  - EBS: Encrypted volumes
  - Redshift: AES-256 encryption

Data in Transit:
  - TLS 1.3 for all API communications
  - VPC Endpoints for AWS service communication
  - Certificate pinning for mobile apps

Key Management:
  - Customer-managed KMS keys
  - Automatic key rotation (annual)
  - Separate keys per environment
  - Cross-region key replication for DR
```

### Access Control
```yaml
IAM Roles:
  - BMC-InvoiceService-Role
  - BMC-ProductService-Role
  - BMC-OCRService-Role
  - BMC-CommissionService-Role
  - BMC-CertificateService-Role

User Roles:
  - BMC-Admin (full access)
  - BMC-Operator (read/write invoices)
  - BMC-Viewer (read-only reports)
  - BMC-External (SFTP access only)

Policies:
  - Least privilege principle
  - Resource-based permissions
  - Time-based access (business hours)
  - IP restriction for admin access
  - MFA required for admin operations
```

## Monitoring y Observabilidad

### Metrics & KPIs
```yaml
Business Metrics:
  - OCR Accuracy Rate (>95%)
  - Invoice Processing Time (<3 seconds)
  - Product Lookup Time (<500ms)
  - System Availability (>99.9%)
  - Commission Calculation Accuracy (100%)

Technical Metrics:
  - API Response Time (p95 < 1s)
  - Error Rate (<0.1%)
  - Database Connection Pool Usage
  - Cache Hit Rate (>80%)
  - Queue Depth and Processing Rate

Infrastructure Metrics:
  - CPU Utilization (<70%)
  - Memory Utilization (<80%)
  - Network I/O
  - Disk I/O and Storage Usage
  - Auto Scaling Events
```

### Alerting Strategy
```yaml
Critical Alerts (PagerDuty):
  - System Down (>5 minutes)
  - OCR Accuracy Drop (<90%)
  - Database Connection Failures
  - Security Incidents

Warning Alerts (Email/Slack):
  - High Error Rate (>1%)
  - Performance Degradation
  - Queue Backlog
  - Resource Utilization (>80%)

Info Alerts (Dashboard):
  - Deployment Notifications
  - Scaling Events
  - Backup Completion
  - Maintenance Windows
```

## Disaster Recovery

### RTO/RPO Objectives
```yaml
Recovery Time Objective (RTO): 4 hours
Recovery Point Objective (RPO): 1 hour

Backup Strategy:
  - RDS: Automated backups (35 days)
  - S3: Cross-region replication
  - Redshift: Daily snapshots
  - Application Data: AWS Backup

DR Region: us-west-2 (Oregon)
Failover: Automated via Route 53 health checks
Testing: Quarterly DR drills
```

### Runbook Automation
```yaml
Automated Procedures:
  - Database failover
  - Application deployment to DR region
  - DNS failover
  - Certificate renewal
  - Scaling adjustments

Manual Procedures:
  - Incident response coordination
  - Stakeholder communication
  - Post-incident review
  - Compliance reporting
```

## Cronograma de Implementación

### Fase 1: Fundación (Semanas 1-8)
- AWS environment setup
- VPC, subnets, security groups
- RDS PostgreSQL setup y migración de 60M productos
- ElastiCache Redis cluster
- Basic monitoring setup

### Fase 2: Core Services (Semanas 9-16)
- Product Service implementation
- Invoice Service development
- OCR Service con Textract integration
- API Gateway setup
- EventBridge configuration

### Fase 3: Business Logic (Semanas 17-22)
- Commission Service
- Certificate Service
- Business rules engine
- Step Functions workflows
- DIAN API integration

### Fase 4: Frontend & Integration (Semanas 23-26)
- React frontend migration
- Mobile app updates
- SFTP Gateway setup
- Email service integration
- End-to-end testing

### Fase 5: Go-Live (Semanas 27-30)
- Performance optimization
- Security hardening
- Compliance validation
- Production deployment
- Post-launch monitoring

## Costos Estimados (Mensual)

### Compute
- ECS Fargate: $2,500
- Lambda: $300
- API Gateway: $200

### Storage
- RDS PostgreSQL: $1,800
- ElastiCache Redis: $600
- S3: $400
- Redshift: $1,200

### AI/ML Services
- Textract: $800
- Comprehend: $200

### Networking & Security
- CloudFront: $150
- WAF: $100
- Transfer Family: $300

### Total Estimado: ~$8,650/mes

## Métricas de Éxito

### Performance KPIs
- OCR Processing: <5 segundos (imágenes), <3 segundos (PDFs)
- Product Lookup: <500ms (60M records)
- Invoice Processing: <3 segundos (individual)
- System Availability: >99.9%

### Business KPIs
- OCR Accuracy: >95%
- Processing Throughput: 10,000 invoices/hour
- Compliance Rate: 100% DIAN validation
- User Satisfaction: >4.5/5.0
- Cost Reduction: 30% vs current infrastructure
